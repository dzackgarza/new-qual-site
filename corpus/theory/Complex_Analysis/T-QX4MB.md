---
schema: qual/card@1
id: T-QX4MB
kind: theorem
title: Phragmén--Lindelöf principle
slogan: 'A function bounded by $1$ on the boundary of a sector, and growing slower than a power fixed by the angle, is bounded by $1$ in the sector.'
prompts:
- State the Phragmén--Lindelöf principle for a sector.
- When does a bound on the boundary of a sector extend to the interior?
classification:
  areas:
  - complex-analysis
  topics:
  - Phragmén-Lindelöf
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.theorem}
Let $\beta>0$, let $S$ be the open sector with vertex $0$ and opening angle $\pi/\beta$, and let $F$ be [[D-E7A5W|holomorphic]] on $S$ and continuous on $\overline S$.
Suppose that $\abs{F}\leq 1$ on $\bd S$ and that there are $C, c>0$ and $0<\alpha<\beta$ with
$$
\abs{F(z)} \leq C e^{c\abs z^\alpha} \qquad \text{for all } z\in S.
$$
Then $\abs{F(z)}\leq 1$ for all $z\in S$ [@SS03, ch. 4, §4, Exercise 9(b)].

The case $\abs{\arg z}<\pi/4$, where $\beta=2$, is proved under the stronger growth hypothesis $\abs{F(z)}\leq Ce^{c\abs z}$ [@SS03, ch. 4, §3, Theorem 3.4].
:::

::: {.remark title="Why the growth hypothesis is needed"}
The maximum modulus principle is the case in which $F$ is bounded in $S$; the content of the theorem is that a bound on $\bd S$ suffices under growth below the power $\abs z^\beta$.
On the sector $\abs{\arg z}<\pi/4$ the function $e^{z^2}$ satisfies $\abs{e^{z^2}} = 1$ on the two boundary rays, since $z^2 = \pm i r^2$ there, and $\abs{e^{z^2}} = e^{x^2}$ on the real axis, so the bound on $\bd S$ alone gives nothing [@SS03, ch. 4, §3, Theorem 3.4].
:::
