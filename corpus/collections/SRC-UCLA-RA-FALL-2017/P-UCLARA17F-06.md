---
schema: qual/card@1
id: P-UCLARA17F-06
kind: problem
title: $L^2$ boundedness of the truncated Riesz potential $\int_{|w-z|\le1}\frac{|f(w)|}{|w-z|}\,dA(w)$
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 6. Let $f\in L^2(\CC)$. For $z\in\CC$ define
\[
g(z)=\int_{\{w\in\CC:|w-z|\le1\}}\frac{|f(w)|}{|w-z|}\,dA(w),
\]
where $dA$ denotes integration with respect to Lebesgue measure on $\CC\cong\RR^2$. Show that $|g(z)|<\infty$ for almost every $z\in\CC$ and that $g\in L^2(\CC)$.
:::

::: {.solution}

Define
\[
k(u)
=
\frac{\mathbf 1_{\{|u|\le1\}}}{|u|}
\]
on \(\CC\cong\RR^2\).

::: pf

::: {.pf-step #s1-1}

The kernel \(k\) belongs to \(L^1(\CC)\).


::: pf-proof

Using polar coordinates,
\[
\int_{\CC}k(u)\,dA(u)
=
\int_{|u|\le1}\frac{1}{|u|}\,dA(u)
=
\int_0^{2\pi}\int_0^1\frac1r\,r\,dr\,d\theta
=
2\pi.
\]
Thus the integral is finite.

:::

:::

::: {.pf-step #s1-2}

More precisely,
\[
\boxed{
\|k\|_1=2\pi}.
\]


::: pf-proof

This is the value computed in step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

After the change of variables
\[
u=w-z,
\]
the function \(g\) can be written as
\[
\boxed{
g(z)
=
\int_{\CC}
|f(z+u)|\,k(u)\,dA(u)}.
\]


::: pf-proof

The condition
\[
|w-z|\le1
\]
becomes
\[
|u|\le1,
\]
and
\[
dA(w)=dA(u).
\]
Thus
\[
\frac{|f(w)|}{|w-z|}
=
|f(z+u)|\,k(u).
\]

:::

:::

::: {.pf-step #s1-4}

The function
\[
(z,u)\longmapsto |f(z+u)|k(u)
\]
is measurable on \(\CC\times\CC\).


::: pf-proof

The map
\[
(z,u)\mapsto z+u
\]
is continuous, \(f\) has a measurable representative, and \(k\) is measurable. Products and compositions of measurable functions are measurable.

:::

:::

::: pf-step

Therefore \(g\) is measurable as an extended-valued nonnegative function.


::: pf-proof

By step [](#s1-4){.pf-ref}, Tonelli's theorem implies that the integral in \(u\) defines a measurable function of \(z\), possibly taking the value \(+\infty\).

:::

:::

::: {.pf-step #s1-6}

One has
\[
\|g\|_2
\le
\int_{\CC}
k(u)
\left(
\int_{\CC}
|f(z+u)|^2\,dA(z)
\right)^{1/2}
dA(u).
\]


::: pf-proof

Apply Minkowski's integral inequality to the nonnegative function
\[
H(z,u)=|f(z+u)|k(u):
\]
\[
\left\|
\int H(\cdot,u)\,dA(u)
\right\|_{L^2_z}
\le
\int
\|H(\cdot,u)\|_{L^2_z}
\,dA(u).
\]
Since \(k(u)\) is independent of \(z\),
\[
\|H(\cdot,u)\|_2
=
k(u)
\left(
\int |f(z+u)|^2\,dA(z)
\right)^{1/2}.
\]

:::

:::

::: {.pf-step #s1-7}

For every \(u\in\CC\),
\[
\boxed{
\left(
\int_{\CC}
|f(z+u)|^2\,dA(z)
\right)^{1/2}
=
\|f\|_2}.
\]


::: pf-proof

Lebesgue measure is translation invariant. With
\[
w=z+u,
\]
\[
\int_{\CC}|f(z+u)|^2\,dA(z)
=
\int_{\CC}|f(w)|^2\,dA(w).
\]

:::

:::

::: pf-step

Hence
\[
\|g\|_2
\le
\|f\|_2
\int_{\CC}k(u)\,dA(u).
\]


::: pf-proof

Substitute the constant value from step [](#s1-7){.pf-ref} into step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Using step [](#s1-2){.pf-ref},
\[
\boxed{
\|g\|_2
\le
2\pi\|f\|_2}.
\]


::: pf-proof

\[
\int_{\CC}k(u)\,dA(u)
=
2\pi.
\]

:::

:::

::: {.pf-step #s1-10}

Therefore
\[
\boxed{
g\in L^2(\CC)}.
\]


::: pf-proof

The right-hand side of step [](#s1-9){.pf-ref} is finite because
\[
f\in L^2(\CC).
\]
Thus \(\|g\|_2<\infty\).

:::

:::

::: {.pf-step #s1-11}

In particular,
\[
\boxed{
|g(z)|<\infty}
\]
for almost every \(z\in\CC\).


::: pf-proof

An \(L^2\)-function is finite almost everywhere; otherwise the integral of its square would be infinite.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} proves \(g\in L^2\), and step [](#s1-11){.pf-ref} gives the almost-everywhere finiteness.

:::

:::

:::
