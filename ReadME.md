# WebSocket_Server

這是基於 Django 和 Django Channels 的 WebSocket 聊天伺服器專案，支援 WebSocket 連線進行即時訊息傳遞。

## 專案結構

```
WebSocket_Server/
│
├── WebSocket_Server/
│   ├── __init__.py           # 專案初始化檔案
│   ├── asgi.py               # ASGI 設定檔
│   ├── settings.py           # Django 設定檔
│   ├── urls.py               # 路由設定
│   └── consumers.py          # WebSocket 消費者
│
├── manage.py                 # Django 管理工具
├── requirements.txt          # 專案依賴檔案
└── README.md  
```
# 專案說明
安裝與啟動
1. 安裝虛擬環境
首先，您需要安裝虛擬環境並啟動它。可以使用以下命令創建並啟動虛擬環境：

```

# 在專案根目錄下創建虛擬環境
python -m venv .venv

# 啟動虛擬環境
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```
2. 安裝依賴包
安裝所需的 Python 套件，使用 requirements.txt 安裝：
```
pip install -r requirements.txt
```

3. 運行伺服器
運行 Daphne ASGI 伺服器：
```

daphne -b 0.0.0.0 -p 8000 WebSocket_Server.asgi:application
```

這樣伺服器將會在 http://127.0.0.1:8000 啟動。

4. WebSocket 連線
您可以透過以下 WebSocket URL 進行連線：
```
ws://127.0.0.1:8000/ws/chat/
```

發送訊息格式：

```
{
  "message": "data"
}
```

專案檔案說明
WebSocket_Server/asgi.py: 設定 Django ASGI 應用程式，處理 WebSocket 連線。

WebSocket_Server/settings.py: Django 專案設定檔。

WebSocket_Server/urls.py: 路由設定，負責將請求導向相對應的處理程序。

WebSocket_Server/consumers.py: WebSocket 消費者處理即時訊息的邏輯。

requirements.txt: 列出所有需要安裝的依賴套件。

manage.py: Django 管理工具，執行命令行任務。

