
#include "workload.h"

#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/ptrace.h>
#include <sys/wait.h>
#include <memory.h>

#include <linux/perf_event.h>

#include <sys/mman.h>
#include <sys/sysinfo.h>
#include <sys/fcntl.h>
#include <sys/ioctl.h>

using namespace std;


char** convert(const vector<string>& v)
{
    char** args= new char*[v.size()+1];
    for(unsigned int i=0; i<v.size(); i++)
        args[i]= const_cast<char*>(v[i].c_str());
    args[v.size()]= nullptr;
    return args;
}

Workload::Workload(vector<string> args)
{
    char** p_args= convert(args);
    this->pid= create_wrokload(p_args);
    this->isAlive= 1;
}

int Workload::create_wrokload(char **argv)
{
    int pid = fork();
    if(pid < 0)
        throw "Error on fork";
    if (pid == 0)
    {
        int fd = open("out.stdout", O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);
        dup2(fd, STDOUT_FILENO);
        fd = open("out.stderr", O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);
        dup2(fd, STDERR_FILENO);
        ptrace(PTRACE_TRACEME, 0, 0, 0);
        if (execl(argv[0], (const char *)argv, NULL) < 0)
            throw "Error executing program";
    }
    return pid;
}

void Workload::wait_finish()
{
    int status;
    while(1)
    {
        waitpid(pid, &status, WNOHANG);
        if (WIFEXITED(status))
            break;
    }
    isAlive= 0;
}

void Workload::start()
{
    if(isAlive)
    {
        int status;
        waitpid(pid, &status, 0);
        ptrace(PTRACE_CONT, pid, 0, 0);
        waiter = new thread(&Workload::wait_finish, this);
    }
}

void Workload::add_events(std::vector<int> fds_)
{
    fds.insert(fds.end(), fds_.begin(), fds_.end());
}

vector<vector<signed long int>> Workload::run(bool reset, double sample_perid)
{
    vector<vector<signed long int>> samples;
    vector<signed long int> row;
    signed long int buff[MAX_SIZE_GROUP];
    ssize_t bytes_read;
    int i, status;

    samples.reserve(1000);
    row.reserve(300);

    for(i=0; i<fds.size(); i++)
    {
        ioctl(fds[i], PERF_EVENT_IOC_RESET, PERF_IOC_FLAG_GROUP);
        ioctl(fds[i], PERF_EVENT_IOC_ENABLE, PERF_IOC_FLAG_GROUP);
    }
    waitpid(pid, &status, 0);
    ptrace(PTRACE_CONT, pid, 0, 0);
    while(1)
    {
        waitpid(pid, &status, WNOHANG);
        if (WIFEXITED(status))
            break;
        
        usleep(sample_perid);
        row.clear();
        for(i=0; i<fds.size(); i++)
        {
            bytes_read= read(fds[i], buff, MAX_SIZE_GROUP*sizeof(signed long int));
            if(reset) ioctl(fds[i], PERF_EVENT_IOC_RESET, PERF_IOC_FLAG_GROUP);
            if(bytes_read <= 0)
                throw "Error on sampling ";
            
            copy(buff, buff+bytes_read/8, back_inserter(row));
        }
        samples.push_back(row);
    }
    isAlive= 0;
    row.clear();
    for(i=0; i<fds.size(); i++)
    {
        bytes_read= read(fds[i], buff, MAX_SIZE_GROUP*sizeof(signed long int));
        if(reset) ioctl(fds[i], PERF_EVENT_IOC_RESET, PERF_IOC_FLAG_GROUP);
        if(bytes_read <= 0)
            throw "Error on sampling ";
        
        copy(buff, buff+bytes_read/8, back_inserter(row));
    }
    samples.push_back(row);
    return samples;
}