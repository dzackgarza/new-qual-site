---
schema: qual/card@1
id: P-GXAKN
kind: problem
title: $x^{1/3}(1+xy)^{-3/2}$ on $0\leq x\leq y$ is in $L^1(\mathbb R^2)$
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Integrals
  - L¹
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the recorded UGA Spring 2015 real-analysis exam source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Define
\[
f(x,y)=
\begin{cases}
\dfrac{x^{1/3}}{(1+xy)^{3/2}},&0\le x\le y,\\[1ex]
0,&\text{otherwise}.
\end{cases}
\]
Carefully show that $f\in L^1(\mathbb R^2)$.
:::

::: solution
<1>1. Use Tonelli and compute the inner integral.
::: proof
The function $f$ is nonnegative and measurable, so Tonelli's theorem gives
\[
\int_{\mathbb R^2}|f|\,d(x,y)
=\int_0^\infty\int_x^\infty
x^{1/3}(1+xy)^{-3/2}\,dy\,dx.
\]
For fixed $x>0$,
\[
\begin{aligned}
\int_x^\infty x^{1/3}(1+xy)^{-3/2}\,dy
&=2x^{-2/3}(1+x^2)^{-1/2}.
\end{aligned}
\]
Hence
\[
\int_{\mathbb R^2}|f|
=2\int_0^\infty\frac{dx}{x^{2/3}\sqrt{1+x^2}}.
\]
:::

<1>2. Check integrability at zero and infinity.
::: proof
For $0<x\le1$,
\[
\frac{2}{x^{2/3}\sqrt{1+x^2}}
\le 2x^{-2/3},
\]
and
\[
\int_0^1x^{-2/3}\,dx<\infty.
\]
For $x\ge1$,
\[
\sqrt{1+x^2}\ge x,
\]
so
\[
\frac{2}{x^{2/3}\sqrt{1+x^2}}
\le 2x^{-5/3},
\]
and
\[
\int_1^\infty x^{-5/3}\,dx<\infty.
\]
Therefore
\[
\boxed{\int_{\mathbb R^2}|f|<\infty,}
\]
so $f\in L^1(\mathbb R^2)$.
:::
:::
