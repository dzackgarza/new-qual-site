---
schema: qual/card@1
id: P-MMAQ-5HMKSRNSGM
kind: problem
title: Let
classification:
  areas:
  - real-analysis
  topics:
  - series-of-functions
  - integrals
  - convergence-of-functions
  - l1
relations: []
review: draft
---

::: problem
Let
$$
f_{n}(x)=a e^{-n a x}-b e^{-n b x} \quad \text{ where } 0 < a < b.
$$

Show that

a.  $\sum_{n=1}^{\infty}\left|f_{n}\right| \text { is not in } L^{1}([0, \infty), m)$

> Hint: $f_n(x)$ has a root $x_n$.

b.  $$
    \sum_{n=1}^{\infty} f_{n} \text { is in } L^{1}([0, \infty), m) 
    \quad \text { and } \quad 
    \int_{0}^{\infty} \sum_{n=1}^{\infty} f_{n}(x) ~d m=\ln \frac{b}{a}
    $$
:::
