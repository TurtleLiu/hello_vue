#!/usr/bin/python
# -*- coding: UTF-8 -*-

def check_description_in_file(file_path):
    total_count = 5
    pass_count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("------------多类型数据采集测试---------------")
            if 'description' in content:
                print("文本输入：测试通过✅")
                pass_count += 1
            else:
                print("文本输入：测试不通过❌")
            if 'imageUrl' in content:
                print("图片输入：测试通过✅")
                pass_count += 1
            else:
                print("图片输入：测试不通过❌")
            if 'video' in content:
                print("视频输入：测试通过✅")
                pass_count += 1
            else:
                print("视频输入：测试不通过❌")
            if 'location' in content:
                print("定位输入：测试通过✅")
                pass_count += 1
            else:
                print("定位输入：测试不通过❌")
            if 'sensor' in content:
                print("传感器输入：测试通过✅")
                pass_count += 1
            else:
                print("传感器输入：测试不通过❌")
            pass_rate = pass_count / total_count * 100
            print(f"测试通过数：{pass_count}，测试通过率：{pass_rate}%")
    except FileNotFoundError:
        print("文件未找到，请检查文件路径。")

if __name__ == "__main__":
    # 调用函数并传入文件路径
    check_description_in_file('src/App.vue')