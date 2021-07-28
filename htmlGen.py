#!/usr/bin/env python

import markdown
import os


def GenerateHTML(mdPath, htmlPath):
    with os.scandir(path=mdPath) as it:
        for entry in it:
            if entry.name.endswith(".md"):
                with open(entry, "r") as markfile:
                    out = markdown.markdown(markfile.read())
                with open(
                    htmlPath + "/" + entry.name.replace(".md", ".html"), "w"
                ) as outfile:
                    outfile.write(out)


if __name__ == "__main__":
    GenerateHTML("md-posts", "html-posts")
