---
schema: qual/card@1
id: P-WBB2M
kind: problem
title: Intermediate fields of a $D_8$-extension with $E/F$ and $K/E$ Galois but $K/F$
  not Galois
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Let $F \subset L$ be fields such that $L/F$ is a Galois field extension with Galois group equal to $D_8 = \left< \sigma,\tau \mid \sigma^4 = \tau^2 = 1,~ \sigma\tau = \tau \sigma^3 \right>$.
Show that there are fields $F \subset E \subset K \subset L$ such that $E/F$ and $K/E$ are Galois field extensions, but $K/F$ is not Galois.
:::

::: {.solution}

The argument is the card's own, by the fundamental theorem of Galois theory; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $L/F$ be Galois with group $G=D_{8}=\langle\sigma,\tau\mid\sigma^{4}=\tau^{2}=1,\ \sigma\tau=\tau\sigma^{3}\rangle$, and put
$$
H=\langle\sigma^{2},\tau\rangle,\qquad J=\langle\tau\rangle,\qquad E=L^{H},\qquad K=L^{J}.
$$

::: pf

::: {.pf-step #subgroups}
$H\cong C_{2}\times C_{2}$, $H\trianglelefteq D_{8}$, $J\le H$ and $J\trianglelefteq H$.

::: pf-proof
$\sigma^{2}$ and $\tau$ are distinct commuting elements of order $2$ — they commute because $\sigma\tau=\tau\sigma^{3}$ gives $\sigma^{2}\tau=\tau\sigma^{6}=\tau\sigma^{2}$ — so $H=\{1,\sigma^{2},\tau,\sigma^{2}\tau\}$ is a Klein four group. Its order is $4$ and $\abs{D_{8}}=8$, so $[D_{8}:H]=2$, and a subgroup of index $2$ is normal (its complement is a single coset). $J=\{1,\tau\}\subset H$, and $H$ is abelian, so every subgroup of it is normal in it.
:::

:::

::: {.pf-step #not-normal}
$J$ is not normal in $D_{8}$.

::: pf-proof
$\sigma\tau\sigma^{-1}=\tau\sigma^{3}\sigma^{-1}=\tau\sigma^{2}$ by the relation $\sigma\tau=\tau\sigma^{3}$, and $\tau\sigma^{2}\notin\{1,\tau\}=J$ because $\sigma^{2}\ne1$. Hence $J$ is not stable under conjugation by $\sigma$ and is not normal.
:::

:::

::: {.pf-step #chain}
$F\subsetneq E\subsetneq K\subsetneq L$, and $K/F$ is the extension in question.

::: pf-proof
$H\ne D_{8}$ and $J\ne H$, so by the fundamental theorem of Galois theory, which reverses inclusions and gives $[L:L^{S}]=\abs{S}$ for each subgroup $S\le D_{8}$, the fixed fields satisfy $F=L^{D_{8}}\subsetneq L^{H}=E\subsetneq L^{J}=K\subsetneq L^{1}=L$. Also $L/F$ is Galois, hence separable and normal, so every intermediate extension $L/M$ is Galois and every intermediate field is separable over $F$.
:::

:::

::: {.pf-step #galois}
$E/F$ and $K/E$ are Galois and $K/F$ is not.

::: pf-proof
By the fundamental theorem, for a subgroup $S\le D_{8}$ the extension $L^{S}/F$ is Galois exactly when $S\trianglelefteq D_{8}$, and then its group is $D_{8}/S$; here $L/F$ is finite Galois, so the correspondence applies in both directions. Since $H\trianglelefteq D_{8}$ by step [](#subgroups){.pf-ref}, $E=L^{H}$ is Galois over $F$. Inside $L/E$, whose group is $H$, the subgroup $J$ is normal by step [](#subgroups){.pf-ref}, so $K=L^{J}$ is Galois over $E$. But $J\not\trianglelefteq D_{8}$ by step [](#not-normal){.pf-ref}, so $K$ is not Galois over $F$: $K/F$ is separable, and a separable extension is Galois exactly when it is normal, which by the correspondence fails here.
:::

:::

:::
:::
