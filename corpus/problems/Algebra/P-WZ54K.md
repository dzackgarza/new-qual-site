---
schema: qual/card@1
id: P-WZ54K
kind: problem
title: $x^{p^n}-x$ is the product of monic irreducibles in $\FF_p[x]$ of degree dividing
  $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Factorization
  - Irreducibility Criteria
relations: []
review: draft
---

::: problem
Prove that
\[
x^{p^n}-x
\]
is the product of all monic irreducible polynomials in $\FF_p[x]$ whose degrees divide $n$.
:::

::: solution
Let $f\in\FF_p[x]$ be monic irreducible of degree $d$, and let $\alpha$ be one of its roots. Then
\[
\FF_p(\alpha)\cong\FF_{p^d}.
\]
Hence
\[
f\mid x^{p^n}-x
\]
if and only if $\alpha\in\FF_{p^n}$, equivalently
\[
\FF_{p^d}\subseteq\FF_{p^n}.
\]
The subfield criterion for finite fields gives
\[
\FF_{p^d}\subseteq\FF_{p^n}\iff d\mid n.
\]
Thus the irreducible factors are exactly the monic irreducibles whose degrees divide $n$.

Finally,
\[
\frac{d}{dx}(x^{p^n}-x)=-1,
\]
so $x^{p^n}-x$ is squarefree. Therefore every such irreducible occurs with multiplicity one, and
\[
x^{p^n}-x
=\prod_{\substack{f\text{ monic irreducible}\\ \deg f\mid n}} f(x).
\]
:::
