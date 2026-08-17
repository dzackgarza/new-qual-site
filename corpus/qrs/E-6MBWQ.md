---
schema: qual/card@1
id: E-6MBWQ
kind: exercise
title: A metrizable space is compact if and only if it is sequentially compact
classification:
  areas:
  - topology
  topics:
  - metric-spaces
  - compactness
relations:
- kind: related-to
  target: E-2LZES
review: draft
solved: true
---

::: exercise
Show that a metrizable space is compact if and only if it is sequentially compact.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $(X, d)$ be a metric space.

**$(\Longrightarrow)$ Compact $\implies$ Sequentially Compact:** Let $(x_n)_{n=1}^\infty$ be a sequence in $X$.

- If the set of values $S = \{x_n : n \in \mathbb{N}\}$ is finite, then by the Pigeonhole Principle there is a point $x \in S$ and a subsequence that is identically constant $x_{n_k} = x$, which trivially converges to $x$.

- If $S$ is infinite: Suppose towards a contradiction that $(x_n)$ has no convergent subsequence.
  Then no point $x \in X$ is an accumulation point of $S$.
  Thus, for every $x \in X$, there exists an open ball $U_x = B(x, \varepsilon_x)$ containing at most finitely many points of $S$ (specifically, at most $x$ itself).
  The collection $\{U_x\}_{x \in X}$ is an open cover of the compact space $X$.
  By compactness, there exists a finite subcover $\{U_{x_1}, \ldots, U_{x_m}\}$ covering $X$.
  Then $S \subseteq X \subseteq \bigcup_{i=1}^m U_{x_i}$, which implies that $S$ is a subset of a finite union of finite sets, hence $S$ must be finite, a contradiction.
  Thus $(x_n)$ must have a convergent subsequence.

**$(\Longleftarrow)$ Sequentially Compact $\implies$ Compact:** We establish this via Lebesgue Number and Total Boundedness:

1. **Lebesgue's Number Lemma:** Let $\mathcal{U} = \{U_\alpha\}_{\alpha \in A}$ be an open cover of $X$.
   Suppose towards a contradiction that there is no Lebesgue number: for every $n \in \mathbb{N}$, there exists $x_n \in X$ such that $B(x_n, 1/n)$ is not contained in any single set $U_\alpha \in \mathcal{U}$.
   Since $X$ is sequentially compact, $(x_n)$ has a subsequence $(x_{n_k})$ converging to some point $x \in X$.
   Since $\mathcal{U}$ covers $X$, $x \in U_{\alpha_0}$ for some $\alpha_0$.
   Since $U_{\alpha_0}$ is open, there exists $r > 0$ such that $B(x, r) \subseteq U_{\alpha_0}$.
   Since $x_{n_k} \to x$, choose $k$ large enough such that $d(x_{n_k}, x) < r/2$ and $1/n_k < r/2$.
   Then for any $y \in B(x_{n_k}, 1/n_k)$:
   $$
   d(y, x) \leq d(y, x_{n_k}) + d(x_{n_k}, x) < \frac{1}{n_k} + \frac{r}{2} < \frac{r}{2} + \frac{r}{2} = r.
   $$
   Thus $B(x_{n_k}, 1/n_k) \subseteq B(x, r) \subseteq U_{\alpha_0}$, contradicting the choice of $x_{n_k}$.
   Hence, there exists a Lebesgue number $\delta > 0$ for the cover $\mathcal{U}$.

2. **Total Boundedness:** As proved in standard metric space theory, sequential compactness implies that $X$ is totally bounded (otherwise an infinite $\delta$-separated sequence would have no Cauchy/convergent subsequence).
   Thus, for the Lebesgue number $\delta > 0$, $X$ can be covered by finitely many open balls of radius $\delta$:
   $$
   X = \bigcup_{i=1}^N B(y_i, \delta).
   $$

3. **Finite Subcover:** By the definition of the Lebesgue number $\delta$, each ball $B(y_i, \delta)$ is entirely contained in some open set $U_{\alpha_i} \in \mathcal{U}$.
   Therefore:
   $$
   X = \bigcup_{i=1}^N B(y_i, \delta) \subseteq \bigcup_{i=1}^N U_{\alpha_i}.
   $$
   Thus $\{U_{\alpha_1}, \ldots, U_{\alpha_N}\}$ is a finite subcover of $\mathcal{U}$, proving that $X$ is compact.
:::

::: {.remark}
Munkres, *Topology*, §28, Theorem 28.2, which adds limit point compactness as a third equivalent condition.

As printed upstream this exercise read "Show that if $X$ is metrizable, then $X$ is compact", which is false: $\RR$ is metrizable and not compact.
:::
