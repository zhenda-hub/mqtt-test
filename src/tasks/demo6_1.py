import multiprocessing
import time

def long_running_task(queue):
    print("开始耗时请求...")
    time.sleep(2)  # 模拟耗时操作
    queue.put("任务成功完成")  # 将结果放入队列

def run_task_with_timeout():
    # 创建队列用于接收结果
    queue = multiprocessing.Queue()

    # 创建进程，传入队列
    process = multiprocessing.Process(target=long_running_task, args=(queue,))
    process.start()

    # 等待最多3秒
    process.join(timeout=3)

    if process.is_alive():
        print("任务超时")
        process.terminate()  # 超时后终止进程
        process.join()  # 确保进程已经终止
    else:
        # 任务成功完成，从队列中获取结果
        if not queue.empty():
            result = queue.get()
            print(f"任务结果: {result}")
        else:
            print("任务完成，但没有返回结果")

run_task_with_timeout()
