---
schema: qual/card@1
id: P-XRGV7
kind: problem
title: Klein bottle as two annuli, and its homology via Mayer–Vietoris
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 6 of the official UGA Fall 2015 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the mapping-torus annulus cover, the identity/reflection transition maps on the two overlap components, and the resulting Mayer–Vietoris matrices and Smith normal form.
---

::: problem
Express a Klein bottle as the union of two annuli.

Use the Mayer–Vietoris sequence and this decomposition to compute its homology.
:::

::: {.solution}
Write the Klein bottle as the mapping torus of the reflection
\[
r:S^1\longrightarrow S^1,
\qquad
r(z)=\overline z:
\qquad
K=(S^1\times[0,1])/((z,0)\sim(r(z),1)).
\]
Let
\[
p:K\longrightarrow S^1,
\qquad
p([z,t])=e^{2\pi i t},
\]
be the mapping-torus projection.

<1>1. The Klein bottle is the union of two annuli $U$ and $V$ whose intersection is the disjoint union of two annuli.
::: {.proof}
Choose two closed arcs $A,B\subset S^1$ such that
\[
A\cup B=S^1,
\qquad
\operatorname{int}(A)\cup\operatorname{int}(B)=S^1,
\]
and $A\cap B$ has exactly two connected components $C_0,C_1$, each an arc.
Set
\[
U=p^{-1}(A),
\qquad
V=p^{-1}(B).
\]
The mapping torus is an $S^1$-bundle over $S^1$ with monodromy $r$.
Over an arc the bundle is trivial, hence
\[
U\cong S^1\times[0,1],
\qquad
V\cong S^1\times[0,1].
\]
Thus $U$ and $V$ are annuli.
Likewise
\[
U\cap V=p^{-1}(C_0)\sqcup p^{-1}(C_1)
\]
is the disjoint union of two annuli.
Because the interiors of $U$ and $V$ cover $K$, this is an excisive pair and the Mayer–Vietoris sequence applies.
:::

<1>2. With suitable generators, the Mayer–Vietoris map
\[
\alpha:H_1(U\cap V)\longrightarrow H_1(U)\oplus H_1(V)
\]
is represented by
\[
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix}.
\]
::: {.proof}
Each annulus deformation retracts onto a fiber circle, so
\[
H_1(U\cap V)\cong\ZZ^2,
\qquad
H_1(U)\oplus H_1(V)\cong\ZZ^2.
\]
Choose fiber generators $x_0,x_1$ on the two components of $U\cap V$, and generators $a,b$ for $U,V$.

Choose the trivializations so that on the overlap component $C_0$ away from the mapping-torus seam the transition function is the identity, while on the component $C_1$ crossing the seam it is the reflection $r$.
The reflection has degree $-1$ on $S^1$.
Thus, for the Mayer–Vietoris map $(i_*,-j_*)$,
\[
\alpha(x_0)=(a,-b),
\qquad
\alpha(x_1)=(a,b),
\]
which gives the displayed matrix.
:::

<1>3. One has
\[
H_2(K;\ZZ)=0
\qquad\text{and}\qquad
\operatorname{coker}(\alpha)\cong\ZZ/2\ZZ.
\]
::: {.proof}
The relevant part of Mayer–Vietoris begins
\[
0
\longrightarrow H_2(K)
\longrightarrow \ZZ^2
\xrightarrow{\alpha}
\ZZ^2.
\]
The matrix in <1>2 has determinant $2$, so $\alpha$ is injective over $\ZZ$ and therefore $H_2(K)=0$.

Its entries have greatest common divisor $1$ and its determinant has absolute value $2$.
Hence its Smith normal form is
\[
\operatorname{diag}(1,2),
\]
so
\[
\operatorname{coker}(\alpha)\cong\ZZ/2\ZZ.
\]
:::

<1>4. The map
\[
\beta:H_0(U\cap V)\longrightarrow H_0(U)\oplus H_0(V)
\]
has kernel isomorphic to $\ZZ$ and cokernel isomorphic to $\ZZ$.
::: {.proof}
Both $U$ and $V$ are connected, while $U\cap V$ has two components.
Thus, under the standard generators,
\[
\beta:\ZZ^2\longrightarrow\ZZ^2,
\qquad
\beta(m,n)=(m+n,-m-n).
\]
Therefore
\[
\ker\beta=\{(m,-m):m\in\ZZ\}\cong\ZZ,
\]
and
\[
\operatorname{coker}\beta\cong\ZZ.
\]
:::

<1>5. The integral homology of the Klein bottle is
\[
\boxed{
H_n(K;\ZZ)\cong
\begin{cases}
\ZZ,&n=0,\\
\ZZ\oplus\ZZ/2\ZZ,&n=1,\\
0,&n\ge2.
\end{cases}}
\]
::: {.proof}
Exactness around $H_1(K)$ gives
\[
0
\longrightarrow\operatorname{coker}(\alpha)
\longrightarrow H_1(K)
\longrightarrow\ker(\beta)
\longrightarrow0.
\]
By <1>3 and <1>4 this is
\[
0\longrightarrow\ZZ/2\ZZ
\longrightarrow H_1(K)
\longrightarrow\ZZ
\longrightarrow0.
\]
Since $\ZZ$ is free, the sequence splits, so
\[
H_1(K)\cong\ZZ\oplus\ZZ/2\ZZ.
\]
Also $H_0(K)\cong\operatorname{coker}(\beta)\cong\ZZ$, <1>3 gives $H_2(K)=0$, and Mayer–Vietoris gives $H_n(K)=0$ for $n\ge3$ because the annuli and their intersection have no homology in those degrees.
:::
:::
