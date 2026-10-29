---
schema: qual/card@1
id: P-WESCA11-4
kind: problem
title: 'Radius of convergence of the coefficientwise product'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
If $A$ and $B$ are the radii of convergence of
\[
\sum_{n=0}^\infty a_nz^n
\quad\text{and}\quad
\sum_{n=0}^\infty b_nz^n,
\]
prove that the radius of convergence of
\[
\sum_{n=0}^\infty a_nb_nz^n
\]
is at least $AB$.
:::

::: {.solution}

Let \(R\) denote the radius of convergence of
\[
\sum_{n=0}^{\infty}a_nb_nz^n.
\]

::: pf

::: pf-step

If
\[
AB=0,
\]
then
\[
\boxed{R\ge AB}.
\]


::: pf-proof

Every radius of convergence is nonnegative, so
\[
R\ge0=AB.
\]

:::

:::

::: pf-step

Assume now
\[
AB>0,
\]
and fix \(z\in\CC\) with
\[
\boxed{|z|<AB}.
\]


::: pf-proof

To prove \(R\ge AB\), it suffices to show convergence for every such \(z\).

:::

:::

::: {.pf-step #s1-3}

There exist positive numbers
\[
r<A,
\qquad
s<B
\]
such that
\[
\boxed{|z|<rs}.
\]


::: pf-proof

Since
\[
|z|<AB,
\]
choose \(r<A\) sufficiently close to \(A\) and \(s<B\) sufficiently close to
\(B\) so that their product still exceeds \(|z|\). If one radius is infinite,
choose the corresponding finite \(r\) or \(s\) large enough.

:::

:::

::: pf-step

The series
\[
\sum_{n=0}^{\infty}|a_n|r^n
\]
converges.


::: pf-proof

A power series converges absolutely at every point strictly inside its radius
of convergence. Since \(r<A\), apply this to the first power series.

:::

:::

::: {.pf-step #s1-5}

Therefore the sequence
\[
\boxed{
\{|a_n|r^n\}_{n\ge0}}
\]
is bounded.


::: pf-proof

Every convergent series has terms tending to \(0\), hence in particular its
terms form a bounded sequence.

:::

:::

::: {.pf-step #s1-6}

Likewise,
\[
\boxed{
\{|b_n|s^n\}_{n\ge0}}
\]
is bounded.


::: pf-proof

Since \(s<B\), the second power series converges absolutely at \(s\), and the
same argument as in step [](#s1-5){.pf-ref} applies.

:::

:::

::: {.pf-step #s1-7}

Choose constants
\[
M,N>0
\]
such that
\[
|a_n|r^n\le M
\]
and
\[
|b_n|s^n\le N
\]
for all \(n\).


::: pf-proof

Use the boundedness from steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Set
\[
\boxed{
q=\frac{|z|}{rs}}.
\]
Then
\[
0\le q<1.
\]


::: pf-proof

This is step [](#s1-3){.pf-ref} divided by the positive number \(rs\).

:::

:::

::: {.pf-step #s1-9}

For every \(n\),
\[
|a_nb_nz^n|
=
(|a_n|r^n)(|b_n|s^n)q^n.
\]


::: pf-proof

Since
\[
|z|^n
=
(rs)^nq^n,
\]
one has
\[
|a_nb_n||z|^n
=
(|a_n|r^n)(|b_n|s^n)q^n.
\]

:::

:::

::: {.pf-step #s1-10}

Hence
\[
\boxed{
|a_nb_nz^n|
\le
MNq^n}.
\]


::: pf-proof

Apply the bounds from step [](#s1-7){.pf-ref} to step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

The geometric series
\[
\sum_{n=0}^{\infty}MNq^n
\]
converges.


::: pf-proof

Step [](#s1-8){.pf-ref} gives
\[
0\le q<1.
\]

:::

:::

::: {.pf-step #s1-12}

Therefore
\[
\sum_{n=0}^{\infty}a_nb_nz^n
\]
converges absolutely.


::: pf-proof

Apply the comparison test using steps [](#s1-10){.pf-ref} through [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Since every \(z\) with
\[
|z|<AB
\]
lies in the disk of convergence of the coefficientwise product series,
\[
\boxed{R\ge AB}.
\]


::: pf-proof

Step [](#s1-12){.pf-ref} holds for an arbitrary \(z\) satisfying \(|z|<AB\). Therefore the
radius \(R\) is at least \(AB\).

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} is the required estimate.

:::

:::

:::
