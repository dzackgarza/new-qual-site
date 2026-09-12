---
schema: qual/card@1
id: E-SMI-8000E-FEE
kind: problem
title: Proof choice — algebraicity of finite extensions or existence of root fields
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared both proof choices with Smith 8000 Fall 2006 final part E; solved option (i)."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "For an arbitrary element alpha, used linear dependence of 1, alpha, ..., alpha^n in the finite-dimensional k-vector space E to produce a nonzero annihilating polynomial."
---

::: {.exercise}
Prove one:

(i) If $k$ is a field and $E$ a finite dimensional extension field (as $k$-vector space), then $E$ is algebraic over $k$;

or

(ii) If $k$ is a field and $f$ a polynomial of degree $\geq 1$ in $k[X]$, there is a field $E$ containing $k$ in which $f$ has at least one root.
:::

::: solution
We prove option (i).

<1>1. Every element of $E$ satisfies a nonzero polynomial over $k$.
::: proof
Let
$$
n=\dim_k E<\infty
$$
and fix any $\alpha\in E$. The $n+1$ vectors
$$
1,\alpha,\alpha^2,\ldots,\alpha^n
$$
belong to the $n$-dimensional $k$-vector space $E$, so they are linearly
dependent. Hence there are scalars
$$
c_0,c_1,\ldots,c_n\in k,
$$
not all zero, such that
$$
c_0+c_1\alpha+\cdots+c_n\alpha^n=0.
$$
Define
$$
p(X)=c_0+c_1X+\cdots+c_nX^n\in k[X].
$$
Because the coefficients are not all zero, $p$ is a nonzero polynomial, and
the displayed dependence says
$$
p(\alpha)=0.
$$
Therefore $\alpha$ is algebraic over $k$.
:::

<1>2. Conclude that the extension is algebraic.
::: proof
The element $\alpha\in E$ was arbitrary. Thus every element of $E$ is
algebraic over $k$, which is exactly the statement that
$$
\boxed{E/k\text{ is algebraic}.}
$$
:::
:::
