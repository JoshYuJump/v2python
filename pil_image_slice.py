import os
from PIL import Image

# Slice png fomart image
def image_slice(img_path, max_height, index=1, blank_pix=(255, 255, 255, 255)):
    critical = 10.0 / 100
    n = 0
    try:
        i = Image.open(img_path)
    except Exception, e:
        print e
        return n

    (i_width, i_height) = i.size    
    
    if i_height < max_height:
        return n
    for h in range(max_height, 0, -1):
        blank_pix_num = 0
        for w in range(0, i_width):
            if i.getpixel((w, h)) == blank_pix:
                blank_pix_num += 1
        # slice now        
        if (float(blank_pix_num) / i_width) < critical:
            a = i.crop((0, 0, i_width, h + 1))
            b = i.crop((0, h, i_width, i_height))
            a.save(img_path[:-4] + '_' + str(index) + '.png')
            b.save(img_path[:-4] + '_' + str(index + 1) + '.png')
            os.remove(img_path)
            n += 1
            image_slice(img_path[:-4] + '_' + str(index + 1) + '.png', max_height, index + 1)
            return n


if __name__ == '__main__':
    # 1728 is the real critical height
    print image_slice('C:\\Users\\byux\\Pictures\\1.png', 1700)
