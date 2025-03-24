"""
Django 設定檔 - WebSocket_Server 專案。

這個檔案是由 'django-admin startproject' 生成的，使用的是 Django 5.1.7 版本。

更多資訊，請參考：
https://docs.djangoproject.com/en/5.1/topics/settings/

如需完整的設定列表及其值，請參見：
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# 設定專案的基礎目錄，便於管理檔案路徑
BASE_DIR = Path(__file__).resolve().parent.parent


# 快速啟動開發設定 - 不適用於生產環境
# 請參考 https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# 安全警告：生產環境中請保管好秘鑰
SECRET_KEY = 'django-insecure-l#j4mjik^!ttz5+f-9&lq0r8*_e3i!%k+zuqri+ovkncp7--40'

# 安全警告：不要在生產環境中啟用 Debug
DEBUG = True

# 設定允許的主機（通常是伺服器域名或IP地址）
ALLOWED_HOSTS = []


# 應用程式定義

INSTALLED_APPS = [
    'django.contrib.admin',  # Django 管理後台
    'django.contrib.auth',   # 使用者認證
    'django.contrib.contenttypes',  # 內容型態系統
    'django.contrib.sessions',  # 會話管理
    'django.contrib.messages',  # 消息框架
    'django.contrib.staticfiles',  # 靜態檔案處理
    'channels',  # 加入 Django Channels 應用
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # 安全中介軟體
    'django.contrib.sessions.middleware.SessionMiddleware',  # 會話中介軟體
    'django.middleware.common.CommonMiddleware',  # 常規中介軟體
    'django.middleware.csrf.CsrfViewMiddleware',  # 防止 CSRF 攻擊
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 身份驗證中介軟體
    'django.contrib.messages.middleware.MessageMiddleware',  # 消息中介軟體
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # 防止點擊劫持
]

ROOT_URLCONF = 'WebSocket_Server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # 使用 Django 模板引擎
        'DIRS': [],  # 指定模板目錄
        'APP_DIRS': True,  # 啟用應用程式模板
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Debug 設定
                'django.template.context_processors.request',  # 請求處理
                'django.contrib.auth.context_processors.auth',  # 認證處理
                'django.contrib.messages.context_processors.messages',  # 消息處理
            ],
        },
    },
]

# 設定 ASGI 應用，用來支援 WebSocket
ASGI_APPLICATION = 'WebSocket_Server.asgi.application'

# 設定 WSGI 應用
WSGI_APPLICATION = 'WebSocket_Server.wsgi.application'


# 資料庫設定
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 使用 SQLite 資料庫
        'NAME': BASE_DIR / 'db.sqlite3',  # 資料庫檔案儲存位置
    }
}


# 密碼驗證
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # 用戶屬性相似性驗證
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # 密碼最小長度驗證
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # 常見密碼驗證
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # 數字密碼驗證
    },
]


# 國際化設置
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'  # 設定語言為美式英語

TIME_ZONE = 'UTC'  # 設定時區為 UTC

USE_I18N = True  # 啟用國際化
USE_TZ = True  # 啟用時區設定


# 靜態檔案設定（CSS, JavaScript, 圖像等）
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'  # 靜態檔案的 URL 路徑

# Redis 配置：Django Channels 使用 Redis 作為訊息層
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',  # 使用 Redis 作為訊息後端
        'CONFIG': {
            'hosts': [('49.213.238.75', 6379)],  # Redis 伺服器的主機和端口
        },
    },
}

# 設定預設的主鍵欄位類型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
