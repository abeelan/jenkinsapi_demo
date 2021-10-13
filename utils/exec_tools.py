"""
@Time   : 2021/10/13 下午6:19
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 
"""
import time

from jenkinsapi.jenkins import Jenkins


class ExecTools:

    BASE_URL = "http://localhost:8080/"
    USERNAME = "admin"
    PASSWORD = "111ed6f8e26c25cf319da5bb67490aa517"

    def __init__(self):
        self.jenkins = Jenkins(
            self.BASE_URL,
            self.USERNAME,
            self.PASSWORD
        )

    def get_jobs(self) -> list:
        return self.jenkins.keys()

    def invoke(self) -> str:
        job_name = "weather-slave"

        job = self.jenkins.get_job(job_name)

        # 通过参数化构建 job
        job.invoke(build_params={"task": "123"})

        # 如何获取测试报告？
        # 1. Jenkins 自动生成 Junit.xml 报告，拿到之后解析 xml 文件，获取用例执行信息
        # 2. 拿到 allure 的数据信息，解析 json 文件，获取用例执行信息
        # 3. 直接拿到 allure 的连接，就是 allure 的报告信息

        # 这个 API 不准，因为是构建完成立刻获取到的构建次数，一般都会是上一位
        last_build_num = job.get_last_buildnumber()

        # 通过一个循环来规避上面异步的问题，解决拿到的最新构建次数不准
        sec = 30
        while sec > 0:
            build_num = job.get_last_buildnumber()
            if last_build_num != build_num:
                last_build_num = build_num
                break
            sec -= 1
            time.sleep(1)

        report_path = f"{self.BASE_URL}job/{job_name}/{last_build_num}/allure"
        return report_path


