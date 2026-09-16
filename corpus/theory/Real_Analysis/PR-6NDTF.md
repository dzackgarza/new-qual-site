---
schema: qual/card@1
id: PR-6NDTF
kind: proposition
title: Measurable slices
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $n=n_1+n_2$, let $m$ denote Lebesgue measure on each $\RR^k$, and let $E\subseteq\RR^{n}=\RR^{n_1}\times\RR^{n_2}$ be [[D-MDJII|Lebesgue measurable]].
For $x\in\RR^{n_1}$, let $E_x \coloneqq \theset{y \in \RR^{n_2} \suchthat (x,y) \in E}$.
Then:

- For almost every $x\in \RR^{n_1}$, the slice $E_x$ is measurable in $\RR^{n_2}$.

- The function
$$
F\colon \RR^{n_1} \to [0,\infty], \qquad x \mapsto m(E_x) = \int_{\RR^{n_2}} \chi_{E_x}(y) \,dy,
$$
defined for almost every $x$, is measurable, and
$$
m(E) = \int_{\RR^{n_1}} m(E_x) \,dx
= \int_{\RR^{n_1}} \int_{\RR^{n_2}} \chi_{E_x}(y) \,dy \,dx .
$$
:::
