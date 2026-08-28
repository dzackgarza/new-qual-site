---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-02
kind: problem
title: The pullback of a covering map is a covering map
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
(Jan ’06) Let $p:\widetilde X\to X$ be a covering map, and $f:Y\to X$ be a continuous map.
Define $$\widetilde Y=\{(y,\widetilde x)\in Y\times\widetilde X:f(y)=p(\widetilde x)\}\subseteq Y\times\widetilde X$$ with the subspace topology inherited from $Y\times\widetilde X$ and define $q:\widetilde Y\to Y$ by $q(y,\widetilde x)=y$.
Show that $q$ is also a covering map.
:::

::: {.solution}
**Goal.** Show the pullback $\tilde Y$ of a covering map $p: \tilde X \to X$ along $f: Y \to X$ is again a covering map.

<1>1. Let $y \in Y$ and let $U \subseteq X$ be an evenly covered neighborhood of $f(y)$.
<2>1. $p^{-1}(U) = \bigsqcup_\alpha \tilde U_\alpha$ with each $\tilde U_\alpha$ mapping homeomorphically onto $U$ via $p$.
Proof: definition of an evenly covered neighborhood.

<1>2. $V \definedas f^{-1}(U)$ is an open neighborhood of $y$.
Proof: $f$ is continuous and $f(y) \in U$.

<1>3. $q^{-1}(V) = \bigsqcup_\alpha \qty(V \times \tilde U_\alpha) \cap \tilde Y$.
<2>1. $q^{-1}(V) = \theset{(y', \tilde x) \in \tilde Y : y' \in V}$.
Proof: $q(y', \tilde x) = y'$.
<2>2. For $(y', \tilde x) \in \tilde Y$ with $y' \in V$, we have $f(y') \in U$ and $p(\tilde x) = f(y') \in U$, so $\tilde x \in p^{-1}(U) = \bigsqcup_\alpha \tilde U_\alpha$.
Proof: $f(y') = p(\tilde x)$ and $f(y') \in U$.
<2>3. Hence $q^{-1}(V) = \bigsqcup_\alpha \theset{(y', \tilde x) : y' \in V, \tilde x \in \tilde U_\alpha, f(y') = p(\tilde x)}$.
Proof: partition by which $\tilde U_\alpha$ contains $\tilde x$.

<1>4. Each piece maps homeomorphically onto $V$ via $q$.
<2>1. For fixed $\alpha$, the map $q: \theset{(y', \tilde x) \in V \times \tilde U_\alpha : f(y') = p(\tilde x)} \to V$ is a homeomorphism.
Proof: since $p|_{\tilde U_\alpha}: \tilde U_\alpha \to U$ is a homeomorphism, for each $y' \in V$ there is a unique $\tilde x \in \tilde U_\alpha$ with $p(\tilde x) = f(y')$, namely $\tilde x = (p|_{\tilde U_\alpha})^{-1}(f(y'))$; this gives a continuous inverse $y' \mapsto (y', (p|_{\tilde U_\alpha})^{-1}(f(y')))$.
<2>2. Hence $q$ is a covering map.
Proof: $V$ is an evenly covered neighborhood of $y$, and $y$ was arbitrary.

<1>5. Q.E.D.
Proof: <1>4.2 shows $q$ is a covering map.
:::
