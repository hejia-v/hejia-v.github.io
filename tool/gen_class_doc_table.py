# -*- coding:utf-8 -*-
# desc: 根据阅读代码时做的笔记，生成类的文档表格，目前仅支持C#。笔记的格式如下：
# path/源文件路径
# class/类声明
# - 成员变量
# 变量说明
# end/
# ...
# + 成员方法
# 方法说明
# end/

import os
from jinja2 import Template

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(CUR_DIR, 'class_doc_template.html')
DOC_TEMPLATE = ''
with open(TEMPLATE_PATH, 'rt', encoding='utf8') as fd:
    DOC_TEMPLATE = fd.read()


class MemberDoc(object):
    def __init__(self, define):
        self.define = define
        self.desc = []

    def add_line(self, line):
        line = line.strip()
        self.desc.append(line)


class ClassDoc(object):
    def __init__(self):
        self.path = ''
        self.define = ''
        self.members = []
        self.methods = []
        self.is_adding_desc = False
        self.curr_member = None

    def add_line(self, line):
        line = line.strip()
        if line.startswith('path/'):
            line = line.replace('path/', '', 1)
            self.path = line
        elif line.startswith('class/'):
            line = line.replace('class/', '', 1)
            self.define = line
        elif line.startswith('-'):
            line = line.replace('-', '', 1)
            self.is_adding_desc = True
            self.curr_member = MemberDoc(line)
            self.members.append(self.curr_member)
        elif line.startswith('+'):
            line = line.replace('+', '', 1)
            self.is_adding_desc = True
            self.curr_member = MemberDoc(line)
            self.methods.append(self.curr_member)
        elif line.startswith('end/'):
            line = line.replace('end/', '', 1)
            self.is_adding_desc = False
        elif self.is_adding_desc:
            self.curr_member.add_line(line)

    def serial(self):
        template = Template(DOC_TEMPLATE)
        html = template.render(src_path=self.path,
                               use_css=True,
                               type=self.define,
                               type_name='',
                               inherit='',
                               has_field=len(self.members) > 0,
                               members=self.members,
                               has_method=len(self.methods) > 0,
                               methods=self.methods
                               )
        lines = html.split('\n')
        lines = [l.rstrip() for l in lines if l.strip()]
        html = '\n'.join(lines)
        # print(html)
        return html


def gen_doc_from_file(filename, only_first=False):
    with open(filename, 'rt', encoding='utf8') as fd:
        lines = fd.readlines()
    divider = '-' * 10
    doc_list = []
    curr_doc = None
    for line in lines:
        if line.startswith(divider):
            curr_doc = None
            if only_first:
                break
            continue
        if curr_doc is None:
            curr_doc = ClassDoc()
            doc_list.append(curr_doc)
        curr_doc.add_line(line)
    print(doc_list)
    for doc in doc_list:
        html = doc.serial()
        with open(os.path.join(CUR_DIR, 'data/data.html'), 'wt', encoding='utf8') as fd:
            fd.write(html)


def main():
    # print(DOC_TEMPLATE)
    dirname = os.path.normpath(os.path.join(CUR_DIR, '../source/_drafts'))
    filename = os.path.join(dirname, 'et-framework-client-code.txt')
    gen_doc_from_file(filename)


if __name__ == '__main__':
    main()
