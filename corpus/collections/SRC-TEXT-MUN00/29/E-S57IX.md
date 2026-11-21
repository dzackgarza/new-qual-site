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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with seven steps, three for the lemma and three for the theorem, each carrying a
    `pf-proof`; the arguments and the attribution are unchanged. Cited by number only:
    Exercise 29.10 (a point of a locally compact Hausdorff space has a compact neighbourhood),
    Lemma 26.8 (the tube lemma), and the definitions of quotient map, saturation and
    product map. Checked: that $B$ contains $x$ and is saturated, that $p(B)\times C\subseteq A$
    pointwise, and that the second factor of part (b) is the first factor of (a) after the swap
    homeomorphisms.
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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.11** (`tmp/sources/munkres-solutions-positron-ch3.pdf`) for part (a) — its numbering runs past the ten exercises of §29 into the supplementary exercises on nets, where this is the last of them — with the saturation argument written out, as their paragraph only asserts the last step. Part (b) is not in that set and is proved below from part (a).

::: pf

::: pf-step

(a) $\pi=p\times i_{Z}:X\times Z\to Y\times Z$ is continuous and surjective.

::: pf-proof

$\pi$ is the product of the continuous maps $p$ and $i_Z$, hence continuous. It is surjective because $p$ is: a point $(y,z)$ is $\pi(x,z)$ for any $x\in p^{-1}(y)$, and $p^{-1}(y)\ne\varnothing$ for every $y\in Y$.

:::

:::

::: pf-step

(a) Let $A\subset Y\times Z$ with $\pi^{-1}(A)$ open, let $y\times z\in A$ and $x\in p^{-1}(y)$, and let $C$ be a compact neighbourhood of $z$. Then
$$
B=\{x'\in X\mid \{x'\}\times C\subset\pi^{-1}(A)\}
$$
contains $x$, and it is open.

::: pf-proof

$Z$ is locally compact Hausdorff, so $z$ has a compact neighbourhood $C$ (Exercise 29.10). For $c\in C$ we have $\pi(x,c)=p(x)\times c=y\times c\in A$, so $\{x\}\times C\subseteq\pi^{-1}(A)$ and $x\in B$. For openness, let $x'\in B$; then $\{x'\}\times C$ is a compact slice inside the open set $\pi^{-1}(A)\cap(X\times C)$ of $X\times C$, so the tube lemma (Munkres, Lemma 26.8) gives a neighbourhood $U$ of $x'$ with $U\times C\subseteq\pi^{-1}(A)$, that is $U\subseteq B$.

:::

:::

::: pf-step

(a) $B$ is saturated, so $p(B)$ is open in $Y$, and
$$
(y,z)\in p(B)\times\operatorname{int}C\subset A;
$$
hence $A$ is open and $\pi$ is a quotient map.

::: pf-proof

If $x'\in B$ and $p(x'')=p(x')$, then for every $c\in C$ one has $\pi(x'',c)=p(x'')\times c=p(x')\times c=\pi(x',c)\in A$, so $x''\in B$ and $B=p^{-1}(p(B))$ is saturated. $p$ is a quotient map and $B$ is open and saturated, so $p(B)$ is open in $Y$. For $y'=p(x')\in p(B)$ and $z'\in C$ we have $y'\times z'=\pi(x',z')\in A$, so $p(B)\times C\subseteq A$; and $\operatorname{int}C$ is an open neighbourhood of $z$ contained in $C$. Thus $p(B)\times\operatorname{int}C$ is an open neighbourhood of $y\times z$ inside $A$, and every point of $A$ is interior to it. Since $\pi$ is continuous and surjective (step 1) and pulls open sets of $A$ back to open sets, $\pi$ is a quotient map.

:::

:::

::: pf-step

(b) $p\times q:A\times C\to B\times D$ factors as
$$
A\times C\ \xrightarrow{\ p\times i_{C}\ }\ B\times C\ \xrightarrow{\ i_{B}\times q\ }\ B\times D.
$$

::: pf-proof

For $(a,c)\in A\times C$ the composite sends it to $(p(a),c)$ and then to $(p(a),q(c))$, which is $(p\times q)(a,c)$; the two maps agree pointwise, so the displayed factorisation is legitimate.

:::

:::

::: pf-step

(b) Both factors are quotient maps.

::: pf-proof

The first factor is $p\times i_C$ with $C$ locally compact Hausdorff, so it is a quotient map by part (a). The second is $i_B\times q:B\times C\to B\times D$; composing with the swap homeomorphisms $C\times B\to B\times C$ and $D\times B\to B\times D$ it becomes $q\times i_B:C\times B\to D\times B$, which is a quotient map by part (a) with $Z=B$, locally compact Hausdorff by hypothesis. Composing a quotient map with homeomorphisms on both sides gives a quotient map, so $i_B\times q$ is one.

:::

:::

::: pf-step

(b) Hence $p\times q$ is a quotient map.

::: pf-proof

A composite of two quotient maps is a quotient map: if $\pi_1$ and $\pi_2$ are quotient and $\pi_2\circ\pi_1$ is continuous, then a set in the target is open exactly when its preimage under $\pi_2\circ\pi_1$ is open, because each factor has that property. By steps 4 and 5 this applies to the factorisation of $p\times q$.

:::

:::

::: pf-step

Both parts are proved: the lemma for a single quotient map times a locally compact Hausdorff factor, and the theorem for a product of two quotient maps with locally compact Hausdorff middle spaces.

::: pf-proof

Part (a) is steps 1--3 and part (b) steps 4--6.

:::

:::

:::
:::
