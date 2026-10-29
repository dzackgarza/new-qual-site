---
schema: qual/card@1
id: P-ZHTDW
kind: problem
title: $\Aut((\ZZ/p)^n)$ as a matrix group
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Matrix Groups
  - Finite Fields
relations: []
review: draft
---

::: {.problem}
Identify $\Aut_\Grp(\bigoplus_{i=1}^n \ZZ/p)$ as a matrix group and determine its size.
:::

::: {.solution}
Write $V=(\ZZ/p)^n\cong \FF_p^n$.

::: pf

::: {.pf-step #linear}

$\Aut_{\Grp}(V)=\boxed{\GL_n(\FF_p)}$.

::: pf-proof

A group endomorphism $\phi$ of $V$ is $\FF_p$-linear: for $a\in\{0,\ldots,p-1\}$ and $v\in V$, $\phi(av)=\phi(v+\cdots+v)=a\phi(v)$. Hence $\Endo_{\Grp}(V)=\Endo_{\FF_p}(V)\cong M_n(\FF_p)$, and the automorphisms are the invertible linear maps.

:::

:::

::: pf-step

$\abs{\Aut_{\Grp}(V)}=\boxed{\prod_{j=0}^{n-1}(p^n-p^j)}$.

::: pf-proof

By step [](#linear){.pf-ref}, count invertible matrices by choosing columns in turn. A matrix is invertible exactly when its columns are linearly independent. Once $j$ independent columns are chosen, their span has $p^j$ elements, so the next column has $p^n-p^j$ choices.

:::

:::

:::

:::
