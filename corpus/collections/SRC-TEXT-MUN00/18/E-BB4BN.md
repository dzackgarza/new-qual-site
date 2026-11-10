---
schema: qual/card@1
id: E-BB4BN
kind: problem
title: Intervals homeomorphic with the unit interval
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 5, printed p. 111, with the subspace
    topology of §16; the stored statement is the printed sentence, and the card treats a < b
    and a = b separately.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 18.5, printed p. 181.
    The maps x -> (x-a)/(b-a) and y -> a + y(b-a) and the argument that they are mutually
    inverse continuous bijections are his, as is the remark that [a,a] cannot be
    homeomorphic with [0,1]. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Show that the subspace $(a, b)$ of $\RR$ is homeomorphic with $(0, 1)$ and the subspace $[a, b]$ of $\RR$ is homeomorphic with $[0, 1]$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 18.5, printed p. 181** (`tmp/sources/munkres-solutions-whitman.pdf`); the maps and the argument are his, including the observation about the degenerate case.

Suppose $a<b$ and put $X=(a,b)$, $Y=(0,1)$ and
$$
f:X\longrightarrow Y,\qquad f(x)=\frac{x-a}{b-a},
$$
which is defined because $b-a>0$. This is a bijection (its inverse, computed below, is defined on all of $Y$), and it is the restriction to $X$ of the linear map $\RR\to\RR$, $x\mapsto(x-a)/(b-a)$, which is continuous by elementary calculus; by Theorem 18.2(d) its restriction to the subspace $X$ is continuous. Its inverse is
$$
f^{-1}:Y\longrightarrow X,\qquad f^{-1}(y)=a+y(b-a),
$$
again linear, hence continuous. So $f$ is a homeomorphism.

The same formula with $X=[a,b]$ and $Y=[0,1]$ shows that $[a,b]$ is homeomorphic with $[0,1]$: the same two maps are mutually inverse bijections, and continuity is again that of a restriction of a linear map.

If $a=b$ then $[a,b]=\{a\}$ is a one-point space, which is not homeomorphic with $[0,1]$: a homeomorphism is a bijection, and $[0,1]$ is infinite.
:::
