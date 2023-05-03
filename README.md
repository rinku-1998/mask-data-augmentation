# mask-da

Mask 影像資料集的資料增強工具

## 安裝

```shell
# poetry
poetry install # 正式
poetry install --dev # 開發

# pip
pip install -r requirements.txt # 正式
pip install -r requirements-dev.txt # 開發
```

## 使用說明

- 執行步驟

1. (可選)定義資料增強，可以修改 `define_transform.py`，並參考 [Albumentations - A list of transforms and their supported targets](<(https://albumentations.ai/docs/getting_started/transforms_and_targets/)>) 的說明網頁。
1. 將影像與 Mask 分別放到 `data/imgs` 與 `data/masks` 資料夾下
1. 執行 `generate.py`

- 參數說明

| 參數名稱                | 型態 | 必填 | 預設值                    | 說明               |
| ----------------------- | ---- | ---- | ------------------------- | ------------------ |
| `-ii`, `--in_img_dir`   | str  |      | ./data/imgs               | 影像目錄           |
| `-im`, `--in_mask_dir`  | str  |      | ./data/masks              | Mask 目錄          |
| `-oi`, `--out_img_dir`  | str  |      | ./data_augmentation/imgs  | 影像輸出目錄       |
| `-om`, `--out_mask_dir` | str  |      | ./data_augmentation/masks | Mask 輸出目錄      |
| `-t`, `--times`         | int  |      | 1                         | 每張照片產生的張數 |
