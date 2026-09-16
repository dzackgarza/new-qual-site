---
schema: qual/card@1
id: E-HAT-3.D-2
kind: problem
title: "Fundamental group of $SO(n)$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.D, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Using the CW structure on $SO(n)$, show that $\pi_1 SO(n) \approx \mathbb{Z}_2$ for $n \geq 3$.
Find a loop representing a generator, and describe how twice this loop is nullhomotopic.
:::

::: {.solution}
Use the CW structure of Proposition 3D.1. For $n\ge3$, its cells are indexed by strictly decreasing sequences
\[
n>i_1>\cdots>i_r>0,
\]
with cell dimension $i_1+\cdots+i_r$, together with the single $0$-cell.

In dimensions at most $2$ there are therefore exactly three cells:
\[
e^0,\qquad e^1,\qquad e^2.
\]
The cells $e^1$ and $e^2$ are the images of the standard cells of
\[
\mathbb{RP}^{n-1}\subset SO(n)
\]
under Hatcher's map
\[
\rho(v)=r(v)r(e_1).
\]
The characteristic map of the $2$-cell of $\mathbb{RP}^{n-1}$ restricts on its boundary circle to the double covering
\[
S^1\to\mathbb{RP}^1\cong S^1.
\]
Consequently the $2$-cell of $SO(n)$ is attached to the $1$-cell by a map of degree $2$. Thus the $2$-skeleton has fundamental group
\[
\pi_1(SO(n)^{(2)})
\cong\langle a\mid a^2=1\rangle
\cong\mathbb Z_2.
\]
Attaching cells of dimension at least $3$ does not change the fundamental group, so
\[
\boxed{\pi_1SO(n)\cong\mathbb Z_2\qquad(n\ge3).}
\]

The generator has a concrete geometric description. Let a fixed oriented $2$-plane in $\mathbb R^n$ rotate through angle
\[
0\le\theta\le2\pi
\]
while the orthogonal complement is fixed pointwise. This gives a loop in $SO(n)$; it is precisely the loop represented by the $1$-cell $e^1$, hence represents the nonzero element of $\pi_1SO(n)$.

Traversing this loop twice gives a $4\pi$ rotation. In the CW structure, the attaching map of $e^2$ traverses the $1$-cell twice, so the characteristic disk of $e^2$ is an explicit nullhomotopy of this doubled loop. Thus the generator has order exactly $2$.
:::
