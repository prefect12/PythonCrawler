from scrapy.cmdline import execute
import sys,os
# subprocess.run(["I:\Python\\anaconda\Scripts\\activate.bat 'Scrapy Env'"])

# print(__file__)
# print(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","51job"])