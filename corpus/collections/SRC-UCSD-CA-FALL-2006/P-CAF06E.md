---
schema: qual/card@1
id: P-CAF06E
kind: problem
title: "Counting roots of a polynomial in the right half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
How many roots of the equation $z^4 + 8z^3 + 3z^2 + 8z + 3 = 0$ lie in the right half plane?
Justify your answer.
:::

::: {.solution}

The argument is the card's own, by the argument principle on the right half-disc; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $p(z)=z^{4}+8z^{3}+3z^{2}+8z+3$.

::: pf

::: {.pf-step #axis}
$p$ has no zero on the imaginary axis, and the change of $\arg p$ along the segment from $-iR$ to $iR$ tends to $0$ as $R\to\infty$.

::: pf-proof
For real $y$,
$$
p(iy)=y^{4}-8iy^{3}-3y^{2}+8iy+3=\big(y^{4}-3y^{2}+3\big)+8iy\big(1-y^{2}\big),
$$
and with $t=y^{2}$ one has $t^{2}-3t+3=\big(t-\tfrac32\big)^{2}+\tfrac34>0$, so $\operatorname{Re}p(iy)>0$ for every $y$; in particular $p(iy)\ne0$. Hence $p(iy)$ lies in the open right half-plane, and the continuous branch of $\arg$ with values in $(-\pi/2,\pi/2)$ applies along the whole segment. For $\abs{y}$ large, $p(iy)=y^{4}\big(1+O(y^{-2})\big)$ has argument tending to $0$, since $y^{4}>0$; so the change of argument along $[-iR,iR]$ is $\arg p(iR)-\arg p(-iR)\to0$.
:::

:::

::: {.pf-step #arc}
The change of $\arg p$ along the right semicircle $z=Re^{i\theta}$, $-\pi/2\le\theta\le\pi/2$, tends to $4\pi$.

::: pf-proof
On that arc, $\dfrac{p(z)}{z^{4}}=1+\dfrac{8}{z}+\dfrac{3}{z^{2}}+\dfrac{8}{z^{3}}+\dfrac{3}{z^{4}}=1+O(R^{-1})$ uniformly as $R\to\infty$. For large $R$ the value stays in the disc of radius $\tfrac12$ about $1$, on which the principal branch of $\log$ is defined, so $\arg p(z)=\arg z^{4}+o(1)$ uniformly there. Since $z^{4}=R^{4}e^{4i\theta}$ and $\theta$ runs from $-\pi/2$ to $\pi/2$, the change of $\arg z^{4}$ is $4\big(\tfrac{\pi}{2}-(-\tfrac{\pi}{2})\big)=4\pi$, and the $o(1)$ perturbation does not change the change of argument in the limit.
:::

:::

::: {.pf-step #count}
$p$ has exactly $2$ zeros in the right half-plane, counted with multiplicity.

::: pf-proof
For $R$ large the positively oriented boundary of the right half-disc $\{z:\abs{z}\le R,\ \operatorname{Re}z\ge0\}$ consists of the segment from $-iR$ to $iR$ followed by the semicircle from $iR$ to $-iR$; $p$ has no zero on that boundary by step [](#axis){.pf-ref}, and $p$ is a polynomial, hence holomorphic everywhere. The argument principle then says that the number of zeros of $p$ inside, counted with multiplicity, is $\frac{1}{2\pi}$ times the total change of $\arg p$ around this boundary, which by steps [](#axis){.pf-ref} and [](#arc){.pf-ref} tends to $\frac{1}{2\pi}(0+4\pi)=2$. All zeros of $p$ lie in some disc, so for $R$ large enough the count inside the half-disc is the count in the right half-plane.
:::

:::

:::
:::
