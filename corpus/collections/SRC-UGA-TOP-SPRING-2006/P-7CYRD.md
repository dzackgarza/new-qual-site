---
schema: qual/card@1
id: P-7CYRD
kind: problem
title: Open-set, $\varepsilon$-$\delta$, and sequential criteria for continuity in
  a metric space
classification:
  areas:
  - topology
  topics:
  - Continuity
  - Metric Spaces
  - Convergence
relations: []
review: draft
---

::: {.problem}
Suppose $(X, d)$ is a metric space.
State criteria for continuity of a function $f : X \to X$ in terms of:

i. open sets;

ii.
$\eps$'s and $\delta$'s; and

iii.
convergent sequences.

Then prove that (iii) implies (i).
:::

::: {.solution}
<1>1. The three continuity criteria are as follows.
::: {.proof}
For a map $f:X\to X$ between metric spaces:

<2>1. **Open-set criterion:** for every open set $U\subseteq X$, the inverse image $f^{-1}(U)$ is open in $X$.

<2>2. **$\varepsilon$-$\delta$ criterion:** for every $x\in X$ and every $\varepsilon>0$, there is $\delta>0$ such that
\[
d(x,y)<\delta
\implies
d(f(x),f(y))<\varepsilon
\]
for every $y\in X$.

<2>3. **Sequential criterion:** whenever $x_n\to x$ in $X$, one has
\[
f(x_n)\to f(x).
\]
:::

<1>2. Assume the sequential criterion <1>1.<2>3. Let $U\subseteq X$ be open and let $x\in f^{-1}(U)$.
::: {.proof}
To prove the open-set criterion, it suffices to prove that every point of $f^{-1}(U)$ is an interior point of $f^{-1}(U)$.
:::

<1>3. The point $x$ from <1>2 is an interior point of $f^{-1}(U)$.
::: {.proof}
Suppose not. Then every ball $B_{1/n}(x)$ contains a point outside $f^{-1}(U)$. Choose
\[
x_n\in B_{1/n}(x)\setminus f^{-1}(U).
\]
Then $d(x_n,x)<1/n$, hence $x_n\to x$.

By the sequential criterion,
\[
f(x_n)\to f(x).
\]
Since $x\in f^{-1}(U)$, we have $f(x)\in U$. Because $U$ is open and $f(x_n)\to f(x)$, there is $N$ such that
\[
n\ge N\implies f(x_n)\in U.
\]
But $x_n\notin f^{-1}(U)$ for every $n$, so $f(x_n)\notin U$ for every $n$, a contradiction.
:::

<1>4. The sequential criterion implies the open-set criterion.
::: {.proof}
The open set $U$ in <1>2 was arbitrary, and <1>3 shows every point of $f^{-1}(U)$ is interior. Hence $f^{-1}(U)$ is open for every open $U$, which is criterion <1>1.<2>1.
:::
:::
