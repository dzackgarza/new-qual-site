---
schema: qual/card@1
id: P-BKF85-1
kind: problem
title: Evaluate an integral involving $1-\cos(ax)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 in the deterministic MinerU Flash extraction assets/attachments/Fall85_extracted.md.
---

::: {.problem}
Evaluate
\[
\int_0^\infty \frac{1-\cos(ax)}{x^2}\,dx
\]
for $a\in\mathbb R$.
:::

::: {.solution}
<1>1. For $a\neq0$,
$$
\int_0^\infty \frac{1-\cos(ax)}{x^2}\,dx
=
\abs{a}
\int_0^\infty\frac{1-\cos t}{t^2}\,dt.
$$

::: {.proof}
The integrand depends on $a$ only through $\abs{a}$, since cosine is even. For $a\neq0$, set
$$
t=\abs{a}x.
$$
Then $dx=dt/\abs{a}$ and $x^2=t^2/\abs{a}^2$, which gives the displayed identity.
:::

<1>2. One has
$$
\int_0^\infty\frac{1-\cos t}{t^2}\,dt
=
\int_0^\infty\frac{\sin t}{t}\,dt.
$$

::: {.proof}
For $0<\varepsilon<R$, integration by parts gives
$$
\int_\varepsilon^R\frac{1-\cos t}{t^2}\,dt
=
\left[-\frac{1-\cos t}{t}\right]_{\varepsilon}^{R}
+\int_\varepsilon^R\frac{\sin t}{t}\,dt.
$$
As $\varepsilon\downarrow0$,
$$
\frac{1-\cos\varepsilon}{\varepsilon}\longrightarrow0,
$$
and as $R\to\infty$,
$$
\frac{1-\cos R}{R}\longrightarrow0.
$$
The integral of $\sin t/t$ converges by Dirichlet's test, so passage to the improper limits yields the claim.
:::

<1>3. For every $s>0$,
$$
F(s)\coloneqq\int_0^\infty e^{-st}\frac{\sin t}{t}\,dt
=
\frac\pi2-\arctan s.
$$

::: {.proof}
Fix $s_0>0$. For $s\geq s_0/2$, the derivative of the integrand with respect to $s$ has absolute value at most $e^{-s_0t/2}$, which is integrable on $[0,\infty)$. Thus differentiation under the integral sign is justified at $s_0$. Since $s_0$ was arbitrary,
$$
F'(s)
=
-\int_0^\infty e^{-st}\sin t\,dt
=
-\frac1{1+s^2}.
$$
Also $F(s)\to0$ as $s\to\infty$: after the substitution $u=st$,
$$
F(s)
=
\int_0^\infty e^{-u}\frac{\sin(u/s)}u\,du,
$$
and
$$
\left|\frac{\sin(u/s)}u\right|\leq\frac1s,
$$
so $\abs{F(s)}\leq1/s$.

Therefore
$$
F(s)
=
-\int_s^\infty F'(v)\,dv
=
\int_s^\infty\frac{dv}{1+v^2}
=
\frac\pi2-\arctan s.
$$
:::

<1>4. The Dirichlet integral is
$$
\int_0^\infty\frac{\sin t}{t}\,dt
=
\frac\pi2.
$$

::: {.proof}
Fix $R>0$. On $[0,R]$, dominated convergence gives
$$
\lim_{s\downarrow0}
\int_0^R e^{-st}\frac{\sin t}{t}\,dt
=
\int_0^R\frac{\sin t}{t}\,dt.
$$
For every $s\geq0$, the function
$$
t\longmapsto\frac{e^{-st}}t
$$
is positive and decreasing on $[R,\infty)$. Dirichlet's estimate therefore gives, uniformly in $s\geq0$,
$$
\left|
\int_R^\infty e^{-st}\frac{\sin t}{t}\,dt
\right|
\leq
\frac{2}{R}.
$$
Thus the tails are uniformly negligible as $R\to\infty$, and consequently
$$
\int_0^\infty\frac{\sin t}{t}\,dt
=
\lim_{s\downarrow0}F(s).
$$
Step <1>3 gives
$$
\lim_{s\downarrow0}F(s)=\frac\pi2.
$$
:::

<1>5. For every $a\in\RR$,
$$
\boxed{
\int_0^\infty \frac{1-\cos(ax)}{x^2}\,dx
=
\frac\pi2\abs{a}
}.
$$

::: {.proof}
If $a=0$, the integrand vanishes identically. If $a\neq0$, combine steps <1>1, <1>2, and <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required evaluation.
:::
:::
