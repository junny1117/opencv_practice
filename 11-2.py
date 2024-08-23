import cv2


def corner_fast():
    src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        exit()

    # 밝기 차이 임계값으로 60 지정하여 FAST 방법으로 코너 점을 검출, 비최대 억제 수행
    fast = cv2.FastFeatureDetector_create(60)
    keypoints = fast.detect(src)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    for kp in keypoints:
        pt = (int(kp.pt[0]), int(kp.pt[1]))
        cv2.circle(dst, pt, 5, (0, 0, 255), 2)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    corner_fast()