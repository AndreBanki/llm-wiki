---
title: "You Don’t Need a PhD to Build an Ontology"
source: "https://medium.com/@irregularbi/you-dont-need-a-phd-to-build-an-ontology-f50ff00b6db9"
author:
  - "[[Ralfo Becher]]"
published: 2026-04-01
created: 2026-05-03
description: "More"
tags:
  - "clippings"
---
I keep running into the same ridiculous problem. Every few months, I need to build an ontology: define some classes, add properties, maybe put together a SKOS vocabulary. And every single time, I end up in exactly the same place: staring at a tool clearly designed for people who spend their entire professional lives thinking about Description Logic, clicking through menus and trying to remember where they hid the one thing I actually need.

To be fair, these tools are not bad. They are built for serious ontology engineers doing serious ontology engineering all day long. Fine. Good for them. But that is not me. I do not want a philosophical experience. I want to create a sensible class hierarchy, add properties and annotations, and export a valid Turtle without needing a seminar first.

So eventually I stopped grumbling about it and built something.

## OrionBelt Ontology Builder

is a browser-based ontology editor built with Streamlit and rdflib. You install it with pip, run one command, and then you are working. No circus, no elaborate setup, no unnecessary drama.

It covers the things you would expect: classes, properties, individuals, restrictions, and annotations. You can build hierarchies, rename entities without breaking references, and import or export in Turtle, RDF/XML, JSON-LD, and several other formats.

That part is useful, obviously. But the things I spent extra time on were the parts that kept irritating me in other tools.

One of them is bulk operations. If I need to create 30 classes, I do not want to fill in the same form 30 times like some sort of office punishment. In OrionBelt, you paste in the names, either one per line or as CSV, and the classes are created. The same works for properties and individuals.

Another is undo. Actual undo. Not the fake kind where the software effectively tells you to close everything, reopen it, and reflect on your life choices. Every change creates a checkpoint. If you try to delete a class, the tool shows you what depends on it before anything happens. Bulk operations roll back as a single step, which is how it should work in the first place.

Then there are imports. I have lost count of how many times I imported a file into some ontology editor only to discover later that it had quietly overwritten half the work. Wonderful. OrionBelt shows a full diff before anything is applied: what is new, what conflicts, and which prefixes change. You decide how to merge it. You can even download a report before applying the import. It sounds excessive until the first time it saves you from a complete mess.

## The SKOS Part

A lot of my work involves controlled vocabularies, not just OWL class hierarchies, so there is a dedicated SKOS page as well. You can build concept schemes, manage broader and narrower relationships, and the tool handles the inverse triples for you, because there is no reason to make that more tedious than it already is.

There is also validation for common problems, including cycles and missing labels. I included a sample geography thesaurus with around a hundred concepts, so there is something realistic to work with immediately, instead of the usual empty screen that politely asks you to invent everything from scratch.

## A Few Other Things Worth Mentioning

There is a graph visualization that is actually useful for navigation. Click a node to jump straight to the editor for that entity. In a larger ontology, this is much faster than scrolling through long lists and pretending that counts as a workflow.

There is also a source view that shows the raw Turtle with syntax highlighting. It is read-only because edits should go through the UI, but it is handy when you want to verify that what you built is, in fact, what you meant to build.

The validation is designed to be informative rather than theatrical. Instead of dumping “47 warnings” on you and calling it a day, it tells you what is wrong: this class is orphaned, that property has no domain, these concepts have a broader-narrower cycle, and so on. If you need reasoning, OWL-RL is built in.

There are also five starter templates: organization, product catalog, events, people, and a SKOS thesaurus. So no, you do not always have to begin with a blank ontology and a vague sense of irritation.

## What It Is Not

This is not Protégé.

Protégé does many things OrionBelt does not even try to do, including full Description Logic support, SWRL, and more complex axiom modeling. If that is what you need, then use Protégé. It is excellent software.

OrionBelt is for a different situation. It is for when you need to build a clean ontology, move quickly, maybe share it with colleagues, and not waste the first hour just getting the tool into a usable state.

## If You Want to Try It

There is a live version at [orionbelt.streamlit.app](http://orionbelt.streamlit.app/), so you can try it without installing anything.

If you want to run it locally:

```c
pip install orionbelt-ontology-builder
streamlit run app.py
```

The code is on [GitHub](https://github.com/ralfbecher/orionbelt-ontology-builder).

There is also a companion project, [OrionBelt Analytics](https://github.com/ralfbecher/orionbelt-analytics), which generates ontologies from database schemas such as PostgreSQL, Snowflake, and Dremio. That is useful when you are trying to get from relational data to a knowledge graph without doing everything by hand, as if it were still 2009.

If you try it and something breaks, open an issue. And if it saves you an afternoon, I would be very happy to hear about that, too.

*Ralf Becher is the creator of OrionBelt Ontology Builder, OrionBelt Analytics, and OrionBelt Semantic Layer. Connect on* [*LinkedIn*](https://linkedin.com/in/ralfbecher) *or explore the projects on* [*GitHub*](https://github.com/ralfbecher)*.*