---
schema: qual/card@1
id: T-TORCOHOM
kind: definition
title: The Stanley--Reisner presentation of the cohomology of a smooth toric variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Stanley-Reisner Ring
  - Chow Ring
relations:
- kind: uses
  target: T-TORDIV
- kind: related-to
  target: D-CHOWRING
- kind: related-to
  target: T-FULBETTI
review: draft
prompts:
- What is the Stanley--Reisner relation?
- What are the Betti numbers of a smooth complete toric variety?
---

For a smooth complete toric variety, fan combinatorics presents cohomology: non-cones give monomial relations and characters give linear relations.

::: {.definition title="Stanley--Reisner ideal"}
Let $\Sigma$ have rays $\rho_1,\ldots,\rho_r$.
The \dfn{Stanley--Reisner ideal} is
$$
I_\Sigma
\coloneqq
\bigl(
x_{i_1}\cdots x_{i_k}
\st
\rho_{i_1},\ldots,\rho_{i_k}
\text{ do not span a cone of }\Sigma
\bigr)
\subseteq\ZZ[x_1,\ldots,x_r].
$$
The corresponding vanishing products of invariant divisor classes are the Stanley--Reisner relations.
:::

::: {.theorem title="Jurkiewicz--Danilov"}
Let $X_\Sigma$ be a smooth complete toric variety over $\CC$ with rays $\rho_1, \ldots, \rho_r$, primitive generators $u_i$, and invariant divisors $D_i$.
Then
$$
A^*(X_\Sigma)
\cong
\ZZ[x_1,\ldots,x_r]/(I_\Sigma+J_\Sigma),
$$
where
$$
J_\Sigma
\coloneqq
\left(
\sum_i\inner{m}{u_i}x_i
\st m\in M
\right).
$$
Under the cycle-class map,
$$
A^k(X_\Sigma)\xrightarrow{\sim}H^{2k}(X_\Sigma(\CC),\ZZ),
$$
and $x_i$ maps to the class of $D_i$.
The odd singular cohomology groups vanish.

This is Cox--Little--Schenck, *Toric Varieties*, Theorem 12.4.4 (Jurkiewicz--Danilov), whose statement is the ring isomorphism $R(\Sigma)=\ZZ[x_1,\dots,x_r]/(I_\Sigma+J_\Sigma)\cong H^\bullet(X_\Sigma,\ZZ)$ for a smooth complete $X_\Sigma$, induced by $x_i\mapsto[D_{\rho_i}]$; the two ideals are displayed in their (12.4.2) and (12.4.3), the first being the Stanley--Reisner ideal defined above. The comparison with the Chow ring is [*ibid.*, Theorem 12.5.3], stated with $\QQ$ coefficients — $R_\QQ(\Sigma)_\QQ\cong A^\bullet(X_\Sigma)_\QQ\cong H^\bullet(X_\Sigma,\QQ)$ for a complete simplicial $X_\Sigma$; over $\ZZ$ the composite is an isomorphism for smooth $X_\Sigma$ as well, since $H^\bullet(X_\Sigma,\ZZ)$ is then torsion-free in even degrees and vanishes in odd ones.
:::

::: {.remark}
The Stanley--Reisner relation $D_{i_1}\cdots D_{i_k}=0$ says that invariant divisors whose rays span no cone have empty common intersection, since their orbit closures do not meet.
The linear relations are $\div(\chi^m) \sim 0$ from the class-group sequence.
:::

::: {.example}
For $\PP^2$ with rays $e_1, e_2, -e_1 - e_2$, the three rays together span no cone, so $I_\Sigma = (x_1 x_2 x_3)$, and $J_\Sigma = (x_1 - x_3, x_2 - x_3)$.
So $H^\bullet(\PP^2) = \ZZ[H]/(H^3)$.
For the Hirzebruch surface $\FF_a$ with rays $e_1, e_2, -e_1 + a e_2, -e_2$, the pairs $\{\rho_1,\rho_3\}$ and $\{\rho_2,\rho_4\}$ span no cone, so $x_1 x_3 = x_2 x_4 = 0$, with linear relations $x_1 = x_3$ and $x_2 = x_4 - a x_3$, and the ring is $\ZZ[f, s]/(f^2, s^2 - a s f)$ for $f = x_1$ and $s = x_4$; so $D_4^2 = a$ and $D_2^2 = (s - af)^2 = -a$.
:::

::: {.remark title="Betti numbers"}
The fan-count formula for the Betti numbers and Euler characteristic is recorded separately in [[T-FULBETTI]].
:::
