---
schema: qual/card@1
id: P-BKS14-7A
kind: problem
title: Number of complete flags in $\FF_q^n$ as $q\to1$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the quotient-line count, product formula for complete flags, and q->1 limit.
---

::: {.problem}
Let $F$ be a finite field with $q$ elements.
A complete flag in $F^n$ is a nested sequence
$$
V^1\subset V^2\subset\cdots\subset V^{n-1}
$$
with $\dim V^j=j$. Let $f_n(q)$ be the number of complete flags in $F^n$. Find
$$
\lim_{q\to1} f_n(q).
$$
:::

::: {.solution}
For convenience, set
$$
V^0=\{0\}.
$$

::: pf

::: {.pf-step #s1}

Suppose
$$
V^0\subset V^1\subset\cdots\subset V^k
$$
has already been chosen, with
$$
\dim V^k=k<n-1.
$$
Then the possible subspaces $V^{k+1}$ extending the partial flag are in
bijection with the one-dimensional subspaces of
$$
F^n/V^k.
$$

::: pf-proof

A subspace $V^{k+1}$ containing $V^k$ corresponds under the quotient map
to the subspace
$$
V^{k+1}/V^k
\subseteq
F^n/V^k.
$$
Its dimension is
$$
\dim V^{k+1}-\dim V^k
=
1.
$$
Conversely, the inverse image of a one-dimensional subspace of the
quotient is a $(k+1)$-dimensional subspace containing $V^k$.

:::

:::

::: {.pf-step #s2}

A $d$-dimensional vector space over $F$ has
$$
\frac{q^d-1}{q-1}
=
1+q+\cdots+q^{d-1}
$$
one-dimensional subspaces.

::: pf-proof

There are
$$
q^d-1
$$
nonzero vectors. Every one-dimensional subspace contains exactly
$$
q-1
$$
nonzero vectors, and distinct one-dimensional subspaces have disjoint
sets of nonzero vectors. Dividing gives the count.

:::

:::

::: {.pf-step #s3}

Once $V^k$ is fixed, the number of choices for $V^{k+1}$ is
$$
\frac{q^{n-k}-1}{q-1}.
$$

::: pf-proof

The quotient
$$
F^n/V^k
$$
has dimension $n-k$. Apply steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

The number of complete flags is
$$
f_n(q)
=
\prod_{k=0}^{n-2}
\frac{q^{n-k}-1}{q-1}
=
\prod_{d=2}^{n}
\left(
1+q+\cdots+q^{d-1}
\right).
$$

::: pf-proof

Choose $V^1,V^2,\ldots,V^{n-1}$ successively. By step [](#s3){.pf-ref}, the number
of choices at stage $k$ is the displayed factor. Multiplying independent
successive choice counts gives the first product. Reindex with
$$
d=n-k
$$
and use the geometric-sum identity for the second formula.

:::

:::

::: {.pf-step #s5}

For every integer $d\geq2$,
$$
\lim_{q\to1}
\left(
1+q+\cdots+q^{d-1}
\right)
=
d.
$$

::: pf-proof

The expression is a polynomial in $q$, hence continuous at $q=1$. Its
value there is the sum of $d$ copies of $1$.

:::

:::

::: {.pf-step #s6}

Therefore
$$
\boxed{
\lim_{q\to1}f_n(q)
=
n!
}.
$$

::: pf-proof

The product in step [](#s4){.pf-ref} is finite, so step [](#s5){.pf-ref} gives
$$
\lim_{q\to1}f_n(q)
=
\prod_{d=2}^n d
=
n!.
$$

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the requested limit.

:::

:::

:::
