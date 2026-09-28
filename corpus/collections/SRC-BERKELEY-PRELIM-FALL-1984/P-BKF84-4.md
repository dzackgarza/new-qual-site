---
schema: qual/card@1
id: P-BKF84-4
kind: problem
title: The integral $\int_0^\infty\frac{x-\sin x}{x^3}\,dx$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the deterministic MinerU Flash extraction of the Berkeley Fall 1984 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked both improper integrations by parts and a Laplace-damping proof of the Dirichlet integral.
---

::: {.problem}
Evaluate
\[
\int_0^\infty \frac{x-\sin x}{x^3}\,dx.
\]
:::

::: {.solution}
<1>1. One has
$$
\int_0^\infty\frac{x-\sin x}{x^3}\,dx
=
\frac12
\int_0^\infty\frac{1-\cos x}{x^2}\,dx.
$$

::: {.proof}
Integrate by parts first on $[\varepsilon,R]$:
$$
\begin{aligned}
\int_\varepsilon^R\frac{x-\sin x}{x^3}\,dx
&=
\left[
-\frac{x-\sin x}{2x^2}
\right]_\varepsilon^R
+
\frac12
\int_\varepsilon^R\frac{1-\cos x}{x^2}\,dx.
\end{aligned}
$$
As $x\to0$,
$$
x-\sin x=O(x^3),
$$
so the boundary term at $\varepsilon$ tends to $0$. As $R\to\infty$,
$$
\frac{R-\sin R}{R^2}\longrightarrow0.
$$
Also
$$
\frac{1-\cos x}{x^2}
$$
is bounded near $0$ and is $O(x^{-2})$ at infinity, so its improper
integral converges. Taking the two limits proves the identity.
:::

<1>2. One has
$$
\int_0^\infty\frac{1-\cos x}{x^2}\,dx
=
\int_0^\infty\frac{\sin x}{x}\,dx.
$$

::: {.proof}
On $[\varepsilon,R]$, another integration by parts gives
$$
\int_\varepsilon^R\frac{1-\cos x}{x^2}\,dx
=
\left[
-\frac{1-\cos x}{x}
\right]_\varepsilon^R
+
\int_\varepsilon^R\frac{\sin x}{x}\,dx.
$$
The boundary term tends to $0$ at both endpoints, since
$$
1-\cos x=O(x^2)
$$
at $0$ and is bounded at infinity. The integral of $\sin x/x$
converges by Dirichlet's test, so passage to the improper limits is
valid.
:::

<1>3. The Dirichlet integral is
$$
\int_0^\infty\frac{\sin x}{x}\,dx
=
\frac\pi2.
$$

::: {.proof}
For $a>0$, define
$$
D(a)
\coloneqq
\int_0^\infty e^{-ax}\frac{\sin x}{x}\,dx.
$$
The integral is absolutely convergent. Differentiation under the
integral sign gives
$$
D'(a)
=
-\int_0^\infty e^{-ax}\sin x\,dx
=
-\frac1{1+a^2}.
$$
Moreover,
$$
\abs{D(a)}
\leq
\int_0^\infty e^{-ax}\,dx
=
\frac1a,
$$
so $D(a)\to0$ as $a\to\infty$. Therefore
$$
D(a)
=
\int_a^\infty\frac{ds}{1+s^2}
=
\frac\pi2-\arctan a.
$$

It remains to pass to $a\downarrow0$. For
$$
g_a(x)=\frac{e^{-ax}}x
$$
and $S>R>0$, integration by parts gives the uniform tail bound
$$
\left|
\int_R^Sg_a(x)\sin x\,dx
\right|
\leq
2g_a(R)
\leq
\frac2R.
$$
The same estimate holds for $a=0$. On every fixed interval $[0,R]$,
dominated convergence gives
$$
e^{-ax}\frac{\sin x}{x}
\longrightarrow
\frac{\sin x}{x}.
$$
Thus
$$
\lim_{a\downarrow0}D(a)
=
\int_0^\infty\frac{\sin x}{x}\,dx.
$$
Taking $a\downarrow0$ in the explicit formula for $D(a)$ yields
$\pi/2$.
:::

<1>4. Hence
$$
\boxed{
\int_0^\infty\frac{x-\sin x}{x^3}\,dx
=
\frac\pi4
}.
$$

::: {.proof}
Combine steps <1>1--<1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested evaluation.
:::
:::
