### **📌 إنشاء ملف `README.md` في مشروعك**  

ملف `README.md` مهم جدًا لأنه يساعد المطورين الآخرين (وأنت في المستقبل) على فهم مشروعك بسرعة، ومعرفة كيفية تشغيله واستخدامه.  

---

## **📌 الخطوات لإنشاء `README.md`**
### 1️⃣ افتح **Terminal** وانتقل إلى مجلد المشروع:
```bash
cd advanced_api_project
```

### 2️⃣ قم بإنشاء ملف `README.md`:
```bash
touch README.md
```

### 3️⃣ افتح الملف باستخدام أي محرر نصوص (مثل VS Code أو Nano):
```bash
code README.md  # إذا كنت تستخدم VS Code
```
أو
```bash
nano README.md  # إذا كنت تستخدم Terminal
```

### 4️⃣ أضف هذا المحتوى إلى `README.md`:

---

## **📘 Advanced API Project (Django REST Framework)**  
🚀 **مشروع API متقدم باستخدام Django REST Framework**، لإدارة بيانات الكتب والمؤلفين، مع دعم للعلاقات المتداخلة، الصلاحيات، والتوثيق.  

---

## **📌 كيفية تشغيل المشروع**
### **1️⃣ تثبيت المتطلبات**
```bash
pip install django djangorestframework
```

### **2️⃣ إنشاء المشروع وتطبيق المايجريشن**
```bash
django-admin startproject advanced_api_project
cd advanced_api_project
python manage.py startapp api
python manage.py makemigrations
python manage.py migrate
```

### **3️⃣ إنشاء مستخدم مشرف (Superuser)**
```bash
python manage.py createsuperuser
```
ثم قم بتسجيل الدخول في **Django Admin** عبر:  
🔗 `http://127.0.0.1:8000/admin/`

### **4️⃣ تشغيل السيرفر**
```bash
python manage.py runserver
```

---

## **📌 Endpoints المتاحة:**
| HTTP Method | Endpoint                  | الوصف |
|------------|---------------------------|----------------|
| **GET**    | `/api/books/`             | عرض جميع الكتب 📖 |
| **GET**    | `/api/books/<id>/`        | عرض تفاصيل كتاب معين 🔎 |
| **POST**   | `/api/books/create/`      | إضافة كتاب جديد ➕ (يتطلب تسجيل دخول) |
| **PUT**    | `/api/books/<id>/update/` | تعديل بيانات كتاب ✏️ (يتطلب تسجيل دخول) |
| **DELETE** | `/api/books/<id>/delete/` | حذف كتاب ❌ (يتطلب تسجيل دخول) |

---





## 📌 Filtering, Searching, and Ordering in API

### ✅ Filtering
تصفية الكتب حسب العنوان أو المؤلف أو سنة النشر:
```bash
GET /api/books/?title=Django
GET /api/books/?author=1
GET /api/books/?publication_year=2020
```

### ✅ Searching
البحث عن كتب تحتوي على كلمات معينة في العنوان أو اسم المؤلف:
```bash
GET /api/books/?search=Django
```

### ✅ Ordering
فرز النتائج حسب العنوان أو سنة النشر:
```bash
GET /api/books/?ordering=title
GET /api/books/?ordering=-publication_year
```
```