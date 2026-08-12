---
schema: qual/card@1
id: P-GFCIL
kind: problem
title: "Let $I = [0,1]$ and denote $\\|\\cdot\\|_p$ the $p$-norm $\\|f\\|_p = \\left(\\int_I |f|^p\\right)^{1/p}$ for $1 \\le p < \\infty$ (we admit this is a norm) and $\\|f\\|_\\infty = \\operatorname{ess\\,sup}|f|$."
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

:::{.problem title="?"}
Let $I = [0,1]$ and denote $\|\cdot\|_p$ the $p$-norm $\|f\|_p = \left(\int_I |f|^p\right)^{1/p}$ for $1 \le p < \infty$ (we admit this is a norm) and $\|f\|_\infty = \operatorname{ess\,sup}|f|$.

- Show that the space of continuous functions on $I$ endowed with the norm $\|\cdot\|_p$ for $1 \le p < \infty$ is not a Banach space.
- Prove that the space of (Lebesgue) measurable functions on $I$ such that their $p$-norm is finite is a Banach space for $1 \le p \le \infty$.
- Prove that there is no smooth function $h$ such that $f * h = f$ for every $f \in L^1(I)$.
- Prove the Hölder inequality: for $p, q \ge 1$ such that $\frac{1}{p}+\frac{1}{q}=1$
$$\int_I fg \le \|f\|_p\|g\|_q$$
One can use the inequality $ab \le \frac{a^p}{p}+\frac{a^q}{q}$ for any $a,b \ge 0$.
- Deduce the Young inequality: $L^p * L^q \subset L^r$ for $\frac{1}{p}+\frac{1}{q} = 1+\frac{1}{r}$
:::
