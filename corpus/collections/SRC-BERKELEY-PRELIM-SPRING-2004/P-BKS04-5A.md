---
schema: qual/card@1
id: P-BKS04-5A
kind: problem
title: Limit of $e^{it^2}(f(t)-f(-t))$ for $f'+2itf=e^{2it}$, $f(0)=0$
classification:
  areas: [prelim]
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Suppose $f\colon\RR\to\CC$ satisfies $f'(t)+2itf(t)=e^{2it}$ and $f(0)=0$. Compute

$$
\lim_{t\to+\infty}e^{it^2}(f(t)-f(-t)).
$$

You may assume $\int_0^\infty e^{-t^2}\,dt=\sqrt\pi/2$.
:::

::: {.solution}

The argument is the card's own: an integrating factor solves the linear equation, and the resulting integral is a Fresnel integral whose value is given.

::: pf

::: {.pf-step #factor}

With the integrating factor $e^{it^{2}}$, $\dfrac{d}{dt}\bigl(e^{it^{2}}f(t)\bigr)=e^{it^{2}}\bigl(f'(t)+2itf(t)\bigr)=e^{i(t^{2}+2t)}$.

::: pf-proof

The product rule gives $\frac{d}{dt}(e^{it^{2}}f)=e^{it^{2}}\cdot2itf+e^{it^{2}}f'=e^{it^{2}}(f'+2itf)$, and the differential equation says $f'+2itf=e^{2it}$. So the derivative is $e^{it^{2}}e^{2it}=e^{i(t^{2}+2t)}$.

:::

:::

::: {.pf-step #solve}

$e^{it^{2}}f(t)=e^{-i}\displaystyle\int_{0}^{t}e^{i(x+1)^{2}}dx$.

::: pf-proof

Integrating the derivative of step [](#factor){.pf-ref} from $0$ to $t$ and using $f(0)=0$,
$$
e^{it^{2}}f(t)-0=\int_{0}^{t}e^{i(x^{2}+2x)}dx.
$$
Completing the square, $x^{2}+2x=(x+1)^{2}-1$, so the integrand is $e^{-i}e^{i(x+1)^{2}}$.

:::

:::

::: {.pf-step #difference}

$e^{it^{2}}\bigl(f(t)-f(-t)\bigr)=e^{-i}\displaystyle\int_{-t}^{t}e^{i(x+1)^{2}}dx$.

::: pf-proof

Apply step [](#solve){.pf-ref} twice: at $t$ and at $-t$, noting $e^{i(-t)^{2}}=e^{it^{2}}$. Subtracting the two expressions and factoring out $e^{-i}$ leaves the integral over $[-t,t]$, since $\int_{0}^{t}-\int_{0}^{-t}=\int_{-t}^{t}$.

:::

:::

::: {.pf-step #fresnel}

$\displaystyle\lim_{t\to+\infty}\int_{-t}^{t}e^{i(x+1)^{2}}dx=\sqrt{\pi}\,e^{i\pi/4}$.

::: pf-proof

Substituting $u=x+1$ gives $\int_{-t}^{t}e^{i(x+1)^{2}}dx=\int_{-t+1}^{t+1}e^{iu^{2}}du\to\int_{-\infty}^{\infty}e^{iu^{2}}du$ as $t\to\infty$. The Fresnel integral equals $\sqrt{\pi i}=\sqrt{\pi}e^{i\pi/4}$: rotating the contour of $\int_{\RR}e^{-z^{2}}dz=\sqrt\pi$ by $\pi/4$ is justified because the integrand decays on the two closing arcs, and $e^{iu^{2}}=e^{-(e^{-i\pi/4}u)^{2}}$ along that rotation.

:::

:::

::: {.pf-step #conclusion}

$\displaystyle\lim_{t\to+\infty}e^{it^{2}}\bigl(f(t)-f(-t)\bigr)=\sqrt{\pi}\,e^{i(\pi/4-1)}$.

::: pf-proof

By steps [](#difference){.pf-ref} and [](#fresnel){.pf-ref},
$$
\boxed{\lim_{t\to+\infty}e^{it^{2}}\bigl(f(t)-f(-t)\bigr)=e^{-i}\sqrt{\pi}e^{i\pi/4}=\sqrt{\pi}\,e^{i(\pi/4-1)}.}
$$

:::

:::

:::

:::
