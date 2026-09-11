---
schema: qual/card@1
id: P-AGH427ETALEDEGREETWO
kind: problem
title: Étale double covers of $Y$ correspond to $2$-torsion elements of $\Pic Y$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Jacobians
  - Curves
relations: []
review: draft
---

::: problem
Let $Y$ be a curve over a field $k$ of characteristic $\neq 2$. We show there is a one-to-one correspondence between finite étale morphisms $f: X \to Y$ of degree 2, and 2-torsion elements of $\Pic Y$, i.e., invertible sheaves $\mcl$ on $Y$ with $\mcl^2 \cong \OO_Y$.

a. Given an étale morphism $f: X \to Y$ of degree 2, there is a natural map $\OO_Y \to f_* \OO_X$. Let $\mcl$ be the cokernel. Then $\mcl$ is an invertible sheaf on $Y$, $\mcl \cong \det f_* \OO_X$, and so $\mcl^2 \cong \OO_Y$ by (Ex. 2.6). Thus an étale cover of degree 2 determines a 2-torsion element in $\Pic Y$.

b. Conversely, given a 2-torsion element $\mcl$ in $\Pic Y$, define an $\OO_Y\dash$algebra structure on $\OO_Y \oplus \mcl$ by $\langle a, b\rangle \cdot\left\langle a', b'\right\rangle=\left\langle a a'+\varphi(b \tensor b'), a b'+a' b\right\rangle$, where $\varphi$ is an isomorphism of $\mcl \tensor \mcl \to \OO_Y$. Then take $X=\Spec(\OO_Y \oplus \mcl)$ (II, Ex. 5.17). Show that $X$ is an étale cover of $Y$.

c. Show that these two processes are inverse to each other. Hint: Let $\tau: X \to X$ be the involution which interchanges the points of each fibre of $f$. Use the trace map $a \mapsto a+\tau(a)$ from $f_* \OO_X \to \OO_Y$ to show that the sequence of $\OO_Y\dash$modules in a. is split exact:
$$
0 \to \OO_Y \to f_* \OO_X \to \mcl \to 0
$$

Note. This is a special case of the more general fact that for $(n, \characteristic k)=1$, the étale Galois covers of $Y$ with group $\ZZ/n\ZZ$ are classified by the étale cohomology group $H_{\text{et}}^1(Y, \ZZ/n\ZZ)$, which is equal to the group of $n$-torsion points of $\Pic Y$. See Serre.
:::
