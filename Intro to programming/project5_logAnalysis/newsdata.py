#! /usr/bin/env python3

import psycopg2
DB_NAME = "news"

# 1. What are the most popular three articles ?
query1 = "select * from popular"

# 2. Who are the most popular article authors of all time?
query2 = "select name,sum(views)as views from author_pop group by name order by views desc"

# 3. On which days did more than 1% of requests lead to errors?
query3 = "select * from perc"

# store results
query_1_result = dict()
query_1_result['title'] = "\n1. The 3 most popular articles are:\n"

query_2_result = dict()
query_2_result['title'] = """\n2. Most popular article authors of
all time are:\n"""

query_3_result = dict()
query_3_result['title'] = """\n3. Days with more than 1% of request that
lead to an error:\n"""


# returns query result
def get_query_result(query):
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' views')


def print_error_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' %')


# stores query result
query_1_result['results'] = get_query_result(query1)
query_2_result['results'] = get_query_result(query2)
query_3_result['results'] = get_query_result(query3)

# print formatted output
print_query_results(query_1_result)
print_query_results(query_2_result)
print_error_query_results(query_3_result)
