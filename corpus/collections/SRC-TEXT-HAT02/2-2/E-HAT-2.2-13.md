---
schema: qual/card@1
id: E-HAT-2.2-13
kind: problem
title: 2-complex from $S^1$ with two 2-cells of degrees 2 and 3
classification:
  areas:
  - topology
  topics:
  - Homology
  - CW Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 13 and the published correction to part (b); the local statement already contains the corrected wording.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Enumerated all subcomplexes, computed quotient cellular homology, and tracked the quotient maps on top homology.
---

Let $X$ be the 2 complex obtained from $S^1$ with its usual cell structure by attaching two 2 cells by maps of degrees 2 and 3, respectively.

(a) Compute the homology groups of all the subcomplexes $A \subset X$ and the corresponding quotient complexes $X/A$.

(b) Show that $X \simeq S^2$ and that the only subcomplex $A \subset X$ for which the quotient map $X \to X/A$ is a homotopy equivalence is the trivial subcomplex, the 0 cell.

::: {.solution}
Let $e^0,e^1,e^2_2,e^2_3$ denote the cells, where the subscripts record the degrees of the two attaching maps. The cellular chain complex of $X$ is
\[
0\longrightarrow \mathbb Z^2
\xrightarrow{d_2}\mathbb Z
\xrightarrow{0}\mathbb Z\longrightarrow0,
\qquad
 d_2(a,b)=2a+3b.
\]
Hence
\[
H_2(X)=\ker d_2=\mathbb Z(3,-2),
\qquad H_1(X)=0,
\qquad H_0(X)=\mathbb Z.
\]

<1>1. The subcomplexes of $X$ are exactly
\[
\{e^0\},\quad
S^1=e^0\cup e^1,\quad
A_2=S^1\cup e^2_2,\quad
A_3=S^1\cup e^2_3,\quad
X.
\]
Their homology groups are
\[
\begin{array}{c|ccc}
A&H_0&H_1&H_2\\ \hline
\{e^0\}&\mathbb Z&0&0\\
S^1&\mathbb Z&\mathbb Z&0\\
A_2&\mathbb Z&\mathbb Z_2&0\\
A_3&\mathbb Z&\mathbb Z_3&0\\
X&\mathbb Z&0&\mathbb Z.
\end{array}
\]
::: {.proof}
A subcomplex containing a $2$-cell must contain its attaching circle, hence $e^1$. This gives the displayed list. The chain complexes for $A_2$ and $A_3$ are respectively
\[
0\to\mathbb Z\xrightarrow{2}\mathbb Z\to\mathbb Z\to0
\]
and
\[
0\to\mathbb Z\xrightarrow{3}\mathbb Z\to\mathbb Z\to0,
\]
which give the stated groups. The groups for $X$ follow from the cellular complex above.
:::

<1>2. The quotient spaces and their homology are as follows:
\[
X/\{e^0\}=X,
\qquad
X/S^1\cong S^2\vee S^2,
\qquad
X/A_2\cong S^2,
\qquad
X/A_3\cong S^2,
\qquad
X/X=\mathrm{pt}.
\]
Thus
\[
\widetilde H_2(X/S^1)\cong\mathbb Z^2,
\quad
\widetilde H_2(X/A_2)\cong\mathbb Z,
\quad
\widetilde H_2(X/A_3)\cong\mathbb Z,
\]
and all other reduced homology groups of these three quotients vanish.
::: {.proof}
Collapsing the $1$-skeleton turns each $2$-cell into a $2$-sphere, giving $S^2\vee S^2$. If $A_2$ is collapsed, only the interior of $e^2_3$ remains, with its entire boundary collapsed, giving $S^2$; similarly for $A_3$.
:::

<1>3. The space $X$ is homotopy equivalent to $S^2$.
::: {.proof}
First attach the degree-$2$ cell, obtaining $A_2$. Its fundamental group is
\[
\pi_1(A_2)\cong\mathbb Z_2.
\]
The degree-$3$ attaching loop for the second $2$-cell represents the same element of this group as a degree-$1$ loop, since $3\equiv1\pmod2$. Hence these two attaching maps are homotopic in $A_2$. Replacing the degree-$3$ attaching map by the homotopic degree-$1$ attaching map does not change the homotopy type of the adjunction space.

With this replacement, $S^1\cup e^2_3$ is a disk, so the remaining degree-$2$ cell is attached to a contractible disk along a loop that is nullhomotopic there. Therefore the resulting space is homotopy equivalent to
\[
D^2\vee S^2\simeq S^2.
\]
Thus $X\simeq S^2$.
:::

<1>4. For $A=A_2$, the quotient map
\[
q_2:X\to X/A_2\cong S^2
\]
induces multiplication by $-2$ on $H_2$, up to orientation; for $A=A_3$, the quotient map induces multiplication by $3$, up to orientation.
::: {.proof}
The generator of $H_2(X)$ is the cellular cycle
\[
3e^2_2-2e^2_3.
\]
After collapsing $A_2$, the first term disappears and the second $2$-cell generates $H_2(X/A_2)$, so
\[
(q_2)_*(3,-2)=-2.
\]
After collapsing $A_3$, only the first cell survives, giving
\[
(q_3)_*(3,-2)=3.
\]
Changing orientations changes only the signs.
:::

<1>5. The quotient map $X\to X/A$ is a homotopy equivalence only for the trivial subcomplex $A=\{e^0\}$.
::: {.proof}
For $A=S^1$, the quotient has $H_2\cong\mathbb Z^2$, unlike $H_2(X)\cong\mathbb Z$. For $A=A_2$ or $A=A_3$, the quotient is a sphere, but by <1>4 the induced map on $H_2$ is multiplication by $2$ or $3$, not an isomorphism. For $A=X$ the quotient is a point. Finally collapsing the single $0$-cell does nothing: $X/\{e^0\}$ is canonically homeomorphic to $X$. Hence precisely the trivial subcomplex gives a quotient homotopy equivalence.
:::
:::
