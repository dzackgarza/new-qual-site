---
schema: qual/card@1
id: P-UCLARA14S-01
kind: problem
title: Layer-cake formula for the L1 distance
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
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
Let $(X,\mathcal A,\mu)$ be a $\sigma$-finite measure space.
For $t\in\mathbb R$, let $e_t$ be the characteristic function of $(t,\infty)$.
Prove that for measurable $f,g:X\to\mathbb R$,
\[
\|f-g\|_{L^1(X)}=\int_{\mathbb R}\|e_t\circ f-e_t\circ g\|_{L^1(X)}\,dt.
\]
:::

::: pf

::: pf-step

For every $x\in X$,
\[
\int_{\mathbb R}
|e_t(f(x))-e_t(g(x))|\,dt
=
|f(x)-g(x)|.
\]


::: pf-proof

Fix $x\in X$. If $f(x)=g(x)$, then the integrand is identically zero and the equality is immediate.

Suppose first that $f(x)<g(x)$. Then
\[
e_t(f(x))
=
\mathbf 1_{\{t<f(x)\}},
\qquad
e_t(g(x))
=
\mathbf 1_{\{t<g(x)\}}.
\]
Hence
\[
|e_t(f(x))-e_t(g(x))|
=
\mathbf 1_{[f(x),g(x))}(t)
\]
up to endpoints, which do not affect the Lebesgue integral. Therefore
\[
\int_{\mathbb R}
|e_t(f(x))-e_t(g(x))|\,dt
=
g(x)-f(x).
\]
The case $g(x)<f(x)$ is identical with the roles reversed, giving $f(x)-g(x)$. Thus the value is always $|f(x)-g(x)|$.

:::

:::

::: pf-step

The function
\[
(x,t)
\longmapsto
|e_t(f(x))-e_t(g(x))|
\]
is measurable and nonnegative on $X\times\mathbb R$.


::: pf-proof

The set
\[
\{(x,t):t<f(x)\}
\]
is measurable because the map
\[
(x,t)\longmapsto f(x)-t
\]
is measurable. Hence $(x,t)\mapsto e_t(f(x))$ is measurable. The same holds for $g$, and therefore their absolute difference is measurable. Nonnegativity is immediate.

:::

:::

::: pf-step

One has
\[
\int_{\mathbb R}
\|e_t\circ f-e_t\circ g\|_{L^1(X)}\,dt
=
\int_X
\int_{\mathbb R}
|e_t(f(x))-e_t(g(x))|\,dt\,d\mu(x).
\]


::: pf-proof

By step <1>2, the integrand is nonnegative and measurable. Since $(X,\mathcal A,\mu)$ is $\sigma$-finite and Lebesgue measure on $\mathbb R$ is $\sigma$-finite, Tonelli's theorem applies:
\[
\begin{aligned}
\int_{\mathbb R}
\|e_t\circ f-e_t\circ g\|_{L^1(X)}\,dt
&=
\int_{\mathbb R}
\int_X
|e_t(f(x))-e_t(g(x))|\,d\mu(x)\,dt\\
&=
\int_X
\int_{\mathbb R}
|e_t(f(x))-e_t(g(x))|\,dt\,d\mu(x).
\end{aligned}
\]
The equality is valid in $[0,\infty]$.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\|f-g\|_{L^1(X)}
=
\int_{\mathbb R}
\|e_t\circ f-e_t\circ g\|_{L^1(X)}\,dt
}.
\]


::: pf-proof

Apply step <1>1 inside the iterated integral from step <1>3:
\[
\begin{aligned}
\int_{\mathbb R}
\|e_t\circ f-e_t\circ g\|_{L^1(X)}\,dt
&=
\int_X|f(x)-g(x)|\,d\mu(x)\\
&=
\|f-g\|_{L^1(X)}.
\end{aligned}
\]

:::

:::

::: pf-qed

Step <1>4 is the required identity.

:::

:::
