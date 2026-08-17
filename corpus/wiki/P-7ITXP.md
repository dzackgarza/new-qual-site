---
schema: qual/card@1
id: P-7ITXP
kind: problem
title: "\\label{equivalence_of_approximating_measures}"
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
solved: true
---

::: problem
\label{equivalence_of_approximating_measures}
Let $E \subseteq \RR^n$ be bounded.
Prove the following are equivalent: 

1. For any \( \epsilon>0 \) there exists and open set \( G \) and a closed set \( F \) such that 
\[
F \subseteq E \subseteq G && m(G\sm F) < \epsilon
.\]

2. There exists a \( G_ \delta \) set $V$ and an \( F_ \sigma \) set $H$ such that 
\[
m(V\sm H) = 0
.\]
:::

::: {.solution}
> **AI-Generated Solution**

**Honesty note:** as printed, condition (2) does not mention $E$ at all, which makes it vacuous. The intended equivalence — the standard one — is: (1) holds iff there exist $V \in G_\delta$ and $H \in F_\sigma$ with $H \subseteq E \subseteq V$ and $m(V \setminus H) = 0$. The proof below is for that statement.

<1>1. (1) $\implies$ (2): for each $k$, hypothesis (1) with $\eps = 1/k$ gives open $G_k$ and closed $F_k$ with $F_k \subseteq E \subseteq G_k$ and $m(G_k \setminus F_k) < 1/k$.
    Proof: hypothesis.

<1>2. Set $V = \bigcap_k G_k$ (a $G_\delta$) and $H = \bigcup_k F_k$ (an $F_\sigma$); then $H \subseteq E \subseteq V$.
    Proof: $F_k \subseteq E \subseteq G_k$ for all $k$.

<1>3. $m(V \setminus H) = 0$.
    Proof: for each $k$, $V \setminus H \subseteq G_k \setminus F_k$ (since $V \subseteq G_k$ and $F_k \subseteq H$), so $m(V \setminus H) \le m(G_k \setminus F_k) < 1/k$; letting $k \to \infty$ gives $m(V \setminus H) = 0$.

<1>4. (2) $\implies$ (1): write $V = \bigcap_m G_m$ and $H = \bigcup_m F_m$ with $G_m$ open decreasing and $F_m$ closed increasing.
    Proof: any $G_\delta$ is an intersection of open sets (take finite intersections to make them decreasing); similarly for $F_m$.

<1>5. $\mu(G_m \setminus V) \to 0$ and $\mu(H \setminus F_m) \to 0$ as $m \to \infty$.
    Proof: continuity from above for $G_m \downarrow V$ (all have finite measure, $E$ bounded), and continuity from below for $F_m \uparrow H$ (with $m(H) \le m(V) < \infty$).

<1>6. Given $\eps > 0$, choose $m$ with $m(G_m \setminus V) < \eps/2$ and $m(H \setminus F_m) < \eps/2$; set $G = G_m$ and $F = F_m$; then $F \subseteq E \subseteq G$ and $m(G \setminus F) \le m(G \setminus V) + m(V \setminus H) + m(H \setminus F) < \eps$.
    Proof: $F_m \subseteq H \subseteq E \subseteq V \subseteq G_m$; the triangle inequality for measures via the three-set decomposition, with $m(V \setminus H) = 0$.

<1>7. Q.E.D.
    Proof: <1>1–<1>3 give (1) $\implies$ (2) and <1>4–<1>6 give (2) $\implies$ (1).
:::
