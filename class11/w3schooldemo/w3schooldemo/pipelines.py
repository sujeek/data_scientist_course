# -*- coding: utf-8 -*-

class W3SchooldemoPipeline(object):
    def process_item(self, item, spider):
     	file = open('D://demo//data_drk//ch11//w3schooldemo//W3School_data.txt','a',encoding='utf-8')
     	line = str(item)
     	file.write(line)
     	file.write('\n')
     	file.close()
     	return item
