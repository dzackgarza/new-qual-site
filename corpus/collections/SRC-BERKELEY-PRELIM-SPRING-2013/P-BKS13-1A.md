---
schema: qual/card@1
id: P-BKS13-1A
kind: problem
title: Poisson kernel limit $\int f(t)\,\epsilon/(\epsilon^2+t^2)\,dt$ as $\epsilon\to 0^+$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 1 of the retained Spring 2013 solution PDF and independently reviewed the scaling argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the change of variables and an elementary core-tail estimate justifying passage to the limit without an unproved interchange.
---

::: {.problem}
Suppose $f:\mathbb{R}\to\mathbb{R}$ is a bounded continuous function. Calculate the limit
\[
\lim_{\epsilon\to0^+}\int_{-\infty}^{\infty} f(t)\frac{\epsilon}{\epsilon^2+t^2}\,dt.
\]
:::

::: {.solution}
For $\varepsilon>0$, write
$$
I_\varepsilon
\coloneqq
\int_{-\infty}^{\infty}
f(t)\frac{\varepsilon}{\varepsilon^2+t^2}\,dt.
$$

<1>1. The substitution
$$
t=\varepsilon u
$$
gives
$$
I_\varepsilon
=
\int_{-\infty}^{\infty}
\frac{f(\varepsilon u)}{1+u^2}\,du.
$$

::: {.proof}
Since
$$
dt=\varepsilon\,du,
$$
one has
$$
\frac{\varepsilon}{\varepsilon^2+t^2}\,dt
=
\frac{\varepsilon}{\varepsilon^2(1+u^2)}
\varepsilon\,du
=
\frac{du}{1+u^2}.
$$
:::

<1>2. One has
$$
\int_{-\infty}^{\infty}\frac{du}{1+u^2}=\pi.
$$

::: {.proof}
Since
$$
\frac{d}{du}\arctan u
=
\frac1{1+u^2},
$$
the improper integral equals
$$
\lim_{R\to\infty}
\bigl(\arctan R-\arctan(-R)\bigr)
=
\frac\pi2-\left(-\frac\pi2\right)
=
\pi.
$$
:::

<1>3. One has
$$
I_\varepsilon-\pi f(0)
=
\int_{-\infty}^{\infty}
\frac{f(\varepsilon u)-f(0)}{1+u^2}\,du.
$$

::: {.proof}
Combine step <1>1 with step <1>2:
$$
\pi f(0)
=
\int_{-\infty}^{\infty}
\frac{f(0)}{1+u^2}\,du,
$$
and subtract the two integrals.
:::

<1>4. For every $\eta>0$, there is $A>0$ such that for every
$\varepsilon>0$,
$$
\int_{\abs{u}>A}
\frac{\abs{f(\varepsilon u)-f(0)}}{1+u^2}\,du
<
\frac{\eta}{2}.
$$

::: {.proof}
Because $f$ is bounded, choose $M\geq1$ such that
$$
\abs{f(x)}\leq M
$$
for all $x\in\RR$. Then
$$
\abs{f(\varepsilon u)-f(0)}
\leq
2M.
$$
Since
$$
\int_{-\infty}^{\infty}\frac{du}{1+u^2}<\infty,
$$
choose $A$ so large that
$$
\int_{\abs{u}>A}\frac{du}{1+u^2}
<
\frac{\eta}{4M}.
$$
Multiplying by $2M$ gives the required estimate.
:::

<1>5. For the $A$ chosen in step <1>4, all sufficiently small
$\varepsilon>0$ satisfy
$$
\int_{\abs{u}\leq A}
\frac{\abs{f(\varepsilon u)-f(0)}}{1+u^2}\,du
<
\frac{\eta}{2}.
$$

::: {.proof}
By continuity of $f$ at $0$, there is $\delta>0$ such that
$$
\abs{s}<\delta
\quad\Longrightarrow\quad
\abs{f(s)-f(0)}
<
\frac{\eta}{2\pi}.
$$
If
$$
0<\varepsilon<\frac{\delta}{A},
$$
then $\abs{\varepsilon u}<\delta$ for $\abs{u}\leq A$. Therefore, using
step <1>2,
$$
\begin{aligned}
\int_{\abs{u}\leq A}
\frac{\abs{f(\varepsilon u)-f(0)}}{1+u^2}\,du
&<
\frac{\eta}{2\pi}
\int_{\abs{u}\leq A}\frac{du}{1+u^2}\\
&\leq
\frac{\eta}{2}.
\end{aligned}
$$
:::

<1>6. The required limit is
$$
\boxed{
\lim_{\varepsilon\to0^+}I_\varepsilon
=
\pi f(0)
}.
$$

::: {.proof}
Let $\eta>0$. Steps <1>3--<1>5 show that for all sufficiently small
$\varepsilon>0$,
$$
\abs{I_\varepsilon-\pi f(0)}
<
\frac{\eta}{2}
+
\frac{\eta}{2}
=
\eta.
$$
This is exactly the stated limit.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the requested value.
:::
:::
