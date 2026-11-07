---
schema: qual/card@1
id: E-HAT-2.2-29
kind: problem
title: Homology of double of genus-$g$ surface via Mayer–Vietoris
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 29; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete Mayer--Vietoris/Wang-sequence calculation checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the double: $R$ is a genus-$g$ handlebody, $i_*:\ZZ^{2g}\to\ZZ^g$ is onto with kernel
    $\ZZ^g$, and Mayer-Vietoris gives $H_3=\ZZ$, $H_2=\ZZ^g$ from the kernel of $(i_*,-i_*)$ and
    $H_1=\ZZ^g$ from its anti-diagonal cokernel. Read the relative groups from the long exact
    sequence of $(R,M_g)$: $H_3=\ZZ$, $H_2=\ZZ^g$, $H_1=H_0=0$, consistent with Lefschetz duality
    for a compact $3$-manifold with boundary.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 29 as printed on p. 158. Recomputed both answers: with
    H_1(M_g)=Z^2g onto H_1(R)=Z^g, Mayer-Vietoris gives H_3(X)=coker(H_2(M_g)->0)=Z,
    H_2(X)=ker(i_*,-i_*)=ker i_* = Z^g, H_1(X)=(Z^g+Z^g)/anti-diagonal = Z^g and H_0(X)=Z,
    which is #_g (S^1 x S^2) as expected; the pair sequence gives H_3(R,M_g)=Z,
    H_2(R,M_g)=ker i_* = Z^g, H_1(R,M_g)=0, H_0(R,M_g)=0. The handlebody facts are now stated
    with their reason - R is a regular neighborhood of a wedge of g circles and the meridians
    bound disks while the longitudes are the core circles of the 1-handles - and the
    Mayer-Vietoris sequence is cited to p. 149 and the pair sequence to Theorem 2.16 p. 117.
    What is not covered: Hatcher does not develop handlebodies, so R = wedge of g circles and
    the meridian/longitude description are stated as standard facts about the standard
    embedding rather than proved here.
---

::: {.problem}
The surface $M_g$ of genus $g$, embedded in $\RR^3$ in the standard way, bounds a compact region $R$.
Two copies of $R$, glued together by the identity map between their boundary surfaces $M_g$, form a closed 3-manifold $X$.
Compute the homology groups of $X$ via the Mayer–Vietoris sequence for this decomposition of $X$ into two copies of $R$.
Also compute the relative groups $H_i(R, M_g)$.
:::

::: {.solution}
The region $R$ bounded by the standard genus-$g$ surface is the standard genus-$g$ handlebody, a regular neighborhood of a wedge of $g$ circles in $\RR^3$, so
$$
R\simeq\bigvee^g S^1,
$$
by deformation retraction onto that spine. Hence
$$
H_0(R)=\ZZ,
\qquad
H_1(R)=\ZZ^g,
\qquad
H_i(R)=0\quad(i\ge2).
$$
The homology of $M_g$ is that of Example 2.36 (p. 141):
$$
H_0(M_g)=\ZZ,\qquad H_1(M_g)=\ZZ^{2g},\qquad H_2(M_g)=\ZZ.
$$
The inclusion
$$
i:M_g=\partial R\hookrightarrow R
$$
induces a surjection
$$
i_*:H_1(M_g)=\ZZ^{2g}\twoheadrightarrow H_1(R)=\ZZ^g
$$
whose kernel has rank $g$: the meridians bound disks in $R$ and so die, while the longitudes are the core circles of the $g$ one-handles and form a basis of $H_1(R)$. This is the usual symplectic basis of $H_1(M_g)$, $g$ meridians and $g$ longitudes.

The Mayer--Vietoris sequence for the decomposition is the one in the subsection of that name beginning on p. 149, which applies because the interiors of $R_1$ and $R_2$ together with a collar of $M_g$ cover $X$.

Let
$$
X=R_1\cup_{M_g}R_2
$$
be the double.

::: pf

::: pf-step

The homology of $X$ is
$$
H_i(X)\cong
\begin{cases}
\ZZ,&i=0,3,\\
\ZZ^g,&i=1,2,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

Mayer--Vietoris, applied to $X=R_1\cup R_2$ with intersection $M_g$, gives in high degrees
$$
0\to H_3(X)\to H_2(M_g)=\ZZ
\to H_2(R_1)\oplus H_2(R_2)=0,
$$
so $H_3(X)\cong\ZZ$. Next,
$$
0\to H_2(X)\to H_1(M_g)
\xrightarrow{(i_*,-i_*)}
H_1(R_1)\oplus H_1(R_2)
\to H_1(X)\to0.
$$
The kernel of $(i_*,-i_*)$ is exactly $\ker i_*\cong\ZZ^g$, hence
$$
H_2(X)\cong\ZZ^g.
$$
Since $i_*$ is onto, the image of $(i_*,-i_*)$ is the anti-diagonal copy of $\ZZ^g$ in $\ZZ^g\oplus\ZZ^g$. Its cokernel is $\ZZ^g$, so
$$
H_1(X)\cong\ZZ^g.
$$
Finally $X$ is connected, giving $H_0(X)=\ZZ$.

:::

:::

::: pf-step

The relative homology of the handlebody pair is
$$
H_i(R,M_g)\cong
\begin{cases}
\ZZ,&i=3,\\
\ZZ^g,&i=2,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

The long exact sequence of the pair, that of Theorem 2.16 (p. 117), begins
$$
0=H_3(R)\to H_3(R,M_g)\to H_2(M_g)=\ZZ\to H_2(R)=0,
$$
so $H_3(R,M_g)\cong\ZZ$. The next portion is
$$
0\to H_2(R,M_g)\to H_1(M_g)
\xrightarrow{i_*}H_1(R)
\to H_1(R,M_g)
\to H_0(M_g)\xrightarrow{\cong}H_0(R).
$$
Since $i_*$ is surjective with kernel $\ZZ^g$, exactness gives
$$
H_2(R,M_g)\cong\ZZ^g,
\qquad
H_1(R,M_g)=0,
\qquad
H_0(R,M_g)=0.
$$

:::

:::

:::

:::
