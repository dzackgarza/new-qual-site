---
schema: qual/card@1
id: P-JHUU67RA3
kind: problem
title: Holder inequality, Young inequality, and Lp Banach spaces
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
---

Let $I = [0,1]$ and denote $\|\cdot\|_p$ the $p$-norm $\|f\|_p = \left(\int_I |f|^p\right)^{1/p}$ for $1 \leq p < \infty$ and $\|f\|_\infty = \ess\sup |f|$.

- Show that the space of continuous functions on $I$ endowed with the norm $\|\cdot\|_p$ for $1 \leq p < \infty$ is not a Banach space.

- Prove that the space of (Lebesgue) measurable functions on $I$ such that their $p$-norm is finite is a Banach space for $1 \leq p \leq \infty$.

- Prove that there is no smooth function $h$ such that $f * h = f$ for every $f \in L^1(I)$.

- Prove the Hölder inequality: for $p, q \geq 1$ such that $\frac{1}{p} + \frac{1}{q} = 1$

$$\int_I fg \leq \|f\|_p \|g\|_q.$$

One can use the inequality $ab \leq \frac{a^p}{p} + \frac{a^q}{q}$ for any $a, b \geq 0$.

- Deduce the Young inequality: $L^p * L^q \subset L^r$ for $\frac{1}{p} + \frac{1}{q} = 1 + \frac{1}{r}$.
