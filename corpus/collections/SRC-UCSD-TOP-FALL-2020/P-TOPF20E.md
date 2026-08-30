---
schema: qual/card@1
id: P-TOPF20E
kind: problem
title: "No retraction of S^n x S^n onto the coordinate axes union"
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Cohomology
  - Spheres
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
For $n \geq 1$, take a point $p \in S^n$ and consider the subspace $A = \{(x, y) \in S^n \times S^n \mid x = p \text{ or } y = p\}$ of $S^n \times S^n$.
Show that there does not exist a retraction of $S^n \times S^n$ to $A$.
:::

::: solution
**Goal:** Show that no retraction $r:S^n \times S^n\to A$ exists.

<1> Assume a retraction $r$ exists.
    *Proof:*
    <2>1. Let $i:A\hookrightarrow S^n\times S^n$ be the inclusion. Then $r\circ i=\id_A$.
    <2>2. Passing to reduced cohomology gives a left inverse:
        $$r^*\circ i^*=\id_{ \widetilde H^\ast(A)}.$$
        Hence $i^*$ is injective.

<1>1. Compute degree-$2n$ cohomology on the ambient product.
    *Proof:*
    <2>1. By the Künneth theorem,
        $$\widetilde H^{2n}(S^n\times S^n;\ZZ)\cong \ZZ.$$

<1>3. Compute degree-$2n$ cohomology on the subspace $A$.
    *Proof:*
    <2>1. $A=(S^n\times\{p\})\cup(\{p\}\times S^n)$ with contractible intersection $\{(p,p)\}$.
    <2>2. By Mayer--Vietoris, $A$ is homotopy equivalent to $S^n\vee S^n$.
    <2>3. Therefore
        $$\widetilde H^{2n}(A;\ZZ)=\widetilde H^{2n}(S^n\vee S^n;\ZZ)=0,$$
        since $\dim S^n\vee S^n=n$.

<1>4. Conclude by contradiction.
    *Proof:*
    <2>1. Since $i^*$ is injective, its target cannot be zero while its source is $\ZZ$.
    <2>2. But $i^*:\widetilde H^{2n}(S^n\times S^n)\to \widetilde H^{2n}(A)$ would map
        $\ZZ\to 0$.
    <2>3. Contradiction.

<1>5. Therefore no such retraction exists for $n\ge1$.

Authored by **Codex 5.3 Spark Extra High**.
:::
