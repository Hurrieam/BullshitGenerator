from src.statements import *
from src.OldSayings import *
from src.SubSomething import *
from src.PreSomething import *

from random import *


def generator():
    theme = input("请键入文章主题，以回车键结束。\n>>")

    passage = []

    while len(passage) <= 2000:  # 文章句子少于2000句时一直生成
        randnum = randint(1, 4)
        if randnum == 1:  # 生成一句论述
            passage.append(statements[randint(0, len(statements) - 1)])
        if randnum == 2:  # 生成一句名人名言
            passage.append(OldSayings[randint(0, len(OldSayings) - 1)])
        if randnum == 3:  # 生成一句前垫话
            passage.append(PreSomething[randint(0, len(PreSomething) - 1)])
        if randnum == 4:  # 生成一句后垫话
            passage.append(SubSomething[randint(0, len(SubSomething) - 1)])

    passage_string = "    "
    for sentence in range(0, len(passage), 1):
        passage_string = passage_string + passage[sentence]
        if randint(1, 10) >= 8:
            passage_string = passage_string + "\n    "

    passage_string = passage_string.replace("主题", theme)
    print(passage_string)
