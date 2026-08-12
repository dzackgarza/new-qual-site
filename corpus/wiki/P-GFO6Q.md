---
schema: qual/card@1
id: P-GFO6Q
kind: problem
title: "Let $R$ be an algebra over $\\CC$ which is finite-dimensional as a $\\CC\\dash$\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Let $R$ be an algebra over $\CC$ which is finite-dimensional as a $\CC\dash$vector space. Recall that an ideal $I$ of $R$ can be considered as a $\CC\dash$subvector space of $R$. We define the codimension of $I$ in $R$ to be 
\[
\codim_R I \da 
\dim_{\CC} R - \dim_{\CC} I
,\] 
the difference between the dimension of $R$ as a $\CC\dash$vector space, $\dim_{\CC} R$, and the dimension of $I$ as a $\CC\dash$vector space, $\dim_\CC I$.

a.
Show that any maximal ideal $m \subset R$ has codimension 1 .

b.
Suppose that $\operatorname{dim}_{\CC} R=2$. Show that there exists a surjective homomorphism of $\CC\dash$algebras from the polynomial ring $\CC[t]$ to $R$.

c.
Classify such algebras $R$ for which $\dim_{\CC} R=2$, and list their maximal ideals.

> (DZG): my impression is that this is an unusually difficult problem, or was something specifically covered in this year's qual class.


:::{.solution .foldopen}
**Part a**:
Since $I$ is proper, we have $\codim_R I \geq 1$ since $\codim_R I = 0 \implies I = R$ since $I\leq R$ is a vector subspace of the same dimension.
We also have $\codim_R I \leq \dim_\CC R$, and noting that $\codim_R I = \dim_\CC R \iff \dim_\CC I = \dim_\CC R$ and if $I$ is maximal it is necessarily proper, we in fact have $\codim_R I < \dim_\CC R$, so
\[
1 \leq \codim_R I \leq \dim_\CC R - 1
.\]
Now if $\codim_R I \geq 2$, then $\dim_\CC I \leq \dim_\CC R - 2$.
Choosing a basis $\ts{v_1,\cdots, v_n}$ for $R$ as a $\CC\dash$vector space induces a basis $\ts{v_1,\cdots, v_k}$ on $I$ for some $k\leq n-2$.
But then $I' \da \gens{v_1,\cdots, v_k, v_{k+1}}$ is a proper $\CC\dash$vector subspace of $R$ containing $I$, contradicting maximality of $I$.
So $\codim_R I < 2$, forcing $\codim_R I = 1$.

**Part b**:
Choose a vector space basis $\ts{v_1, v_2}$ for $R$ and define a map
\[
\phi: \CC[t] &\to R \\
1 & \mapsto v_1 \\
t & \mapsto v_2
,\]
extended by linearity.


**Part c**:
???


:::
