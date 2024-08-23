#어파인 변환
import numpy as np
import cv2

def affine_transform():
    src=cv2.imread('test.png')
    if src is None:
        print('Image load failed')
        exit()
    
    rows=src.shape[0]
    cols=src.shape[1]
    
    src_pts = np.array([[0,0],
                        [cols - 1, 0],
                        [cols-1,rows-1]]).astype(np.float32)
    
    dst_pts = np.array([[50,50],
                        [cols - 100, 100],
                        [cols - 50, rows -50]]).astype(np.float32)
    
    affine_mat = cv2.getAffineTransform(src_pts, dst_pts)
    print(affine_mat)
    dst=cv2.warpAffine(src, affine_mat, (0,0))
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()

if __name__ == '__main__':
    affine_transform()