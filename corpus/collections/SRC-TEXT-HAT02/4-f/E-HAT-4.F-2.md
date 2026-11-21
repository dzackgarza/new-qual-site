---
schema: qual/card@1
id: E-HAT-4.F-2
kind: problem
title: "Suspension sequences of CW complexes"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.F, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §4.F, printed p. 455, with the Freudenthal suspension
    theorem (Corollary 4.24, p. 360) and the Puppe sequence of p. 398. Correct. For $X=S^q$ the
    suspension map is $\pi_{q+r}(\Sigma^rY)\to\pi_{q+r+1}(\Sigma^{r+1}Y)$, and $\Sigma^rY$ is
    $(r-1)$-connected, so $q+r<2(r-1)-1$ holds for large $r$ and Freudenthal makes it an
    isomorphism; a finite wedge follows by the same argument applied to its summands. For the
    inductive step, $X=A\cup_\varphi e^q$ gives the cofibration $S^{q-1}\to A\to X\to S^q$, and the
    Puppe sequence of the suspended cofibration mapped into $\Sigma^rY$ is exact, with the two
    consecutive sequences connected by the suspension maps; the terms are groups once $r$ is large
    because the target is then highly connected, so the five lemma applies and gives the
    isomorphism for $X$. Finitely many cells end the induction. Nothing changed. Not claimed: a
    published solution, and no certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher, §4.F Exercise 2 and its hint, with the Freudenthal suspension theorem
    (Corollary 4.24), the Puppe sequence of a cofibration (§4.3) and the five lemma (§2.2). The
    route is right: connectivity of $\Sigma^rY$ grows with $r$, Freudenthal makes the suspension
    iso on each sphere and on finite wedges, and the induction over cells compares two consecutive
    Puppe sequences by the five lemma. Two gaps closed and the citation repaired. (1) The proof
    said "after increasing $r$ if necessary, the relevant terms are groups", which is the hypothesis
    the five lemma needs; the terms are $\pi_{q-1+r}(\Sigma^rY)$ and its neighbours, of index at
    least $1$ for $r\ge1$ and $q\ge1$, so they are groups for every $r\ge1$ and abelian once the
    index is $2$, and the step now says which index each has and why the maps are homomorphisms.
    (2) The five lemma was applied to a diagram whose rows must be exact *as groups*; exactness of
    the suspended Puppe sequence is a sequence of pointed sets in general, and the step now notes
    that exactness as groups holds in the range where all terms are groups, which is the range in
    which the comparison is made. The text cited pages for Corollaries 4.24, the Puppe sequence and
    the five lemma; by the owner's correction of this date it cites the numbered statements only.
    The prose is now a structured proof, and the lead states that no retained solution set covers
    the exercise. No statement changed. Not checked: no certificate.

---

::: {.problem}
For CW complexes $X$ and $Y$ consider the suspension sequence

$$\langle X, Y \rangle \stackrel{\Sigma}{\longrightarrow} \langle \Sigma X, \Sigma Y \rangle \stackrel{\Sigma}{\longrightarrow} \langle \Sigma^2 X, \Sigma^2 Y \rangle \longrightarrow \cdots$$

Show that if $X$ is a finite complex, these maps eventually become isomorphisms.
[Use induction on the number of cells of $X$ and the five-lemma.]
:::

::: {.solution}
No retained solution set covers this exercise — Sam's set stops at §4.3 and none of the other sets retained for this project has a §4.F solution — so the argument is the card's own, following the printed hint. It uses the Freudenthal suspension theorem (Corollary 4.24), the Puppe sequence of a cofibration and its exactness (§4.3), and the five lemma. Throughout $X$ is a finite CW complex, $Y$ any CW complex, and $\Sigma$ denotes the suspension of maps.

::: pf

