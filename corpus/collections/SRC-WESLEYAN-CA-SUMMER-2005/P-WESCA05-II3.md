---
schema: qual/card@1
id: P-WESCA05-II3
kind: problem
title: "Maximum modulus of $e^{z^2}$ on a square"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 2, problem 3 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let $f(z)=e^{z^2}$ and
\[
S=\{x+iy:0\le x\le2,\ 0\le y\le2\}.
\]

1. Compute the maximum value of $|f(z)|$ on $S$.

2. Find the set of points in $S$ where this maximum is attained.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If \(z=x+iy\), then
\[
|e^{z^2}|=e^{x^2-y^2}.
\]


::: pf-proof

One has
\[
z^2=(x+iy)^2=x^2-y^2+2ixy.
\]
For every \(w\in\CC\),
\[
|e^w|=e^{\operatorname{Re}w}.
\]
Therefore
\[
|e^{z^2}|=e^{\operatorname{Re}(z^2)}
=e^{x^2-y^2}.
\]

:::

:::

::: {.pf-step #s1-2}

On the square \(S\),
\[
x^2-y^2\le4.
\]


::: pf-proof

For \(0\le x\le2\),
\[
x^2\le4,
\]
and for \(0\le y\le2\),
\[
-y^2\le0.
\]
Adding gives
\[
x^2-y^2\le4.
\]

:::

:::

::: {.pf-step #s1-3}

Equality
\[
x^2-y^2=4
\]
holds in \(S\) exactly at
\[
z=2.
\]


::: pf-proof

Equality in step [](#s1-2){.pf-ref} requires both
\[
x^2=4
\qquad\text{and}\qquad
y^2=0.
\]
Because \(0\le x,y\le2\), this forces
\[
x=2,\qquad y=0.
\]
Conversely, at \((x,y)=(2,0)\) one has \(x^2-y^2=4\).

:::

:::

::: {.pf-step #s1-4}

The maximum modulus is
\[
\boxed{\max_{z\in S}|f(z)|=e^4,}
\]
and it is attained exactly at
\[
\boxed{z=2.}
\]


::: pf-proof

The real exponential function is strictly increasing. By steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref},
\[
|f(z)|=e^{x^2-y^2}\le e^4,
\]
with equality exactly when \(z=2\).

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives both the requested maximum value and the complete set of maximizers.

:::

:::

:::
