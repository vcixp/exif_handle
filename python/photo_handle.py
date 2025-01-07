from PIL import Image


def fill_transparent_with_white(input_image_path, output_image_path):
    image = Image.open(input_image_path)

    if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
        image_data = image.getdata()
        new_data = []

        for item in image_data:
            if item[3] == 0:  # 判断像素是否为透明
                new_data.append((255, 255, 255, 255))  # 将透明像素填充为白色
            else:
                new_data.append(item)

        image.putdata(new_data)
        image.save(output_image_path)
    else:
        print("该图片没有透明通道！")


if __name__ == "__main__":
    # 使用示例
    input_image_path = "./logo/HUAWEI.png"
    output_image_path = "./logo/huawei.png"
    fill_transparent_with_white(input_image_path, output_image_path)
