"""
@Time   : 2021/10/13 下午6:22
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 
"""
from loguru import logger
from utils.exec_tools import ExecTools


class TestExecTools:

    def setup_class(self):
        self.jenkins = ExecTools()

    def test_get_jobs(self):
        jobs = self.jenkins.get_jobs()
        logger.info(f"【 jobs 】\n{jobs}")
        assert isinstance(jobs, list)

    def test_invoke(self):
        self.jenkins.invoke()
