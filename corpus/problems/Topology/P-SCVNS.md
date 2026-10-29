---
schema: qual/card@1
id: P-SCVNS
kind: problem
title: Connected covering spaces of $\RP^2\vee\RP^2$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
Describe all connected covering spaces of $\RP^2 \vee \RP^2$.
:::

::: {.solution}
Let $X = A \vee B$ with $A \cong B \cong \RP^2$, joined at the point $x_0$.
Let $a$ and $b$ be the generators of $\pi_1(A, x_0) \cong C_2$ and $\pi_1(B, x_0) \cong C_2$.

::: pf

::: pf-step
$\pi_1(X, x_0) \cong C_2 * C_2 \cong D_\infty = \langle r, s \mid s^2 = 1,\ srs = r^{-1}\rangle$, with $s = a$ and $r = ab$.

::: pf-proof
Van Kampen's theorem, applied to open neighbourhoods of $A$ and $B$ that deformation retract onto them and meet in a contractible set, gives $\pi_1(X) \cong \langle a, b \mid a^2, b^2 \rangle$.
With $s = a$ and $r = ab$ we have $srs = a \cdot ab \cdot a = ba = r^{-1}$, and $a = s$, $b = sr$ recover the generators.
:::

:::

::: {.pf-step #s2}
Connected covering spaces of $X$, up to isomorphism, correspond to conjugacy classes of subgroups of $D_\infty$, and the number of sheets is the index.

::: pf-proof
The space $X$ is connected, locally path connected, and semilocally simply connected, so the classification of covering spaces applies.
:::

:::

::: {.pf-step #s3}
Every subgroup $H \leq D_\infty$ is one of
$$
\{1\},\qquad \langle r^n\rangle\ (n\ge1),\qquad \langle r^k s\rangle\ (k \in \ZZ),\qquad \langle r^n,r^k s\rangle\ (n\ge1,\ k \in \ZZ).
$$

::: pf-proof
The subgroup $\langle r\rangle\cong\ZZ$ has index $2$ in $D_\infty$, and every element outside it is a reflection $r^k s$, of order $2$.
If $H\subseteq\langle r\rangle$, then $H$ is trivial or $\langle r^n\rangle$.
Otherwise $H$ contains a reflection $r^k s$, and $H = (H \cap \langle r \rangle) \cup (H \cap \langle r \rangle) r^k s$.
If $H \cap \langle r\rangle$ is trivial, then $H=\langle r^k s\rangle\cong C_2$; if it is $\langle r^n\rangle$, then $H=\langle r^n,r^k s\rangle\cong D_\infty$.
:::

:::

::: {.pf-step #s4}
The subgroups $\langle r^n\rangle$ are normal and pairwise distinct, of index $2n$; the subgroups $\langle r^k s\rangle$, of infinite index, form exactly two conjugacy classes, represented by $\langle a \rangle = \langle s\rangle$ and $\langle b \rangle$, which is conjugate to $\langle rs\rangle$.

::: pf-proof
Conjugation by $r^m$ sends $r^k s$ to $r^{k+2m}s$, and conjugation by $s$ sends $r^k s$ to $r^{-k} s$, so the parity of $k$ is the only conjugacy invariant of $\langle r^k s \rangle$.
We have $a b a^{-1} = rs$, so $\langle b \rangle$ is conjugate to $\langle rs \rangle$.
Each $\langle r^n \rangle$ is characteristic in $\langle r \rangle$, which is normal, and $[D_\infty : \langle r^n \rangle] = 2 \cdot n$.
:::

:::

::: {.pf-step #s5}
The subgroups $H_{n,k}=\langle r^n,r^k s\rangle$ have index $n$, and $k$ matters only modulo $n$.
For $n$ odd they form one conjugacy class; for $n$ even they form exactly two, represented by $k=0$ and $k=1$.

::: pf-proof
The subgroup $H_{n,k}$ is the union of $\langle r^n \rangle$ and one coset of it consisting of reflections, so its index is $2n/2 = n$.
Replacing the reflection generator by $r^{n\ell}r^k s$ changes $k$ by a multiple of $n$.
By the conjugation formulas of step [](#s4){.pf-ref}, the conjugacy classes are the orbits on $\ZZ/n$ of $k\mapsto k+2m$ and $k\mapsto-k$.
When $n$ is odd, $2$ is invertible modulo $n$, giving one orbit; when $n$ is even, parity is preserved, giving two orbits.
:::

:::

::: pf-step
The connected covers of $X$ are the following spaces.
In each, a sphere $S^2$ covers $A$ or $B$ by the antipodal quotient, an $\RP^2$ covers $A$ or $B$ homeomorphically, and consecutive pieces are joined at single points, each sphere meeting its two neighbours at an antipodal pair of points.

(i) The trivial subgroup: the universal cover, a bi-infinite chain $\cdots \vee S^2 \vee S^2 \vee S^2 \vee \cdots$ of spheres, alternately covering $A$ and $B$.

(ii) $\langle r^n \rangle$, $n \geq 1$: a necklace of $2n$ spheres joined cyclically, alternately covering $A$ and $B$; a $2n$-sheeted normal cover.

(iii) $\langle r^k s \rangle$: a one-sided infinite chain $\RP^2 \vee S^2 \vee S^2 \vee \cdots$, whose end $\RP^2$ maps homeomorphically onto $A$ (for $\langle a \rangle$) or onto $B$ (for $\langle b \rangle$); two covers.

(iv) $H_{n,k}$, $n \geq 1$: a finite chain $\RP^2 \vee S^2 \vee \cdots \vee S^2 \vee \RP^2$ with $n-1$ spheres, an $n$-sheeted cover.
For $n$ odd the two end copies of $\RP^2$ cover different summands, and there is one such cover; for $n$ even both ends cover the same summand, $A$ or $B$, and there are two.
For $n = 1$ this is $X$ itself.

::: pf-proof
Over $A$, the preimage of $A$ in a connected cover is a disjoint union of copies of $S^2$ and $\RP^2$, the connected covers of $\RP^2$, and similarly over $B$; each copy of $S^2$ contains two preimages of $x_0$ and each copy of $\RP^2$ contains one.
Since each preimage of $x_0$ lies on exactly one piece over $A$ and one over $B$, the pieces form a connected chain or cycle, alternating between pieces over $A$ and over $B$, in which spheres have two neighbours and copies of $\RP^2$ have one.
So a connected cover is a bi-infinite chain of spheres, a cycle of an even number $2n$ of spheres, a one-sided infinite chain ending in one $\RP^2$, or a finite chain with an $\RP^2$ at each end.
Counting preimages of a point of $A \setminus \{x_0\}$ gives the sheet numbers $\infty$, $2n$, $\infty$, and $n$ when the finite chain has $n - 1$ spheres.
The end of a one-sided chain covers $A$ or $B$; a finite chain with $n+1$ pieces alternating between $A$ and $B$ has ends over different summands exactly when $n$ is odd.
These spaces are pairwise non-isomorphic over $X$ and match, with the same sheet numbers and the same count in each case, the conjugacy classes of steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, and [](#s5){.pf-ref}, which by step [](#s2){.pf-ref} classify all connected covers.
:::

:::

:::

:::
