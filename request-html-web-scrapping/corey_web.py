import csv
from requests_html import HTML, HTMLSession

csv_file = open("scrape.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Headline", "Summary", "Video"])

session = HTMLSession()
res  = session.get("https://coreyms.com/")

articles = res.html.find("article")

for article in articles:

    headline = article.find(".entry-title-link", first=True).text
    summary = article.find(".entry-content p", first=True).text

    try:
        vid_src = article.find("iframe", first=True).attrs["src"]
        vid_id = vid_src.split("/")[4]
        vid_id = vid_id.split("?")[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}" 
    except AttributeError:
        yt_link = None
    except PermissionError:
        print("File already exists..")

    csv_writer.writerow([headline, summary, yt_link])
    
print("Successfully Compiled..")
csv_file.close()
