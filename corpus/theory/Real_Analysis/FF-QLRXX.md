---
schema: qual/card@1
id: FF-QLRXX
kind: fact
title: Growth rates of common functions
prompts:
- How do $n!$, $c^n$, $n^c$, $n\log n$, $n$ and $\log n$ rank by growth rate?
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
relations: []
review: draft
---

::: {.fact}
For real sequences $a(n)$, $b(n)$ that are positive for all sufficiently large $n$, write $a\prec b$ if $a(n)/b(n)\to 0$ as $n\to\infty$.
For every real $c>1$,
$$
1 \prec \log(\log n) \prec \log n \prec n \prec n\log n \prec n^{c} \prec c^n \prec n!.
$$

![](https://i.imgur.com/M9u3lOr.png)
:::
