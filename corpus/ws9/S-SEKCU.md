---
schema: qual/card@1
id: S-SEKCU
kind: solution
title: Solution to P-US46A
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Measure Theory
  - Continuity
relations:
- kind: solves
  target: P-US46A
review: draft
---

:::{.solution}
(a) See Fall 2011 #3.

(b) Let $f(x)=\chi_W(x)$ and $f_y(x)=\chi_W(x+y)$. We calculate
$$||f-f_y||_{L^2}^2 = \int (\chi_W(x)-\chi_W(x+y))^2\,dx$$
$$= \int \chi_W(x)^2 + \chi_W(x+y)^2 - 2\chi_W(x)\chi_W(x+y)\,dx$$
$$= 2m(W) - 2\int \chi_W(x)\chi_W(x+y)\,dx.$$
By part (a), this quantity goes to 0 as $y\to0$. Thus for all $y$ sufficiently small,
$$\int \chi_W(x)\chi_W(x+y)\,dx > \frac{1}{2}m(W) > 0.$$
In particular, there is at least one $x$ such that $\chi_W(x)\chi_W(x+y)=1$, i.e. $x\in W$ and $x+y\in W$, so $y\in W-W$. Thus $W-W$ contains all sufficiently small $y$, as desired. $\square$
:::
