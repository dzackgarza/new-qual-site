---
schema: qual/card@1
id: P-CASP23A
kind: problem
title: "Power series with radius of convergence 1: divergence, absolute convergence, singularities, and nonnegative coefficients"
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Radius of Convergence
  - Analytic Continuation
  - Singularities
relations: []
review: draft
---

::: {.problem}
Let $A(z) = \sum_{n=0}^\infty a_n z^n$ be a power series with radius of convergence equal to one.

(a) Give an example where $A(z)$ diverges at each point of $\circlegroup$, and explain why.

(b) Give an example where $A(z)$ converges absolutely on $\circlegroup$, and explain why.

(c) Prove that $A(z)$ has a singularity on $\circlegroup$, i.e. cannot be analytically continued to an open set containing $\overline{\DD}$.

(d) Prove that if $A(z)$ has nonnegative coefficients, the point $z = 1$ is a singularity of $A(z)$. (Hint: the previous problem could be useful.)

(e) Verify that $A(z) = \sum_{n=0}^\infty z^{n!}$ has radius of convergence one, and that each point of $\circlegroup$ is a singularity of $A(z)$.
:::

::: {.remark}
The official Spring 2023 UCSD exam has $A(z)=\sum_{n=0}^\infty z^{n!}$ in
part (e). An earlier transcription of this card incorrectly read
$\sum n!z^n$, which has radius of convergence $0$.
:::

::: {.solution}

The examples and the three arguments are the card's own; the two steps that the original compressed — the compactness in (c) and the convergence radius about $r$ in (d) — are expanded, because in both the conclusion depends on a point strictly beyond the unit circle being reached.

Let $A(z)=\sum_{n\ge0}a_{n}z^{n}$ have radius of convergence $1$.

::: pf

