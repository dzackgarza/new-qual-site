---
schema: qual/card@1
id: P-ALGS25C
kind: problem
title: Annihilator and invariant factors of $F[x]/\langle x^n\rangle \otimes_F F[x]/\langle x^m\rangle$
classification:
  areas:
  - algebra
  topics:
  - Modules
relations: []
review: draft
---

::: problem
Suppose $F$ is a field.
Let $m \leq n$ be two positive integers and
\[
M_{m,n} := F[x]/\langle x^n\rangle \otimes_F F[x]/\langle x^m\rangle.
\]
Notice that $M_{m,n}$ is an $F[x]$-module where
\[
x \cdot \bigl(\overline{a(x)} \otimes \overline{b(x)}\bigr) = \overline{xa(x)} \otimes \overline{xb(x)}
\]
and $\overline{\bullet}$ denotes the corresponding coset.
(Let's emphasize that the tensor is over $F$, and not over $F[x]$.)

(a) Prove that $\operatorname{Ann}(M_{m,n}) = \langle x^m\rangle$.

(b) Let $d(M_{m,n})$ be the minimum number of generators of $M_{m,n}$ as an $F[x]$-module.
Prove that $d(M_{m,n}) = \dim_F(M_{m,n}/x M_{m,n}) = m + n - 1$.

(c) Find the multiplicity of $x^m$ among the invariant factors of $M_{m,n}$.
:::
