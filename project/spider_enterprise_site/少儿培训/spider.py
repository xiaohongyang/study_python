import sys
import os
from pathlib import *
sys.path.append("D:\www\project\study_python")
from project.tools.spider.spider import Spider


spider = Spider("")

spider.setLinkList([
    "http://static.qifeiye.com/caches/f14b4b77c0eecfe5a34c716fea5c2437/aHR0cDovLzU5NDdhOTc1OTAwNzYudDczLnFpZmVpeWUuY29tL3FmeS1jb250ZW50L3VwbG9hZHMvMjAxNy8wNi8yNGU4Yjc4NWQ2NzcxZGI5NTNlZWQzNjZlY2IyMzQ1NS02NHg2NC5wbmc_p_p100_p_3D.png"
]);

currentPath = sys.path[0]
downPath = currentPath + "/down_source"
spider.downLinkList(downPath)


print("finished")