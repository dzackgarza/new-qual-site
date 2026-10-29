---
schema: qual/card@1
id: P-UCLARA13F-12
kind: problem
title: Absolute continuity near zero and bounded variation
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
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Let $f:[0,1]\to\RR$ be continuous and absolutely continuous on every interval $[\varepsilon,1]$ with $0<\varepsilon\le1$.

(a) Show by example that $f$ need not be absolutely continuous on $[0,1]$.

(b) Show that if, in addition, $f$ is of bounded variation on $[0,1]$, then $f$ is absolutely continuous on $[0,1]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For part (a), define
\[
f(0)=0,
\qquad
f(x)=x\sin(1/x)
\quad(0<x\leq1).
\]
Then $f$ is continuous on $[0,1]$ and absolutely continuous on every $[\varepsilon,1]$.


::: pf-proof

Since $|x\sin(1/x)|\leq x$, one has $f(x)\to0=f(0)$ as $x\downarrow0$. On every $[\varepsilon,1]$, the function is continuously differentiable, hence absolutely continuous.

:::

:::

::: {.pf-step #s1-2}

For $x>0$,
\[
f'(x)=\sin(1/x)-\frac{\cos(1/x)}x.
\]


::: pf-proof

Differentiate $x\sin(1/x)$ by the product and chain rules.

:::

:::

::: {.pf-step #s1-3}

The derivative is not integrable on $(0,1)$:
\[
\int_0^1|f'(x)|\,dx=\infty.
\]


::: pf-proof

The term $\sin(1/x)$ is bounded and hence integrable on $(0,1)$. It therefore suffices to show
\[
\int_0^1\frac{|\cos(1/x)|}{x}\,dx=\infty.
\]
With $t=1/x$, this becomes
\[
\int_1^\infty\frac{|\cos t|}{t}\,dt.
\]
On each interval $[k\pi,k\pi+\pi/3]$, one has $|\cos t|\geq1/2$ after choosing the corresponding half-period subinterval, so the integral dominates a positive constant times a harmonic series and diverges.

:::

:::

::: {.pf-step #s1-4}

Thus $f$ is not absolutely continuous on $[0,1]$.


::: pf-proof

An absolutely continuous function on a compact interval has derivative in $L^1$ and satisfies
\[
f(x)-f(0)=\int_0^xf'(t)\,dt.
\]
Step [](#s1-3){.pf-ref} contradicts the required $L^1$ integrability.

:::

:::

::: {.pf-step #s1-5}

For part (b), assume additionally that $f$ has bounded variation on $[0,1]$. Let
\[
V(t)=\operatorname{Var}_{[0,t]}(f).
\]
Then
\[
V(t)\longrightarrow0
\qquad(t\downarrow0).
\]


::: pf-proof

Because $f$ has bounded variation, it is the difference of two bounded monotone functions, and its total-variation function $V$ is increasing and finite. Hence $L=\lim_{t\downarrow0}V(t)$ exists. For every $t>0$,
\[
V(t)\geq |f(t)-f(0)|,
\]
but more is needed to exclude $L>0$. The variation measure associated to a BV function has an atom at $0$ of mass exactly the jump $|f(0+)-f(0)|$. On $(0,1]$, local absolute continuity implies that this variation measure is absolutely continuous with density $|f'|$. Thus its only possible singular mass is at $0$. Continuity of $f$ at $0$ makes that atom zero, so continuity from above of the finite variation measure gives $V(t)\to0$.

:::

:::

::: {.pf-step #s1-6}

Fix $\eta>0$. Choose $\delta_0>0$ so that
\[
\operatorname{Var}_{[0,\delta_0]}(f)<\eta/2.
\]


::: pf-proof

This follows from step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Since $f$ is absolutely continuous on $[\delta_0/2,1]$, there exists $\delta_1>0$ such that every finite pairwise-disjoint family of intervals $(a_j,b_j)\subset[\delta_0/2,1]$ with
\[
\sum_j(b_j-a_j)<\delta_1
\]
satisfies
\[
\sum_j|f(b_j)-f(a_j)|<\eta/2.
\]


::: pf-proof

This is the defining interval criterion for absolute continuity on $[\delta_0/2,1]$.

:::

:::

::: {.pf-step #s1-8}

Set
\[
\delta=\min\{\delta_0/2,\delta_1\}.
\]
Then any finite pairwise-disjoint family $(a_j,b_j)\subset[0,1]$ with total length $<\delta$ satisfies
\[
\sum_j|f(b_j)-f(a_j)|<\eta.
\]


::: pf-proof

Separate the intervals into those meeting $[0,\delta_0]$ and those lying in $[\delta_0/2,1]$. Because their total length is $<\delta_0/2$, an interval beginning below $\delta_0/2$ cannot end beyond $\delta_0$; hence every such interval lies in $[0,\delta_0]$. The sum of oscillations over all intervals in this first group is at most $\operatorname{Var}_{[0,\delta_0]}(f)<\eta/2$ by step [](#s1-6){.pf-ref}. The remaining intervals lie in $[\delta_0/2,1]$ and have total length $<\delta_1$, so step [](#s1-7){.pf-ref} bounds their sum by $\eta/2$. Adding the two bounds gives $<\eta$.

:::

:::

::: {.pf-step #s1-9}

Therefore $f$ is absolutely continuous on $[0,1]$.


::: pf-proof

Step [](#s1-8){.pf-ref} verifies the defining $\varepsilon$--$\delta$ interval criterion for absolute continuity, with arbitrary $\eta>0$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} prove part (a), and steps [](#s1-5){.pf-ref} through [](#s1-9){.pf-ref} prove part (b).

:::

:::

:::
