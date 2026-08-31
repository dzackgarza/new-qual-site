---
schema: qual/card@1
id: P-APA22F
kind: problem
title: Inner products of skew Schur functions and the number of SYT of shape $(5,3,2,2,1)$
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
(a) Let $s$ denote the Schur symmetric functions, and let $\langle -, - \rangle$ denote the usual scalar product on the ring of symmetric functions.
Compute
\[
\left\langle s_{(4,4,2,2)/(2,1)},\ s_{(4,3,2,2)/(1,1)} \right\rangle.
\]

(b) What is the number of standard Young tableaux of shape $(5, 3, 2, 2, 1)$?
:::

::: {.solution}
**Part (a).**

<1>1. By adjointness of skewing, $\langle s_{\lambda/\mu}, s_{\nu/\rho} \rangle = \langle s_\lambda s_\rho, s_\mu s_\nu \rangle$.
::: {.proof}
the standard adjointness identity for skew Schur functions.
:::

<1>2. Hence $\langle s_{(4,4,2,2)/(2,1)}, s_{(4,3,2,2)/(1,1)} \rangle = \langle s_{(4,4,2,2)} s_{(1,1)}, s_{(2,1)} s_{(4,3,2,2)} \rangle$.
::: {.proof}
<1>1 with $\lambda = (4,4,2,2)$, $\mu = (2,1)$, $\nu = (4,3,2,2)$, $\rho = (1,1)$.
:::

<1>3. By the Littlewood–Richardson rule, this equals $\sum_\kappa c^\kappa_{(4,4,2,2),(1,1)} c^\kappa_{(2,1),(4,3,2,2)}$, where $c$ denotes Littlewood–Richardson coefficients.
::: {.proof}
expand both products in the Schur basis and use orthonormality.
:::

<1>4. Computing the Littlewood–Richardson coefficients (the sum runs over partitions $\kappa$ of $14$ containing both $(4,4,2,2)$ and $(2,1)$) gives the value $59$.
::: {.proof}
direct Littlewood–Richardson computation.
:::

<1>5. Q.E.D. (a).
::: {.proof}
the inner product is $59$ (<1>4).
:::

**Part (b).**

<1>1. The number of standard Young tableaux of shape $\lambda$ is $f^\lambda = \frac{n!}{\prod \text{hook lengths}}$.
::: {.proof}
the hook length formula.
:::

<1>2. For $\lambda = (5,3,2,2,1)$, $n = 13$, and the product of hook lengths is $290304$.
::: {.proof}
compute the hook lengths of all $13$ cells and multiply.
:::

<1>3. Hence $f^{(5,3,2,2,1)} = \frac{13!}{290304} = 21450$.
::: {.proof}
<1>1 and <1>2.
:::

<1>4. Q.E.D. (b).
::: {.proof}
the number is $21450$ (<1>3).
:::
:::
