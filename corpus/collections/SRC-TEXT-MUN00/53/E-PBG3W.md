---
schema: qual/card@1
id: E-PBG3W
kind: problem
title: Composites of covering maps with finite fibers
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 53: Problem 4 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-53-covering-spaces/problem-4-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-53-covering-spaces/problem-4-solution.txt), and against Munkres, Topology (2000), Section 53
    Exercise 4, printed p. 341, with the definition of a covering map on printed p. 336. dbFin's argument shrinks the evenly covered neighbourhood of $z$ to a finite intersection of images of evenly covered neighbourhoods upstairs; the card does the same. One step is implicit in both and is now stated on the card: with $W_i$ evenly covered by $q$ and $W_i\subseteq V_i$, the slice $W_i'=W_i\cap r^{-1}(U')$ equals $V_i\cap r^{-1}(U')$, because $r$ restricted to $V_i$ is injective, so the slices over $U'$ really are the sets $W_i'$. Nothing else needed repair.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the argument dbFin's Section 53 Problem 4 solution gives, rechecked against Munkres, Topology (2000), Section 53 Exercise 4, printed p. 341, and the definition of a covering map on printed p. 336. The card's earlier prose asserted that the slices over U' "really are" W_i'; that identity is now proved as a step, from injectivity of r on V_i, because it is what makes p^{-1}(U') the disjoint union of the sheets recorded. Also proved rather than asserted: that an open subset of an evenly covered set is evenly covered, used twice, and that r restricted to W_i' is a homeomorphism onto U'. No statement repair.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repair of a review finding on this card. Munkres's definition of a covering map (printed p. 336) requires the map to be continuous AND surjective, and the final step had proved only continuity and local triviality. Surjectivity of p = r o q is now its own step, from surjectivity of q and r, which are covering maps; the definition cited in the first step records both requirements. Continuity was split into its own step so that the last step cites the three parts separately. Nothing else changed; the slice identity, the shrinking lemma and the disjoint-union computation are as before.
---

::: {.exercise}

Let $q: X \to Y$ and $r: Y \to Z$ be covering maps; let $p = r \circ q$.
Show that if $r^{-1}(z)$ is finite for each $z \in Z$, then $p$ is a covering map.
:::

::: {.solution}
The argument follows the published solution **dbFin, "Section 53: Problem 4 Solution"** (Munkres, *Topology*, Section 53, Problem 4), which shrinks an evenly covered neighbourhood of $z$ to a finite intersection of images of evenly covered neighbourhoods upstairs; the implicit slice identity is stated below. The exercise is Munkres, *Topology* (2000), Section 53 Exercise 4, printed p. 341, and the definition of a covering map is on printed p. 336.

::: pf

::: {.pf-step #evenly}
Fix $z\in Z$. There is an open neighbourhood $U$ of $z$ with
$$
r^{-1}(U)=\bigsqcup_{i=1}^{m}V_i,
$$
where the $V_i$ are open and disjoint, each $r\restrict_{V_i}:V_i\to U$ is a homeomorphism, and $m=\cardinality{r^{-1}(z)}<\infty$.

::: pf-proof
Because $r$ is a covering map, $z$ has an evenly covered neighbourhood $U$: $r^{-1}(U)$ is a disjoint union of open sets $V_i$, each mapped homeomorphically onto $U$ by $r$ (Definition, printed p. 336, which requires the map to be continuous and surjective). Each $V_i$ meets $r^{-1}(z)$ in exactly one point, since $r\restrict_{V_i}$ is a bijection onto $U\ni z$; the $V_i$ cover $r^{-1}(U)\supseteq r^{-1}(z)$, so $r^{-1}(z)$ has exactly $m$ points. The hypothesis that $r^{-1}(z)$ is finite is therefore exactly the statement that the union has $m<\infty$ members.
:::

:::

::: {.pf-step #shrink}
For each $i$ let $y_i$ be the point of $V_i$ over $z$. There is an evenly covered neighbourhood $W_i\subseteq V_i$ of $y_i$ for $q$, and
$$
U'\coloneqq\bigcap_{i=1}^{m}r(W_i)
$$
is an open neighbourhood of $z$ contained in $U$.

::: pf-proof
$q$ is a covering map, so $y_i$ has an evenly covered neighbourhood $N_i$. The set $V_i$ is an open neighbourhood of $y_i$; replacing $N_i$ by $N_i\cap V_i$ if necessary, take a point $y_i\in N_i\subseteq V_i$ with $N_i$ evenly covered. (An open subset of an evenly covered set is evenly covered: if $q^{-1}(N_i)=\bigsqcup_\alpha S_\alpha$ with $q\restrict_{S_\alpha}$ a homeomorphism onto $N_i$ and $T\subseteq N_i$ is open, then $q^{-1}(T)=\bigsqcup_\alpha\big(S_\alpha\cap q^{-1}(T)\big)$ and $q\restrict_{S_\alpha\cap q^{-1}(T)}$ is a homeomorphism onto $T$.) So $W_i\subseteq V_i$ may be taken evenly covered.
Then $r\restrict_{V_i}$ is an open map, being a homeomorphism, so $r(W_i)=(r\restrict_{V_i})(W_i)$ is open in $U$ and contains $r(y_i)=z$. The intersection $U'$ of the finitely many open sets $r(W_i)$ is open, contains $z$, and lies in $U$ because $r(W_i)\subseteq r(V_i)=U$.
:::

:::

::: {.pf-step #sliceidentity}
$V_i\cap r^{-1}(U')=W_i\cap r^{-1}(U')$ for every $i$.

::: pf-proof
Let $y\in V_i$ with $r(y)\in U'\subseteq r(W_i)$. Choose $w\in W_i\subseteq V_i$ with $r(w)=r(y)$; since $r\restrict_{V_i}$ is injective, $y=w\in W_i$. So $V_i\cap r^{-1}(U')\subseteq W_i\cap r^{-1}(U')$, and the reverse inclusion is immediate from $W_i\subseteq V_i$.
:::

:::

::: {.pf-step #slices}
For each $i$, $W'_i\coloneqq W_i\cap r^{-1}(U')$ is an evenly covered neighbourhood of $y_i$ for $q$, and $r\restrict_{W'_i}:W'_i\to U'$ is a homeomorphism. Hence for every sheet $S$ of $q$ over $W'_i$ the composite $p\restrict_{S}=r\circ q\restrict_{S}$ is a homeomorphism of $S$ onto $U'$.

::: pf-proof
$W'_i$ is open and lies in the evenly covered set $W_i$, so it is evenly covered by $q$ (the argument of step [](#shrink){.pf-ref}), and it contains $y_i$ because $r(y_i)=z\in U'$; so $q^{-1}(W'_i)$ is a disjoint union of open sheets $S$, each mapped homeomorphically onto $W'_i$ by $q$.
For the second claim: $r\restrict_{W'_i}$ is injective, being a restriction of the injective $r\restrict_{V_i}$, and it is continuous. Its image is $r(W_i)\cap U'=U'$, since $U'\subseteq r(W_i)$; and its inverse is the restriction to $U'$ of the continuous map $(r\restrict_{V_i})^{-1}$, because $U'\subseteq U$. A continuous bijection whose inverse is continuous is a homeomorphism.
The composite of the homeomorphisms $q\restrict_{S}:S\to W'_i$ and $r\restrict_{W'_i}:W'_i\to U'$ is a homeomorphism of $S$ onto $U'$.
:::

:::

::: {.pf-step #preimage}
$p^{-1}(U')=\bigsqcup_{i=1}^{m}\bigsqcup_{S} S$, the inner union over the sheets of $q$ over $W'_i$, and these sets are pairwise disjoint.

::: pf-proof
$p^{-1}(U')=q^{-1}\big(r^{-1}(U')\big)$. Since $r^{-1}(U)=\bigsqcup_i V_i$, we have $r^{-1}(U')=\bigsqcup_i\big(V_i\cap r^{-1}(U')\big)=\bigsqcup_i W'_i$ by step [](#sliceidentity){.pf-ref}. Therefore $p^{-1}(U')=\bigsqcup_i q^{-1}(W'_i)=\bigsqcup_i\bigsqcup_S S$: the $W'_i$ are pairwise disjoint subsets of the disjoint $V_i$, so their preimages are disjoint, and the sheets over one $W'_i$ are disjoint because $q^{-1}(W'_i)$ is a disjoint union of them.
:::

:::

::: {.pf-step #surjective}
$p=r\circ q$ is surjective.

::: pf-proof
$q:X\to Y$ and $r:Y\to Z$ are covering maps, hence surjective by the definition (printed p. 336). For $z\in Z$ choose $y\in Y$ with $r(y)=z$ and then $x\in X$ with $q(x)=y$; then $p(x)=r\big(q(x)\big)=r(y)=z$. So $p(X)=Z$.
:::

:::

::: {.pf-step #continuous}
$p=r\circ q$ is continuous.

::: pf-proof
$q$ and $r$ are continuous by the definition of a covering map, and a composite of continuous maps is continuous.
:::

:::

::: {.pf-step #covering}
$p=r\circ q$ is a covering map.

::: pf-proof
$p$ is continuous and surjective by steps [](#continuous){.pf-ref} and [](#surjective){.pf-ref}. For each $z\in Z$, step [](#shrink){.pf-ref} produces an open neighbourhood $U'$ of $z$ and steps [](#preimage){.pf-ref} and [](#slices){.pf-ref} exhibit $p^{-1}(U')$ as a disjoint union of open sets each mapped homeomorphically onto $U'$ by $p$. So every point of $Z$ has an evenly covered neighbourhood, and with continuity and surjectivity this is the definition of a covering map (printed p. 336).
:::

:::

:::
:::
