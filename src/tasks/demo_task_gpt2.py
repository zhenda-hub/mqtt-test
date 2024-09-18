import asyncio

async def long_running_task():
    print("开始耗时请求...")
    await asyncio.sleep(20)  # 模拟一个耗时操作（20秒）
    return "任务成功完成"

async def run_async_task_with_timeout():
    try:
        # 设置超时时间为 30 秒
        result = await asyncio.wait_for(long_running_task(), timeout=3)
        print(f"任务结果: {result}")
    except asyncio.TimeoutError:
        print("任务超时")
    except Exception as e:
        print(f"任务失败，原因: {str(e)}")

# 运行异步任务
asyncio.run(run_async_task_with_timeout())
