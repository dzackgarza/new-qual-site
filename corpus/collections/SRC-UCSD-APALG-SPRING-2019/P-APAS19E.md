---
schema: qual/card@1
id: P-APAS19E
kind: problem
title: Same character need not imply isomorphic representations of $\mathrm{GL}_2(\mathbb{R})$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: {.problem}
Let $G=\mathrm{GL}_2(\mathbb{R})$ be the group of invertible $2\times 2$ real matrices and let $X,Y\colon G\to\mathrm{GL}_d(\mathbb{C})$ be two complex matrix representations of $G$ with the same degree $d$.
If $X$ and $Y$ have the same character, are $X$ and $Y$ necessarily isomorphic?
Justify your answer.
:::

::: {.solution}
No. For infinite groups, equality of characters need not imply that two finite-dimensional complex representations are isomorphic.

Take \(d=2\). Since
\[
\ell(g)=\log|\det g|
\]
is a homomorphism from \(\mathrm{GL}_2(\mathbb R)\) to the additive group \((\mathbb R,+)\), define
\[
X(g)=
\begin{pmatrix}
1&\ell(g)\\
0&1
\end{pmatrix},
\qquad
Y(g)=I_2.
\]
Then
\[
X(gh)=
\begin{pmatrix}1&\ell(g)+\ell(h)\\0&1\end{pmatrix}
=X(g)X(h),
\]
so \(X\) is a representation, and \(Y\) is the two-dimensional trivial representation.

For every \(g\in G\),
\[
\chi_X(g)=\operatorname{tr}X(g)=2=\operatorname{tr}Y(g)=\chi_Y(g).
\]
Thus \(X\) and \(Y\) have the same character.

They are not isomorphic. If they were, there would be an invertible matrix \(S\) such that
\[
SX(g)S^{-1}=Y(g)=I_2
\]
for every \(g\). This would force \(X(g)=I_2\) for every \(g\), which is false; for example, for \(g=2I_2\),
\[
\ell(g)=\log 4\ne0.
\]
Hence equal characters do not imply isomorphic representations in this infinite-group setting.
:::
