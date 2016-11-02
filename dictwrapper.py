# coding=UTF-8

class DictWrapper(dict):

    def __getattr__(self, name):
        try:
            return super(DictWrapper, self).__getitem__(name)
        except KeyError:
            raise AttributeError("key %s not found" % name)

    def __setattr__(self, name, value):
        super(DictWrapper, self).__setitem__(name, value)

    def __delattr__(self, name):
        super(DictWrapper, self).__delitem__(name)

    def hasattr(self, name):
        return name in self

    @classmethod
    def load_dict(cls, org_data):
        """支持将嵌套的dict转成wrapper, e.g.:
        test_dict = {'a':{'b':1,'c':[2,{'e':3}],'f':{'g':4}}}
        ss = DictWrapper.load_dict(test_dict)
        print ss.a.c[1].e
        print ss.a.b
        """
        if isinstance(org_data, dict):
            dr = {}
            for k, v in org_data.items():
                dr.update({k: cls.load_dict(v)})
            return cls(dr)
        elif isinstance(org_data, (list, tuple)):
            return [cls.load_dict(i) for i in org_data]
        else:
            return org_data