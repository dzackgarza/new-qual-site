---
schema: qual/card@1
id: P-UCLARA15S-05
kind: problem
title: Plancherel identity for a Gaussian transform
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $u\in L^2(\mathbb R)$ and set
\[
U(x,\xi)=\int_{\mathbb R}e^{-(x+i\xi-y)^2/2}u(y)\,dy,
\qquad x,\xi\in\mathbb R.
\]
Show that $U(x,\xi)$ is well defined on $\mathbb R^2$ and that there exists a constant $C>0$ such that for all $u\in L^2(\mathbb R)$,
\[
\iint_{\mathbb R^2}|U(x,\xi)|^2e^{-\xi^2}\,dx\,d\xi
=C\int_{\mathbb R}|u(y)|^2\,dy.
\]
Determine $C$ explicitly.
:::

Use the Fourier transform convention
\[
\mathcal Fh(\eta)
\coloneqq
\int_{\mathbb R}h(y)e^{-i\eta y}\,dy,
\]
for which Plancherel's theorem reads
\[
\int_{\mathbb R}|\mathcal Fh(\eta)|^2\,d\eta
=
2\pi
\int_{\mathbb R}|h(y)|^2\,dy.
\]

::: pf

::: {.pf-step #s1-1}

For every $(x,\xi)\in\mathbb R^2$, the integral defining $U(x,\xi)$ converges absolutely.


::: pf-proof

Since
\[
\left|
e^{-(x+i\xi-y)^2/2}
\right|
=
e^{\xi^2/2}
e^{-(x-y)^2/2},
\]
Cauchy--Schwarz gives
\[
\begin{aligned}
\int_{\mathbb R}
\left|
e^{-(x+i\xi-y)^2/2}u(y)
\right|dy
&\le
e^{\xi^2/2}
\left(
\int_{\mathbb R}
e^{-(x-y)^2}\,dy
\right)^{1/2}
\|u\|_2\\
&=
e^{\xi^2/2}
\pi^{1/4}
\|u\|_2
<
\infty.
\end{aligned}
\]
Thus $U(x,\xi)$ is well defined.

:::

:::

::: {.pf-step #s1-2}

For fixed $x\in\mathbb R$, define
\[
h_x(y)
\coloneqq
e^{xy-y^2/2}u(y).
\]
Then $h_x\in L^2(\mathbb R)$ and
\[
U(x,\xi)
=
e^{-x^2/2}
e^{\xi^2/2}
e^{-ix\xi}
\mathcal Fh_x(-\xi).
\]


::: pf-proof

Complete the square:
\[
xy-\frac{y^2}{2}
=
\frac{x^2}{2}
-\frac{(y-x)^2}{2}.
\]
Hence
\[
|e^{xy-y^2/2}|
\le
e^{x^2/2},
\]
so $h_x\in L^2$ because $u\in L^2$.

Also,
\[
\begin{aligned}
-\frac{(x+i\xi-y)^2}{2}
&=
-\frac{x^2}{2}
+\frac{\xi^2}{2}
-ix\xi
+xy
-\frac{y^2}{2}
+i\xi y.
\end{aligned}
\]
Substituting this expansion into the definition of $U$ gives
\[
U(x,\xi)
=
e^{-x^2/2}
e^{\xi^2/2}
e^{-ix\xi}
\int_{\mathbb R}
h_x(y)e^{i\xi y}\,dy.
\]
The last integral is $\mathcal Fh_x(-\xi)$.

:::

:::

::: {.pf-step #s1-3}

For every fixed $x\in\mathbb R$,
\[
\int_{\mathbb R}
|U(x,\xi)|^2e^{-\xi^2}\,d\xi
=
2\pi
\int_{\mathbb R}
e^{-(x-y)^2}
|u(y)|^2\,dy.
\]


::: pf-proof

By step [](#s1-2){.pf-ref},
\[
|U(x,\xi)|^2e^{-\xi^2}
=
e^{-x^2}
|\mathcal Fh_x(-\xi)|^2.
\]
Therefore Plancherel gives
\[
\begin{aligned}
\int_{\mathbb R}
|U(x,\xi)|^2e^{-\xi^2}\,d\xi
&=
e^{-x^2}
\int_{\mathbb R}
|\mathcal Fh_x(\xi)|^2\,d\xi\\
&=
2\pi e^{-x^2}
\int_{\mathbb R}
|h_x(y)|^2\,dy\\
&=
2\pi
\int_{\mathbb R}
e^{-x^2+2xy-y^2}
|u(y)|^2\,dy\\
&=
2\pi
\int_{\mathbb R}
e^{-(x-y)^2}
|u(y)|^2\,dy.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-4}

One has
\[
\boxed{
\iint_{\mathbb R^2}
|U(x,\xi)|^2e^{-\xi^2}\,dx\,d\xi
=
2\pi^{3/2}
\int_{\mathbb R}|u(y)|^2\,dy
}.
\]


::: pf-proof

The integrand in step [](#s1-3){.pf-ref} is nonnegative, so Tonelli's theorem permits integration in $x$ and $y$ in either order:
\[
\begin{aligned}
\iint_{\mathbb R^2}
|U(x,\xi)|^2e^{-\xi^2}\,dx\,d\xi
&=
2\pi
\int_{\mathbb R}
\int_{\mathbb R}
e^{-(x-y)^2}
|u(y)|^2\,dy\,dx\\
&=
2\pi
\int_{\mathbb R}
|u(y)|^2
\left(
\int_{\mathbb R}
e^{-(x-y)^2}\,dx
\right)dy\\
&=
2\pi\sqrt\pi
\int_{\mathbb R}|u(y)|^2\,dy.
\end{aligned}
\]
Since
\[
2\pi\sqrt\pi
=
2\pi^{3/2},
\]
the boxed identity follows.

:::

:::

::: {.pf-step #s1-5}

Thus the required constant is
\[
\boxed{C=2\pi^{3/2}}.
\]


::: pf-proof

Compare the identity in step [](#s1-4){.pf-ref} with the form required in the problem.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves well-definedness, and steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} prove the norm identity and determine the constant.

:::

:::
