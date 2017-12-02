# -*- coding:utf-8 -*-
import re
import os


def match_pair(content, head, tail, pos=0, direction="l"):  # pos为匹配的开始位置
    ''' 匹配成对的模式，例如括号，if,endif等 '''
    # 有一个问题，如在"{}{};"中匹配("{","};")前面的会对后面产生影响，导致匹配不成功
    #-------------------------------------------------------------------------
    iLeftCnt, iRightCnt, iLeft, iRight, iHeadLen, iTailLen = 0, 0, 0, 0, len(
        head), len(tail)
    content = content[pos:]
    i, contentLen = 0, len(content)
    while i < contentLen:  # 考虑这种特殊配对(if, ifend)(ifend, if), 待优化
        sHeadTry = content[i:i + iHeadLen]
        sTailTry = content[i:i + iTailLen]
        if iLeftCnt == 0:
            if sHeadTry == head:
                iLeftCnt += 1
                iLeft = i
                i += iHeadLen
            else:
                i += 1
        else:
            if sHeadTry == head and sTailTry == tail:
                if iHeadLen >= iTailLen:
                    iLeftCnt += 1
                    i += iHeadLen
                else:
                    iRightCnt += 1
                    i += iTailLen
            elif sHeadTry == head and sTailTry != tail:
                iLeftCnt += 1
                i += iHeadLen
            elif sHeadTry != head and sTailTry == tail:
                iRightCnt += 1
                i += iTailLen
            else:
                i += 1
        if iLeftCnt == iRightCnt and iLeftCnt != 0:
            iRight = i
            return content[:iLeft], content[iLeft:iRight], content[iRight:]
    return content, "", ""  # 找不到匹配的返回值，content已被裁剪了


class Line(object):
    def __init__(self, line):
        line = line.strip()
        if line.startswith('|'):
            line = line[1:]
        if line.endswith('|'):
            line = line[:-1]
        self.rows = [r.strip() for r in line.split('|')]

    def __repr__(self):
        return f'[{self.rows}]'

    def serial(self):
        line = ' | '.join(self.rows)
        return f'| {line} |'

    def get_link_text(self, link):
        r = match_pair(link, '[', ']')
        text = r[1][1:-1]
        return text


def update_func_useage1(lines, new_data_path):
    with open(new_data_path, 'rt', encoding='utf8') as fd:
        new_data = [l.strip() for l in fd.readlines() if l.strip()]
    while new_data:
        e = new_data.pop(0)
        for line in lines:
            link_text = line.get_link_text(line.rows[0]).strip()
            if link_text and e.lower().startswith(f'{link_text.lower()}('):
                line.rows[1] = e
                break
        # print(e)
    pass


def update_func_useage2(lines, new_data_path):
    with open(new_data_path, 'rt', encoding='utf8') as fd:
        new_data = [l.strip() for l in fd.readlines() if l.strip()]
    while new_data:
        e = new_data.pop(0)
        e = [x.strip() for x in e.split('|')]
        e_func, e_desc = e
        for line in lines:
            link_text = line.get_link_text(line.rows[0]).strip()
            if link_text and f'{link_text.lower()}('.startswith((e_func + '(').lower()):
                line.rows[2] = e_desc
                break
        # print(e)
    pass


def run():
    basepath = os.path.abspath(os.path.dirname(__file__))
    with open(f'{basepath}/data.md', 'rt', encoding='utf8') as fd:
        lines = [l.strip() for l in fd.readlines() if l.strip()]
    lines = [Line(l) for l in lines]
    print(lines[2])
    # update_func_useage1(lines, f'{basepath}/data')
    update_func_useage2(lines, f'{basepath}/data')

    output = '\n'.join([l.serial() for l in lines])
    with open(f'{basepath}/outpu.md', 'wt', encoding='utf8') as fd:
        fd.write(output)
    # print(output)
    # print(new_data)


def main():
    run()

if __name__ == '__main__':
    main()
