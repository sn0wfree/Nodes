# coding=utf-8

class LazyProxy(object):
    def __init__(self, cls, *args, **kwargs):
        self.__dict__['_cls'] = cls
        self.__dict__['_params'] = args
        self.__dict__['_kwargs'] = kwargs
        self.__dict__['_obj'] = None
        self.__name__ = cls.__name__
        self.__doc__ = cls.__doc__

    def __getattr__(self, item):
        if self.__dict__['_obj'] is None:
            self.__init_obj()
        return getattr(self.__dict__['_obj'], item)

    def __setattr__(self, key, value):
        if self.__dict__['_obj'] is None:
            self.__init_obj()
        setattr(self.__dict__['_obj'], key, value)

    def __init_obj(self):
        self.__dict__['_obj'] = object.__new__(self.__dict__['_cls'], )
        self.__dict__['_obj'].__init__(*self.__dict__['_params'], **self.__dict__['_kwargs'])


class LazyInit(object):
    def __new__(cls, *args, **kwargs):
        return LazyProxy(cls, *args, **kwargs)
