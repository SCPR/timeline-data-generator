# Timeline Data Generator

### About

Queries the KPCC content API and returns a specified number of results as a .csv that is structured and ready for use in [tabletop.js-based timelines](https://github.com/MinnPost/jquery-vertical-timeline) like [this one](http://projects.scpr.org/static/timelines/christopher-dorner-timeline/).

### Setup & Use

The script uses core Python libraries to query KPCC's content API and write the results to a comma-separated file.

That file is imported into a Google spreadsheet, and with some copy-editing and formatted, is ready to power a tabletop.js-based timeline. 

To use the ```timeline-data-generator.py``` script:

* Clone the repository or download and unzip it to a directory on your machine.
* Using terminal, change into the directory and type ```python timeline-data-generator.py``` into your command line.
* You will be asked for a search term and the number of results you'd like to retrieve. Below is an example:

    * **Enter the search term for the KPCC API**: Gov. Jerry Brown
    * **Enter the number of results you'd like from the KPCC API**: 15

* A ```timeline-data-file.csv``` will be output to the directory. The csv file contains the following columns:

    * ```title```: This is the headline of the piece of content.
    * ```date```: This is the date the item took place and is required for sorting purposes. The end user will not see this value. Please note that the date column should contain data in a **Month Day, Year** format. -- **April 25, 2012** so the JavaScript can parse it correctly. If you don't know the date something occurred, we can fudge it for sorting purposes by just entering the first or second day of a month.
    * ```display date```: This is the date the user will see on the timeline. You can format this however it makes sense given the item's context. Sometime we use March 2003, sometimes 2003. It's really a free form text field to explain to the user when something happened.
    * ```media type```: Defaults to image.
    * ```media url```: This is an AssetHost link to the first image found for an article. If an article doesn't have an image associated with it, this value will be blank.
    * ```caption```: This field is the AssetHost caption for the image.
    * ```body```: This field contains the teaser for a piece of content. This should be copy edted or added to.
    * ```read more source```: Defaults to KPCC.
    * ```read more url```: A link to a given piece of content.

* Create a copy of the Timeline template stored in the KPCC DataDesk Google Drive account. Import the csv file into the ```Posts``` sheet. Don't use the contents as is. While this script gets you close, remember that the content should be copy edited and reduced so it works within the timeline format.

* To finish, follow along with the rest of the tutorial outlined on the KPCC webdesk wiki.

* Sit back and relax because you won.

![winner](http://i0.kym-cdn.com/entries/icons/original/000/012/982/post-19715-Brent-Rambo-gif-thumbs-up-imgu-L3yP.gif)

### But what about…

I know what you're thinking. The KPCC timeline has a [config file](https://github.com/SCPR/static-projects/blob/master/timelines/christopher-dorner-timeline/timeline-config.js) that allows you to specify whether to use a Google spreadsheet or a [flat json file](https://github.com/SCPR/static-projects/blob/master/timelines/christopher-dorner-timeline/timeline-data.json) to power a timeline. So why don't we have a flat json file option for this script?

My initial thinking is this is a quick way to get information that can be used in a timeline, not a method of creating a fully-baked, ready-to-roll-and-fit-for-the-public timeline. That said, it could be done and it's something I may work on as time permits.

### Links & Resources

* [Python](http://www.python.org/)
* [tabletop.js](https://github.com/jsoma/tabletop)
* [MinnPost's jquery-vertical-timeline](https://github.com/MinnPost/jquery-vertical-timeline)
* Balance Media's [Timeline](https://github.com/balancemedia/Timeline)