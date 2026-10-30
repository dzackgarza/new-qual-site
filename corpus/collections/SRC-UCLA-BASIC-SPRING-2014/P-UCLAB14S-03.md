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
Suppose that $A,B\in M_{n,n}(\CC)$ satisfy
$$
AB-BA=A.
$$
Show that $A$ is not invertible.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose, for contradiction, that $A$ is invertible.


::: pf-proof

The goal is to prove noninvertibility, so assume the negation.

:::

:::

::: pf-step

Multiplying
$$
AB-BA=A
$$
on the left by $A^{-1}$ gives
$$
B-A^{-1}BA=I.
$$


::: pf-proof

Using $A^{-1}A=I$,
$$
A^{-1}(AB-BA)=B-A^{-1}BA,
$$
while $A^{-1}A=I$ on the right-hand side.

:::

:::

::: {.pf-step #s1-3}

Taking traces gives
$$
\operatorname{tr}(B)-\operatorname{tr}(A^{-1}BA)=n.
$$


::: pf-proof

Trace is linear and $\operatorname{tr}(I_n)=n$.

:::

:::

::: {.pf-step #s1-4}

But
$$
\operatorname{tr}(A^{-1}BA)=\operatorname{tr}(B).
$$


::: pf-proof

The cyclic property of trace gives
$$
\operatorname{tr}(A^{-1}BA)
=\operatorname{tr}(BAA^{-1})
=\operatorname{tr}(B).
$$
Equivalently, $A^{-1}BA$ is similar to $B$.

:::

:::

::: {.pf-step #s1-5}

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} imply
$$
0=n,
$$
a contradiction.


::: pf-proof

Substitute the equality from step [](#s1-4){.pf-ref} into step [](#s1-3){.pf-ref}. Since the matrices are $n\times n$ with $n\geq1$, the scalar $n$ is nonzero in $\CC$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{A\text{ is not invertible}.}
$$


::: pf-proof

The assumption of invertibility in step [](#s1-1){.pf-ref} led to the contradiction in step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the desired conclusion.

:::

:::

:::
