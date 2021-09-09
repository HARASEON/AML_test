from selenium import webdriver
import time
import os
import getopt
import sys

def usage():
    print("-------------------------------------------------usage-------------------------------------------------------------------------")
    print("python3 crawler.py [-e search engine] [-t search word]")
    print("python3 crawler.py [--engine search engine] [--target search word]")
    print("-------------------------------------------------------------------------------------------------------------------------------")

def search_engine_list():
    print("-------------------------------------------------search engine list------------------------------------------------------------")
    print("|ahmia: python3 crawler.py -e ahmia -t search word                                                                            |")
    print("|torch: python3 crawler.py -e torch -t search word                                                                            |")
    print("|duckduckgo: python3 crawler.py -e duckduckgo -t search word                                                                  |")
    print("|haystack: python3 crawler.py -e haystack -t search word                                                                      |")
    # print("|recon: python3 crawler.py -e recon -t search word                                                                            |")
    # print("|dread: python3 crawler.py -e dread -t search word                                                                            |")
    print("|onionland: python3 crawler.py -e onionland -t search word                                                                    |")
    print("-------------------------------------------------------------------------------------------------------------------------------")

def connection():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("-disable-notifications")
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome('/home/hr/washer/chromedriver', chrome_options=chrome_options)

    if engine == "haystack":
        query = "http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + text

    elif engine == "ahmia":
        query = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q=" + text

    elif engine == "torch":
        query = "http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/search?query="+ text + "&action=search"

    elif engine == "duckduckgo":
        query = "https://duckduckgo.com/?q=" + text + "&ia=web"

    #elif engine == "recon":
        #query = "http://recon222tttn4ob7ujdhbn3s4gjre7netvzybuvbq2bcqwltkiqinhad.onion/search/?q=" + text

    #elif engine == "dread":
        #query = "http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/search/?q=" + text
    
    elif engine == "onionland search engine":
        query = "http://3bbad7fauom4d6sgppalyqddsqbf5u5p56b5k5uk2zxsy3d6ey2jobad.onion/search?q=" + text

    else:
        usage()
        search_engine_list()
        sys.exit()

    driver.get(query)
    #time.sleep(15)

def bypasscaptcha ():


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "he:t:", ["help", "engine=", "text="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    global engine
    global text

    engine = None
    text = None

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            bypasscaptcha()
            sys.exit()
        elif o in ("-e", "--engine"):
            engine = a
        elif o in ("-t", "--text"):
            text = a

        else:
            usage()
            search_engine_list()
            sys.exit()

    connection()


if __name__ == "__main__":
    main()
