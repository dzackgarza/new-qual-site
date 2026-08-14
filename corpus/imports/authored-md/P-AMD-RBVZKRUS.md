---
schema: qual/card@1
id: P-AMD-RBVZKRUS
kind: problem
title: "Show that $L^2([0, 1]) \u2286 L^1([0, 1])$ and argue that $L^2([0, 1])$ in fact forms a dense subset of $L^1([0, 1])$."
classification:
  areas:
  - real-analysis
  topics:
  - riesz-representation
  - lp-spaces
  - density
relations: []
review: draft
---

::: {.problem}
a.  Show that $L^2([0, 1]) ⊆ L^1([0, 1])$ and argue that $L^2([0, 1])$ in fact forms a dense subset of $L^1([0, 1])$.

b.  Let $Λ$ be a continuous linear functional on $L^1([0, 1])$.
  
    Prove the Riesz Representation Theorem for $L^1([0, 1])$ by following the steps below:


    i. Establish the existence of a function $g ∈ L^2([0, 1])$ which represents $Λ$ in the sense that
    $$
    Λ(f ) = f (x)g(x) dx \text{ for all } f ∈ L^2([0, 1]).
    $$

    > Hint: You may use, without proof, the Riesz Representation Theorem for $L^2([0, 1])$.

    ii. Argue that the $g$ obtained above must in fact belong to $L^∞([0, 1])$ and represent $Λ$ in the sense that
    $$
    \Lambda(f)=\int_{0}^{1} f(x) \overline{g(x)} d x \quad \text { for all } f \in L^{1}([0,1])
    $$
    with
    $$
    \|g\|_{L^{\infty}([0,1])}=\|\Lambda\|_{L^{1}([0,1])\dual}
    $$
:::
