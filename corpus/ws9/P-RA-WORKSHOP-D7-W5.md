---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W5
kind: problem
title: Equicontinuity upgrades pointwise convergence to uniform convergence
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Uniform Convergence
  - Compactness
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Show that if $\{f_n\}$ is an equicontinuous sequence of functions on a compact set $K$ and $f_n\to f$ pointwise on $K$, then $f_n\to f$ uniformly on $K$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Show $\{f_n\}$ equicontinuous on compact $K$ with $f_n \to f$ pointwise implies $f_n \to f$ uniformly on $K$.

<1>1. $f$ is continuous.
Proof: uniform limits are continuous; here we only know pointwise convergence, so instead: fix $x_0$ and $\varepsilon > 0$; by equicontinuity choose $\delta$ with $\|x-x_0\| < \delta \Rightarrow |f_n(x) - f_n(x_0)| < \varepsilon/3$ for all $n$.
For $\|x - x_0\| < \delta$, let $n \to \infty$ in $|f_n(x) - f_n(x_0)| < \varepsilon/3$ to get $|f(x) - f(x_0)| \le \varepsilon/3 < \varepsilon$.
So $f$ is continuous at $x_0$.

<1>2. Fix $\varepsilon > 0$.
By equicontinuity, for each $x \in K$ there is $\delta_x > 0$ with $\|y - x\| < \delta_x \Rightarrow |f_n(y) - f_n(x)| < \varepsilon/3$ for all $n$.
Proof: definition of equicontinuity (uniform over $n$).

<1>3. Choose finitely many $x_1, \ldots, x_m$ such that $K \subseteq \bigcup_i B(x_i, \delta_{x_i}/2)$.
Proof: compactness of $K$.

<1>4. For each $i$, choose $N_i$ with $|f_n(x_i) - f(x_i)| < \varepsilon/3$ for all $n \ge N_i$.
Proof: pointwise convergence at $x_i$.

<1>5. Set $N = \max_i N_i$.
For $n \ge N$ and any $x \in K$: pick $i$ with $x \in B(x_i, \delta_{x_i}/2)$; then $|f_n(x) - f(x)| \le |f_n(x) - f_n(x_i)| + |f_n(x_i) - f(x_i)| + |f(x_i) - f(x)|$.
Proof: triangle inequality.

<1>6. Each of the three terms is $< \varepsilon/3$ for $n \ge N$.
<2>1. $|f_n(x) - f_n(x_i)| < \varepsilon/3$: $\|x - x_i\| < \delta_{x_i}/2 < \delta_{x_i}$, equicontinuity.
<2>2. $|f_n(x_i) - f(x_i)| < \varepsilon/3$: $n \ge N \ge N_i$, by <1>4. <2>3. $|f(x_i) - f(x)| < \varepsilon/3$: since $|f_n(x) - f_n(x_i)| < \varepsilon/3$ for all $n$ (equicontinuity with $\|x - x_i\| < \delta_{x_i}$), let $n \to \infty$; continuity of $f$ from <1>1 also works with a suitable $\delta$.
Proof: pointwise convergence $f_n \to f$ at both $x$ and $x_i$ gives $|f(x) - f(x_i)| = \lim_n |f_n(x) - f_n(x_i)| \le \varepsilon/3$.
<2>4. Q.E.D. Proof: <2>1–<2>3 sum to $|f_n(x) - f(x)| < \varepsilon$ for all $x \in K$, $n \ge N$: uniform convergence.
:::
