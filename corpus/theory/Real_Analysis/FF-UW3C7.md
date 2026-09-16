---
schema: qual/card@1
id: FF-UW3C7
kind: fact
title: A composition of Lebesgue measurable functions need not be measurable
prompts:
- Is the composition of Lebesgue measurable functions again Lebesgue measurable?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Cantor Set
  - Counterexamples
relations:
- kind: variant-of
  target: FE-YOIJM
review: draft
---

::: {.fact}
There exist a [[D-DHFN4|Lebesgue measurable]] function $h\colon\RR\to\RR$ and a continuous function $\phi\colon[0,2]\to[0,1]$ such that $h\circ\phi$ is not Lebesgue measurable.
:::

::: {.proof}
Let $C\subseteq[0,1]$ be the Cantor set and $f\colon[0,1]\to[0,1]$ the Cantor--Lebesgue function, which is continuous, nondecreasing, and constant on each connected component of $[0,1]\setminus C$.
Put $g(x)\coloneqq f(x) + x$.
Then $g\colon[0,1]\to[0,2]$ is continuous and strictly increasing with $g(0) = 0$ and $g(1) = 2$, so it is a homeomorphism, and $\phi\coloneqq g\inv\colon[0,2]\to[0,1]$ is continuous.

The set $[0,1]\setminus C$ is a disjoint union of open intervals of total length $1$, and $g$ maps each of them onto an interval of the same length because $f$ is constant on it.
Hence $m(g([0,1]\setminus C)) = 1$ and $m(g(C)) = 2 - 1 = 1 > 0$.
Every subset of $\RR$ of positive Lebesgue measure contains a subset that is not [[D-MDJII|Lebesgue measurable]], so there is a non-measurable $A\subseteq g(C)$.

The set $B\coloneqq g\inv(A)$ is contained in $C$, which has measure $0$, so $B$ is Lebesgue measurable and $h\coloneqq\chi_B$ is a Lebesgue measurable function.
For $y\in[0,2]$, $(h\circ\phi)(y) = 1$ if and only if $g\inv(y)\in g\inv(A)$, that is, $y\in A$.
Hence $(h\circ\phi)\inv(\theset{1}) = A$ is not Lebesgue measurable, so $h\circ\phi$ is not Lebesgue measurable.
:::
