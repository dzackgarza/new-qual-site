---
schema: qual/card@1
id: P-DUKEBA14-9
kind: problem
title: A $C^1$ map of full rank $p$ is a linear inclusion after a change of target coordinates
classification:
  areas: [real-analysis]
  topics: [Inverse Function Theorem, Constant Rank Theorem]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part II, Problem 3 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $U\subset\RR^p$ be open and let $f:U\to\RR^n$ be $C^1$. Suppose that for some $x_0\in U$, $Df_{x_0}$ has rank $p$. Show that there is a change of variables in some neighborhood of $f(x_0)$ so that in the new coordinate system, $f$ is a linear inclusion.
:::

::: {.solution}

::: pf

::: pf-step
Choose $p$ target coordinates with an invertible Jacobian minor.

::: pf-proof
Since $Df_{x_0}$ has rank $p$, some $p\times p$ minor is invertible. After permuting the coordinates of $\RR^n$, assume it is the minor formed by the first $p$ components. Write
$$
F=(f_1,\ldots,f_p):U\to\RR^p.
$$
Then $DF_{x_0}$ is invertible.
:::

:::

::: pf-step
Invert $F$ near $x_0$.

::: pf-proof
By the inverse function theorem, there are neighborhoods $V$ of $x_0$ and $W$ of $F(x_0)$ such that
$$
F:V\to W
$$
is a $C^1$ diffeomorphism. Let $H=F^{-1}:W\to V$, and write
$$
g=(f_{p+1},\ldots,f_n):U\to\RR^{n-p},
$$
so that $f=(F,g)$.
:::

:::

::: pf-step
Define a change of variables near $f(x_0)$.

::: pf-proof
On the open set $W\times\RR^{n-p}$, which contains $f(x_0)$, define
$$
\Theta(y',y'')=\bigl(H(y'),\,y''-g(H(y'))\bigr),
\qquad
(y',y'')\in\RR^p\times\RR^{n-p}.
$$
It is $C^1$ and maps onto $V\times\RR^{n-p}$. The $C^1$ map
$$
(x,w)\longmapsto\bigl(F(x),\,w+g(x)\bigr)
$$
on $V\times\RR^{n-p}$ is its inverse, since $F(H(y'))=y'$ and $H(F(x))=x$. Thus $\Theta$ is a $C^1$ change of variables on a neighborhood of $f(x_0)$.
:::

:::

::: pf-step
In the new coordinates $f$ is a linear inclusion.

::: pf-proof
For $x\in V$, $f(x)=(F(x),g(x))$ lies in $W\times\RR^{n-p}$, and
$$
\Theta(f(x))=\bigl(H(F(x)),\,g(x)-g(H(F(x)))\bigr)=(x,0).
$$
Hence, in the coordinate system $\Theta$ near $f(x_0)$, the map $f$ is the linear inclusion
$$
x\longmapsto(x,0)\in\RR^p\times\RR^{n-p}.
$$
:::

:::

:::
:::
