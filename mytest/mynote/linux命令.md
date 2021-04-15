常见指令：
http://192.168.0.79:8890 ipython
http://192.168.0.53:8889 ipython

1.tail / head
	head 查看一个文件的前多少行，默认10行
	tail 查看一个文件的后多少行，默认10行
	从最后的一行开始数，查询1650-1660行的日志
	tail -1650 run.log | head -10

2.df 查看整个硬盘（又称：磁盘）占用情况%
	df -h
	```
		Filesystem      1K-blocks       Used Available Use% Mounted on
		udev             65883048          4  65883044   1% /dev
		tmpfs            13179424       1152  13178272   1% /run
		/dev/dm-0      1770140372 1315554472 364644908  79% /       硬盘占用79%
		none                    4          0         4   0% /sys/fs/cgroup
		none                 5120          0      5120   0% /run/lock
		none             65897104         88  65897016   1% /run/shm
		none               102400         44    102356   1% /run/user
		/dev/sdb1          240972      80870    147661  36% /boot
		/dev/sda1      1968878716  874471720 994370732  47% /var/lib/mongodb
	```

3.free 查看内存使用情况（注意：内存不够用的时候用硬盘充当内存空间使用）
	free -g   m是兆/g是几个G
	```
		[root@VM_0_15_centos local]# free -g
				  total        used        free      shared  buff/cache   available
	Mem:              1           0           0           0           1           1
	Swap:             0           0           0
	```
	79/70 是251g的内存、4T固态硬盘，其他71-78都是120g的内存、2T机械硬盘硬盘
4.

```
history | grep activate    					 查看历史 包含activate的命令
source ~/wangpeng/Spider3.4/bin/activate     
du -h --max-depth=1 ~/jeans/
```

运程启程序，后台启动程序

```mysql
https://blog.mythsman.com/2016/01/19/1/
screen -S name(起个别名) python test.py
screen -ls 查看正在跑的程序
screen -r name  回到name程序看
ctrl + a + k / ctrl + c 完全杀死程序
ctrl + a + d  暂离当前screen

screen -S stra python run.py   stratechery
screen -S damodaran python run.py  Aswathdamodaran
screen -S retaildive python run.py

后台执行root目录下的test.sh 脚本：
nohup /root/test.sh &

后台执行 root 目录下的 test.sh 脚本，并重定向输入到 test.log 文件：
nohup /root/test.sh > test.log 2>&1 & 

ps -aux | grep "test.sh" 
直接kill pid
```
```python
保存，但不退出vi                       :w
保存并退出vi                           :wq
退出vi，但不保存更改                   :q!
用其他文件名保存                       :w filename
在现有文件中保存并覆盖该文件           :w! filename
```

```linux
lftp jiuqian:Meritco@0126@publicftp.meritco-group.com:2121 -e "set verify-certificate false"   连接ftp
cat wechat_publish_A_201812.csv | wc -l  查看总条数
put /home/m2/yushiqi/out/wechat_publish_A_201812.rar  将该文件上传ftp
bye 
```


上传文件快捷方式

```
cd 到要上传的路径  rz  选择上传文件
sz 文件所在路径  选择存放地点
```


打包压缩/解压

```linux
sudo rar a wechat_publish_A_201812.rar wechat_publish_A_201812.csv  生成压缩文件
rar a test.rar ./test/  将./test/文件夹打包成test.rar
rar x BasicInformation.rar        解压文件

gzip -r 目录
gzip -d part-r-00049.gz   解压文件 并 删除压缩包part-r-00049.gz
```


mongostat  查看mongo状态
```
sudo mongod --config  /etc/mongod.conf  --maxConns=2000 重启mongo ，设置最大连接数
 ./bin/mongod --dbpath=/root/db --maxConns=2000
 nohup sudo mongod --config /etc/mongod.conf  2>&1 & 后台启动
/var/log/mongodb    查看日志


查看进程|批量杀死进程
``` 
ps aux | grep kol_clear
ps -ef|grep pid
ps -ef|grep 51953
kill 进程id  第二列
pgrep -f '/home/m2/xueersi/xueersi.py' | wc -l
pkill -f '/home/m2/xueersi/xueersi.py'
pgrep -f '/home/m2/yangshengqin/codes/weiboSpider/WeiboKOLProduct/weibo_publish_sprider.py' | wc -l

