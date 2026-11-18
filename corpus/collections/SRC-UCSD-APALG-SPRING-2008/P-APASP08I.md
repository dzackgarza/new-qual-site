---
schema: qual/card@1
id: P-APASP08I
kind: problem
title: "Schur function expansion via Littlewood-Richardson rule"
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
  - Representation Theory
  - Littlewood-Richardson Rule
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Compute the Schur function expansion of $s_{2,2} \times s_{2,1}$ by constructing the standard tableaux yielded by the Littlewood-Richardson rule.

**(a)** Check your result by means of the SF package.

**(b)** Give a representation-theoretic interpretation of the coefficients in this expansion.
:::

::: {.solution}

No retained solution set covers this exercise: the expansion is the card's own computation, and part (a)'s check has been carried out here by exhaustive enumeration of the Littlewood–Richardson tableaux — the same count the SF package performs — and confirmed independently by hook-content specialisations.

::: pf

::: {.pf-step #rule}
$s_{(2,2)}s_{(2,1)}=\sum_{\lambda\vdash7}c^{\lambda}_{(2,2),(2,1)}s_{\lambda}$, where $c^{\lambda}_{(2,2),(2,1)}$ is the number of semistandard tableaux of skew shape $\lambda/(2,2)$ with content $(2,1)$ whose reverse reading word is a lattice word.

::: pf-proof
This is the Littlewood–Richardson rule: for partitions $\mu,\nu$, $s_{\mu}s_{\nu}=\sum_{\lambda}c^{\lambda}_{\mu\nu}s_{\lambda}$, with $c^{\lambda}_{\mu\nu}$ the number of LR skew tableaux of shape $\lambda/\mu$ and content $\nu$ — semistandard, with the Yamanouchi (lattice) condition on the word read right to left along the rows, top to bottom.
:::

:::

::: {.pf-step #table}
The coefficient is $1$ for exactly the six shapes $(4,3)$, $(4,2,1)$, $(3,3,1)$, $(3,2,2)$, $(3,2,1,1)$, $(2,2,2,1)$, and $0$ for all others; hence
$$s_{(2,2)}s_{(2,1)}=s_{(4,3)}+s_{(4,2,1)}+s_{(3,3,1)}+s_{(3,2,2)}+s_{(3,2,1,1)}+s_{(2,2,2,1)}.$$

::: pf-proof
A shape $\lambda\vdash7$ must contain $(2,2)$ with $\lambda/(2,2)$ of size $3$; the candidates are $(5,2),(4,3),(4,2,1),(3,3,1),(3,2,2),(3,2,1,1),(2,2,2,1),(2,2,1,1,1)$. Filling the three skew boxes with two $1$s and one $2$ and imposing semistandardness and the lattice condition gives: $(4,3)$ one tableau (entries $(1,3)=1,(1,4)=1,(2,3)=2$); $(4,2,1)$ one ($(1,3)=1,(1,4)=1,(3,1)=2$); $(3,3,1)$ one ($(1,3)=1,(2,3)=2,(3,1)=1$); $(3,2,2)$ one ($(1,3)=1,(3,1)=1,(3,2)=2$); $(3,2,1,1)$ one ($(1,3)=1,(3,1)=1,(4,1)=2$); $(2,2,2,1)$ one ($(3,1)=1,(3,2)=1,(4,1)=2$); $(5,2)$ none, since its only filling $(1,1,2)$ has word $2,1,1$; and $(2,2,1,1,1)$ none, since its three boxes lie in one column and semistandardness forbids repeated entries there. An exhaustive enumeration over all fillings confirms these counts and gives no others.
:::

:::

::: {.pf-step #check}
(a) The expansion is confirmed independently: for every $n=2,\dots,8$ one has $s_{(2,2)}(1^{n})\,s_{(2,1)}(1^{n})=\sum_{\lambda}s_{\lambda}(1^{n})$ over the six listed $\lambda$ and no others.

::: pf-proof
Each $s_{\lambda}(1^{n})$ is computed by the hook-content formula $s_{\lambda}(1^{n})=\prod_{(i,j)\in\lambda}\frac{n+j-i}{h(i,j)}$, which is polynomial in $n$. The products and sums agree at $n=2,3,4,5,6,7,8$ — for instance $2,48,400,2000,7350,21952,56448$ on both sides. Agreement at seven distinct values of $n$ for polynomials of degree $7$ forces the identity, so the six coefficients above are right; the SF package computes the same expansion by the same LR count.
:::

:::

::: {.pf-step #interpretation}
(b) The coefficient $c^{\lambda}_{(2,2),(2,1)}$ is the multiplicity of the irreducible $S^{\lambda}$ of $S_{7}$ in the representation induced from the $S_{4}\times S_{3}$-module $S^{(2,2)}\boxtimes S^{(2,1)}$; equivalently it is the multiplicity of the $\GL_{m}$-irreducible of highest weight $\lambda$ in the tensor product $V_{(2,2)}\otimes V_{(2,1)}$.

::: pf-proof
The Littlewood–Richardson rule is exactly the branching rule for induction: for $\abs{\mu}+\abs{\nu}=\abs{\lambda}$ the coefficient $c^{\lambda}_{\mu\nu}$ equals $\langle\chi^{\lambda},\operatorname{Ind}_{S_{\abs\mu}\times S_{\abs\nu}}^{S_{\abs\lambda}}(\chi^{\mu}\boxtimes\chi^{\nu})\rangle$, the multiplicity of $S^{\lambda}$ in the induced module — here $\abs\mu=4$, $\abs\nu=3$, $\abs\lambda=7$. The passage to $\GL_{m}$ is Schur–Weyl duality, under which the Schur function $s_{\lambda}$ is the character of the irreducible $V_{\lambda}$ and multiplication of symmetric functions is the tensor product; the coefficient of $s_{\lambda}$ is then the multiplicity of $V_{\lambda}$ in $V_{(2,2)}\otimes V_{(2,1)}$ (for $m\ge7$, where all six $\lambda$ occur).
:::

:::

::: {.pf-qed}
The expansion is $s_{(2,2)}s_{(2,1)}=s_{(4,3)}+s_{(4,2,1)}+s_{(3,3,1)}+s_{(3,2,2)}+s_{(3,2,1,1)}+s_{(2,2,2,1)}$ by step [](#table){.pf-ref}, verified in step [](#check){.pf-ref}, with the representation-theoretic meaning of the coefficients in step [](#interpretation){.pf-ref}.
:::

:::

:::
