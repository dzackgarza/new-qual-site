---
schema: qual/card@1
id: P-DUKEBA14-3
kind: problem
title: Squaring preserves Riemann integrability
classification:
  areas: [real-analysis]
  topics: [Riemann Integration]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part I, Problem 3 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $f$ be a bounded Riemann integrable function on $[0,1]$. Prove that $f^2$ is Riemann integrable on $[0,1]$.
:::

::: solution
<1>1. Control the oscillation of $f^2$ by that of $f$.
::: proof
Choose $M\ge1$ with $|f(x)|\le M$ on $[0,1]$. For all $x,y$,
\[
|f(x)^2-f(y)^2|
=|f(x)-f(y)|\,|f(x)+f(y)|
\le2M|f(x)-f(y)|.
\]
Hence on every subinterval $I$,
\[
\operatorname{osc}_I(f^2)
\le2M\operatorname{osc}_I(f).
\]
:::

<1>2. Apply the Darboux criterion.
::: proof
Given $\varepsilon>0$, Riemann integrability of $f$ gives a partition $P$ such that
\[
U(f,P)-L(f,P)
=\sum_{I\in P}\operatorname{osc}_I(f)|I|
<\frac{\varepsilon}{2M}.
\]
Therefore
\[
U(f^2,P)-L(f^2,P)
\le2M\sum_{I\in P}\operatorname{osc}_I(f)|I|
<\varepsilon.
\]
By the Darboux criterion, $f^2$ is Riemann integrable.
:::
:::