ps -ef | grep weibo_reposts_thread_sprider.py|grep -v grep|cut -c 9-15|xargs kill -9
ps -ef | grep weibo_comment_sprider.py|grep -v grep|cut -c 9-15|xargs kill -9
ps -ef | grep weibo_attitudes_sprider.py|grep -v grep|cut -c 9-15|xargs kill -9
ps -ef | grep bili_publish_list.py|grep -v grep|cut -c 9-15|xargs kill -9
ps -ef | grep user_detail_spider.py|grep -v grep|cut -c 9-15|xargs kill -9
ps -ef | grep weibo_attitudes_sprider.py|grep -v grep|cut -c 9-15|xargs kill -9

管道符"|"用来隔开两个命令，管道符左边命令的输出会作为管道符右边命令的输入。
"ps -ef" 是linux里查看所有进程的命令。这时检索出的进程将作为下一条命令"grep LOCAL=NO"的输入。
"grep weibo_reposts_thread_sprider.py" 的输出结果是，所有含有关键字"weibo_reposts_thread_sprider.py"的进程。
"grep -v grep" 是在列出的进程中去除含有关键字"grep"的进程。
"cut -c 9-15" 是截取输入行的第9个字符到第15个字符，而这正好是进程号PID。
"xargs kill -9" 中的 xargs 命令是用来把前面命令的输出结果（PID）作为"kill -9"命令的参数，并执行该命令。"kill -9"会强行杀掉指定进程。
```

# 查看终端信息
cd /dev/pts
echo '消息' > 11【终端代码】

(weiboenv) m2@crawl-10:/dev/pts$ who 
m2       tty1         2019-04-23 16:46
m2       pts/1        2019-12-10 20:32 (10.153.89.57)
m2       pts/7        2019-07-19 10:25 (10.153.89.23:S.1)
m2       pts/11       2019-12-09 15:19 (10.153.88.88)
m2       pts/24       2019-11-22 19:29 (192.168.0.103)
m2       pts/27       2019-11-25 20:16 (192.168.0.103)
m2       pts/3        2019-12-10 20:39 (10.153.89.57)
m2       pts/20       2019-09-11 21:16 (10.153.89.23:S.0)
m2       pts/2        2019-07-19 10:24 (10.153.89.23:S.0)
m2       pts/28       2019-12-04 10:22 (10.153.89.23)



top 查看
```
top  shift + m按照使用内存大小排序    c 显示爬取的程序  
locate  AKOLthread_show_batch_50_playnum_0315.py  查看文件位置
```

```
Python虚拟环境创建3种方式
1.virtualenv【默认虚拟环境路径：/home/m2/.virtualenvs/my_project_env】
	通过pip安装virtualenv：
	pip install virtualenv
	virtualenv --version
	为一个工程项目搭建一个虚拟环境:
	cd my_project
	virtualenv my_project_env
	virtualenv -p /usr/bin/python2.7 my_project_env 创建虚拟环境
	source my_project_env/bin/activate 激活虚拟环境
	
2.virtualenvwrapper【默认虚拟环境路径：/home/m2/Envs/my_project_env】 
	mkvirtualenv spider
3.conda virtualenvwrapper
conda create -n python2.7 python=2.7.9 指定创建2.7.9的python环境，系统默认2.7.6
conda activate python2.7   启动虚拟环境
conda create -n weiboenv python=3.7.3
source ~/.bashrc

