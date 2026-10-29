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
Show that $\RP ^ { 2 n } , \CP ^ { 2 n }$ , HP2n cannot be boundaries.
:::

::: {.solution}

Assume $n\geq1$. By the preceding Euler-characteristic criterion, the boundary of a compact manifold must have even Euler characteristic.

::: pf

::: {.pf-step #s1-1}

Real projective space $\RP^{2n}$ has a CW decomposition with exactly one cell in every dimension
\[
0,1,\ldots,2n.
\]


::: pf-proof

The standard filtration
\[
\RP^0\subset\RP^1\subset\cdots\subset\RP^{2n}
\]
is obtained by attaching one $k$-cell in passing from $\RP^{k-1}$ to $\RP^k$.

:::

:::

::: {.pf-step #s1-2}

Therefore
\[
\chi(\RP^{2n})
=\sum_{k=0}^{2n}(-1)^k=1.
\]


::: pf-proof

Euler characteristic is the alternating sum of the numbers of cells in a finite CW decomposition. Step [](#s1-1){.pf-ref} gives one cell in each dimension. Since the sum has an odd number $2n+1$ of alternating terms beginning and ending with $+1$, its value is $1$.

:::

:::

::: {.pf-step #s1-3}

Complex projective space $\CP^{2n}$ has one cell in each even real dimension
\[
0,2,4,\ldots,4n
\]
and no odd-dimensional cells.


::: pf-proof

The standard filtration
\[
\CP^0\subset\CP^1\subset\cdots\subset\CP^{2n}
\]
attaches one real $2k$-cell at the $k$th stage.

:::

:::

::: {.pf-step #s1-4}

Hence
\[
\chi(\CP^{2n})=2n+1.
\]


::: pf-proof

All $2n+1$ cells from step [](#s1-3){.pf-ref} have even dimension, so each contributes $+1$ to the Euler characteristic.

:::

:::

::: {.pf-step #s1-5}

Quaternionic projective space $\quatprojective^{2n}$ has one cell in each real dimension
\[
0,4,8,\ldots,8n,
\]
so
\[
\chi(\quatprojective^{2n})=2n+1.
\]


::: pf-proof

The standard projective-space filtration attaches one quaternionic $k$-cell, of real dimension $4k$, at each stage. Thus there are $2n+1$ cells, all in even real dimensions, and every cell contributes $+1$ to the Euler characteristic.

:::

:::

::: {.pf-step #s1-6}

Each of the three Euler characteristics is odd.


::: pf-proof

Step [](#s1-2){.pf-ref} gives $1$ for $\RP^{2n}$, while steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} give $2n+1$ for the complex and quaternionic projective spaces. These integers are odd.

:::

:::

::: {.pf-step #s1-7}

None of these manifolds can be the boundary of a compact manifold.


::: pf-proof

If any one were such a boundary, its Euler characteristic would be even by the boundary theorem proved in the preceding problem. Step [](#s1-6){.pf-ref} gives a contradiction in each case.

:::

:::

::: {.pf-step #s1-8}

Therefore
\[
\boxed{
\RP^{2n},\ \CP^{2n},\ \quatprojective^{2n}
\text{ are not boundaries}.}
\]


::: pf-proof

This is step [](#s1-7){.pf-ref} applied to the three projective spaces.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
