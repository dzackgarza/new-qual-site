---
schema: qual/card@1
id: P-BKS03-1A
kind: problem
title: A matrix for which every nonzero vector is an eigenvector is scalar
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $k$ be a field and $A\in M_n(k)$.
Prove that the following are equivalent:

(a) $A$ is a scalar multiple of the identity.

(b) Every nonzero vector in $k^n$ is an eigenvector of $A$.
:::

::: {.solution}

The argument is the card's own: (a) is immediate, and in (b) the standard basis and then the vectors $e_{i}+e_{j}$ force all diagonal entries to agree.

::: pf

::: {.pf-step #forward}

(a) $\Rightarrow$ (b).

::: pf-proof

If $A=\lambda I$ then $Av=\lambda v$ for every $v\in k^{n}$, so every nonzero vector is an eigenvector with eigenvalue $\lambda$.

:::

:::

::: {.pf-step #diagonal}

Under (b), $A$ is diagonal with respect to the standard basis $e_{1},\dots,e_{n}$.

::: pf-proof

By (b) each $e_{j}\ne0$ is an eigenvector, say $Ae_{j}=\lambda_{j}e_{j}$. The $j$-th column of $A$ is the coordinate vector of $Ae_{j}$, namely $\lambda_{j}e_{j}$, which has $\lambda_{j}$ in position $j$ and $0$ elsewhere. So $A_{jj}=\lambda_{j}$ and $A_{ij}=0$ for $i\ne j$.

:::

:::

::: {.pf-step #equal}

$\lambda_{i}=\lambda_{j}$ for all $i,j$.

::: pf-proof

Suppose $\lambda_{i}\ne\lambda_{j}$ with $i\ne j$. The vector $w=e_{i}+e_{j}$ is nonzero, so by (b) it is an eigenvector, say $Aw=\mu w$. On the other hand step [](#diagonal){.pf-ref} gives $Aw=\lambda_{i}e_{i}+\lambda_{j}e_{j}$, and this equals $\mu e_{i}+\mu e_{j}$ only if $\lambda_{i}=\mu=\lambda_{j}$, since the $e_{k}$ form a basis. That contradicts $\lambda_{i}\ne\lambda_{j}$.

:::

:::

::: {.pf-step #conclusion}

(a) and (b) are equivalent.

::: pf-proof

Steps [](#forward){.pf-ref} and [](#equal){.pf-ref} together with the diagonal shape of step [](#diagonal){.pf-ref} show that (b) forces $A=\lambda I$ for the common value $\lambda$, and (a) forces (b):
$$
\boxed{A=\lambda I\iff\text{every nonzero vector is an eigenvector of } A.}
$$

:::

:::

:::

:::