````
pip3 install virtualenvwrapper --upgrade
mkvirtualenv -p /usr/bin/python3 py3_test
rmvirtualenv py3_test
查看datacsv文件夹占用硬盘大小
```
du -h --max-depth=1 ./datacsv/    #29G
```
查看内存使用情况
free -g  【free -m】

清除缓存
sudo sync  
sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"  

vim  
```
set bomb?
set bomb
```
查看僵尸进程
```
ps -aux |grep Z
```

合并文件【场景：B站14个表，筛选出kol_name以及粉丝数，按kol_name去重】
```
cat *.csv |awk -F ',' '!a[$7]++{print $7,$13}' >author.csv
cat 连接文件
AWK是一种处理文本文件的语言，是一个强大的文本分析工具  -F指定分隔符为, !a[$7]按照第7列去重，输出第7列和第13列
> 重定向符输出，将结果输出author.csv

将一个大文件分成若干个小文件方法
例如将一个BLM.txt文件分成前缀为 BLM_ 的1000个小文件，后缀为系数形式，且后缀为4位数字形式
先利用
wc -l BLM.txt       读出 BLM.txt 文件一共有多少行
再利用 split 命令
split -l 2482 ../BLM/BLM.txt -d -a 4 BLM_
split -l 56045256 ../BLM/BLM.txt -d -a 4 BLM_
将 文件 BLM.txt 分成若干个小文件，每个文件2482行(-l 2482)，文件前缀为BLM_ ，系数不是字母而是数字（-d），后缀系数为四位数（-a 4）


删除最后一行【分隔符：,】
awk -F, 'OFS=","{$NF="";print}' zf0_1_0_1_01_ab.csv
删除最后一个分隔符
awk -F, 'OFS=","{$NF="";print}' zf0_1_0_1_01_ab.csv |sed 's/,$//g'
ls ./factset/ | wc -w  查看factset文件夹下有几个文件
find ./ -type f -size 0  | wc -w  统计./目录下文件为0的文件个数
```
curl myip.ipip.net 查看服务器IP

vim批量注释
```
1.批量插入
ctrl + v  
按 j （向下选取列）或者 k （向上选取列）
再按Shift + i 进入编辑模式然后输入你想要插入的字符（任意字符）
2.批量删除
ctrl + v  
按 j （向下选取列）或者 k （向上选取列）
再按d删除保存退出 
```
查看进程下的线程数 46741进程id
ps -T -p 93948
ps -T -p 23528
scp /home/omnivoice/yangshengqin/AllContentIds.rar m2@192.168.0.70:/home/m2/yangshengqin/datacsv/

入hive库数据
2.5g的数据大约耗用10g内存
3g的数据大约耗用12g内存

（1）问题：每周入hive库数据post_date可能追溯到半年前，【新增加的kol会爬取前半年】。假如入库的过程的中出现问题，需要删除部分数据进行重新入库时，只能根据文章发布日期删除，这样需要删除数据量会过于庞大且会误删正确数据，非常耗时，且效率低下。越往后期数据量会越来越庞大，出现问题要重新入库的数据量就会不可控。
（2）出现问题的大致原因：1.服务器/公司电脑突发性断电；2.数据库连接出现问题；3.数据格式出现问题；4.数据错列。5.手抖~。等等
（3）建议：多增加几个分区字段，例如：ver【上传日期】，或者你们还要更好的解决方案我们也可以一起讨论下
（4）注意：
1.hive库数据删除只能根据分区进行删除
2.微博综合表分区字段post_date【文章发布日期】，微博转评赞表分区字段post_date + tablename
3.hive查询速度本身就很不稳定，快的2分钟之内，慢的30分钟左右
4.入库操作也很耗时，也是快的几分钟，慢的几十分钟

搭建自己的代理服务器trojan
https://amos-x.com/index.php/amos/archives/centos7-trojan/

#杀死chromedriver + 重启chromedriver 
ps aux |grep chrome |awk '{print $2}' |xargs kill -9
ps aux |grep dianping_shop_review |awk '{print $2}' |xargs kill -9
nohup chromedriver &