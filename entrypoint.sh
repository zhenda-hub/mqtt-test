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
