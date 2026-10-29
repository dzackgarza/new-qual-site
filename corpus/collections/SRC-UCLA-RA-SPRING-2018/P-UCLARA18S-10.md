---
schema: qual/card@1
id: P-UCLARA18S-10
kind: problem
title: Injective holomorphic self-maps of the thrice-punctured sphere
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 10. Let $\CC^*=\CC\cup\{\infty\}$ be the Riemann sphere and let
\[
\Omega=\CC^*\setminus\{0,1\}.
\]
Let $f:\Omega\to\Omega$ be a holomorphic function.

(a) Prove that if $f$ is injective then $f(\Omega)=\Omega$.

(b) Make a list of all such injective functions $f$.
:::

::: {.solution}

Let
\[
\widetilde\Omega
=
\widehat{\CC}\setminus\{0,\infty\}
=
\CC^\times
\]
and define the Möbius transformation
\[
T(z)=\frac{z}{z+1}.
\]
Then
\[
T(0)=0,
\qquad
T(\infty)=1,
\]
so
\[
T:\widetilde\Omega\xrightarrow{\sim}\Omega.
\]

::: pf

::: {.pf-step #s1-1}

If
\[
f:\Omega\to\Omega
\]
is injective and holomorphic, then
\[
g
=
T^{-1}\circ f\circ T
:
\CC^\times\to\CC^\times
\]
is injective and holomorphic.


::: pf-proof

The maps \(T\) and \(T^{-1}\) are Möbius transformations and hence
biholomorphic on the indicated domains. Composition preserves holomorphy and
injectivity.

:::

:::

::: {.pf-step #s1-2}

Neither \(0\) nor \(\infty\) can be an essential singularity of \(g\).


::: pf-proof

Suppose \(0\) were an essential singularity. By the Great Picard theorem,
in every punctured neighborhood of \(0\), the function \(g\) assumes every
complex value with at most one exception infinitely often. Since
\[
g(\CC^\times)\subseteq\CC^\times,
\]
the value \(0\) is already omitted. Hence every nonzero value is assumed
infinitely often near \(0\), contradicting injectivity.

The same argument at \(\infty\), applied after the change of variable
\[
z\longmapsto\frac1z,
\]
rules out an essential singularity there.

:::

:::

::: {.pf-step #s1-3}

Any pole of \(g\) at \(0\) or \(\infty\) has order at most \(1\).


::: pf-proof

Suppose \(g\) had a pole of order \(m\ge2\) at \(0\). Then
\[
h=\frac1g
\]
extends holomorphically across \(0\) with a zero of order \(m\ge2\).
Thus
\[
h'(0)=0.
\]
The local mapping theorem for holomorphic functions says that near a zero of
multiplicity \(m\), the map is locally \(m\)-to-one onto nearby nonzero
values. Hence there are distinct nonzero points arbitrarily near \(0\) with
the same value of \(h\), and therefore the same value of \(g\), contradicting
injectivity.

The argument at \(\infty\) is identical after replacing \(z\) by \(1/z\).

:::

:::

::: {.pf-step #s1-4}

Hence \(g\), viewed as a meromorphic function on the Riemann sphere,
has the form
\[
\boxed{
g(z)
=
\frac{a}{z}+b+cz}
\]
for some \(a,b,c\in\CC\).


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, the only possible poles are at \(0\) and \(\infty\),
each of order at most one. Subtract the possible principal part
\[
\frac az
\]
at \(0\) and the possible linear term
\[
cz
\]
corresponding to a simple pole at \(\infty\). The remainder is holomorphic
on the entire Riemann sphere and therefore constant.

:::

:::

::: {.pf-step #s1-5}

The coefficients \(a\) and \(c\) cannot both be nonzero.


::: pf-proof

If \(a\ne0\) and \(c\ne0\), then
\[
g(z)=0
\]
is equivalent to
\[
cz^2+bz+a=0.
\]
This quadratic has two roots in \(\CC\), counted with multiplicity,
and their product is
\[
\frac ac\ne0.
\]
Thus every root is nonzero, so \(g\) would take the forbidden value \(0\)
at a point of \(\CC^\times\), contradicting
\[
g(\CC^\times)\subseteq\CC^\times.
\]

:::

:::

::: pf-step

If \(a=0\), then
\[
\boxed{g(z)=cz}
\]
for some \(c\in\CC^\times\).


::: pf-proof

With \(a=0\),
\[
g(z)=b+cz.
\]
Injectivity rules out \(c=0\). If \(b\ne0\), then
\[
z=-\frac bc
\]
is a nonzero zero of \(g\), impossible. Hence \(b=0\), and \(c\ne0\).

:::

:::

::: {.pf-step #s1-7}

If \(c=0\), then
\[
\boxed{g(z)=\frac az}
\]
for some \(a\in\CC^\times\).


::: pf-proof

With \(c=0\),
\[
g(z)=\frac az+b.
\]
Injectivity rules out \(a=0\). If \(b\ne0\), then
\[
z=-\frac ab
\]
is a nonzero zero of \(g\), impossible. Hence \(b=0\), and \(a\ne0\).

:::

:::

::: {.pf-step #s1-8}

Therefore every injective holomorphic self-map of
\(\CC^\times\) is exactly one of
\[
\boxed{
g_a(z)=az
\qquad\text{or}\qquad
h_a(z)=\frac az,
\qquad
a\in\CC^\times}.
\]


::: pf-proof

Steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref} exhaust the possibilities from step [](#s1-4){.pf-ref}.
Conversely, both displayed maps are visibly injective holomorphic self-maps
of \(\CC^\times\).

:::

:::

::: {.pf-step #s1-9}

The inverse Möbius transformation is
\[
\boxed{
T^{-1}(w)
=
\frac{w}{1-w}}.
\]


::: pf-proof

Solving
\[
w=\frac z{z+1}
\]
for \(z\) gives
\[
w(z+1)=z,
\qquad
w=z(1-w),
\qquad
z=\frac{w}{1-w}.
\]

:::

:::

::: {.pf-step #s1-10}

Conjugating \(g_a(z)=az\) back to \(\Omega\) gives
\[
\boxed{
f_a(w)
=
\frac{aw}{1+(a-1)w},
\qquad
a\in\CC^\times}.
\]


::: pf-proof

Using step [](#s1-9){.pf-ref},
\[
\begin{aligned}
T\!\left(
aT^{-1}(w)
\right)
&=
T\!\left(
\frac{aw}{1-w}
\right)\\
&=
\frac{\frac{aw}{1-w}}
{\frac{aw}{1-w}+1}\\
&=
\frac{aw}{1+(a-1)w}.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-11}

Conjugating \(h_a(z)=a/z\) back to \(\Omega\) gives
\[
\boxed{
\widetilde f_a(w)
=
\frac{a(1-w)}
{a+(1-a)w},
\qquad
a\in\CC^\times}.
\]


::: pf-proof

Again using step [](#s1-9){.pf-ref},
\[
\begin{aligned}
T\!\left(
\frac{a}{T^{-1}(w)}
\right)
&=
T\!\left(
\frac{a(1-w)}{w}
\right)\\
&=
\frac{a(1-w)}
{a(1-w)+w}\\
&=
\frac{a(1-w)}
{a+(1-a)w}.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-12}

The complete list in part (b) is therefore
\[
\boxed{
f(w)
=
\frac{aw}{1+(a-1)w}
\quad\text{or}\quad
f(w)
=
\frac{a(1-w)}{a+(1-a)w},
\qquad
a\in\CC^\times}.
\]


::: pf-proof

By step [](#s1-1){.pf-ref}, every injective \(f\) is conjugate to an injective \(g\) on
\(\CC^\times\). Step [](#s1-8){.pf-ref} classifies the latter, and steps [](#s1-10){.pf-ref} and [](#s1-11){.pf-ref} compute their conjugates. Conversely, every displayed map is a
conjugate of an injective holomorphic self-map of \(\CC^\times\), so
it is injective and holomorphic on \(\Omega\).

:::

:::

::: {.pf-step #s1-13}

Every injective holomorphic \(f:\Omega\to\Omega\) is surjective.


::: pf-proof

The maps
\[
z\mapsto az
\qquad\text{and}\qquad
z\mapsto\frac az
\]
are surjective on \(\CC^\times\). Since \(T\) is a bijection, their
conjugates in steps [](#s1-10){.pf-ref} and [](#s1-11){.pf-ref} are surjective on \(\Omega\). By step
[](#s1-12){.pf-ref}, every injective \(f\) is one of these conjugates. Hence
\[
\boxed{f(\Omega)=\Omega}.
\]

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} proves part (a), and step [](#s1-12){.pf-ref} gives the complete list required
in part (b).

:::

:::

:::
