from base import BaseComment
from tools import *


class SrchComment1(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "请输入领导姓名ENAME:"
    # todo:完善以下函数（下同）：
    # def __call__(self, *args, **kwargs):


class SrchComment2(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "请输入项目所在地PLOCATION:"


class SrchComment3(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "请输入项目名称PNAME:"


class SrchComment4(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "请输入居住地ADDRESS和工资SALARY（空格隔开，如：广东 1999）:"


class SrchComment5(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "请输入项目编号PNO:"


class SrchComment6(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "请输入领导工作日期MGRSTARTDATE:"


class SrchComment7(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "请输入总工作量HOURS:"


class SrchComment8(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "请输入指定工作时间HOURS:"


class SrchComment9(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "请输入项目N和制定工作时间HOURS（空格隔开，如：101 19）:"
