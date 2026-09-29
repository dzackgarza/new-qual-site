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
Suppose $f:\RR\to\RR$ is a bounded continuous function. Calculate the limit
$$
\lim_{\epsilon\to0^+}\int_{-\infty}^{\infty} f(t)\frac{\epsilon}{\epsilon^2+t^2}\,dt.
$$
:::

::: {.solution}
For $\varepsilon>0$, write
$$
I_\varepsilon
\coloneqq
\int_{-\infty}^{\infty}
f(t)\frac{\varepsilon}{\varepsilon^2+t^2}\,dt.
$$

::: pf

::: {.pf-step #s1}

The substitution
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

::: pf-proof

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

:::

::: {.pf-step #s2}

One has
$$
\int_{-\infty}^{\infty}\frac{du}{1+u^2}=\pi.
$$

::: pf-proof

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

:::

::: {.pf-step #s3}

One has
$$
I_\varepsilon-\pi f(0)
=
\int_{-\infty}^{\infty}
\frac{f(\varepsilon u)-f(0)}{1+u^2}\,du.
$$

::: pf-proof

Combine step [](#s1){.pf-ref} with step [](#s2){.pf-ref}:
$$
\pi f(0)
=
\int_{-\infty}^{\infty}
\frac{f(0)}{1+u^2}\,du,
$$
and subtract the two integrals.

:::

:::

::: {.pf-step #s4}

For every $\eta>0$, there is $A>0$ such that for every
$\varepsilon>0$,
$$
\int_{\abs{u}>A}
\frac{\abs{f(\varepsilon u)-f(0)}}{1+u^2}\,du
<
\frac{\eta}{2}.
$$

::: pf-proof

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

:::

::: {.pf-step #s5}

For the $A$ chosen in step [](#s4){.pf-ref}, all sufficiently small
$\varepsilon>0$ satisfy
$$
\int_{\abs{u}\leq A}
\frac{\abs{f(\varepsilon u)-f(0)}}{1+u^2}\,du
<
\frac{\eta}{2}.
$$

::: pf-proof

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
step [](#s2){.pf-ref},
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

:::

::: {.pf-step #s6}

The required limit is
$$
\boxed{
\lim_{\varepsilon\to0^+}I_\varepsilon
=
\pi f(0)
}.
$$

::: pf-proof

Let $\eta>0$. Steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} show that for all sufficiently small
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

:::

::: pf-qed

Step [](#s6){.pf-ref} gives the requested value.

:::

:::

:::
