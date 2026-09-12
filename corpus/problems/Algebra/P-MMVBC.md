---
schema: qual/card@1
id: P-MMVBC
kind: problem
title: The Galois group of $x^4-2$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Find the Galois group of $x^4-2$ over $\QQ$.
:::

::: {.solution}
Let
\[
\alpha=2^{1/4}.
\]
The roots are
\[
\alpha,-\alpha,i\alpha,-i\alpha,
\]
so the splitting field is
\[
L=\QQ(\alpha,i).
\]

The polynomial $x^4-2$ is Eisenstein at $2$, hence
\[
[\QQ(\alpha):\QQ]=4.
\]
Since $\QQ(\alpha)\subset\RR$ but $i\notin\RR$,
\[
[L:\QQ]=8.
\]
Thus the Galois group has order $8$.

Define automorphisms
\[
r(\alpha)=i\alpha,
\qquad r(i)=i,
\]
and
\[
s(\alpha)=\alpha,
\qquad s(i)=-i.
\]
Then
\[
r^4=s^2=1,
\]
and
\[
srs=r^{-1}.
\]
Moreover, $r$ has order $4$, $s$ has order $2$, and together they generate all $8$ automorphisms.

Hence
\[
\Gal(L/\QQ)
\cong
\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle,
\]
the dihedral group of order $8$.
:::
