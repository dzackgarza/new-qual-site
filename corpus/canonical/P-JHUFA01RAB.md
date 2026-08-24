---
schema: qual/card@1
id: P-JHUFA01RAB
kind: problem
title: Convolution of functions vanishing at infinity
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

Let $f$ and $g$ be continuous real valued functions on $\mathbb{R}$ such that $\lim_{|x| \to \infty} f(x) = 0$ and $\int_{-\infty}^\infty |g(x)| \, dx < \infty$.
Define the function $h$ on $\mathbb{R}$ by

$$h(x) = \int_{-\infty}^\infty f(x - y) g(y) \, dy.$$

Prove that $\lim_{|x| \to \infty} h(x) = 0$.
