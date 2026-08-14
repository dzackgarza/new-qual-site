---
schema: qual/card@1
id: P-MMAQ-MZ6ONVPBKI
kind: problem
title: 'Let $I$ be an index set and $\alpha: I \to (0, \infty)$.'
classification:
  areas:
  - real-analysis
  topics:
  - series-of-numbers
  - continuity
relations: []
review: draft
---

::: problem
Let $I$ be an index set and $\alpha: I \to (0, \infty)$.

1. Show that
   $$
   \sum_{i \in I} a(i):=\sup _{\substack{ J \subset I \\ J \text { finite }}} \sum_{i \in J} a(i)<\infty \implies I \text{ is countable.}
   $$

2. Suppose $I = \QQ$ and $\sum_{q \in \mathbb{Q}} a(q)<\infty$.
   Define
   $$
   f(x):=\sum_{\substack{q \in \mathbb{Q}\\ q \leq x}} a(q).
   $$
   Show that $f$ is continuous at $x \iff x\not\in \QQ$.
:::
