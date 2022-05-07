# Homework Collection

## requirements

1. prompt_toolkit
2. re
3. pickle
4. pymail
5. numpy(暂未用到)
6. Panda(暂未用到)
7. Matplotlib(暂未用到)

## capabilities

1. 指定一个路径作为作业文件夹路径，读取它，然后用正则判断命名是否符合规则和匹配学号，将命名正确的作业放进指定zip路径中。（通过启动程序的路径决定默认作业文件路径，生成的zip默认放在作业文件路径的上级目录）
2. 依据在conf文件中的配置决定受否生成欠交名单或命名不合法的名单，并将名单放入zip中。
3. 给未交作业或命名不正确的同学发一份邮件

