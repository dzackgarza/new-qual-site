---
schema: qual/card@1
id: P-BKS04-8A
kind: problem
title: A multilinear map vanishing on equal adjacent arguments is zero when $\dim V<n$
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the two-variable antisymmetry, its propagation to any
    repeated pair, and the linear-combination contradiction when $\dim V<n$. The argument is the retained
    packet's (problem 8A of `assets/attachments/s04solution.pdf`), read again for this pass and unchanged.
---

::: {.problem}
Let $V$ and $W$ be finite-dimensional vector spaces over a field $k$. Let $f\colon V^n\to W$ be a function such that

(a) For each fixed $i\in\{1,\ldots,n\}$ and fixed $v_1,\ldots,v_{i-1},v_{i+1},\ldots,v_n\in V$, the map

$$
\begin{aligned}
&V\to W\\
&x\mapsto f(v_1,\ldots,v_{i-1},x,v_{i+1},\ldots,v_n)
\end{aligned}
$$

is a $k$-linear transformation; and

(b) $f(v_1,\ldots,v_n)=0$ whenever $v_i=v_{i+1}$ for some $i\in\{1,\ldots,n-1\}$.

Prove that either $\dim V\geq n$ or $f$ is identically zero.
:::

::: {.solution}
The retained solution set is the **Berkeley Spring 2004 preliminary solution packet** (`assets/attachments/s04solution.pdf`, extracted text at `assets/attachments/s04solution_extracted.md`), problem 8A; the argument below is its, split into steps.

::: pf

::: {.pf-step #swap}
Interchanging two adjacent arguments changes the sign of $f$: for each $i<n$ and all $x,y$ with the other arguments fixed, $f(\dots,y,x,\dots)=-f(\dots,x,y,\dots)$.

::: pf-proof
Fix $i$ and the remaining arguments, and put $g(x,y)$ for $f$ with $x$ in position $i$ and $y$ in position $i+1$; then $g$ is linear in each variable separately by (a). Hypothesis (b) gives $g(x+y,x+y)=0$, and expanding by linearity in each slot,
$$
0=g(x+y,x+y)=g(x+y,x)+g(x+y,y)=g(x,x)+g(y,x)+g(x,y)+g(y,y).
$$
Again by (b), $g(x,x)=0$ and $g(y,y)=0$, so $g(y,x)+g(x,y)=0$, which is the stated antisymmetry.
:::

:::

::: {.pf-step #repeat}
$f(v_{1},\dots,v_{n})=0$ whenever $v_{i}=v_{j}$ for some $i\ne j$.

::: pf-proof
Suppose $v_{i}=v_{j}$ with $i<j$. Move $v_{j}$ leftwards by successive adjacent transpositions until it occupies position $i+1$; each transposition multiplies the value by $-1$ by step [](#swap){.pf-ref}, so the value after the moves is $\pm f(v_{1},\dots,v_{n})$. In the final arrangement the equal vectors occupy adjacent positions $i$ and $i+1$, so by (b) the value there is $0$; hence $\pm f(v_{1},\dots,v_{n})=0$ and $f(v_{1},\dots,v_{n})=0$.
:::

:::

::: {.pf-step}
Either $\dim V\ge n$ or $f$ is identically zero.

::: pf-proof
Suppose $\dim V<n$ and some $f(v_{1},\dots,v_{n})\ne0$. Then $v_{1},\dots,v_{n}$ are linearly dependent, so some $v_{i}$ is a linear combination $\sum_{j\ne i}c_{j}v_{j}$ of the others. By linearity of $f$ in the $i$-th argument,
$$
f(v_{1},\dots,v_{n})=\sum_{j\ne i}c_{j}\,f(v_{1},\dots,\underset{i}{v_{j}},\dots,v_{n}),
$$
where each summand has $v_{j}$ in position $i$ as well as in position $j$, so each summand vanishes by step [](#repeat){.pf-ref}. Hence $f(v_{1},\dots,v_{n})=0$, contradicting the choice. So if $\dim V<n$ then $f$ is identically zero, which is the assertion.
:::

:::

:::
:::
