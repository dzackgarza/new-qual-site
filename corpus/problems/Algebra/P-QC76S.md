---
schema: qual/card@1
id: P-QC76S
kind: problem
title: Free modules over an integral domain are torsion-free; $\QQ$ is torsion-free
  but not free as a $\ZZ$-module
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Torsion
  - Integral Domains
relations: []
review: draft
---

::: problem
Let $R$ be an integral domain.

1. Prove that every free $R$-module is torsion-free.
2. Show that $\QQ$ is torsion-free but not free as a $\ZZ$-module.
:::

::: {.solution}
<1>1. Free modules over a domain are torsion-free.
::: {.proof}
Let $F$ be free with basis $\{e_i\}_{i\in I}$, and let
\[
0\ne x=\sum_{i\in I} r_i e_i
\]
be a finite linear combination. Choose $j$ with $r_j\ne0$.
If $0\ne a\in R$ satisfied $ax=0$, then
\[
0=ax=\sum_i ar_i e_i.
\]
Linear independence gives $ar_i=0$ for every $i$, in particular $ar_j=0$. Since $R$ is a domain and both $a,r_j$ are nonzero, this is impossible. Hence no nonzero element is torsion.
:::

<1>2. $\QQ$ is torsion-free but not free over $\ZZ$.
::: {.proof}
If $0\ne n\in\ZZ$ and $q\in\QQ$ satisfy $nq=0$, then $q=0$, so $\QQ$ is torsion-free.

Suppose $\QQ$ were free over $\ZZ$ with basis $\mathcal B$. Choose $0\ne b\in\mathcal B$. Since $\QQ$ is divisible, there exists $x\in\QQ$ with
\[
2x=b.
\]
Write the finite basis expansion
\[
x=\sum_{c\in\mathcal B} n_c c,
\qquad n_c\in\ZZ.
\]
Then
\[
b=2x=\sum_c 2n_c c.
\]
Uniqueness of basis coordinates forces the coefficient of $b$ to satisfy
\[
1=2n_b,
\]
impossible in $\ZZ$. Therefore $\QQ$ is not a free $\ZZ$-module.
:::
:::
