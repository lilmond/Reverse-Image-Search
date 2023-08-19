import os
import typing

class URLs_Dict(typing.TypedDict):
    Google:str
    Yandex:str
    TinEye:str
    Bing:str

class Invalid_URL_Type(Exception):
    def __init__(self,variable_type):
        self.variable_type=variable_type
    def __str__(self):
        if self.variable_type is None:
            return "No URL has been provied (None)"
        else:
            return f"The variable provided is a {self.variable_type} wich is NOT a string it can't be processed."

def main(image_url:typing.Union[str,None,typing.List[str]]=None) -> typing.Union[URLs_Dict,None,typing.List[URLs_Dict]]:
    if image_url is None:
        try:
            c_blue = "\u001b[34;1m"
            c_reset = "\u001b[0;0m"

            os.system("")

            while True:
                image_url = input(f"{c_blue}Image URL:{c_reset} ").strip()
                URLs = unique_url_to_all(image_url)
                for search_engine_name,url in URLs.items():
                    print(f"{c_blue}{search_engine_name}:{c_reset} {url} \n")
                print("\n")
        except KeyboardInterrupt:
            return
    elif isinstance(image_url,list):
        Transformed_URLS = []
        for URL in image_url:
            Transformed_URLS.append(unique_url_to_all(URL))
        return Transformed_URLS
    else:
        return unique_url_to_all(image_url)


def unique_url_to_all(image_url:str=None) -> URLs_Dict:
    if not isinstance(image_url,str):
        raise Invalid_URL_Type(type(image_url))
    return {"Google":f"https://lens.google.com/uploadbyurl?url={image_url}",
            "Yandex":f"https://yandex.com/images/search?rpt=imageview&url={image_url}",
            "TinEye":"https://tineye.com/search?url={image_url}",
            "Bing":f"https://www.bing.com/images/searchbyimage?cbir=sbi&imgurl={image_url}"}

if __name__ == "__main__":
    main()
