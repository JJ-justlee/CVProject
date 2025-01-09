import threading

import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from saveImage import continueOrNo
from threadsImage import showImage

def weightedImageBlend():
    while True:
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)  # 최상위 설정

        # 사용자로부터 첫 번째 이미지 선택
        file_path1 = askopenfilename(title="Select the first image")
        image1 = cv2.imread(file_path1, cv2.IMREAD_GRAYSCALE)

        # 사용자로부터 두 번째 이미지 선택
        file_path2 = askopenfilename(title="Select the first image")
        image2 = cv2.imread(file_path2, cv2.IMREAD_GRAYSCALE)

        # 두 번째 이미지를 첫 번째 이미지와 동일한 크기로 조정
        image2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

        blended_image = cv2.addWeighted(image1, 0.7, image2_resized, 0.3, 0.0)

        # 이미지 출력 스레드 시작
        image_thread = threading.Thread(target=showImage, args=(blended_image,))
        image_thread.start()

        image_thread.join()

        saveOrNo = input("Do you want to save this image?(Yes or No): ").strip().lower()

        if saveOrNo == 'yes':
            # 새로운 창 생성 및 최상위 설정
            save_window = Tk()
            save_window.withdraw()
            save_window.attributes('-topmost', True)

            save_path = asksaveasfilename(defaultextension=".jpg",
                                          filetypes=[("JPEG files", "*.jpg"),
                                                     ("PNG files", "*.png"),
                                                     ("All files", "*.*")],
                                          title="Save the blended image as")

            # 강제로 창 활성화 및 포커스
            save_window.focus_force()
            save_window.grab_set()

            if save_path:
                cv2.imwrite(save_path, blended_image)
                print(f"Image saved as: {save_path}")

        # 반복 여부 확인
        if not continueOrNo():
            print('이용해주셔서 감사드립니다.')
            break