---
schema: qual/card@1
id: P-Q7WNK
kind: problem
title: Equivalent approximation of Borel sets by open and closed sets versus $G_\delta$
  and $F_\sigma$ sets for a finite Borel measure on $\RR^n$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: problem
Let $\mu$ be a finite Borel measure on $\RR^n$ and $E$ be a Borel subset of $\RR^n$.
Prove that the following two statements are equivalent:

1. For any $\varepsilon > 0$, there exists an open set $G$ and closed set $F$ such that
$$
F \subseteq E \subseteq G \quad \text{and} \quad \mu(G\setminus F) < \varepsilon.
$$

2. There exists a $G_\delta$ set $V$ and an $F_\sigma$ set $H$ such that
$$
H \subseteq E \subseteq V \quad \text{and}\quad \mu(V\setminus H) = 0.
$$
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (1) $\Rightarrow$ (2). Proof: for each $k \in \NN$, (1) with $\eps = 1/k$ gives open $G_k$ and closed $F_k$ with $F_k \subseteq E \subseteq G_k$ and $\mu(G_k \setminus F_k) < 1/k$.
Set $V = \cap_k G_k \in G_\delta$ and $H = \cup_k F_k \in F_\sigma$; then $H \subseteq E \subseteq V$.
Moreover $V \setminus H \subseteq G_k \setminus F_k$ for every $k$ (since $V \subseteq G_k$ and $H \supseteq F_k$), so $\mu(V \setminus H) \le \mu(G_k \setminus F_k) < 1/k$ for all $k$, hence $\mu(V \setminus H) = 0$.
<1>2. (2) $\Rightarrow$ (1). Proof: let $V = \cap_k V_k$ with $V_k$ open, $H = \cup_k H_k$ with $H_k$ closed, $H \subseteq E \subseteq V$, $\mu(V \setminus H) = 0$.
Given $\eps > 0$: the sets $V \setminus \cap_{k\le m} V_k$ decrease to $V \setminus V = \emptyset$, so by continuity from above $\mu(V \setminus \cap_{k\le m}V_k) \to 0$; choose $m$ with $\mu(V \setminus G) < \eps/2$ for $G = \cap_{k \le m} V_k$ (open, $E \subseteq G$). Similarly $\cup_{k\le m}H_k \nearrow H$, so $\mu(V \setminus \cup_{k\le m}H_k) \to \mu(V \setminus H) = 0$; choose $n$ with $\mu(V \setminus F) < \eps/2$ for $F = \cup_{k\le n}H_k$ (closed, $F \subseteq E$). Then \[ \mu(G \setminus F) \le \mu(G \setminus V) + \mu(V \setminus F) < \eps/2 + \eps/2 = \eps . \] <1>3. Q.E.D.
:::
