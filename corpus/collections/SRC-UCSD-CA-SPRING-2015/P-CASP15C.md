---
schema: qual/card@1
id: P-CASP15C
kind: problem
title: 'Roots of $z^4-6z+3$ in an annulus'
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Rouché
  - Polynomial Roots
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The
      source is a course examination, so there is no retained solution set behind the card and the
      problem statement is the source. The two Rouché comparisons were checked by hand: on |z| = 1
      one has |z^4 + 3| <= 4 < 6 = |-6z|, and on |z| = 2, |-6z + 3| <= 15 < 16 = |z^4|. The card
      also records that no zero lies on either circle, which the strict inequalities give and
      which is what makes the subtraction 4 - 1 legitimate. Not claimed: the location of the
      individual roots, or the argument principle's finer count.
---

::: {.problem}
How many roots does the polynomial $z^4 - 6z + 3 = 0$ have in the annulus $U = \{z \in \CC \mid 1 < \abs{z} < 2\}$?
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #inner}
$z^{4}-6z+3$ has exactly one zero in $\abs{z}<1$.

::: pf-proof
On $\abs{z}=1$ we have $\abs{z^{4}+3}\le1+3=4<6=\abs{-6z}$, so $z^{4}-6z+3$ and $-6z$ satisfy the hypotheses of Rouché's theorem and have the same number of zeros in $\abs{z}<1$; that number is the single zero of $-6z$ at the origin.
:::

:::

::: {.pf-step #outer}
$z^{4}-6z+3$ has exactly four zeros in $\abs{z}<2$.

::: pf-proof
On $\abs{z}=2$ we have $\abs{-6z+3}\le12+3=15<16=\abs{z^{4}}$, so by Rouché's theorem the polynomial has as many zeros in $\abs{z}<2$ as $z^{4}$, namely four counted with multiplicity; all four lie in $\abs{z}<2$ since $\deg=4$.
:::

:::

::: {.pf-step #annulus}
The annulus $1<\abs{z}<2$ contains exactly three zeros.

::: pf-proof
The zeros in the annulus are the zeros in $\abs{z}<2$ that are not in $\abs{z}\le1$. Steps [](#inner){.pf-ref} and [](#outer){.pf-ref} count one and four respectively, and no zero lies on either circle, because Rouché's estimates give strict inequality there and force the relevant functions to be nonzero; hence the count is $4-1=3$.
:::

:::

::: {.pf-step}
The polynomial has $3$ roots in $U$.

::: pf-proof
Step [](#annulus){.pf-ref} gives
$$
\boxed{\text{the number of roots of }z^{4}-6z+3\text{ in }1<\abs{z}<2\text{ is }3.}
$$
The count is with multiplicity; the bounds $\abs{z^{4}+3}\le4<6$ and $\abs{-6z+3}\le15<16$ are both strict on their circles, which is what excludes roots on $\abs{z}=1$ and $\abs{z}=2$.
:::

:::

:::
:::
