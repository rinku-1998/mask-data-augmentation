import cv2
from define_transform import transform
from pathlib import Path
from utils.image_util import load_img, save_img


def run(img_dir: str,
        mask_dir: str,
        save_img_dir: str,
        save_mask_dir: str,
        times: int = 4):

    # 1. 搜尋影像
    img_dirp = Path(img_dir)
    img_paths = img_dirp.rglob('*.jpg')

    for img_path in img_paths:

        # 2. 讀取影像
        mask_path = Path(mask_dir, f'{img_path.stem}_mask.png')
        img = load_img(str(img_path))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mask = cv2.imread(str(mask_path), cv2.IMREAD_GRAYSCALE)

        # 3. 產生資料增強後的影像
        for _ in range(times):

            # 套用資料增強
            transformed = transform(image=img, mask=mask)
            transformed_image = transformed['image']
            transformed_mask = transformed['mask']

            # 存檔
            new_img_path = Path(save_img_dir, f'{img_path.stem}_{_}.jpg')
            new_mask_path = Path(save_mask_dir,
                                 f'{img_path.stem}_{_}_mask.png')
            transformed_image = cv2.cvtColor(transformed_image,
                                             cv2.COLOR_RGB2BGR)
            save_img(transformed_image, str(new_img_path))
            save_img(transformed_mask, str(new_mask_path))


if __name__ == '__main__':

    # 1. 定義參數
    import argparse
    parser = argparse.ArgumentParser(
        description='A tool for generate transformed image and mask')
    parser.add_argument('-ii',
                        '--in_img_dir',
                        type=str,
                        default='./data/imgs',
                        required=False,
                        help='Directory to image files')
    parser.add_argument('-im',
                        '--in_mask_dir',
                        type=str,
                        default='./data/masks',
                        required=False,
                        help='Directory to mask files')
    parser.add_argument('-oi',
                        '--out_img_dir',
                        type=str,
                        default='./data_augmentation/imgs',
                        required=False,
                        help='Directory to output image files')
    parser.add_argument('-om',
                        '--out_mask_dir',
                        type=str,
                        default='./data_augmentation/masks',
                        required=False,
                        help='Directory to output mask files')
    parser.add_argument('-t',
                        '--times',
                        type=int,
                        default=1,
                        required=False,
                        help='times to number to generate per image')

    args = parser.parse_args()

    # 2. 執行
    run(args.in_img_dir, args.in_mask_dir, args.out_img_dir, args.out_mask_dir,
        args.times)
