import gevent
from gevent import monkey; monkey.patch_all()
import time

def long_running_task():
    print("开始耗时请求...")
    time.sleep(20)  # 模拟耗时操作
    return "任务成功完成"

def run_task_with_timeout():
    try:
        with gevent.Timeout(3):
            result = long_running_task()
            print(f"任务结果: {result}")
    except gevent.Timeout:
        print("任务超时")
    except Exception as e:
        print(f"任务失败，原因: {str(e)}")

run_task_with_timeout()
