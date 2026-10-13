---
schema: qual/card@1
id: P-BKS21-3A
kind: problem
title: Uniform convergence of $\sum_n\sin(x/n^2)$ on bounded intervals
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2021 M-test argument. The conclusion is correct; the printed proof bounds $\sin t/t$ only on the original interval, which need not contain the scaled arguments $x/n^2$. The solution below uses the global inequality $|\sin t|\le |t|$.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the uniform $B/n^2$ bound on an arbitrary bounded interval and convergence of the majorant series.
---

::: {.problem}
Show that
$$
\sum_{n=1}^{\infty}\sin\frac{x}{n^2}
$$
converges uniformly on every bounded interval in $\RR$.
:::

::: {.solution}
Let $I\subset\mathbb R$ be a bounded interval and set
$$
B\coloneqq\sup_{x\in I}|x|<\infty.
$$

<1>1. For every $x\in I$ and every $n\geq1$,
$$
\left|\sin\frac{x}{n^2}\right|\leq\frac{B}{n^2}.
$$

::: {.proof}
The elementary inequality
$$
|\sin t|\leq|t|
$$
holds for every real $t$. Hence
$$
\left|\sin\frac{x}{n^2}\right|
\leq
\frac{|x|}{n^2}
\leq
\frac{B}{n^2}.
$$
:::

<1>2. The numerical series
$$
\sum_{n=1}^{\infty}\frac{B}{n^2}
$$
converges.

::: {.proof}
It is $B$ times the convergent $p$-series $\sum_{n\ge1}n^{-2}$.
:::

<1>3. The series
$$
\sum_{n=1}^{\infty}\sin\frac{x}{n^2}
$$
converges uniformly on $I$.

::: {.proof}
Step <1>1 supplies the uniform majorants $B/n^2$, and step <1>2 shows that their sum converges. The Weierstrass M-test therefore gives uniform convergence on $I$.
:::

<1>4. Q.E.D.

::: {.proof}
Since $I$ was an arbitrary bounded interval, step <1>3 proves the assertion.
:::
:::
