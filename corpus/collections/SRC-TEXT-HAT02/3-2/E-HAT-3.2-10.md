---
schema: qual/card@1
id: E-HAT-3.2-10
kind: problem
title: Failure of the Künneth cross product for infinite discrete spaces
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 10; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the counterexample: for discrete $X$ the cross product in degree zero is
    $\operatorname{Map}(X,\ZZ)\otimes\operatorname{Map}(Y,\ZZ)\to\operatorname{Map}(X\times Y,\ZZ)$,
    and the function $\delta_{ij}$ on a countable rectangle is not a finite sum of products because
    an $N$-term sum has rank at most $N$ on every finite submatrix.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 10 (p.229) including the bracketed remark about Theorem 3.15. Rechecked the counterexample: for discrete X and Y, H^0 is Map(X,Z) = product of copies of Z, the degree-zero cross product is f tensor g -> ((x,y) -> f(x)g(y)), and the function delta_ij on a countable rectangle is not a finite sum of such products since a sum of N terms has rank at most N on each finite submatrix while the (N+1)x(N+1) identity minor has rank N+1. Neither space is finitely generated in degree 0, which is why Theorem 3.15 does not apply. Citations added: the discreteness of the cochain complex and Theorem 3.15 p.216. Not covered: nothing about the higher cross products, cohomology vanishing above degree 0.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the counterexample, which is what Queue D asks for on this card. The vanishing of the higher cohomology of a discrete space is now a step with the boundary formula for constant simplices written out; the degree-zero form of the cross product is a step; the witness and the rank count are a step; and the conclusion records which hypothesis of Theorem 3.15 the example violates. No retained set covers this exercise; the card now says so. Locators checked: Theorem 3.15 on printed p. 216, the exercise on printed p. 229. No statement repair.
---

::: {.problem}
Show that the cross product map $H^*(X; \ZZ) \otimes H^*(Y; \ZZ) \to H^*(X \times Y; \ZZ)$ is not an isomorphism if $X$ and $Y$ are infinite discrete sets.
[This shows the necessity of the hypothesis of finite generation in Theorem 3.15.]
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout reach §3.2 in Li (exercises 1, 2, 3, 4, 6 and 11) and Sam (1, 4, 11), and neither holds exercise 10. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §3.2 Exercise 10, printed p. 229, and it shows that the finite-generation hypothesis of Theorem 3.15, printed p. 216, cannot be dropped.

::: pf

::: {.pf-step #discrete-cohomology}
For a discrete space $X$, $H^0(X;\ZZ)=\operatorname{Map}(X,\ZZ)=\prod_{x\in X}\ZZ$ and $H^n(X;\ZZ)=0$ for $n>0$.

::: pf-proof
A singular $n$-simplex into a discrete space is constant, so $C_n(X;\ZZ)$ is the free abelian group on the points of $X$ for every $n\ge0$, and the boundary is $\partial\sigma=\sum_{i=0}^n(-1)^i\sigma$, which is $\sigma$ for $n$ even and $0$ for $n$ odd, because all faces of a constant simplex are that simplex. Taking the dual complex with $\delta$ the transpose of $\partial$: in degree $0$ the map $\delta_0=\partial_1^*=0$, so $H^0=\operatorname{Hom}(C_0,\ZZ)=\operatorname{Map}(X,\ZZ)$; and for $n\ge1$ the differentials alternate between an isomorphism and zero, so $\ker\delta_n=\operatorname{im}\delta_{n-1}$ and $H^n=0$.
:::

:::

::: {.pf-step #degree-zero}
The cross product $H^*(X;\ZZ)\otimes H^*(Y;\ZZ)\to H^*(X\times Y;\ZZ)$ is, in degree zero, the map $\operatorname{Map}(X,\ZZ)\otimes\operatorname{Map}(Y,\ZZ)\to\operatorname{Map}(X\times Y,\ZZ)$ sending $f\otimes g$ to $(x,y)\mapsto f(x)g(y)$.

::: pf-proof
By step [](#discrete-cohomology){.pf-ref} both sides are concentrated in degree zero, and there the cross product is $p_X^*a\smile p_Y^*b$ with $p_X,p_Y$ the projections of $X\times Y$; pulling a function back along a projection is precomposition, and the cup product of two degree-zero classes is their pointwise product, which gives the stated formula.
:::

:::

::: {.pf-step #witness}
There is a function $h\in\operatorname{Map}(X\times Y,\ZZ)$ that is not in the image of the cross product.

::: pf-proof
Take countably infinite subsets $\{x_i\}_{i\ge1}\subset X$ and $\{y_j\}_{j\ge1}\subset Y$ and set $h(x_i,y_j)=\delta_{ij}$, with $h=0$ at every other point of $X\times Y$. Suppose $h$ were in the image; an element of the tensor product is a finite sum $\sum_{r=1}^N f_r\otimes g_r$, so on the countable rectangle we would have $\delta_{ij}=\sum_{r=1}^Na_r(i)b_r(j)$ for all $i,j$, where $a_r(i)=f_r(x_i)$ and $b_r(j)=g_r(y_j)$. The $(N+1)\times(N+1)$ block of the matrix $(\delta_{ij})$ is then the product of the $(N+1)\times N$ matrix $(a_r(i))$ with the $N\times(N+1)$ matrix $(b_r(j))$, hence has rank at most $N$; but that block is the identity matrix, of rank $N+1$. This contradiction shows that $h$ is not in the image.
:::

:::

::: {.pf-step #not-iso}
The cross product is not an isomorphism for infinite discrete $X$ and $Y$.

::: pf-proof
It is not surjective, by step [](#witness){.pf-ref}, so it is not an isomorphism; and this is exactly the failure that the finite-generation hypothesis on one factor in Theorem 3.15, printed p. 216, rules out.
:::

:::

:::
:::
