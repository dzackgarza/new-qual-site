---
schema: qual/card@1
id: P-COY2N
kind: problem
title: $\sup_{\norm{g}_1\le 1}\norm{fg}_1=\norm{f}_\infty$ for continuous $f$ on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Norms
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against entry 6 of the UGA Fall 2015 real-analysis qualifying exam recorded by the collection.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $f: [0, 1] \to \RR$ be continuous.
Show that
$$
\sup \left\{\norm{f g}_{1} \suchthat g \in L^{1}[0,1],~~ \norm{g}_{1} \leq 1\right\}=\norm{f}_{\infty}.
$$
:::

::: {.solution}

::: pf

::: pf-step

Prove the upper bound.

::: pf-proof

For every $g\in L^1([0,1])$ with $\norm{g}_1\le1$,
$$
\norm{fg}_1
=\int_0^1\abs{f(x)g(x)}\,dx
\le \norm{f}_\infty\norm{g}_1
\le \norm{f}_\infty.
$$
Hence
$$
\sup_{\norm{g}_1\le1}\norm{fg}_1\le\norm{f}_\infty.
$$

:::

:::

::: pf-step

Prove the reverse inequality.

::: pf-proof

Since $f$ is continuous on the compact interval $[0,1]$, there is $x_0\in[0,1]$ such that
$$
\abs{f(x_0)}=\norm{f}_\infty.
$$
Fix $\varepsilon>0$. By continuity, there is a measurable interval $I\subset[0,1]$ of positive length containing $x_0$ such that
$$
\abs{f(x)}\ge \norm{f}_\infty-\varepsilon
\qquad(x\in I).
$$
Set
$$
g=\frac{\mathbf1_I}{m(I)}.
$$
Then $\norm{g}_1=1$ and
$$
\norm{fg}_1
=\frac1{m(I)}\int_I\abs{f(x)}\,dx
\ge \norm{f}_\infty-\varepsilon.
$$
Therefore
$$
\sup_{\norm{g}_1\le1}\norm{fg}_1\ge \norm{f}_\infty-\varepsilon.
$$
Letting $\varepsilon\downarrow0$ gives the reverse inequality. Thus
$$
\boxed{
\sup_{\norm{g}_1\le1}\norm{fg}_1=\norm{f}_\infty.}
$$

:::

:::

:::

:::
