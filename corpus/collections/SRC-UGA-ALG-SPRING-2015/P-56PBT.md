---
schema: qual/card@1
id: P-56PBT
kind: problem
title: The additive group of a finite field and cyclicity of its multiplicative group
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Structure Theorem
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $\FF$ be a finite field.

a. Give (with proof) the decomposition of the additive group $(\FF, +)$ into a direct sum of cyclic groups.

b. The *exponent* of a finite group is the least common multiple of the orders of its elements.
   Prove that a finite abelian group has an element of order equal to its exponent.

c. Prove that the multiplicative group $(\units{\FF}, \cdot)$ is cyclic.
:::

::: {.solution}

::: pf

::: {.pf-step #additive}

If $\operatorname{char}\FF=p$ and $[\FF:\FF_p]=n$, then $(\FF,+)\cong(\ZZ/p\ZZ)^{\oplus n}$.

::: pf-proof

The characteristic of a field is $0$ or prime, and it is not $0$ because $\FF$ is finite. So the prime subfield is $\FF_p\cong\ZZ/p\ZZ$, and $\FF$ is a finite-dimensional $\FF_p$-vector space, of some dimension $n$. A choice of basis gives an $\FF_p$-linear, hence additive, isomorphism $\FF\cong\FF_p^{\,n}$.

:::

:::

::: {.pf-step #exponent}

A finite abelian group $G$ has an element whose order is $\exp(G)$.

::: pf-proof

By the structure theorem, $G\cong\ZZ/d_1\oplus\cdots\oplus\ZZ/d_k$ with $d_1\mid d_2\mid\cdots\mid d_k$. Every element has order dividing $d_k$, so $\exp(G)\mid d_k$. The element $(0,\ldots,0,1)$ has order $d_k$, so $d_k\mid\exp(G)$. Hence this element has order $\exp(G)$.

:::

:::

::: {.pf-step #cyclic}

$\FF^\times$ is cyclic.

::: pf-proof

Let $N=\cardinality{\FF^\times}$ and $m=\exp(\FF^\times)$. By Step [](#exponent){.pf-ref} there is $g\in\FF^\times$ of order $m$, and $m\le N$ by Lagrange's theorem. Every $x\in\FF^\times$ satisfies $x^m=1$, so the polynomial $T^m-1$ has at least $N$ roots in the field $\FF$. A nonzero polynomial of degree $m$ over a field has at most $m$ roots, so $N\le m$. Hence $g$ has order $N$ and generates $\FF^\times$.

:::

:::

::: pf-qed

Steps [](#additive){.pf-ref}, [](#exponent){.pf-ref} and [](#cyclic){.pf-ref} prove parts (a), (b) and (c).

:::

:::

:::
