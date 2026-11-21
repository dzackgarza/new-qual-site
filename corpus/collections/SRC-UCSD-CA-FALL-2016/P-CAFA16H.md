---
schema: qual/card@1
id: P-CAFA16H
kind: problem
title: 'An $L^2$ harmonic function on $\CC$ is zero'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the circle
    mean-value property weighted by 2s and integrated, the passage to polar coordinates
    over the disc, then Cauchy-Schwarz on the disc with the bound 1/(sqrt(pi) r) times the
    L2 norm over the plane, which tends to 0. Part (b)'s dependence on part (a) is now a
    reference. The collection's provenance is the examination paper only, so no retained
    solution set covers the exercise and the argument is the card's own.
---

::: {.problem}
Let $u: \CC \to \RR$ be a harmonic function such that $\iint \abs{u(x+iy)}^2 \, dx\,dy < \infty$.

(a) Prove that $u(a) = \frac{1}{\pi r^2} \iint_{B_r(a)} u(x+iy)\,dx\,dy$ for every $a \in \CC$ and $r > 0$.
Here $B_r(a) = \{z \in \CC : \abs{z - a} < r\}$.

(b) Prove that $u(z) = 0$ for every $z \in \CC$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Write $\iint_{\CC}\abs{u}^2$ for $\iint_\CC\abs{u(x+iy)}^2\,dx\,dy$, which is finite by hypothesis.

::: pf

::: {.pf-step #circle-mean}
For every $a\in\CC$ and every $s>0$,
$$
u(a)=\frac{1}{2\pi}\int_0^{2\pi}u(a+se^{i\theta})\,d\theta .
$$

::: pf-proof
This is the mean-value property of harmonic functions on a circle: $u$ is harmonic on the disc $B_s(a)$, which is contained in the plane, and the circle of radius $s$ about $a$ is its boundary.
:::

:::

::: {.pf-step #weighted}
For every $a\in\CC$ and every $r>0$,
$$
r^2u(a)=\frac{1}{\pi}\int_0^r\int_0^{2\pi}u(a+se^{i\theta})\,s\,d\theta\,ds .
$$

::: pf-proof
Multiply the identity of step [](#circle-mean){.pf-ref}, valid for every $0<s<r$, by $2s$ and integrate in $s$ from $0$ to $r$: the left side gives $2u(a)\int_0^rs\,ds=r^2u(a)$, and the right side gives $\frac{2}{2\pi}\int_0^r\int_0^{2\pi}u(a+se^{i\theta})s\,d\theta\,ds$, which is the displayed expression. The integrand is continuous on the compact set $[0,r]\times[0,2\pi]$, so the integration is legitimate.
:::

:::

::: {.pf-step}
(a) For every $a\in\CC$ and every $r>0$,
$$
u(a)=\frac{1}{\pi r^2}\iint_{B_r(a)}u(x+iy)\,dx\,dy .
$$

::: pf-proof
In polar coordinates about $a$, the point $a+se^{i\theta}$ with $0\le s<r$ runs over $B_r(a)$, and the area element is $s\,ds\,d\theta$. Hence step [](#weighted){.pf-ref} reads $r^2u(a)=\frac1\pi\iint_{B_r(a)}u$, and dividing by $r^2>0$ gives the claim.
:::

:::

::: {.pf-step}
(b) $u(z)=0$ for every $z\in\CC$.

::: pf-proof

::: {.pf-step #cauchy-schwarz}
For every $a\in\CC$ and every $r>0$,
$$
\abs{u(a)}\le\frac{1}{\sqrt{\pi}\,r}\left(\iint_{\CC}\abs{u}^2\right)^{1/2}.
$$

::: pf-proof
Part (a) gives
$$
\abs{u(a)}\le\frac{1}{\pi r^2}\iint_{B_r(a)}\abs{u}.
$$
Cauchy--Schwarz on $B_r(a)$ bounds that integral by $(\pi r^2)^{1/2}\left(\iint_{B_r(a)}\abs{u}^2\right)^{1/2}$, and the last factor is at most $(\iint_{\CC}\abs{u}^2)^{1/2}$ because $B_r(a)\subset\CC$. Combining,
$$
\abs{u(a)}\le\frac{1}{\pi r^2}(\pi r^2)^{1/2}\left(\iint_{\CC}\abs{u}^2\right)^{1/2}=\frac{1}{\sqrt\pi\,r}\left(\iint_{\CC}\abs{u}^2\right)^{1/2}.
$$
:::

:::

::: {.pf-step}
$u\equiv0$.

::: pf-proof
Fix $a\in\CC$. The bound of step [](#cauchy-schwarz){.pf-ref} holds for every $r>0$, and its right-hand side tends to $0$ as $r\to\infty$, the factor $\left(\iint_{\CC}\abs{u}^2\right)^{1/2}$ being a finite constant. Hence $\abs{u(a)}=0$, and $a$ was arbitrary.
:::

:::

:::

:::

:::
:::
