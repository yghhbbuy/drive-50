# generate_cron.py
import random

# 生成随机的分钟（30-58）
minute = random.randint(30, 58)
print(f"{minute} * * * *")
