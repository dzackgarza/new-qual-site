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
Fix $y \in Y$, let $U \subseteq X$ be an evenly covered open neighborhood of $f(y)$ with $p^{-1}(U) = \bigsqcup_\alpha \widetilde U_\alpha$ and each $p|_{\widetilde U_\alpha}\colon \widetilde U_\alpha \to U$ a homeomorphism, and put $V = f^{-1}(U)$, an open neighborhood of $y$ because $f$ is continuous. For each $\alpha$ let $s_\alpha = (p|_{\widetilde U_\alpha})^{-1}\colon U \to \widetilde U_\alpha$ and $W_\alpha = \widetilde Y \cap (V \times \widetilde U_\alpha)$.

<1>1. $q^{-1}(V) = \bigsqcup_\alpha W_\alpha$, a disjoint union of open subsets of $\widetilde Y$.
::: {.proof}
Each $W_\alpha$ is open in $\widetilde Y$ because $V \times \widetilde U_\alpha$ is open in $Y \times \widetilde X$, and the $W_\alpha$ are pairwise disjoint because the $\widetilde U_\alpha$ are. If $(y', \widetilde x) \in \widetilde Y$ with $y' \in V$, then $p(\widetilde x) = f(y') \in U$, so $\widetilde x$ lies in exactly one $\widetilde U_\alpha$, and $(y', \widetilde x) \in W_\alpha$. Conversely every $W_\alpha$ lies in $q^{-1}(V)$.
:::

<1>2. For each $\alpha$, $q|_{W_\alpha}\colon W_\alpha \to V$ is a homeomorphism.
::: {.proof}
The map $\sigma_\alpha\colon V \to W_\alpha$, $\sigma_\alpha(y') = (y', s_\alpha(f(y')))$, is continuous, lands in $\widetilde Y$ because $p(s_\alpha(f(y'))) = f(y')$, and satisfies $q \circ \sigma_\alpha = \operatorname{id}_V$. If $(y', \widetilde x) \in W_\alpha$, then $\widetilde x \in \widetilde U_\alpha$ and $p(\widetilde x) = f(y')$, so $\widetilde x = s_\alpha(f(y'))$ and $\sigma_\alpha(q(y', \widetilde x)) = (y', \widetilde x)$. Thus $\sigma_\alpha$ is a continuous inverse of the continuous map $q|_{W_\alpha}$.
:::

<1>3. Q.E.D.
::: {.proof}
By steps <1>1 and <1>2, every $y \in Y$ has an open neighborhood $V$ evenly covered by $q$, so $q$ is a covering map.
:::
:::
