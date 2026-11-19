---
schema: qual/card@1
id: P-CASP21C
kind: problem
title: 'The maximum of $\abs{f''(0)}$ over holomorphic functions omitting $(-\infty,0]$ with $f(0)=1$'
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
  - Extremal Problems
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The source is a course examination, so there is no retained solution set behind the card and the problem statement is the source. Each step re-read and the constant recomputed: the principal square root carries Omega onto the right half-plane and fixes 1; the Cayley transform (u-1)/(u+1) sends the right half-plane into the disc because |u+1|^2 - |u-1|^2 = 4 Re u; its derivative at 0 is 2u'(0)/4 = f'(0)/4, using s'(1) = 1/2; Schwarz then gives |f'(0)| <= 4; and the extremal (h(e^{i theta} z))^2 has derivative 4 e^{i theta} at 0. Not claimed: uniqueness of the extremal, which holds only up to the rotation parameter.
---

::: {.problem}
Let $\mathcal{F}$ denote the family of holomorphic functions $f : \DD \to \CC$ such that (i) $f$ omits all strictly negative real numbers, and (ii) $f(0) = 1$.
Find the maximum value of $\abs{f'(0)}$ as $f \in \mathcal{F}$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #range}
Every $f\in\mathcal F$ takes values in $\Omega=\CC\setminus(-\infty,0]$, and the principal square root $s$ of $\Omega$ with $s(1)=1$ maps $\Omega$ onto the right half-plane.

::: pf-proof
Condition (i) says $f$ omits the strictly negative reals, so $f(\DD)\subseteq\Omega$. The principal branch of the square root is holomorphic on $\Omega$, satisfies $s(1)=1$, and has image exactly $\{w:\operatorname{Re}w>0\}$: a number outside $(-\infty,0]$ has an argument in $(-\pi,\pi)$, whose half lies in $(-\pi/2,\pi/2)$, and squaring a point of the right half-plane gives a point whose argument lies in $(-\pi,\pi)$, never a negative real.
:::

:::

::: {.pf-step #cayley}
With $u=s\circ f$, the map $g=(u-1)/(u+1)$ is holomorphic on $\DD$, takes values in $\DD$, and satisfies $g(0)=0$.

::: pf-proof
$u$ is holomorphic with values in the right half-plane, so $u+1$ never vanishes there. For $\operatorname{Re}u>0$ one has $\abs{u-1}<\abs{u+1}$, since $\abs{u+1}^{2}-\abs{u-1}^{2}=4\operatorname{Re}u>0$; hence $\abs{g}<1$. Finally $u(0)=s(f(0))=s(1)=1$, so $g(0)=0$.
:::

:::

::: {.pf-step #derivative}
$g'(0)=\dfrac{f'(0)}{4}$.

::: pf-proof
For $g=(u-1)/(u+1)$ the quotient rule gives $g'=2u'/(u+1)^{2}$, so $g'(0)=2u'(0)/4=u'(0)/2$ because $u(0)=1$. And $u'(0)=s'(f(0))f'(0)=s'(1)f'(0)=\tfrac12f'(0)$, since $s(w)=w^{1/2}$ has $s'(1)=\tfrac12$. Hence $g'(0)=f'(0)/4$.
:::

:::

::: {.pf-step #bound}
$\abs{f'(0)}\le4$ for every $f\in\mathcal F$.

::: pf-proof
$g$ is a self-map of the disc fixing $0$, so Schwarz's lemma gives $\abs{g'(0)}\le1$; by step [](#derivative){.pf-ref} this is $\abs{f'(0)}\le4$.
:::

:::

::: {.pf-step #extremal}
$f_{\theta}(z)=\Bigl(\dfrac{1+e^{i\theta}z}{1-e^{i\theta}z}\Bigr)^{2}$ lies in $\mathcal F$ and has $\abs{f_{\theta}'(0)}=4$.

::: pf-proof
$h(w)=(1+w)/(1-w)$ maps $\DD$ holomorphically onto the right half-plane (it is a Möbius map sending $0\mapsto1$, and $\abs{1+w}>\abs{1-w}$ for $\abs{w}<1$), so $h(e^{i\theta}z)^{2}$ takes values in $\Omega$ and omits the strictly negative reals; also $f_{\theta}(0)=h(0)^{2}=1$. Differentiating, $f_{\theta}'=2h\,h'\,e^{i\theta}$ with $h(0)=1$ and $h'(0)=2$, so $f_{\theta}'(0)=4e^{i\theta}$ and the modulus is $4$.
:::

:::

::: {.pf-step}
$\max_{f\in\mathcal F}\abs{f'(0)}=4$.

::: pf-proof
Steps [](#bound){.pf-ref} and [](#extremal){.pf-ref} give the bound and its attainment:
$$
\boxed{\max_{f\in\mathcal F}\abs{f'(0)}=4,}
$$
the maximum being attained by each $f_{\theta}$.
:::

:::

:::
:::
