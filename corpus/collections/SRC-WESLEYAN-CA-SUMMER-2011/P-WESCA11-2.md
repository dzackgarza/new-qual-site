---
schema: qual/card@1
id: P-WESCA11-2
kind: problem
title: 'Partial fractions for $z^4/(z^3-1)$'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Represent
\[
\frac{z^4}{z^3-1}
\]
by partial fractions.
:::

::: {.solution}
Let
\[
\omega=e^{2\pi i/3},
\]
so
\[
1+\omega+\omega^2=0,
\qquad
\omega^3=1.
\]

<1>1. Polynomial division gives
\[
\boxed{
\frac{z^4}{z^3-1}
=
z+\frac{z}{z^3-1}}.
\]

::: {.proof}
Since
\[
z(z^3-1)=z^4-z,
\]
the remainder after division by \(z^3-1\) is \(z\).
:::

<1>2. Factor
\[
\boxed{
z^3-1
=
(z-1)(z-\omega)(z-\omega^2)}.
\]

::: {.proof}
The three cube roots of \(1\) are
\[
1,\omega,\omega^2.
\]
:::

<1>3. Write
\[
\frac{z}{z^3-1}
=
\frac{A}{z-1}
+
\frac{B}{z-\omega}
+
\frac{C}{z-\omega^2}.
\]

::: {.proof}
All three roots of \(z^3-1\) are simple, so the proper rational function has
a partial-fraction expansion with one simple term at each root.
:::

<1>4. For a simple root \(r\) of \(z^3-1\), the coefficient of
\[
\frac1{z-r}
\]
in
\[
\frac{z}{z^3-1}
\]
is
\[
\boxed{\frac1{3r}}.
\]

::: {.proof}
The coefficient is
\[
\lim_{z\to r}
(z-r)\frac{z}{z^3-1}.
\]
Since
\[
z^3-1
=
(z-r)\cdot\frac{z^3-r^3}{z-r}
\]
and
\[
\lim_{z\to r}
\frac{z^3-r^3}{z-r}
=
3r^2,
\]
the limit is
\[
\frac{r}{3r^2}
=
\frac1{3r}.
\]
:::

<1>5. At \(r=1\),
\[
\boxed{A=\frac13}.
\]

::: {.proof}
Apply step <1>4.
:::

<1>6. At \(r=\omega\),
\[
\boxed{
B=\frac1{3\omega}
=
\frac{\omega^2}{3}}.
\]

::: {.proof}
Since
\[
\omega^3=1,
\]
one has
\[
\omega^{-1}=\omega^2.
\]
:::

<1>7. At \(r=\omega^2\),
\[
\boxed{
C=\frac1{3\omega^2}
=
\frac{\omega}{3}}.
\]

::: {.proof}
Again use
\[
\omega^{-2}=\omega.
\]
:::

<1>8. Therefore
\[
\boxed{
\frac{z^4}{z^3-1}
=
z
+
\frac1{3(z-1)}
+
\frac{\omega^2}{3(z-\omega)}
+
\frac{\omega}{3(z-\omega^2)}}.
\]

::: {.proof}
Combine steps <1>1 and <1>3--<1>7.
:::

<1>9. Over the real quadratic factorization
\[
z^3-1
=
(z-1)(z^2+z+1),
\]
one may instead write
\[
\frac{z}{z^3-1}
=
\frac{A}{z-1}
+
\frac{Bz+C}{z^2+z+1}.
\]

::: {.proof}
This is the standard partial-fraction form over the real coefficients.
:::

<1>10. Clearing denominators gives
\[
z
=
A(z^2+z+1)
+
(Bz+C)(z-1).
\]

::: {.proof}
Multiply the identity in step <1>9 by
\[
(z-1)(z^2+z+1).
\]
:::

<1>11. Comparing coefficients yields
\[
\boxed{
A=\frac13,
\qquad
B=-\frac13,
\qquad
C=\frac13}.
\]

::: {.proof}
Expanding step <1>10 gives
\[
z
=
(A+B)z^2
+
(A-B+C)z
+
(A-C).
\]
Thus
\[
A+B=0,
\qquad
A-B+C=1,
\qquad
A-C=0.
\]
Solving gives the displayed values.
:::

<1>12. Hence an equivalent real-coefficient form is
\[
\boxed{
\frac{z^4}{z^3-1}
=
z
+
\frac1{3(z-1)}
+
\frac{1-z}{3(z^2+z+1)}}.
\]

::: {.proof}
Insert step <1>11 into step <1>9 and combine with step <1>1.
:::

<1>13. Q.E.D.

::: {.proof}
Step <1>8 gives the complete complex partial-fraction decomposition, and
step <1>12 gives the equivalent real-coefficient form.
:::
:::
