---
schema: qual/card@1
id: P-UCLAB16F-01
kind: problem
title: Eigenvalues of $B$ with $ABA^{-1}=B^3$ are roots of unity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 1 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
Suppose $A, B$ are invertible $n \times n$ matrices with complex entries, such that $ABA^{-1} = B^3$. Show that all the eigenvalues of $B$ are roots of unity.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The matrices $B$ and $B^3$ have the same characteristic polynomial.


::: pf-proof

The hypothesis gives
$$
B^3=ABA^{-1}.
$$
Thus $B^3$ is similar to $B$.
Similar matrices have the same characteristic polynomial.

:::

:::

::: {.pf-step #s1-2}

If
$$
\lambda
$$
is an eigenvalue of $B$, then
$$
\lambda^3
$$
is an eigenvalue of $B$.


::: pf-proof

If
$$
Bv=\lambda v
$$
for some nonzero $v$, then
$$
B^3v=\lambda^3v.
$$
Thus $\lambda^3$ is an eigenvalue of $B^3$.
By step [](#s1-1){.pf-ref}, $B$ and $B^3$ have the same eigenvalues with algebraic multiplicity.
Hence $\lambda^3$ is also an eigenvalue of $B$.

:::

:::

::: {.pf-step #s1-3}

For every integer $r\ge0$,
$$
\lambda^{3^r}
$$
is an eigenvalue of $B$.


::: pf-proof

Proceed by induction on $r$.
For $r=0$, the number is $\lambda$, an eigenvalue by hypothesis.
If
$$
\lambda^{3^r}
$$
is an eigenvalue, step [](#s1-2){.pf-ref} implies that its cube
$$
\lambda^{3^{r+1}}
$$
is also an eigenvalue.

:::

:::

::: {.pf-step #s1-4}

There exist integers
$$
0\le s<r
$$
such that
$$
\lambda^{3^r}
=
\lambda^{3^s}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, all numbers
$$
\lambda,\lambda^3,\lambda^{3^2},\ldots
$$
belong to the finite set of eigenvalues of the $n\times n$ matrix $B$.
An infinite sequence taking values in a finite set must repeat.
Thus two terms with distinct indices are equal.

:::

:::

::: {.pf-step #s1-5}

Since $B$ is invertible,
$$
\lambda\ne0.
$$


::: pf-proof

An invertible matrix has no zero eigenvalue.

:::

:::

::: {.pf-step #s1-6}

The eigenvalue $\lambda$ satisfies
$$
\lambda^{3^s(3^{r-s}-1)}=1.
$$


::: pf-proof

From step [](#s1-4){.pf-ref},
$$
\lambda^{3^r}
=
\lambda^{3^s}.
$$
By step [](#s1-5){.pf-ref}, divide by
$$
\lambda^{3^s}
$$
to obtain
$$
\lambda^{3^r-3^s}=1.
$$
Factor the exponent:
$$
3^r-3^s
=
3^s(3^{r-s}-1).
$$

:::

:::

::: {.pf-step #s1-7}

Therefore every eigenvalue of $B$ is a root of unity.


::: pf-proof

The exponent in step [](#s1-6){.pf-ref} is a positive integer because
$$
r>s.
$$
Thus every eigenvalue $\lambda$ satisfies
$$
\lambda^N=1
$$
for some positive integer $N$, which is exactly the definition of a root of unity.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
