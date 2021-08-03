import sys
import os

C_BLUE = "\u001b[34;1m"
C_RESET = "\u001b[0;0m"

def clearConsole():
    if sys.platform == "linux":
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")

def main():
    try:
        clearConsole()
        while True:
            image_url = input("Image URL: ")
            google_url = f"https://www.google.com/searchbyimage?image_url={image_url}"
            bing_url = f"https://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl={image_url}"
            yandex_url = f"https://yandex.com/images/search?source=collections&url={image_url}&rpt=imageview"
            tineye_url = f"https://www.tineye.com/search/?&url={image_url}"
            print(f"{C_BLUE}Google Result:{C_RESET} {google_url}\r\n{C_BLUE}Bing Result:{C_RESET} {bing_url}\r\n{C_BLUE}Yandex Result:{C_RESET} {yandex_url}\r\n{C_BLUE}Tineye Result:{C_RESET} {tineye_url}\r\n\r\n")
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
