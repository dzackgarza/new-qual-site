---
schema: qual/card@1
id: P-YKB6A
kind: problem
title: Abelianness of Galois groups is not transitive
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Abelian Groups
  - Counterexamples
relations: []
review: draft
---

::: problem
Suppose $F\subset E\subset K$, with $K/F$ Galois, and both $E/F$ and $K/E$ have abelian Galois groups. Must $\operatorname{Gal}(K/F)$ be abelian? Give counterexamples for number fields and function fields.
:::

::: solution
No.

<1>1. Number-field counterexample.

Let $K$ be the splitting field of
\[
x^3-2
\]
over $\QQ$. Then
\[
\operatorname{Gal}(K/\QQ)\cong S_3,
\]
which is nonabelian.

Let
\[
E=K^{A_3}=\QQ(\sqrt{-3}).
\]
Since $A_3\trianglelefteq S_3$,
\[
\operatorname{Gal}(E/\QQ)
\cong S_3/A_3
\cong C_2,
\]
and
\[
\operatorname{Gal}(K/E)\cong A_3\cong C_3.
\]
Both successive Galois groups are abelian, but the total group is $S_3$.

<1>2. Function-field counterexample.

Let $\omega$ be a primitive cube root of unity and let
\[
K=\CC(x).
\]
Define automorphisms
\[
r(x)=\omega x,
\qquad
s(x)=x^{-1}.
\]
They generate a group
\[
\langle r,s\rangle\cong S_3.
\]
Set
\[
E=K^{\langle r\rangle}=\CC(x^3),
\]
and
\[
F=K^{S_3}=\CC(x^3+x^{-3}).
\]
Then
\[
\operatorname{Gal}(K/E)\cong C_3,
\qquad
\operatorname{Gal}(E/F)\cong C_2,
\]
but
\[
\operatorname{Gal}(K/F)\cong S_3
\]
is nonabelian.

Thus abelianness of successive Galois groups is not transitive.
:::
