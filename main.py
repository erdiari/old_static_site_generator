#!/usr/bin/env python

import htmlGen
import os


def main():
    # TODO - move these to a config file
    mdPath = "md-posts"
    htmlPath = "html-posts"
    # Generate html files from md files
    htmlGen.GenerateHTML(mdPath, htmlPath)
    # Generate an indexer for html entries
    index = []
    with os.scandir(path=htmlPath) as it:
        for entry in it:
            if entry.name.endswith(".html"):
                index.append(entry.name)
    # create a basic starts page
    start = "<h1> Hello </h1> \n <h2> pages: </h2> \n"
    start += "<ul>"
    for i in index:
        start += "<li> <a href='{}'> {} </a></li>".format(htmlPath + "/" + i, i)
    start += "</ul>"
    with open("index.html", "w") as indexfile:
        indexfile.write(start)


if __name__ == "__main__":
    main()
