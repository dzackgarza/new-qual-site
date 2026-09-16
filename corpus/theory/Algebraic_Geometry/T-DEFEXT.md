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

::: {.example}
For a smooth projective curve $C$ of genus $g \geq 2$, $H^0(T_C) = 0$, so $C$ has no infinitesimal automorphisms, $H^2(T_C) = 0$, so deformations are unobstructed, and $h^1(T_C) = h^0(\omega_C^{\otimes 2}) = 3g - 3$ by Serre duality and Riemann--Roch.
:::
