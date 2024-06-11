import pandas as pd

data = [20, 30, 1, 234, "sdf"]
index_labels = ["1st", "2nd", "3rd", "4th", "5th"]
column_label = ["Value"]  # 열 인덱스를 "Value"로 설정

x = pd.DataFrame(data, index=index_labels, columns=column_label)
print(x)