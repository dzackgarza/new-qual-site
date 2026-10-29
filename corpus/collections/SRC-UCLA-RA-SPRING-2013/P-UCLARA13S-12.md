---
schema: qual/card@1
id: P-UCLARA13S-12
kind: problem
title: Cauchy-transform representation of a self-map of the upper half-plane
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Let $\halfplane$ be the upper half-plane and let $f:\halfplane\to\halfplane$ be holomorphic.
Assume
\[
\lim_{y\to\infty} y f(iy)=i,
\qquad
|f(z)|\le \frac{1}{\operatorname{Im}z}
\quad(z\in\halfplane).
\]
For $\varepsilon>0$, define
\[
g_\varepsilon(x)=\frac1\pi\operatorname{Im}f(x+i\varepsilon).
\]

(a) Show that
\[
f(z+i\varepsilon)=\int_{\RR}\frac{g_\varepsilon(x)}{x-z}\,dx.
\]

(b) Show that there exists a Borel probability measure $\mu$ on $\RR$ such that
\[
f(z)=\int_{\RR}\frac{d\mu(x)}{x-z}.
\]
:::

::: {.solution}

Fix $\varepsilon>0$ and define
\[
u_\varepsilon(z)
\coloneqq
\operatorname{Im}f(z+i\varepsilon)
\qquad
(z\in\halfplane).
\]

::: pf

