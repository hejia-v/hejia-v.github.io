# -*- coding:utf-8 -*-
import os
import re


def get_file_list(dirname):
    files = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        path = os.path.normpath(path)
        if not os.path.isfile(path):
            continue
        files.append(path)
    return files


def replace_md_image_ref(file):
    with open(file, 'r', encoding='utf8') as fd:
        text = fd.read()

    patt = re.compile('!\[[\s\S]+?\]\(/images/[\s\S]+?\)')

    qnurl = 'http://ozy76jm8o.bkt.clouddn.com/blog'
    def f(m):
        s = m.group()
        return s.replace('(/images/', '(%s/images/' % qnurl)
    text = patt.sub(f, text)
    # print(text)
    with open(file, 'w', encoding='utf8') as fd:
        fd.write(text)


def main():
    curdir = os.path.dirname(os.path.abspath(__file__))
    dirname = os.path.normpath(os.path.join(curdir, '../source/_posts'))
    files = get_file_list(dirname)
    # print(files)
    for filename in files:
        replace_md_image_ref(filename)

if __name__ == '__main__':
    main()

