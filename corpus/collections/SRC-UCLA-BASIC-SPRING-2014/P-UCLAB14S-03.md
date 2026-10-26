---
schema: qual/card@1
id: P-UCLAB14S-03
kind: problem
title: A commutator relation forces singularity
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
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Problem 3. Suppose that $A,B\in M_{n,n}(\mathbb C)$ satisfy
\[
AB-BA=A.
\]
Show that $A$ is not invertible.
:::

::: pf

::: pf-step

Suppose, for contradiction, that $A$ is invertible.


::: pf-proof

The goal is to prove noninvertibility, so assume the negation.

:::

:::

::: pf-step

Multiplying
\[
AB-BA=A
\]
on the left by $A^{-1}$ gives
\[
B-A^{-1}BA=I.
\]


::: pf-proof

Using $A^{-1}A=I$,
\[
A^{-1}(AB-BA)=B-A^{-1}BA,
\]
while $A^{-1}A=I$ on the right-hand side.

:::

:::

::: pf-step

Taking traces gives
\[
\operatorname{tr}(B)-\operatorname{tr}(A^{-1}BA)=n.
\]


::: pf-proof

Trace is linear and $\operatorname{tr}(I_n)=n$.

:::

:::

::: pf-step

But
\[
\operatorname{tr}(A^{-1}BA)=\operatorname{tr}(B).
\]


::: pf-proof

The cyclic property of trace gives
\[
\operatorname{tr}(A^{-1}BA)
=\operatorname{tr}(BAA^{-1})
=\operatorname{tr}(B).
\]
Equivalently, $A^{-1}BA$ is similar to $B$.

:::

:::

::: pf-step

Steps <1>3--<1>4 imply
\[
0=n,
\]
a contradiction.


::: pf-proof

Substitute the equality from step <1>4 into step <1>3. Since the matrices are $n\times n$ with $n\geq1$, the scalar $n$ is nonzero in $\mathbb C$.

:::

:::

::: pf-step

Therefore
\[
\boxed{A\text{ is not invertible}.}
\]


::: pf-proof

The assumption of invertibility in step <1>1 led to the contradiction in step <1>5.

:::

:::

::: pf-qed

Step <1>6 is the desired conclusion.

:::

:::
