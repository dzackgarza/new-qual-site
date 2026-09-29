---
schema: qual/card@1
id: P-JHUFA02CAC
kind: problem
title: "Equicontinuity and the Arzela-Ascoli theorem on a Sobolev family"
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Arzela-Ascoli Theorem
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retyped the statement against Problem 3 of the JHU Fall 2002 Real Analysis qualifying exam in JHU Years of Analysis Exams.
---

::: {.problem}
(i) Define equicontinuity and state the Arzela-Ascoli theorem.

(ii) Let $\mathcal{F}$ be the family of real valued functions on $[0,1]$ satisfying $f(0)=0$ and $\int_0^1 f'(x)^2\,dx\le 1$.
Show that any sequence in $\mathcal{F}$ has a subsequence that converges uniformly.
:::

::: {.solution}
The functions in $\mathcal F$ are taken absolutely continuous, so that $f(x)=\int_0^xf'(t)\,dt$ for $f\in\mathcal F$.

::: pf

::: {.pf-step #s1}

(i) A family $\mathcal F\subseteq C([0,1])$ is equicontinuous if for every $\eps>0$ there is $\delta>0$ with $\abs{f(x)-f(y)}<\eps$ whenever $\abs{x-y}<\delta$ and $f\in\mathcal F$. The Arzelà--Ascoli theorem: for a compact metric space $K$, a family in $C(K)$ that is pointwise bounded and equicontinuous has the property that every sequence in it has a uniformly convergent subsequence.

::: pf-proof

These are the requested definition and statement; on the compact interval $[0,1]$ equicontinuity at every point is equivalent to the uniform version stated.

:::

:::

::: {.pf-step #s2}

$\abs{f(x)-f(y)}\le\sqrt{\abs{x-y}}$ for $f\in\mathcal F$ and $x,y\in[0,1]$.

::: pf-proof

For $y\le x$, the Cauchy--Schwarz inequality gives $\abs{\int_y^xf'}\le(x-y)^{1/2}\bigl(\int_0^1f'^2\bigr)^{1/2}\le\sqrt{x-y}$.

:::

:::

::: pf-qed

By step [](#s2){.pf-ref} with $y=0$, $\abs f\le1$ on $[0,1]$ for all $f\in\mathcal F$, and with $\delta=\eps^2$ the family is equicontinuous. By the Arzelà--Ascoli theorem of step [](#s1){.pf-ref}, every sequence in $\mathcal F$ has a uniformly convergent subsequence.

:::

:::

:::
