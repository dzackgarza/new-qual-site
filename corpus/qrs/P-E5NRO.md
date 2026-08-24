---
schema: qual/card@1
id: P-E5NRO
kind: problem
title: Equivalence of open-closed approximation and a $G_\delta$-$F_\sigma$ sandwich
  for finite Borel measures on $\mathbb{R}$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: problem
Let $\mu$ be a finite Borel measure on $\RR$ and $E \subset \RR$ Borel.
Prove that the following statements are equivalent:

1. $\forall \varepsilon > 0$ there exists $G$ open and $F$ closed such that
$$
F \subseteq E \subseteq G \quad \text{and} \quad \mu(G\setminus F) < \varepsilon.
$$

2. There exists a $V \in G_\delta$ and $H \in F_\sigma$ such that
$$
H \subseteq E \subseteq V \quad \text{and}\quad \mu(V\setminus H) = 0
$$
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. (1) $\implies$ (2). <2>1. For each $k \ge 1$, choose open $G_k$ and closed $F_k$ with $F_k \subseteq E \subseteq G_k$ and $\mu(G_k \setminus F_k) < 1/k$.
Proof: hypothesis (1) with $\eps = 1/k$.
<2>2. Set $V = \bigcap_k G_k$ and $H = \bigcup_k F_k$; then $V$ is a $G_\delta$, $H$ is an $F_\sigma$, and $H \subseteq E \subseteq V$.
Proof: $F_k \subseteq E \subseteq G_k$ for all $k$.
<2>3. $\mu(V \setminus H) = 0$.
Proof: for each $k$, $V \setminus H \subseteq G_k \setminus F_k$ (since $V \subseteq G_k$ and $F_k \subseteq H$), so $\mu(V \setminus H) \le \mu(G_k \setminus F_k) < 1/k$; letting $k \to \infty$ gives $\mu(V \setminus H) = 0$.
<2>4. Q.E.D. Proof: <2>2 and <2>3.

<1>2. (2) $\implies$ (1). <2>1. Write $V = \bigcap_m G_m$ with $G_m$ open and decreasing, and $H = \bigcup_m F_m$ with $F_m$ closed and increasing.
Proof: any $G_\delta$ is an intersection of open sets; replacing by finite intersections makes the sequence decreasing; similarly for $F_m$ via finite unions.
<2>2. $\mu(G_m \setminus V) \to 0$ and $\mu(H \setminus F_m) \to 0$ as $m \to \infty$.
Proof: continuity from above for the decreasing sets $G_m \downarrow V$ (with $\mu(G_1) \le \mu(\RR) < \infty$), and continuity from below for $F_m \uparrow H$ (with $\mu(H) \le \mu(V) < \infty$). <2>3. Given $\eps > 0$, choose $m$ with $\mu(G_m \setminus V) < \eps/2$ and $\mu(H \setminus F_m) < \eps/2$; set $G = G_m$ and $F = F_m$.
Proof: <2>2. <2>4. $F \subseteq E \subseteq G$ and $\mu(G \setminus F) < \eps$.
Proof: $F_m \subseteq H \subseteq E \subseteq V \subseteq G_m$; and $G \setminus F \subseteq (G \setminus V) \cup (V \setminus H) \cup (H \setminus F)$, so $\mu(G \setminus F) \le \eps/2 + 0 + \eps/2 = \eps$ using (2) for $\mu(V \setminus H) = 0$.
<2>5. Q.E.D. Proof: <2>3 and <2>4.
:::
