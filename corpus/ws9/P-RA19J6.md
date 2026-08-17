---
schema: qual/card@1
id: P-RA19J6
kind: problem
title: 'UGA analysis qualifying exam, January 2019, problem 6'
classification:
  areas:
  - real-analysis
  topics:
  - compactness
  - continuity
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Use the Heine--Borel Theorem to prove that if $f$ is continuous on $[a,b]$ and $f(x)>0$ for every $x\in[a,b]$, then there exists $\varepsilon>0$ such that $f(x)\ge\varepsilon$ for every $x\in[a,b]$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Use the Heine–Borel theorem to prove: $f$ continuous on $[a,b]$ with $f(x) > 0$ for all $x$ implies $f(x) \ge \varepsilon$ for some $\varepsilon > 0$ and all $x$.

<1>1. Cover $[a,b]$ by neighborhoods where $f$ is bounded below by a positive constant.
<2>1. For each $x_0 \in [a,b]$: since $f(x_0) > 0$ and $f$ is continuous at $x_0$, choose $\delta_{x_0} > 0$ with $|f(x) - f(x_0)| < f(x_0)/2$ for $|x - x_0| < \delta_{x_0}$; then $f(x) > f(x_0)/2 > 0$ on $(x_0 - \delta_{x_0}, x_0 + \delta_{x_0}) \cap [a,b]$.
Proof: $\varepsilon$-$\delta$ definition of continuity with $\varepsilon = f(x_0)/2$.
<2>2. The intervals $\{B(x_0, \delta_{x_0})\}$ form an open cover of $[a,b]$.
Proof: each $x_0$ lies in its own ball.

<1>2. Extract a finite subcover $B(x_1, \delta_{x_1}), \ldots, B(x_n, \delta_{x_n})$.
Proof: Heine–Borel: $[a,b]$ is compact, so every open cover has a finite subcover.

<1>3. Set $\varepsilon := \min_i \frac{f(x_i)}{2} > 0$; then $f(x) \ge \varepsilon$ for all $x \in [a,b]$.
Proof: every $x \in [a,b]$ lies in some $B(x_i, \delta_{x_i})$ by <1>2, where $f(x) > f(x_i)/2 \ge \varepsilon$ by <1>1 and the definition of $\varepsilon$; $\varepsilon > 0$ since each $f(x_i) > 0$ and the minimum is over finitely many positive numbers.

<1>4. Q.E.D. Proof: <1>3 is the claim.
:::
