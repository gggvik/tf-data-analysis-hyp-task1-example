import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  p_1 = x_success/x_cnt
  p_2 = y_success/y_cnt
# Вычисление Z-статистики и p-value
p_pooled = (p_1 + p_2) / (x_success + y_success)
z_stat = (p_2 - p_1) / ((p_pooled * (1 - p_pooled) * (1/x_success + 1/y_success)) ** 0.5)
p_value = st.norm.sf(abs(z_stat)) * 2

# Определение статистической значимости
return p_value < 0.03
