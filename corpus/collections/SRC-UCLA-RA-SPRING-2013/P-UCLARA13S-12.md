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
Let $\mathbb H$ be the upper half-plane and let $f:\mathbb H\to\mathbb H$ be holomorphic.
Assume
\[
\lim_{y\to\infty} y f(iy)=i,
\qquad
|f(z)|\le \frac{1}{\operatorname{Im}z}
\quad(z\in\mathbb H).
\]
For $\varepsilon>0$, define
\[
g_\varepsilon(x)=\frac1\pi\operatorname{Im}f(x+i\varepsilon).
\]

(a) Show that
\[
f(z+i\varepsilon)=\int_{\mathbb R}\frac{g_\varepsilon(x)}{x-z}\,dx.
\]

(b) Show that there exists a Borel probability measure $\mu$ on $\mathbb R$ such that
\[
f(z)=\int_{\mathbb R}\frac{d\mu(x)}{x-z}.
\]
:::

::: {.solution}
Fix $\varepsilon>0$ and define
\[
u_\varepsilon(z)
\coloneqq
\operatorname{Im}f(z+i\varepsilon)
\qquad
(z\in\mathbb H).
\]

<1>1. The function $u_\varepsilon$ is a positive bounded harmonic function on $\mathbb H$, extends continuously to $\mathbb R$, and
\[
u_\varepsilon(x)
=
\pi g_\varepsilon(x)
\qquad
(x\in\mathbb R).
\]

::: {.proof}
Because $f$ is holomorphic and maps $\mathbb H$ into itself, its imaginary part is positive harmonic. Translation by $i\varepsilon$ preserves harmonicity, so $u_\varepsilon$ is positive harmonic.

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

<1>2. For $z=x+iy\in\mathbb H$,
\[
u_\varepsilon(x+iy)
=
\int_{\mathbb R}
g_\varepsilon(t)
\frac{y}{(t-x)^2+y^2}\,dt.
\]

::: {.proof}
Apply the Poisson representation theorem for bounded harmonic functions on the upper half-plane, continuous on its boundary:
\[
u_\varepsilon(x+iy)
=
\frac1\pi
\int_{\mathbb R}
u_\varepsilon(t)
\frac{y}{(t-x)^2+y^2}\,dt.
\]
Using
\[
u_\varepsilon(t)=\pi g_\varepsilon(t)
\]
from step <1>1 gives the stated formula.
:::

<1>3. For every $\varepsilon>0$,
\[
g_\varepsilon\ge0
\qquad\text{and}\qquad
\boxed{
\int_{\mathbb R}g_\varepsilon(t)\,dt=1
}.
\]

::: {.proof}
Positivity follows from $f(\mathbb H)\subset\mathbb H$.

Set $x=0$ in step <1>2 and multiply by $y$:
\[
y\operatorname{Im}f(i(y+\varepsilon))
=
\int_{\mathbb R}
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
\int_{\mathbb R}g_\varepsilon(t)\,dt.
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

<1>4. For $z\in\mathbb H$, define
\[
F_\varepsilon(z)
\coloneqq
\int_{\mathbb R}
\frac{g_\varepsilon(t)}{t-z}\,dt.
\]
Then $F_\varepsilon$ is holomorphic on $\mathbb H$.

::: {.proof}
By step <1>3, $g_\varepsilon\in L^1(\mathbb R)$. If $z=x+iy\in\mathbb H$, then
\[
|t-z|\ge y,
\]
so
\[
\int_{\mathbb R}
\left|
\frac{g_\varepsilon(t)}{t-z}
\right|dt
\le
\frac1y
\int_{\mathbb R}g_\varepsilon(t)\,dt
=
\frac1y.
\]
On compact subsets of $\mathbb H$, the same positive lower bound for $\operatorname{Im}z$ permits differentiation under the integral sign, proving holomorphy.
:::

<1>5. For every $z\in\mathbb H$,
\[
\operatorname{Im}F_\varepsilon(z)
=
\operatorname{Im}f(z+i\varepsilon).
\]

::: {.proof}
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
\int_{\mathbb R}
g_\varepsilon(t)
\frac{y}{(t-x)^2+y^2}\,dt.
\]
Step <1>2 identifies the right-hand side with
\[
u_\varepsilon(x+iy)
=
\operatorname{Im}f(x+i(y+\varepsilon)).
\]
:::

