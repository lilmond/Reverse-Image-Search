import os

def main():
    try:
        c_blue = "\u001b[34;1m"
        c_reset = "\u001b[0;0m"

        os.system("")

        while True:
            image_url = input(f"{c_blue}Image URL:{c_reset} ").strip()

            print(
                f"{c_blue}Google:{c_reset} https://lens.google.com/uploadbyurl?url={image_url}\n" \
                f"{c_blue}Yandex:{c_reset} https://yandex.com/images/search?rpt=imageview&url={image_url}\n" \
                f"{c_blue}TinEye:{c_reset} https://tineye.com/search?url={image_url}\n" \
                f"{c_blue}Bing:{c_reset} https://www.bing.com/images/searchbyimage?cbir=sbi&imgurl={image_url}\n\n"
            )
    except KeyboardInterrupt:
        return
        
if __name__ == "__main__":
    main()
