from Comment.search import *
from Comment.add import *
from Comment.remove import *
from Comment.update import *
from base import BasePage, ExitHandler, ReturnHandler

PAGE_MAIN = '''
欢迎来到公司管理系统
-----------------------
1.查询员工信息
2.增加新员工信息
3.更新员工信息
4.删除员工信息
5.退出
-----------------------
'''
PAGE_SEARCH = '''
1.直接领导为ENAME的员工编号
2.参与项目所在地为PLOCATION的部门名称
3.参与PNAME项目的所有工作人员的名字和居住地址
4.部门领导居住地在ADDRESS且工资不低于SALARY元的员工姓名和居住地
5.没有参与项目编号为PNO项目的员工姓名
6.部门领导工作日期在MGRSTARTDATE之后的部门名称
7.总工作量大于HOURS的项目名称
8.员工平均工作时间低于HOURS的项目名称
9.至少参与了N个项目且工作时间超过HOURS小时的员工名字
10.返回
11.退出
'''


class PageMain(BasePage):
    def __init__(self):
        super().__init__()
        self.content = PAGE_MAIN
        self.next = {1: SearchPage, 2: AddPage, 3: UpdatePage, 4: RemovePage, 5: ExitHandler}


class SearchPage(BasePage):
    def __init__(self):
        super().__init__()
        self.content = PAGE_SEARCH
        self.next = {
            1: SrchComment1,
            2: SrchComment2,
            3: SrchComment3,
            4: SrchComment4,
            5: SrchComment5,
            6: SrchComment6,
            7: SrchComment7,
            8: SrchComment8,
            9: SrchComment9,
            10: ReturnHandler,
            11: ExitHandler
        }


class AddPage(BasePage):
    def __init__(self):
        super().__init__()
        self.content = ""
        self.next = {}

    def __call__(self, *args, **kwargs):
        AddComment()()


class UpdatePage(BasePage):
    def __init__(self):
        super().__init__()
        self.content = ""
        self.next = {}

    def __call__(self, *args, **kwargs):
        UpdateComment()()


class RemovePage(BasePage):
    def __init__(self):
        super().__init__()
        self.content = ""
        self.next = {}

    def __call__(self, *args, **kwargs):
        RemoveComment()()
