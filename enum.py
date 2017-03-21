# coding=utf-8


class EnumType(object):

    def __init__(self, value, desc):
        self.value = value
        self.desc = desc


class MetaEnum(type):

    def __new__(cls, name, bases, attrs):
        if name != 'MetaEnum':
            enum_choices = []
            enum_desc_dict = {}
            enum_value_dict = {}
            for k, v in attrs.items():
                if isinstance(v, EnumType):
                    enum_choices.append((v.value, v.desc))
                    enum_desc_dict.update({v.value: v.desc})
                    enum_value_dict.update({k: v.value})
            attrs.update({
                'choices': tuple(enum_choices),
                'desc_dict': enum_desc_dict
            })
            attrs.update(enum_value_dict)
        new_cls = super(MetaEnum, cls).__new__(cls, name, bases, attrs)
        return new_cls


class BaseEnum(object):
    __metaclass__ = MetaEnum
    # def __new__(cls, name, bases, attrs):
    #     if name != 'MetaEnum':
    #         enum_choices = []
    #         enum_desc_dict = {}
    #         enum_value_dict = {}
    #         for k, v in attrs.items():
    #             if isinstance(v, EnumType):
    #                 enum_choices.append((v.value, v.desc))
    #                 enum_desc_dict.update({v.value: v.desc})
    #                 enum_value_dict.update({k: v.value})
    #         attrs.update({
    #             'choices': tuple(enum_choices),
    #             'desc_dict': enum_desc_dict
    #         })
    #         attrs.update(enum_value_dict)
    #     new_cls = super(BaseEnum, cls).__new__(cls, name, bases, attrs)
    #     return new_cls

    choices = ()  # 字段choices
    desc_dict = {}  # 描述字段

    @classmethod
    def display(cls, value):
        return cls.desc_dict.get(value, value)






if __name__ == '__main__':
    class GenderEnum(BaseEnum):
        male = EnumType(1, u'男')
        female = EnumType(0, u'女')
        unknown = EnumType(-1, u'未知')


    print GenderEnum.male
    print GenderEnum.choices
    print GenderEnum.display(0)

