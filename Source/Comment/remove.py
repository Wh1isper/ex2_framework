from base import BaseComment
from tools import *


class RemoveComment(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "请输入删除员工的员工号ESSN:"
    # todo:完善以下函数：
    # def __call__(self, *args, **kwargs):
