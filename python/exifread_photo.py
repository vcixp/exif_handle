import os.path
import sys

import cv2
import numpy as np
import exifread
import datetime
from PIL import Image, ImageFont, ImageDraw
import pyheif
import piexif

white = (255, 255, 255)  # 白色常量
fist_row_font_size = 100  # 第一行文字大小
fist_row_font_rate = 0.9  # 第二行文字和第一行文字大小比例
tow_row_middle = 80  # 两行文字间隔
sides_length = 200  # 文字距离两边的距离
font_top = 60  # 字体最上方的位置
frame_height = 300  # 相框的高
logo_rate = 0.6  # logo缩放比例
logo_top = 80  # logo高度
line_top = 30  # 线高度位置
line_length = 150  # 线长度


# 计算文字长度
def computeTextSize(text, fontType):
    canvas = Image.new('RGB', (2048, 2048))
    draw = ImageDraw.Draw(canvas)
    draw.text((0, 0), text, font=fontType, fill=white)
    bbox = canvas.getbbox()
    size = (bbox[2] - bbox[0], bbox[3] - bbox[1])
    return size[0]


def HeicToJpg(from_path, to_path):
    img = pyheif.read(from_path)  # 读取HEIC图片文件
    # filename = file.split('.')[0]  # 获取文件名
    img_bytes = Image.frombytes(mode=img.mode, size=img.size, data=img.data)  # 读取图片参数
    img_bytes.save(to_path, format="jpeg")  # 保存图片为JPEG
    exif = (img.metadata[0])["data"]  # 获取exif信息
    # piexif.insert(exif, target_path + filename + ".jpeg")
    piexif.insert(exif, to_path)


def executeExposureTime(exposureTime):
    if '/' in exposureTime:
        a = exposureTime.split('/')
        b = int(a[0])
        c = int(a[1])
        if int(b) == 1:
            return exposureTime
        else:
            return str(1) + '/' + str(int(c / b))
    else:
        return exposureTime


def transparence_to_white(img):
    # 如果图像加载正确，且具有透明通道
    if img is not None and len(img.shape) == 3 and img.shape[2] == 4:
        # 分离通道
        b, g, a = cv2.split(img)

        # 确定透明区域（这里假设a全为0即为透明，可根据实际情况调整阈值）
        transparent_mask = a == 0

        # 将透明区域替换为白色
        img[transparent_mask] = [255, 255, 255, 255]

        # 保存结果
        return img
    return img


def create_blank_image(w, h):
    img = np.full((h, w, 3), 255, np.uint8)
    return img


def exif(src):
    file = open(src, "rb")
    tag = exifread.process_file(file)
    photo_time = ''
    make = ''
    model = ''
    info = ''
    if 'EXIF DateTimeDigitized' in tag:
        datetime_digitized = tag['EXIF DateTimeDigitized']
        time = datetime.datetime.strptime(str(datetime_digitized), "%Y:%m:%d %H:%M:%S")
        photo_time = time.strftime("%Y-%m-%d %H:%M")
    if 'Image Make' in tag:
        make = str(tag['Image Make'])
        if make.startswith("NIKON"):
            make = "NIKON"
    if 'Image Model' in tag:
        model = str(tag['Image Model'])
        if model.startswith("NIKON "):
            model = model.replace("NIKON ", "")
    if 'EXIF FocalLengthIn35mmFilm' in tag:
        focal_length = tag['EXIF FocalLengthIn35mmFilm']
        if "{:.1f}".format(eval(str(focal_length))) == '0.0':
            if 'EXIF FocalLength' in tag:
                focal_length = tag['EXIF FocalLength']
                info += "{:.1f}".format(eval(str(focal_length))) + "mm"
        else:
            info += "{:.1f}".format(eval(str(focal_length))) + "mm"
    elif 'EXIF FocalLength' in tag:
        focal_length = tag['EXIF FocalLength']
        info += "{:.1f}".format(eval(str(focal_length))) + "mm"
    if 'EXIF ApertureValue' in tag:
        aperture_value = tag['EXIF ApertureValue']
        info += ' f/' + ("{:.1f}".format(eval(str(aperture_value)))).replace('.0', '')
    if 'EXIF ExposureTime' in tag:
        exposure_time = tag['EXIF ExposureTime']
        info += " " + executeExposureTime(str(exposure_time)) + 's'
    if 'EXIF ISOSpeedRatings' in tag:
        info += ' ISO' + str(tag['EXIF ISOSpeedRatings'])
    return photo_time, make, model, info


