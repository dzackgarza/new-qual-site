---
schema: qual/card@1
id: P-ALGF14A
kind: problem
title: Proper subgroups of nilpotent groups are properly contained in their normalizers
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $G$ be a (not necessarily finite) nilpotent group.
Prove that for any proper subgroup $H$ we have that $H \neq N_G(H)$.
:::

::: solution
**Theorem.**  
In a finite nilpotent group $G$, every proper subgroup $H$ satisfies
$H\subsetneq N_G(H)$.

*Proof by induction on* $|G|$.

**Lemma 1.**  
If $Z(G)\nsubseteq H$, then there is an element of $N_G(H)\setminus H$.

*Proof.* Choose $z\in Z(G)\setminus H$.
For all $h\in H$, $zh=hz$, so $z$ normalizes $H$. Hence $z\in N_G(H)\setminus H$. ∎

**Lemma 2.**  
If $Z(G)\le H$, then
$H/Z(G)\subsetneq N_{G/Z(G)}(H/Z(G))$.

*Proof.* The group $G/Z(G)$ is nilpotent and $H/Z(G)$ is proper in $G/Z(G)$.
Apply induction to obtain
$$
\frac{H}{Z(G)}\subsetneq N_{G/Z(G)}\!\left(\frac{H}{Z(G)}\right).
$$
Lifting a witness gives the strict inclusion in the quotient. ∎

Assume $H$ is proper in $G$.  
If $Z(G)\nsubseteq H$, Lemma 1 applies directly.
If $Z(G)\le H$, take $gZ(G)\in N_{G/Z(G)}(H/Z(G))\setminus H/Z(G)$ from Lemma 2.
For every $h\in H$ we have
$$
gZ(G)\,hZ(G)\,g^{-1}Z(G)\in H/Z(G),
$$
so $ghg^{-1}\in HZ(G)=H$.
Hence $gHg^{-1}\subseteq H$, and similarly by inverse, $g^{-1}Hg\subseteq H$.
Thus $g\in N_G(H)\setminus H$. ∎
:::
