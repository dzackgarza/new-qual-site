---
schema: qual/card@1
id: PR-3LBLV
kind: proposition
title: Centered vertical half-strip to upper half-plane by $\sin$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Trigonometry
relations: []
review: draft
---

::: {.proposition}
Let $S\coloneqq\theset{z\in\CC : -\pi/2<\Re z<\pi/2,\ \Im z>0}$.
Then $\sin$ restricts to a [[D-TM4TE|biholomorphism]] $S\to\HH$, and its inverse $\arcsin\colon\HH\to S$ is a biholomorphism from the upper half-plane onto the vertical half-strip.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-12-31_23-01-11.png)
:::

::: {.proof}
Let $J(u)\coloneqq\frac12\qty{u+u\inv}$ for $u\neq0$.
For every $z\in\CC$,
$$
\sin(z)=\frac{e^{iz}-e^{-iz}}{2i}=-\frac12\qty{ie^{iz}+\frac{1}{ie^{iz}}}=-J\qty{ie^{iz}},
$$
so $\sin$ on $S$ is the composite of the following holomorphic maps, each of which is a bijection onto the stated set.

- $z\mapsto iz$ maps $S$ onto $\theset{\zeta : \Re\zeta<0,\ \abs{\Im\zeta}<\pi/2}$.

- $\zeta\mapsto e^\zeta$ maps that half-strip onto $\theset{w : \abs{w}<1,\ \Re w>0}$: for $\zeta=s+it$ with $s<0$ and $\abs{t}<\pi/2$, $e^\zeta$ has modulus $e^s\in(0,1)$ and argument $t\in(-\pi/2,\pi/2)$, and each such modulus and argument occur exactly once.

- $w\mapsto iw$ maps that half-disc onto the upper half-disc $\theset{u : \abs{u}<1,\ \Im u>0}$.

- $J$ maps the upper half-disc onto the lower half-plane.
For $u=re^{i\theta}$ with $0<r<1$ and $0<\theta<\pi$, $\Im J(u)=\frac12\qty{r-r\inv}\sin\theta<0$.
For $c$ in the lower half-plane, the solutions of $J(u)=c$ are the roots of $u^2-2cu+1=0$, whose product is $1$; neither root lies on the unit circle, where $J$ is real, so exactly one root $u$ satisfies $\abs{u}<1$, and $\Im J(u)<0$ forces $\sin\theta>0$, so that root lies in the upper half-disc.

- $v\mapsto-v$ maps the lower half-plane onto $\HH$.

A bijective holomorphic map has a holomorphic inverse, so $\sin\colon S\to\HH$ is a biholomorphism.
:::

::: {.remark}
The boundary of $S$ maps onto $\RR$: the segment $[-\pi/2,\pi/2]$ maps onto $[-1,1]$, the ray $\pi/2+it$ ($t\ge0$) maps to $\sin(\pi/2+it)=\cosh t$, tracing $[1,\infty)$, and the ray $-\pi/2+it$ maps to $-\cosh t$, tracing $(-\infty,-1]$.
The imaginary axis $it$ ($t>0$) maps to $\sin(it)=i\sinh t$, the positive imaginary axis.
:::
