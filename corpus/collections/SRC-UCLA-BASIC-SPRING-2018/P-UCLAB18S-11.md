---
schema: qual/card@1
id: P-UCLAB18S-11
kind: problem
title: An isometry of a compact metric space is onto
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Let $(X,\rho)$ be a compact metric space and let $f:X\to X$ be an isometry.
Prove that $f$ is surjective.

Hint: assume $x\notin f(X)$ and follow the iterates of $f$ on $x$.
:::

::: {.solution}
<1>1. Suppose, for contradiction, that $f$ is not surjective. Then there is $x_0\in X\setminus f(X)$ and a number $\delta>0$ such that
$$
\rho(x_0,y)\ge\delta
$$
for every $y\in f(X)$.

::: {.proof}
If $f$ is not surjective, choose $x_0\notin f(X)$. The map $f$ is an isometry and hence continuous, so $f(X)$ is compact as the continuous image of the compact space $X$. Therefore the continuous function $y\mapsto\rho(x_0,y)$ attains its minimum on $f(X)$. Since $x_0\notin f(X)$, that minimum is strictly positive; denote it by $\delta$.
:::

<1>2. Define $x_n=f^n(x_0)$ for $n\ge0$. If $m>n$, then
$$
\rho(x_m,x_n)\ge\delta.
$$

::: {.proof}
Because $f$ preserves distances, so does every iterate $f^n$. Hence, for $m>n$,
$$
\rho(x_m,x_n)
=\rho\bigl(f^n(x_{m-n}),f^n(x_0)\bigr)
=\rho(x_{m-n},x_0).
$$
Since $m-n\ge1$, one has
$$
x_{m-n}=f(x_{m-n-1})\in f(X).
$$
The definition of $\delta$ in step <1>1 therefore gives $\rho(x_{m-n},x_0)\ge\delta$.
:::

<1>3. The sequence $(x_n)_{n\ge0}$ has no convergent subsequence.

::: {.proof}
By step <1>2, any two distinct terms of the sequence are at distance at least $\delta$. Every convergent sequence is Cauchy, whereas no subsequence of $(x_n)$ can be Cauchy: for two distinct terms in any subsequence, their distance is at least $\delta$. Hence no subsequence converges.
:::

<1>4. Q.E.D.

::: {.proof}
Compact metric spaces are sequentially compact, so every sequence in $X$ has a convergent subsequence. Step <1>3 contradicts this for the sequence $(x_n)$. Therefore the assumption in step <1>1 was false, and $f$ is surjective.
:::
:::
