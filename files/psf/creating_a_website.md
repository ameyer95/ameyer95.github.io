---
title: 'PSF 840 Week 9 - Create an academic website'
date: 2023-10-31
permalink: /psf/website/
layout: singlefull
---

## Why do I need an academic website?
It presents you & your research to the world, making you more visible. It's especially useful for applying to jobs.
I know in my field (computer science), it's basically assumed that all grad students should have a website. From Googling/searching Twitter, I think it's valued in other STEM fields, too! 

### What should go on the website?
[This document](https://docs.google.com/document/d/12AHVGVTnWkIPC-7XmEuHkXS0m7opXHDKSHffz2uvIXo/) has some ideas about what should go on a website (and other tips on having an online presence as a grad student). TLDR, you need your name, educational background and current program, advisor's name, your projects, and your publications.

## The basics
To make a website you need two things: the content, and the hosting.

Possible hosting sites include GitHub pages, Google Sites, Wix, Wordpress, and Weebly. You can also build your website with any of these tools and then host it on a custom domain (e.g., yourname.com), but that is not free.  GitHub pages requires some coding, while the other sites are all no-code.

I'm including instructions for **Google Sites** because the UI was most intuitive to me, and for **GitHub pages** because that's what I use.

## Instructions for Google Sites
Go to [Google Sites](sites.google.com). I recommend using your personal account, not your UW account so that you maintain access even after graduating.

More instructions are available at [this website I made](https://sites.google.com/view/psf840creatingawebsite/home).

## Instructions for GitHub
These are very simplified instructions, intended to minimize the amount of coding that's required. If you already use Git, and/or want to learn it, I recommend following [these instructions](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll). Then, you can skip to Step 5.

> This is a simplified workflow and not how people normally use GitHub. It's fine for these purposes, just be aware of that in case you ever need to use git in the future

See [https://github.com/spookypancakes/spookypancakes.github.io](https://github.com/spookypancakes/spookypancakes.github.io) for an example website and some more tips.

1. Create a [GitHub](https://github.com/) account. Choose your username carefully: your website URL will be **username**.github.io. 

2. Create a public GitHub repository called **username**.github.io

3. Download [this file](https://annapmeyer.github.io/files/Archive.zip), and unzip it.

4. Create a new directory on your computer called **username**.github.io and move all of the files you just downloaded into this directory. 

5. Edit the files!

    * `_config.yml` Edit lines 16, 17, 18 (optional), 22, and 23. If you don't have twitter, you can replace the username on line 22 with "". 
    * `index.md` Add any information you want on the homepage.
    * `cv.md` If you want to include a link to a PDF version of your CV,
        * Move a copy of your CV to the directory with the other files.
        * Edit lines 7,8, and 9 of `cv.md` to have the correct URL (update both your username and the PDF name)
        * Also make sure to delete `cvplaceholder.pdf` - you don't need it anymore. 
        * If you *don't* want to include your CV, delete both `cvplaceholder.pdf` and `cv.md`. 
    * `teaching.md` I included this as a placeholder for teaching or anything else you want a page for. You'll need to updates the content (line 7-end), and also the header (lines 3 and 4) if you want the page to have a different title. If you don't want this page, you can just delete it. If you want additional subpages, copy the contents into a new file.

6. Upload all files to your GitHub repository:
* Navigate to the repository (will be at github.com/username/username.github.io)
* Click Add File ->  Upload Files -> Commit changes
* Make sure the website is live: Click Settings --> Pages and there should be a link to your page at the top! It might take up to 10 minutes from committing changes for them to take effect. 

7. By default, your repository will be public and your website will be available to the world! If you don't want that, you can change the repository to private (Settings -> General -> Danger Zone -> Change Repository Visibility). the downside is that you are not able to test changes and see what the website looks like without paying for GitHub premium.
* The way to get around this is to set up a development environment locally. I can help if you're interested, or see the webpage linked at the top of these instructions.

8. If you want to make changes to the website content, just update the appropriate files and re-upload them to GitHub.