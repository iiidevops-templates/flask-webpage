# Flask Webpage with menu example
flask簡易網頁程式碼範例-docker

## 教學參考來源:
* [how-to-build-a-web-application-using-flask](https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/)

## (local)本地環境隔離快速專案部屬(隨機PORT) + Postman-collection(newman)自動測試
需安裝Docker, 若在Linux環境需額外手動安裝docker-compose, 部屬結果與UI相同
``` 
docker-compose up -d --build 
```
部屬包含flask網頁 + Postman-collection(newman)自動測試, 自動測試報告結果會自動產生在`app/newman-report.xml`, 驗證後即可上傳程式碼
### 查看部屬結果 `docker-compose ps`
```
                   Name                                  Command               State             Ports
---------------------------------------------------------------------------------------------------------------
docker-flask-webpage-1_postman_collection_1   newman run /etc/postman/po ...   Exit 0
docker-flask-webpage-1_web_1                  /bin/sh -c python3 -u main.py    Up       0.0.0.0:49196->5000/tcp
```
訊息內有顯示`0.0.0.0:49196`，則代表可透過 http://localhost:49196 或是 http://您主機IP:49196 來連線到本地部屬的網站
### 查看與追蹤部屬的網頁伺服器紀錄Log `docker-compose logs -f web`
可用`Ctrl+V`來離開Log追蹤
```
web_1                 |  * Serving Flask app "main" (lazy loading)
web_1                 |  * Environment: production
web_1                 |    WARNING: This is a development server. Do not use it in a production deployment.
web_1                 |    Use a production WSGI server instead.
web_1                 |  * Debug mode: on
web_1                 |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1                 |  * Restarting with stat
web_1                 |  * Debugger is active!
web_1                 |  * Debugger PIN: 196-195-249
web_1                 | 172.21.0.3 - - [08/Mar/2021 03:38:29] "GET / HTTP/1.1" 200 -
web_1                 | 10.212.134.104 - - [08/Mar/2021 03:58:23] "GET / HTTP/1.1" 200 -
web_1                 | 10.212.134.104 - - [08/Mar/2021 03:58:23] "GET /static/css/template.css HTTP/1.1" 200 -
web_1                 | 10.212.134.104 - - [08/Mar/2021 03:58:23] "GET /favicon.ico HTTP/1.1" 404 -
web_1                 | 10.212.134.104 - - [08/Mar/2021 03:58:25] "GET /about HTTP/1.1" 200 -
```
### 查看(local)Postman-collection(newman)自動測試以及報告文件
當執行本地環境快速專案部屬時，會自動將您的網站與資料庫部屬完成後再進行自動測試
* 自動測試的檔案在`app/postman_collection_local.json` 使用者可以按照開發上的需求去進行修改
:warning: 
```
  若您是在本地環境直接開發的話，可能會透過瀏覽器連http://localhost:5000
  而到了json檔案內就將http://localhost:5000改成http://web:5000即可
```
自動測試報告結果會自動產生在`app`資料夾內的`newman-report.xml`

## Flask 
### function:
* `url_for()`. It accepts the name of the function as an argument
### folder:
* `templates`: html template file
* `static`: css and image file

## 修改程式碼注意事項
1. 修改Python版本  
版本若非Python:3.8, 想要更換版本請至`Dockefile`修改為自己想要的版本(如需要本機上做測試則須一併連同`Dockerfile.local`去做修改)
2. 部屬環境額外環境變數
若開發需求上可能有針對專案需要的特別環境變數，由於目前此需求不再系統開發考慮範圍內，因此可能要麻煩使用者透過修改`Dockerfile`的形式去加入
```dockerfile
ENV 環境變數名稱1 值1
ENV 環境變數名稱2 值2
ENV 環境變數名稱3 值3
```

## iiidevops
* 專案內`.rancher-pipeline.yml`請勿更動，產品系統設計上不支援pipeline修改
* 目前系統pipeline限制，因此寫的服務請一定要在port:`5000`，資料庫類型無法更改。
* `iiidevops`資料夾內`pipeline_settings.json`請勿更動
* `postman`資料夾內則是您在devops管理網頁上的Postman-collection(newman)自動測試檔案，devops系統會以`postman`資料夾內檔案做自動測試

## reference
https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
