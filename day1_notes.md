# Day 1 学习记录

## 今天做了什么
- 创建了 learning-notes 仓库
- 安装了 Git，并解决了 VS Code 中找不到 Git: Clone 的问题
- 配置了 Clash 代理（端口 7897），解决了 Git 无法连接 GitHub 的问题
- 成功克隆仓库到本地
- 编写并多次优化了 day1_hello.py
- 完成了从“写死数据”到“支持用户输入名字和数字”的改动

## 学到的点
- `if __name__ == "__main__":` 的作用：只有直接运行这个文件时才会执行下面的代码
- 函数的定义与调用：
  - `def 函数名(参数: 类型) -> 返回类型:`
  - 调用时把值传进去，用返回值
- 类型注解（`name: str`、`-> str`）的基本写法
- f-string 的使用：`f"你好，{name}！"`
- `input()` 获取用户输入，并用 `int()` 转换成整数
- 如何给 Git 配置代理：
  ```bash
  git config --global http.proxy http://127.0.0.1:7897
  git config --global https.proxy http://127.0.0.1:7897