::: {.pf-step #connectivity}
If $Y$ is $(k-1)$-connected then $\Sigma^rY$ is $(k+r-1)$-connected for every $r\ge0$.

::: pf-proof
Suspension raises connectivity by one: if $W$ is $(j-1)$-connected then $\Sigma W$ is $j$-connected, since $\Sigma W$ is the union of two cones on $W$ and the Mayer–Vietoris sequence, or directly the suspension isomorphism together with Hurewicz, gives $\pi_i(\Sigma W)=0$ for $i\le j$. Applying this $r$ times to the $(k-1)$-connected $Y$ gives the claim.
:::

:::

::: {.pf-step #sphere}
For $X=S^q$ with $q\ge0$ the suspension map $\langle\Sigma^rS^q,\Sigma^rY\rangle\to\langle\Sigma^{r+1}S^q,\Sigma^{r+1}Y\rangle$ is an isomorphism for all sufficiently large $r$.

::: pf-proof
The two sets are $\pi_{q+r}(\Sigma^rY)$ and $\pi_{q+r+1}(\Sigma^{r+1}Y)$, and the map is the suspension homomorphism. By step [](#connectivity){.pf-ref} the space $\Sigma^rY$ is $(k+r-1)$-connected, so Corollary 4.24 applies to the suspension $\pi_i(\Sigma^rY)\to\pi_{i+1}(\Sigma^{r+1}Y)$ with $i=q+r$ and gives an isomorphism whenever $q+r<2(k+r-1)-1$, that is whenever $2k+r>q+3$. That inequality holds for all $r>q+3-2k$, which proves the step.
:::

:::

::: {.pf-step #wedge}
For $X$ a finite wedge of spheres the suspension map is an isomorphism for all sufficiently large $r$.

::: pf-proof
A based map out of a finite wedge is a tuple of based maps on the summands, so $\langle\Sigma^rX,\Sigma^rY\rangle$ is the product of the corresponding sets over the summands, and $\Sigma$ acts coordinatewise. A product of maps is a bijection exactly when each factor is, so step [](#sphere){.pf-ref} applied to each summand gives the result for $r$ beyond the largest of the finitely many thresholds.
:::

:::

::: {.pf-step #range}
For $q\ge1$ and $r\ge1$ every set appearing in the rows below is a group, and every map in them is a group homomorphism.

::: pf-proof
The entries are $\langle\Sigma^rS^i,\Sigma^rY\rangle=\pi_{i+r}(\Sigma^rY)$ for $i\in\{q-1,q\}$ and the corresponding $\langle\Sigma^rA,\Sigma^rY\rangle$ and $\langle\Sigma^rX,\Sigma^rY\rangle$; the first two are homotopy groups of index at least $q-1+r\ge1$ since $q,r\ge1$, hence groups, and $\langle\Sigma^rA,\Sigma^rY\rangle$ is a group once $\Sigma^rA$ is a suspension, the set of based homotopy classes out of a suspension carrying the group structure induced by the pinch map, which $\Sigma^rX$ also carries. All maps in the sequence are induced by based maps of the source spaces or by suspension of the target, and each is additive: for a based $h$ of sources, $[(u+v)\circ h]=[u\circ h]+[v\circ h]$ since pinching commutes with $h$ up to homotopy, and $\Sigma(u+v)\simeq\Sigma u+\Sigma v$ since suspension of the pinch of $S^{i}$ is the pinch of $S^{i+1}$.
:::

:::

::: {.pf-step #puppe}
Let $X=A\cup_\varphi e^q$ be obtained from a subcomplex $A$ by attaching one $q$-cell. Then for every $r\ge1$ there is a commutative diagram with exact rows

$$\begin{array}{ccccccccc}
\langle\Sigma^rS^{q},\Sigma^rY\rangle & \to & \langle\Sigma^rA,\Sigma^rY\rangle & \to & \langle\Sigma^rX,\Sigma^rY\rangle & \to & \langle\Sigma^rS^{q-1},\Sigma^rY\rangle & \to & \langle\Sigma^{r+1}S^{q},\Sigma^{r+1}Y\rangle \\
\downarrow & & \downarrow & & \downarrow & & \downarrow & & \downarrow \\
\langle\Sigma^{r+1}S^{q},\Sigma^{r+1}Y\rangle & \to & \langle\Sigma^{r+1}A,\Sigma^{r+1}Y\rangle & \to & \langle\Sigma^{r+1}X,\Sigma^{r+1}Y\rangle & \to & \langle\Sigma^{r+1}S^{q-1},\Sigma^{r+1}Y\rangle & \to & \langle\Sigma^{r+2}S^{q},\Sigma^{r+2}Y\rangle
\end{array}$$

in which the vertical maps are the suspensions, and whose rows are exact as groups in the range of step [](#range){.pf-ref}.

::: pf-proof
The cofibration $S^{q-1}\xrightarrow{\varphi}A\to X$ has cofibre $X/A=S^q$, so there is a cofibration sequence $S^{q-1}\to A\to X\to S^q\to\Sigma A\to\cdots$, and applying $\langle -,\Sigma^rY\rangle$ to $r$-fold suspensions of it gives the exact Puppe sequence of the row, by the exactness properties of the Puppe sequence in §4.3. Naturality of that sequence in the target and compatibility of suspension with cofibration sequences give the commuting squares. Exactness as a sequence of groups holds because every term is a group in this range and the maps are homomorphisms, by step [](#range){.pf-ref}; the entries at the two ends of the row are $\pi_{q+r}(\Sigma^rY)$ and $\pi_{q-1+r}(\Sigma^rY)$ with $q+r\ge2$ and $q-1+r\ge1$, so they are groups as well.
:::

:::

::: {.pf-step #induction}
If the suspension map is an isomorphism for $A$ for all $r\ge r_0$, then it is an isomorphism for $X=A\cup_\varphi e^q$ for all $r\ge r_0'$.

::: pf-proof
Apply the five lemma to the diagram of step [](#puppe){.pf-ref} with $r\ge\max(r_0,r_1)$, where $r_1$ is a threshold beyond which the suspension maps for $S^q$ and $S^{q-1}$ are isomorphisms, by step [](#sphere){.pf-ref}. Four of the five vertical maps are then isomorphisms, so the middle one is, which is the suspension map for $X$.
:::

:::

::: {.pf-step #finite}
For a finite CW complex $X$ the suspension map is an isomorphism for all sufficiently large $r$.

::: pf-proof
Induct on the number of cells of $X$. For the empty complex and for a point the assertion is immediate, and for a finite wedge of spheres it is step [](#wedge){.pf-ref}, which also covers the complexes of at most one cell. For the induction step write $X=A\cup_\varphi e^q$ with $A$ a subcomplex having one cell fewer; the induction hypothesis gives the threshold for $A$, and step [](#induction){.pf-ref} gives one for $X$. A finite CW complex has finitely many cells, so the induction terminates and yields a threshold for $X$.
:::

:::

::: {.pf-step}
$\boxed{\text{For } X \text{ a finite CW complex the suspension maps } \langle \Sigma^r X, \Sigma^r Y\rangle\to\langle \Sigma^{r+1}X,\Sigma^{r+1}Y\rangle \text{ are isomorphisms for all sufficiently large } r.}$

::: pf-proof
That is step [](#finite){.pf-ref}, which is the exercise's claim for an arbitrary CW complex $Y$ and a finite complex $X$.
:::

:::

:::
:::
