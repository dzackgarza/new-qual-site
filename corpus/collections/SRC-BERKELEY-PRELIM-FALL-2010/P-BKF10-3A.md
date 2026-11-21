---
schema: qual/card@1
id: P-BKF10-3A
kind: problem
title: Bounded isolated singularities are removable
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance repaired, the defect this date's COMPLAINTS screen recorded ("opens with the step
    statement"). The solution now opens with the provenance paragraph the convention asks for, naming
    the retained packet: Problem 3A of `assets/attachments/f10solutions.pdf`, printed p. 2 of that
    file, read in its text layer in this pass. The card's four steps are that solution's three --- the
    Laurent coefficient formula on the circle of radius $r$, the estimate $\abs{c_j}\le Mr^{-j}$ from
    $\abs{f}\le M$, and the passage $r\to0^+$ --- with the hypotheses written out; the problem
    statement is the packet's Problem 3A. Checked: the packet read at its pp. 1--2, both the statement
    and the solution; `qualc.authoring check`; the Lamport filter, five numbered steps with QED
    present. Not checked: no other card of this collection was read in this pass.
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 3A of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the Laurent-coefficient formula and the small-circle estimate
    forcing every negative coefficient to vanish.
---

::: {.problem}
Suppose that $f$ is bounded and analytic on a deleted neighborhood $0<\abs{z}<\varepsilon$ of the origin.
Let
$$
f(z)=\sum_{j=-\infty}^{\infty}c_jz^j
$$
be the Laurent expansion of $f$.
Show that if $j<0$, then $c_j=0$.
:::

::: {.solution}

The argument is Problem 3A of the retained Berkeley preliminary-exam solution packet, `assets/attachments/f10solutions.pdf`, printed p. 2 of that file, transcribed: the Laurent coefficient formula on the circle $\abs{z}=r$, the maximum estimate $\abs{c_j}\le Mr^{-j}$ it draws from $\abs{f}\le M$, and the passage $r\to0^+$ that kills the coefficients with $j<0$ are that solution's three steps. What the card adds is the step structure and the hypotheses written out --- that $M$ exists by boundedness, and that the circle $\abs{z}=r$ lies in the annulus of analyticity for every $0<r<\varepsilon$ --- not the argument.

::: pf

::: pf-step

Choose $M>0$ such that
$$
\abs{f(z)}\le M
$$
for all $0<\abs{z}<\varepsilon$.

::: pf-proof

Such an $M$ exists by the boundedness hypothesis.

:::

:::

::: {.pf-step #s2}

For every integer $j$ and every $0<r<\varepsilon$,
$$
c_j
=\frac1{2\pi i}
\int_{\abs{z}=r}z^{-j-1}f(z)\,dz.
$$

::: pf-proof

This is the Laurent coefficient formula applied on the circle
$\abs{z}=r$, which lies in the annulus of analyticity.

:::

:::

::: {.pf-step #s3}

For every integer $j$ and every $0<r<\varepsilon$,
$$
\abs{c_j}\le M r^{-j}.
$$

::: pf-proof

By step [](#s2){.pf-ref} and the ML estimate,
$$
\begin{aligned}
\abs{c_j}
&\le\frac1{2\pi}
   \max_{\abs{z}=r}\abs{z^{-j-1}f(z)}\cdot 2\pi r\\
&\le\frac1{2\pi}r^{-j-1}M\cdot2\pi r\\
&=Mr^{-j}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s4}

If $j<0$, then $c_j=0$.

::: pf-proof

For fixed $j<0$, the exponent $-j$ is positive. Step [](#s3){.pf-ref} holds for
every $0<r<\varepsilon$, so letting $r\to0^+$ gives
$$
0\le\abs{c_j}\le Mr^{-j}\longrightarrow0.
$$
Therefore $\abs{c_j}=0$, hence $c_j=0$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves that every negative Laurent coefficient vanishes.

:::

:::

:::
