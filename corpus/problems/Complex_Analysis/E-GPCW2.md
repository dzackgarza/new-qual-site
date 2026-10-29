---
schema: qual/card@1
id: E-GPCW2
kind: problem
title: $\int_{-1}^1 ((x-a)\sqrt{1-x^2})^{-1}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
For $a\in\RR$ with $\abs{a}>1$, evaluate
$$
I(a)\coloneqq \int_{-1}^1 {dx\over (x-a)\sqrt{1-x^2}}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #theta}
$I(a)=\int_0^\pi {d\theta\over \cos\theta-a}$.

::: pf-proof
Put $x=\cos\theta$ with $\theta\in(0,\pi)$; then $dx=-\sin\theta\,d\theta$ and $\sqrt{1-x^2}=\sin\theta$, and the limits $x=-1,1$ become $\theta=\pi,0$.
:::

:::

::: {.pf-step #t}
$I(a)=2\int_0^\infty {dt\over (1-a)-(1+a)t^2}$.

::: pf-proof
Substitute $t=\tan(\theta/2)$ in step [](#theta){.pf-ref}, so that $\cos\theta={1-t^2\over1+t^2}$, $d\theta={2\,dt\over1+t^2}$, and $\cos\theta-a={(1-a)-(1+a)t^2\over1+t^2}$.
:::

:::

::: pf-step
$I(a)=\boxed{-\operatorname{sgn}(a){\pi\over\sqrt{a^2-1}}}$.

::: pf-proof
For $p,q>0$, $\int_0^\infty{dt\over p+qt^2}={\pi\over2\sqrt{pq}}$.
If $a>1$, step [](#t){.pf-ref} gives $I(a)=-2\int_0^\infty{dt\over(a-1)+(a+1)t^2}=-{\pi\over\sqrt{a^2-1}}$.
If $a<-1$, both $1-a$ and $-(1+a)$ are positive, and the same formula gives $I(a)={\pi\over\sqrt{a^2-1}}$.
:::

:::

:::

:::
