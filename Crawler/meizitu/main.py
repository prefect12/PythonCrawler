# from scrapy.cmdline import execute
# import sys,os
# import subprocess
#
# # subprocess.run(["I:\Python\\anaconda\Scripts\\activate.bat 'Scrapy Env'"])
# # os.system('I:\Python\\anaconda\Scripts\\activate.bat "Scrapy Env"')
# # os.system('scrapy crawl jobbole')
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "jobbole"])


from scrapy.cmdline import execute
import sys,os
# subprocess.run(["I:\Python\\anaconda\Scripts\\activate.bat 'Scrapy Env'"])

# print(__file__)
# print(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","mzt"])