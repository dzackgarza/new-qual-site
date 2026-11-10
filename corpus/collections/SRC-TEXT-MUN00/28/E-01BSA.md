---
schema: qual/card@1
id: E-01BSA
kind: problem
title: Isometries of compact metric spaces are surjective
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §28 Exercise 6, printed p. 181, with Exercise
    21.2, Theorem 27.4 and Theorem 28.2; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 28.6, PDF p. 19. An isometry of a compact metric
    space is an imbedding; if it missed a point, iterating it would give a sequence with all
    mutual distances bounded below, contradicting sequential compactness.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $(X, d)$ be a metric space.
If $f: X \to X$ satisfies the condition

$$
d(f(x), f(y)) = d(x, y)
$$

for all $x, y \in X$, then $f$ is called an isometry of $X$.
Show that if $f$ is an isometry and $X$ is compact, then $f$ is bijective and hence a homeomorphism.
[Hint: If $a \notin f(X)$, choose $\epsilon$ so that the $\epsilon$-neighborhood of $a$ is disjoint from $f(X)$. Set $x_1 = a$, and $x_{n+1} = f(x_n)$ in general. Show that $d(x_n, x_m) \geq \epsilon$ for $n \neq m$.]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.6, PDF p. 19** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument follows the hint as they use it.

Let $(X,d)$ be compact and $f:X\to X$ satisfy $d(f(x),f(y))=d(x,y)$. By Exercise 21.2 $f$ is an imbedding; suppose it is not surjective and pick $a\in X-f(X)$. Since $f(X)$ is compact, hence closed, there is $\varepsilon>0$ with $B_{d}(a,\varepsilon)\cap f(X)=\varnothing$.

Put $x_{1}=a$ and $x_{n+1}=f(x_{n})$. For $n<m$,
$$
d(x_{n},x_{m})=d(f(x_{n-1}),f(x_{m-1}))=d(x_{n-1},x_{m-1})=\cdots=d(a,\,x_{m-n}),
$$
and $x_{m-n}=f(x_{m-n-1})\in f(X)$ when $m-n>1$, while $x_{1}=a$; in either case $d(x_{n},x_{m})\ge\varepsilon$ for $n\ne m$. So $(x_{n})$ has no convergent subsequence, and $X$ is not sequentially compact — contradicting Theorem 28.2, since compact metric spaces are sequentially compact. Hence $f$ is surjective and therefore a homeomorphism.
:::
