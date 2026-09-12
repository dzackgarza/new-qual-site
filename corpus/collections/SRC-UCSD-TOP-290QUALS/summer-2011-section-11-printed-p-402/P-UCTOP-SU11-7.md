---
schema: qual/card@1
id: P-UCTOP-SU11-7
kind: problem
title: Fundamental group of surface is not free
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

Show that a closed orientable surface $\Sigma$ of genus $g \geq 1$ has $\pi_{\geq 2}(\Sigma_g) = 0$, and deduce that the fundamental group of $\Sigma_g$ is not a free group.

::: {.solution}
<1>1. For $g=1$, the universal cover of $\Sigma_g=T^2$ is $\mathbb R^2$; for $g\ge2$, the universal cover is the open disk (equivalently the hyperbolic plane).
::: {.proof}
The torus is $\mathbb R^2/\mathbb Z^2$. Every closed orientable surface of genus at least $2$ admits a hyperbolic structure, whose universal cover is $\mathbb H^2$, homeomorphic to an open disk.
:::

<1>2. Therefore the universal cover of $\Sigma_g$ is contractible for every $g\ge1$.
::: {.proof}
Both $\mathbb R^2$ and the open disk are contractible.
:::

<1>3. Hence
$$
\pi_i(\Sigma_g)=0\qquad(i\ge2).
$$
::: {.proof}
A covering map induces isomorphisms on homotopy groups in all degrees $i\ge2$, and the contractible universal cover has all such homotopy groups zero.
:::

<1>4. Suppose, for contradiction, that $\pi_1(\Sigma_g)$ were a free group $F_r$.
::: {.proof}
Since $H_1(\Sigma_g;\mathbb Z)\cong\mathbb Z^{2g}$, abelianization would force $r=2g$.
:::

<1>5. Both $\Sigma_g$ and the bouquet $\bigvee^{2g}S^1$ would then be CW models of the Eilenberg--Mac Lane space $K(F_{2g},1)$.
::: {.proof}
By <1>3, $\Sigma_g$ is aspherical with fundamental group $F_{2g}$ under the supposition. The bouquet of $2g$ circles has fundamental group $F_{2g}$ and contractible universal cover, hence is also a $K(F_{2g},1)$. CW models of $K(G,1)$ are homotopy equivalent.
:::

<1>6. This is impossible because
$$
H_2(\Sigma_g;\mathbb Z)\cong\mathbb Z,
\qquad
H_2\!\left(\bigvee^{2g}S^1;\mathbb Z\right)=0.
$$
::: {.proof}
A closed orientable surface has a fundamental class in degree $2$, while a graph has no homology above degree $1$. Homotopy-equivalent spaces must have isomorphic homology.
:::

<1>7. Therefore $\pi_1(\Sigma_g)$ is not free.
::: {.proof}
The assumption in <1>4 leads to the contradiction in <1>6.
:::
:::
