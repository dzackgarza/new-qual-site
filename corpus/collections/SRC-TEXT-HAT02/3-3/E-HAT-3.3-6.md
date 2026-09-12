---
schema: qual/card@1
id: E-HAT-3.3-6
kind: problem
title: "Connected sums of manifolds"
classification:
  areas:
  - topology
  topics:
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

Given two disjoint connected $n$-manifolds $M_1$ and $M_2$, a connected $n$-manifold $M_1 \sharp M_2$, their connected sum, can be constructed by deleting the interiors of closed $n$-balls $B_1 \subset M_1$ and $B_2 \subset M_2$ and identifying the resulting boundary spheres $\partial B_1$ and $\partial B_2$ via some homeomorphism between them.
(Assume that each $B_i$ embeds nicely in a larger ball in $M_i$.)

(a) Show that if $M_1$ and $M_2$ are closed then there are isomorphisms $H_i(M_1 \sharp M_2; \mathbb{Z}) \approx H_i(M_1; \mathbb{Z}) \oplus H_i(M_2; \mathbb{Z})$ for $0 < i < n$, with one exception: If both $M_1$ and $M_2$ are nonorientable, then $H_{n-1}(M_1 \sharp M_2; \mathbb{Z})$ is obtained from $H_{n-1}(M_1; \mathbb{Z}) \oplus H_{n-1}(M_2; \mathbb{Z})$ by replacing one of the two $\mathbb{Z}_2$ summands by a $\mathbb{Z}$ summand.

(b) Show that $\chi(M_1 \sharp M_2) = \chi(M_1) + \chi(M_2) - \chi(S^n)$ if $M_1$ and $M_2$ are closed.

::: {.solution}
Let
\[
N_i=M_i-\operatorname{int}B_i,
\qquad
M=M_1\#M_2=N_1\cup_{S^{n-1}}N_2.
\]
For $0<i<n-1$, removing an open $n$-ball does not change homology in degree $i$, and $H_i(S^{n-1})=0$. Mayer--Vietoris therefore gives
\[
H_i(M)\cong H_i(M_1)\oplus H_i(M_2)
\qquad(0<i<n-1).
\]

It remains to analyze degree $n-1$. Excision gives
\[
H_j(M_i,N_i)\cong H_j(D^n,S^{n-1}),
\]
so the long exact sequence of $(M_i,N_i)$ contains
\[
0\longrightarrow H_n(M_i)\longrightarrow \mathbb Z
\xrightarrow{\partial_i}H_{n-1}(N_i)
\longrightarrow H_{n-1}(M_i)\longrightarrow0.
\]
If $M_i$ is orientable, $H_n(M_i)\cong\mathbb Z$ and the first map is an isomorphism, so
\[
H_{n-1}(N_i)\cong H_{n-1}(M_i)
\]
and the boundary sphere represents zero in $H_{n-1}(N_i)$.

If $M_i$ is nonorientable, $H_n(M_i)=0$. Corollary 3.28 gives a distinguished $\mathbb Z_2$ torsion summand in $H_{n-1}(M_i)$. On the other hand Lefschetz duality for the compact manifold with boundary $N_i$ gives
\[
H_{n-1}(N_i;\mathbb Z)\cong H^1(N_i,\partial N_i;\mathbb Z),
\]
and the universal coefficient theorem shows that the group on the right is torsion-free. Hence the extension above cannot split on the $\mathbb Z_2$ summand; there it is necessarily
\[
0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb Z_2\to0.
\]
The free part is unchanged. Thus $H_{n-1}(N_i)$ is obtained from $H_{n-1}(M_i)$ by replacing its $\mathbb Z_2$ summand by $\mathbb Z$, and the boundary sphere class is twice the new generator.

Now use Mayer--Vietoris for $M=N_1\cup N_2$. Since the intersection is $S^{n-1}$, the relevant quotient is
\[
H_{n-1}(M)
\cong
\frac{H_{n-1}(N_1)\oplus H_{n-1}(N_2)}
{\langle([S],-[S])\rangle},
\]
with the usual harmless choice of sign.

If both $M_i$ are orientable, both boundary classes vanish, and the usual top-dimensional Mayer--Vietoris term supplies the expected direct sum in degree $n-1$. If exactly one, say $M_2$, is nonorientable, the relation is $2z_2=0$ on its new $\mathbb Z$ summand, restoring precisely the original $\mathbb Z_2$ summand. Thus again
\[
H_{n-1}(M)\cong H_{n-1}(M_1)\oplus H_{n-1}(M_2).
\]

If both are nonorientable, the two $\mathbb Z_2$ summands have first been replaced by $\mathbb Z z_1\oplus\mathbb Z z_2$, and Mayer--Vietoris imposes the single relation
\[
2z_1-2z_2=0.
\]
Hence
\[
(\mathbb Z z_1\oplus\mathbb Z z_2)/\langle2z_1-2z_2\rangle
\cong \mathbb Z\oplus\mathbb Z_2.
\]
Thus, compared with
\[
H_{n-1}(M_1)\oplus H_{n-1}(M_2),
\]
one of the two $\mathbb Z_2$ summands is replaced by a $\mathbb Z$ summand, exactly as claimed.

For Euler characteristic, write again $M=N_1\cup N_2$ with intersection $S^{n-1}$. Removing the interior of one $n$-cell changes Euler characteristic by $-(-1)^n$, so
\[
\chi(N_i)=\chi(M_i)-(-1)^n.
\]
Therefore
\[
\begin{aligned}
\chi(M)
&=\chi(N_1)+\chi(N_2)-\chi(S^{n-1})\\
&=\chi(M_1)+\chi(M_2)-2(-1)^n-(1+(-1)^{n-1})\\
&=\chi(M_1)+\chi(M_2)-(1+(-1)^n)\\
&=\boxed{\chi(M_1)+\chi(M_2)-\chi(S^n)}.
\end{aligned}
\]
:::
