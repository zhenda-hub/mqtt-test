import concurrent.futures
import time

def long_running_task():
    print("开始耗时请求...")
    time.sleep(20)  # 模拟耗时操作
    return "任务成功完成"

def run_task_with_timeout():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(long_running_task)
        try:
            result = future.result(timeout=3)
            print(f"任务结果: {result}")
        except concurrent.futures.TimeoutError:
            print("任务超时")
        except Exception as e:
            print(f"任务失败，原因: {str(e)}")

run_task_with_timeout()
