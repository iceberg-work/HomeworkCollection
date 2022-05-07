import pickle

# 用于校验作业文件名的正则表达式
regular_name_file = None

# 获取学号的正则表达式
regular_number_stu = None

# 作业文件夹路径
folder_path = None

# zip路径
zip_path = None

# 班级名单xlsx路径
class_list_path = None

# 是否开启强制改名
forced_name_change = None

# 是否生成作业欠交名单
generate_list_underpayment_jobs = None

# 是否生成命名不规范名单
generate_the_list_naming_irregularities = None


def save_conf(**kwargs):
    with open('../../docs/conf.bat', 'wb') as conf:
        pickle.dump(kwargs['regular_name_file'], conf)
        pickle.dump(kwargs['regular_number_stu'], conf)
        # pickle.dump(kwargs['folder_path'], conf)
        # pickle.dump(kwargs['zip_path'], conf)
        pickle.dump(kwargs['class_list_path'], conf)
        pickle.dump(kwargs['forced_name_change'], conf)
        pickle.dump(kwargs['generate_list_underpayment_jobs'], conf)
        pickle.dump(kwargs['generate_the_list_naming_irregularities'], conf)


def get_conf():
    with open('../../docs/conf.bat', 'rb') as conf:
        global regular_name_file
        global regular_number_stu
        # global folder_path
        # global zip_path
        global class_list_path
        global forced_name_change
        global generate_list_underpayment_jobs
        global generate_the_list_naming_irregularities
        regular_name_file = pickle.load(conf)
        regular_number_stu = pickle.load(conf)
        # folder_path = pickle.load(conf)
        # zip_path = pickle.load(conf)
        class_list_path = pickle.load(conf)
        forced_name_change = pickle.load(conf)
        generate_list_underpayment_jobs = pickle.load(conf)
        generate_the_list_naming_irregularities = pickle.load(conf)


if __name__ == '__main__':
    save_conf(regular_name_file='[0-9][0-9]')
    get_conf()
