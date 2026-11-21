---
schema: qual/card@1
id: P-BKF04-7B
kind: problem
title: Dimension of the span of commutators $AB-BA$ in $M_n(\RR)$
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose proof into numbered steps and re-checked it: the reduction to
    elementary commutators, the four-case product computation, the spanning set of off-diagonal
    matrices and consecutive diagonal differences, their independence, and the trace-zero
    identification. Nothing was changed mathematically. Not checked against a printed source: the
    Berkeley preliminary examinations are not retained in tmp/sources and the card records no
    page.
---

::: {.problem}
Let $n\geq1$, and let $M_n(\RR)$ be the ring of $n\times n$ matrices over the field of real numbers. What is the dimension of the subspace $V$ of $M_n(\RR)$ spanned by the matrices of the form $AB-BA$ where $A,B\in M_n(\RR)$?
:::

::: {.solution}

The argument is the card's own: no solution set for this source is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $E_{ij}$ is the matrix with $1$ in position $(i,j)$ and $0$ elsewhere, $AB-BA$ is the commutator, and $V$ is the span of all commutators in $M_n(\RR)$.

::: pf

::: {.pf-step #span}

$V$ is spanned by the commutators $E_{ij}E_{k\ell}-E_{k\ell}E_{ij}$.

::: pf-proof

The commutator is linear in $A$ and in $B$, so the span of all $AB-BA$ equals the span of the values on a spanning set of pairs; the $E_{ij}$ span $M_n(\RR)$.

:::

:::

::: {.pf-step #product}

$E_{ij}E_{k\ell}=\delta_{jk}E_{i\ell}$ and $E_{k\ell}E_{ij}=\delta_{\ell i}E_{kj}$.

::: pf-proof

Multiplying elementary matrices: a product of two such matrices is the elementary matrix indexed by the outer indices when the inner indices agree, and $0$ otherwise.

:::

:::

::: {.pf-step #cases}

$E_{ij}E_{k\ell}-E_{k\ell}E_{ij}$ is $0$ if $j\neq k$ and $i\neq\ell$, is $E_{i\ell}$ if $j=k$ and $i\neq\ell$, is $-E_{kj}$ if $j\neq k$ and $i=\ell$, and is $E_{ii}-E_{jj}$ if $j=k$ and $i=\ell$.

::: pf-proof

Substitute step [](#product){.pf-ref} in the four cases.

:::

:::

::: {.pf-step #span2}

$V$ is spanned by $\theset{E_{ij}\mid i\neq j}\cup\theset{E_{ii}-E_{i+1,i+1}\mid 1\leq i\leq n-1}$.

::: pf-proof

By steps [](#span){.pf-ref} and [](#cases){.pf-ref}, $V$ is spanned by the off-diagonal $E_{ij}$ and the differences $E_{ii}-E_{jj}$; and $E_{ii}-E_{jj}$ is a sum of consecutive differences $E_{ii}-E_{i+1,i+1}+\cdots+E_{j-1,j-1}-E_{jj}$ when $i<j$, or the negative of such a sum when $i>j$.

:::

:::

::: {.pf-step #indep}

These $n^{2}-n+n-1$ matrices are linearly independent.

::: pf-proof

A relation $\sum_{i\neq j}c_{ij}E_{ij}+\sum_{i}d_{i}(E_{ii}-E_{i+1,i+1})=0$ has off-diagonal entries $c_{ij}=0$ and diagonal entries $d_{1},d_{2}-d_{1},\dots,d_{n-1}-d_{n-2},-d_{n-1}$, all zero, so every $d_{i}=0$ by induction; the matrices are supported in distinct matrix positions.

:::

:::

::: {.pf-step #dim}

$\dim V=n^{2}-1$.

::: pf-proof

Steps [](#span2){.pf-ref} and [](#indep){.pf-ref}: a spanning set of $n^{2}-n+n-1=n^{2}-1$ independent matrices.

:::

:::

::: {.pf-step #trace}

$V$ is the space of trace-zero matrices.

::: pf-proof

Every commutator has trace $\operatorname{tr}(AB)-\operatorname{tr}(BA)=0$, so $V$ lies in the trace-zero hyperplane; that hyperplane has dimension $n^{2}-1$, equal to $\dim V$ by step [](#dim){.pf-ref}.

:::

:::

:::

:::
