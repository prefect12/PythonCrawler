
import requests
from scrapy.selector import Selector
import MySQLdb


conn = MySQLdb.connect('127.0.0.1', 'root', '',db="job", charset="utf8", use_unicode=True)
cursor = conn.cursor()

def crawl_ips():
    #爬取免费ip
    # ON
    # DUPLICATE
    # KEY
    # UPDATE
    # connectionSpeed = Value(connectionSpeed), networkSpeed = value(networkSpeed), aliveTime = value(aliveTime), checkTime = value(checkTime)
    insert_sql = '''insert into ips (ip,port,ipType,connectionSpeed,networkSpeed,aliveTime,checkTime) values (%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE connectionSpeed = Values(connectionSpeed),networkSpeed = values(networkSpeed),aliveTime = values(aliveTime),checkTime = values(checkTime)'''
    url = 'https://www.xicidaili.com/nn/{page}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }

    for pageNum in range(1,150):
        re = requests.get(url=url.format(page = pageNum),headers=headers)
        selector = Selector(text=re.text)
        all_trs = selector.xpath('//tr[position()>1]')

        ip_list = []

        for tr in all_trs:
            ip = tr.xpath('.//td[2]/text()').extract_first()
            port = tr.xpath('.//td[3]/text()').extract_first()
            ipType = tr.xpath('.//td[6]/text()').extract_first()
            speed = tr.xpath('.//div[@class="bar"]/@title').extract()
            connectionSpeed = speed[1]
            networkSpeed = speed[0]
            aliveTime = tr.xpath('.//td[last()-1]/text()').extract_first()
            checkTime = tr.xpath('.//td[last()]/text()').extract_first()
            ip_list.append((ip,port,ipType,connectionSpeed,networkSpeed,aliveTime,checkTime))

        for ip in ip_list:
            cursor.execute(insert_sql, ip)
            conn.commit()
            print(ip)

class GetIP(object):

    def check_ip(self,ip,port):
        http_url = 'http://www.baidu.com'
        proxy_url = 'http://%s:%s'%(ip,port)
        proxy_dic = {
            "http":proxy_url
        }
        try:
            response = requests.get(http_url,proxies = proxy_dic,timeout = 10)
        except Exception as e:
            print(ip+':'+port,'invalid')
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if 200 <= code < 300:
                print('effective ip')
                return True
            else:
                print('invalid ip')
                self.delete_ip(ip)
                return False

    def get_ip(self):
        #随机获取一个可用ip
        while True:
            sql = '''select ip,port from job.ips order by checkTime DESC limit 1;'''
            result = cursor.execute(sql)
            for ip_info in cursor.fetchall():
                ip = ip_info[0]
                port = ip_info[1]
                if self.check_ip(ip,port):
                    return (ip,port)

    def delete_ip(self,ip):
        #删除无效ip
        delete_sql = """
        delete from ips where ip = '{0}'
        """.format(ip)

        cursor.execute(delete_sql)
        conn.commit()
        return True


if __name__ == '__main__':
    # crawl_ips()
    getip = GetIP()
    n = getip.get_ip()
    print(n)