---
schema: qual/card@1
id: P-UCLARA18F-07
kind: problem
title: Entire functions with integrable $\log\abs{f}$ are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Subharmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 7. Let $f(z)$ be an analytic function on the entire complex plane $\CC$ such that
$$
U(z)=\log\abs{f(z)}
$$
is Lebesgue-area integrable:
$$
\int_{\CC}\abs{U(z)}\,dx\,dy<\infty.
$$
Prove that $f$ is constant.
:::

::: {.solution}

Put $u(z)=\log\abs{f(z)}$.

::: pf

::: {.pf-step #s1-1}

If $f$ is nonconstant, then there is $z_0\in\CC$ such that
$$
u(z_0)>1.
$$


::: pf-proof

If $\abs{f(z)}\le e$ for every $z\in\CC$, then Liouville's theorem would make $f$ constant. Hence a nonconstant entire $f$ has some $z_0$ with $\abs{f(z_0)}>e$, which is equivalent to the displayed inequality.

:::

:::

::: {.pf-step #s1-2}

For every $r>0$,
$$
\int_0^{2\pi}u(z_0+re^{i\theta})\,d\theta>2\pi.
$$


::: pf-proof

For an entire function, $\log\abs{f}$ is subharmonic, with the value $-\infty$ allowed at zeros. Its submean inequality at $z_0$ gives
$$
u(z_0)
\le\frac1{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})\,d\theta.
$$
Step [](#s1-1){.pf-ref} now yields the asserted strict lower bound.

:::

:::

::: {.pf-step #s1-3}

If $f$ were nonconstant, then
$$
\int_{\CC}\abs{u(z)}\,dx\,dy=\infty.
$$


::: pf-proof

By step [](#s1-2){.pf-ref} and the triangle inequality,
$$
\int_0^{2\pi}\abs{u(z_0+re^{i\theta})}\,d\theta
\ge
\abs{\int_0^{2\pi}u(z_0+re^{i\theta})\,d\theta}
>2\pi
$$
for every $r>0$. Tonelli's theorem in polar coordinates centered at $z_0$ therefore gives
$$
\begin{aligned}
\int_{\CC}\abs{u(z)}\,dx\,dy
&=\int_0^\infty\int_0^{2\pi}\abs{u(z_0+re^{i\theta})}\,r\,d\theta\,dr\\
&\ge2\pi\int_0^\infty r\,dr
=\infty.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Hence $\boxed{f\text{ is constant}}$.


::: pf-proof

Step [](#s1-3){.pf-ref} contradicts the assumed absolute integrability of $U=u$ whenever $f$ is nonconstant. Therefore $f$ must be constant.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
