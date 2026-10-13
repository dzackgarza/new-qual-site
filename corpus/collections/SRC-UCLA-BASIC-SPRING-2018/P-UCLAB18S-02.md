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
Let $A,B\in M_5(\mathbb R)$ satisfy $A^2=A$, $B^2=B$, and suppose $I-(A+B)$ is invertible.
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

<1>1. One has
\[
\boxed{CA=-BA}.
\]

::: {.proof}
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

<1>2. One also has
\[
\boxed{BC=-BA}.
\]

::: {.proof}
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

<1>3. Therefore
\[
\boxed{CA=BC}.
\]

::: {.proof}
Both sides equal
\[
-BA
\]
by steps <1>1--<1>2.
:::

<1>4. Since $C$ is invertible,
\[
\boxed{B=CAC^{-1}}.
\]

::: {.proof}
Multiply the identity
\[
CA=BC
\]
from step <1>3 on the right by
\[
C^{-1}.
\]
This gives
\[
CAC^{-1}=B.
\]
:::

<1>5. Thus $A$ and $B$ are similar.

::: {.proof}
Step <1>4 expresses $B$ as a conjugate of $A$ by the invertible matrix $C$.
That is precisely similarity.
:::

<1>6. Similar matrices have the same rank.

::: {.proof}
Multiplication on either side by an invertible matrix does not change rank.
Hence
\[
\operatorname{rank}(CAC^{-1})
=
\operatorname{rank}(A).
\]
Using step <1>4,
\[
\operatorname{rank}(B)
=
\operatorname{rank}(A).
\]
:::

<1>7. Therefore
\[
\boxed{
\operatorname{rank}(A)=\operatorname{rank}(B).
}
\]

::: {.proof}
This is exactly step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
