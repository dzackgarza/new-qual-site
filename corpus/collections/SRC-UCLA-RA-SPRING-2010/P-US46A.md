---
schema: qual/card@1
id: P-US46A
kind: problem
title: $L^2$ continuity of translations, and $W-W$ contains a neighbourhood of $0$
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Measure Theory
  - Continuity
relations: []
review: draft
---

::: {.problem}
a. For $f\in L^2(\mathbb{R})$ and a sequence $\{x_n\}\subseteq\mathbb{R}$ which converges to zero, define $f_n(x):=f(x+x_n)$.
Show that $\{f_n\}$ converges to $f$ in $L^2$.

b. Let $W\subseteq\mathbb{R}$ be a Lebesgue measurable set of positive Lebesgue measure.
Show that the set of differences $W-W = \{x-y: x,y\in W\}$ contains an open neighborhood of the origin.
:::

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
