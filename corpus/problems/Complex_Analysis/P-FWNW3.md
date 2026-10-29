---
schema: qual/card@1
id: P-FWNW3
kind: problem
title: Uniform approximation of holomorphic functions by polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Uniform Convergence
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source read "any holomorphic function f on a simply connected domain (or compact set with connected complement) can be uniformly approximated by polynomials on compact subsets". A function is not holomorphic on a compact set, so the parenthetical case now requires f holomorphic on a neighborhood of K and asks for approximation on K; the two cases are parts (a) and (b).
---

::: {.problem}
(a) Let $K\subset\CC$ be compact with $\CC\setminus K$ connected, and let $f$ be holomorphic on a neighborhood of $K$. Show that $f$ can be uniformly approximated by polynomials on $K$.

(b) Let $\Omega\subseteq\CC$ be a simply connected domain and $f$ holomorphic on $\Omega$. Show that $f$ can be uniformly approximated by polynomials on every compact subset of $\Omega$.
:::

::: {.solution}
::: pf

::: {.pf-step #part-a}
(a) For every $\varepsilon>0$ there is a polynomial $p$ with $\sup_{z\in K}\abs{f(z)-p(z)}<\varepsilon$.

::: pf-proof
Runge's theorem approximates $f$ uniformly on $K$ by rational functions with poles in a prescribed set containing one point of each component of $\widehat\CC\setminus K$. Because $\CC\setminus K$ is connected, $\widehat\CC\setminus K$ has one component, which contains $\infty$, so we may prescribe the single pole $\infty$. A rational function whose only pole is $\infty$ is a polynomial.
:::

:::

::: {.pf-step #hull}
(b) Let $K\subset\Omega$ be compact, and let $\widehat K$ be the union of $K$ with the bounded components of $\CC\setminus K$. Then $\widehat K$ is compact, $\CC\setminus\widehat K$ is connected, and $\widehat K\subset\Omega$.

::: pf-proof
$\CC\setminus\widehat K$ is the unbounded component of $\CC\setminus K$, which is open and connected, and $\widehat K$ is closed and bounded.
A plane domain $\Omega$ is simply connected exactly when $\widehat\CC\setminus\Omega$ is connected.
The set $\widehat\CC\setminus\Omega$ is connected, contains $\infty$, and does not meet $K$, so it lies in the component of $\widehat\CC\setminus K$ that contains $\infty$.
Hence no bounded component of $\CC\setminus K$ meets $\CC\setminus\Omega$, that is, every bounded component lies in $\Omega$.
:::

:::

::: pf-step
(b) For every compact $K\subset\Omega$ and $\varepsilon>0$ there is a polynomial $p$ with $\sup_{z\in K}\abs{f(z)-p(z)}<\varepsilon$.

::: pf-proof
By step [](#hull){.pf-ref}, $f$ is holomorphic on the open neighborhood $\Omega$ of $\widehat K$ and $\CC\setminus\widehat K$ is connected. Step [](#part-a){.pf-ref} gives a polynomial $p$ within $\varepsilon$ of $f$ on $\widehat K\supseteq K$.
:::

:::

:::

:::
