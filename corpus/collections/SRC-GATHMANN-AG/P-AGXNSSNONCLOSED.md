---
schema: qual/card@1
id: P-AGXNSSNONCLOSED
kind: problem
title: Failure of $I(V(J)) = \sqrt J$ over a field that is not algebraically closed
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nullstellensatz
  - Maximal Ideals
  - Counterexamples
relations: []
review: draft
---

::: problem
Let $J \normal k[x_1, \cdots, x_n]$ be an ideal, and find a counterexample to $I(V(J)) =\sqrt{J}$ when $k$ is not algebraically closed.
:::

::: solution
Take $J = \gens{x^2+1} \normal \RR[x]$, noting that $J$ is nontrivial and proper but $\RR$ is not algebraically closed.
Then $V(J) \subseteq \RR$ is empty, so $I(V(J)) = I(\emptyset)$.

**Claim**: $I(V(J)) = \RR[x]$.

For any set $X \subset \AA^n/k$,
\[
I(X) = \ts{f\in \RR[x] \st \forall x\in X,\, f(x)=0}
,\]
and so vacuously
\[
I(\emptyset) = \ts{f\in \RR[x] \st \forall x\in \emptyset,\, f(x)=0} = \ts{f\in \RR[x]} = \RR[x]
.\]

**Claim**: $\sqrt{J} \neq \RR[x]$.

Maximal ideals are radical, and $\RR[x]/ J \cong \CC$ being a field implies $J$ is maximal.
In this case $\sqrt{J} = J \neq \RR[x]$.

That maximal ideals are radical follows because if $J\normal R$ is maximal, then $J \subset \sqrt{J} \subset R$, forcing $\sqrt{J} = J$ or $\sqrt{J}=R$.
But if $\sqrt{J}=R$, then
\[
1\in \sqrt{J} \implies 1^n \in J \text{ for some }n \implies 1 \in J \implies J=R
,\]
contradicting that $J$ is maximal and thus proper.
:::
