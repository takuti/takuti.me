---
categories: [Data Science & Analytics, Business]
series: [malawi]
date: 2023-09-29
lang: en
title: 'Dilemma over "Best Practice": How We Could Develop Data Protection Practices
  in Malawi'
images: [/images/data-protection-law-in-malawi-2023/me-speaking.jpg]
keywords: [protection, malawi, privacy, data, law, audiences, policy, standards, digital,
  increases]
recommendations: [/note/digital-malawi-2023/, /note/relativize-and-contextualize/,
  /note/volunteering-in-malawi/]
---

Here in southeastern Africa, I see [Malawi's digital transformation](/note/digital-malawi-2023/) is still immature and yet to be caught up in many aspects. As a software developer volunteering in the country, one of the immediate questions I came up with was about data privacy. Unfortunately, while the use of digital technologies is slowly but certainly progressing in various sectors, data governance is rarely spoken as far as I can see. Let me think about what I might do if I were a Malawian service provider who lets users install an application to their phones, collects and stores data digitally for analytics purposes, or launches a web portal for businesses.

### The basics

Importantly, as [GDPR](https://gdpr.eu/), [CCPA](https://oag.ca.gov/privacy/ccpa), or any regional regulation define, it's not a matter of where you (developer; service provider) are physically present. It's more of who uses your service from where, and how their data is stored and processed. In that sense, we first need to be clear about the target audiences and why we collect their data for what purposes. Then, if the audiences do include people accessing the service from a certain country, that's where we should double-click their local regulations.

It should be noted that it's not wise to simply assume "everyone" is a group of audiences. On the one hand, when it comes to data protection policy-making, it is likely true that the more strict, the safer at a global scale. However, at the same time, it usually comes with the cost of complying with regulations e.g., by receiving legal consultations, designing and maintaining data infrastructure as regulated, and providing a certain set of features to end users. Yahoo! Japan, for example, [stopped providing their service in Europe in early 2022](https://www.theverge.com/2022/2/1/22911965/yahoo-japan-europe-offline-regulations-compliance-gdpr) due to such cost implications. Your ambiguous definition of audiences not only [makes your product "bad"](/note/foundations-of-humane-technology/) but increases the complexity of data-related requirements you should incorporate.

In the end, data protection is very much under development in many developing countries, including Malawi, and we won't know what to come in the next few years. Thus, I believe it is also a risk to make a big investment in implementing the "best practices" at this moment; if we do too much and new regulation is off from it, making an alignment causes further complexity.

For these reasons, my general approach is to **stay minimal**. This means not collecting unnecessary information, focusing on domestic audiences first by restricting foreign access requests (to avoid a need to fully comply with the global standards), yet having a basic privacy policy highlighting common aspects. If you do have an extra resource, it is of course advised to take legal advice from a local specialist on the top.

### Current status in Malawi

Coming back to the particular situation in Malawi, the first thing to know is that there is no data protection law in the country as of September 2023, according to the third-party insights from [Data Protection Africa](https://dataprotection.africa/malawi/) and [DataGuidance](https://www.dataguidance.com/jurisdiction/malawi). However, it doesn't mean there has been no debate about data privacy; there are three key documents we should be aware of in this context:

1. [Constitution of Malawi](https://www.malawi.gov.mw/index.php/resources/documents/constitution-of-the-republic-of-malawi) (1994) explicitly states that "every person shall have the right to personal privacy," in Section 21, where "interference with private communications, including mail and all forms of telecommunications" is mentioned.
2. In 2016, the [Electronic Transactions and Cybersecurity Act No. 33](https://macra.mw/download/electronic-transaction-and-cyber-security-act-2016/) provided some basic principles similar to what's commonly seen in other data protection laws across the globe, such as the definition of personal data and implications behind processing such data.
3. In 2021, the [Data Protection Bill](https://digmap.pppc.mw/data-protection-bill-draft/) was published to call for public comments. The Bill aims to consolidate various provisions spread across the Acts, including Act No. 33, and provide a comprehensive legislative framework for personal data protection and its security.

Though the country seems making some progress as someone passionately reported "[Data Protection Law on the Horizon in Malawi](https://cipesa.org/2021/06/data-protection-law-on-the-horizon-in-malawi/)" after the 2021 Bill, I'm still pessimistic about the situation. Even after almost two years, what I can find online is "[Malawi needs data protection law](https://www.nyasatimes.com/malawi-needs-data-protection-laws-against-exploitation-suleman/)" type of discussions with no concrete action plans. We can also see how far it is on the United Nations Economic Commission for Africa's [Digital Trade Regulatory Integration: Country Profile - Malawi](https://repository.uneca.org/handle/10855/48137).

Consider environmental problems. Even though protecting the environment is a critical issue for humans, priorities in developing countries often differ from the Western definition of "urgency" as fundamental needs such as economic growth and public health are clearly more urgent for them[^1].

![garbage](/images/data-protection-law-in-malawi-2023/garbage.jpg)
_\* The city is hopelessly dirty in the developing country._

Similarly, although data protection is indeed important, the nation and businesses won't stop implementing digital solutions for the sake of economic growth. Consequently, the awareness of digital literacy only increases as income also increases at the later phase of development, which can be too late to respond.

At the end of the day, business owners and developers are humans, and without law enforcement, they won't have strong motivation ("incentive") to implement the standards. The lack of attention then makes the internet a simple playground for them. This is very dangerous, and data privacy and safety, in fact, do impact the population's life and health as *[The Social Dilemma](https://www.thesocialdilemma.com/)* and *[The AI Dilemma](https://www.youtube.com/watch?v=xoVJKj8lcNQ)* highlighted; in an emerging era of technology, developers can do whatever they want, and it'll be too late when a real issue arises.

### How's everyone else doing?

To get a better sense of the current status, let's take a look at Malawian organizations' digital privacy policies.

- Government: [Police department privacy policy](https://www.police.gov.mw/about-us/privacy-policy)
- Financial institutes
  - [National Bank of Malawi mobile app privacy](https://www.natbank.co.mw/mobile-app-privacy-policy)
  - [First Capital Bank](https://www.firstcapitalbank.co.mw/privacy/)
- Mobile service and network providers
  - Airtel
      - [Copyright Privacy](https://www.airtel.mw/copyRightPrivacy)
      - [Website terms and conditions](https://www.airtel.mw/termCondition)
  - [TNM](https://www.tnm.co.mw/personal/support/privacy-policy/)

Well, it's actually not easy to find organizations that have a privacy policy link on their website. Even if they do, the contents usually look very short, ambiguous, and stale despite the reputation of the organization.

So, how should we move forward from here? If I were a key stakeholder in a Malawian organization, I might approach the situation as follows.

1. **Awareness**. Implement digital literacy training and teach the role, risk, and mitigation strategy of data being collected, processed, and utilized by organizations. No matter how far your job is from the technologies, today's world is built on top of data, and it is the foundation of web/mobile applications, IoT, and AI. That is, being unaware of the fundamental asset immediately puts you in a difficult position both as a consumer and producer of the services.
2. **Basics**. As mentioned earlier, focus on the basics with a minimal set of target audiences for your activities (e.g., domestic population in a specific region/age range). Draft a simple privacy policy by using a tool like [privacy policy generator](https://www.termsfeed.com/privacy-policy-generator/) and ensure to have a clear understanding of what's written in there and why the information needs to be documented in such a way.
3. **Collaboration**. Cultivate inter-organizational relationships and share data privacy practices with each other. Thinking about data allows organizations not just to fill a gap with the global standards but also to increase the quality of data-driven insights they probably benefit from anytime soon.
4. **Expansion**. Expand the collaborative network and data privacy standards little by little. We might look for neighboring countries and [South Africa's "POPIA" law](https://www.dataguidance.com/jurisdiction/south-africa) as a representative case in southern Africa, or try to catch up on regulations in specific countries where partner organizations' headquarters are based.

Of course, change takes time, and we should never overlook a sustainability aspect of the effort; if we attempt to "short-cut" without acknowledging local contexts (e.g., by letting an external GDPR expert fix everything), we'll miss an opportunity to cultivate your data literacy in a long-lasting way. As a result, you won't be able to survive in a dynamic environment where the standards constantly change due to technological disruptions.

That, in fact, is the dilemma I hold as an international volunteer. On the one hand, I want to address as many problems as possible in a limited amount of time, and I experientially know how to tackle these problems. On the other hand, I understand it is not sustainable if I do everything by myself, and hence I have to decide more not-to-dos than to-dos. No matter what, I'd rather choose an inclusive path where I work \*with\* locals, resulting in a lot more human-human interactions than I used to practice.

![me-speaking](/images/data-protection-law-in-malawi-2023/me-speaking.jpg)
_\* Me engaging with passionate Malawian audiences._

Nevertheless, I believe it is important to take one step at a time, and it is better than nothing&mdash;in my opinion, in this particular context of data protection.

[^1]: Check out *[Globalization and environmental problems in developing countries](https://link.springer.com/article/10.1007/s11356-021-14105-z),* for example. The article discusses the difference in priorities depending on development stages. In the early phase, "global economies plan to generate business and employment opportunities rather than support environmental quality," whereas "ecological awareness increases as income also increases, making it the fundamental reason for reducing environmental degradation in the later stages of economic development."
