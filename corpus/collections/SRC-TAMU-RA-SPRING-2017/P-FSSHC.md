---
schema: qual/card@1
id: P-FSSHC
kind: problem
title: Extreme points of the unit ball of convergent sequences, and whether the ball
  is their closed convex hull
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Functional Analysis
  - Norms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: The TAMU source specifies convergent sequences of real numbers; its retained solution explicitly left the closed-convex-hull part unresolved.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
---

::: {.problem}
Let $C$ denote the real Banach space of all convergent real sequences under the norm $\|\cdot\|_\infty$.
Compute the extreme points of the unit ball $B$ of $C$ and determine whether $B$ is the closed convex hull of its extreme points.
:::

::: {.solution}
<1>1. If $a=(a_n)\in B$ has $|a_m|<1$ for some $m$, then $a$ is not an extreme point of $B$.
::: {.proof}
Choose $\delta>0$ with
\[
|a_m\pm\delta|\le1.
\]
Define $b^+,b^-\in C$ by changing only the $m$-th coordinate:
\[
b_n^\pm=a_n\quad(n\ne m),
\qquad
b_m^\pm=a_m\pm\delta.
\]
Changing one coordinate preserves convergence, and $\|b^\pm\|_\infty\le1$, so $b^\pm\in B$.
They are distinct and
\[
a={b^++b^-\over2}.
\]
:::

<1>2. If $a=(a_n)\in B$ satisfies $|a_n|=1$ for every $n$, then $a$ is an extreme point of $B$.
::: {.proof}
Suppose
\[
a=\lambda b+(1-\lambda)c,
\qquad
0<\lambda<1,
\qquad
b,c\in B.
\]
For each $n$,
\[
1=|a_n|
\le\lambda|b_n|+(1-\lambda)|c_n|
\le1.
\]
Since the scalars are real and $a_n=\pm1$, equality forces
\[
b_n=c_n=a_n.
\]
Thus $b=c=a$.
:::

<1>3. The extreme points are exactly the convergent sign sequences:
\[
\operatorname{Ext}(B)
=\left\{a\in C:|a_n|=1\text{ for all }n\right\}.
\]
Equivalently, they are the $\{\pm1\}$-valued sequences that are eventually constant.
::: {.proof}
The first description follows from <1>1 and <1>2.
A convergent sequence taking values only in the discrete set $\{-1,1\}$ must eventually equal its limit, which is either $1$ or $-1$.
:::

<1>4. Let $a=(a_n)\in B$ and let $L=\lim_n a_n$.
For each $N$, define
\[
a^{(N)}=(a_1,\ldots,a_N,L,L,\ldots).
\]
Then
\[
\|a-a^{(N)}\|_\infty\longrightarrow0.
\]
::: {.proof}
We have
\[
\|a-a^{(N)}\|_\infty
=\sup_{n>N}|a_n-L|,
\]
which tends to $0$ because $a_n\to L$.
:::

<1>5. Every $a^{(N)}$ in <1>4 belongs to $\operatorname{conv}(\operatorname{Ext}(B))$.
::: {.proof}
The vector
\[
(a_1,\ldots,a_N,L)
\]
lies in the cube $[-1,1]^{N+1}$.
This cube is the convex hull of its vertices $\{\pm1\}^{N+1}$.
For each vertex
\[
(\varepsilon_1,\ldots,\varepsilon_N,\varepsilon_\infty),
\]
associate the convergent sequence
\[
(\varepsilon_1,\ldots,\varepsilon_N,
\varepsilon_\infty,\varepsilon_\infty,\ldots),
\]
which is an extreme point by <1>3.
The same convex combination representing $(a_1,\ldots,a_N,L)$ in the cube represents $a^{(N)}$ as a convex combination of these extreme sequences.
:::

<1>6. The unit ball is the norm-closed convex hull of its extreme points:
\[
\boxed{B=\overline{\operatorname{conv}}(\operatorname{Ext}(B))}.
\]
::: {.proof}
By <1>4 and <1>5, every $a\in B$ is a norm limit of elements of $\operatorname{conv}(\operatorname{Ext}(B))$.
Thus
\[
B\subseteq\overline{\operatorname{conv}}(\operatorname{Ext}(B)).
\]
The reverse inclusion holds because $B$ is closed and convex and contains all its extreme points.
:::
:::
