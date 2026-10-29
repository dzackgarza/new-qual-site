---
schema: qual/card@1
id: P-UCLAB07F-09
kind: problem
title: Limits and continuous dependence for a bounded scalar ODE
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Fall 2007 PDF.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Part (b) of the source asks for uniform convergence of u_n to u, which fails on all of R (F(y,x)=tanh y, u_n(0)=1/n). Part (b) now asks for uniform convergence on every compact interval.
---

::: {.problem}
Suppose $u_n:\RR\to\RR$ is differentiable and satisfies \[u_n'(x)=F(u_n(x),x),\] where $F$ is continuous and bounded.

(a) If $u_n\to u$ uniformly, show that $u$ is differentiable and satisfies $u'(x)=F(u(x),x)$.

(b) Suppose the initial-value problem \[u'(x)=F(u(x),x),\qquad u(x_0)=y_0\] has a unique solution $u:\RR\to\RR$, and $u_n(x_0)\to y_0$.
Show that $u_n$ converges to $u$ uniformly on every compact interval.
:::

::: {.solution}
Let $M=\sup\abs{F}$.

::: pf

::: {.pf-step #s1}
If $u_n\to v$ uniformly on every compact interval, then $v$ is differentiable and $v'(x)=F(v(x),x)$. In particular part (a) holds.

::: pf-proof
Fix $x\in\RR$ and let $J$ be the compact interval between $x_0$ and $x$.
For each $n$,
\[
u_n(x)-u_n(x_0)=\int_{x_0}^x F(u_n(t),t)\,dt.
\]
The values $u_n(t)$, $t\in J$, lie in a fixed compact set for large $n$, on which $F$ is uniformly continuous, so $F(u_n(t),t)\to F(v(t),t)$ uniformly on $J$.
Passing to the limit,
\[
v(x)-v(x_0)=\int_{x_0}^x F(v(t),t)\,dt.
\]
The integrand is continuous, so by the fundamental theorem of calculus $v$ is differentiable with $v'(x)=F(v(x),x)$.
:::

:::

::: {.pf-step #s2}
Every subsequence of $(u_n)$ has a further subsequence that converges uniformly on every compact interval.

::: pf-proof
By the mean value theorem $\abs{u_n(x)-u_n(x')}\le M\abs{x-x'}$, so the family is equicontinuous.
Since $u_n(x_0)$ converges, it is bounded, and $\abs{u_n(x)}\le\abs{u_n(x_0)}+M\abs{x-x_0}$ is bounded on each compact interval.
Arzelà–Ascoli on $[-k,k]$ for $k=1,2,\ldots$ and a diagonal argument give the claimed subsequence.
:::

:::

::: {.pf-step #s3}
Part (b) holds.

::: pf-proof
Suppose not. Then there are a compact interval $J$, an $\varepsilon>0$ and a subsequence with $\sup_J\abs{u_{n_k}-u}\ge\varepsilon$.
By step [](#s2){.pf-ref} a further subsequence converges uniformly on compact intervals to some $v$.
By step [](#s1){.pf-ref}, $v$ solves the differential equation, and $v(x_0)=\lim u_{n_k}(x_0)=y_0$.
Uniqueness gives $v=u$, so this further subsequence converges to $u$ uniformly on $J$, contradicting the choice of the subsequence.
:::

:::

:::
:::
