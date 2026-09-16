---
schema: qual/card@1
id: FF-YXTQY
kind: fact
title: $\{1/n\}$ and $\ZZ$ are nowhere dense; $\QQ$ is not
prompts:
- Give an example of a set that is not nowhere dense.
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Counterexamples
relations: []
review: draft
---

::: {.fact}
In $\RR$:

- $\theset{1/n\suchthat n\geq 1}$ and $\ZZ$ are [[D-2MJRE|nowhere dense]], since their closures $\theset{0}\cup\theset{1/n\suchthat n\geq 1}$ and $\ZZ$ contain no open interval;

- $\QQ$ and $\ZZ\cup\qty{(a, b)\cap\QQ}$ for $a<b$ are not nowhere dense, since their closures $\RR$ and $\ZZ\cup[a,b]$ contain the open interval $(a,b)$.
:::
