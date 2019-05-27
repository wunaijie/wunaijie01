import allure


class Test02(object):
    def test02(self):
        """添加图片进测试报告"""
        with open("C:\\Users\\Administrator\\Desktop\\day07\\.pytest_cache\\自己画的PO流程png.png", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
