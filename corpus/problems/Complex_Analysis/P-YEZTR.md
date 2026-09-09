---
schema: qual/card@1
id: P-YEZTR
kind: problem
title: $\lim a_n/a_{n+1}=z_0$ for the power series of a function with a pole at $z_0\in\partial\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Poles
  - Convergence Tests
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
Suppose that $f$ is holomorphic on an open set containing the closed unit disk $\overline{\mathbb{D}} = \{z \in \mathbb{C} \mid |z| \le 1\}$ except for a single pole at $z_0 \in \partial\mathbb{D}$ ($|z_0| = 1$).
Let $\sum_{n=0}^\infty a_n z^n$ be the Maclaurin series expansion of $f$ in $\mathbb{D}$.
Prove that:
$$\lim_{n \to \infty} \frac{a_n}{a_{n+1}} = z_0.$$
:::

::: solution
Let the pole at $z_0$ have order $m$. Its principal part can be written
$$
Q(z)=\sum_{j=1}^m\frac{c_j}{(z_0-z)^j},
\qquad c_m\ne0.
$$
After subtracting $Q$, the function $g=f-Q$ is holomorphic on a neighborhood of the closed unit disk. Hence there is some $R>1$ such that $g$ is holomorphic on $D_R(0)$.

<1>1. For $|z|<1$,
$$
\frac1{(z_0-z)^j}
=\sum_{n=0}^\infty
\binom{n+j-1}{j-1}z_0^{-(n+j)}z^n.
$$
Thus, if $q_n$ denotes the $n$th Taylor coefficient of $Q$,
$$
q_n=\sum_{j=1}^m c_j
\binom{n+j-1}{j-1}z_0^{-(n+j)}.
$$
The term $j=m$ has highest polynomial degree in $n$, so
$$
q_n=
\frac{c_m}{(m-1)!}n^{m-1}z_0^{-(n+m)}
\left(1+O(n^{-1})\right).
$$

<1>2. Write $g(z)=\sum b_nz^n$. Cauchy's estimates on any circle of radius $r$ with $1<r<R$ give $b_n=O(r^{-n})$. Hence the Taylor coefficients $a_n=q_n+b_n$ of $f$ satisfy
$$
a_n=
\frac{c_m}{(m-1)!}n^{m-1}z_0^{-(n+m)}
\left(1+O(n^{-1})\right),
$$
because the exponentially decaying $b_n$ is negligible compared with the nonzero polynomial-size leading term.

Therefore, for all sufficiently large $n$, $a_{n+1}\ne0$, and
$$
\frac{a_n}{a_{n+1}}
=z_0\left(\frac{n}{n+1}\right)^{m-1}
\frac{1+O(n^{-1})}{1+O((n+1)^{-1})}
\longrightarrow z_0.
$$
:::
