---
schema: qual/card@1
id: E-HAT-2.B-3
kind: problem
title: "Complement of a disk pair in a sphere pair"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the Alexander-duality and Mayer--Vietoris calculations and all degree shifts.
---

::: {.problem}
Let $(D, S) \subset (D^n, S^{n-1})$ be a pair of subspaces homeomorphic to $(D^k, S^{k-1})$, with $D \cap S^{n-1} = S$.
Show the inclusion $S^{n-1} - S \hookrightarrow D^n - D$ induces an isomorphism on homology.
[Glue two copies of $(D^n, D)$ to the two ends of $(S^{n-1} \times I, S \times I)$ to produce a $k$-sphere in $S^n$ and look at a Mayer–Vietoris sequence for the complement of this $k$-sphere.]
:::

::: {.solution}
If $k=0<n$, then $D$ is one interior point of $D^n$, and radial projection from that point retracts $D^n\setminus D$ onto $S^{n-1}$. Hence the inclusion induces an isomorphism.

Now suppose $0<k<n$ and put $d=n-k-1\ge0$. Write
$$
A=S^{n-1}\setminus S,\qquad B=D^n\setminus D.
$$
Glue two copies of $(D^n,D)$ to the ends of $(S^{n-1}\times I,S\times I)$. Their ambient union is $S^n$, and the two copies of $D^k$, joined by $S^{k-1}\times I$, form an embedded $S^k$. Let $W$ be its complement. Enlarging the two copies of $B$ slightly into the cylinder gives an open cover of $W$. Its intersection retracts onto $A$, and both inclusion maps from $A$ to the two copies of $B$ induce the map $i_*$ in the statement. Reduced Mayer--Vietoris therefore contains
$$
\cdots\longrightarrow\widetilde H_j(A)
\xrightarrow{(i_*,-i_*)}\widetilde H_j(B)^2
\longrightarrow\widetilde H_j(W)
\longrightarrow\widetilde H_{j-1}(A)\longrightarrow\cdots.
$$
Alexander duality for the embedded spheres $S\subset S^{n-1}$ and $S^k\subset S^n$ gives
$$
\widetilde H_j(A)\cong\widetilde H_j(W)\cong
\begin{cases}\ZZ,&j=d,\\0,&j\ne d.\end{cases}
$$
Thus $\widetilde H_j(B)=0$ for $j\ne d$. In degree $d$, the adjacent groups vanish, so the sequence reduces to
$$
0\longrightarrow\ZZ\xrightarrow{(i_*,-i_*)}
\widetilde H_d(B)^2\longrightarrow\ZZ\longrightarrow0.
$$
The middle group is free of rank two because this sequence splits as a sequence of abelian groups. Hence $\widetilde H_d(B)\cong\ZZ$. After choosing orientations, $i_*$ is multiplication by a positive integer $m$. The cokernel of the diagonal map $(m,-m):\ZZ\to\ZZ^2$ is $\ZZ\oplus\ZZ_m$, while the displayed exact sequence says it is $\ZZ$. Therefore $m=1$, and $i_*$ is an isomorphism. The reduced result gives the ordinary $H_0$ result as well, since both spaces are nonempty.

If $k=n$, then $S=S^{n-1}$ and $A$ is empty. The embedded $D^n$ has its boundary on $\partial D^n$. Invariance of domain makes its interior image open in $\operatorname{int}D^n$; it is also closed there, since the image of the whole disk is compact and its boundary image lies on $\partial D^n$. Hence $D=D^n$, so $B$ is empty too.
:::
