---
schema: qual/card@1
id: P-WESRA04-E3
kind: problem
title: Functions separating $L^2(\RR)$ and $L^3(\RR)$
classification:
  areas: [real-analysis]
  topics: [Function Spaces]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.2, item 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Give examples of

1. a real-valued function in $L^2(\RR)$ but not in $L^3(\RR)$;

2. a real-valued function in $L^3(\RR)$ but not in $L^2(\RR)$.
:::

::: {.solution}
For the first example, take
$$
f(x)=x^{-2/5}\mathbf1_{(0,1)}(x).
$$
Then
$$
\int_0^1|f(x)|^2\,dx
=\int_0^1x^{-4/5}\,dx<\infty,
$$
while
$$
\int_0^1|f(x)|^3\,dx
=\int_0^1x^{-6/5}\,dx=\infty.
$$
Hence
$$
f\in L^2(\RR)\setminus L^3(\RR).
$$

For the second example, take
$$
g(x)=x^{-2/5}\mathbf1_{[1,\infty)}(x).
$$
Then
$$
\int_1^\infty|g(x)|^3\,dx
=\int_1^\infty x^{-6/5}\,dx<\infty,
$$
whereas
$$
\int_1^\infty|g(x)|^2\,dx
=\int_1^\infty x^{-4/5}\,dx=\infty.
$$
Thus
$$
\boxed{g\in L^3(\RR)\setminus L^2(\RR).}
$$
:::
