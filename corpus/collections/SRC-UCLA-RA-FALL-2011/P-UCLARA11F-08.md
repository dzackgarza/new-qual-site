---
schema: qual/card@1
id: P-UCLARA11F-08
kind: problem
title: Counting zeros in a right half-plane
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Determine the number of solutions of
\[
z-2-e^{-z}=0
\]
in the right half-plane $H=\{z\in\mathbb C:\operatorname{Re}z>0\}$.
:::

::: {.solution}
Define
\[
F(z)=z-2-e^{-z}
\]
and
\[
G(z)=z-2.
\]

For \(R>3\), let
\[
D_R
=
\{z\in\mathbb C:\operatorname{Re}z>0,\ |z|<R\},
\]
whose boundary consists of the vertical segment
\[
\{-iR\le z\le iR:\operatorname{Re}z=0\}
\]
and the right semicircle
\[
\{Re^{i\theta}:-\pi/2\le\theta\le\pi/2\}.
\]

<1>1. On the imaginary-axis part of \(\partial D_R\),
\[
\boxed{|e^{-z}|=1}.
\]

::: {.proof}
If
\[
z=iy,
\]
then
\[
|e^{-z}|
=
|e^{-iy}|
=
1.
\]
:::

<1>2. On the same boundary segment,
\[
\boxed{|z-2|\ge2}.
\]

::: {.proof}
If \(z=iy\), then
\[
|z-2|
=
|-2+iy|
=
\sqrt{4+y^2}
\ge2.
\]
:::

<1>3. Hence on the imaginary-axis part,
\[
\boxed{|e^{-z}|<|z-2|}.
\]

::: {.proof}
Combine steps <1>1--<1>2.
:::

<1>4. On the right semicircle,
\[
\boxed{|e^{-z}|\le1}.
\]

::: {.proof}
There
\[
\operatorname{Re}z\ge0,
\]
so
\[
|e^{-z}|
=
e^{-\operatorname{Re}z}
\le1.
\]
:::

<1>5. On the right semicircle,
\[
\boxed{|z-2|\ge R-2}.
\]

::: {.proof}
By the reverse triangle inequality,
\[
|z-2|
\ge
\bigl||z|-2\bigr|
=
R-2.
\]
:::

<1>6. Since \(R>3\),
\[
R-2>1.
\]

::: {.proof}
Subtract \(2\) from \(R>3\).
:::

<1>7. Therefore on the right semicircle,
\[
\boxed{|e^{-z}|<|z-2|}.
\]

::: {.proof}
Use steps <1>4--<1>6.
:::

<1>8. Thus on all of \(\partial D_R\),
\[
\boxed{|e^{-z}|<|G(z)|}.
\]

::: {.proof}
The boundary is the union of the two pieces handled in steps <1>3 and <1>7.
:::

<1>9. By Rouché's theorem, \(F\) and \(G\) have the same number of zeros in \(D_R\), counted with multiplicity.

::: {.proof}
Since
\[
F=G-e^{-z},
\]
the perturbation \(e^{-z}\) has modulus strictly smaller than \(|G|\) on the boundary by step <1>8.
:::

<1>10. The function
\[
G(z)=z-2
\]
has exactly one zero in \(D_R\), namely
\[
\boxed{z=2}.
\]

::: {.proof}
The only zero of \(G\) is \(2\), and for \(R>3\),
\[
\operatorname{Re}2>0,
\qquad
|2|<R.
\]
It is a simple zero.
:::

<1>11. Therefore \(F\) has exactly one zero in \(D_R\).

::: {.proof}
Apply step <1>9 using step <1>10.
:::

<1>12. Every zero of \(F\) in the open right half-plane belongs to \(D_R\) for all sufficiently large \(R\).

::: {.proof}
If \(z_0\in H\), then choose
\[
R>\max\{3,|z_0|\}.
\]
Then \(z_0\in D_R\).
:::

<1>13. Hence \(F\) has at most one zero in
\[
H=\{z:\operatorname{Re}z>0\}.
\]

::: {.proof}
If there were two distinct zeros in \(H\), choose \(R>3\) large enough to contain both. This would contradict step <1>11.
:::

<1>14. Since step <1>11 gives one zero in every \(D_R\) with \(R>3\), \(F\) has at least one zero in \(H\).

::: {.proof}
Each \(D_R\) is contained in \(H\), and \(F\) has one zero there.
:::

<1>15. Therefore
\[
\boxed{
z-2-e^{-z}=0
\text{ has exactly one solution in }H},
\]
counted with multiplicity.

::: {.proof}
Combine steps <1>13--<1>14.
:::

<1>16. Q.E.D.

::: {.proof}
Step <1>15 is the required zero count.
:::
:::
