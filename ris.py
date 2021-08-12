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
            results = {}
            results["Google"] = f"https://www.google.com/searchbyimage?image_url={image_url}"
            results["Yandex"] = f"https://yandex.com/images/search?source=collections&url={image_url}&rpt=imageview"
            results["TinEye"] = f"https://www.tineye.com/search/?&url={image_url}"
            results["Bing"] = f"https://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl={image_url}"
            for result in results:
                print(f"{C_BLUE}{result}: {C_RESET}{results[result]}")
            print(f"\r\n")
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
