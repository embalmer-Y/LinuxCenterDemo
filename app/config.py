from app.test import main


# 创建命令与函数的联系
CommandDescription = {
    "root": {
        "HelloWorld": main.main,
    },
    "user": {
        "HelloWorld": main.main,
    },
}

# 用户组
UserLists = {
    "root": ["Emb"],
    "user": [],
}
