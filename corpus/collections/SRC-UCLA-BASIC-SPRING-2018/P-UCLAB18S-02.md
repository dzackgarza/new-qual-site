---
schema: qual/card@1
id: P-UCLAB18S-02
kind: problem
title: Ranks of two idempotent matrices
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Let $A,B\in M_5(\RR)$ satisfy $A^2=A$, $B^2=B$, and suppose $I-(A+B)$ is invertible.
Prove that
\[
\operatorname{rank}(A)=\operatorname{rank}(B).
\]
:::

::: {.solution}

Define
\[
C=I-A-B.
\]
By hypothesis, $C$ is invertible.

::: pf

::: {.pf-step #s1-1}

One has
\[
\boxed{CA=-BA}.
\]


::: pf-proof

Using
\[
A^2=A,
\]
compute
\[
\begin{aligned}
CA
&=
(I-A-B)A\\
&=
A-A^2-BA\\
&=
A-A-BA\\
&=
-BA.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-2}

One also has
\[
\boxed{BC=-BA}.
\]


::: pf-proof

Using
\[
B^2=B,
\]
compute
\[
\begin{aligned}
BC
&=
B(I-A-B)\\
&=
B-BA-B^2\\
&=
B-BA-B\\
&=
-BA.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-3}

Therefore
\[
\boxed{CA=BC}.
\]


::: pf-proof

Both sides equal
\[
-BA
\]
by steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Since $C$ is invertible,
\[
\boxed{B=CAC^{-1}}.
\]


::: pf-proof

Multiply the identity
\[
CA=BC
\]
from step [](#s1-3){.pf-ref} on the right by
\[
C^{-1}.
\]
This gives
\[
CAC^{-1}=B.
\]

:::

:::

::: pf-step

Thus $A$ and $B$ are similar.


::: pf-proof

Step [](#s1-4){.pf-ref} expresses $B$ as a conjugate of $A$ by the invertible matrix $C$.
That is precisely similarity.

:::

:::

::: {.pf-step #s1-6}

Similar matrices have the same rank.


::: pf-proof

Multiplication on either side by an invertible matrix does not change rank.
Hence
\[
\operatorname{rank}(CAC^{-1})
=
\operatorname{rank}(A).
\]
Using step [](#s1-4){.pf-ref},
\[
\operatorname{rank}(B)
=
\operatorname{rank}(A).
\]

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{
\operatorname{rank}(A)=\operatorname{rank}(B).
}
\]


::: pf-proof

This is exactly step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
