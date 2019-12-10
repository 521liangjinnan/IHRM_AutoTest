def read_txt(filename):
    with open("./data/" + filename, "r", encoding="utf-8")as f:
        arr = []
        for data in f.readlines():
            arr.append(tuple(data.strip().split(",")))
        return arr[1::]


if __name__ == '__main__':
    print(read_txt("employee_post.txt"))
    print("--" * 60)

"""
        strip: 去除字符串前后空格、换行符
        split("字符"): 以指定字符分隔字符串，并 以列表的形式返回
"""
