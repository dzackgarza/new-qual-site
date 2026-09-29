---
schema: qual/card@1
id: P-BKF20-7A
kind: problem
title: Counting subspaces of a finite vector space
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
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 counting argument. Counting
    ordered independent k-tuples and dividing by the number of ordered bases
    of a fixed k-subspace gives the stated Gaussian binomial coefficient; an
    exponent typo in the extracted source is not propagated.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the number of choices at each stage of an independent k-tuple,
    the constant number of bases per k-subspace, and the product-index
    simplification to the requested formula.
---

::: {.problem}
Let $V$ be $n$-dimensional over the finite field with $q$ elements. Prove that the number of $k$-dimensional subspaces $W\subseteq V$ equals
\[
\frac{\prod_{j=1}^n(q^j-1)}{\left(\prod_{j=1}^k(q^j-1)\right)\left(\prod_{j=1}^{n-k}(q^j-1)\right)}.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The number of ordered linearly independent $k$-tuples in $V$ is
$$
\prod_{i=0}^{k-1}(q^n-q^i).
$$

::: pf-proof

There are
$$
q^n-1
$$
choices for the first vector. After choosing $i$ linearly independent
vectors, their span has exactly $q^i$ elements. Hence the next vector
may be any of the
$$
q^n-q^i
$$
vectors outside that span. Multiplying these choices for
$i=0,\ldots,k-1$ gives the formula.

:::

:::

::: {.pf-step #s2}

Every fixed $k$-dimensional subspace $W\subseteq V$ has exactly
$$
\prod_{i=0}^{k-1}(q^k-q^i)
$$
ordered bases.

::: pf-proof

The same argument as in step [](#s1){.pf-ref} applies inside $W$, which has
$q^k$ elements. An ordered basis is exactly an ordered linearly
independent $k$-tuple in $W$.

:::

:::

::: {.pf-step #s3}

If $N_{n,k}(q)$ denotes the number of $k$-dimensional subspaces
of $V$, then
$$
N_{n,k}(q)
=
\frac{\prod_{i=0}^{k-1}(q^n-q^i)}
{\prod_{i=0}^{k-1}(q^k-q^i)}.
$$

::: pf-proof

Every ordered linearly independent $k$-tuple spans a unique
$k$-dimensional subspace. Conversely, for each such subspace $W$, the
ordered independent $k$-tuples spanning it are precisely its ordered
bases, whose number is the quantity in step [](#s2){.pf-ref}.

Thus the set counted in step [](#s1){.pf-ref} is partitioned into equally sized
blocks indexed by the $k$-dimensional subspaces, and division gives the
displayed formula.

:::

:::

::: {.pf-step #s4}

The quotient in step [](#s3){.pf-ref} equals
$$
\frac{
\prod_{j=n-k+1}^{n}(q^j-1)
}{
\prod_{j=1}^{k}(q^j-1)
}.
$$

::: pf-proof

For each $i$,
$$
q^n-q^i
=
q^i(q^{n-i}-1)
$$
and
$$
q^k-q^i
=
q^i(q^{k-i}-1).
$$
The factors $q^i$ cancel in the quotient of step [](#s3){.pf-ref}, leaving
$$
\frac{
\prod_{i=0}^{k-1}(q^{n-i}-1)
}{
\prod_{i=0}^{k-1}(q^{k-i}-1)
}.
$$
Reindexing the numerator by
$$
j=n-i
$$
and the denominator by
$$
j=k-i
$$
gives the claim.

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{
N_{n,k}(q)
=
\frac{\prod_{j=1}^n(q^j-1)}
{\left(\prod_{j=1}^k(q^j-1)\right)
\left(\prod_{j=1}^{n-k}(q^j-1)\right)}.
}
$$

::: pf-proof

Factor
$$
\prod_{j=1}^{n}(q^j-1)
=
\left(
\prod_{j=1}^{n-k}(q^j-1)
\right)
\left(
\prod_{j=n-k+1}^{n}(q^j-1)
\right).
$$
Solving this identity for the second product and substituting it into
step [](#s4){.pf-ref} gives exactly the displayed expression.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required count.

:::

:::

:::
