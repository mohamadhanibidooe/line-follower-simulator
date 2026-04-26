# شبیه‌ساز ربات دنبال‌کننده خط

یک شبیه‌ساز ساده با **Python و Pygame** برای آزمایش الگوریتم‌های ربات دنبال‌کننده خط.

در این پروژه می‌توانید الگوریتم کنترل ربات خود را بنویسید و آن را روی یک مسیر مجازی تست کنید، بدون اینکه به ربات واقعی نیاز داشته باشید.

این پروژه برای موارد زیر مفید است:

- یادگیری مفاهیم رباتیک
- تمرین الگوریتم‌های دنبال‌کننده خط
- تست منطق قبل از اجرا روی ربات واقعی
- آموزش برنامه‌نویسی و رباتیک

---

# ویژگی‌ها

- شبیه‌سازی ربات دو موتوره
- ۵ سنسور تشخیص خط
- امکان نوشتن الگوریتم سفارشی
- تعیین نقطه شروع ربات
- شبیه‌سازی لحظه‌ای با pygame
- API ساده برای کنترل ربات

---

# پیش‌نیازها

- Python 3.9 یا بالاتر
- pygame

نصب pygame:

```bash
pip install pygame
```

---

# اجرای شبیه‌ساز

برای اجرای برنامه:

```bash
python runner.py
```

در شروع برنامه ممکن است از شما مختصات شروع ربات پرسیده شود:

```text
Enter robot start X
Enter robot start Y
```

اگر چیزی وارد نکنید، مقدار پیش‌فرض استفاده می‌شود.

---

# ساختار پروژه

```text
line-follower-simulator/
│
├── config.py
├── runner.py
├── user_code
    ├── user_code.py
├── track.png
│
└── simulator/
    ├── engine.py
    ├── robot.py
    ├── world.py
    ├── __init__.py
    ├── sensors.py
    ├── track.png
    └── api_stub.py
```

توضیح فایل‌ها:

### runner.py
فایل اصلی برای اجرای شبیه‌ساز.

### user_code.py
در این فایل الگوریتم کنترل ربات نوشته می‌شود.

### track.png
تصویر مسیر حرکت ربات.

### simulator/
هسته اصلی شبیه‌ساز.

---

# نحوه کار شبیه‌ساز

شبیه‌ساز در یک حلقه دائمی اجرا می‌شود:

1. دریافت رویدادها
2. محاسبه زمان بین فریم‌ها (dt)
3. به‌روزرسانی محیط
4. به‌روزرسانی فیزیک ربات
5. به‌روزرسانی سنسورها
6. اجرای الگوریتم شما
7. رسم همه چیز روی صفحه

کد شما در هر فریم اجرا می‌شود.

---

# نوشتن کد ربات

تمام الگوریتم ربات در فایل زیر نوشته می‌شود:

```
user_code.py
```

---

# ساختار فایل user_code.py

```python
from simulator.api_stub import read_line_sensors, set_motors


def setup():
    print("Robot started")


def loop(dt):
    sensors = read_line_sensors()

    if sensors[2]:
        set_motors(50, 50)
    else:
        set_motors(0, 0)
```

---

# تابع setup()

این تابع **یک بار در شروع برنامه** اجرا می‌شود.

```python
def setup():
    print("Algorithm initialized")
```

---

# تابع loop(dt)

این تابع در **هر فریم** اجرا می‌شود.

پارامتر:

```
dt = زمان گذشته از فریم قبلی
```

مثال:

```python
def loop(dt):
    sensors = read_line_sensors()

    if sensors[2] == 1:
        set_motors(60, 60)
    else:
        set_motors(30, 60)
```

---

# توابع API

برای استفاده از API:

```python
from simulator.api_stub import read_line_sensors, set_motors
```

---

# read_line_sensors()

خواندن مقدار سنسورهای خط.

```python
sensors = read_line_sensors()
```

نمونه خروجی:

```text
[0, 1, 1, 0, 0]
```

ترتیب سنسورها:

```text
[L2, L1, C, R1, R2]
```

معنی سنسورها:

- L2 : چپ دور
- L1 : چپ
- C : وسط
- R1 : راست
- R2 : راست دور

مقادیر:

```
1 = خط دیده شده
0 = خط دیده نشده
```

---

# set_motors(left, right)

کنترل سرعت موتورهای ربات.

```python
set_motors(left_speed, right_speed)
```

محدوده سرعت:

```
0 تا 100
```

مثال:

```python
set_motors(50, 50)
set_motors(30, 70)
set_motors(70, 30)
set_motors(0, 0)
```

---

# مثال الگوریتم دنبال‌کننده خط

```python
from simulator.api_stub import read_line_sensors, set_motors


def setup():
    print("Line follower ready")


def loop(dt):
    s = read_line_sensors()

    if s[2]:
        set_motors(60, 60)

    elif s[1]:
        set_motors(30, 60)

    elif s[3]:
        set_motors(60, 30)

    else:
        set_motors(20, 20)
```

---

# رفع مشکلات

اگر pygame نصب نیست:

```bash
pip install pygame
```

اگر برنامه اجرا نمی‌شود مطمئن شوید داخل پوشه پروژه دستور زیر را اجرا می‌کنید:

```bash
python runner.py
```

---

# توسعه‌های آینده

- اضافه شدن کنترلر PID
- نمایش سنسورها روی صفحه
- پشتیبانی از چند مسیر
- تنظیم پارامترهای ربات
- حالت مسابقه

---