def log(log_path, info):
    with open(log_path, mode='a', encoding="utf-8") as file:
        file.write(info)


def compute_size(width):
    new_height = int(float(width) / float(4608) * frame_height)
    font_scala = float(width) / float(4608) * 2
    new_top = int(float(width) / float(4608) * font_top)
    new_middle = int(float(width) / float(4608) * tow_row_middle)
    new_left = int(float(width) / float(4608) * (4608 - 1100))
    new_left1 = int(float(width) / float(4608) * sides_length)
    font_size = int(float(width) / float(4608) * fist_row_font_size)
    return new_height, font_scala, new_top, new_middle, new_left, new_left1, font_size


def exifread_photo(from_path, to_path, log_path):
    photo_time, make, model, info = exif(from_path)
    src_img = cv2.imread(from_path)
    height, width = src_img.shape[:2]
    new_height, font_scala, new_top, new_middle, new_left, new_left1, font_size = compute_size(width)
    result_img = create_blank_image(width, height + new_height)
    result_img[0:height, 0:width] = src_img[0:height, 0:width]
    cv2.imwrite(to_path, result_img)
    image = Image.open(to_path)
    font1 = ImageFont.truetype("***/font.ttf", font_size)
    font2 = ImageFont.truetype("***/font.ttf",
                               font_size * fist_row_font_rate)
    drawer = ImageDraw.Draw(image)

    drawer.text((new_left1, height + new_top), make, fill=(0, 0, 0), font=font1)
    drawer.text((new_left1, height + new_top + new_middle), model, fill=(150, 150, 150), font=font2)

    length1 = computeTextSize(info, font1)
    length2 = computeTextSize(photo_time, font2)
    max_length = max(length1, length2) + new_left1
    drawer.text((width - max_length, height + new_top), info, fill=(0, 0, 0), font=font1)
    drawer.text((width - max_length, height + new_top + new_middle), photo_time, fill=(150, 150, 150), font=font2)
    image.save(to_path)
    if make != '' and os.path.exists('***/logo/' + make + '.png'):
        result_img = cv2.imread(to_path)
        logo_img = cv2.imread('***/logo/' + make + '.png')
        logo_img = transparence_to_white(logo_img)
        height1, width1 = logo_img.shape[:2]
        logo_img = cv2.resize(logo_img, (
            int(float(new_height) * logo_rate / float(height1) * float(width1)), int(float(new_height) * logo_rate)))
        height1, width1 = logo_img.shape[:2]
        left = width - max_length - width1 - int(float(100) / float(4608) * float(width))
        logo_height = int(float(width) / float(4608) * logo_top)
        line_height = int(float(frame_height) / float(300) * line_top)
        line_length1 = int(float(frame_height) / float(300) * line_length)
        result_img[height + logo_height:height + logo_height + height1, left:left + width1] = logo_img
        cv2.line(result_img, (left + width1 + int(float(30) / float(4608) * float(width)), height + line_height),
                 (left + width1 + int(float(30) / float(4608) * float(width)), height + line_height + line_length1),
                 (200, 200, 200), 3)
        cv2.imwrite(to_path, result_img)
    log(log_path, "ok")


if __name__ == "__main__":
    fromPath = (str(sys.argv[1]))
    toPath = (str(sys.argv[2]))
    logPath = (str(sys.argv[3]))
    if fromPath.lower().endswith(".heic"):
        HeicToJpg(fromPath, fromPath + ".jpg")
        fromPath = fromPath + ".jpg"
    exifread_photo(fromPath, toPath, logPath)
