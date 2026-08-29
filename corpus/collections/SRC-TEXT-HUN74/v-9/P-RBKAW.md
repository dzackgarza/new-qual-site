---
schema: qual/card@1
id: P-RBKAW
kind: problem
title: Hungerford 5.9.1
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Solvable Groups
  - Galois Theory
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.problem}
If $F$ is a radical extension field of $K$ and $E$ is an intermediate field, then $F$ is a radical extension of $E$.
:::

::: solution
**Theorem.**  
Let $F=K(\alpha_1,\dots,\alpha_n)$ be radical over $K$ and $K\subseteq E\subseteq F$.
Then there exist $\beta_1,\dots,\beta_m$ such that
$$
F=E(\beta_1,\dots,\beta_m),
$$
and for each $r$ there is $N_r>0$ with
$$
\beta_r^{N_r}\in E(\beta_1,\dots,\beta_{r-1}).
$$

*Proof.* Set
$$
S:=\{\alpha_i:\alpha_i\notin E\}.
$$

**Lemma 1.**  
There is an ordering $\alpha_{i_1},\dots,\alpha_{i_m}$ of $S$ such that
$$
F=E(\alpha_{i_1},\dots,\alpha_{i_m}).
$$

*Proof.* Because $K\subseteq E$ and $F=K(\alpha_1,\dots,\alpha_n)$, adjoin precisely the generators outside $E$ to get $F$ from $E$.
Ordering them by index gives the chain. ∎

Define
$$
E_0:=E,\qquad E_r:=E_{r-1}(\alpha_{i_r}),\ r=1,\dots,m.
$$

**Lemma 2.**  
For each $r$, there exists $N_r>0$ such that
$$
\alpha_{i_r}^{N_r}\in E_{r-1}.
$$

*Proof.* By hypothesis, there is $n_{i_r}>0$ with
$$
\alpha_{i_r}^{n_{i_r}}\in K[\alpha_1,\dots,\alpha_{i_r-1}].
$$
Every element on the right has index $<i_r$, hence belongs to $E_{r-1}$.
Set $N_r:=n_{i_r}$. ∎

**Lemma 3.**  
We have $F=E_m$.

*Proof.* By construction,
$$
E_m=E(\alpha_{i_1},\dots,\alpha_{i_m})=E(S)=F.
$$
∎

Take $\beta_r:=\alpha_{i_r}$.
Lemmas 2 and 3 produce the required radical tower. ∎
:::
