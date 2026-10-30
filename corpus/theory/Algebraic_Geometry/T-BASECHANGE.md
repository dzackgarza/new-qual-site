---
schema: qual/card@1
id: T-BASECHANGE
kind: theorem
title: Flat, proper and smooth base change
slogan: 'Under the right flat, proper, or smooth hypotheses, higher direct images commute with pulling the base around a Cartesian square.'
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
$$
\begin{array}{ccc}
X' & \xrightarrow{g'} & X \\
\downarrow{\scriptstyle f'} & & \downarrow{\scriptstyle f} \\
Y' & \xrightarrow{g} & Y
\end{array}
$$
of schemes.

::: {.theorem title="Flat base change"}
If $f$ is quasicompact and quasiseparated, $g$ is flat, and $\mathcal{F}$ is quasicoherent on $X$, the base change map
$$
g^*R^if_*\mathcal F
\xrightarrow{\sim}
R^if'_*g'^*\mathcal F
$$
is an isomorphism for all $i$.
[@Har77, Proposition III.9.3]
:::

::: {.corollary title="Extension of the base field"}
Let $X$ be a quasicompact separated scheme over a field $k$, $\mathcal{F}$ a quasicoherent sheaf on $X$, and $K/k$ a field extension, with $X_K = X \times_k \Spec K$ and $\mathcal{F}_K$ the pullback of $\mathcal{F}$.
Then $H^i(X_K, \mathcal{F}_K) \cong H^i(X, \mathcal{F}) \otimes_k K$ for every $i$; in particular $\dim_k H^i(X, \mathcal{F}) = \dim_K H^i(X_K, \mathcal{F}_K)$ [@Har77, Proposition III.9.3].
:::

::: {.theorem title="Proper base change"}
If $f$ is proper, $g$ is arbitrary, and $\mathcal{F}$ is an abelian torsion sheaf on the small étale site $X_{\acute{e}tale}$, then
$$
g^{-1}R^if_*\mathcal F
\xrightarrow{\sim}
R^if'_*g'^{-1}\mathcal F
$$
for every $i\geq0$.
In particular, for a geometric point $\bar y\to Y$,
$$
(R^if_*\mathcal F)_{\bar y}
\cong
H^i_{\acute{e}tale}(X_{\bar y},\mathcal F\restrict_{X_{\bar y}}).
$$
:::

::: {.theorem title="Smooth base change"}
If $g$ is smooth, $f$ is quasicompact and quasiseparated, and $\mathcal{F}$ is an abelian étale sheaf on $X$ whose geometric stalks are torsion of orders invertible on $Y$, then
$$
g^{-1}R^if_*\mathcal F
\xrightarrow{\sim}
R^if'_*g'^{-1}\mathcal F
$$
for every $i\geq0$.
:::

::: {.remark}
Without flatness of $g$, quasicoherent base change fails.
Let $E$ be an elliptic curve over an algebraically closed field, $p \in E$, $f \colon E \times E \to E$ the second projection, and $\mathcal{L} = \OO(\Delta - \{p\} \times E)$.
The restriction of $\mathcal{L}$ to the fibre $E \times \{t\}$ is $\OO_E(t - p)$, which has no nonzero sections for $t \neq p$. Thus $f_*\mathcal L$ vanishes on $E\sm\theset p$. It is torsion-free: a section of $\mathcal L$ over $E\times U$ that vanishes after restricting to a dense open subset of the integral scheme $E\times U$ is zero. Hence $f_*\mathcal L=0$.
For $g$ the inclusion of the point $p$, $g^* f_* \mathcal{L} = 0$, while the fibre gives $H^0(E, \OO_E) = k$.
The coherent statement comparing $R^i f_* \mathcal{F} \otimes \kappa(y)$ with $H^i(X_y, \mathcal{F}_y)$ at arbitrary points is the theorem on cohomology and base change.
:::
