---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W2
kind: problem
title: Pointwise and uniform equicontinuity on a compact set
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Compactness
  - Uniform Continuity
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
To clarify Remark 6.6: A family of functions $\mathcal F\subset C(K,\mathbb R^m)$ mapping a set $K\subset\mathbb R^n$ into $\mathbb R^m$ is pointwise equicontinuous on $K$ provided for every $x\in K$ and $\epsilon>0$ there exists some $\delta>0$ (which may depend on $x$) such that $\|f(x)-f(y)\|<\epsilon$ for all $f\in\mathcal F$ and $y\in K$ with $\|x-y\|<\delta$.
The family $\mathcal F$ is uniformly equicontinuous if for every $\epsilon>0$ there exists some $\delta>0$ such that $\|f(x)-f(y)\|<\epsilon$ for all $f\in\mathcal F$ and $x,y\in K$ with $\|x-y\|<\delta$.
Prove that these definitions are equivalent when $K$ is compact.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove pointwise equicontinuity and uniform equicontinuity of a family $\mathcal F \subseteq C(K;\mathbb R^m)$ are equivalent when $K$ is compact.

<1>1. Uniform equicontinuity implies pointwise equicontinuity.
Proof: if $\delta$ works for all $x, y$ simultaneously, then in particular it works for all $y$ with $y$ near a fixed $x$; so the pointwise condition holds with the same $\delta$ (independent of $x$, hence certainly allowed to depend on $x$).

<1>2. Pointwise equicontinuity implies uniform equicontinuity.
<2>1. Fix $\varepsilon > 0$.
For each $x \in K$ choose $\delta_x > 0$ such that $\|x - y\| < \delta_x \Rightarrow \|f(x) - f(y)\| < \varepsilon/2$ for all $f \in \mathcal F$.
Proof: the pointwise equicontinuity hypothesis at $x$ with $\varepsilon/2$ in place of $\varepsilon$.
<2>2. The balls $B(x, \delta_x/2)$, $x \in K$, cover $K$.
Proof: $x \in B(x, \delta_x/2)$ for each $x$.
<2>3. $K$ is covered by finitely many of them: $K \subseteq \bigcup_{i=1}^n B(x_i, \delta_{x_i}/2)$.
Proof: compactness of $K$ applied to the open cover of <2>2. <2>4. Set $\delta := \min_i \delta_{x_i}/2 > 0$.
If $\|x - y\| < \delta$, then for every $f \in \mathcal F$, $\|f(x) - f(y)\| < \varepsilon$.
Proof: $x$ lies in some $B(x_i, \delta_{x_i}/2)$ by <2>3, so $\|x - x_i\| < \delta_{x_i}/2$; then $\|y - x_i\| \le \|y - x\| + \|x - x_i\| < \delta + \delta_{x_i}/2 \le \delta_{x_i}/2 + \delta_{x_i}/2 = \delta_{x_i}$ since $\delta \le \delta_{x_i}/2$.
Both $x$ and $y$ are within $\delta_{x_i}$ of $x_i$, so $\|f(x) - f(x_i)\| < \varepsilon/2$ and $\|f(y) - f(x_i)\| < \varepsilon/2$, hence $\|f(x) - f(y)\| \le \|f(x)-f(x_i)\| + \|f(y)-f(x_i)\| < \varepsilon$ by the triangle inequality.
This holds for all $f \in \mathcal F$ simultaneously, and $\delta$ is independent of $x, y, f$.
<2>5. Q.E.D. Proof: <2>4 is uniform equicontinuity.
:::
