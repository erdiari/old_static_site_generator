#!/usr/bin/env python

import markdown
import os


def main():
    # TODO - move these to a config file
    outputPath = "docs"
    mdPath = "md-posts"
    htmlPath = "posts"
    skeletonPath = "skeletons"
    # Generate html files from md files
    with open(skeletonPath + "/post_preamble.html", "r") as pre:
        start = pre.read()
    with open(skeletonPath + "/post_postamble.html", "r") as post:
        post = post.read()
    # Generate an indexer for html entries
    index = []
    with os.scandir(path=mdPath) as it:
        for entry in it:
            if entry.name.endswith(".md"):
                outputName = entry.name.replace(".md", ".html")
                with open(entry, "r") as markfile:
                    out = markdown.markdown(markfile.read())
                with open(
                    outputPath + "/" + htmlPath + "/" + outputName, "w"
                ) as outfile:
                    index.append(outputName)
                    outfile.write(start + out + post)
    # create a basic starts page
    with open(skeletonPath + "/index_preamble.html", "r") as pre:
        start = pre.read()
    start += "<ul>"
    for i in index:
        start += "<li> <a href='{}'> {} </a></li>".format(htmlPath + "/" + i, i)
    start += "</ul>"
    with open(skeletonPath + "/index_postamble.html", "r") as post:
        start += post.read()
    with open(outputPath + "/" + "index.html", "w") as indexfile:
        indexfile.write(start)


if __name__ == "__main__":
    main()
