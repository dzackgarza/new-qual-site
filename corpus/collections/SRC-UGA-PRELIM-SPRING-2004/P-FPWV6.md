---
schema: qual/card@1
id: P-FPWV6
kind: problem
title: Examples - a false converse, continuous not differentiable, separate continuity, non-Cauchy bounded sequence, and a series converging exactly on $[0,2]$
classification:
  areas:
  - prelim
  topics:
  - Counterexamples
  - Differentiation
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Provide examples of the following.
[No justification is required.]

a) a true implication whose converse is false,

b) a function $f: \mathbb{R} \to \mathbb{R}$ which is continuous at $7$, but not differentiable there,

c) a function $f: \mathbb{R}^2 \to \mathbb{R}$ which is continuous in each variable separately, but is not continuous at $(0,0)$,

d) a bounded sequence which is not Cauchy,

e) a (real) power series whose domain of convergence is the closed interval $[0,2]$.
:::

::: {.solution}
<1>1. (a) $p\Rightarrow q$ with $p:$ $n$ divisible by $4$, $q:$ $n$ even. Converse false ($2$ even but not divisible by $4$).
Proof: example.

<1>2. (b) $f(x)=|x-7|$ continuous at $7$ but not differentiable (corner).
Proof: $|x|$.

<1>3. (c) $f(x,y)=xy/(x^2+y^2)$ for $(x,y)\neq(0,0)$, $0$ at origin: separately continuous but not continuous at $(0,0)$ (limit along $y=x$ is $1/2$).
Proof: check.

<1>4. (d) $a_n=(-1)^n$ bounded but not Cauchy.
Proof: $|a_{n+1}-a_n|=2$.

<1>5. (e) $\sum_{n\ge1}(x-1)^n/n^2$ has radius $1$, converges at $x=0,2$ ($p$-series), diverges for $|x-1|>1$, so domain $[0,2]$.
Proof: root test.

<1>6. Q.E.D.
Proof: <1>1 and <1>5.
:::
