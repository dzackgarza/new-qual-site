---
schema: qual/card@1
id: T-CRVJACFUN
kind: theorem
title: The Jacobian represents $\Pic^0(X/-)$, and is a smooth proper group scheme of dimension $g$
slogan: 'The Jacobian represents degree-zero line bundles; its tangent space is $H^1(\OO_X)$, so it is a smooth proper group variety of dimension $g$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Jacobians
  - Moduli
  - Group Schemes
relations:
- kind: uses
  target: T-MWDVL
- kind: uses
  target: D-MODPIC
- kind: related-to
  target: T-U5QSY
- kind: related-to
  target: PR-CRVGRP
review: draft
prompts:
- What functor does the Jacobian represent, and why is the quotient by $p^* \Pic(T)$ there?
- Why is $\Jac(X)$ smooth of dimension $g$?
- Why is $\Jac(X)$ proper?
- What are the fibres of the map from the $n$-fold symmetric product to $\Jac(X)$?
- Construct the Jacobian without using $\CC$.
---

::: {.theorem title="Representability"}
Let $X/k$ be a smooth projective geometrically connected curve of genus $g$, and assume $p_0\in X(k)$.
The degree-zero relative Picard functor $\underline{\Pic}^{\,0}_{X/k}$ from [[D-MODPIC]] is represented by a smooth proper connected group scheme
$$
\Jac(X)\longrightarrow\Spec k
$$
of dimension $g$.

Equivalently, for every $k$-scheme $T$ there is a natural group isomorphism
$$
\Hom_k(T,\Jac(X))
\xrightarrow{\sim}
\underline{\Pic}^{\,0}_{X/k}(T).
$$
The point $p_0$ determines a normalized Poincaré line bundle $\mathcal P$ on $X\times_k\Jac(X)$, characterized by
$$
\mathcal P\restrict_{\theset{p_0}\times\Jac(X)}\cong\OO_{\Jac(X)},
$$
whose pullback along $\operatorname{id}_X\times f$ represents the class corresponding to $f\colon T\to\Jac(X)$.

Moreover:

- On $k$-points, the chosen rational point identifies $\Jac(X)(k)$ with the degree-zero line-bundle classes on $X$.

- The group law is induced by tensor product in $\underline{\Pic}^{\,0}_{X/k}$; the identity is $[\OO_X]$ and inversion sends $[L]$ to $[L^\vee]$.

- The tangent space at the identity is
  $$
  T_0\Jac(X)\cong H^1(X,\OO_X).
  $$

- Thus $\Jac(X)$ is an abelian variety of dimension $g$.

For an elliptic curve $(E,p_0)$, the Abel map $p\mapsto\OO_E(p-p_0)$ is an isomorphism $E\xrightarrow{\sim}\Jac(E)$, as in [[PR-CRVGRP]].
:::

::: {.theorem title="The symmetric product"}
For each $n\geq0$, the assignment
$$
(p_1,\ldots,p_n)
\longmapsto
\OO_X\!\left(\sum_i p_i-np_0\right)
$$
is symmetric and induces the Abel morphism
$$
a_n\colon\Sym^nX\longrightarrow\Jac(X).
$$
For a degree-zero line bundle $L$ on $X$, the fibre is the complete linear system
$$
a_n^{-1}([L])
\cong
\abs{L(np_0)}
\cong
\PP H^0\bigl(X,L(np_0)\bigr).
$$
Riemann--Roch gives $h^0(X,L(np_0))\geq n+1-g$, so $a_n$ is surjective for $n\geq g$.
For $n\geq2g-1$, $H^1(X,L(np_0))=0$ for every $L\in\Pic^0(X)$, and $a_n$ is a projective bundle with fibres $\PP^{n-g}$.
:::

::: {.remark title="Representability and rigidification"}
Two features of the functor control representability.

The quotient by line bundles pulled back from $T$ in [[D-MODPIC]] identifies families that determine the same fibrewise line-bundle class. The section $p_0\times T\subseteq X\times T$ chooses a normalized representative: for a line bundle $L$ on $X\times T$, replace it by
$$
L\tensor p^*\bigl((p_0\times\operatorname{id}_T)^*L\bigr)^\vee.
$$
Its restriction to $p_0\times T$ is canonically trivial. This normalization is what permits the universal Poincaré line bundle above.

Thus $\Jac(X)$ upgrades degree-zero line-bundle classes to a group scheme representing their families.
:::

::: {.remark title="Smooth, of dimension $g$, and proper"}
For $X_\varepsilon=X\times_k\Spec k[\varepsilon]/(\varepsilon^2)$, the exact sequence
$$
1\to1+\varepsilon\OO_X\to\OO_{X_\varepsilon}^\times\to\OO_X^\times\to1
$$
identifies the kernel of $\Pic(X_\varepsilon)\to\Pic(X)$ with $H^1(X,\OO_X)$, since $1+\varepsilon\OO_X\cong\OO_X$ additively. This gives the displayed tangent-space isomorphism.

Infinitesimal deformations of a line bundle across a square-zero thickening have obstruction in $H^2(X,\OO_X)$, which vanishes for a curve. Hence the Picard functor is formally smooth; finite type representability makes $\Jac(X)$ smooth. Its dimension is therefore
$$
\dim T_0\Jac(X)=h^1(X,\OO_X)=g.
$$

The morphism $a_g\colon\Sym^gX\to\Jac(X)$ is surjective by Riemann--Roch. Since $\Sym^gX$ is projective and geometrically connected, its surjective image $\Jac(X)$ is proper and connected. Together with smoothness and the group law, this makes $\Jac(X)$ an abelian variety.
The properness implication uses separatedness of the Picard scheme: after any base change $T\to\Spec k$, the projection $\Sym^gX_T\to T$ is closed, and surjectivity of $a_{g,T}$ implies that the projection $\Jac(X)_T\to T$ carries closed subsets to closed subsets. Thus $\Jac(X)\to\Spec k$ is universally closed; finite type and separatedness then give properness.
:::

::: {.remark title="Comparison with the analytic construction"}
Over $\CC$ one can write
$$
\Jac(X)(\CC)=H^0(X,\Omega_X^1)^\vee/H_1(X,\ZZ),
$$
where the homology lattice is embedded by integration. This analytic construction produces a complex torus; GAGA identifies it with the algebraic Jacobian above.
The functorial construction above needs no ground-field hypothesis and therefore applies in characteristic $p$ and to families, where the analytic construction is unavailable.
The divisor-class description and the analytic torus are identified by the Abel--Jacobi theorem.

In genus $1$ with the chosen point $p_0$, the Abel morphism $a_1\colon X\to\Jac(X)$ is an isomorphism.
:::
