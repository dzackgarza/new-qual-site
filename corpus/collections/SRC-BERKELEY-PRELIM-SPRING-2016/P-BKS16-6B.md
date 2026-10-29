---
schema: qual/card@1
id: P-BKS16-6B
kind: problem
title: Optimality condition for nonnegative least squares
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Checked Problem 6B against the vendored Berkeley Spring 2016 exam. The exam states $A^T(y-Ax)\geq0$, while its supplied solution proves the opposite sign by working with $A^T(Ax-y)$.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified a one-dimensional counterexample to the printed sign and proved the corrected first-order inequality in every coordinate.
- event: solution-written
  by: deepseek-v4.1-flash-free
  date: 2026-10-27
  note: Added the solution section proving the corrected nonpositive sign; the earlier entry recorded the argument that the solution now states in full.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The exam printed that v = A^T(y-Ax) has nonnegative entries, which fails for A=(1), y=-1, x=0; the statement now asks to show that v has nonpositive entries.
---

::: {.problem}
Let $A$ be an $m\times n$ real matrix and $y\in\RR^m$.
Let $x\in\RR^n$ be a vector with nonnegative entries that minimizes the Euclidean distance $\norm{y-Ax}$ among all nonnegative vectors $x$.
Show that the vector
$$
v=A^T(y-Ax)
$$
has nonpositive entries.
:::

::: {.solution}
We prove that $v_i\le0$ for every $i$, and also that $v_i=0$ whenever $x_i>0$. Since $s\mapsto s^2$ is strictly increasing on $[0,\infty)$, the minimizer $x$ also minimizes the squared distance $\norm{y-Az}^2$ over the nonnegative vectors.

::: pf

::: {.pf-step #setup}
Let $\varphi(z)=\norm{y-Az}^2$, and let $a_i=Ae_i$ be the $i$-th column of $A$. For every real $t$,
$$
\varphi(x+te_i)=\varphi(x)-2t v_i+t^2\norm{a_i}^2.
$$

::: pf-proof
Since $y-A(x+te_i)=y-Ax-ta_i$,
$$
\norm{y-Ax-ta_i}^2
=\norm{y-Ax}^2-2t\langle a_i,y-Ax\rangle+t^2\norm{a_i}^2
=\varphi(x)-2t v_i+t^2\norm{a_i}^2.
$$
:::

:::

::: {.pf-step #one-sided}
For every $i$, $v_i\le0$.

::: pf-proof
For $t>0$, the vector $x+te_i$ has nonnegative entries, so minimality of $x$ gives $\varphi(x+te_i)\ge\varphi(x)$. By step [](#setup){.pf-ref},
$$
0\le\frac{\varphi(x+te_i)-\varphi(x)}{t}=-2v_i+t\norm{a_i}^2.
$$
Letting $t\to0^+$ gives $-2v_i\ge0$, hence $v_i\le0$.
:::

:::

::: {.pf-step #support}
If $x_i>0$, then $v_i=0$.

::: pf-proof
Choose $\delta>0$ with $x_i-\delta>0$. For every $t\in(-\delta,\delta)$, the vector $x+te_i$ has nonnegative entries, so $t=0$ is a local minimum of $t\mapsto\varphi(x+te_i)$. By step [](#setup){.pf-ref}, this function is differentiable at $0$ with derivative $-2v_i$. Hence $v_i=0$.
:::

:::

::: {.pf-step #conclusion}
Thus $v\le0$, and $x_i v_i=0$ for every $i$.

::: pf-proof
Step [](#one-sided){.pf-ref} gives $v_i\le0$ for every $i$. If $x_i>0$, step [](#support){.pf-ref} gives $v_i=0$; if $x_i=0$, then $x_i v_i=0$. Hence $x_i v_i=0$ for every $i$, and $x^Tv=0$.
:::

:::

:::

:::

