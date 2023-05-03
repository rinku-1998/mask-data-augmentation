import cv2
import os
import numpy as np
from pathlib import Path
from typing import Optional


def load_img(img_path: str) -> Optional[np.ndarray]:
    """載入圖片

    Args:
        img_path (str): 影像路徑

    Raises:
        e: 全域例外

    Returns:
        Optional[np.ndarray]: 影像ndarray
    """

    # 1. 使用OpenCV直接讀取
    try:
        img = cv2.imread(img_path)
        if img is not None:
            return img
    except Exception as e:
        raise e

    # 2. 從numpy讀取後轉檔(適用中文路徑)
    np_ary = np.fromfile(img_path, dtype=np.uint8)
    img = cv2.imdecode(np_ary, -1)
    if img is not None:
        return img

    return None


def save_img(img: np.ndarray, save_path: str) -> None:
    """儲存圖片

    Args:
        img (np.ndarray): 影像ndarray
        save_path (str): 儲存路徑
    """

    # 1. 檢查路徑
    if not Path(save_path).parent.exists():
        os.makedirs(Path(save_path).parent)

    # 2. 寫入
    cv2.imwrite(str(save_path), img)
