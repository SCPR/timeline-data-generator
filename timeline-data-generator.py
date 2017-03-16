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


def _init(query, limit):
    search = query.lower().replace(" ", "+")
    csv_file_name = query.lower().replace(" ", "-")
    url = build_search_url(search, limit)
    json_data = retrieve_json_from(url)
    create_csv_from(json_data, csv_file_name)


def build_search_url(search, limit):
    target_url = "http://www.scpr.org/api/v3/articles?types=news,blogs&query=%s&limit=%s" % (search, limit)
    return target_url


def retrieve_json_from(url):
    json_request = urllib2.urlopen(url)
    json_data = json.load(json_request)
    return json_data


def create_csv_from(json_data, csv_file_name):
    with open(csv_file_name + ".csv", "wb+", buffering=0) as new_csv:
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
        csv_object = csv.writer(new_csv, delimiter=",", quoting=csv.QUOTE_ALL)
        csv_object.writerow(header_row)
        for data in json_data["articles"]:
            title = data["title"].encode("ascii", "ignore")
            timeline_date = convert_string_date_for_timeline(data["published_at"], "%b %d, %Y")
            display_date = convert_string_date_for_timeline(data["published_at"], "%B %d")
            media_type = "image"
            if data["assets"]:
                media_url = data["assets"][0]["full"]["url"].encode("ascii", "ignore")
                try:
                    caption = data["assets"][0]["caption"].encode("ascii", "ignore")
                except:
                    caption = None
            else:
                media_url = None
                caption = None
            teaser = data["teaser"].encode("ascii", "ignore")
            source = "KPCC"
            url = data["public_url"].encode("ascii", "ignore")
            csv_row = [
                title,
                timeline_date,
                display_date,
                media_type,
                media_url,
                caption,
                teaser,
                source,
                url
            ]
            logger.debug(csv_row)
            csv_object.writerow(csv_row)


def convert_string_date_for_timeline(input, format):
    string_date = str(input)
    date_list = string_date.split("T")
    date_list = date_list[0].split("-")
    date_object = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    output = datetime.strftime(date_object, format)
    return output


if __name__ == "__main__":
    query_input = raw_input("Enter the search term for the KPCC API: ")
    results_limit = raw_input("Enter the number of results you\'d like from the KPCC API: ")
    _init(query_input, results_limit)
