# -*- coding: utf-8 -*-
# @Time  : 2023/03/14 19:12
# Author : Adan
import datetime
import pytest

# 獲取當前日期和時間
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#報告檔名中的冒號（:）替換為其他有效的字元。例如，你可以將冒號（:）替換為底線（_）：
report_path = "reports/report_{}.html".format(current_time.replace(":", "_"))
# 在報告中添加日期和時間

pytest.main(["--html={}".format(report_path), "--self-contained-html"])
#pytest.main(["--html=reports/report_{}.html".format(current_time), "--self-contained-html"])

#pytest.main(["--html=reports/report.html", "--self-contained-html"])