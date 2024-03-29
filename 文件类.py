# 请封装设计一个操作文件和文件夹类，
import os

class File:
# 创建文件
    def create_file(self, file_name):
        with open(file_name, 'w') :
            pass
        print(f'{file_name}'"创建成功")
# 删除文件
    def delete_file(self, file_name):
        if os.path.exists(file_name):
          os.remove(file_name)
          print(f'{file_name}'"删除成功")
        else:
          print(f'{file_name}'"不存在")
# 文件备份
    def backup_file(self, file_name):
        if os.path.exists(file_name):
          os.rename(file_name, file_name+".bak")
          print(f'{file_name}'"备份成功")
        else:
          print(f'{file_name}'"不存在")

# 示例用法
if __name__ == '__main__':
    file = File()
user_input = input("你要创建文件吗? (yes/no): ")
if user_input.lower() == "yes":
    create = input('请输入要创建的文件名: ')
    file.create_file(create)
else:
    print("没有执行任何操作.")
user_dele = input("你要删除文件吗? (yes/no): ")
if user_dele.lower() == "yes":
    delete = input('请输入要删除的文件名: ')
    file.delete_file(delete)
else:
        print("没有执行任何操作.")

user_backup = input("你要备份文件吗? (yes/no): ")
if user_backup.lower() == "yes":
    backup = input('请输入要备份的文件名: ')
    file.backup_file(backup)
else:
    print("没有执行任何操作.")























