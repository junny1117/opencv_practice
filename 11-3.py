import cv2

def keypoint_matching():
    src1 = cv2.imread('box.png', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('box_in_scene.png', cv2.IMREAD_GRAYSCALE)
    if src1 is None or src2 is None:
        print('Image load failed!')
        return
    orb = cv2.ORB_create()
    keypoints1, desc1 = orb.detectAndCompute(src1, None)
    keypoints2, desc2 = orb.detectAndCompute(src2, None)
    print('desc1.shape:', desc1.shape)
    print('desc2.shape:', desc2.shape)

    matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)
    matches = matcher.match(desc1, desc2)
    dst = cv2.drawMatches(src1, keypoints1, src2, keypoints2, matches, None)

    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

def good_matching():
    src1 = cv2.imread('box.png', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('box_in_scene.png', cv2.IMREAD_GRAYSCALE)
    if src1 is None or src2 is None:
        print('Image load failed!')
        return

    orb = cv2.ORB_create()
    keypoints1, desc1 = orb.detectAndCompute(src1, None)
    keypoints2, desc2 = orb.detectAndCompute(src2, None)

    matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)
    matches = matcher.match(desc1, desc2)
    matches = sorted(matches, key=lambda x: x.distance)
    good_matches = matches[:50]
    dst = cv2.drawMatches(src1, keypoints1, src2, keypoints2, good_matches, None,
                          flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    keypoint_matching()
    good_matching()