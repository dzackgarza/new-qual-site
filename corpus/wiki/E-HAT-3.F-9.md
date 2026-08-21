---
schema: qual/card@1
id: E-HAT-3.F-9
kind: exercise
title: "Spliced exact sequences for $p$-primary components"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
solved: false
---

For an abelian group $A$ let $p: A \to A$ be multiplication by $p$, and let ${}_pA = \ker p$, $pA = \operatorname{im} p$, and $A_p = \operatorname{coker} p$ as in the proof of Proposition 3F.12. Show that the six-term exact sequences involving $\operatorname{Hom}(-, \mathbb{Z})$ and $\operatorname{Ext}(-, \mathbb{Z})$ associated to the short exact sequences $0 \to {}_pA \to A \to pA \to 0$ and $0 \to pA \to A \to A_p \to 0$ can be spliced together to yield an exact sequence

$$\operatorname{Hom}(pA, \mathbb{Z}) \to \operatorname{Ext}(A_p, \mathbb{Z}) \to \operatorname{Ext}(A, \mathbb{Z}) \xrightarrow{p} \operatorname{Ext}(A, \mathbb{Z}) \to \operatorname{Ext}({}_pA, \mathbb{Z}) \to 0$$

where the map labeled "$p$" is multiplication by $p$.
Use this to show:

(a) $\operatorname{Ext}(A, \mathbb{Z})$ is divisible if $A$ is torsionfree.

(b) $\operatorname{Ext}(A, \mathbb{Z})$ is torsionfree if $A$ is divisible, and the converse holds if $\operatorname{Hom}(A, \mathbb{Z}) = 0$.
