---
schema: qual/card@1
id: P-BERK80S-16
kind: problem
title: Subsequence convergence for oscillatory functions
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 16 of the vendored Berkeley Preliminary Exam, Summer 1980.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the bounded and unbounded parameter subsequences and locally uniform convergence to a continuous limit in every case.
---

::: {.problem}
Let $(a_n)$ be a sequence of nonzero real numbers.
Prove that the sequence of functions $f_n:\RR\to\RR$

$$
f_n(x)=\frac{1}{a_n}\sin(a_nx)+\cos(x+a_n)
$$

has a subsequence converging to a continuous function.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $(a_n)$ has a bounded subsequence, then $(f_n)$ has a subsequence
converging locally uniformly to a continuous function.

::: pf-proof

By Bolzano--Weierstrass, after passing to a subsequence we may assume
$$
a_n\to a\in\RR.
$$

If $a\ne0$, then for each compact interval $K\subset\RR$,
$$
\frac{\sin(a_nx)}{a_n}\longrightarrow \frac{\sin(ax)}a
$$
uniformly for $x\in K$, because the function
$$
(t,x)\longmapsto \frac{\sin(tx)}t
$$
is uniformly continuous on $[a-\delta,a+\delta]\times K$ for
$0<\delta<\abs{a}$. Also
$$
\abs{\cos(x+a_n)-\cos(x+a)}\le\abs{a_n-a},
$$
so $\cos(x+a_n)\to\cos(x+a)$ uniformly in $x$. Hence
$$
f_n(x)\longrightarrow \frac{\sin(ax)}a+\cos(x+a)
$$
locally uniformly.

If $a=0$, then $\abs{\sin u-u}\le\abs{u}^3/6$ gives
$$
\abs{\frac{\sin(a_nx)}{a_n}-x}\le\frac{a_n^2\abs{x}^3}{6},
$$
so $\sin(a_nx)/a_n\to x$ uniformly on every compact interval. Also
$\cos(x+a_n)\to\cos x$ uniformly. Thus
$$
f_n(x)\longrightarrow x+\cos x
$$
locally uniformly.

In either case the limit is continuous.

:::

:::

::: {.pf-step #s2}

If $(a_n)$ has no bounded subsequence, then $(f_n)$ has a subsequence
converging uniformly on $\RR$ to a continuous function.

::: pf-proof

If $(a_n)$ has no bounded subsequence, then $\abs{a_n}\to\infty$, so
$$
\sup_{x\in\RR}\abs{\frac{\sin(a_nx)}{a_n}}
\le \frac1{\abs{a_n}}\longrightarrow0.
$$

The points $e^{ia_n}$ lie on the compact unit circle, so after passing to
a subsequence,
$$
e^{ia_n}\to e^{i\theta}
$$
for some real $\theta$. Then for every $x$,
$$
\begin{aligned}
\abs{\cos(x+a_n)-\cos(x+\theta)}
&=\abs{\Re\left(e^{ix}(e^{ia_n}-e^{i\theta})\right)}\\
&\le \abs{e^{ia_n}-e^{i\theta}},
\end{aligned}
$$
and the right-hand side is independent of $x$ and tends to $0$. Hence
$\cos(x+a_n)\to\cos(x+\theta)$ uniformly on $\RR$, and
$$
f_n\longrightarrow \cos(x+\theta)
$$
uniformly, with continuous limit.

:::

:::

::: pf-qed

Every real sequence either has a bounded subsequence or has none, so
step [](#s1){.pf-ref} or step [](#s2){.pf-ref} applies.

:::

:::

:::
