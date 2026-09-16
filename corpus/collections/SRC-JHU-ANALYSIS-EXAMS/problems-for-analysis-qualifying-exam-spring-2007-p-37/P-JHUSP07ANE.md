---
schema: qual/card@1
id: P-JHUSP07ANE
kind: problem
title: 'Membership of $1/x$ in $L^p(0,\infty)$'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Analysis Qualifying Exam, Spring 2007, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
For which values of $p$ does the function $x\mapsto 1/x$ belong to $L^p((0,\infty))$?
:::

::: {.solution}
<1>1. No finite exponent $1\le p<\infty$ works.
::: {.proof}
Indeed,
$$
\int_0^\infty x^{-p}\,dx
=\int_0^1x^{-p}\,dx+\int_1^\infty x^{-p}\,dx.
$$
The first integral is finite exactly when $p<1$, whereas the second is finite exactly when $p>1$. These conditions cannot hold simultaneously. For $p=1$, both integrals diverge logarithmically.
:::

<1>2. The function also fails to belong to $L^\infty((0,\infty))$.
::: {.proof}
The function $1/x$ is unbounded on every neighborhood of $0$, so its essential supremum on $(0,\infty)$ is infinite.
:::

<1>3. Q.E.D.
::: {.proof}
Steps <1>1--<1>2 show that there is no $p\in[1,\infty]$ for which $x\mapsto1/x$ belongs to $L^p((0,\infty))$.
:::
:::