::: {.pf-step #a}
(a) $A(z)=\sum_{n\ge0}z^{n}$ has radius $1$ and diverges at every point of $\circlegroup$.

::: pf-proof
The coefficients are $a_{n}=1$, so $\limsup\abs{a_{n}}^{1/n}=1$ and the radius is $1$. For $\abs z=1$ the terms are $z^{n}$, of modulus $1$, so they do not tend to $0$ and the series diverges by the vanishing test.
:::

:::

::: {.pf-step #b}
(b) $A(z)=\sum_{n\ge1}z^{n}/n^{2}$ has radius $1$ and converges absolutely on $\circlegroup$.

::: pf-proof
$\limsup\abs{a_{n}}^{1/n}=\limsup n^{-2/n}=1$, since $n^{2/n}\to1$, so the radius is $1$. For $\abs z=1$ the terms have modulus $1/n^{2}$ and $\sum_{n\ge1}n^{-2}<\infty$, so the series converges absolutely there.
:::

:::

::: {.pf-step #c}
(c) $A$ has at least one singularity on $\circlegroup$: it cannot be continued analytically to an open set containing $\overline{\DD}$.

::: pf-proof
Suppose $f$ is holomorphic on an open set $U\supseteq\overline\DD$ and agrees with $A$ on $\DD$. For each $z$ with $\abs z=1$ there is $\rho_{z}>0$ with $B(z,\rho_{z})\subset U$; the balls $B(z,\rho_{z}/2)$ cover the compact circle, so finitely many of them do, say for $z_{1},\ldots,z_{m}$, and then the disc $\{\abs w<1\}\cup\bigcup_{j}B(z_{j},\rho_{z_{j}})$ contains $\{\abs w<1+\varepsilon\}$ for some $\varepsilon>0$: a point $w$ with $1\le\abs w<1+\varepsilon$ is within $\varepsilon$ of the circle, and $\varepsilon$ taken below $\min_{j}\rho_{z_{j}}/2$ puts it in one of the chosen balls. So $f$ is holomorphic on $\{\abs w<1+\varepsilon\}$, and its Taylor series at $0$ is $\sum a_{n}w^{n}$ because $f=A$ on $\DD$ and Taylor coefficients are derivatives at $0$. That series would then have radius at least $1+\varepsilon$, contradicting radius $1$.
:::

:::

::: {.pf-step #d}
(d) If $a_{n}\ge0$ for all $n$, then $z=1$ is a singularity of $A$.

::: pf-proof

::: {.pf-step #positive}
For $0<r<1$ and $k\ge0$, $\dfrac{A^{(k)}(r)}{k!}=\displaystyle\sum_{n\ge k}\binom{n}{k}a_{n}r^{n-k}\ge0$, and the Taylor series of $A$ about $r$ converges at $r+s$ for every $0<s<2\delta$ if $A$ is holomorphic on $D(1,2\delta)$ with $r=1-\delta$.

::: pf-proof
The derivatives of a power series inside its disc are computed by termwise differentiation, giving the displayed formula, and every term is nonnegative because $a_{n}\ge0$, $r>0$ and $\binom{n}{k}>0$. If $A$ is holomorphic on $D(1,2\delta)$ and $r=1-\delta$, then every point $r+s$ with $0\le s\le2\delta$ satisfies $\abs{(r+s)-1}=\abs{s-\delta}\le2\delta$, so the segment from $r$ to $1+\delta$ lies in $D(1,2\delta)$, where $A$ is holomorphic; hence the Taylor series of $A$ about $r$ converges on a disc about $r$ of radius more than $\delta$, in particular at each $r+s$ with $0<s<2\delta$.
:::

:::

::: {.pf-step #rearrange}
Under the hypothesis of the previous step, $\displaystyle\sum_{k\ge0}\frac{A^{(k)}(r)}{k!}s^{k}=\sum_{n\ge0}a_{n}(r+s)^{n}$ for $0<s<2\delta$, and the sum is finite.

::: pf-proof
Substituting the formula for $A^{(k)}(r)/k!$ and using nonnegativity to apply Tonelli's theorem (all terms are nonnegative, so the double sum may be computed in either order, finite or infinite),
$$
\sum_{k\ge0}\frac{A^{(k)}(r)}{k!}s^{k}=\sum_{k\ge0}\sum_{n\ge k}\binom{n}{k}a_{n}r^{n-k}s^{k}=\sum_{n\ge0}a_{n}\sum_{k=0}^{n}\binom{n}{k}r^{n-k}s^{k}=\sum_{n\ge0}a_{n}(r+s)^{n},
$$
the inner sum being the binomial expansion of $(r+s)^{n}$. The left side is the value at $r+s$ of a convergent Taylor series, by step [](#positive){.pf-ref}, so it is finite.
:::

:::

::: {.pf-qed}
Suppose $A$ were holomorphic on a neighbourhood of $1$; choose $\delta>0$ with $A$ holomorphic on $D(1,2\delta)$ and put $r=1-\delta$. Pick $s$ with $\delta<s<2\delta$. By step [](#rearrange){.pf-ref}, $\sum_{n}a_{n}(r+s)^{n}<\infty$ with $r+s>1$, so the series $\sum a_{n}z^{n}$ converges at the point $z=r+s$ of modulus greater than $1$, contradicting the radius $1$. Hence $A$ is not holomorphic near $1$, that is $1$ is a singularity.
:::

:::

:::

::: {.pf-step #e}
(e) $A(z)=\sum_{n\ge0}z^{n!}$ has radius $1$, and every point of $\circlegroup$ is a singularity.

::: pf-proof
As an ordinary power series its coefficients are $a_{m}=1$ when $m=n!$ and $a_{m}=0$ otherwise; there are infinitely many $m$ with $a_{m}=1$ and all satisfy $a_{m}\le1$, so $\limsup_{m}\abs{a_{m}}^{1/m}=1$ and the radius is $1$. The nonzero exponents $n_{k}=k!$ satisfy $n_{k+1}/n_{k}=k+1\to\infty$, in particular $n_{k+1}/n_{k}\ge2$ for every $k\ge1$; by Hadamard's gap theorem a power series whose exponents satisfy $n_{k+1}/n_{k}\ge\lambda>1$ eventually has the circle of convergence as a natural boundary, that is no point of the circle is a regular point. So every point of $\circlegroup$ is a singularity of $A$.
:::

:::

:::
:::
