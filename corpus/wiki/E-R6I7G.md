---
schema: qual/card@1
id: E-R6I7G
kind: exercise
title: "Prove the \"recognizing direct products\" theorem. Can the\u2026"
classification:
  areas:
  - algebra
  topics:
  - direct-products
  - normal-subgroups
relations: []
review: draft
---
:::{.exercise title="?"}
Prove the "recognizing direct products" theorem.
Can the conditions be relaxed?
:::

:::{.remark}
Things are particularly nice when the orders of $H$ and $k$ are coprime.
For 3, $x\in H \intersect K$ implies that the order of $x$ divides $\gcd(\size H, \size K) = 1$, so $H \intersect K = \ts{e}$.
Thus for 2, one only needs that $\size(HK) = \size G$.
:::

:::{.proof title="?"}
With these conditions, the following map is an isomorphism:
\[
\Gamma: H\cross K &\to G \\
(h, k) &\mapsto hk
.\]

- This is a group morphism by condition (1):
\[
\Gamma(h_1, k_1) \Gamma(h_2, k_2) 
&\da (h_1 k_1) (h_2 k_2) = h_1 ({ \color{red} k_1 h_2 } ) k_2 \\
&= h_1 ( { \color{red} h_2 k_1 } ) k_2 \\
&= (h_1 h_2) ( k_1 k_2) \\
&\da \Gamma( (h_1, k_1)(h_2, k_2) )
.\]
- This is surjective by condition (2)
- This is injective by condition(3) and checking the kernel:
\[
\ker \Gamma = \ts{ (h,k) \st hk = 1_G,\, hk = 1_G} \implies h = k ^{-1} \implies hk \in K \intersect H = \ts{1_G}
.\]

:::
