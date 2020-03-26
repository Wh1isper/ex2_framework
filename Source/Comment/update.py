from base import BaseComment
from tools import *


class UpdateComment(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "输入拟更新员工的员工号ESSN"
    # todo:完善以下函数：
    # def __call__(self, *args, **kwargs):