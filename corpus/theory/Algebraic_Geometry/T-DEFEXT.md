---
schema: qual/card@1
id: T-DEFEXT
kind: theorem
title: Infinitesimal automorphisms and first-order deformations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Deformation Theory
  - Tangent Sheaf
  - Ext Groups
relations:
- kind: uses
  target: D-COTCPLX
review: draft
prompts:
- For $X \to B$ smooth, why is $\operatorname{Ext}^0(\Omega_{X/B}, \OO_X) \cong H^0(T_{X/B})$, and why does it measure infinitesimal automorphisms?
- Why does $\operatorname{Ext}^1(\Omega_{X/B}, \OO_X)$ measure first-order deformations?
---

Let $k$ be a field, $D = \Spec k[\varepsilon]/(\varepsilon^2)$, and $X$ a smooth separated scheme of finite type over $k$ with tangent sheaf $T_X = \mathcal{H}om(\Omega_{X/k}, \OO_X)$.

::: {.theorem}
1. $\operatorname{Ext}^0(\Omega_{X/k}, \OO_X) = H^0(X, T_X)$, and it is in bijection with the automorphisms of $X \times D$ over $D$ that restrict to the identity on $X$.

2. $\operatorname{Ext}^1(\Omega_{X/k}, \OO_X) = H^1(X, T_X)$, and it is in bijection with the isomorphism classes of first-order deformations: flat $D$-schemes $\mathcal{X}$ with $\mathcal{X} \times_D \Spec k \cong X$.

3. Let $A_n = k[t]/(t^{n+1})$ for $n \geq 1$, so $A_1 \cong k[\varepsilon]/(\varepsilon^2)$.
   A flat deformation $\mathcal{X}_n$ of $X$ over $A_n$ determines an obstruction class $o(\mathcal{X}_n) \in H^2(X, T_X)$, and $o(\mathcal{X}_n) = 0$ if and only if there is a flat deformation $\mathcal{X}_{n+1}$ over $A_{n+1}$ with $\mathcal{X}_{n+1} \times_{A_{n+1}} \Spec A_n \cong \mathcal{X}_n$.
:::

::: {.proof}
1. $\Omega_{X/k}$ is locally free, so $\mathcal{E}xt^q(\Omega_{X/k}, \OO_X) = 0$ for $q > 0$ and the local-to-global spectral sequence gives $\operatorname{Ext}^p(\Omega_{X/k}, \OO_X) = H^p(X, T_X)$.

2. An automorphism of $X \times D$ restricting to the identity is, on each affine $\Spec A$, a ring map $a \mapsto a + \varepsilon\, \delta(a)$ of $A[\varepsilon]$; it is a ring homomorphism exactly when $\delta$ is a $k$-derivation, and derivations $A \to A$ are $\Hom_A(\Omega_{A/k}, A)$.
   These glue to $H^0(X, T_X)$.

3. A first-order deformation of a smooth affine $X$ is trivial, because smooth algebras lift uniquely up to isomorphism over square-zero extensions.
   So a deformation is glued from trivial ones $U_i \times D$ on an affine cover along automorphisms of $U_{ij} \times D$, which by step 2 are sections $\theta_{ij} \in T_X(U_{ij})$.
   The cocycle condition for gluing is the Čech cocycle condition, changing the trivializations changes $\theta$ by a coboundary, and so isomorphism classes are $\check{H}^1(\mathcal{U}, T_X) = H^1(X, T_X)$.

4. The kernel of $A_{n+1} \to A_n$ is the ideal $(t^{n+1}) \cong k$, with square zero.
   Cover $\mathcal{X}_n$ by affine opens $U_i$; each lifts to a smooth $A_{n+1}$-scheme $V_i$, unique up to isomorphism by the lifting property used in step 3.
   Choose isomorphisms $\phi_{ij} \colon V_j|_{U_{ij}} \to V_i|_{U_{ij}}$ lifting the identity of $U_{ij}$.
   On triple overlaps $\phi_{ij} \phi_{jk} \phi_{ik}^{-1}$ restricts to the identity over $A_n$, so by the argument of step 2, with $t^{n+1}$ in place of $\varepsilon$, it is $\id + t^{n+1} \theta_{ijk}$ for a section $\theta_{ijk} \in T_X(U_{ijk})$.
   The sections $\theta_{ijk}$ form a Čech $2$-cocycle, and changing the lifts $V_i$ or the isomorphisms $\phi_{ij}$ changes it by a coboundary, so its class $o(\mathcal{X}_n) \in H^2(X, T_X)$ is well defined.
   The class is zero exactly when the $\phi_{ij}$ can be corrected by sections of $T_X$ so that the cocycle condition holds, which is exactly when the $V_i$ glue to a deformation $\mathcal{X}_{n+1}$.
:::

::: {.example}
For a smooth projective curve $C$ of genus $g \geq 2$, $H^0(T_C) = 0$, so $C$ has no infinitesimal automorphisms, $H^2(T_C) = 0$, so deformations are unobstructed, and $h^1(T_C) = h^0(\omega_C^{\otimes 2}) = 3g - 3$ by Serre duality and Riemann--Roch.
:::
