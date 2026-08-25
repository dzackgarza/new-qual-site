---
schema: qual/card@1
id: P-RAF04C
kind: problem
title: "Translation inner product of L^2 functions vanishes at infinity"
classification:
  areas:
  - real-analysis
  topics:
  - L2 Spaces
  - Translations
  - Dense Subsets
relations: []
review: draft
---

::: problem
Let $f$ and $g$ be two real $L^2(\mathbb{R}, m)$-functions.
Show
$$
\lim_{n \to \infty} \int_\mathbb{R} f(x) g(x-n) \, dx = 0.
$$

Hint: First prove the result holds if $g \in L^2(\mathbb{R}, m)$ is further assumed to have compact support.
:::
