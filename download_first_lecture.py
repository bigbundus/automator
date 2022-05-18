import pyautogui
import time

from automate_utils import center_of_box

def find_and_click_next_lecture(button_image):
    next_lec_loc = pyautogui.locateOnScreen(button_image)
    next_lec_x, next_lec_y = center_of_box(next_lec_loc)
    pyautogui.moveTo(next_lec_x, next_lec_y, duration = 1.8)
    pyautogui.click(next_lec_x, next_lec_y)
    print("clicked on continue button")
    time.sleep(4)


def download_single_lecture():
    #pyautogui.displayMousePosition()

    # move to center of screen
    pyautogui.moveTo(1000, 600, duration = 1)

    # what if there is no download button?
    download_button_image = "am_download_button.png"
    complete_continue_button_image = "am_complete_continue_button.png"

    download_button_present = False
    scroll_attempts = 0
    max_scroll_attempts = 3

    while not download_button_present:
        # scroll down to include the download button
        pyautogui.scroll(-300)
        scroll_attempts += 1
        time.sleep(2)

        download_loc = pyautogui.locateOnScreen(download_button_image)
        if download_loc is not None:
            print("download button found!")
            download_button_present = True

        if scroll_attempts > max_scroll_attempts:
            print("no scroll button found -> complete + continue")
            find_and_click_next_lecture(complete_continue_button_image)
            return

    # eh, not a good system - should just go click on complete and continue if not found...

    download_x, download_y = center_of_box(download_loc)
    pyautogui.moveTo(download_x, download_y, duration = 1.8)
    print("download here...")
    time.sleep(3)
    print("downloading complete, going to next page")
    find_and_click_next_lecture(complete_continue_button_image)


download_single_lecture()
download_single_lecture()
download_single_lecture()
