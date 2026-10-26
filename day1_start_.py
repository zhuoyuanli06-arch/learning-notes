# day1_hello.py
# 第一天练习：重新熟悉 Python 基础

def greet(name: str) -> str:
    """简单的问候函数"""
    return f"你好，{name}！欢迎回到编程的世界。"

def calculate_sum(a: int, b: int) -> int:
    """计算两个数的和"""
    return a + b

if __name__ == "__main__":
    name = input("请输入你的名字：")
    print(greet(name))
    a = int(input("请输入第一个整数："))
    b = int(input("请输入第二个整数："))
    print(f"{a} + {b} = {calculate_sum(a, b)}")
    print("今天完成了第一次代码提交！")