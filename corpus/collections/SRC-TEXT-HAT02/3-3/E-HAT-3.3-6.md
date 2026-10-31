---
schema: qual/card@1
id: E-HAT-3.3-6
kind: problem
title: Connected sums of manifolds
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Rechecked the statement against Hatcher and repaired the existing solution.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced the invalid homological argument with a correct proof.
---

::: {.problem}
Given two disjoint connected $n$-manifolds $M_1$ and $M_2$, a connected $n$-manifold $M_1 \sharp M_2$, their connected sum, can be constructed by deleting the interiors of closed $n$-balls $B_1 \subset M_1$ and $B_2 \subset M_2$ and identifying the resulting boundary spheres $\partial B_1$ and $\partial B_2$ via some homeomorphism between them.
(Assume that each $B_i$ embeds nicely in a larger ball in $M_i$.)

(a) Show that if $M_1$ and $M_2$ are closed then there are isomorphisms $H_i(M_1 \sharp M_2; \ZZ) \approx H_i(M_1; \ZZ) \oplus H_i(M_2; \ZZ)$ for $0 < i < n$, with one exception: If both $M_1$ and $M_2$ are nonorientable, then $H_{n-1}(M_1 \sharp M_2; \ZZ)$ is obtained from $H_{n-1}(M_1; \ZZ) \oplus H_{n-1}(M_2; \ZZ)$ by replacing one of the two $\ZZ_2$ summands by a $\ZZ$ summand.

(b) Show that $\chi(M_1 \sharp M_2) = \chi(M_1) + \chi(M_2) - \chi(S^n)$ if $M_1$ and $M_2$ are closed.
:::

::: {.solution}
Put $N_i=M_i\setminus\operatorname{int}B_i$ and $M=M_1\#M_2=N_1\cup_{S^{n-1}}N_2$. For $n=1$ there are no degrees $0<i<n$; the Euler-characteristic calculation below still applies. Assume $n\ge2$ for part (a).

Excision gives $H_j(M_i,N_i;\ZZ)\cong H_j(D^n,S^{n-1};\ZZ)$, which is $\ZZ$ in degree $n$ and zero otherwise. Thus $H_j(N_i;\ZZ)\cong H_j(M_i;\ZZ)$ for $0<j<n-1$. Mayer--Vietoris for $M=N_1\cup N_2$ gives the direct sum formula in these degrees.

It remains to determine $H_{n-1}(M;\ZZ)$ as a finitely generated abelian group. Let $\epsilon_i=0$ when $M_i$ is orientable and $\epsilon_i=1$ otherwise. With rational coefficients, the pair sequence gives
$$
0\longrightarrow H_n(M_i;\QQ)\longrightarrow\QQ
\longrightarrow H_{n-1}(N_i;\QQ)
\longrightarrow H_{n-1}(M_i;\QQ)\longrightarrow0.
$$
The first map is an isomorphism for orientable $M_i$ and zero for nonorientable $M_i$. Hence
$$
\operatorname{rank}H_{n-1}(N_i)
=\operatorname{rank}H_{n-1}(M_i)+\epsilon_i,
$$
and the boundary sphere has a nonzero rational class in $N_i$ exactly when $\epsilon_i=1$.

The Mayer--Vietoris sequence with rational coefficients shows that $H_{n-1}(M;\QQ)$ is the cokernel of
$$
H_{n-1}(S^{n-1};\QQ)\longrightarrow
H_{n-1}(N_1;\QQ)\oplus H_{n-1}(N_2;\QQ).
$$
This map has rank zero if both $M_i$ are orientable and rank one otherwise. For $n=2$, the same conclusion follows from the reduced Mayer--Vietoris sequence, since both $N_i$ are connected. Therefore
$$
\operatorname{rank}H_{n-1}(M)
=
\begin{cases}
\operatorname{rank}H_{n-1}(M_1)+\operatorname{rank}H_{n-1}(M_2)+1,
&\epsilon_1=\epsilon_2=1,\\
\operatorname{rank}H_{n-1}(M_1)+\operatorname{rank}H_{n-1}(M_2),
&\text{otherwise}.
\end{cases}
$$
The connected sum is orientable exactly when both summands are orientable: an orientation restricts to each punctured summand, and compatible orientations on the punctured summands glue. Corollary 3.28 says that the torsion subgroup of $H_{n-1}$ of a closed connected $n$-manifold is zero if it is orientable and $\ZZ_2$ otherwise. Combining this torsion statement with the rank calculation and the classification of finitely generated abelian groups gives the direct sum formula when at most one $M_i$ is nonorientable. When both are nonorientable, the rank rises by one and the torsion changes from $\ZZ_2\oplus\ZZ_2$ to $\ZZ_2$, exactly replacing one $\ZZ_2$ summand by $\ZZ$.

For part (b), removing the interior of an $n$-ball changes Euler characteristic by $-(-1)^n$, so $\chi(N_i)=\chi(M_i)-(-1)^n$. Additivity for the gluing along $S^{n-1}$ gives
$$
\begin{aligned}
\chi(M)
&=\chi(N_1)+\chi(N_2)-\chi(S^{n-1})\\
&=\chi(M_1)+\chi(M_2)-2(-1)^n-(1+(-1)^{n-1})\\
&=\chi(M_1)+\chi(M_2)-\chi(S^n).
\end{aligned}
$$
:::
