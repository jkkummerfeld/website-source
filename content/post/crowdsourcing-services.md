+++
title = "Crowdsourcing Services"
date = 2019-04-14T10:49:35-04:00
draft = false

summary = "A range of services exist for collecting annotations from paid workers. This post gives an overview of a bunch of them."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["crowdsourcing"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Crowdsourcing, collecting annotations of data from a distributed group of people online, is a major source of data for AI research.
The original idea involved people doing it as volunteers (e.g. Folding@home) or as a byproduct of some other goal (e.g. reCAPTCHA), but most of the data collected in AI today is from paid workers.
Recently, [Hal Daumé III](http://users.umiacs.umd.edu/~hal/) mentioned on [Twitter](https://twitter.com/haldaume3/status/1113889907586535425) that Figure Eight, a paid crowdsourcing service, had removed their free licenses for academics, and asked for alternatives.
A bunch of people had suggestions which I wanted to record for my own future reference, hence this blog post.

These fell into a few categories:

- Crowd providers, which directly connect with workers.
- Annotation tools, which are designed to integrate with crowd providers (or your own internal workers).
- Crowd enhancers, which provide a layer on top of the providers that adds features (e.g. active learning, nice templates, sophisticated workflows).

I decided not to break the list into parts because it was sometimes unclear whether a service was using their own crowd or providing a layer over another, but I have roughly sorted them.
Where possible I have included pricing, though some services did not make it easy to find.
Take note of the description in each case because the data collected varies substantially.
Also note that many tasks can be structured as a classification task (e.g. "Is this coreference link correct?"), making many of these services more flexible than the 'text classification' label below may seem (though structuring your task so costs don't explode may require some thought).

- [Mechanical Turk](https://www.mturk.com/), a small set of templates and the option to define a web UI that does whatever you want. Cost is a 20% fee on top of whatever you choose to pay workers (though note it jumps to 40% if you have more than 10 assignments for a HIT!).
- [Figure Eight](https://www.figure-eight.com/) (included for completeness, did not investigate further due to the cost)
- [Hybrid](http://www.gethybrid.io/), seems to be any task you can define in text (including with links?). 40% fee, though there is a [discount](http://www.gethybrid.io/faq) of some type for academic and non-profit institutions.
- [Prolific](https://prolific.ac/), seems to be that you just provide a link to a site for annotations (originally intended for survey research). 30% fee. Last year they had a [research grant](https://blog.prolific.ac/announcing-2018-junior-grant-winners/) program.
- [Gorilla](https://gorilla.sc/), designed for social science research, but could be used for any classification or free text task. Costs $1.19 / response, though note that you construct a questionnaire with a series of questions. There are also [discounts](https://gorilla.sc/support/reference/subscription-FAQ#subscription-types) available when collecting thousands of responses.
- [Scale](https://scale.ai/), classification tasks for 8c / annotation. There is an academic program, but details are not available online (mentioned [here](https://twitter.com/umbrant/status/1114312024970764290)).
- [Amazon SageMaker Ground Truth](https://aws.amazon.com/sagemaker/groundtruth/), text classification for 8c / label, decreasing after 50,000 annotations + a workflow fee of 1.2c / label.
- [iMerit](https://imerit.net/), NER, classification, and sentiment tasks. When used on the Amazon Marketplace they are 5 dollars / hour (India based workers) or 25 (US based workers).
- [LegionTools](https://www.cromalab.net/LegionTools/), an interface for mechanical turk that handles integration with their APIs. Designed particularly for real-time systems. Free and self-host-able.
- [Prodigy](https://prodi.gy/), span classification (e.g. NER), multiple choice questions (which can be used to do a wide range of tasks), and relations (see [examples](https://prodi.gy/features/)). Cost is whatever you pay a crowd provider + $390 for a lifetime license, and $10k for a university-wide lifetime license, though they also often give free licenses to academics. One distinctive property is that you download and run it yourself, providing complete control over your data.
- [LightTAG](https://www.lighttag.io/), span classification and links. Cost is 1c / annotation + the cost from a crowd provider, but there is an academic license that makes it free.

