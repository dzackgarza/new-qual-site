---
schema: qual/card@1
id: D-OKSJJ
kind: definition
title: Inverse limit
classification:
  areas:
  - topology
  topics:
  - Category Theory
  - Homological Algebra
relations: []
review: draft
---

::: {.definition}
Let $(I,\leq)$ be a directed set.
An \dfn{inverse system} of abelian groups indexed by $I$ consists of abelian groups $A_\alpha$ for $\alpha\in I$ and homomorphisms $f_{\beta\alpha}\colon A_\beta\to A_\alpha$ for $\alpha\leq\beta$, with $f_{\alpha\alpha}=\id_{A_\alpha}$ and $f_{\beta\alpha}\circ f_{\gamma\beta}=f_{\gamma\alpha}$ for $\alpha\leq\beta\leq\gamma$.
Its \dfn{inverse limit} is the subgroup of compatible families
$$
\varprojlim_\alpha A_\alpha\coloneqq\ts{(a_\alpha)_{\alpha\in I}\in\prod_{\alpha\in I}A_\alpha \st f_{\beta\alpha}(a_\beta)=a_\alpha\text{ whenever }\alpha\leq\beta},
$$
with the projections $\pi_\alpha\colon\varprojlim A_\alpha\to A_\alpha$.
:::

::: {.proposition}
Inverse limits are left exact: if $0\to A_\alpha\mapsvia{u_\alpha}B_\alpha\mapsvia{v_\alpha}C_\alpha$ is exact for every $\alpha\in I$ and the $u_\alpha$ and $v_\alpha$ commute with the maps of the inverse systems, then the induced sequence $0\to\varprojlim A_\alpha\mapsvia{u}\varprojlim B_\alpha\mapsvia{v}\varprojlim C_\alpha$ is exact.
:::

::: {.remark}
For $I=\NN$, write $f_n\colon A_{n+1}\to A_n$ for the bonding maps and define $\delta\colon\prod_nA_n\to\prod_nA_n$ by $\delta((a_n)_n)\coloneqq(a_n-f_n(a_{n+1}))_n$.
Then $\ker\delta=\varprojlim A_n$, and $\varprojlim^1A_n\coloneqq\coker\delta$.
A short exact sequence $0\to A_n\to B_n\to C_n\to0$ of inverse systems indexed by $\NN$ gives an exact sequence
$$
0\to\varprojlim A_n\to\varprojlim B_n\to\varprojlim C_n\to\varprojlim{}^1A_n\to\varprojlim{}^1B_n\to\varprojlim{}^1C_n\to0,
$$
so $\varprojlim^1$ measures the failure of $\varprojlim B_n\to\varprojlim C_n$ to be surjective [@Hat02, p. 312].
:::
