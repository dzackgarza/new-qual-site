---
schema: qual/card@1
id: P-UCLARA11S-02
kind: problem
title: An oscillatory approximate identity converges almost everywhere to zero
classification: {areas: [real-analysis], topics: []}
relations: []
review: draft
---

::: {.problem}
Let $f\in L^3(\mathbb R)$ and
\[
\phi(x)=
\begin{cases}
\sin(\pi x),& |x|\le1,\\
0,&\text{otherwise}.
\end{cases}
\]
Show that
\[
f_n(x):=n\int_{\mathbb R}f(x-y)\phi(ny)\,dy\longrightarrow0
\]
Lebesgue almost everywhere.
:::

Define
\[
h(x)
\coloneqq
\phi(x)\mathbf 1_{[0,1]}(x),
\qquad
g(x)
\coloneqq
-\phi(x)\mathbf 1_{[-1,0]}(x).
\]
Then $h,g\ge0$ and
\[
\phi=h-g.
\]
For $n\ge1$, set
\[
h_n(x)=nh(nx),
\qquad
g_n(x)=ng(nx).
\]

::: pf

::: pf-step

One has
\[
\int_{\mathbb R}h_n
=
\int_{\mathbb R}g_n
=
\frac2\pi.
\]


::: pf-proof

By the change of variables $u=nx$,
\[
\int h_n=\int h,
\qquad
\int g_n=\int g.
\]
Moreover,
\[
\int_0^1\sin(\pi u)\,du
=
\frac2\pi,
\]
and by oddness of $\sin(\pi u)$,
\[
\int_{-1}^0-\sin(\pi u)\,du
=
\frac2\pi.
\]

:::

:::

::: pf-step

If $x$ is a Lebesgue point of $f$, then
\[
(f*h_n)(x)
\longrightarrow
\frac2\pi f(x).
\]


::: pf-proof

Since $h_n$ is supported in $[0,1/n]$,
\[
\begin{aligned}
\left|
(f*h_n)(x)
-
\frac2\pi f(x)
\right|
&=
\left|
\int_0^{1/n}
[f(x-y)-f(x)]
n\sin(\pi ny)\,dy
\right|\\
&\le
n\int_0^{1/n}
|f(x-y)-f(x)|\,dy.
\end{aligned}
\]
At every Lebesgue point $x$ of $f$, the one-sided differentiation theorem gives
\[
n\int_0^{1/n}
|f(x-y)-f(x)|\,dy
\longrightarrow0.
\]
Hence the claimed limit follows.

:::

:::

::: pf-step

If $x$ is a Lebesgue point of $f$, then
\[
(f*g_n)(x)
\longrightarrow
\frac2\pi f(x).
\]


::: pf-proof

Now $g_n$ is supported in $[-1/n,0]$. Exactly as in step <1>2,
\[
\left|
(f*g_n)(x)
-
\frac2\pi f(x)
\right|
\le
n\int_0^{1/n}
|f(x+y)-f(x)|\,dy,
\]
which tends to $0$ at every Lebesgue point.

:::

:::

::: pf-step

The function $f\in L^1_{\mathrm{loc}}(\mathbb R)$, so almost every point is a Lebesgue point of $f$.


::: pf-proof

Since $f\in L^3(\mathbb R)$, Hölder's inequality gives
\[
\int_E|f|
\le
|E|^{2/3}\|f\|_3
\]
for every bounded measurable set $E$. Thus $f\in L^1_{\mathrm{loc}}$, and the Lebesgue differentiation theorem applies.

:::

:::

::: pf-step

For almost every $x$,
\[
f_n(x)\longrightarrow0.
\]


::: pf-proof

The rescaled kernel in the problem is
\[
n\phi(n\cdot)
=
h_n-g_n.
\]
Therefore
\[
f_n
=
f*h_n-f*g_n.
\]
At every Lebesgue point of $f$, steps <1>2 and <1>3 give
\[
f_n(x)
\longrightarrow
\frac2\pi f(x)-\frac2\pi f(x)
=0.
\]
Step <1>4 says this holds almost everywhere.

:::

:::

::: pf-qed

Step <1>5 is the desired almost-everywhere convergence.

:::

:::
