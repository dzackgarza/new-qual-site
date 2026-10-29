---
schema: qual/card@1
id: P-PRACT20-W5-21
kind: problem
title: Nonexistence of $\lim_{z\to0}\bar z^2/z^2$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 21).
---

::: {.problem}
Find $\displaystyle\lim_{z \to 0} \frac{(\overline{z})^2}{z^2}$ or show that the limit does not exist.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Along the real axis, the quotient is identically $1$ away from the
origin.


::: pf-proof

If $z=t\in\RR\setminus\{0\}$, then
\[
\overline z=z=t,
\]
so
\[
\frac{\overline z^{\,2}}{z^2}=1.
\]
Hence along this path the limit is $1$.

:::

:::

::: {.pf-step #s1-2}

Along the line $y=x$, the quotient is identically $-1$ away from the
origin.


::: pf-proof

Take
\[
z=t(1+i),
\qquad
t\in\RR\setminus\{0\}.
\]
Then
\[
\overline z=t(1-i),
\]
and therefore
\[
\frac{\overline z^{\,2}}{z^2}
=
\frac{(1-i)^2}{(1+i)^2}
=
\frac{-2i}{2i}
=-1.
\]
Hence along this path the limit is $-1$.

:::

:::

::: {.pf-step #s1-3}

Therefore
\[
\boxed{\lim_{z\to0}\frac{\overline z^{\,2}}{z^2}\text{ does not exist}}.
\]


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give two paths approaching the same point $0$ along
which the function has different limiting values, namely $1$ and $-1$.
Therefore no two-dimensional limit exists.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
