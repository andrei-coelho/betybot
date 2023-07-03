
from testes import scrapy


"""


status = c.exec("INSERT INTO tests(test_nome) values ('test7')")

e = Connector()

allv = e.query("SELECT * FROM tests;")

f = Connector()

f.exec("INSERT INTO tests(test_nome) values ('test8')")

j = Connector()

allv2 = j.query("SELECT * FROM tests;")

print(allv2)


from libs.connector import Connector

allf = Connector().query("SELECT * FROM tests") 

print(allf)


import importlib

slug = "slugdacasa"

my_module = importlib.import_module('houses.'+slug+'.scrapy')

"""
