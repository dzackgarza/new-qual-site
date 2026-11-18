---
schema: qual/card@1
id: P-Q5LN7
kind: problem
title: The cube and the square roots of $-2+2\sqrt{3}i$
classification:
  areas:
  - prelim
  topics:
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $\alpha$ be the complex number $-2+2\sqrt{3}i$.
Express $\alpha^3$ and the two square roots of $\alpha$ in the standard form $a+bi$.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/grad_prelim_Fall04.pdf` and no solutions sheet accompanies it, so the computation below is the card's own. It uses only the polar form of a complex number and De Moivre's formula, and the two answers are checked by direct multiplication in the last step.

Throughout, $\alpha\coloneqq-2+2\sqrt3\,i$, and for real $\theta$ one writes $e^{i\theta}\coloneqq\cos\theta+i\sin\theta$, so that $e^{i\theta}e^{i\phi}=e^{i(\theta+\phi)}$.

::: pf

::: {.pf-step #polar}
$\alpha=4e^{2\pi i/3}$.

:::: pf-proof

::: {.pf-step #modulus}
$\abs{\alpha}=4$.

::: pf-proof
$\abs{\alpha}^{2}=(-2)^{2}+(2\sqrt3)^{2}=4+12=16$, and a modulus is nonnegative, so $\abs{\alpha}=4$.
:::

:::

::: {.pf-step #argument}
The argument of $\alpha$ is $2\pi/3$.

::: pf-proof
$\alpha$ has negative real part and positive imaginary part, so its argument lies in $(\pi/2,\pi)$, where it is determined by $\tan\theta=\dfrac{2\sqrt3}{-2}=-\sqrt3$; the angle in $(\pi/2,\pi)$ with tangent $-\sqrt3$ is $\pi-\pi/3=2\pi/3$. Hence $\alpha=4\big(\cos(2\pi/3)+i\sin(2\pi/3)\big)=4e^{2\pi i/3}$.
:::

:::

::::

:::

::: {.pf-step #cube}
$$
\boxed{\alpha^{3}=64.}
$$

::: pf-proof
By step [](#polar){.pf-ref} and the multiplicativity of the exponential, $\alpha^{3}=4^{3}\big(e^{2\pi i/3}\big)^{3}=64\,e^{2\pi i}=64(\cos2\pi+i\sin2\pi)=64$.
:::

:::

::: {.pf-step #roots}
The two square roots of $\alpha$ are
$$
\boxed{1+\sqrt3\,i\quad\text{and}\quad -1-\sqrt3\,i.}
$$

:::: pf-proof

::: {.pf-step #half-angle}
$2e^{\pi i/3}=1+\sqrt3\,i$.

::: pf-proof
$e^{\pi i/3}=\cos(\pi/3)+i\sin(\pi/3)=\tfrac12+\tfrac{\sqrt3}{2}i$, and multiplying by $2$ gives $1+\sqrt3\,i$.
:::

:::

::: {.pf-step #both-roots}
The square roots of $\alpha$ are exactly $\pm2e^{\pi i/3}$.

::: pf-proof
A nonzero complex number $re^{i\theta}$ with $r>0$ has exactly two square roots, $\pm\sqrt{r}\,e^{i\theta/2}$, since $(we^{i\varphi})^{2}=w^{2}e^{2i\varphi}$ and $w\mapsto w^{2}$ is two-to-one away from $0$ on the circle of each radius. Here $r=4$ and $\theta=2\pi/3$ by step [](#polar){.pf-ref}, so $\sqrt r=2$ and $\theta/2=\pi/3$; the two roots are therefore $\pm2e^{\pi i/3}$, which by step [](#half-angle){.pf-ref} are $\pm(1+\sqrt3\,i)$.
:::

:::

::::

:::

::: pf-step
Both answers are confirmed by direct multiplication, so the two displayed values are correct.

::: pf-proof
$(1+\sqrt3\,i)^{2}=1+2\sqrt3\,i+3i^{2}=1-3+2\sqrt3\,i=-2+2\sqrt3\,i=\alpha$, so $1+\sqrt3\,i$ and its negative are square roots of $\alpha$, and by step [](#roots){.pf-ref} they are the only two. For the cube, $\alpha^{2}=(-2+2\sqrt3\,i)^{2}=4-12-8\sqrt3\,i=-8-8\sqrt3\,i$, and $\alpha^{3}=\alpha^{2}\alpha=(-8-8\sqrt3\,i)(-2+2\sqrt3\,i)=16-16\sqrt3\,i+16\sqrt3\,i+48=64$, the middle terms cancelling because $i^{2}=-1$.
:::

:::

:::

:::
