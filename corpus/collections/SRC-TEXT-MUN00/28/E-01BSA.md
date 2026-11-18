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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.6, PDF p. 19** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument follows the book's hint as they use it, with the imbedding step and the separating distance as separate steps.

Let $(X,d)$ be compact and let $f:X\to X$ satisfy $d\big(f(x),f(y)\big)=d(x,y)$ for all $x,y$.

::: pf

::: {.pf-step #imbedding}
$f$ is injective and continuous, hence an imbedding of $X$ onto $f(X)$.

::: pf-proof
If $f(x)=f(y)$ then $d(x,y)=d(f(x),f(y))=0$, so $x=y$. For continuity, given $\varepsilon>0$ the choice $\delta=\varepsilon$ gives $d(f(x),f(y))=d(x,y)<\delta\Rightarrow<\varepsilon$; and $f^{-1}:f(X)\to X$ is continuous by the same computation, so $f$ is an imbedding (Exercise 21.2, printed p. 136).
:::

:::

::: {.pf-step #separate}
If $f$ were not surjective, there would be $a\in X\setminus f(X)$ and $\varepsilon>0$ with $B_{d}(a,\varepsilon)\cap f(X)=\varnothing$.

::: pf-proof
$f(X)$ is compact, being the continuous image of the compact space $X$ (Theorem 26.5, printed p. 166), hence closed in the metric space $X$; a point outside a closed set has positive distance from it, so such an $\varepsilon$ exists.
:::

:::

::: {.pf-step #orbits}
With $x_{1}=a$ and $x_{n+1}=f(x_{n})$, one has $d(x_{n},x_{m})\ge\varepsilon$ for all $n\ne m$.

::: pf-proof
For $n<m$ the isometry property iterated gives $d(x_{n},x_{m})=d\big(f^{n-1}(a),f^{n-1}(x_{m-n+1})\big)=d(a,x_{m-n+1})$. Now $x_{m-n+1}\in f(X)$ when $m-n+1\ge2$, and $x_{1}=a$ when $m-n+1=1$; in the first case $d(a,x_{m-n+1})\ge\varepsilon$ by step [](#separate){.pf-ref}, in the second $d(a,a)=0$ — but that case has $m=n$, excluded. So $d(x_{n},x_{m})\ge\varepsilon$.
:::

:::

::: {.pf-step #contradiction}
The sequence $(x_{n})$ has no convergent subsequence, contradicting sequential compactness of $X$.

::: pf-proof
A convergent subsequence would have its terms eventually within $\varepsilon/2$ of the limit, hence within $\varepsilon$ of each other, contradicting step [](#orbits){.pf-ref}. A compact metric space is sequentially compact (Theorem 28.2, printed p. 181).
:::

:::

::: {.pf-qed}
$f$ is surjective by step [](#contradiction){.pf-ref} and injective by step [](#imbedding){.pf-ref}, so it is bijective; a continuous bijection from the compact space $X$ to the Hausdorff space $X$ is a homeomorphism (Theorem 26.6, printed p. 167).
:::

:::

:::
