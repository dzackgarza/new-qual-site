---
schema: qual/card@1
id: P-BKF05-7B
kind: problem
title: The Cayley transform of a Hermitian operator is unitary
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
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained adjoint computation. The proof below
    makes invertibility of I-iT explicit before its inverse is used and checks
    the unitary identity using commutativity of the two polynomial expressions
    in T.
---

::: {.problem}
Let \(V\) be a finite-dimensional complex inner-product space and let \(T:V\to V\) be Hermitian.

(a) Prove that \(I+iT\) is invertible.

(b) Prove that
\[
(I-iT)(I+iT)^{-1}
\]
is unitary.
:::

::: {.solution}
<1>1. (a) The operator $I+iT$ is invertible.

::: {.proof}
It suffices, since $V$ is finite-dimensional, to prove that $I+iT$ is
injective. Suppose
$$
(I+iT)v=0.
$$
Since $T$ is Hermitian, $\inner{v}{Tv}$ is real. Hence the two cross
terms cancel in
$$
\begin{aligned}
\norm{(I+iT)v}^2
&=
\norm{v+iTv}^2
\\
&=
\norm v^2+\norm{Tv}^2.
\end{aligned}
$$
The left side is zero, so both nonnegative terms on the right vanish.
In particular $\norm v=0$, hence $v=0$. Thus $I+iT$ is injective and
hence invertible.
:::

<1>2. The operator $I-iT$ is also invertible.

::: {.proof}
Since $T^*=T$,
$$
(I+iT)^*=I-iT.
$$
The adjoint of an invertible operator is invertible, with
$$
\big((I+iT)^*\big)^{-1}
=
\big((I+iT)^{-1}\big)^*.
$$
Step <1>1 therefore implies that $I-iT$ is invertible.
:::

<1>3. (b) If
$$
A=(I-iT)(I+iT)^{-1},
$$
then
$$
A^*=(I-iT)^{-1}(I+iT).
$$

::: {.proof}
Using $(BC)^*=C^*B^*$, step <1>2, and $T^*=T$ gives
$$
\begin{aligned}
A^*
&=
\big((I+iT)^{-1}\big)^*(I-iT)^*
\\
&=
\big((I+iT)^*\big)^{-1}(I+iT)
\\
&=
(I-iT)^{-1}(I+iT).
\end{aligned}
$$
:::

<1>4. The operator $A$ is unitary.

::: {.proof}
The operators $I+iT$ and $I-iT$ commute, since both are polynomials
in $T$. Therefore step <1>3 gives
$$
\begin{aligned}
A^*A
&=
(I-iT)^{-1}(I+iT)(I-iT)(I+iT)^{-1}
\\
&=
(I-iT)^{-1}(I-iT)(I+iT)(I+iT)^{-1}
\\
&=
I.
\end{aligned}
$$
Thus $A^*=A^{-1}$, so $A$ is unitary.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves part (a), and step <1>4 proves part (b).
:::
:::
