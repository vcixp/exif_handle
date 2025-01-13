# exif_handle 
## 部署方法

---

### 1. PYTHON
1. 安装python环境,本项目需要安装python版本 $ \geq $ 3.8 
2. 安装python依赖
```
pip install opencv-python
pip install exifread
pip install pillow
pip install pyheif
pip install piexif
```
3. python程序部署
python目录文件
> exifread_photo.py $ \qquad \,$ 程序文件
> logo $ \qquad \qquad \qquad \quad \,\, $ logo目录,不同品牌的logo以png文件放入该目录
> fonts $ \qquad \qquad \qquad \quad $ 字符样式目录，将需要的字符的fft放入该目录

将Python目录的文件放置于任意目录，修改exifread_photo.py文件：
146-148行，将“***/font.ttf”修改为字体所在目录
```
    font1 = ImageFont.truetype("***/font.ttf", font_size)
    font2 = ImageFont.truetype("***/font.ttf",
                               font_size * fist_row_font_rate)
```
160-162行,将“***/logo/”修改为logo目录所在位置
```
if make != '' and os.path.exists('***/logo/' + make + '.png'):
        result_img = cv2.imread(to_path)
        logo_img = cv2.imread('***/logo/' + make + '.png')
```
至此，python 部分部署结束

---

### 后端部分
1. 安装java 并配置环境变量
2. 安装maven并配置环境变量
3. 进入exif_backend目录，修改src-main-resources-application.yml文件中的三个位置
```
app:
  location: uploadpath                      #图片上传的临时位置
  python-exec: python_exec_path             #python执行文件的位置
  python-file: path_exifread_photo.py       #exifread_photo.py所在的位置
```

例如
```
app:
  location: /opt/temp
  python-exec: /opt/anaconda3/envs/cv39/bin/python
  python-file: /data/python/exifread_photo.py 
```
4. 切换目录至exif_backend目录，执行maven打包
` mvn package`
在target目录中得到“exif_handle-1.0-SNAPSHOT.jar”文件，运行以下代码启动后端
` java -jar exif_handle-1.0-SNAPSHOT.jar &`

---

### 部署前端

1. 安装ngixn
2. 进入exif_frontend目录，运行以下目录打包
   ```
   yarn install
   yarn build
   ```
   得到dist目录
3. 修改nginx配置
   ```
   server {
	    listen 80 default_server;
        root dist目录;//修改该位置
        //新增以下代码
        client_max_body_size 500m;
        location /api/ {
		    proxy_pass http://localhost:10000/;
	    }
    }
   
   ```