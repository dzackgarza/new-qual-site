---
schema: qual/card@1
id: P-M3BT5
kind: problem
title: A radical extension is radical over any intermediate field
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Solvable Groups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: problem
Suppose $F = K[\alpha_1, \cdots, \alpha_n]$ where $\alpha_1^{n_1} \in K$ for some $n_1$ and for each $i$ we have $\alpha_i^{n_i} \in K[\alpha_1, \cdots \alpha_{i-1}]$ for some powers $n_i$.
We want to show that $F = E[\beta_1, \cdots \beta_m]$ where each $\beta_i$ satisfies a similar condition.
:::

::: solution
**Theorem.**  
Let $F=K(\alpha_1,\dots,\alpha_n)$ be radical over $K$.  
If $K\subseteq E\subseteq F$, then there are elements
$$\beta_1,\dots,\beta_m\in F$$
such that
$$
F=E(\beta_1,\dots,\beta_m),\qquad \beta_r^{N_r}\in E(\beta_1,\dots,\beta_{r-1})\text{ for some }N_r>0.
$$

**Proof.**  
Set
$$
S:=\{\alpha_i:\alpha_i\notin E\}.
$$

**Lemma 1.**  
There is a unique ordering
$$\alpha_{i_1},\alpha_{i_2},\dots,\alpha_{i_m}\qquad(i_1<\cdots<i_m)$$
of $S$ such that
$$
F=E(\alpha_{i_1},\dots,\alpha_{i_m}).
$$

*Proof.* Because $K\subseteq E$ and $F=K(\alpha_1,\dots,\alpha_n)$, every generator in $S$ is needed to adjoin to $E$.
Listing the elements of $S$ in increasing original index order gives the stated chain. ∎

Define
$$E_0:=E,\qquad E_r:=E_{r-1}(\alpha_{i_r}),\ r=1,\dots,m.$$

**Lemma 2.**  
For each $r\in\{1,\dots,m\}$, there exists $N_r>0$ with
$$
\alpha_{i_r}^{N_r}\in E_{r-1}.
$$

*Proof.*  
By hypothesis on the original tower,
$$
\alpha_{i_r}^{n_{i_r}}\in K[\alpha_1,\dots,\alpha_{i_r-1}]
$$
for some integer $n_{i_r}>0$.
Every factor on the right has index $<i_r$, so it belongs to $E_{r-1}$:
either it is already in $E$ or equals $\alpha_{i_t}$ with $t<r$.
Hence
$$
\alpha_{i_r}^{n_{i_r}}\in E_{r-1}.
$$
Set $N_r:=n_{i_r}$. ∎

**Lemma 3.**  
We have $F=E_m$.

*Proof.*  
By definition of the $E_r$,
$$
E_m=E(\alpha_{i_1},\dots,\alpha_{i_m})=E(S).
$$
Since $S$ is exactly the set of generators removed from $K(\alpha_1,\dots,\alpha_n)$ when passing from $K$ to $E$, $E(S)=F$. ∎

Take $\beta_r:=\alpha_{i_r}$ for $r=1,\dots,m$.
By Lemma 2 each radical step is over the previous field, and by Lemma 3 the full extension is $E_m=F$. ∎
:::
