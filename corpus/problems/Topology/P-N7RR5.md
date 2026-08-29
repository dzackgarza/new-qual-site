---
schema: qual/card@1
id: P-N7RR5
kind: problem
title: Interior of a product versus product of interiors
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Is it true that the interior of a product is the product of the interiors? Specifically, for topological spaces $X$ and $Y$ and subsets $A \subseteq X$ and $B \subseteq Y$, is $\operatorname{int}(A \times B) = \operatorname{int}(A) \times \operatorname{int}(B)$? What about infinite products?
:::

::: solution
**Goal:** Prove $\operatorname{int}(A \times B) = \operatorname{int}(A) \times \operatorname{int}(B)$ for finite products, and discuss the infinite product case.

<1>1. Finite product case: $\operatorname{int}(A \times B) = \operatorname{int}(A) \times \operatorname{int}(B)$:
    *Proof:*
    <2>1. **Inclusion $\operatorname{int}(A) \times \operatorname{int}(B) \subseteq \operatorname{int}(A \times B)$:**
        - $\operatorname{int}(A)$ is open in $X$ and $\operatorname{int}(B)$ is open in $Y$.
        - By definition of the product topology, $\operatorname{int}(A) \times \operatorname{int}(B)$ is an open set in $X \times Y$.
        - Furthermore, $\operatorname{int}(A) \times \operatorname{int}(B) \subseteq A \times B$.
        - Since $\operatorname{int}(A \times B)$ is the largest open subset of $A \times B$, we have $\operatorname{int}(A) \times \operatorname{int}(B) \subseteq \operatorname{int}(A \times B)$.
    <2>2. **Inclusion $\operatorname{int}(A \times B) \subseteq \operatorname{int}(A) \times \operatorname{int}(B)$:**
        - Let $(x, y) \in \operatorname{int}(A \times B)$.
        - By definition of the product topology, there exist open sets $U \subseteq X$ and $V \subseteq Y$ such that $(x, y) \in U \times V \subseteq A \times B$.
        - Then $x \in U \subseteq A$, which means $x \in \operatorname{int}(A)$ since $U$ is open.
        - Similarly, $y \in V \subseteq B$, which means $y \in \operatorname{int}(B)$ since $V$ is open.
        - Therefore $(x, y) \in \operatorname{int}(A) \times \operatorname{int}(B)$.
    <2>3. Combining both inclusions yields $\operatorname{int}(A \times B) = \operatorname{int}(A) \times \operatorname{int}(B)$.

<1>2. Infinite product case:
    *Proof:*
    <2>1. For an arbitrary product $\prod_{\alpha \in I} A_\alpha \subseteq \prod_{\alpha \in I} X_\alpha$:
    <2>2. **In the box topology:** The equality $\operatorname{int}\left(\prod A_\alpha\right) = \prod \operatorname{int}(A_\alpha)$ always holds, by the same argument.
    <2>3. **In the product (Tychonoff) topology:** The equality **fails** in general when infinitely many $A_\alpha$ are proper subsets with non-empty interior!
        - In the product topology, any non-empty open set $U$ must have $\pi_\alpha(U) = X_\alpha$ for all but finitely many $\alpha$.
        - If infinitely many $A_\alpha \subsetneq X_\alpha$ have $\operatorname{int}(A_\alpha) \ne \varnothing$, then $\prod \operatorname{int}(A_\alpha)$ is not open in the product topology, and in fact $\operatorname{int}\left(\prod A_\alpha\right) = \varnothing$ whenever infinitely many $A_\alpha \ne X_\alpha$.
        - Example: In $\mathbb{R}^\mathbb{N}$ with product topology, let $A_n = [0, 1]$ for all $n \in \mathbb{N}$. Then $\operatorname{int}(A_n) = (0, 1)$, but $\operatorname{int}\left(\prod_{n=1}^\infty [0, 1]\right) = \varnothing \ne \prod_{n=1}^\infty (0, 1)$.

<1>3. Conclusion:
    Yes, $\operatorname{int}(A \times B) = \operatorname{int}(A) \times \operatorname{int}(B)$ is true for any finite product, but fails for infinite products under the standard product topology. Q.E.D.
:::
