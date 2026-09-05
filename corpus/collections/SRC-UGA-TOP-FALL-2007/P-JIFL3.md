---
schema: qual/card@1
id: P-JIFL3
kind: problem
title: Homology of $S^2$ glued to a torus along an equatorial circle
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Quotient Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 7 of the official UGA Fall 2007 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the Mayer-Vietoris maps induced by the equator inclusion in S^2 and the primitive factor circle in T^2.
---

::: problem
Let $X$ be the space obtained as the quotient of a disjoint union of a 2-sphere $S^2$ and a torus $T = S^1 \times S^1$ by identifying the equator in $S^2$ with a circle $S^1 \times \theset{p}$ in $T$.

Compute the homology groups of $X$.
:::

::: {.solution}
Let
\[
C\cong S^1
\]
denote the circle obtained by identifying the equator of $S^2$ with
\[
S^1\times\{p\}\subset T^2.
\]

<1>1. Mayer--Vietoris may be applied using an open cover $X=U\cup V$ with
\[
U\simeq S^2,
\qquad
V\simeq T^2,
\qquad
U\cap V\simeq C\simeq S^1.
\]
::: {.proof}
The equator in $S^2$ and the circle $S^1\times\{p\}$ in $T^2$ both have annular neighborhoods.
After the two circles are identified, enlarge the images of $S^2$ and $T^2$ slightly across these annuli.
The resulting sets $U$ and $V$ are open, retract respectively onto the sphere and torus, and their intersection retracts onto the common circle $C$.
Thus their homology may be replaced by that of the displayed deformation retracts in the Mayer--Vietoris sequence.
:::

<1>2. The relevant homology groups are
\[
H_k(S^2;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,2,\\
0,&\text{otherwise},
\end{cases}
\]
\[
H_k(T^2;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,2,\\
\ZZ^2,&k=1,\\
0,&\text{otherwise},
\end{cases}
\]
and
\[
H_k(C;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,1,\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
These are the standard integral homology groups of the sphere, torus, and circle.
:::

<1>3. The Mayer--Vietoris map
\[
\Phi:H_1(C)\longrightarrow H_1(S^2)\oplus H_1(T^2)
\]
is injective and has cokernel isomorphic to $\ZZ$.
::: {.proof}
Let $a,b$ be the standard basis of
\[
H_1(T^2;\ZZ)\cong\ZZ^2,
\]
with $a$ represented by the factor circle $S^1\times\{p\}$.
The inclusion of the equator into $S^2$ induces the zero map on $H_1$ because
\[
H_1(S^2)=0.
\]
The inclusion of $C=S^1\times\{p\}$ into the torus sends a generator of $H_1(C)$ to the primitive class $a$.
Hence, up to the irrelevant Mayer--Vietoris sign convention,
\[
\Phi:\ZZ\longrightarrow 0\oplus\ZZ^2,
\qquad
1\longmapsto (0,a).
\]
This map is injective, and
\[
\operatorname{coker}\Phi
\cong
\ZZ^2/\langle a\rangle
\cong\ZZ.
\]
:::

<1>4. One has
\[
H_2(X;\ZZ)\cong\ZZ^2.
\]
::: {.proof}
The degree-$2$ portion of Mayer--Vietoris is
\[
H_2(C)
\longrightarrow
H_2(S^2)\oplus H_2(T^2)
\longrightarrow
H_2(X)
\longrightarrow
H_1(C)
\xrightarrow{\Phi}
H_1(S^2)\oplus H_1(T^2).
\]
Using <1>2, this becomes
\[
0
\longrightarrow
\ZZ^2
\longrightarrow
H_2(X)
\longrightarrow
\ZZ
\xrightarrow{\Phi}
\ZZ^2.
\]
The map $\Phi$ is injective by <1>3, so the image of
\[
H_2(X)\longrightarrow\ZZ
\]
is zero by exactness.
Therefore
\[
\ZZ^2\longrightarrow H_2(X)
\]
is both injective and surjective, hence an isomorphism.
:::

<1>5. One has
\[
H_1(X;\ZZ)\cong\ZZ.
\]
::: {.proof}
The next part of Mayer--Vietoris is
\[
H_1(C)
\xrightarrow{\Phi}
H_1(S^2)\oplus H_1(T^2)
\longrightarrow
H_1(X)
\longrightarrow
H_0(C)
\longrightarrow
H_0(S^2)\oplus H_0(T^2).
\]
All three spaces $C,S^2,T^2$ are connected, so the last map is, up to sign,
\[
\ZZ\longrightarrow\ZZ^2,
\qquad
1\longmapsto(1,-1),
\]
and is injective.
Exactness therefore gives
\[
H_1(X)\cong\operatorname{coker}\Phi.
\]
By <1>3 this cokernel is $\ZZ$.
:::

<1>6. The space $X$ is connected, so
\[
H_0(X;\ZZ)\cong\ZZ,
\]
and
\[
H_k(X;\ZZ)=0
\qquad(k\ge3).
\]
::: {.proof}
The images of $S^2$ and $T^2$ in $X$ are connected and meet along the nonempty circle $C$, so their union $X$ is connected.
Thus $H_0(X)\cong\ZZ$.

For $k\ge3$, the adjacent homology groups of $C$, $S^2$, and $T^2$ in the Mayer--Vietoris sequence vanish by <1>2, except possibly the groups in degree $2$ already used in <1>4.
In particular, the degree-$3$ segment is
\[
0\longrightarrow0\longrightarrow H_3(X)\longrightarrow H_2(C)=0,
\]
so $H_3(X)=0$, and the same vanishing argument applies in all higher degrees.
:::

<1>7. Therefore
\[
H_k(X;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,1,\\
\ZZ^2,&k=2,\\
0,&k\ge3.
\end{cases}
\]
::: {.proof}
This collects <1>4--<1>6.
:::
:::
