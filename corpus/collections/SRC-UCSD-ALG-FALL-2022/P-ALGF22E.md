---
schema: qual/card@1
id: P-ALGF22E
kind: problem
title: "Flat quotient ring implies I ∩ J = IJ for all ideals J"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 5 of the official UCSD Algebra Qualifying Exam, Fall 2022 source; the flatness hypothesis and conclusion for every ideal J agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the tensor-injectivity argument and identified its kernel as (I intersection J)/IJ.
---

::: {.problem}
Let $I$ be an ideal of a commutative ring $R$.
Suppose that $R/I$ is a flat $R$-module.
Show that $I \cap J = IJ$ for all ideals $J$ of $R$.
:::

::: {.solution}
Fix an ideal $J\trianglelefteq R$.

::: pf

::: {.pf-step #s1}

Tensoring the inclusion $J\hookrightarrow R$ with the flat module $R/I$ gives an injection
\[
J\otimes_R R/I
\longrightarrow
R\otimes_R R/I.
\]

::: pf-proof

The sequence
\[
0\longrightarrow J\longrightarrow R
\]
is exact.
Since $R/I$ is flat, the functor
\[
-\otimes_R R/I
\]
preserves this injection.

:::

:::

::: pf-step

Under the canonical identifications
\[
J\otimes_R R/I\cong J/IJ
\]
and
\[
R\otimes_R R/I\cong R/I,
\]
the map in step [](#s1){.pf-ref} is
\[
\psi:J/IJ\longrightarrow R/I,
\qquad
x+IJ\longmapsto x+I.
\]

::: pf-proof

For any $R$-module $M$, the map
\[
M\otimes_R R/I\longrightarrow M/IM,
\qquad
m\otimes(r+I)\longmapsto rm+IM
\]
is the standard natural isomorphism.
Applying it to $M=J$ and $M=R$ identifies the tensor of the inclusion $J\hookrightarrow R$ with the displayed quotient map.

:::

:::

::: {.pf-step #s3}

The kernel of $\psi$ is
\[
\ker\psi=(I\cap J)/IJ.
\]

::: pf-proof

An element $x+IJ\in J/IJ$ lies in the kernel exactly when
\[
x\in I.
\]
Since already $x\in J$, this is equivalent to
\[
x\in I\cap J.
\]
Also
\[
IJ\subseteq I\cap J,
\]
so the kernel is precisely the indicated quotient.

:::

:::

::: pf-step

One has
\[
I\cap J=IJ.
\]

::: pf-proof

By step [](#s1){.pf-ref}, the map $\psi$ is injective.
Hence step [](#s3){.pf-ref} gives
\[
(I\cap J)/IJ=0.
\]
Therefore $I\cap J=IJ$.
Since $J$ was arbitrary, the equality holds for every ideal $J$ of $R$.

:::

:::

:::

:::
