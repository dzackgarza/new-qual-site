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
Suppose $A , B$ are invertible $n \times n$ matrices with complex entries, such that $A B A ^ { - 1 } = B ^ { 3 }$ . Show that all the eigenvalues of B are roots of unity.
:::

::: {.solution}
<1>1. The matrices $B$ and $B^3$ have the same characteristic polynomial.

::: {.proof}
The hypothesis gives
\[
B^3=ABA^{-1}.
\]
Thus $B^3$ is similar to $B$.
Similar matrices have the same characteristic polynomial.
:::

<1>2. If
\[
\lambda
\]
is an eigenvalue of $B$, then
\[
\lambda^3
\]
is an eigenvalue of $B$.

::: {.proof}
If
\[
Bv=\lambda v
\]
for some nonzero $v$, then
\[
B^3v=\lambda^3v.
\]
Thus $\lambda^3$ is an eigenvalue of $B^3$.
By step <1>1, $B$ and $B^3$ have the same eigenvalues with algebraic multiplicity.
Hence $\lambda^3$ is also an eigenvalue of $B$.
:::

<1>3. For every integer $r\ge0$,
\[
\lambda^{3^r}
\]
is an eigenvalue of $B$.

::: {.proof}
Proceed by induction on $r$.
For $r=0$, the number is $\lambda$, an eigenvalue by hypothesis.
If
\[
\lambda^{3^r}
\]
is an eigenvalue, step <1>2 implies that its cube
\[
\lambda^{3^{r+1}}
\]
is also an eigenvalue.
:::

<1>4. There exist integers
\[
0\le s<r
\]
such that
\[
\lambda^{3^r}
=
\lambda^{3^s}.
\]

::: {.proof}
By step <1>3, all numbers
\[
\lambda,\lambda^3,\lambda^{3^2},\ldots
\]
belong to the finite set of eigenvalues of the $n\times n$ matrix $B$.
An infinite sequence taking values in a finite set must repeat.
Thus two terms with distinct indices are equal.
:::

<1>5. Since $B$ is invertible,
\[
\lambda\ne0.
\]

::: {.proof}
An invertible matrix has no zero eigenvalue.
:::

<1>6. The eigenvalue $\lambda$ satisfies
\[
\lambda^{3^s(3^{r-s}-1)}=1.
\]

::: {.proof}
From step <1>4,
\[
\lambda^{3^r}
=
\lambda^{3^s}.
\]
By step <1>5, divide by
\[
\lambda^{3^s}
\]
to obtain
\[
\lambda^{3^r-3^s}=1.
\]
Factor the exponent:
\[
3^r-3^s
=
3^s(3^{r-s}-1).
\]
:::

<1>7. Therefore every eigenvalue of $B$ is a root of unity.

::: {.proof}
The exponent in step <1>6 is a positive integer because
\[
r>s.
\]
Thus every eigenvalue $\lambda$ satisfies
\[
\lambda^N=1
\]
for some positive integer $N$, which is exactly the definition of a root of unity.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
