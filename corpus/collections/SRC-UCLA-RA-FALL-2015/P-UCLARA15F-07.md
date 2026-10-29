---
schema: qual/card@1
id: P-UCLARA15F-07
kind: problem
title: Disk functions with symmetric boundary values under $z\mapsto 1/z$ are constant
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 7 on page 2 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Assume that $f(z)$ is analytic in $\{z : |z| < 1\}$ and continuous on $\{z : |z| \leq 1\}$. If $f(z) = f(1/z)$ when $|z| = 1$, prove that $f(z)$ is constant.
:::

::: {.solution}

Define
$$
F:\CC\to\CC
$$
by
$$
\boxed{
F(z)
=
\begin{cases}
f(z),&|z|\le1,\\[4pt]
f(1/z),&|z|\ge1.
\end{cases}}
$$

::: pf

::: {.pf-step #s1-1}

The two formulas agree on the unit circle.


::: pf-proof

If $|z|=1$, the hypothesis gives
$$
f(z)=f(1/z).
$$
Thus the inside and outside definitions coincide.

:::

:::

::: pf-step

Therefore $F$ is well defined.


::: pf-proof

The only overlap of the two regions in the definition is $|z|=1$, and step [](#s1-1){.pf-ref} shows equality there.

:::

:::

::: pf-step

The function $F$ is continuous on $\CC$.


::: pf-proof

On $|z|\le1$, continuity follows from the assumed continuity of $f$ on the closed disk.

On $|z|\ge1$, the map
$$
z\mapsto \frac1z
$$
is continuous and maps this region into $|w|\le1$, so
$$
z\mapsto f(1/z)
$$
is continuous there.

The two continuous pieces agree on their common boundary by step [](#s1-1){.pf-ref}, so they paste to a continuous function on $\CC$.

:::

:::

::: {.pf-step #s1-4}

The function $F$ is analytic on
$$
\{z:|z|<1\}.
$$


::: pf-proof

There
$$
F=f,
$$
and $f$ is analytic by hypothesis.

:::

:::

::: {.pf-step #s1-5}

The function $F$ is analytic on
$$
\{z:|z|>1\}.
$$


::: pf-proof

There
$$
F(z)=f(1/z).
$$
The map $z\mapsto1/z$ is analytic on $\CC\setminus\{0\}$, and for $|z|>1$, one has $|1/z|<1$, where $f$ is analytic. Hence the composition is analytic.

:::

:::

::: {.pf-step #s1-6}

The continuous function $F$, analytic on both sides of the unit circle, is analytic across the unit circle.


::: pf-proof

Apply the analytic pasting lemma, equivalently Morera's theorem.

Indeed, let $\Delta$ be any triangle meeting the unit circle. Split $\Delta$ along the circle into finitely many regions lying inside and outside after approximating the circular arcs by smooth subdivision; on each side the integral of $F$ around the region boundary is zero by Cauchy's theorem. The integrals along the common interface cancel because $F$ is continuous and has the same boundary values from both sides. Hence
$$
\int_{\partial\Delta}F(z)\,dz=0.
$$
Morera's theorem then gives analyticity near every point of the circle.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{F\text{ is entire}.}
$$


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} cover all points of $\CC$.

:::

:::

::: {.pf-step #s1-8}

Since $f$ is continuous on the compact closed unit disk, there exists $M>0$ such that
$$
\boxed{|f(w)|\le M}
$$
for every $|w|\le1$.


::: pf-proof

A continuous function on a compact set is bounded.

:::

:::

::: {.pf-step #s1-9}

For every $|z|\le1$,
$$
|F(z)|\le M.
$$


::: pf-proof

On this region,
$$
F(z)=f(z),
$$
and apply step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

For every $|z|\ge1$,
$$
|F(z)|\le M.
$$


::: pf-proof

On this region,
$$
F(z)=f(1/z),
$$
and
$$
|1/z|\le1.
$$
Apply step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Hence
$$
\boxed{|F(z)|\le M}
$$
for every $z\in\CC$.


::: pf-proof

Combine steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

By Liouville's theorem,
$$
\boxed{F\text{ is constant}.}
$$


::: pf-proof

Step [](#s1-7){.pf-ref} says $F$ is entire, and step [](#s1-11){.pf-ref} says it is bounded.

:::

:::

::: {.pf-step #s1-13}

Therefore $f$ is constant on the unit disk.


::: pf-proof

For $|z|<1$,
$$
f(z)=F(z),
$$
and the right-hand side is constant by step [](#s1-12){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} is the required conclusion.

:::

:::

:::
