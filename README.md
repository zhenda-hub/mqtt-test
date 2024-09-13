# mqtt-test


# tornado-stu

#### use docker

1. 
```bash
docker init
```

2. 改为 entrypoint.sh 启动
   
```Dockerfile
ENTRYPOINT ["sh", "./entrypoint.sh"]
CMD ["tail", "-f", "/dev/null"]
```

```sh
#!/bin/bash

echo "start sh!!!!!!!"
ls
echo "pwd: "
pwd
whoami
echo "pip list: "
pip list

# pip freeze > requirements.txt

# python 

# 执行传入的命令或默认命令
exec "$@"
```

```yaml
volumes:
  - .:/app  # 挂载本地所有文件!!
```

3. 
```bash
docker compose up --build
```
