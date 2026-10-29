---
schema: qual/card@1
id: P-UCLARA17S-12
kind: problem
title: Derivative growth of Hölder continuous analytic functions on the disk
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $0<\alpha<1$ and let $f(z)$ be analytic on the unit disk $D$. Prove that if
$$
|f(z)-f(w)|\le C|z-w|^\alpha
$$
for all $z,w\in D$ and some constant $C\in\RR$, then there is a constant $A=A(C)<\infty$ such that
$$
|f'(z)|\le A(1-|z|)^{\alpha-1}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Fix $z\in D$ and set
$$
d\coloneqq1-|z|,
\qquad
r\coloneqq\frac d2.
$$
Then the closed disk $\overline{B(z,r)}$ is contained in $D$.


::: pf-proof

If $|\zeta-z|\le r$, then
$$
|\zeta|
\le |z|+r
=|z|+\frac{1-|z|}{2}
=\frac{1+|z|}{2}
<1.
$$

:::

:::

::: {.pf-step #s1-2}

Cauchy's derivative formula gives
$$
f'(z)
=\frac1{2\pi i}
\int_{|\zeta-z|=r}
\frac{f(\zeta)-f(z)}{(\zeta-z)^2}\,d\zeta.
$$


::: pf-proof

The constant function $f(z)$ has derivative $0$. Apply Cauchy's derivative formula to the analytic function
$$
\zeta\longmapsto f(\zeta)-f(z)
$$
on the circle from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

One has
$$
|f'(z)|
\le C r^{\alpha-1}.
$$


::: pf-proof

On $|\zeta-z|=r$, the Hölder hypothesis gives
$$
|f(\zeta)-f(z)|\le C r^\alpha.
$$
Using step [](#s1-2){.pf-ref} and the fact that the circle has length $2\pi r$,
$$
\begin{aligned}
|f'(z)|
&\le\frac1{2\pi}
(2\pi r)
\frac{C r^\alpha}{r^2}\\
&=C r^{\alpha-1}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
|f'(z)|
\le 2C(1-|z|)^{\alpha-1}}
$$
for every $z\in D$.


::: pf-proof

Substitute $r=(1-|z|)/2$ from step [](#s1-1){.pf-ref} into step [](#s1-3){.pf-ref}:
$$
C r^{\alpha-1}
=C\left(\frac{1-|z|}{2}\right)^{\alpha-1}
=2^{1-\alpha}C(1-|z|)^{\alpha-1}.
$$
Because $0<\alpha<1$, one has $2^{1-\alpha}\le2$. Thus the required constant may be taken to be
$$
A(C)=2C<\infty.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required derivative estimate.

:::

:::

:::
