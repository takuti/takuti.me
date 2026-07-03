---
categories: [Design, Society & Business]
series: [ab, product]
date: 2026-07-03
lang: en
title: Developer's Guide to Building E-Learning Solutions in Resource-Constrained
  Environments
lastmod: '2026-07-03'
---

Knowledge and skills are the power. One can be self-reliant and seize a brighter future with the right capacity, even without status and wealth.

Yet, its foundation &mdash; education &mdash; is extremely fragile and a prime example of today's global inequality.

- Too many students over teachers.
- Low relevance of the content to learners' reality.
- Limited choices due to financial and geographical hurdles.

Receiving quality education is still a privilege in many parts of the world.

To fill the gap, many development organizations see hope in ICT for its scalability and cost-effectiveness. And some come up with the idea of mobile learning applications: the use of portable digital devices to deliver training programs remotely.

However, I've witnessed common problems in project sustainability in the field, especially in rural communities where there's a greater need for development support; that is, mobile learning solutions do not penetrate to remote users as efficiently as developers hoped, or can even be abandoned at an incomplete state, for practical constraints in connectivity, literacy, and local contexts.

To ensure long-term "real" success of such projects, here is the practical guide I drew from my experience. Starting from today, let's incorporate them into our interventions *by design.*


### Rule 1. Be offline first

It's about technological simplicity.

As soon as developers start designing e-learning applications, they'll propose features like: user account, usage tracking, personalization, multimedia content (videos and PDFs), assessments, AI chatbot, and student-student or student-teacher interaction, because the industry examples like [Coursera](https://www.coursera.org) and [Udemy](https://www.udemy.com/) teach them how mobile learning should be.

But keep in mind that [one in four persons in the world still doesn't have access to the internet](https://data.worldbank.org/indicator/IT.NET.USER.ZS), while many of the anticipated features require a decent internet connection. In fact, the offline population is dominant in many low-income countries and can even account for more than 80% of the country's total population.

So, your "users" won't have infrastructure to enjoy the application's fancy features, making it a wasteful investment.

However, at the same time, [mobile phones are becoming more accessible](https://www.itu.int/itu-d/reports/statistics/2025/10/15/ff25-mobile-phone-ownership/) and show higher penetration globally than the internet. Wider availability of feature phones and affordable smartphones vs. expensive data bundles could explain the trend.

Thus, although e-learning is promising, people are not ready in terms of internet access, even if they have mobile phones.

Here, I recommend intervening in an offline-friendly way. It could mean delivering educational content through USSD (["low-tech" approach](https://ab.takuti.me/p/celebrating-low-tech-applications)), or building an application as a [progressive web application](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/What_is_a_progressive_web_app) (PWA) to minimize the dependency on connectivity.

No matter how sophisticated and state-of-the-art your solution may be, it's pointless if target populations cannot access it.

### Rule 2. Design for low literacy

Next, make the user interface and experience (UI/UX) as straightforward as possible.

Not everyone can read, write, do the math, and use digital devices as fluently as you can. Globally, the [adult literacy rate is still far from 100%](https://data.worldbank.org/indicator/SE.ADT.LITR.ZS), and in Sub-Saharan Africa, I've seen many individuals who have difficulty in some or all of the abilities.

They may be able to read a simple paragraph or use computer/smartphone to watch YouTube videos. But it doesn't mean they can comprehend full educational materials written in English, or work on Google Search to navigate between various pieces of information. There is a huge gap between passive consumers and active users, so developers had better optimize solutions for the former.

For mobile learning applications, this could mean:

- Eliminating all the "nice-to-have" features, like user registration and personalization
- Having a clear, one-way navigation to the learning journey rather than making it open-ended
- Sticking with simple vocabulary and sentence structures, i.e., avoid lengthy texts with jargons
- Making content bite-sized, e.g., 3-5 sentences per topic
- Using images to give visual clues
- Localizing content to their own language

We need to cultivate a "less is better" mindset to effectively convey essential knowledge to those who are in urgent situations. So, please spend more time on *what NOT to include* in the application than on adding more.

### Rule 3. Build in agile

Lastly, we need to co-develop an application *with* target audiences based on local needs and seeds.

Not all education programs are equally effective, and regardless of design choice, technology alone is extremely fragile. That is, we should optimize our approach for the local context. I've discussed the problem in [here](/note/digital-divide/) and [there](/note/computer-education-in-malawi/) in the context of digital skills development.

Our task is to deliver not only workable but also relevant educational applications.

In practice, developers should work in an agile manner. It is an iterative, user-centred approach to product development, and the principle forces us to build a tailored solution incrementally through prototypes and feedback.

Key activities include:

- In-field user engagements to vividly capture their problems and build solid hypotheses, rather than assuming based on common senses
- Rapid prototyping, possibly with AI coding agents to alleviate resource constraints on the developer side
- Validation at a small field experiment, letting a handful of real users try working software
- Fine-tuning the design and content based on the feedback to better address the user's problem
- Responsive change management for phased onboarding and long-term adoption

On the contrary, development projects often aim to achieve something big in a one-size-fits-all, one-shot manner. This is likely due to the tight budget and timeline, as well as the complexity of stakeholder coordination; these projects are often backed by international nonprofits, government bodies, and multilateral organizations, and they tend to live in more political environments that are far from firsthand insights.

So, an agile approach may not exactly fit how your organization operates. Yet, at an individual activity level, it's still possible for us to stay close to the field and shape up a deliverable in a collaborative, participatory manner. Eventually, it starts with shifting the developer's mindset.
