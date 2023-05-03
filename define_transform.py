import albumentations as A



transform = A.Compose([
    A.HorizontalFlip(p=0.2),
    A.VerticalFlip(p=0.2),
    A.ShiftScaleRotate(rotate_limit=20), 
    A.Perspective(),
    A.GaussNoise(),
    A.HueSaturationValue(), 
    A.CoarseDropout(p=0.2), 
    A.OneOf([A.CropAndPad(percent=0.1)], p=0.2)
])    