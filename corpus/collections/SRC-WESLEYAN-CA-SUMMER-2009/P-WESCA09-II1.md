---
schema: qual/card@1
id: P-WESCA09-II1
kind: problem
title: 'Entire functions with one-sided exponential growth'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Section II, problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $f$ be entire and suppose
\[
|f(z)|\le m e^{\alpha x},\qquad z=x+iy,
\]
where $m,\alpha>0$.
Show that
\[
f(z)=Ae^{\alpha z}
\]
for some $A\in\CC$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function
\[
g(z)=f(z)e^{-\alpha z}
\]
is entire and bounded by $m$ on $\CC$.


::: pf-proof

Both $f$ and $z\mapsto e^{-\alpha z}$ are entire, so $g$ is entire. If
$z=x+iy$, then
\[
|e^{-\alpha z}|=e^{-\alpha x}.
\]
Therefore the assumed estimate gives
\[
|g(z)|
=|f(z)|e^{-\alpha x}
\le m e^{\alpha x}e^{-\alpha x}
=m.
\]

:::

:::

::: {.pf-step #s1-2}

There is a constant $A\in\CC$ such that
\[
\boxed{f(z)=Ae^{\alpha z}\qquad(z\in\CC)}.
\]


::: pf-proof

By step [](#s1-1){.pf-ref}, $g$ is a bounded entire function. Liouville's theorem therefore
implies that $g$ is constant, say $g(z)=A$. Thus
\[
f(z)e^{-\alpha z}=A,
\]
and multiplication by $e^{\alpha z}$ gives the stated formula.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} is the required conclusion.

:::

:::

:::
