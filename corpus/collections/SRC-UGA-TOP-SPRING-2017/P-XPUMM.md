---
schema: qual/card@1
id: P-XPUMM
kind: problem
title: Homology of $\RP^2\#\RP^2$ via Mayer–Vietoris
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
  note: Checked the statement against problem 8 of the official UGA Spring 2017 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the Mayer-Vietoris map using that the boundary circle of a Mobius band represents twice its core generator.
---

::: problem
Use the circle along which the connected sum is performed and the Mayer-Vietoris long exact sequence to compute the homology of $\RP^2 \# \RP^2$.
:::

::: {.solution}
Let
\[
X=\RP^2\#\RP^2.
\]
Write $M_1$ and $M_2$ for the two copies of $\RP^2$ with an open disk removed, so each $M_i$ is a Mobius band and
\[
X=M_1\cup_C M_2,
\]
where
\[
C=\partial M_1=\partial M_2\cong S^1
\]
is the connected-sum circle.

<1>1. Mayer-Vietoris may be applied with pieces homotopy equivalent to $M_1$, $M_2$, and $C$.
::: {.proof}
Choose a collar
\[
C\times(-\varepsilon,\varepsilon)\subset X
\]
of the gluing circle, with $M_1$ on one side and $M_2$ on the other.
Enlarge the interiors of $M_1$ and $M_2$ slightly across the collar to obtain open sets $U,V\subset X$ such that
\[
X=U\cup V,
\qquad
U\simeq M_1,
\qquad
V\simeq M_2,
\qquad
U\cap V\simeq C.
\]
Hence the Mayer-Vietoris sequence for $U\cup V$ can be identified with the one obtained from $M_1,M_2,C$.
:::

<1>2. For a Mobius band $M$ with boundary circle $C$, the inclusion
\[
i:C\hookrightarrow M
\]
induces multiplication by $2$ on first homology, up to the choice of generator:
\[
i_*:H_1(C;\ZZ)\longrightarrow H_1(M;\ZZ),
\qquad
i_*(1)=2.
\]
::: {.proof}
Use the standard model
\[
M=[0,1]\times[-1,1]/(0,t)\sim(1,-t).
\]
The core
\[
[0,1]\times\{0\}/\sim
\]
is a deformation retract of $M$ and represents a generator of
\[
H_1(M;\ZZ)\cong\ZZ.
\]
The boundary of the rectangle becomes a single circle in $M$.
Traversing this boundary circle once passes once along each of the two horizontal boundary edges; under the deformation retraction to the core, these two passages concatenate with the same orientation.
Thus the boundary circle winds twice around the core, so its homology class is twice the core generator.
:::

<1>3. The relevant part of the Mayer-Vietoris sequence is
\[
0\longrightarrow H_2(X;\ZZ)
\longrightarrow \ZZ
\xrightarrow{\ \phi\ }
\ZZ\oplus\ZZ
\longrightarrow H_1(X;\ZZ)
\longrightarrow \ZZ
\xrightarrow{\ \psi\ }
\ZZ\oplus\ZZ,
\]
where, after choosing orientations,
\[
\phi(n)=(2n,-2n)
\]
and
\[
\psi(n)=(n,-n).
\]
::: {.proof}
Each Mobius band deformation retracts to a circle, so
\[
H_2(M_i;\ZZ)=0,
\qquad
H_1(M_i;\ZZ)\cong\ZZ,
\qquad
H_0(M_i;\ZZ)\cong\ZZ.
\]
Also
\[
H_1(C;\ZZ)\cong\ZZ,
\qquad
H_0(C;\ZZ)\cong\ZZ.
\]
The Mayer-Vietoris map on $H_1(C)$ is the difference of the two inclusion maps.
By <1>2, each inclusion has degree $2$ on first homology, so signs may be chosen to give
\[
\phi(n)=(2n,-2n).
\]

Since $C,M_1,M_2$ are connected, the map on $H_0$ induced by the two inclusions is, with the Mayer-Vietoris sign convention,
\[
\psi(n)=(n,-n).
\]
:::

<1>4. The second homology vanishes:
\[
H_2(X;\ZZ)=0.
\]
::: {.proof}
The map
\[
\phi:\ZZ\longrightarrow\ZZ^2,
\qquad
n\longmapsto(2n,-2n),
\]
is injective.
Exactness at $H_1(C;\ZZ)$ therefore gives
\[
H_2(X;\ZZ)=\ker\phi=0.
\]
:::

<1>5. The first homology is
\[
H_1(X;\ZZ)\cong\ZZ\oplus\ZZ/2.
\]
::: {.proof}
The map
\[
\psi:\ZZ\longrightarrow\ZZ^2,
\qquad
n\longmapsto(n,-n),
\]
is injective.
Exactness therefore says that the map
\[
\ZZ^2\longrightarrow H_1(X;\ZZ)
\]
is surjective with kernel $\operatorname{im}\phi$.
Hence
\[
H_1(X;\ZZ)
\cong
\frac{\ZZ^2}{\langle(2,-2)\rangle}.
\]
The vector $(1,-1)$ is primitive in $\ZZ^2$, so extending it to a basis gives
\[
\frac{\ZZ^2}{\langle2(1,-1)\rangle}
\cong
\ZZ\oplus\ZZ/2.
\]
:::

<1>6. Thus the integral homology of $\RP^2\#\RP^2$ is
\[
\boxed{
H_n(X;\ZZ)\cong
\begin{cases}
\ZZ, & n=0,\\
\ZZ\oplus\ZZ/2, & n=1,\\
0, & n\ge2.
\end{cases}}
\]
::: {.proof}
The space $X$ is connected, so $H_0(X;\ZZ)\cong\ZZ$.
The groups in degrees $1$ and $2$ were computed in <1>4 and <1>5. Since $X$ is a closed surface, it has the homotopy type of a $2$-dimensional CW complex, so its homology vanishes in degrees greater than $2$.
:::
:::
