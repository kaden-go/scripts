import argparse
import requests
import os
import time
import exceptions as e 
from bs4 import *
from urllib.parse import urljoin, urlparse
from tqdm import tqdm
 
URL_PREFIX = "https://"

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL to download images from", required=True)
parser.add_argument("--dir", help="directory to safe all images", required=True)
parser.add_argument("--verbose", help="increase output verbosity", action="store_true")

args = parser.parse_args()

if URL_PREFIX not in args.url:
    #args.url = URL_PREFIX + args.url
    pass

if args.verbose:
    print("Downloading all images from {URL} to {CWD}/{DIR}".format(URL=args.url, CWD=os.getcwd(), DIR=args.dir))

class ImageScraper():
    def __init__(self, url, dir):
        self.url = url 
        self.dir = dir
        self.image_urls = []
        self.count = 0

    def is_valid_url(self):
        """
        Checks whether 'url' is a valid URL
        """
        parsed = urlparse(self.url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def get_images(self):
        """
        Gets all images from specified URL
        """
        soup = BeautifulSoup(requests.get(self.url).content, "html.parser")

        for image in tqdm(soup.findAll("img"), "Extracting images from {URL}".format(URL=self.url)):
            self.count = self.count + 1
            img_url = image.attrs.get("src")
            img_url = urljoin(self.url, img_url)
            self.image_urls.append(img_url)

        return self.image_urls

    def create_dir(self):
        """
        Creates directory to store downloaded images
        """
        current_dir = os.getcwd()
        os.mkdir(path = current_dir + '/' + self.dir)

    def download_images(self):
        """
        Downloads images from url to dir
        """
        count = 0

        for img in self.image_urls:
            r = requests.get(img)
            with open(self.dir + "/" + "image" + str(count), "wb") as f:
                f.write(r.content)
                count = count + 1 


    def get_image_urls(self):
        return self.image_urls

    def get_url(self):
        return self.url

    def get_dir(self):
        return self.dir

    def get_count(self):
        return self.count
    

if __name__ == "__main__":
    i = ImageScraper(args.url, args.dir)

    valid = i.is_valid_url()

    if valid:
        image_urls = i.get_images()
    else:
        raise e.UrlNotValidError("Provided URL is not a valid URL.")
        exit()

    if args.verbose:
        print("Extracted {COUNT} images on {URL}".format(COUNT=i.get_count(), URL=i.get_url()))

    i.create_dir()
    i.download_images()

