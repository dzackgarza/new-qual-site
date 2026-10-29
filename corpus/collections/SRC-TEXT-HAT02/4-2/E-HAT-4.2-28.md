---
schema: qual/card@1
id: E-HAT-4.2-28
kind: problem
title: "$\\ZZ_p \\times \\ZZ_p$ cannot act freely on spheres"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 28; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that the group $\ZZ_p \times \ZZ_p$ with $p$ prime cannot act freely on any sphere $S^n$.
:::

::: {.solution}
Let
$$
G=\ZZ_p\times\ZZ_p.
$$
Suppose first $n>1$ and that $G$ acts freely on $S^n$. Then
$$
S^n\longrightarrow M=S^n/G
$$
is the universal covering of a closed $n$-manifold, with
$$
\pi_1(M)=G,
\qquad
\pi_i(M)=0\quad(1<i<n),
\qquad
\pi_n(M)\cong\ZZ.
$$
Attach one $(n+1)$-cell along a generator of $\pi_n(M)$, then cells of dimensions at least $n+2$ to kill all remaining higher homotopy groups. This produces a $K(G,1)$.

Up through dimension $n+1$ this CW complex has exactly one new $(n+1)$-cell beyond the $n$-dimensional manifold $M$. With $\FF_p$-coefficients the cochain group in degree $n+1$ is therefore one-dimensional. Consequently
$$
\dim_{\FF_p}H^{n+1}(K(G,1);\FF_p)\le1.
$$

But
$$
K(G,1)\simeq K(\ZZ_p,1)\times K(\ZZ_p,1).
$$
For $p=2$,
$$
H^*(K(\ZZ_2,1);\FF_2)\cong\FF_2[u],\quad |u|=1,
$$
and for odd $p$,
$$
H^*(K(\ZZ_p,1);\FF_p)
\cong\Lambda(u)\otimes\FF_p[v],
\quad |u|=1,\ |v|=2.
$$
In either case the Künneth formula shows that the degree-$d$ cohomology of the product has dimension $d+1$. In particular
$$
\dim H^{n+1}(K(G,1);\FF_p)=n+2>1,
$$
a contradiction.

If $n=1$, any finite group acting freely on $S^1$ is cyclic: an orientation-reversing homeomorphism of $S^1$ has a fixed point, so a finite free action is orientation-preserving and conjugate to a rotation action. Since $\ZZ_p\times\ZZ_p$ is not cyclic, it cannot act freely on $S^1$ either.

Thus
$$
\boxed{\ZZ_p\times\ZZ_p\text{ acts freely on no sphere}.}
$$
:::