<1>6. The holomorphic function
\[
D_\varepsilon(z)
\coloneqq
f(z+i\varepsilon)-F_\varepsilon(z)
\]
is a real constant on $\mathbb H$.

::: {.proof}
By step <1>5,
\[
\operatorname{Im}D_\varepsilon(z)=0
\]
throughout the connected domain $\mathbb H$. A holomorphic function with image contained in $\mathbb R$ is constant, by the open mapping theorem.
:::

<1>7. In fact,
\[
D_\varepsilon\equiv0.
\]

::: {.proof}
Evaluate on the imaginary axis. The normalization implies
\[
f(i(y+\varepsilon))\longrightarrow0
\qquad
(y\to\infty).
\]
By step <1>3,
\[
|F_\varepsilon(iy)|
\le
\int_{\mathbb R}
\frac{g_\varepsilon(t)}{|t-iy|}\,dt
\le
\frac1y
\int_{\mathbb R}g_\varepsilon(t)\,dt
=
\frac1y
\longrightarrow0.
\]
Hence
\[
D_\varepsilon(iy)\to0.
\]
Since $D_\varepsilon$ is constant by step <1>6, that constant is $0$.
:::

<1>8. For every $\varepsilon>0$ and $z\in\mathbb H$,
\[
\boxed{
f(z+i\varepsilon)
=
\int_{\mathbb R}
\frac{g_\varepsilon(t)}{t-z}\,dt
}.
\]

::: {.proof}
This is the identity $D_\varepsilon\equiv0$ from step <1>7.
:::

<1>9. Let
\[
\varepsilon_n\downarrow0
\]
and define probability measures
\[
d\mu_n(t)
\coloneqq
g_{\varepsilon_n}(t)\,dt.
\]
After passing to a subsequence, there is a finite positive Borel measure $\mu$ on $\mathbb R$ such that
\[
\int_{\mathbb R}\phi\,d\mu_n
\longrightarrow
\int_{\mathbb R}\phi\,d\mu
\qquad
(\phi\in C_0(\mathbb R)).
\]

::: {.proof}
By step <1>3, every $\mu_n$ is a positive measure of total mass $1$. Via the Riesz representation theorem, these measures lie in the closed unit ball of
\[
C_0(\mathbb R)^*.
\]
Banach--Alaoglu makes that ball weak-* compact. Since $C_0(\mathbb R)$ is separable, the weak-* topology on the ball is metrizable and sequentially compact. Hence a subsequence converges weak-* to a positive bounded functional, which the Riesz representation theorem identifies with a finite positive Borel measure $\mu$.
:::

<1>10. For every $z\in\mathbb H$,
\[
f(z)
=
\int_{\mathbb R}
\frac{d\mu(t)}{t-z}.
\]

::: {.proof}
For fixed $z\in\mathbb H$, the function
\[
t\longmapsto\frac1{t-z}
\]
is continuous on $\mathbb R$ and tends to $0$ as $|t|\to\infty$, so it belongs to $C_0(\mathbb R)$. Step <1>9 therefore gives
\[
\int_{\mathbb R}
\frac{d\mu_n(t)}{t-z}
\longrightarrow
\int_{\mathbb R}
\frac{d\mu(t)}{t-z}.
\]
By step <1>8, the left-hand side is
\[
f(z+i\varepsilon_n),
\]
which tends to $f(z)$ by continuity of $f$.
:::

<1>11. The measure $\mu$ has total mass
\[
\boxed{\mu(\mathbb R)=1}.
\]

::: {.proof}
Set $z=iy$ in step <1>10 and multiply by $y$:
\[
yf(iy)
=
\int_{\mathbb R}
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
i\mu(\mathbb R).
\]
The given normalization makes the same limit equal to $i$. Therefore
\[
\mu(\mathbb R)=1.
\]
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>8 proves part (a). Steps <1>9--<1>11 produce a Borel probability measure $\mu$ and prove the representation required in part (b).
:::
:::
