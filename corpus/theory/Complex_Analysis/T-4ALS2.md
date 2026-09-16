---
schema: qual/card@1
id: T-4ALS2
kind: theorem
title: Montel's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Montel
  - Normal Families
  - Equicontinuity
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open and let $\mcf$ be a family of [[D-E7A5W|holomorphic]] functions on $\Omega$ that is [[D-MBDTR|uniformly bounded on compact subsets]] of $\Omega$. Then

- $\mcf$ is equicontinuous on every compact subset of $\Omega$, and

- $\mcf$ is a [[D-QTJ7T|normal family]].
:::

::: {.proof}
Let $K\subseteq\Omega$ be compact and choose $r>0$ with $3r<\operatorname{dist}(K,\CC\sm\Omega)$ (any $r>0$ if $\Omega=\CC$).
The set $K'\coloneqq\ts{z\st\operatorname{dist}(z,K)\le2r}$ is a compact subset of $\Omega$, so there is $M$ with $\abs f\le M$ on $K'$ for all $f\in\mcf$.
For $z,w\in K$ with $\abs{z-w}<r$, the circle $C=\ts{\abs{\zeta-w}=2r}$ lies in $K'$, and the Cauchy integral formula gives
$$
\abs{f(z)-f(w)}=\abs{\frac{1}{2\pi i}\int_Cf(\zeta)\Big(\frac{1}{\zeta-z}-\frac{1}{\zeta-w}\Big)d\zeta}\le\frac{1}{2\pi}\cdot2\pi(2r)\cdot M\cdot\frac{\abs{z-w}}{r\cdot2r}=\frac{M}{r}\abs{z-w},
$$
which is independent of $f$; this is equicontinuity on $K$.
Normality follows from the Arzelà--Ascoli theorem applied on an exhaustion of $\Omega$ by compact sets, with a diagonal argument.
:::

::: {.remark}
Montel's second theorem uses the extended convention for normality in the remark on [[D-QTJ7T]], where a subsequence may instead tend to $\infty$ uniformly on compact subsets: a family of meromorphic functions on a region $\Omega$ that omits the same three values of the Riemann sphere is normal in that sense.
:::
