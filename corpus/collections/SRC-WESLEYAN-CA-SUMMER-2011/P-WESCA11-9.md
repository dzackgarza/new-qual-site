---
schema: qual/card@1
id: P-WESCA11-9
kind: problem
title: 'Prove Schwarz’s lemma using the maximum principle'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $f$ be holomorphic on the unit disk, with $f(0)=0$ and $|f(z)|\le1$ for $|z|<1$.
Prove, using the maximum principle, that
\[
|f(z)|\le|z|
\]
for $|z|<1$.
:::

::: {.solution}

::: pf

::: pf-step

Define
\[
g(z)
\coloneqq
\begin{cases}
\dfrac{f(z)}{z},&z\ne0,\\[2mm]
f'(0),&z=0.
\end{cases}
\]
Then $g$ is holomorphic on the unit disk.


::: pf-proof

Since
\[
f(0)=0,
\]
the Taylor expansion of $f$ at $0$ has the form
\[
f(z)
=
a_1z+a_2z^2+\cdots.
\]
Therefore, for $z\ne0$,
\[
\frac{f(z)}z
=
a_1+a_2z+\cdots,
\]
which extends holomorphically across $0$ with value
\[
a_1=f'(0).
\]

:::

:::

::: {.pf-step #s1-2}

Fix
\[
0<r<1.
\]
On the circle
\[
|z|=r,
\]
one has
\[
|g(z)|
\le
\frac1r.
\]


::: pf-proof

For
\[
|z|=r,
\]
the hypothesis gives
\[
|f(z)|\le1.
\]
Hence
\[
|g(z)|
=
\frac{|f(z)|}{|z|}
\le
\frac1r.
\]

:::

:::

::: {.pf-step #s1-3}

For every
\[
|z|\le r,
\]
one has
\[
|g(z)|
\le
\frac1r.
\]


::: pf-proof

The function $g$ is holomorphic on a neighborhood of the closed disk
\[
\{|z|\le r\}.
\]
By the maximum modulus principle,
\[
\max_{|z|\le r}|g(z)|
=
\max_{|z|=r}|g(z)|.
\]
Apply the boundary estimate from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Fix
\[
z\in\DD.
\]
Then
\[
|g(z)|\le1.
\]


::: pf-proof

Choose any
\[
r
\]
with
\[
|z|<r<1.
\]
Step [](#s1-3){.pf-ref} gives
\[
|g(z)|
\le
\frac1r.
\]
This holds for every such $r$. Letting
\[
r\uparrow1
\]
gives
\[
|g(z)|\le1.
\]

:::

:::

::: {.pf-step #s1-5}

Therefore
\[
\boxed{
|f(z)|\le|z|
\qquad
(|z|<1).
}
\]


::: pf-proof

For
\[
z\ne0,
\]
one has
\[
f(z)=zg(z).
\]
By step [](#s1-4){.pf-ref},
\[
|f(z)|
=
|z|\,|g(z)|
\le
|z|.
\]
At
\[
z=0,
\]
the inequality is
\[
0\le0
\]
because
\[
f(0)=0.
\]

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is Schwarz's estimate obtained from the maximum principle.

:::

:::

:::