::: {.pf-step #s1-1}

The function $u_\varepsilon$ is a positive bounded harmonic function on $\halfplane$, extends continuously to $\RR$, and
\[
u_\varepsilon(x)
=
\pi g_\varepsilon(x)
\qquad
(x\in\RR).
\]


::: pf-proof

Because $f$ is holomorphic and maps $\halfplane$ into itself, its imaginary part is positive harmonic. Translation by $i\varepsilon$ preserves harmonicity, so $u_\varepsilon$ is positive harmonic.

The hypothesis
\[
|f(w)|
\le
\frac1{\operatorname{Im}w}
\]
gives
\[
0<
u_\varepsilon(z)
\le
|f(z+i\varepsilon)|
\le
\frac1{\operatorname{Im}z+\varepsilon}
\le
\frac1\varepsilon.
\]
Since $f$ is holomorphic on the larger half-plane $\operatorname{Im}w>0$, the translated function $z\mapsto f(z+i\varepsilon)$ is holomorphic on $\operatorname{Im}z>-\varepsilon$ and hence continuous across the real axis. The boundary identity is the definition of $g_\varepsilon$.

:::

:::

::: {.pf-step #s1-2}

For $z=x+iy\in\halfplane$,
\[
u_\varepsilon(x+iy)
=
\int_{\RR}
g_\varepsilon(t)
\frac{y}{(t-x)^2+y^2}\,dt.
\]


::: pf-proof

Apply the Poisson representation theorem for bounded harmonic functions on the upper half-plane, continuous on its boundary:
\[
u_\varepsilon(x+iy)
=
\frac1\pi
\int_{\RR}
u_\varepsilon(t)
\frac{y}{(t-x)^2+y^2}\,dt.
\]
Using
\[
u_\varepsilon(t)=\pi g_\varepsilon(t)
\]
from step [](#s1-1){.pf-ref} gives the stated formula.

:::

:::

::: {.pf-step #s1-3}

For every $\varepsilon>0$,
\[
g_\varepsilon\ge0
\qquad\text{and}\qquad
\boxed{
\int_{\RR}g_\varepsilon(t)\,dt=1
}.
\]


::: pf-proof

Positivity follows from $f(\halfplane)\subset\halfplane$.

Set $x=0$ in step [](#s1-2){.pf-ref} and multiply by $y$:
\[
y\operatorname{Im}f(i(y+\varepsilon))
=
\int_{\RR}
g_\varepsilon(t)
\frac{y^2}{t^2+y^2}\,dt.
\]
As $y\to\infty$, the factors
\[
\frac{y^2}{t^2+y^2}
\]
increase pointwise to $1$. Thus the monotone convergence theorem gives
\[
\lim_{y\to\infty}
y\operatorname{Im}f(i(y+\varepsilon))
=
\int_{\RR}g_\varepsilon(t)\,dt.
\]

Writing $Y=y+\varepsilon$, the normalization
\[
Yf(iY)\longrightarrow i
\]
gives
\[
Y\operatorname{Im}f(iY)\longrightarrow1.
\]
Since $y/Y\to1$, the left-hand side above tends to $1$. Hence the integral of $g_\varepsilon$ is $1$.

:::

:::

::: pf-step

For $z\in\halfplane$, define
\[
F_\varepsilon(z)
\coloneqq
\int_{\RR}
\frac{g_\varepsilon(t)}{t-z}\,dt.
\]
Then $F_\varepsilon$ is holomorphic on $\halfplane$.


::: pf-proof

By step [](#s1-3){.pf-ref}, $g_\varepsilon\in L^1(\RR)$. If $z=x+iy\in\halfplane$, then
\[
|t-z|\ge y,
\]
so
\[
\int_{\RR}
\left|
\frac{g_\varepsilon(t)}{t-z}
\right|dt
\le
\frac1y
\int_{\RR}g_\varepsilon(t)\,dt
=
\frac1y.
\]
On compact subsets of $\halfplane$, the same positive lower bound for $\operatorname{Im}z$ permits differentiation under the integral sign, proving holomorphy.

:::

:::

::: {.pf-step #s1-5}

For every $z\in\halfplane$,
\[
\operatorname{Im}F_\varepsilon(z)
=
\operatorname{Im}f(z+i\varepsilon).
\]


::: pf-proof

For $z=x+iy$,
\[
\operatorname{Im}\frac1{t-z}
=
\frac{y}{(t-x)^2+y^2}.
\]
Thus
\[
\operatorname{Im}F_\varepsilon(x+iy)
=
\int_{\RR}
g_\varepsilon(t)
\frac{y}{(t-x)^2+y^2}\,dt.
\]
Step [](#s1-2){.pf-ref} identifies the right-hand side with
\[
u_\varepsilon(x+iy)
=
\operatorname{Im}f(x+i(y+\varepsilon)).
\]

:::

:::

::: {.pf-step #s1-6}

The holomorphic function
\[
D_\varepsilon(z)
\coloneqq
f(z+i\varepsilon)-F_\varepsilon(z)
\]
is a real constant on $\halfplane$.


::: pf-proof

By step [](#s1-5){.pf-ref},
\[
\operatorname{Im}D_\varepsilon(z)=0
\]
throughout the connected domain $\halfplane$. A holomorphic function with image contained in $\RR$ is constant, by the open mapping theorem.

:::

:::

::: {.pf-step #s1-7}

In fact,
\[
D_\varepsilon\equiv0.
\]


::: pf-proof

Evaluate on the imaginary axis. The normalization implies
\[
f(i(y+\varepsilon))\longrightarrow0
\qquad
(y\to\infty).
\]
By step [](#s1-3){.pf-ref},
\[
|F_\varepsilon(iy)|
\le
\int_{\RR}
\frac{g_\varepsilon(t)}{|t-iy|}\,dt
\le
\frac1y
\int_{\RR}g_\varepsilon(t)\,dt
=
\frac1y
\longrightarrow0.
\]
Hence
\[
D_\varepsilon(iy)\to0.
\]
Since $D_\varepsilon$ is constant by step [](#s1-6){.pf-ref}, that constant is $0$.

:::

:::

::: {.pf-step #s1-8}

For every $\varepsilon>0$ and $z\in\halfplane$,
\[
\boxed{
f(z+i\varepsilon)
=
\int_{\RR}
\frac{g_\varepsilon(t)}{t-z}\,dt
}.
\]


::: pf-proof

This is the identity $D_\varepsilon\equiv0$ from step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Let
\[
\varepsilon_n\downarrow0
\]
and define probability measures
\[
d\mu_n(t)
\coloneqq
g_{\varepsilon_n}(t)\,dt.
\]
After passing to a subsequence, there is a finite positive Borel measure $\mu$ on $\RR$ such that
\[
\int_{\RR}\phi\,d\mu_n
\longrightarrow
\int_{\RR}\phi\,d\mu
\qquad
(\phi\in C_0(\RR)).
\]


::: pf-proof

By step [](#s1-3){.pf-ref}, every $\mu_n$ is a positive measure of total mass $1$. Via the Riesz representation theorem, these measures lie in the closed unit ball of
\[
C_0(\RR)^*.
\]
Banach--Alaoglu makes that ball weak-* compact. Since $C_0(\RR)$ is separable, the weak-* topology on the ball is metrizable and sequentially compact. Hence a subsequence converges weak-* to a positive bounded functional, which the Riesz representation theorem identifies with a finite positive Borel measure $\mu$.

:::

:::

::: {.pf-step #s1-10}

For every $z\in\halfplane$,
\[
f(z)
=
\int_{\RR}
\frac{d\mu(t)}{t-z}.
\]


::: pf-proof

For fixed $z\in\halfplane$, the function
\[
t\longmapsto\frac1{t-z}
\]
is continuous on $\RR$ and tends to $0$ as $|t|\to\infty$, so it belongs to $C_0(\RR)$. Step [](#s1-9){.pf-ref} therefore gives
\[
\int_{\RR}
\frac{d\mu_n(t)}{t-z}
\longrightarrow
\int_{\RR}
\frac{d\mu(t)}{t-z}.
\]
By step [](#s1-8){.pf-ref}, the left-hand side is
\[
f(z+i\varepsilon_n),
\]
which tends to $f(z)$ by continuity of $f$.

:::

:::

::: {.pf-step #s1-11}

The measure $\mu$ has total mass
\[
\boxed{\mu(\RR)=1}.
\]


::: pf-proof

Set $z=iy$ in step [](#s1-10){.pf-ref} and multiply by $y$:
\[
yf(iy)
=
\int_{\RR}
\frac{y}{t-iy}\,d\mu(t).
\]
For each fixed $t$,
\[
\frac{y}{t-iy}
\longrightarrow
i
\qquad
(y\to\infty),
\]
and
\[
\left|
\frac{y}{t-iy}
\right|
\le1.
\]
Since $\mu$ is finite, dominated convergence gives
\[
\lim_{y\to\infty}yf(iy)
=
i\mu(\RR).
\]
The given normalization makes the same limit equal to $i$. Therefore
\[
\mu(\RR)=1.
\]

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} proves part (a). Steps [](#s1-9){.pf-ref} through [](#s1-11){.pf-ref} produce a Borel probability measure $\mu$ and prove the representation required in part (b).

:::

:::

:::
