---
layout: archive
title: "" # TO DO - once I have publications, change title to publications :)
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

Non-peer reviewed and unpublished work
======

{% for post in site.unpublished reversed %}
  {% include archive-single.html %}
{% endfor %}