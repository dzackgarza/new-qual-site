---
schema: qual/card@1
id: P-UCLAB06W-07
kind: problem
title: Cauchy--Schwarz inequality in a complex inner product space
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the official UCLA Basic Qual Winter 2006 PDF.
---

::: {.problem}
Let $V$ be a complex inner product space and let $v,w\in V$.
Prove the Cauchy--Schwarz inequality
\[
|(v,w)|\leq |v|\,|w|.
\]
:::

Use the convention that the complex inner product is linear in its first argument.

::: pf

::: pf-step

If $w=0$, then the Cauchy--Schwarz inequality holds.


::: pf-proof

If $w=0$, then
$$
\langle v,w\rangle=0
$$
and
$$
\norm{w}=0.
$$
Thus both sides of
$$
\abs{\langle v,w\rangle}\le\norm{v}\,\norm{w}
$$
are zero.

:::

:::

::: pf-step

Suppose $w\ne0$ and define
$$
\alpha=\frac{\langle v,w\rangle}{\norm{w}^2},
\qquad
u=v-\alpha w.
$$
Then
$$
\langle u,w\rangle=0.
$$


::: pf-proof

By linearity in the first argument,
$$
\langle u,w\rangle
=
\langle v,w\rangle
-
\alpha\langle w,w\rangle
=
\langle v,w\rangle
-
\frac{\langle v,w\rangle}{\norm{w}^2}\norm{w}^2
=0.
$$

:::

:::

::: pf-step

One has
$$
\norm{v}^2
=
\norm{u}^2+\abs{\alpha}^2\norm{w}^2.
$$


::: pf-proof

Since $v=u+\alpha w$ and $u\perp w$ by step <1>2,
$$
\begin{aligned}
\norm{v}^2
&=\langle u+\alpha w,u+\alpha w\rangle\\
&=\norm{u}^2+\abs{\alpha}^2\norm{w}^2,
\end{aligned}
$$
because both cross terms vanish.

:::

:::

::: pf-step

Therefore
$$
\abs{\langle v,w\rangle}^2
\le
\norm{v}^2\norm{w}^2.
$$


::: pf-proof

Step <1>3 and nonnegativity of $\norm{u}^2$ give
$$
\norm{v}^2
\ge
\abs{\alpha}^2\norm{w}^2.
$$
Using the definition of $\alpha$,
$$
\abs{\alpha}^2\norm{w}^2
=
\frac{\abs{\langle v,w\rangle}^2}{\norm{w}^2}.
$$
Multiplying by the positive number $\norm{w}^2$ gives the claim.

:::

:::

::: pf-step

Hence
$$
\boxed{
\abs{\langle v,w\rangle}
\le
\norm{v}\,\norm{w}
}.
$$


::: pf-proof

Both sides in step <1>4 are nonnegative. Taking square roots gives the displayed inequality.

:::

:::

::: pf-qed

Step <1>1 handles $w=0$, and steps <1>2--<1>5 handle $w\ne0$.

:::

:::
