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

## **📌 الصلاحيات (Permissions)**
- يمكن لأي **مستخدم (حتى غير المسجلين)** قراءة البيانات (`GET`).
- لا يمكن إنشاء (`POST`) أو تحديث (`PUT`) أو حذف (`DELETE`) كتاب إلا إذا كان **المستخدم مسجلاً دخوله**.

### **🔧 إعدادات الصلاحيات في `views.py`**
```python
from rest_framework import permissions

permission_classes = [permissions.IsAuthenticated]  # 🔒 يتطلب تسجيل الدخول
```

---

## **📌 المصادقة والاختبار**
### **✅ تسجيل الدخول باستخدام `Basic Auth`**
1️⃣ **إنشاء مستخدم جديد عبر Django Admin**  
2️⃣ استخدام `Postman` أو `cURL` لاختبار المصادقة.

### **✅ اختبار API باستخدام `cURL`**
**📖 جلب جميع الكتب (متاح للجميع):**
```bash
curl -X GET http://127.0.0.1:8000/api/books/
```
**➕ إضافة كتاب جديد (يتطلب تسجيل الدخول):**
```bash
curl -X POST http://127.0.0.1:8000/api/books/create/ \
    -H "Content-Type: application/json" \
    -u username:password \
    -d '{"title": "REST API with Django", "publication_year": 2022, "author": 1}'
```
**✏️ تحديث كتاب (يتطلب تسجيل الدخول):**
```bash
curl -X PUT http://127.0.0.1:8000/api/books/1/update/ \
    -H "Content-Type: application/json" \
    -u username:password \
    -d '{"title": "Updated Book Title", "publication_year": 2023}'
```

---

## **📌 إعدادات المشروع في `settings.py`**
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ]
}
```

---

## **📌 توثيق الـ API باستخدام `Swagger`**
**لتفعيل `Swagger UI` لتوثيق الـ API:**  
1️⃣ قم بتثبيت `drf-yasg`:  
```bash
pip install drf-yasg
```
2️⃣ أضف هذا الكود إلى `api/urls.py`:
```python
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path

schema_view = get_schema_view(
    openapi.Info(
        title="Books API",
        default_version='v1',
        description="API documentation for managing books",
    ),
    public=True,
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
]
```
3️⃣ افتح المتصفح على:  
🔗 `http://127.0.0.1:8000/swagger/`

---

## **📌 ملاحظات إضافية:**
- يمكنك **إضافة `TokenAuthentication`** لتحسين أمان الـ API.
- استخدم `Postman` أو `cURL` لاختبار الـ API بسهولة.
- **إضافة `pagination` و `filtering`** سيجعل التجربة أفضل للمستخدمين.

🚀 **تم تنفيذ المشروع بواسطة [اسمك]** 😃  
🔥 **هل لديك أي استفسارات؟ لا تتردد في سؤالي!**  

---

### **📌 5️⃣ رفع المشروع على GitHub**
بعد كتابة ملف `README.md`، ارفع المشروع إلى GitHub:

```bash
git init
git add .
git commit -m "Initial commit with API documentation"
git branch -M main
git remote add origin https://github.com/اسم-حسابك/Alx_DjangoLearnLab.git
git push -u origin main
```

💡 **هكذا يصبح مشروعك جاهزًا للعمل والمشاركة مع الآخرين!** 😃🚀