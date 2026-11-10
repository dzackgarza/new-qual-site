---
schema: qual/card@1
id: E-S57IX
kind: problem
title: Products of quotient maps with locally compact Hausdorff factors
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 supplementary exercise on nets, printed p.
    188, with the tube lemma, Exercise 29.10 and §22 for composites of quotient maps; both
    parts of the stored statement are answered.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.11, PDF p. 23 for part (a) — its numbering
    continues into the net exercises. Part (a) is the set's lemma with the saturation
    argument written out. Part (b), the theorem on p x q, is not in the set and is proved
    here: factor p x q as (i_B x q) o (p x i_C) and apply (a) twice, to p with Z = C and to
    q with Z = B, the hypotheses being exactly that B and C are locally compact Hausdorff; a
    composite of quotient maps is a quotient map. (tmp/sources/munkres-solutions-positron-
    ch3.pdf).
---

::: {.exercise}

(a) Lemma.
If $p: X \to Y$ is a quotient map and if $Z$ is a locally compact Hausdorff space, then the map

$$
\pi = p \times i_Z: X \times Z \to Y \times Z
$$

is a quotient map.

[Hint: If $\pi^{-1}(A)$ is open and contains $x \times y$, choose open sets $U_1$ and $V$ with $\overline{V}$ compact, such that $x \times y \in U_1 \times V$ and $U_1 \times \overline{V} \subset \pi^{-1}(A)$. Given $U_i \times \overline{V} \subset \pi^{-1}(A)$, use the tube lemma to choose an open set $U_{i+1}$ containing $p^{-1}(p(U_i))$ such that $U_{i+1} \times \overline{V} \subset \pi^{-1}(A)$. Let $U = \bigcup U_i$; show that $U \times V$ is a saturated neighborhood of $x \times y$ that is contained in $\pi^{-1}(A)$.]

An entirely different proof of this result will be outlined in the exercises of §46.

(b) Theorem.
Let $p: A \to B$ and $q: C \to D$ be quotient maps.
If $B$ and $C$ are locally compact Hausdorff spaces, then $p \times q: A \times C \to B \times D$ is a quotient map.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.11, PDF p. 23** (`tmp/sources/munkres-solutions-positron-ch3.pdf`) for part (a) — its numbering runs past the ten exercises of §29 into the supplementary exercises on nets, where this is the last of them — with the saturation argument written out, as their paragraph only asserts the last step. Part (b) is not in that set and is proved below from part (a).

(a) **Lemma.** If $p:X\to Y$ is a quotient map and $Z$ is locally compact Hausdorff, then $\pi=p\times i_{Z}:X\times Z\to Y\times Z$ is a quotient map.

*Proof.* $\pi$ is continuous and surjective. Let $A\subset Y\times Z$ with $\pi^{-1}(A)$ open in $X\times Z$; we show $A$ open.

Let $y\times z\in A$ and $x\in p^{-1}(y)$; since $Z$ is locally compact Hausdorff there is a compact neighbourhood $C$ of $z$ (Exercise 29.10). Put
$$
B=\big\{x'\in X\ \mid\ \{x'\}\times C\subset\pi^{-1}(A)\big\},
$$
so $x\in B$ because $\pi(x,c)=y\times c\in A$ for every $c\in C$.

$B$ is open: if $x'\in B$ then $\{x'\}\times C\subset\pi^{-1}(A)$, and by the tube lemma applied in $X\times C$ (with $C$ compact) there is a neighbourhood $U$ of $x'$ with $U\times C\subset\pi^{-1}(A)$, i.e. $U\subset B$.

$B$ is saturated: if $x'\in B$ and $p(x'')=p(x')$, then for $c\in C$ one has $\pi(x'',c)=p(x'')\times c=p(x')\times c=\pi(x',c)\in A$, so $x''\in B$.

So $p(B)$ is open in $Y$, $p$ being a quotient map and $B$ open and saturated. And
$$
(y,z)\in p(B)\times\operatorname{int}C\subset A,
$$
since $y'=p(x')\in p(B)$ and $z'\in C$ give $y'\times z'=\pi(x',z')\in A$. So every point of $A$ has an open neighbourhood inside $A$, and $A$ is open. $\square$

(b) **Theorem.** If $p:A\to B$ and $q:C\to D$ are quotient maps with $B$ and $C$ locally compact Hausdorff, then $p\times q:A\times C\to B\times D$ is a quotient map.

*Proof.* Factor $p\times q$ as the composite
$$
A\times C\ \xrightarrow{\ p\times i_{C}\ }\ B\times C\ \xrightarrow{\ i_{B}\times q\ }\ B\times D,
$$
which is legitimate since $(i_{B}\times q)\big((p\times i_{C})(a,c)\big)=(i_{B}\times q)(p(a),c)=(p(a),q(c))$.

The first factor is a quotient map by (a) applied to $p$ with $Z=C$, which is locally compact Hausdorff by hypothesis. The second factor is $i_{B}\times q$; up to the homeomorphisms that interchange the two factors it is $q\times i_{B}:C\times B\to D\times B$, which is a quotient map by (a) applied to $q$ with $Z=B$, locally compact Hausdorff by hypothesis — and composing a quotient map with a homeomorphism on either side leaves a quotient map. A composite of two quotient maps is a quotient map, so $p\times q$ is one. $\square$
:::
