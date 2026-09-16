---
schema: qual/card@1
id: P-AGH448ALGEBRAICFUNDAMENTALGROUP
kind: problem
title: The algebraic fundamental group of an elliptic curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Riemann-Hurwitz
relations: []
review: draft
---

::: {.problem}
For any curve $X$, the **algebraic fundamental group** $\pi_1(X)$ is defined as $\cocolim \operatorname{Gal}(K'/K)$, where $K$ is the function field of $X$, and $K'$ runs over all Galois extensions of $K$ such that the corresponding curve $X'$ is étale over $X$ (III, Ex. 10.3).

Thus, for example, $\pi_1(\PP^1)=1$. (See 2.5.3)

Show that for an elliptic curve $X$,
$$
\pi_1(X) =
\begin{cases}
\Prod_{\ell \text{ prime}} \ZZ_\ell \times \ZZ_\ell & \characteristic k = 0,
\\ \\
\Prod_{\ell\neq p} \ZZ_\ell \times \ZZ_\ell & \characteristic k = p \text{ and } \Hasse X = 0,
\\ \\
\ZZ_p \times \Prod_{\ell\neq p} \ZZ_\ell \times \ZZ_\ell & \characteristic k = p \text{ and } \Hasse X \neq 0
\end{cases}
,$$
where $\ZZ_\ell=\varprojlim \ZZ/\ell^n$ is the $\ell$-adic integers.

Hints: Any Galois étale cover $X'$ of an elliptic curve is again an elliptic curve. If the degree of $X'$ over $X$ is relatively prime to $p$, then $X'$ can be dominated by the cover $n_X: X \to X$ for some integer $n$ with $(n, p)=1$. The Galois group of the covering $n_X$ is $\ZZ/n \times \ZZ/n$. Étale covers of degree divisible by $p$ can occur only if the Hasse invariant of $X$ is not zero.

Note: More generally, Grothendieck has shown (SGA 1, X, 2.6) that the algebraic fundamental group of any curve of genus $g$ is isomorphic to a quotient of the completion, with respect to subgroups of finite index, of the ordinary topological fundamental group of a compact Riemann surface of genus $g$, i.e., a group with $2g$ generators $a_1, \ldots, a_g, b_1, \ldots, b_g$ and the relation $\qty(a_1 b_1 a_1^{-1} b_1^{-1}) \cdots \qty(a_g b_g a_g^{-1} b_g^{-1})=1$.
:::
