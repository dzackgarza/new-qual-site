---
schema: qual/card@1
id: P-UCLARA12S-10
kind: problem
title: Meromorphic continuation of the Gamma function
classification:
  areas:
  - complex-analysis
  topics:
  - Analytic Continuation
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Define
$$
\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}\,dt
$$
wherever the integral is absolutely convergent.
Show that this function extends meromorphically to the whole complex plane.
:::

::: {.solution}

For $t>0$, write $t^{z-1}=e^{(z-1)\log t}$ using the real logarithm.

::: pf

::: pf-step

The defining integral converges absolutely for $\operatorname{Re}z>0$.


::: pf-proof

If $\sigma=\operatorname{Re}z>0$, then
$$
\abs{t^{z-1}e^{-t}}
=
t^{\sigma-1}e^{-t}.
$$
The function $t^{\sigma-1}$ is integrable near $0$, and the exponential factor makes $t^{\sigma-1}e^{-t}$ integrable near $\infty$. Hence the integral converges absolutely.

:::

:::

::: {.pf-step #s1-2}

The function
$$
A(z)\coloneqq\int_1^\infty t^{z-1}e^{-t}\,dt
$$
is entire.


::: pf-proof

Let $K\subset\CC$ be compact and put
$$
M\coloneqq\sup_{z\in K}\operatorname{Re}z.
$$
For $t\ge1$ and $z\in K$,
$$
\abs{t^{z-1}e^{-t}}
\le
t^{M-1}e^{-t},
$$
and the right-hand side is integrable on $[1,\infty)$. The same argument, with an additional factor $\abs{\log t}^j$, controls every $z$-derivative of the integrand uniformly on $K$. Differentiation under the integral sign is therefore valid on every compact set, so $A$ is entire.

:::

:::

::: {.pf-step #s1-3}

For $\operatorname{Re}z>0$,
$$
\int_0^1 t^{z-1}e^{-t}\,dt
=
\sum_{n=0}^\infty
\frac{(-1)^n}{n!(z+n)}.
$$


::: pf-proof

On $[0,1]$,
$$
e^{-t}
=
\sum_{n=0}^\infty\frac{(-1)^n t^n}{n!}
$$
uniformly. If $\operatorname{Re}z>0$, termwise integration is justified by uniform convergence together with integrability of $t^{\operatorname{Re}z-1}$, and gives
$$
\begin{aligned}
\int_0^1 t^{z-1}e^{-t}\,dt
&=
\sum_{n=0}^\infty
\frac{(-1)^n}{n!}
\int_0^1 t^{z+n-1}\,dt\\
&=
\sum_{n=0}^\infty
\frac{(-1)^n}{n!(z+n)}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

The series
$$
B(z)\coloneqq
\sum_{n=0}^\infty
\frac{(-1)^n}{n!(z+n)}
$$
defines a meromorphic function on $\CC$ with possible poles only at $0,-1,-2,\ldots$.


::: pf-proof

Let $K\subset\CC\setminus\{0,-1,-2,\ldots\}$ be compact. For all sufficiently large $n$ and all $z\in K$,
$$
\abs{z+n}\ge\frac n2.
$$
Hence
$$
\abs{\frac{(-1)^n}{n!(z+n)}}
\le
\frac{2}{n!n},
$$
and the majorant series converges. Thus the defining series for $B$ converges locally uniformly away from the nonpositive integers and is holomorphic there.

Near $z=-m$, isolate the $n=m$ term:
$$
B(z)
=
\frac{(-1)^m}{m!(z+m)}
+
\sum_{n\ne m}
\frac{(-1)^n}{n!(z+n)}.
$$
The second summand is holomorphic near $-m$, so $B$ has at worst a simple pole there.

:::

:::

::: {.pf-step #s1-5}

The function
$$
\widetilde\Gamma(z)\coloneqq A(z)+B(z)
$$
is a meromorphic continuation of $\Gamma$ to all of $\CC$.


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref}, $A+B$ is meromorphic on $\CC$. For $\operatorname{Re}z>0$, step [](#s1-3){.pf-ref} gives
$$
\begin{aligned}
\widetilde\Gamma(z)
&=
\int_1^\infty t^{z-1}e^{-t}\,dt
+
\int_0^1 t^{z-1}e^{-t}\,dt\\
&=
\Gamma(z).
\end{aligned}
$$
Thus $\widetilde\Gamma$ agrees with the original Gamma function on its half-plane of definition and extends it meromorphically to the whole plane.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the required meromorphic continuation.

:::

:::

:::
