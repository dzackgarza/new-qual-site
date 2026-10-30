---
schema: qual/card@1
id: P-RASP09D
kind: problem
title: 'Principal value of $\frac{x_1+x_2}{\abs{x}^3}$ defines a distribution on $\RR^2$'
classification:
  areas:
  - real-analysis
  topics:
  - Distributions
  - Principal Value
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Spring 2009 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Show that on $\RR^2$ (with coordinates $(x_1, x_2)$),
$$
\left\langle \operatorname{PV}\left(\frac{x_1 + x_2}{\norm{x}^3}\right), \varphi \right\rangle = \lim_{\varepsilon \to 0} \int_{\norm{x} > \varepsilon} \varphi(x) \frac{x_1 + x_2}{\norm{x}^3} \, dm, \quad \varphi \in C_c^\infty(\RR^2),
$$
exists and defines a distribution on $\RR^2$.
:::

::: {.solution}

::: pf

::: pf-step

Use oddness of the kernel to expose cancellation.

::: pf-proof

Set
$$
K(x):=\frac{x_1+x_2}{\norm{x}^3},
\qquad x\ne0.
$$
Then
$$
K(-x)=-K(x).
$$
For $\varepsilon>0$, the domain $\{\norm{x}>\varepsilon\}$ is symmetric under $x\mapsto -x$. Therefore, after the change of variables $x\mapsto -x$,
$$
\begin{aligned}
I_\varepsilon(\varphi)
&:=\int_{\norm{x}>\varepsilon}\varphi(x)K(x)\,dx\\
&=\frac12\int_{\norm{x}>\varepsilon}
\bigl(\varphi(x)-\varphi(-x)\bigr)K(x)\,dx.
\end{aligned}
$$

:::

:::

::: pf-step

Show that the symmetrized integrand is absolutely integrable near the origin.

::: pf-proof

Fix $R>0$ so that $\operatorname{supp}\varphi\subset B(0,R)$. For $\norm{x}\le R$,
$$
\abs{\varphi(x)-\varphi(-x)}
\le 2\norm{x}\sup_{\norm{y}\le R}\norm{\nabla\varphi(y)}.
$$
Also
$$
\abs{K(x)}
\le \frac{\abs{x_1}+\abs{x_2}}{\norm{x}^3}
\le \frac{\sqrt2}{\norm{x}^2}.
$$
Hence
$$
\abs{
\bigl(\varphi(x)-\varphi(-x)\bigr)K(x)
}
\le
\frac{2\sqrt2}{\norm{x}}
\sup_{\norm{y}\le R}\norm{\nabla\varphi(y)}.
$$
The function $\norm{x}^{-1}$ is locally integrable on $\RR^2$, because in polar coordinates
$$
\int_{\norm{x}<R}\frac{dx}{\norm{x}}
=2\pi R<\infty.
$$
Thus the symmetrized integrand is absolutely integrable near $0$; away from $0$ it is integrable because $\varphi$ has compact support.

:::

:::

::: pf-step

Pass to the principal-value limit.

::: pf-proof

By Step 2 and dominated convergence,
$$
\lim_{\varepsilon\downarrow0}I_\varepsilon(\varphi)
=\frac12\int_{\RR^2}
\bigl(\varphi(x)-\varphi(-x)\bigr)K(x)\,dx.
$$
Therefore the principal value exists for every test function $\varphi$.

:::

:::

::: pf-step

Verify continuity on the test-function space.

::: pf-proof

Let $L\subset\RR^2$ be compact, and suppose $\operatorname{supp}\varphi\subset L$. Choose $R$ with
$$
L\cup(-L)\subset B(0,R).
$$
Using the estimate from Step 2,
$$
\begin{aligned}
\abs{\langle \operatorname{PV}(K),\varphi\rangle}
&\le \frac12\int_{B(0,R)}
\frac{2\sqrt2}{\norm{x}}
\sup_{B(0,R)}\norm{\nabla\varphi}\,dx\\
&\le C_R\sup_{B(0,R)}\norm{\nabla\varphi}.
\end{aligned}
$$
Thus the functional is continuous on every fixed compact-support test-function space. It is linear by construction, so
$$
\boxed{
\operatorname{PV}\!\left(\frac{x_1+x_2}{\norm{x}^3}\right)
\in\mathcal D'(\RR^2).}
$$

:::

:::

:::

:::
