---
schema: qual/card@1
id: P-SB67D
kind: problem
title: Cyclotomic specialization of $\ZZ[t]/(t^p-1)$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Rings
  - Polynomials
relations: []
review: draft
---

::: problem
Let $p$ be prime and let $\zeta_p$ be a primitive $p$th root of unity. Is the homomorphism
\[
\ZZ[t]/(t^p-1)\longrightarrow \ZZ[\zeta_p],
\qquad t\longmapsto \zeta_p,
\]
an isomorphism?
:::

::: solution
No. The map is surjective but not injective.

Let
\[
\Phi_p(t)=1+t+\cdots+t^{p-1}.
\]
Since $\zeta_p$ is primitive, its minimal polynomial over $\QQ$ is $\Phi_p(t)$. Hence the evaluation map
\[
\operatorname{ev}_{\zeta_p}:\ZZ[t]\longrightarrow \ZZ[\zeta_p]
\]
has kernel $(\Phi_p(t))$ and is surjective.

Because
\[
t^p-1=(t-1)\Phi_p(t),
\]
we have $(t^p-1)\subseteq(\Phi_p(t))$. Therefore evaluation factors through
\[
\bar{\operatorname{ev}}_{\zeta_p}:\ZZ[t]/(t^p-1)\longrightarrow\ZZ[\zeta_p].
\]
Its kernel is
\[
\frac{(\Phi_p(t))}{(t^p-1)},
\]
which is nonzero: the class of $\Phi_p(t)$ is not zero modulo $(t^p-1)$ because $\deg\Phi_p=p-1<p$.

Thus
\[
\ZZ[t]/(t^p-1)
ot\cong\ZZ[\zeta_p]
\]
via this map. In fact
\[
\ZZ[\zeta_p]\cong\ZZ[t]/(\Phi_p(t)).
\]
:::
