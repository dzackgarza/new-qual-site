---
schema: qual/card@1
id: D-65VIK
kind: definition
title: Order of a zero of a holomorphic function
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Holomorphic Functions
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open, let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$, let $z_0\in\Omega$, and let $n\ge1$ be an integer.
The point $z_0$ is a \dfn{zero of order $n$} of $f$ if there exist an open neighborhood $U\subseteq\Omega$ of $z_0$ and a holomorphic function $g\colon U\to\CC$ with $g(z_0)\neq0$ such that
$$
f(z)=(z-z_0)^n g(z)\qquad\text{for all } z\in U.
$$
A zero of order $1$ is a \dfn{simple zero}.
:::

::: {.proposition}
Let $\Omega\subseteq\CC$ be a connected open set and let $f$ be holomorphic on $\Omega$ and not identically zero.
Then every $z_0\in\Omega$ with $f(z_0)=0$ is a zero of order $n$ of $f$ for exactly one integer $n\ge1$.
:::

::: {.proof}
Existence.
Let $A$ be the set of $w\in\Omega$ with $f^{(k)}(w)=0$ for all $k\ge0$.
$A$ is closed in $\Omega$ because each $f^{(k)}$ is continuous.
$A$ is open: if $w\in A$, the Taylor series of $f$ at $w$ vanishes identically and equals $f$ on a disc about $w$, so that disc lies in $A$.
Since $f\not\equiv0$ and $\Omega$ is connected, $A=\varnothing$.
Hence there is a least $n$ with $f^{(n)}(z_0)\neq0$, and $n\ge1$ because $f(z_0)=0$.
On a disc $D\subseteq\Omega$ about $z_0$, $f(z)=\sum_{k\ge n}a_k(z-z_0)^k$ with $a_n\neq0$; take $U=D$ and $g(z)\coloneqq\sum_{k\ge n}a_k(z-z_0)^{k-n}$, which converges on $D$ and satisfies $g(z_0)=a_n\neq0$.

Uniqueness.
Suppose $(z-z_0)^n g(z)=(z-z_0)^m h(z)$ near $z_0$ with $g(z_0)\neq0$, $h(z_0)\neq0$, and $n<m$.
Then $g(z)=(z-z_0)^{m-n}h(z)$ for $z\neq z_0$ near $z_0$, and letting $z\to z_0$ gives $g(z_0)=0$, a contradiction.
:::
