---
schema: qual/card@1
id: P-RA18M5
kind: problem
title: 'UNL analysis qualifying exam, May 2018, problem 5'
classification:
  areas:
  - real-analysis
  topics:
  - equicontinuity
  - uniform-convergence
  - compactness
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(a) If $\{f_n\}_{n\ge1}$ is an equicontinuous sequence of functions on a compact interval and $f_n\to f$ pointwise, prove that the convergence is uniform.

(b) Let $\alpha,M>0$ be given, and suppose that $\{f_n\}_{n\ge1}$ satisfies $|f_n(x)-f_n(y)|\le M|x-y|^\alpha$ for all $n\ge1$ and all $x,y$ in an interval $[a,b]$.
Show that $\{f_n\}_{n\ge1}$ is equicontinuous.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** (a) Equicontinuous sequence on a compact interval, converging pointwise, converges uniformly; (b) $|f_n(x) - f_n(y)| \le M|x-y|^\alpha$ implies equicontinuity.

<1>1. (a) $f_n \to f$ uniformly.
<2>1. $f$ is continuous.
Proof: fix $x_0$; equicontinuity gives $\delta$ with $|f_n(x) - f_n(x_0)| < \varepsilon/3$ for all $n$ and $|x - x_0| < \delta$; let $n \to \infty$: $|f(x) - f(x_0)| \le \varepsilon/3$.
<2>2. Fix $\varepsilon > 0$.
By equicontinuity, for each $x$ there is $\delta_x$ with $|f_n(y) - f_n(x)| < \varepsilon/3$ for all $n$ and $|y - x| < \delta_x$; finitely many $\delta_{x_i}/2$-balls cover the interval (compactness).
<2>3. For each $x_i$ choose $N_i$ with $|f_n(x_i) - f(x_i)| < \varepsilon/3$ for $n \ge N_i$ (pointwise convergence); set $N = \max N_i$.
<2>4. For $n \ge N$ and any $x$: pick $i$ with $|x - x_i| < \delta_{x_i}/2$; then $|f_n(x) - f(x)| \le |f_n(x) - f_n(x_i)| + |f_n(x_i) - f(x_i)| + |f(x_i) - f(x)| < \varepsilon$.
Proof: three terms each $< \varepsilon/3$: the first by equicontinuity ($|x - x_i| < \delta_{x_i}/2 < \delta_{x_i}$), the second by $n \ge N_i$, the third by letting $n \to \infty$ in the equicontinuity bound (or continuity of $f$ from <2>1). <2>5. Q.E.D. Proof: <2>4 gives uniform convergence (the standard compactness argument for equicontinuity upgrading pointwise to uniform).

<1>2. (b) $\{f_n\}$ is equicontinuous on $[a,b]$.
<2>1. Given $\varepsilon > 0$, choose $\delta = (\varepsilon/M)^{1/\alpha}$.
<2>2. For $|x - y| < \delta$: $|f_n(x) - f_n(y)| \le M|x - y|^\alpha < M\delta^\alpha = \varepsilon$, for every $n$ simultaneously.
Proof: the Hölder hypothesis with $\delta$ as chosen; $\delta$ is independent of $n$, $x$, $y$.
<2>3. Q.E.D. Proof: <2>2 is exactly equicontinuity.
:::
