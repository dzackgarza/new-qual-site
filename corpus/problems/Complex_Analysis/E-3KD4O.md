---
schema: qual/card@1
id: E-3KD4O
kind: problem
title: Once complex-differentiable functions are holomorphic
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Integral Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source leaves Omega undeclared; the statement declares it an open subset of C.
---

::: {.exercise}
Let $\Omega\subseteq\CC$ be open. Show that if $f$ is once complex differentiable at each point of $\Omega$, then $f$ is holomorphic, in the sense that $f$ is analytic on $\Omega$.
:::

::: {.solution}
For a closed triangle $T\subset\Omega$ write $I(T)=\int_{\partial T}f(z)\,dz$, and let $d$ and $p$ be the diameter and perimeter of $T$.

::: pf

::: {.pf-step #goursat}
$I(T)=0$ for every closed triangle $T\subset\Omega$ (Goursat).

::: pf-proof

::: {.pf-step #nested}
There are nested closed triangles $T=T_0\supset T_1\supset\cdots$ with $\abs{I(T_n)}\ge4^{-n}\abs{I(T)}$, $\operatorname{diam}T_n=2^{-n}d$ and perimeter $2^{-n}p$, whose intersection is one point $z_0\in T$.

::: pf-proof
Subdivide $T_n$ by its midpoints into four congruent triangles. The integrals over interior edges cancel, so $I(T_n)$ is the sum of the four subtriangle integrals, and one of them, $T_{n+1}$, satisfies $\abs{I(T_{n+1})}\ge\frac14\abs{I(T_n)}$.
The intersection is one point because the triangles are compact, nested, and have diameters tending to $0$.
:::

:::

::: pf-step
$I(T)=0$.

::: pf-proof
Differentiability at $z_0$ gives $f(z)=f(z_0)+f'(z_0)(z-z_0)+\eta(z)(z-z_0)$ with $\eta(z)\to0$ as $z\to z_0$.
The first two terms have primitives, so their integrals over $\partial T_n$ vanish.
Given $\varepsilon>0$, for all large $n$ we have $\abs{\eta}\le\varepsilon$ on $T_n$, hence
$$
\abs{I(T_n)}\le\varepsilon\operatorname{diam}(T_n)\cdot 2^{-n}p=4^{-n}\varepsilon dp.
$$
With step [](#nested){.pf-ref} this gives $\abs{I(T)}\le\varepsilon dp$ for every $\varepsilon>0$.
:::

:::

:::

:::

::: {.pf-step #primitive}
On every open disk $D\subseteq\Omega$, $f$ has a primitive.

::: pf-proof
Fix the center $z_*$ of $D$ and set $F(z)=\int_{[z_*,z]}f(w)\,dw$ for $z\in D$.
For $z,z+h\in D$ the triangle with vertices $z_*,z,z+h$ lies in $D$, so step [](#goursat){.pf-ref} gives $F(z+h)-F(z)=\int_{[z,z+h]}f(w)\,dw$.
Since $f$ is continuous (it is complex differentiable), $\frac1h\int_{[z,z+h]}f(w)\,dw\to f(z)$, so $F'=f$ on $D$.
:::

:::

::: pf-step
$f$ is analytic on $\Omega$.

::: pf-proof
On each disk $D\subseteq\Omega$, the primitive $F$ of step [](#primitive){.pf-ref} is complex differentiable on $D$ and hence analytic there by the Cauchy integral formula for $F$, which uses only Cauchy's theorem for $F$; so $f=F'$ is analytic on $D$.
Every point of $\Omega$ lies in such a disk.
:::

:::

:::

:::
