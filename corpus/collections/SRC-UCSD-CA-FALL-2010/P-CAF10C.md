---
schema: qual/card@1
id: P-CAF10C
kind: problem
title: "Uniform limit of injective analytic functions is injective or constant"
classification:
  areas:
  - complex-analysis
  topics:
  - Hurwitz
  - Univalent Functions
  - Sequences of Functions
relations: []
review: draft
---

::: problem
Let $G$ be a domain and $\{f_n\}_{n=1}^{\infty}$ a sequence of analytic functions in $G$ that converge to $f$ in $H(G)$.
Assume that each $f_n$ is 1-to-1. Show that $f$ is either constant or 1-to-1.
:::

::: solution
Assume that $f$ is not constant. We prove that it is injective.

Suppose instead that there are distinct points $a,b\in G$ with
\[
f(a)=f(b).
\]
Choose disjoint closed disks around $a$ and $b$ contained in $G$. For each
$n$, define
\[
g_n(z)=f_n(z)-f_n(a).
\]
Because $f_n$ is injective, $g_n$ has exactly one zero in $G$, namely $a$.
Moreover, local uniform convergence $f_n\to f$ implies
\[
g_n\longrightarrow g:=f-f(a)
\]
locally uniformly on $G$.

The function $g$ is not identically zero because $f$ is nonconstant, and it
has zeros at both $a$ and $b$. Apply Hurwitz's theorem in a small disk around
$b$ not containing $a$. Since $g$ has a zero at $b$, for all sufficiently
large $n$, $g_n$ must have a zero in that disk. This contradicts the fact that
the only zero of $g_n$ is $a$.

Therefore no two distinct points have the same image, so $f$ is injective.
Hence the locally uniform limit of injective holomorphic functions is either
constant or injective.
:::
