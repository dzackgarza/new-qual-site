---
schema: qual/card@1
id: T-BASECHANGE
kind: theorem
title: Flat, proper and smooth base change
classification:
  areas:
  - algebraic-geometry
  topics:
  - Base Change
  - Higher Direct Images
  - Etale Cohomology
relations:
- kind: uses
  target: D-SCHBC
- kind: related-to
  target: T-COHBC
review: draft
prompts:
- What is flat base change for quasicoherent cohomology?
- What is proper base change?
- What is smooth base change?
---

Throughout, consider a Cartesian square
\[
\begin{array}{ccc}
X' & \xrightarrow{g'} & X \\
\downarrow{\scriptstyle f'} & & \downarrow{\scriptstyle f} \\
Y' & \xrightarrow{g} & Y
\end{array}
\]
and the base change map $g^* R^i f_* \mathcal{F} \to R^i f'_* g'^* \mathcal{F}$.

::: {.theorem title="Flat base change"}
If $f$ is quasicompact and separated, $g$ is flat, and $\mathcal{F}$ is quasicoherent on $X$, the base change map is an isomorphism for all $i$.
:::

::: {.proof}
1. The statement is local on $Y$ and $Y'$, so take $Y = \Spec A$ and $Y' = \Spec A'$ with $A \to A'$ flat.

2. $X$ is quasicompact and separated, so choose a finite affine open cover $\mathcal{U}$; its intersections are affine, and $H^i(X, \mathcal{F})$ is the cohomology of the Čech complex $C^\bullet(\mathcal{U}, \mathcal{F})$ of $A$-modules.

3. The preimages of the cover form a finite affine cover of $X' = X \times_A A'$ with intersections affine, and $C^\bullet(\mathcal{U}', g'^* \mathcal{F}) = C^\bullet(\mathcal{U}, \mathcal{F}) \otimes_A A'$, because sections of a quasicoherent sheaf on an affine commute with base change of affines.

4. Since $A'$ is flat, $- \otimes_A A'$ is exact and commutes with taking cohomology, so $H^i(X', g'^* \mathcal{F}) \cong H^i(X, \mathcal{F}) \otimes_A A'$.
:::

::: {.corollary title="Extension of the base field"}
Let $X$ be a quasicompact separated scheme over a field $k$, $\mathcal{F}$ a quasicoherent sheaf on $X$, and $K/k$ a field extension, with $X_K = X \times_k \Spec K$ and $\mathcal{F}_K$ the pullback of $\mathcal{F}$.
Then $H^i(X_K, \mathcal{F}_K) \cong H^i(X, \mathcal{F}) \otimes_k K$ for every $i$; in particular $\dim_k H^i(X, \mathcal{F}) = \dim_K H^i(X_K, \mathcal{F}_K)$ [@Har10a, Proposition III.9.3].
:::

::: {.theorem title="Proper base change"}
If $f$ is proper, $g$ is arbitrary, and $\mathcal{F}$ is a torsion étale sheaf on $X$, the base change map $g^* R^i f_* \mathcal{F} \to R^i f'_* g'^* \mathcal{F}$ is an isomorphism for all $i$.
The same holds for sheaves of abelian groups on locally compact Hausdorff spaces when $f$ is proper.
In particular the stalk of $R^i f_* \mathcal{F}$ at a geometric point $\bar{y}$ is $H^i(X_{\bar{y}}, \mathcal{F})$.
:::

::: {.theorem title="Smooth base change"}
If $g$ is smooth, $f$ is quasicompact and quasiseparated, and $\mathcal{F}$ is a torsion étale sheaf with torsion orders invertible on $Y$, the base change map is an isomorphism for all $i$.
:::

::: {.remark}
Without flatness of $g$, quasicoherent base change fails.
Let $E$ be an elliptic curve over an algebraically closed field, $p \in E$, $f \colon E \times E \to E$ the second projection, and $\mathcal{L} = \OO(\Delta - \{p\} \times E)$.
The restriction of $\mathcal{L}$ to the fibre $E \times \{t\}$ is $\OO_E(t - p)$, which has no nonzero sections for $t \neq p$, so the torsion-free sheaf $f_* \mathcal{L}$ is $0$.
For $g$ the inclusion of the point $p$, $g^* f_* \mathcal{L} = 0$, while the fibre gives $H^0(E, \OO_E) = k$.
The coherent statement comparing $R^i f_* \mathcal{F} \otimes \kappa(y)$ with $H^i(X_y, \mathcal{F}_y)$ at arbitrary points is the theorem on cohomology and base change.
:::
