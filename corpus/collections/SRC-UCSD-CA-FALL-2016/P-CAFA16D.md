---
schema: qual/card@1
id: P-CAFA16D
kind: problem
title: "An analytic function on the disk vanishing on an arc of the boundary is identically zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f: \overline{\mathbb{D}} \to \mathbb{C}$ be a continuous function which is analytic on $\mathbb{D}$.
Assume that there exists $0 < \alpha \leq 2\pi$ such that $f(e^{i\theta}) = 0$ for all $\theta \in (0, \alpha)$.
Prove that $f(z) = 0$ for every $z \in \mathbb{D}$.
:::

::: solution
Choose a point $e^{i\theta_0}$ in the interior of the boundary arc, so $0<\theta_0<\alpha$. After a rotation, a small neighborhood of this point is carried conformally to a neighborhood of an interval of the real axis, with the disk lying on one side.

On that interval the boundary values of $f$ are identically $0$, hence real. By the Schwarz reflection principle, $f$ extends holomorphically across a smaller subarc. The extended function vanishes on that subarc, which is now a set of interior points having accumulation points. By the identity theorem, the extension is identically zero in a neighborhood of the arc.

Thus $f$ vanishes on a nonempty open subset of $\mathbb D$. Applying the identity theorem once more on the connected disk yields
\[
f\equiv0\quad\text{on }\mathbb D.
\]
:::
