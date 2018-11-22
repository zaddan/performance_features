# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_event_group')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_event_group')
    _event_group = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_event_group', [dirname(__file__)])
        except ImportError:
            import _event_group
            return _event_group
        try:
            _mod = imp.load_module('_event_group', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _event_group = swig_import_helper()
    del swig_import_helper
else:
    import _event_group
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _event_group.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _event_group.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _event_group.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _event_group.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _event_group.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _event_group.SwigPyIterator_equal(self, x)

    def copy(self):
        return _event_group.SwigPyIterator_copy(self)

    def next(self):
        return _event_group.SwigPyIterator_next(self)

    def __next__(self):
        return _event_group.SwigPyIterator___next__(self)

    def previous(self):
        return _event_group.SwigPyIterator_previous(self)

    def advance(self, n):
        return _event_group.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _event_group.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _event_group.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _event_group.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _event_group.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _event_group.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _event_group.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _event_group.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class event_group(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, event_group, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, event_group, name)
    __repr__ = _swig_repr
    time = _event_group.event_group_time
    interruption = _event_group.event_group_interruption
    wait = _event_group.event_group_wait
    __swig_setmethods__["event_group_fd_instance"] = _event_group.event_group_event_group_fd_instance_set
    __swig_getmethods__["event_group_fd_instance"] = _event_group.event_group_event_group_fd_instance_get
    if _newclass:
        event_group_fd_instance = _swig_property(_event_group.event_group_event_group_fd_instance_get, _event_group.event_group_event_group_fd_instance_set)
    __swig_setmethods__["s_method"] = _event_group.event_group_s_method_set
    __swig_getmethods__["s_method"] = _event_group.event_group_s_method_get
    if _newclass:
        s_method = _swig_property(_event_group.event_group_s_method_get, _event_group.event_group_s_method_set)

    def __init__(self, *args):
        this = _event_group.new_event_group(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _event_group.delete_event_group
    __del__ = lambda self: None

    def add_event(self, type_id, config):
        return _event_group.event_group_add_event(self, type_id, config)

    def enable(self):
        return _event_group.event_group_enable(self)

    def disable(self):
        return _event_group.event_group_disable(self)

    def reset(self):
        return _event_group.event_group_reset(self)

    def sample(self, reset=True):
        return _event_group.event_group_sample(self, reset)

    def delete_samples(self):
        return _event_group.event_group_delete_samples(self)

    def wait_event(self):
        return _event_group.event_group_wait_event(self)

    def to_csv(self, columns):
        return _event_group.event_group_to_csv(self, columns)
event_group_swigregister = _event_group.event_group_swigregister
event_group_swigregister(event_group)
cvar = _event_group.cvar

class myEvent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, myEvent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, myEvent, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _event_group.myEvent_name_set
    __swig_getmethods__["name"] = _event_group.myEvent_name_get
    if _newclass:
        name = _swig_property(_event_group.myEvent_name_get, _event_group.myEvent_name_set)
    __swig_setmethods__["type"] = _event_group.myEvent_type_set
    __swig_getmethods__["type"] = _event_group.myEvent_type_get
    if _newclass:
        type = _swig_property(_event_group.myEvent_type_get, _event_group.myEvent_type_set)
    __swig_setmethods__["config"] = _event_group.myEvent_config_set
    __swig_getmethods__["config"] = _event_group.myEvent_config_get
    if _newclass:
        config = _swig_property(_event_group.myEvent_config_get, _event_group.myEvent_config_set)

    def __init__(self):
        this = _event_group.new_myEvent()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _event_group.delete_myEvent
    __del__ = lambda self: None
myEvent_swigregister = _event_group.myEvent_swigregister
myEvent_swigregister(myEvent)

class list_events(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, list_events, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, list_events, name)
    __repr__ = _swig_repr

    def __init__(self, verbose=0):
        this = _event_group.new_list_events(verbose)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def show_event(self, info):
        return _event_group.list_events_show_event(self, info)

    def list_pmu_events(self, pmu):
        return _event_group.list_events_list_pmu_events(self, pmu)

    def collect_supported_events(self, *args):
        return _event_group.list_events_collect_supported_events(self, *args)

    def list_all_pmus(self):
        return _event_group.list_events_list_all_pmus(self)

    def generate_header(self):
        return _event_group.list_events_generate_header(self)

    def get_evs(self):
        return _event_group.list_events_get_evs(self)
    __swig_destroy__ = _event_group.delete_list_events
    __del__ = lambda self: None
list_events_swigregister = _event_group.list_events_swigregister
list_events_swigregister(list_events)

class stringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, stringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, stringVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _event_group.stringVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _event_group.stringVector___nonzero__(self)

    def __bool__(self):
        return _event_group.stringVector___bool__(self)

    def __len__(self):
        return _event_group.stringVector___len__(self)

    def __getslice__(self, i, j):
        return _event_group.stringVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _event_group.stringVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _event_group.stringVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _event_group.stringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _event_group.stringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _event_group.stringVector___setitem__(self, *args)

    def pop(self):
        return _event_group.stringVector_pop(self)

    def append(self, x):
        return _event_group.stringVector_append(self, x)

    def empty(self):
        return _event_group.stringVector_empty(self)

    def size(self):
        return _event_group.stringVector_size(self)

    def swap(self, v):
        return _event_group.stringVector_swap(self, v)

    def begin(self):
        return _event_group.stringVector_begin(self)

    def end(self):
        return _event_group.stringVector_end(self)

    def rbegin(self):
        return _event_group.stringVector_rbegin(self)

    def rend(self):
        return _event_group.stringVector_rend(self)

    def clear(self):
        return _event_group.stringVector_clear(self)

    def get_allocator(self):
        return _event_group.stringVector_get_allocator(self)

    def pop_back(self):
        return _event_group.stringVector_pop_back(self)

    def erase(self, *args):
        return _event_group.stringVector_erase(self, *args)

    def __init__(self, *args):
        this = _event_group.new_stringVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _event_group.stringVector_push_back(self, x)

    def front(self):
        return _event_group.stringVector_front(self)

    def back(self):
        return _event_group.stringVector_back(self)

    def assign(self, n, x):
        return _event_group.stringVector_assign(self, n, x)

    def resize(self, *args):
        return _event_group.stringVector_resize(self, *args)

    def insert(self, *args):
        return _event_group.stringVector_insert(self, *args)

    def reserve(self, n):
        return _event_group.stringVector_reserve(self, n)

    def capacity(self):
        return _event_group.stringVector_capacity(self)
    __swig_destroy__ = _event_group.delete_stringVector
    __del__ = lambda self: None
stringVector_swigregister = _event_group.stringVector_swigregister
stringVector_swigregister(stringVector)

class eventList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eventList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eventList, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _event_group.eventList_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _event_group.eventList___nonzero__(self)

    def __bool__(self):
        return _event_group.eventList___bool__(self)

    def __len__(self):
        return _event_group.eventList___len__(self)

    def __getslice__(self, i, j):
        return _event_group.eventList___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _event_group.eventList___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _event_group.eventList___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _event_group.eventList___delitem__(self, *args)

    def __getitem__(self, *args):
        return _event_group.eventList___getitem__(self, *args)

    def __setitem__(self, *args):
        return _event_group.eventList___setitem__(self, *args)

    def pop(self):
        return _event_group.eventList_pop(self)

    def append(self, x):
        return _event_group.eventList_append(self, x)

    def empty(self):
        return _event_group.eventList_empty(self)

    def size(self):
        return _event_group.eventList_size(self)

    def swap(self, v):
        return _event_group.eventList_swap(self, v)

    def begin(self):
        return _event_group.eventList_begin(self)

    def end(self):
        return _event_group.eventList_end(self)

    def rbegin(self):
        return _event_group.eventList_rbegin(self)

    def rend(self):
        return _event_group.eventList_rend(self)

    def clear(self):
        return _event_group.eventList_clear(self)

    def get_allocator(self):
        return _event_group.eventList_get_allocator(self)

    def pop_back(self):
        return _event_group.eventList_pop_back(self)

    def erase(self, *args):
        return _event_group.eventList_erase(self, *args)

    def __init__(self, *args):
        this = _event_group.new_eventList(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _event_group.eventList_push_back(self, x)

    def front(self):
        return _event_group.eventList_front(self)

    def back(self):
        return _event_group.eventList_back(self)

    def assign(self, n, x):
        return _event_group.eventList_assign(self, n, x)

    def resize(self, *args):
        return _event_group.eventList_resize(self, *args)

    def insert(self, *args):
        return _event_group.eventList_insert(self, *args)

    def reserve(self, n):
        return _event_group.eventList_reserve(self, n)

    def capacity(self):
        return _event_group.eventList_capacity(self)
    __swig_destroy__ = _event_group.delete_eventList
    __del__ = lambda self: None
eventList_swigregister = _event_group.eventList_swigregister
eventList_swigregister(eventList)

# This file is compatible with both classic and new-style classes.


