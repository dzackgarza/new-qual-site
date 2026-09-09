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
---

::: {.exercise}
Show that if $f$ is once complex differentiable at each point of $\Omega$, then $f$ is holomorphic.
:::

::: solution
It is enough to prove Goursat's theorem: complex differentiability at every point already implies the Cauchy integral theorem, without assuming continuity of $f'$.

<1>1. Let $T\subset\Omega$ be a closed triangle and set
$$
I(T)=\int_{\partial T}f(z)\,dz.
$$
Subdivide $T$ into four congruent triangles. Since the integrals on internal edges cancel, one subtriangle $T_1$ satisfies
$$
|I(T_1)|\ge\frac14|I(T)|.
$$
Iterating gives nested triangles $T_n$ with
$$
|I(T_n)|\ge4^{-n}|I(T)|,
$$
and with diameter and perimeter scaled respectively by $2^{-n}$. Their intersection is a single point $z_0$.

<1>2. Differentiability at $z_0$ gives
$$
f(z)=f(z_0)+f'(z_0)(z-z_0)+\eta(z)(z-z_0),
\qquad \eta(z)\to0.
$$
The first two terms have zero integral around $\partial T_n$. Hence, for every $\varepsilon>0$ and all sufficiently large $n$,
$$
|I(T_n)|
\le \varepsilon\,\operatorname{diam}(T_n)\,\operatorname{length}(\partial T_n)
=4^{-n}C\varepsilon
$$
for a constant $C$ independent of $n$. Combining with the lower bound gives $|I(T)|\le C\varepsilon$. Since $\varepsilon$ is arbitrary, $I(T)=0$.

<1>3. Thus the integral of $f$ around every triangle compactly contained in $\Omega$ vanishes. On a disk $D\Subset\Omega$, fix $z_*$ and define
$$
F(z)=\int_{[z_*,z]}f(w)\,dw.
$$
The triangle integral identity shows that
$$
F(z+h)-F(z)=\int_{[z,z+h]}f(w)\,dw,
$$
so continuity of $f$ (which follows from complex differentiability) gives $F'(z)=f(z)$. Therefore $F$ is holomorphic and hence analytic; consequently $f=F'$ is analytic on $D$. Since every point of $\Omega$ lies in such a disk, $f$ is holomorphic/analytic throughout $\Omega$.
:::
