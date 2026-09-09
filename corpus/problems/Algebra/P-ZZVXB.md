---
schema: qual/card@1
id: P-ZZVXB
kind: problem
title: Abelian groups of order 9, and groups of order 27
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Abelian Groups
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
(1) Classify all abelian groups of order 9 up to isomorphism. Prove that they are not isomorphic to each other.
(2) Classify all abelian groups of order 27 up to isomorphism, and list the non-abelian groups of order 27.
:::

::: solution
For order
\[
9=3^2,
\]
the fundamental theorem of finite abelian groups gives exactly
\[
\boxed{C_9,\qquad C_3\times C_3}.
\]
They are not isomorphic because $C_9$ has an element of order $9$, whereas every nonidentity element of $C_3^2$ has order $3$.

For order
\[
27=3^3,
\]
the abelian groups are
\[
\boxed{C_{27},\qquad C_9\times C_3,\qquad C_3^3}.
\]
Their exponents are respectively $27,9,3$, so they are pairwise nonisomorphic.

There are exactly two nonabelian groups of order $27$. One is the Heisenberg group
\[
UT_3(\mathbb F_3)
=
\left\{
\begin{pmatrix}
1&a&b\\0&1&c\\0&0&1
\end{pmatrix}
:a,b,c\in\mathbb F_3
\right\},
\]
which has exponent $3$. The other is the nontrivial semidirect product
\[
C_9\rtimes C_3
=\langle x,y\mid x^9=y^3=1,\ yxy^{-1}=x^4\rangle,
\]
which contains elements of order $9$. Hence these two are nonisomorphic.

Thus there are five groups of order $27$ up to isomorphism: three abelian and two nonabelian.
:::
