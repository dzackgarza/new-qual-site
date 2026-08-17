---
schema: qual/card@1
id: P-YFOG7
kind: problem
title: "The splitting field of this polynomial is $\\QQ(\\sqrt[3]2, \\sqrt 3, \\zeta_3)$ where $\\zeta_3$ is a\u2026"
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - splitting-fields
  - field-extensions
relations: []
review: draft
solved: false
---

::: problem
The splitting field of this polynomial is $\QQ(\sqrt[3]2, \sqrt 3, \zeta_3)$ where $\zeta_3$ is a primitive third root of unity.

To get the degree of this extension, we extend fields in the indicated order.
Since $\QQ(\sqrt[3] 2, \sqrt 3)$ is totally real, the minimal polynomial of $\zeta$ over it still has degree $\phi(3) = 2$.
A quick check also shows that $\sqrt 3$ is not contained in $\QQ(\sqrt[3] 2)$, yielding another degree 2 extension, and finally a degree 3 extension.

Thus we have an extension of degree 12, and since we've constructed a Galois extension $L$ (a separable splitting field), if we define $G \definedas \Gal(\QQ/L)$, we have $\abs G = 12$.
Since we know that the splitting field of $\QQ(\sqrt[3] 2)/ \QQ$ has Galois group $D_3$, we must have $D_3 \leq G$.
This reduces the possibilities just $D_3 \cross \ZZ_2 \cong D_6$.

We have the following subgroup diagram (Figure 1).

![Subgroup Diagram](../../assets/10_Algebra/500_Exercises/PSets/PSet%206/figures/2019-10-24-10%3A23.png)\

where we can simplify things by only considering conjugacy classes of subgroups, since these will correspond to conjugate field extensions (Figure 2).

![Subgroups up to Conjugacy](../../assets/10_Algebra/500_Exercises/PSets/PSet%206/figures/2019-10-24-11%3A25.png)\

We can explicitly identify the relevant automorphisms:
\[
\begin{align*}
\sigma: \sqrt[3] 2 \mapsto \zeta_3 \sqrt[3] 2 \\
\tau: \zeta_3 \mapsto \zeta_3^2 \\
\gamma: \sqrt 3 \mapsto -\sqrt 3
.\end{align*}
\]
We can then present $G = \generators{\sigma, \gamma, \tau \mid \sigma^3 = \tau^2 = \gamma^2 = (\sigma\tau)^2 = [\sigma, \gamma] = [\tau, \gamma] = e}$, and obtain the following lattice:

\begin{tikzcd}
                                            &  & {<\sigma, \tau, \gamma>}                       &                                                         &                                      &  &                                                 \\
                                            &  &                                                &                                                         &                                      &  &                                                 \\
<\tau> \times <\gamma> \arrow[rruu, dashed] &  & {<\sigma, \tau>} \arrow[uu]                    &                                                         & {<\sigma, \tau\gamma>} \arrow[lluu]  &  & <\sigma> \times <\gamma> \arrow[lllluu]         \\
                                            &  &                                                &                                                         &                                      &  &                                                 \\
<\tau> \arrow[uu] \arrow[rruu, dashed]      &  & <\tau\gamma> \arrow[rruu, dashed] \arrow[lluu] &                                                         & <\gamma> \arrow[rruu] \arrow[lllluu] &  & <\sigma> \arrow[uu] \arrow[lluu] \arrow[lllluu] \\
                                            &  &                                                &                                                         &                                      &  &                                                 \\
                                            &  &                                                & <e> \arrow[llluu] \arrow[luu] \arrow[ruu] \arrow[rrruu] &                                      &  &                                                
\end{tikzcd}

which, up to conjugacy, fix the following intermediate field extensions (Figure 3).

![Intermediate Field Extensions up to Conjugacy](../../assets/10_Algebra/500_Exercises/PSets/PSet%206/figures/2019-10-24-12%3A12.png)\

$\qed$
:::
