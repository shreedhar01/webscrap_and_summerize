import webscrap
import summerize

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Alexander_the_Great"
    webscrap.scrape_wikipedia(url)

    a = int(input("input index you want to summerize"))
    summerize.print_summary(a)