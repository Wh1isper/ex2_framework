'''
Comment作为最小查询语句单元，应该是用户最后一个选择
Page作为选项卡，应该有下一项选择直至Comment为止
'''
class BaseComment:
    def __init__(self):
        '''
        content:指引用户输入必要的查询信息
        todo:
            实现Comment/文件夹下所有文件的__call__函数，否则会收到Not Implemented
            可以使用tools.py提供的quary，你只需构造查询语句并解析返回
        '''
        self.content = None

    def __str__(self):
        if self.content:
            return self.content
        else:
            raise NotImplementedError("Comment no content.")

    def __call__(self, *args, **kwargs):
        raise NotImplementedError()

class BasePage:
    def __init__(self):
        '''
        content:当前页面内容
        next:下一页面对象
        count:错选计数器，超过一定次数会重新显示content
        '''
        self.content = None
        self.next = None
        self.count = 0

    def __str__(self):
        if self.content:
            return self.content
        else:
            raise NotImplementedError("Page no content.")

    def __call__(self, *args, **kwargs):
        # 默认行为，引导用户输入选项并跳转至下一page/comment
        if self.next is None:
            raise NotImplementedError("No Next Page or Comment")
        while True:
            if self.count % 5 == 0:
                print(self)
            choice = input("请输入:")
            try:
                next_act = self.next[int(choice)]()
                if type(next_act) is ReturnHandler:
                    return
                else:
                    if not callable(next_act):
                        raise Exception("{} is not callable".format(type(next_act)))
                    next_act()
                self.count = 0
            except KeyError:
                print("选项错误，请重新输入")
                self.count += 1


class ExitHandler:
    '''
    留作退出处理
    '''
    def __call__(self, *args, **kwargs):
        exit(0)


class ReturnHandler:
    '''
    留作返回处理
    '''
    def __call__(self, *args, **kwargs):
        return
