---
schema: qual/card@1
id: P-UCLARA13S-07
kind: problem
title: Absolute integrability of log modulus forces an entire function to be constant
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
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Let $f:\mathbb C\to\mathbb C$ be entire and suppose $\log|f|$ is absolutely integrable with respect to planar Lebesgue measure.
Show that $f$ is constant.
:::

::: pf

::: pf-step

If $f$ is nonconstant, then there exists $z_0\in\mathbb C$ such that
\[
\log|f(z_0)|>1.
\]


::: pf-proof

If a nonconstant entire function were bounded, Liouville's theorem would make it constant. Thus $f$ is unbounded. In particular there exists $z_0$ with
\[
|f(z_0)|>e,
\]
which is equivalent to the displayed inequality.

:::

:::

::: pf-step

If $f\not\equiv0$, then
\[
u(z)
\coloneqq
\log|f(z)|
\]
is subharmonic on $\mathbb C$.


::: pf-proof

For a nonzero holomorphic function, $\log|f|$ is a standard subharmonic function, taking the value $-\infty$ at zeros. Equivalently, locally one may factor
\[
f(z)=(z-a)^m g(z),
\qquad
g(a)\ne0,
\]
so
\[
\log|f(z)|
=
m\log|z-a|+\log|g(z)|,
\]
the sum of a subharmonic function and a harmonic function.

:::

:::

::: pf-step

Under the nonconstancy assumption, for every $r>0$,
\[
\frac1{2\pi}
\int_0^{2\pi}
\log|f(z_0+re^{i\theta})|\,d\theta
\ge
\log|f(z_0)|
>
1.
\]


::: pf-proof

Apply the sub-mean-value inequality for the subharmonic function from step <1>2 to the circle centered at $z_0$ of radius $r$. Step <1>1 supplies the final strict inequality.

:::

:::

::: pf-step

For every $R>0$,
\[
\int_{B(z_0,R)}
\log|f(z)|\,dA(z)
>
\pi R^2.
\]


::: pf-proof

Using polar coordinates about $z_0$ and step <1>3,
\[
\begin{aligned}
\int_{B(z_0,R)}
\log|f(z)|\,dA(z)
&=
\int_0^R
r
\left(
\int_0^{2\pi}
\log|f(z_0+re^{i\theta})|\,d\theta
\right)dr\\
&>
\int_0^R 2\pi r\,dr\\
&=
\pi R^2.
\end{aligned}
\]
The local logarithmic singularities at zeros are integrable, so these disk integrals are well defined.

:::

:::

::: pf-step

The nonconstancy assumption contradicts absolute integrability of $\log|f|$.


::: pf-proof

Absolute integrability gives
\[
C
\coloneqq
\int_{\mathbb C}
|\log|f(z)||\,dA(z)
<
\infty.
\]
For every $R>0$,
\[
\int_{B(z_0,R)}
\log|f(z)|\,dA(z)
\le
\int_{B(z_0,R)}
|\log|f(z)||\,dA(z)
\le
C.
\]
Step <1>4 gives the incompatible lower bound
\[
\pi R^2<C
\]
for every $R$. Letting $R\to\infty$ gives a contradiction.

:::

:::

::: pf-step

Therefore
\[
\boxed{f\text{ is constant}.}
\]


::: pf-proof

Assuming that $f$ is nonconstant led to the contradiction in step <1>5.

:::

:::

::: pf-qed

Step <1>6 is the desired conclusion.

:::

:::
