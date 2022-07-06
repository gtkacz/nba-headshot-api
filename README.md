![NBA Logo](https://cdn.nba.com/logos/leagues/logo-nba.svg)
<br><br>

# NBA Headshot API

## Overview
Welcome to nba-headshot-api: an open-source, free-to-use API for retrieving active NBA players' official headshots from nba.com.

## How to use
This API has URIs prefixed with `https://xxx.com/players/` and is structured as described below. There is currently no rate limit.

Stories, comments, jobs, Ask HNs and even polls are just items. They're identified by their ids, which are unique integers, and live under `/v0/item/<id>`.

All items have some of the following properties, with required properties in bold:

Field | Description
------|------------
**id** | The item's unique id.
deleted | `true` if the item is deleted.
type | The type of item. One of "job", "story", "comment", "poll", or "pollopt".
by | The username of the item's author.
time | Creation date of the item, in [Unix Time](http://en.wikipedia.org/wiki/Unix_time).
text | The comment, story or poll text. HTML.
dead | `true` if the item is dead.
parent | The comment's parent: either another comment or the relevant story.
poll | The pollopt's associated poll.
kids | The ids of the item's comments, in ranked display order.
url | The URL of the story.
score | The story's score, or the votes for a pollopt.
title | The title of the story, poll or job. HTML.
parts | A list of related pollopts, in display order.
descendants | In the case of stories or polls, the total comment count.

For example, a story: https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty