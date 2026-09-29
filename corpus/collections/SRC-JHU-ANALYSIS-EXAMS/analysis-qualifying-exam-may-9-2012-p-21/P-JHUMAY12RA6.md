---
schema: qual/card@1
id: P-JHUMAY12RA6
kind: problem
title: 'Absolutely convergent series of $L^1$ functions converges a.e. and in $L^1$'
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the JHU Analysis Qualifying Exam, May 9, 2012, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(g_k)\subset L^1(\RR^n)$ and suppose
$$
\sum_{k=1}^\infty\norm{g_k}_1<\infty.
$$

(a) Show that $\sum_{k=1}^\infty g_k$ converges almost everywhere to some $g\in L^1$.

(b) Show that the partial sums converge to $g$ in $L^1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function $\sum_{k=1}^\infty\abs{g_k}$ is integrable and finite almost everywhere.

::: pf-proof

By [[FT-4JRQX|Tonelli's theorem]],
$$
\int_{\RR^n}\sum_{k=1}^\infty\abs{g_k(x)}\,dx
=\sum_{k=1}^\infty\norm{g_k}_1<\infty.
$$
Hence $\sum_{k=1}^\infty\abs{g_k(x)}<\infty$ for almost every $x$.

:::

:::

::: {.pf-step #s2}

The series $\sum_{k=1}^\infty g_k$ converges almost everywhere to some $g\in L^1(\RR^n)$.

::: pf-proof

By step [](#s1){.pf-ref}, the series converges absolutely for almost every $x$. Define $g(x)$ to be its sum there and set $g(x)=0$ on the null exceptional set. Then
$$
\abs{g(x)}\le\sum_{k=1}^\infty\abs{g_k(x)}
$$
almost everywhere, so step [](#s1){.pf-ref} gives $g\in L^1(\RR^n)$.

:::

:::

::: {.pf-step #s3}

If $S_N=\sum_{k=1}^N g_k$, then
$$
\norm{g-S_N}_1\longrightarrow0.
$$

::: pf-proof

Almost everywhere,
$$
\abs{g-S_N}\le\sum_{k>N}\abs{g_k}.
$$
Therefore
$$
\norm{g-S_N}_1
\le\sum_{k>N}\norm{g_k}_1\longrightarrow0,
$$
because the series of norms converges.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part (a), and step [](#s3){.pf-ref} proves part (b).

:::

:::

:::
