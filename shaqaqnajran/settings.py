from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ct!&ur-+-6k3lemr13b-ac&fgik#o8qmlffct40+r3io1_o#ri'
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'shaqaqnajran.onrender.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts_hub',
    'units_center',
    'booking_flow',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shaqaqnajran.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shaqaqnajran.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ar'

TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# إعدادات WhatsApp Cloud API (ضعي القيم الحقيقية من لوحة Meta)
WHATSAPP_ACCESS_TOKEN = "EAFbYPZAbPJOABQD2cyBV6Xw40LSlZBvRuMXngyzcu6I7Q0OkuxrXVo9wIWXKg4LjWzg8QWRNchTnsxrPD8F3NgvVXrAZCDIXsU8x2ZBDwXUNugNo26ovOmwZCOgohzwi8IZASg1RXodFrFQlKZCjcNODzkeRXyweA5cZAUZADqGokQ5Vdna7vNNARM6AG0voJtnpE8AZDZD"  # ضعِ هنا الـ access token المؤقت أو الدائم
WHATSAPP_PHONE_NUMBER_ID = "855637350972294"
WHATSAPP_BUSINESS_ACCOUNT_ID = "1254994619791622"
