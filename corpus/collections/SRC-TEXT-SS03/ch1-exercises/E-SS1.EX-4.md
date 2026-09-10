---
schema: qual/card@1
id: E-SS1.EX-4
kind: problem
title: The complex numbers admit no ordered-field structure
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: exercise
4. Show that it is impossible to define a total ordering on C. In other words, one cannot find a relation between complex numbers so that:

(i) For any two complex numbers z, w, one and only one of the following is true: $z \succ w , w \succ z \ \mathrm { o r } \ z = w .$

(ii) For all $z _ { 1 } , z _ { 2 } , z _ { 3 } \in \mathbb { C }$ the relation $z _ { 1 } \succ z _ { 2 }$ implies $z _ { 1 } + z _ { 3 } \succ z _ { 2 } + z _ { 3 }$

(iii) Moreover, for all $z _ { 1 } , z _ { 2 } , z _ { 3 } \in \mathbb { C }$ with $z _ { 3 } \succ 0$ , then $z _ { 1 } \succ z _ { 2 }$ implies $z _ { 1 } z _ { 3 } \succ z _ { 2 } z _ { 3 }$

[Hint: First check if $i \succ 0$ is possible.]
:::

::: solution
Assume such an ordering exists. For every nonzero $z\in\mathbb C$, trichotomy gives either $z\succ0$ or $-z\succ0$. In either case, compatibility with multiplication implies
\[
z^2\succ0.
\]
Applying this to $z=1$ and $z=i$ gives
\[
1\succ0,
\qquad
i^2=-1\succ0.
\]
Adding $1$ to the inequality $-1\succ0$ yields
\[
0\succ1,
\]
contradicting $1\succ0$. Therefore no total ordering on $\mathbb C$ can satisfy the ordered-field axioms (i)--(iii).
:::
