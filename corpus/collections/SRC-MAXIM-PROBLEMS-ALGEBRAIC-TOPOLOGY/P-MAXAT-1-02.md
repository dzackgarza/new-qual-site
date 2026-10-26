---
schema: qual/card@1
id: P-MAXAT-1-02
kind: problem
title: Maxim algebraic topology 1.2
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 1, problem 2 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that $\mathbb { R P } ^ { 2 n } , \mathbb { C P } ^ { 2 n }$ , HP2n cannot be boundaries.
:::

Assume $n\geq1$. By the preceding Euler-characteristic criterion, the boundary of a compact manifold must have even Euler characteristic.

::: pf

::: pf-step

Real projective space $\mathbb{RP}^{2n}$ has a CW decomposition with exactly one cell in every dimension
\[
0,1,\ldots,2n.
\]


::: pf-proof

The standard filtration
\[
\mathbb{RP}^0\subset\mathbb{RP}^1\subset\cdots\subset\mathbb{RP}^{2n}
\]
is obtained by attaching one $k$-cell in passing from $\mathbb{RP}^{k-1}$ to $\mathbb{RP}^k$.

:::

:::

::: pf-step

Therefore
\[
\chi(\mathbb{RP}^{2n})
=\sum_{k=0}^{2n}(-1)^k=1.
\]


::: pf-proof

Euler characteristic is the alternating sum of the numbers of cells in a finite CW decomposition. Step <1>1 gives one cell in each dimension. Since the sum has an odd number $2n+1$ of alternating terms beginning and ending with $+1$, its value is $1$.

:::

:::

::: pf-step

Complex projective space $\mathbb{CP}^{2n}$ has one cell in each even real dimension
\[
0,2,4,\ldots,4n
\]
and no odd-dimensional cells.


::: pf-proof

The standard filtration
\[
\mathbb{CP}^0\subset\mathbb{CP}^1\subset\cdots\subset\mathbb{CP}^{2n}
\]
attaches one real $2k$-cell at the $k$th stage.

:::

:::

::: pf-step

Hence
\[
\chi(\mathbb{CP}^{2n})=2n+1.
\]


::: pf-proof

All $2n+1$ cells from step <1>3 have even dimension, so each contributes $+1$ to the Euler characteristic.

:::

:::

::: pf-step

Quaternionic projective space $\mathbb{HP}^{2n}$ has one cell in each real dimension
\[
0,4,8,\ldots,8n,
\]
so
\[
\chi(\mathbb{HP}^{2n})=2n+1.
\]


::: pf-proof

The standard projective-space filtration attaches one quaternionic $k$-cell, of real dimension $4k$, at each stage. Thus there are $2n+1$ cells, all in even real dimensions, and every cell contributes $+1$ to the Euler characteristic.

:::

:::

::: pf-step

Each of the three Euler characteristics is odd.


::: pf-proof

Step <1>2 gives $1$ for $\mathbb{RP}^{2n}$, while steps <1>4--<1>5 give $2n+1$ for the complex and quaternionic projective spaces. These integers are odd.

:::

:::

::: pf-step

None of these manifolds can be the boundary of a compact manifold.


::: pf-proof

If any one were such a boundary, its Euler characteristic would be even by the boundary theorem proved in the preceding problem. Step <1>6 gives a contradiction in each case.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\mathbb{RP}^{2n},\ \mathbb{CP}^{2n},\ \mathbb{HP}^{2n}
\text{ are not boundaries}.}
\]


::: pf-proof

This is step <1>7 applied to the three projective spaces.

:::

:::

::: pf-qed

Step <1>8 is the required conclusion.

:::

:::
