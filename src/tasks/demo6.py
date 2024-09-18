import multiprocessing
import time

def long_running_task():
    print("开始耗时请求...")
    time.sleep(20)  # 模拟耗时操作
    return "任务成功完成"

def run_task_with_timeout():
    # 创建进程池
    process = multiprocessing.Process(target=long_running_task)
    process.start()
    
    # 等待最多3秒
    process.join(timeout=3)
    
    if process.is_alive():
        print("任务超时")
        process.terminate()  # 超时后终止进程
    else:
        print("任务成功完成")

run_task_with_timeout()

