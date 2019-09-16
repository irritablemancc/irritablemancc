#!/usr/bin/env python

import os

import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line, define, options

define("host", default='localhost', help="主机地址", type=str)
define("port", default=8000, help="主机端口", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print('添加了一个打印')
        abc = self.get_argument('arg', '哈哈哈哈哈哈哈哈')
        name = self.get_argument('name', 'Admin')
        sex = self.get_argument('sex', '保密')
        menu = ['红烧肉', '水果沙拉', '糖醋排骨', '牛排', '波士顿龙虾', '三文鱼刺身']
        self.render('index.html', xyz=abc, name=name, sex=sex, menu=menu)


class BlockHandler(tornado.web.RequestHandler):
    def get(self):
        print('添加了两个打印')
        title = '草'
        content = '''
            s十年生死两茫茫，不思量自难忘，千里孤坟，无处话凄凉，纵使相逢应不识，尘满面，鬓如霜。夜来幽梦忽还乡，小轩窗，正梳妆，相顾无言，惟有泪千行。料得年年断肠处，明月夜短松冈。
    。散的宴席，书上还说，人生何处不相逢。
        '''
        self.render('article.html', title=title, content=content)


class StaticTestHandle(tornado.web.RequestHandler):
    def get(self):
        self.render('static_test.html')


def make_app():
    routes = [
        (r"/", MainHandler),
        (r"/block", BlockHandler),
        (r"/tttt", StaticTestHandle)
    ]

    # 获取模版目录和静态文件目录的绝对路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'jingtai')

    return tornado.web.Application(routes,
                                   template_path=template_dir,
                                   static_path=static_dir)


if __name__ == "__main__":
    parse_command_line()

    app = make_app()
    print('server running on %s:%s' % (options.host, options.port))
    app.listen(options.port, options.host)

    loop = tornado.ioloop.IOLoop.current()
    loop.start()
