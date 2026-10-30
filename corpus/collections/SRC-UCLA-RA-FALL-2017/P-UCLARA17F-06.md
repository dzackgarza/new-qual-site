---
schema: qual/card@1
id: P-UCLARA17F-06
kind: problem
title: $L^2$ boundedness of the truncated Riesz potential $\int_{\abs{w-z}\le1}\frac{\abs{f(w)}}{\abs{w-z}}\,dA(w)$
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
$$
g(z)=\int_{\{w\in\CC:\abs{w-z}\le1\}}\frac{\abs{f(w)}}{\abs{w-z}}\,dA(w),
$$
where $dA$ denotes integration with respect to Lebesgue measure on $\CC\cong\RR^2$. Show that $\abs{g(z)}<\infty$ for almost every $z\in\CC$ and that $g\in L^2(\CC)$.
:::

::: {.solution}

Define
$$
k(u)
=
\frac{\mathbf 1_{\{\abs{u}\le1\}}}{\abs{u}}
$$
on $\CC\cong\RR^2$.

::: pf

::: {.pf-step #s1-1}

The kernel $k$ belongs to $L^1(\CC)$.


::: pf-proof

Using polar coordinates,
$$
\int_{\CC}k(u)\,dA(u)
=
\int_{\abs{u}\le1}\frac{1}{\abs{u}}\,dA(u)
=
\int_0^{2\pi}\int_0^1\frac1r\,r\,dr\,d\theta
=
2\pi.
$$
Thus the integral is finite.

:::

:::

::: {.pf-step #s1-2}

More precisely,
$$
\boxed{
\norm{k}_1=2\pi}.
$$


::: pf-proof

This is the value computed in step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

After the change of variables
$$
u=w-z,
$$
the function $g$ can be written as
$$
\boxed{
g(z)
=
\int_{\CC}
\abs{f(z+u)}\,k(u)\,dA(u)}.
$$


::: pf-proof

The condition
$$
\abs{w-z}\le1
$$
becomes
$$
\abs{u}\le1,
$$
and
$$
dA(w)=dA(u).
$$
Thus
$$
\frac{\abs{f(w)}}{\abs{w-z}}
=
\abs{f(z+u)}\,k(u).
$$

:::

:::

::: {.pf-step #s1-4}

The function
$$
(z,u)\longmapsto \abs{f(z+u)}k(u)
$$
is measurable on $\CC\times\CC$.


::: pf-proof

The map
$$
(z,u)\mapsto z+u
$$
is continuous, $f$ has a measurable representative, and $k$ is measurable. Products and compositions of measurable functions are measurable.

:::

:::

::: pf-step

Therefore $g$ is measurable as an extended-valued nonnegative function.


::: pf-proof

By step [](#s1-4){.pf-ref}, Tonelli's theorem implies that the integral in $u$ defines a measurable function of $z$, possibly taking the value $+\infty$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\norm{g}_2
\le
\int_{\CC}
k(u)
\left(
\int_{\CC}
\abs{f(z+u)}^2\,dA(z)
\right)^{1/2}
dA(u).
$$


::: pf-proof

Apply Minkowski's integral inequality to the nonnegative function
$$
H(z,u)=\abs{f(z+u)}k(u):
$$
$$
\norm{
\int H(\cdot,u)\,dA(u)
}_{L^2_z}
\le
\int
\norm{H(\cdot,u)}_{L^2_z}
\,dA(u).
$$
Since $k(u)$ is independent of $z$,
$$
\norm{H(\cdot,u)}_2
=
k(u)
\left(
\int \abs{f(z+u)}^2\,dA(z)
\right)^{1/2}.
$$

:::

:::

::: {.pf-step #s1-7}

For every $u\in\CC$,
$$
\boxed{
\left(
\int_{\CC}
\abs{f(z+u)}^2\,dA(z)
\right)^{1/2}
=
\norm{f}_2}.
$$


::: pf-proof

Lebesgue measure is translation invariant. With
$$
w=z+u,
$$
$$
\int_{\CC}\abs{f(z+u)}^2\,dA(z)
=
\int_{\CC}\abs{f(w)}^2\,dA(w).
$$

:::

:::

::: pf-step

Hence
$$
\norm{g}_2
\le
\norm{f}_2
\int_{\CC}k(u)\,dA(u).
$$


::: pf-proof

Substitute the constant value from step [](#s1-7){.pf-ref} into step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Using step [](#s1-2){.pf-ref},
$$
\boxed{
\norm{g}_2
\le
2\pi\norm{f}_2}.
$$


::: pf-proof

$$
\int_{\CC}k(u)\,dA(u)
=
2\pi.
$$

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
g\in L^2(\CC)}.
$$


::: pf-proof

The right-hand side of step [](#s1-9){.pf-ref} is finite because
$$
f\in L^2(\CC).
$$
Thus $\norm{g}_2<\infty$.

:::

:::

::: {.pf-step #s1-11}

In particular,
$$
\boxed{
\abs{g(z)}<\infty}
$$
for almost every $z\in\CC$.


::: pf-proof

An $L^2$-function is finite almost everywhere; otherwise the integral of its square would be infinite.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} proves $g\in L^2$, and step [](#s1-11){.pf-ref} gives the almost-everywhere finiteness.

:::

:::

:::
