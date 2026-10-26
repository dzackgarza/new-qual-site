---
schema: qual/card@1
id: P-UCLARA18F-07
kind: problem
title: Entire functions with integrable $\log|f|$ are constant
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 7. Let $f(z)$ be an analytic function on the entire complex plane $\mathbb C$ such that
\[
U(z)=\log|f(z)|
\]
is Lebesgue-area integrable:
\[
\int_{\mathbb C}|U(z)|\,dx\,dy<\infty.
\]
Prove that $f$ is constant.
:::

Put \(u(z)=\log|f(z)|\).

::: pf

::: pf-step

If \(f\) is nonconstant, then there is \(z_0\in\mathbb C\) such that
\[
u(z_0)>1.
\]


::: pf-proof

If \(|f(z)|\le e\) for every \(z\in\mathbb C\), then Liouville's theorem would make \(f\) constant. Hence a nonconstant entire \(f\) has some \(z_0\) with \(|f(z_0)|>e\), which is equivalent to the displayed inequality.

:::

:::

::: pf-step

For every \(r>0\),
\[
\int_0^{2\pi}u(z_0+re^{i\theta})\,d\theta>2\pi.
\]


::: pf-proof

For an entire function, \(\log|f|\) is subharmonic, with the value \(-\infty\) allowed at zeros. Its submean inequality at \(z_0\) gives
\[
u(z_0)
\le\frac1{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})\,d\theta.
\]
Step <1>1 now yields the asserted strict lower bound.

:::

:::

::: pf-step

If \(f\) were nonconstant, then
\[
\int_{\mathbb C}|u(z)|\,dx\,dy=\infty.
\]


::: pf-proof

By step <1>2 and the triangle inequality,
\[
\int_0^{2\pi}|u(z_0+re^{i\theta})|\,d\theta
\ge
\left|\int_0^{2\pi}u(z_0+re^{i\theta})\,d\theta\right|
>2\pi
\]
for every \(r>0\). Tonelli's theorem in polar coordinates centered at \(z_0\) therefore gives
\[
\begin{aligned}
\int_{\mathbb C}|u(z)|\,dx\,dy
&=\int_0^\infty\int_0^{2\pi}|u(z_0+re^{i\theta})|\,r\,d\theta\,dr\\
&\ge2\pi\int_0^\infty r\,dr
=\infty.
\end{aligned}
\]

:::

:::

::: pf-step

Hence \(\boxed{f\text{ is constant}}\).


::: pf-proof

Step <1>3 contradicts the assumed absolute integrability of \(U=u\) whenever \(f\) is nonconstant. Therefore \(f\) must be constant.

:::

:::

::: pf-qed

Step <1>4 is the required conclusion.

:::

:::
