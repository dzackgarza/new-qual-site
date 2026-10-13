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

<1>1. If
\[
AB=0,
\]
then
\[
\boxed{R\ge AB}.
\]

::: {.proof}
Every radius of convergence is nonnegative, so
\[
R\ge0=AB.
\]
:::

<1>2. Assume now
\[
AB>0,
\]
and fix \(z\in\mathbb C\) with
\[
\boxed{|z|<AB}.
\]

::: {.proof}
To prove \(R\ge AB\), it suffices to show convergence for every such \(z\).
:::

<1>3. There exist positive numbers
\[
r<A,
\qquad
s<B
\]
such that
\[
\boxed{|z|<rs}.
\]

::: {.proof}
Since
\[
|z|<AB,
\]
choose \(r<A\) sufficiently close to \(A\) and \(s<B\) sufficiently close to
\(B\) so that their product still exceeds \(|z|\). If one radius is infinite,
choose the corresponding finite \(r\) or \(s\) large enough.
:::

<1>4. The series
\[
\sum_{n=0}^{\infty}|a_n|r^n
\]
converges.

::: {.proof}
A power series converges absolutely at every point strictly inside its radius
of convergence. Since \(r<A\), apply this to the first power series.
:::

<1>5. Therefore the sequence
\[
\boxed{
\{|a_n|r^n\}_{n\ge0}}
\]
is bounded.

::: {.proof}
Every convergent series has terms tending to \(0\), hence in particular its
terms form a bounded sequence.
:::

<1>6. Likewise,
\[
\boxed{
\{|b_n|s^n\}_{n\ge0}}
\]
is bounded.

::: {.proof}
Since \(s<B\), the second power series converges absolutely at \(s\), and the
same argument as in step <1>5 applies.
:::

<1>7. Choose constants
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

::: {.proof}
Use the boundedness from steps <1>5--<1>6.
:::

<1>8. Set
\[
\boxed{
q=\frac{|z|}{rs}}.
\]
Then
\[
0\le q<1.
\]

::: {.proof}
This is step <1>3 divided by the positive number \(rs\).
:::

<1>9. For every \(n\),
\[
|a_nb_nz^n|
=
(|a_n|r^n)(|b_n|s^n)q^n.
\]

::: {.proof}
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

<1>10. Hence
\[
\boxed{
|a_nb_nz^n|
\le
MNq^n}.
\]

::: {.proof}
Apply the bounds from step <1>7 to step <1>9.
:::

<1>11. The geometric series
\[
\sum_{n=0}^{\infty}MNq^n
\]
converges.

::: {.proof}
Step <1>8 gives
\[
0\le q<1.
\]
:::

<1>12. Therefore
\[
\sum_{n=0}^{\infty}a_nb_nz^n
\]
converges absolutely.

::: {.proof}
Apply the comparison test using steps <1>10--<1>11.
:::

<1>13. Since every \(z\) with
\[
|z|<AB
\]
lies in the disk of convergence of the coefficientwise product series,
\[
\boxed{R\ge AB}.
\]

::: {.proof}
Step <1>12 holds for an arbitrary \(z\) satisfying \(|z|<AB\). Therefore the
radius \(R\) is at least \(AB\).
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>13 is the required estimate.
:::
:::
