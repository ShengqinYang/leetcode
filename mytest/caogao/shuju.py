
# 日志表 log 有三个字段 id webname time
# 查询每个用户访问过几个不同的网址 ， 同一用户在不同时间点访问同一网址， 记为两次。（同一用户可以在不同时间访问不同网站的，同一用户也可以在同一时间访问同一网站，
# 也就是说这个时间可以理解为是分钟级别的，不是秒级别的:)
# 请问这个SQL怎么写？

# select sum(cnt)
# from (
# select webname,count(distinct time) cnt
# from table
# where id  = 用户id
# group by webname
# )a
