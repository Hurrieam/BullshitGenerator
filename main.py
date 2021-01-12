from src.generator import *

if __name__ == "__main__":
    print("*****狗屁不通文章生成器*****")
    print("****Python版 快速的飓风****")
    while True:
        generator()
        a = input("\n生成完毕，支持拷贝粘贴。继续使用请按回车；若不继续使用请输入全小写“quit”并以回车键结束。\n>>")
        if a == "quit":
            exit(0)
