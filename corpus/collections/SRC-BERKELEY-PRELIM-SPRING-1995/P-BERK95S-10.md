---
schema: qual/card@1
id: P-BERK95S-10
kind: problem
title: A decreasing sequence of nonnegative continuous functions has an attained limiting supremum
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f_n:[0,1]\to[0,\infty)$ be continuous and suppose
\[
f_1(x)\ge f_2(x)\ge f_3(x)\ge\cdots
\]
for every $x\in[0,1]$. Set
\[
f(x)=\lim_{n\to\infty}f_n(x),
\qquad
M=\sup_{0\le x\le1}f(x).
\]

1. Prove that there is $t\in[0,1]$ such that $f(t)=M$.
2. Give an example showing that part 1 can fail if the monotonicity is only eventual pointwise: for each $x$ there is $n_x$ such that $f_n(x)\ge f_{n+1}(x)$ for all $n\ge n_x$.
:::

::: {.solution}
<1>1. There exists $t\in[0,1]$ such that $f(t)=M$.

::: {.proof}
For each positive integer $k$, choose $x_k\in[0,1]$ such that
$$
f(x_k)>M-\frac1k.
$$
By compactness of $[0,1]$, some subsequence
$(x_{k_j})$ converges to a point $t\in[0,1]$.

Fix a positive integer $n$. Since the sequence $(f_m(x))_m$ decreases
to $f(x)$ at every $x$,
$$
f_n(x_{k_j})\ge f(x_{k_j})>M-\frac1{k_j}.
$$
Letting $j\to\infty$ and using continuity of $f_n$ gives
$$
f_n(t)\ge M.
$$
This holds for every $n$. Therefore
$$
f(t)
=\lim_{n\to\infty}f_n(t)
\ge M.
$$
By the definition of $M$ as the supremum of $f$, also $f(t)\le M$.
Hence $f(t)=M$.
:::

<1>2. For part 2, define
$$
f_n(x)\coloneqq
x\min\{1,n(1-x)\},
\qquad
0\le x\le1.
$$
Then each $f_n$ is continuous and nonnegative.

::: {.proof}
Both functions $1$ and $n(1-x)$ are continuous, so their pointwise
minimum is continuous. Multiplication by $x\ge0$ preserves
continuity and nonnegativity.
:::

<1>3. The sequence from step <1>2 is eventually nonincreasing at
every point.

::: {.proof}
Fix $x<1$. For every integer
$$
n\ge\frac1{1-x},
$$
we have $n(1-x)\ge1$, so
$$
f_n(x)=x.
$$
Thus the sequence is eventually constant, hence eventually
nonincreasing, at every $x<1$. At $x=1$,
$$
f_n(1)=0
$$
for every $n$, so the same is true there.
:::

<1>4. The limiting function in this example does not attain its
supremum.

::: {.proof}
By step <1>3,
$$
f(x)\coloneqq\lim_{n\to\infty}f_n(x)
=
\begin{cases}
x,&0\le x<1,\\
0,&x=1.
\end{cases}
$$
Thus
$$
\sup_{0\le x\le1}f(x)=1,
$$
but $f(x)<1$ for every $x\in[0,1]$. Hence the supremum is not
attained.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves part 1, and steps <1>2--<1>4 provide the required
counterexample for part 2.
:::
:::
