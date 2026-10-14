
import numpy as np
import random

# گرفتن تعداد معادلات و متغیرها
n = int(input("تعداد معادلات و متغیرها را وارد کنید: "))

# تولید ماتریس ضرایب و جواب‌های سمت راست
while True:
    A = np.array([
        [random.randint(1, 9) for j in range(n)]
        for i in range(n)
    ], dtype=float)

    B = np.array([
        random.randint(1, 20) for i in range(n)
    ], dtype=float)

    det_A = np.linalg.det(A)

    # بررسی اینکه دترمینان صفر نباشد
    if not np.isclose(det_A, 0):
        break

# چاپ معادلات
print("\nمعادلات تولیدشده:")

for i in range(n):
    equation = ""

    for j in range(n):
        equation += f"{A[i][j]:.0f}x{j + 1}"

        if j < n - 1:
            equation += " + "

    equation += f" = {B[i]:.0f}"
    print(equation)

# چاپ دترمینان
print("\nدترمینان ماتریس ضرایب:")
print(round(det_A, 4))

# محاسبه جواب با ضرب ماتریسی
A_inv = np.linalg.inv(A)
X = A_inv @ B

# چاپ جواب متغیرها
print("\nجواب متغیرها:")

for i in range(n):
    print(f"x{i + 1} = {X[i]:.4f}")
