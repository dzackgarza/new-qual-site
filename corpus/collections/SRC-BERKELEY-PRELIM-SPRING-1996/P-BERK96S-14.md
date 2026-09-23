---
schema: qual/card@1
id: P-BERK96S-14
kind: problem
title: An exponential integral of a continuous function is entire in $z$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified compact-uniform convergence of the exponential series,
    termwise integration, and infinite radius of convergence of the resulting
    power series.
---

::: {.problem}
Let $f:[0,1]\to\mathbb C$ be continuous. Show that
\[
g(z)=\int_0^1 f(t)e^{tz^2}\,dt
\]
defines an entire function $g$ on $\mathbb C$.
:::

::: {.solution}
Since $f$ is continuous on $[0,1]$, set
$$
M\coloneqq\max_{0\leq t\leq1}\abs{f(t)}.
$$

<1>1. For every $R>0$, the series
$$
e^{tz^2}
=
\sum_{n=0}^\infty\frac{t^n z^{2n}}{n!}
$$
converges uniformly for
$$
0\leq t\leq1,
\qquad
\abs{z}\leq R.
$$

::: {.proof}
For such $t$ and $z$,
$$
\abs{\frac{t^n z^{2n}}{n!}}
\leq
\frac{R^{2n}}{n!}.
$$
Since
$$
\sum_{n=0}^\infty\frac{R^{2n}}{n!}
=
e^{R^2},
$$
the Weierstrass $M$-test gives uniform convergence.
:::

<1>2. For every $z\in\CC$,
$$
g(z)
=
\sum_{n=0}^\infty c_n z^{2n},
\qquad
c_n\coloneqq\frac1{n!}\int_0^1 f(t)t^n\,dt.
$$

::: {.proof}
Fix $R>\abs{z}$. By step <1>1, the exponential series converges uniformly
in $t\in[0,1]$ for this $z$. Multiplication by the bounded function $f$
preserves uniform convergence, so termwise integration gives
$$
\begin{aligned}
g(z)
&=
\int_0^1
f(t)
\sum_{n=0}^\infty\frac{t^n z^{2n}}{n!}
\,dt\\
&=
\sum_{n=0}^\infty
\left(
\frac1{n!}\int_0^1f(t)t^n\,dt
\right)z^{2n}.
\end{aligned}
$$
:::

<1>3. The power series in step <1>2 has infinite radius of convergence.

::: {.proof}
For every $n\geq0$,
$$
\abs{c_n}
\leq
\frac{M}{n!}\int_0^1t^n\,dt
=
\frac{M}{(n+1)n!}
\leq
\frac{M}{n!}.
$$
Therefore, for every $z\in\CC$,
$$
\sum_{n=0}^\infty
\abs{c_n z^{2n}}
\leq
M\sum_{n=0}^\infty\frac{\abs{z}^{2n}}{n!}
=
Me^{\abs{z}^2}<\infty.
$$
Hence the series converges everywhere in $\CC$ and defines an entire
function.
:::

<1>4. The function $g$ is entire on $\CC$.

::: {.proof}
Step <1>2 identifies $g$ at every complex number with the everywhere
convergent power series from step <1>3. Thus $g$ is entire.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
