# -*- coding: utf-8 -*-
# Time: 2018/10/13 19:01:30
# File Name: ex_interval.py

from datetime import datetime
import os
from pytz import utc
import datetime
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
#from apscheduler.jobstores.mongodb import MongoDBJobStore
#from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

def tick():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    #interval
    # scheduler = BlockingScheduler()
    # scheduler.add_job(tick, 'interval', seconds=3)
    # print('Press Ctrl+{0} to exit'.format('Break'))
    #
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     pass

    #cron
    # hour = 19, minute = 23
    # hour = '19', minute = '23'
    # minute = '*/3'
    # 表示每3分钟执行一次
    # hour = '19-21', minute = '23'
    # 表示
    # 19: 23、 20: 23、 21: 23
    # 各执行一次任务
    #day_of_week='fri'表示每周五
    # scheduler = BlockingScheduler()
    # scheduler.add_job(tick, 'cron', hour=14, minute=20,second=30)
    # print('Press Ctrl+{0} to exit'.format('Break'))
    #
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     pass


    #date
    # scheduler = BlockingScheduler()
    # scheduler.add_job(tick, 'date', run_date='2021-08-13 14:27:50')
    # print('Press Ctrl+{0} to exit'.format('Break'))
    #
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     pass

    # jobstores = {
    # 'mongo': MongoDBJobStore(),
    # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    # }
    # executors = {
    # 'default': ThreadPoolExecutor(20),
    # 'processpool': ProcessPoolExecutor(5)
    # }
    # job_defaults = {
    # 'coalesce': False,
    # 'max_instances': 3
    # }
    # scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)

    def my_job(id='my_job',name='hello'):
        print(id, '-->', datetime.datetime.now())
        print(name)
    jobstores = {
        'default': MemoryJobStore()
    }
    executors = {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(10)
    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 3
    }
    scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
    scheduler.add_job(my_job, args=['job_intervalone','123'],id='job_interval',trigger='interval', seconds=5,replace_existing=True)
    scheduler.add_job(my_job, args=['job_cronone', ], id='job_cron', trigger='cron',month='4-8,11-12', day='11-13', hour='16-17', minute='*/2',second='*/10',start_date='2021-08-13 17:02:30' ,end_date = '2021-08-13 17:10:20')
    scheduler.add_job(my_job, args=['job_once_nowone',], id='job_once_now')
    scheduler.add_job(my_job, args=['job_date_onceone', ], id='job_date_once', trigger='date',run_date='2021-08-14 16:43:05')
    try:
        scheduler.start()
    except SystemExit:
        print('exit')
        exit()