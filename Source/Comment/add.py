from base import BaseComment
from tools import *


class AddComment(BaseComment):
    def __init__(self):
        super().__init__()
        self.content = "请输入员工信息:"
    # todo:完善以下函数：
    # def __call__(self, *args, **kwargs):
