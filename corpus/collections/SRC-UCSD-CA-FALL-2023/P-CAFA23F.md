---
schema: qual/card@1
id: P-CAFA23F
kind: problem
title: "Zeros of partial sums of the exponential function"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
For each $N \in \mathbb{N}$, let $P_N(z) = \sum_{n=0}^{N} \frac{z^n}{n!}$.

(a) Show that the set $Z = \{z \in \mathbb{C} \mid P_N(z) = 0 \text{ for some } N \in \mathbb{N}\}$ is **discrete** (has no accumulation points in $\mathbb{C}$).

(b) Find a constant $c > 0$ such that $P_N(z)$ has no zeros in $\{z \in \mathbb{C} \mid |z| < cN\}$.
*(You may use the inequality $n! > e^{-n} n^n$.)*
:::

::: solution
Let
$$
R_N(z)=e^z-P_N(z)=\sum_{n=N+1}^\infty\frac{z^n}{n!}.
$$
Choose
$$
c=\frac1{4e}.
$$
Suppose $|z|\le cN$. Since $|z|/(N+j)\le c$ for every $j\ge1$,
$$
|R_N(z)|
\le \frac{|z|^{N+1}}{(N+1)!}\frac1{1-c}.
$$
Using $(N+1)!>e^{-(N+1)}(N+1)^{N+1}$ and $N/(N+1)<1$,
$$
|R_N(z)|
<\frac{(ce)^{N+1}}{1-c}.
$$
On the other hand,
$$
|e^z|=e^{\Re z}\ge e^{-|z|}\ge e^{-cN}.
$$
Therefore
$$
\frac{|R_N(z)|}{|e^z|}
<\frac{ce}{1-c}\bigl(ce^{1+c}\bigr)^N.
$$
For $c=1/(4e)$,
$$
ce=\frac14,
\qquad
ce^{1+c}=\frac14e^{1/(4e)}<\frac13,
$$
so for every $N\ge1$,
$$
\frac{|R_N(z)|}{|e^z|}
<\frac{1/4}{1-1/(4e)}\cdot\frac13<1.
$$
Hence $|R_N(z)|<|e^z|$. If $P_N(z)=0$, then $e^z=R_N(z)$, a contradiction. Thus $P_N$ has no zero in $|z|<cN$.

<1>1. To prove discreteness, let $K\subset\mathbb C$ be compact and choose $R$ with $K\subset\overline{D_R}$. If $N>R/c$, then every zero of $P_N$ has modulus at least $cN>R$, so $P_N$ has no zero in $K$. Only finitely many $N$ can therefore contribute zeros to $K$, and each such polynomial has finitely many zeros. Hence $Z\cap K$ is finite for every compact $K$, so $Z$ has no accumulation point in $\mathbb C$.
:::
