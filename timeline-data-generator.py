import json
import urllib2
import logging
import sys
import csv
import datetime
from datetime import datetime, date

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

def construct_target_url():
    query_input = raw_input("Enter the search term for the KPCC API: ")
    results_limit = raw_input(
        "Enter the number of results you\'d like from the KPCC API: ")
    query_string = query_input.lower().replace(" ", "+")
    csv_file_name = query_input.lower().replace(" ", "-")
    target_url = "http://www.scpr.org/api/v2/content/?types=news,blogs&query=%s&limit=%s" % (
        query_string, results_limit)
    open_json_feed(target_url, csv_file_name)

def open_json_feed(target_url, csv_file_name):
    json_request = urllib2.urlopen(target_url)
    json_data = json.load(json_request)
    write_json_as_timeline_data(json_data, csv_file_name)

def write_json_as_timeline_data(json_data, csv_file_name):
    with open(csv_file_name + ".csv", "wb+", buffering=0) as newCsvFile:
        header_row = [
            "title",
            "date",
            "display date",
            "media type",
            "media url",
            "caption",
            "body",
            "read more source",
            "read more url"
        ]
        dataForCsv = csv.writer(
            newCsvFile, delimiter=",", quoting=csv.QUOTE_ALL)
        dataForCsv.writerow(header_row)
        for data in json_data:
            title = data["title"].encode("ascii", "ignore")
            timeline_date = convert_string_date_for_timeline(
                data["published_at"], "%b %d, %Y")
            display_date = convert_string_date_for_timeline(
                data["published_at"], "%B %d")
            media_type = "image"
            if data["assets"]:
                media_url = data["assets"][0]["full"][
                    "url"].encode("ascii", "ignore")
                try:
                    caption = data["assets"][0][
                        "caption"].encode("ascii", "ignore")
                except:
                    caption = None
            else:
                media_url = None
                caption = None
            teaser = data["teaser"].encode("ascii", "ignore")
            source = "KPCC"
            url = data["permalink"].encode("ascii", "ignore")
            dataForCsv.writerow([
                title,
                timeline_date,
                display_date,
                media_type,
                media_url,
                caption,
                teaser,
                source,
                url
            ])
        newCsvFile.close()

def convert_string_date_for_timeline(input, format):
    string_date = str(input)
    date_list = string_date.split("T")
    date_list = date_list[0].split("-")
    date_object = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    output = datetime.strftime(date_object, format)
    return output

if __name__ == "__main__":
    construct_target_url()
