---
schema: qual/card@1
id: P-AMD-M3CYGD2R
kind: problem
title: Mayer-Vietoris homology of $\RP^2$, $T^2$, the Klein bottle, and $S^1\cup_{z^n}B^2$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Surfaces
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: >-
    Restored against UCSD_290_F14_sheet7.pdf, problem 1. The previous card
    omitted the punctured-torus subproblem and mislabeled the source's twisted
    two-cylinder Klein-bottle construction as T^2.
---

::: {.problem}
Use the Mayer-Vietoris sequence to calculate the integral homology of the following spaces.

1. $\RP^2$, written as a Möbius strip $M$ union a disk along their boundary.

2. $T^2$, written as a punctured torus (homotopy-equivalent to $S^1\vee S^1$) union a disk along the boundary circle.

3. The Klein bottle, written as the twisted union of two cylinders $S^1\times I$: on one overlap circle the gluing is the identity and on the other it is complex conjugation $z\mapsto\bar z$.

4. $S^1\cup_{z^n}B^2$, where the boundary circle of $B^2$ is attached to $S^1$ by $z\mapsto z^n$.
:::

::: {.solution}
All homology groups below have coefficients in $\ZZ$.

<1>1. For $\RP^2=M\cup D^2$,
$$
H_0(\RP^2)=\ZZ,\qquad H_1(\RP^2)=\ZZ/2,\qquad H_i(\RP^2)=0\quad(i\ge2).
$$
::: {.proof}
Take collar neighborhoods so that the intersection deformation retracts to the common boundary circle $S^1$. We have
$$
H_1(S^1)\cong\ZZ,\qquad H_1(M)\cong\ZZ,\qquad H_1(D^2)=0.
$$
The boundary circle of a Möbius strip runs twice around its core, so the inclusion
$$
H_1(S^1)\longrightarrow H_1(M)
$$
is multiplication by $2$. Since all three spaces are connected, the map
$$
H_0(S^1)\longrightarrow H_0(M)\oplus H_0(D^2)
$$
is injective. The relevant Mayer-Vietoris segment is therefore
$$
0\longrightarrow H_2(\RP^2)\longrightarrow\ZZ
\xrightarrow{\times2}\ZZ
\longrightarrow H_1(\RP^2)\longrightarrow0.
$$
Hence $H_2=0$ and $H_1\cong\ZZ/2$. Connectedness gives $H_0\cong\ZZ$, and there is no homology above degree $2$.
:::

<1>2. For the torus,
$$
H_0(T^2)=\ZZ,\qquad H_1(T^2)=\ZZ^2,\qquad H_2(T^2)=\ZZ,
$$
and $H_i(T^2)=0$ for $i>2$.
::: {.proof}
Let $P=T^2\setminus\operatorname{int}(D^2)$ be the punctured torus. Then
$$
P\simeq S^1\vee S^1,\qquad H_1(P)\cong\ZZ^2,\qquad H_2(P)=0.
$$
Write $T^2=P\cup D^2$, with intersection a collar of $\partial P\cong S^1$. Under the deformation retraction $P\simeq S^1\vee S^1$, the boundary loop represents the commutator $aba^{-1}b^{-1}$, so its class vanishes in
$$
H_1(P)=\pi_1(P)^{\mathrm{ab}}.
$$
Thus the Mayer-Vietoris map
$$
H_1(S^1)\longrightarrow H_1(P)\oplus H_1(D^2)
$$
is zero. As in <1>1, the $H_0$ map is injective. Hence exactness gives
$$
0\longrightarrow H_2(T^2)\longrightarrow\ZZ
\xrightarrow{0}\ZZ^2
\longrightarrow H_1(T^2)\longrightarrow0,
$$
which yields $H_2(T^2)\cong\ZZ$ and $H_1(T^2)\cong\ZZ^2$.
:::

<1>3. For the Klein bottle $K$,
$$
H_0(K)=\ZZ,\qquad H_1(K)=\ZZ\oplus\ZZ/2,
\qquad H_i(K)=0\quad(i\ge2).
$$
::: {.proof}
Let $A$ and $B$ be the two cylinder pieces. Each deformation retracts to a circle, while
$$
A\cap B\simeq S^1\sqcup S^1.
$$
Choose generators $e_0,e_1$ for
$$
H_1(A\cap B)\cong\ZZ^2
$$
and generators $a,b$ for $H_1(A)\oplus H_1(B)\cong\ZZ^2$. Orient the first overlap so that both inclusions have degree $+1$. On the second overlap the inclusion into $A$ still has degree $+1$, while the twisted gluing $z\mapsto\bar z$ has degree $-1$ into $B$. With the Mayer-Vietoris sign convention $(i_*,-j_*)$, the $H_1$ map is therefore represented, up to changing basis signs, by
$$
\phi_1=
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix}.
$$
Its determinant is $2$, so $\ker\phi_1=0$ and
$$
\operatorname{coker}\phi_1\cong\ZZ/2.
$$

On $H_0$, both components of $A\cap B$ map to the unique component of each cylinder, so
$$
\phi_0:\ZZ^2\longrightarrow\ZZ^2,
\qquad
(x,y)\longmapsto(x+y,-x-y).
$$
Thus $\ker\phi_0\cong\ZZ$ and $\operatorname{coker}\phi_0\cong\ZZ$. The Mayer-Vietoris sequence gives
$$
0\to H_2(K)\to\ZZ^2\xrightarrow{\phi_1}\ZZ^2
\to H_1(K)\to\ZZ^2\xrightarrow{\phi_0}\ZZ^2
\to H_0(K)\to0.
$$
Hence $H_2(K)=0$, $H_0(K)\cong\ZZ$, and there is a short exact sequence
$$
0\longrightarrow\ZZ/2\longrightarrow H_1(K)
\longrightarrow\ZZ\longrightarrow0.
$$
It splits because $\ZZ$ is free, so
$$
H_1(K)\cong\ZZ\oplus\ZZ/2.
$$
:::

<1>4. Let
$$
Y_n=S^1\cup_{z^n}B^2.
$$
Then
$$
H_0(Y_n)=\ZZ,\qquad
H_1(Y_n)=\operatorname{coker}(\times n)=\ZZ/n\ZZ,\qquad
H_2(Y_n)=\ker(\times n),
$$
and $H_i(Y_n)=0$ for $i>2$. Equivalently,
$$
(H_1,H_2)=
\begin{cases}
(\ZZ/|n|,0),&n\ne0,\\
(\ZZ,\ZZ),&n=0.
\end{cases}
$$
::: {.proof}
Decompose the attached disk into an outer annular collar and an inner disk. Let $A$ be the original $S^1$ together with the outer collar and let $B$ be the inner disk together with a slightly overlapping collar. Then
$$
A\simeq S^1,\qquad B\simeq *,\qquad A\cap B\simeq S^1.
$$
Under the deformation retraction $A\simeq S^1$, the inclusion of $A\cap B$ is the attaching map $z\mapsto z^n$, hence induces multiplication by $n$ on $H_1$. The inclusion into $B$ induces zero on $H_1$. Since the $H_0$ map is injective, Mayer-Vietoris gives
$$
0\longrightarrow H_2(Y_n)\longrightarrow\ZZ
\xrightarrow{\times n}\ZZ
\longrightarrow H_1(Y_n)\longrightarrow0.
$$
Taking kernel and cokernel yields the stated groups, including the previously omitted case $n=0$.
:::

<1>5. Q.E.D.
::: {.proof}
The four Mayer-Vietoris computations in <1>1--<1>4 give all requested homology groups.
:::
:::
