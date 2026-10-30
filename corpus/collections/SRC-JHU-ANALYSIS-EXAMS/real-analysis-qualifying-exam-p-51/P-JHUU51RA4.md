---
schema: qual/card@1
id: P-JHUU51RA4
kind: problem
title: "A function whose every set-integral is bounded by measure is at most 1 a.e."
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 4 of the JHU Real Analysis Qualifying Exam on p. 51 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose $f\in L^1(\RR^n,m)$ satisfies
$$
\abs{\int_E f\,dm}\le m(E)
$$
for every Lebesgue-measurable set $E$. Prove that
$$
\abs{f}\le1
$$
almost everywhere.
:::

::: {.solution}
Define the finite signed or complex measure
$$
\nu(E)=\int_E f\,dm.
$$
The hypothesis says
$$
\abs{\nu(E)}\le m(E)
$$
for every measurable set $E$.

Let $A$ be measurable and let
$$
A=\bigsqcup_{j=1}^N A_j
$$
be any finite measurable partition. Then
$$
\sum_{j=1}^N\abs{\nu(A_j)}
\le\sum_{j=1}^N m(A_j)
=m(A).
$$
Taking the supremum over all finite measurable partitions of $A$ gives
$$
\totalvariation{\nu}(A)\le m(A),
$$
where $\totalvariation{\nu}$ is the total variation measure of $\nu$.

Since $\nu$ has density $f$ with respect to Lebesgue measure, its total variation has density $\abs{f}$:
$$
\totalvariation{\nu}(A)=\int_A\abs{f}\,dm.
$$
Therefore
$$
\int_A\abs{f}\,dm\le m(A)
$$
for every measurable $A$.

Fix $\varepsilon>0$ and let
$$
A_\varepsilon=\{x:\abs{f(x)}>1+\varepsilon\}.
$$
Then
$$
(1+\varepsilon)m(A_\varepsilon)
<\int_{A_\varepsilon}\abs{f}\,dm
\le m(A_\varepsilon).
$$
Hence
$$
m(A_\varepsilon)=0.
$$
Taking the union over positive rational $\varepsilon$ gives
$$
m\{x:\abs{f(x)}>1\}=0.
$$
Thus $\abs{f}\le1$ almost everywhere.
:::
