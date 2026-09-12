---
schema: qual/card@1
id: P-APAF25H
kind: problem
title: Characters of complex representations of $S_n$ are real-valued
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: problem
Let $(V,\varphi)$ be a complex representation of the symmetric group $S_n$, and let $\chi$ be its character.
Prove that $\chi(g)\in\mathbb{R}$ for all $g\in S_n$.
:::

::: {.solution}
<1>1. Every finite-dimensional complex representation of the finite group \(S_n\) admits an invariant Hermitian inner product.
::: {.proof}
Start with any positive-definite Hermitian inner product \(\langle\cdot,\cdot\rangle_0\) on \(V\) and define
\[
\langle v,w\rangle
:=\frac1{|S_n|}\sum_{h\in S_n}
\langle\varphi(h)v,\varphi(h)w\rangle_0.
\]
This is again positive definite and Hermitian. For \(g\in S_n\), left multiplication permutes the summation index, so
\[
\langle\varphi(g)v,\varphi(g)w\rangle=\langle v,w\rangle.
\]
Thus every \(\varphi(g)\) is unitary for this inner product.
:::

<1>2. For every \(g\in S_n\),
\[
\overline{\chi(g)}=\chi(g^{-1}).
\]
::: {.proof}
By <1>1, \(\varphi(g)\) is unitary, so
\[
\varphi(g^{-1})=\varphi(g)^{-1}=\varphi(g)^*.
\]
Hence
\[
\chi(g^{-1})
=\operatorname{Tr}(\varphi(g)^*)
=\overline{\operatorname{Tr}(\varphi(g))}
=\overline{\chi(g)}.
\]
:::

<1>3. Every permutation \(g\in S_n\) is conjugate to \(g^{-1}\).
::: {.proof}
A permutation and its inverse have exactly the same cycle lengths: reversing a cycle does not change its length. Conjugacy classes in \(S_n\) are determined by cycle type. Hence \(g\) and \(g^{-1}\) are conjugate.
:::

<1>4. Therefore \(\chi(g)\in\mathbb R\) for every \(g\in S_n\).
::: {.proof}
Characters are constant on conjugacy classes, so <1>3 gives
\[
\chi(g^{-1})=\chi(g).
\]
Combining with <1>2,
\[
\overline{\chi(g)}=\chi(g^{-1})=\chi(g).
\]
A complex number equal to its complex conjugate is real.
:::
:::
