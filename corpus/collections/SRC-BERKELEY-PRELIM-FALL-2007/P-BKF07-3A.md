---
schema: qual/card@1
id: P-BKF07-3A
kind: problem
title: A Hermitian matrix has the same kernel as its square
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
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Hermitian norm argument.
---

::: {.problem}
Let \(A\) be an \(n\times n\) Hermitian matrix and let \(x\in\mathbb C^n\). Prove that
\[
A^2x=0\quad\Longrightarrow\quad Ax=0.
\]
:::

::: {.solution}
<1>1. If $A^2x=0$, then
$$
x^*A^*Ax=0.
$$

::: {.proof}
Since $A$ is Hermitian,
$$
A^*=A.
$$
Therefore
$$
x^*A^*Ax
=
x^*A^2x
=
x^*0
=
0.
$$
:::

<1>2. One has
$$
x^*A^*Ax=\|Ax\|^2.
$$

::: {.proof}
By the standard Hermitian inner product on $\CC^n$,
$$
x^*A^*Ax
=(Ax)^*(Ax)
=
\langle Ax,Ax\rangle
=
\|Ax\|^2.
$$
:::

<1>3. Hence
$$
\boxed{Ax=0}.
$$

::: {.proof}
Steps <1>1--<1>2 give
$$
\|Ax\|^2=0.
$$
Positive definiteness of the norm implies $Ax=0$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required implication.
:::
:::
