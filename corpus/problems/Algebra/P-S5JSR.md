---
schema: qual/card@1
id: P-S5JSR
kind: problem
title: The Galois group of $x^n-2$ is dihedral exactly for $n=3,4,6$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
---

::: {.problem}
Let $n\ge3$. For the splitting field of $x^n-2$ over $\QQ$, prove the affine embedding
\[
\Gal\hookrightarrow (\ZZ/n\ZZ)\rtimes(\ZZ/n\ZZ)^\times
\]
and prove that the Galois group is dihedral of order $2n$ exactly for $n=3,4,6$.
:::

::: {.solution}
Let $\alpha=2^{1/n}$ and let $\zeta_n$ be primitive. The roots are $\zeta_n^j\alpha$, so the splitting field is
\[
L=\QQ(\alpha,\zeta_n).
\]
Every automorphism has the form
\[
\sigma(\alpha)=\zeta_n^a\alpha,
\qquad
\sigma(\zeta_n)=\zeta_n^b,
\]
with $a\in\ZZ/n\ZZ$ and $b\in(\ZZ/n\ZZ)^\times$, giving an injection into the affine group with law
\[
(a,b)(c,d)=(a+bc,bd).
\]

For $n=3,4,6$, the cyclotomic field has degree $2$ and intersects the real pure field $\QQ(\alpha)$ trivially, so $[L:\QQ]=2n$. The translation $\alpha\mapsto\zeta_n\alpha$ has order $n$, complex conjugation has order $2$, and conjugation inverts the translation. Hence the group is $D_{2n}$.

Conversely, if the group were $D_{2n}$, then its cyclotomic quotient $(\ZZ/n\ZZ)^\times$ would be an abelian quotient of a dihedral group, hence would have order at most $4$ and exponent at most $2$. This reduces to $n=3,4,5,6,8,10,12$. The cases $5,10$ are excluded because the unit group is $C_4$. The case $8$ has order $16$ but generators satisfying $srs=r^3$ rather than $r^{-1}$, and the case $12$ would force $\sqrt2\in\QQ(\zeta_{12})$, impossible. Thus exactly $n=3,4,6$ are dihedral.
:::