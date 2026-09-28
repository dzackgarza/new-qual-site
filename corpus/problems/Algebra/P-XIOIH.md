---
schema: qual/card@1
id: P-XIOIH
kind: problem
title: $\GF(p^d)\subseteq\GF(p^n)$ iff $d$ divides $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Prove
\[
\GF(p^d)\subseteq\GF(p^n)
\iff
d\mid n.
\]
:::

::: {.solution}
Suppose first that
\[
\FF_{p^d}\subseteq\FF_{p^n}.
\]
Then the extension degree satisfies
\[
[\FF_{p^n}:\FF_p]
=[\FF_{p^n}:\FF_{p^d}]
[\FF_{p^d}:\FF_p].
\]
Thus
\[
n=[\FF_{p^n}:\FF_{p^d}]\,d,
\]
so $d\mid n$.

Conversely, suppose $d\mid n$, say $n=dm$. Every element of $\FF_{p^d}$ satisfies
\[
x^{p^d}=x.
\]
Hence
\[
x^{p^n}=x^{(p^d)^m}=x,
\]
so every element of $\FF_{p^d}$ is a root of $x^{p^n}-x$. The roots of this polynomial in an algebraic closure are exactly the elements of $\FF_{p^n}$. Therefore
\[
\FF_{p^d}\subseteq\FF_{p^n}.
\]
:::
