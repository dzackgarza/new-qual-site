---
schema: qual/card@1
id: E-YZUOC
kind: problem
title: Residue at a pole of order $m$, and $\oint_C e^\tau/(\tau^2+\pi^2)^2\,d\tau$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Poles
  - Contour Integration
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source part (a) omitted the factor 1/(m-1)! and had an unbalanced parenthesis, so it was false for m > 2; the statement now includes 1/(m-1)! and orients C counterclockwise.'
---

::: {.exercise}
(a) Let $F$ be an analytic function inside and on a simple closed curve $C$, oriented counterclockwise, except for a pole of order $m\geq 1$ at $z=a$ inside $C$.
Prove that

$$\frac{1}{2 \pi i}\oint_{C} F(\tau) d\tau =
\frac{1}{(m-1)!}\lim_{\tau\rightarrow a} \frac{d^{m-1}}{d\tau^{m-1}}\big((\tau-a)^m F(\tau)\big).$$

(b) Evaluate $$\oint_{C}\frac{e^{\tau}}{(\tau^2+\pi^2)^2}d\tau$$
where $C$ is the circle $\abs{z}=4$.
:::

::: {.solution}
Write the Laurent expansion of $F$ at $a$ as $F(\tau)=\sum_{k=-m}^{\infty}c_k(\tau-a)^k$.

::: pf

::: {.pf-step #residue-integral}

$\frac{1}{2\pi i}\oint_C F(\tau)\,d\tau = c_{-1}$.

::: pf-proof

$a$ is the only singularity of $F$ inside $C$, so the residue theorem gives $\frac{1}{2\pi i}\oint_C F = \operatorname{Res}_{\tau=a}F = c_{-1}$.

:::

:::

::: {.pf-step #residue-formula}

$\frac{1}{(m-1)!}\lim_{\tau\to a}\frac{d^{m-1}}{d\tau^{m-1}}\bigl((\tau-a)^mF(\tau)\bigr) = c_{-1}$, which with step [](#residue-integral){.pf-ref} proves part (a).

::: pf-proof

$g(\tau) = (\tau-a)^mF(\tau) = \sum_{j=0}^\infty c_{j-m}(\tau-a)^j$ is holomorphic at $a$. Its $(m-1)$-st derivative is continuous at $a$ and equals $(m-1)!\,c_{-1}$ there, the coefficient of $(\tau-a)^{m-1}$ being $c_{-1}$.

:::

:::

::: {.pf-step #residues}

The integrand $h(z) = e^z/(z^2+\pi^2)^2$ has double poles at $\pm i\pi$, both inside $\abs{z}=4$, with $\operatorname{Res}_{z=\pm i\pi}h = \frac{1}{4\pi^2} \pm \frac{i}{4\pi^3}$.

::: pf-proof

$z^2+\pi^2 = (z-i\pi)(z+i\pi)$ and $\pi < 4$. By part (a) with $m=2$, $\operatorname{Res}_{z=i\pi}h = \frac{d}{dz}\frac{e^z}{(z+i\pi)^2}\evalfrom_{z=i\pi} = \frac{e^{i\pi}}{(2i\pi)^2} - \frac{2e^{i\pi}}{(2i\pi)^3} = \frac{1}{4\pi^2} + \frac{i}{4\pi^3}$. The same computation at $-i\pi$, with $e^{-i\pi} = -1$ and $(-2i\pi)^3 = 8i\pi^3$, gives $\frac{1}{4\pi^2} - \frac{i}{4\pi^3}$.

:::

:::

::: pf-step

$\oint_C\frac{e^\tau}{(\tau^2+\pi^2)^2}\,d\tau = \boxed{\dfrac{i}{\pi}}$.

::: pf-proof

By step [](#residues){.pf-ref} and the residue theorem, the integral is $2\pi i\cdot\frac{2}{4\pi^2} = \frac{i}{\pi}$.

:::

:::

:::

:::
