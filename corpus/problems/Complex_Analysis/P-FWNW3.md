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
---

::: problem
Show that any holomorphic function $f$ on a simply connected domain (or compact set with connected complement) can be uniformly approximated by polynomials on compact subsets.
:::

::: solution
There are two standard forms of the statement.

<1>1. Let $K\subset\mathbb C$ be compact with connected complement, and suppose $f$ is holomorphic on a neighborhood of $K$. By Runge's theorem, for every $\varepsilon>0$ there exists a polynomial $p$ such that
\[
\sup_{z\in K}|f(z)-p(z)|<\varepsilon.
\]
Indeed, Runge gives approximation by rational functions whose poles may be chosen in the components of $\widehat{\mathbb C}\setminus K$. Since this complement is connected, the only required pole may be placed at $\infty$; rational functions with their only pole at $\infty$ are polynomials.

<1>2. Now let $\Omega\subset\mathbb C$ be simply connected and let $f\in H(\Omega)$. Fix a compact set $K\Subset\Omega$. Choose a bounded Jordan domain $U$ such that
\[
K\subset U,\qquad \overline U\subset\Omega.
\]
Such a $U$ exists because a simply connected plane domain admits an exhaustion by relatively compact Jordan domains. The compact set $L=\overline U$ has connected complement, and $f$ is holomorphic on a neighborhood of $L$.

Applying the compact form of Runge's theorem to $L$, for every $\varepsilon>0$ there is a polynomial $p$ with
\[
\sup_{z\in L}|f(z)-p(z)|<\varepsilon.
\]
Since $K\subset L$,
\[
\sup_{z\in K}|f(z)-p(z)|<\varepsilon.
\]
Thus polynomials approximate $f$ uniformly on every compact subset of $\Omega$.
:::
