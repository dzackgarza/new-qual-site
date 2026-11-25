---
schema: qual/card@1
id: T-FULBETTI
kind: theorem
title: Betti numbers of a smooth complete toric variety from the cone counts
slogan: 'Smooth complete toric cohomology is counted by the fan: odd Betti numbers vanish, even ones come from cone counts, and $\chi$ counts maximal cones.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Cohomology
  - Fans
relations:
- kind: uses
  target: PR-TORMOR
- kind: uses
  target: T-TORDIV
review: draft
prompts:
- Compute the Betti numbers of a smooth complete toric variety from its fan.
- Why is the odd cohomology of a smooth complete toric variety zero?
---

::: {.theorem title="Betti numbers"}
Let $\Sigma$ be a smooth complete fan of dimension $n$, let $X_\Sigma$ be its toric variety over $\CC$, and write $\Sigma(k)$ for the set of $k$-dimensional cones.
Let
$$
\beta_j\coloneqq\operatorname{rank}_{\ZZ}H^j(X_\Sigma(\CC),\ZZ).
$$
Then the odd Betti numbers vanish and
$$
\beta_{2k} = \sum_{i=k}^{n} (-1)^{i-k} \binom{i}{k} \size \Sigma(n-i) .
$$

The formula is Cox--Little--Schenck, *Toric Varieties*, Theorem 12.3.12, stated there for a complete simplicial fan and with the Betti numbers $b_{2k}=\dim_\QQ H^{2k}(X_\Sigma,\QQ)$ — a smooth complete fan being simplicial, this card's hypothesis is the stronger one — together with the symmetry $b_{2k}=b_{2n-2k}$ that the same theorem records. The vanishing of the odd Betti numbers is Theorem 12.3.11 of the same chapter, whose part (a) reads $H^{2k+1}(X_\Sigma,\QQ)=0$. The two theorems are statements over $\QQ$; over $\ZZ$ they give the same numbers for a smooth $X_\Sigma$, because the spectral sequence (12.3.11) with integer coefficients then degenerates at $E_2$ as well (Franz, recorded in the same section immediately before Theorem 12.3.11), so that $H^\bullet(X_\Sigma(\CC),\ZZ)$ is torsion-free, vanishes in odd degrees, and satisfies $\beta_{2k}=b_{2k}$.
:::

::: {.theorem title="Two special cases"}
$$
\beta_0 = \beta_{2n} = 1,
\qquad
\chi\bigl(X_\Sigma(\CC)\bigr) = \size \Sigma(n),
$$
the second by the binomial formula above, and the first Chern class gives
$$
\Pic(X_\Sigma)\xrightarrow{\sim}H^2(X_\Sigma(\CC),\ZZ),
\qquad
\beta_2=\size\Sigma(1)-n.
$$
The isomorphism is [*ibid.*, Theorem 12.3.2], which needs every maximal cone of $\Sigma$ to be $n$-dimensional, as completeness gives; $\beta_2=\size\Sigma(1)-n$ is then the rank of $\ZZ^{\Sigma(1)}/M$ computed in [*ibid.*, Theorem 4.1.3], the class group and the Picard group coinciding on a smooth $X_\Sigma$.
:::

::: {.remark title="Where the formula comes from"}
Cohomology of an affine piece is exterior algebra on the lattice orthogonal to the cone,
$$
H^i(U_\sigma(\CC); \ZZ) \cong \Wedgepower^i M(\sigma),
\qquad
M(\sigma) \coloneqq \sigma^\perp \intersect M ,
$$
so the Mayer--Vietoris spectral sequence for the cover by the $U_\sigma$ over maximal cones has
$$
E_1^{p,q}
=\bigoplus_{i_0 < \cdots < i_p}
\Wedgepower^q M(\sigma_{i_0} \intersect \cdots \intersect \sigma_{i_p})
\abuts H^{p+q}(X_\Sigma(\CC); \ZZ) .
$$
The alternating sum over $q$ of $\rank \Wedgepower^q M(\tau)$ is $0$ unless $\dim \tau = n$, where it is $1$, and only the maximal cones survive.
That is the Euler characteristic statement, and tracking the individual ranks gives the binomial formula.
:::

::: {.remark title="The formula on $\PP^2$ and $\FF_a$"}
For $\PP^2$: $\size \Sigma(2) = 3$, $\size \Sigma(1) = 3$, $\size \Sigma(0) = 1$, giving $\beta_0 = 1$, $\beta_2 = 1$, $\beta_4 = 1$ and $\chi = 3$.
For $\FF_a$: $\size \Sigma(2) = 4$, $\size \Sigma(1) = 4$, giving $\beta_2 = 2 = \rank \Pic(\FF_a)$ and $\chi = 4$.
:::
