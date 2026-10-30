---
schema: qual/card@1
id: P-UCLARA14S-01
kind: problem
title: 'Layer-cake formula for the $L^1$ distance'
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
For $t\in\RR$, let $e_t$ be the characteristic function of $(t,\infty)$.
Prove that for measurable $f,g:X\to\RR$,
$$
\norm{f-g}_{L^1(X)}=\int_{\RR}\norm{e_t\circ f-e_t\circ g}_{L^1(X)}\,dt.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $x\in X$,
$$
\int_{\RR}
\abs{e_t(f(x))-e_t(g(x))}\,dt
=
\abs{f(x)-g(x)}.
$$


::: pf-proof

Fix $x\in X$. If $f(x)=g(x)$, then the integrand is identically zero and the equality is immediate.

Suppose first that $f(x)<g(x)$. Then
$$
e_t(f(x))
=
\mathbf 1_{\{t<f(x)\}},
\qquad
e_t(g(x))
=
\mathbf 1_{\{t<g(x)\}}.
$$
Hence
$$
\abs{e_t(f(x))-e_t(g(x))}
=
\mathbf 1_{[f(x),g(x))}(t)
$$
up to endpoints, which do not affect the Lebesgue integral. Therefore
$$
\int_{\RR}
\abs{e_t(f(x))-e_t(g(x))}\,dt
=
g(x)-f(x).
$$
The case $g(x)<f(x)$ is identical with the roles reversed, giving $f(x)-g(x)$. Thus the value is always $\abs{f(x)-g(x)}$.

:::

:::

::: {.pf-step #s1-2}

The function
$$
(x,t)
\longmapsto
\abs{e_t(f(x))-e_t(g(x))}
$$
is measurable and nonnegative on $X\times\RR$.


::: pf-proof

The set
$$
\{(x,t):t<f(x)\}
$$
is measurable because the map
$$
(x,t)\longmapsto f(x)-t
$$
is measurable. Hence $(x,t)\mapsto e_t(f(x))$ is measurable. The same holds for $g$, and therefore their absolute difference is measurable. Nonnegativity is immediate.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_{\RR}
\norm{e_t\circ f-e_t\circ g}_{L^1(X)}\,dt
=
\int_X
\int_{\RR}
\abs{e_t(f(x))-e_t(g(x))}\,dt\,d\mu(x).
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, the integrand is nonnegative and measurable. Since $(X,\mathcal A,\mu)$ is $\sigma$-finite and Lebesgue measure on $\RR$ is $\sigma$-finite, Tonelli's theorem applies:
$$
\begin{aligned}
\int_{\RR}
\norm{e_t\circ f-e_t\circ g}_{L^1(X)}\,dt
&=
\int_{\RR}
\int_X
\abs{e_t(f(x))-e_t(g(x))}\,d\mu(x)\,dt\\
&=
\int_X
\int_{\RR}
\abs{e_t(f(x))-e_t(g(x))}\,dt\,d\mu(x).
\end{aligned}
$$
The equality is valid in $[0,\infty]$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\norm{f-g}_{L^1(X)}
=
\int_{\RR}
\norm{e_t\circ f-e_t\circ g}_{L^1(X)}\,dt
}.
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} inside the iterated integral from step [](#s1-3){.pf-ref}:
$$
\begin{aligned}
\int_{\RR}
\norm{e_t\circ f-e_t\circ g}_{L^1(X)}\,dt
&=
\int_X\abs{f(x)-g(x)}\,d\mu(x)\\
&=
\norm{f-g}_{L^1(X)}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required identity.

:::

:::

:::
