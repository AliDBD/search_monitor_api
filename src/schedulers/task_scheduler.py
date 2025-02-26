# src/schedulers/task_scheduler.py
"""
调度模块，使用apscheduler定时运行main
"""
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_daily(main_func):
    """
    每天运行指定的主函数
    """
    scheduler = BlockingScheduler()
    scheduler.add_job(main_func, 'cron', hour=1, minute=0)  # 每天凌晨1点运行
    try:
        logger.info("Starting scheduler...")
        scheduler.start()
    except KeyboardInterrupt:
        logger.info("Stopping scheduler...")
        scheduler.shutdown()