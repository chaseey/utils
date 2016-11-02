# coding=utf-8

from utils.enum import EnumType, BaseEnum

class GenderEnum(BaseEnum):

    male=EnumType(1, u'男')
    female=EnumType(0, u'女')
    unknown=EnumType(-1, u'未知')

if __name__ == '__main__':
    print GenderEnum.male
    print GenderEnum.choices
    print GenderEnum.display(0)