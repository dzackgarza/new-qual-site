---
schema: qual/card@1
id: P-DUKEBA14-7
kind: problem
title: Weighted mean value theorem for a Riemann integral
classification:
  areas: [real-analysis]
  topics: [Riemann Integration, Intermediate Value Theorem]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part II, Problem 1 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $g$ be a positive Riemann integrable function on $[1,2]$. Prove that there exists $c\in[1,2]$ such that
\[
\int_1^2 e^{t^2}g(t)\,dt
=e^{c^2}\int_1^2 g(t)\,dt.
\]
:::

::: solution
<1>1. Bound the weighted average.
::: proof
On $[1,2]$,
\[
e\le e^{t^2}\le e^4.
\]
Multiplying by $g(t)\ge0$ and integrating gives
\[
e\int_1^2g(t)\,dt
\le
\int_1^2e^{t^2}g(t)\,dt
\le
e^4\int_1^2g(t)\,dt.
\]
Since $g$ is positive, $\int_1^2g>0$. Hence
\[
e\le
\frac{\int_1^2e^{t^2}g(t)\,dt}{\int_1^2g(t)\,dt}
\le e^4.
\]
:::

<1>2. Apply the intermediate value theorem.
::: proof
The continuous function $h(t)=e^{t^2}$ maps $[1,2]$ onto $[e,e^4]$. Therefore there exists $c\in[1,2]$ such that
\[
e^{c^2}
=
\frac{\int_1^2e^{t^2}g(t)\,dt}{\int_1^2g(t)\,dt}.
\]
Multiplying by $\int_1^2g$ gives the desired identity.
:::
:::
