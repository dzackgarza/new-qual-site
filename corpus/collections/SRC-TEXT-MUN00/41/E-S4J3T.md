---
schema: qual/card@1
id: E-S4J3T
kind: problem
title: Unions of closed paracompact subspaces
classification:
  areas:
  - topology
  topics:
  - Paracompactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Aleksey Zinger, "MAT 530: Topology & Geometry, I",
    Fall 2005, Problem Set 6, "Solution to Problem p260, #7", PDF pp. 2-3
    (tmp/sources/munkres-solutions-zinger-mat530-ps6.pdf; the sheet has no printed page numbers, so the
    PDF page is the locator). Checked against Munkres, Topology (2000), Section 41 Exercise 7, printed
    p. 260, with Lemma 41.3 (the equivalence of its conditions (1), (2), (3) and (4) for a regular space)
    and Theorem 41.2 (a closed subspace of a paracompact space is paracompact). What was corrected: the
    *published* posts on this exercise ("Praying For Stockholm", "Unions of Paracompact Spaces (6.41.7)",
    30 December 2014) refine inside the closed subspaces and then call the union a locally finite open
    refinement of X, although a set open in K_i need not be open in X; the card follows Zinger, who
    derives local finiteness in X explicitly (for x outside B the set X - B, for x in B the same open set
    W that witnesses local finiteness in B, since every member lies in B) and applies Lemma 41.3. In part
    (b) the card keeps Zinger's C_n = A_n - union of the earlier interiors in place of the post's
    intersection with int K_n, and states the passage from local finiteness in each C_n to local
    finiteness in X that both sources leave implicit.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf` with
    nine steps covering both parts, each carrying a `pf-proof`. Cited by number only: Munkres,
    Topology, §41 Exercise 7, Lemma 41.3 (condition (3), a locally finite closed covering refinement)
    and Theorem 41.2 (a closed subspace of a paracompact space is paracompact). The transcription is
    from Aleksey Zinger, MAT 530: Topology & Geometry I, Problem Set 6, Solution to Problem 7, and the
    two passages it leaves to the reader are written out: local finiteness in a closed subspace passes
    to the ambient space, and local finiteness in each C_n passes to the union. Checked: that the
    traces of an open cover on a closed subspace are an open cover of it, that C_n is closed in X, that
    the least m with x in the interior of A_m puts x in C_m, and that a neighbourhood meeting only
    finitely many C_n meets only finitely many members of the corresponding families.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 read, and the proof replaced by a transcription of the published solution the card
    names. The proof that stood here was correct but was not Zinger's: it refined by closed
    families through condition (3) of Lemma 41.3 and built the closed sets
    $C_n=A_n-\bigcup_{i<n}A_i^\circ$, neither of which occurs in his sheet, so the sentence
    calling the argument his was false of the text. The solution is now his Solution to Problem
    p260 #7, parts (a) and (b), read in
    `tmp/sources/munkres-solutions-zinger-mat530-ps6.pdf`: open refinements on the closed
    subspaces, the union of the two families, his transfer of local finiteness from a closed
    subspace to the ambient space, then condition (2) of Lemma 41.3 for (a); and for (b) the open
    refinements $\mathcal B_n$ of the traces on $X_n$, the open sets $V(D)$ cutting them, the
    families $\mathcal D_n=\{V(D)\cap\operatorname{Int}X_n\}$ and condition (1). Written out where
    he leaves it to the reader: the induction reducing a finite union to two closed subspaces, and
    the existence of $V(D)$ from the definition of the subspace topology. Checked against Lemma
    41.3, whose four conditions are quoted in the first step, and §41's definition of
    paracompactness. Citation by number: §41 Exercise 7 and Lemma 41.3.

---

::: {.exercise}

Let $X$ be a regular space.

(a) If $X$ is a finite union of closed paracompact subspaces of $X$, then $X$ is paracompact.

(b) If $X$ is a countable union of closed paracompact subspaces whose interiors cover $X$, show $X$ is paracompact.
:::


::: {.solution}

The argument is Aleksey Zinger's, *MAT 530: Topology & Geometry, I* (Fall 2005), Problem Set 6, Solution to Problem p260 #7, parts (a) and (b), read in `tmp/sources/munkres-solutions-zinger-mat530-ps6.pdf`. Written out here: the induction reducing a finite union to two closed subspaces, and the choice of the open set $V(D)$ cutting a member of the refinement on $X_n$. Zinger's transfer of local finiteness from a closed subspace to $X$ is proved once, in (a), and reused in (b).

::: pf

::: {.pf-step #criterion}
Lemma 41.3: for a regular space, conditions (1)--(4) are equivalent, and condition (4) is paracompactness. Part (a) produces condition (2) and part (b) condition (1), so each yields (4).

::: pf-proof
This is Munkres, Lemma 41.3: every open covering of $X$ has a refinement that is (1) an open covering, countably locally finite; (2) a covering, locally finite; (3) a closed covering, locally finite; (4) an open covering, locally finite. Condition (4) is the definition of paracompactness (§41), and $X$ is regular by hypothesis.
:::

:::

::: {.pf-step #part-a-two-sets}
(a) It suffices to prove the case $X=B\cup C$ with $B$ and $C$ closed and paracompact.

::: pf-proof
If $X=A_1\cup\cdots\cup A_m$ with each $A_i$ closed and paracompact, argue by induction on $m$: for $m=2$ this is the case stated, and for $m>2$ put $B=A_1$ and $C=A_2\cup\cdots\cup A_m$. The set $C$ is closed, being a finite union of closed sets, and it is paracompact by the induction hypothesis applied to the subspaces $A_2,\ldots,A_m$ of $C$; then the two-set case applies to $X=B\cup C$.
:::

:::

::: {.pf-step #part-a-refinements}
Let $\mathcal A$ be an open cover of $X=B\cup C$. There are families $\mathcal B$ and $\mathcal C$, open in $B$ and in $C$, covering $B$ and $C$, refining the traces of $\mathcal A$, and locally finite in $B$ and in $C$.

::: pf-proof
$\mathcal A_B=\theset{U\cap B\mid U\in\mathcal A}$ and $\mathcal A_C=\theset{U\cap C\mid U\in\mathcal A}$ are open covers of $B$ and of $C$ in the subspace topologies. Since $B$ and $C$ are paracompact, paracompactness gives an open refinement $\mathcal B$ of $\mathcal A_B$ covering $B$ and locally finite in $B$, and an open refinement $\mathcal C$ of $\mathcal A_C$ covering $C$ and locally finite in $C$.
:::

:::

::: {.pf-step #transfer}
A family of subsets of a closed subspace $S$ that is locally finite in $S$ is locally finite in $X$.

::: pf-proof
Let $\mathcal F$ be such a family, every member of which lies in $S$, and let $x\in X$. If $x\in X-S$, then $X-S$ is an open set containing $x$ that meets no member of $\mathcal F$. If $x\in S$, local finiteness in $S$ gives an open set $W$ of $X$ with $x\in W\cap S$ meeting only finitely many members of $\mathcal F$; since every $F\in\mathcal F$ lies in $S$, one has $(W\cap S)\cap F=W\cap F$, so $W$ itself meets only those finitely many members.
:::

:::

::: {.pf-step #part-a-union}
$\mathcal D=\mathcal B\cup\mathcal C$ is a locally finite refinement of $\mathcal A$ covering $X$.

::: pf-proof
$\mathcal B$ covers $B$ and $\mathcal C$ covers $C$, so $\mathcal D$ covers $B\cup C=X$. A member of $\mathcal B$ lies in some $U\cap B$ and a member of $\mathcal C$ in some $U\cap C$, so every member of $\mathcal D$ lies in a member of $\mathcal A$. The subspaces $B$ and $C$ are closed, so step [](#transfer){.pf-ref} makes $\mathcal B$ and $\mathcal C$ locally finite in $X$; a union of two families locally finite at a point is locally finite there, by intersecting the two neighbourhoods.
:::

:::

::: {.pf-step #part-a-done}
(a) $X$ is paracompact.

::: pf-proof
Step [](#part-a-union){.pf-ref} gives condition (2) of Lemma 41.3 for an arbitrary open cover, and $X$ is regular, so condition (4) holds, that is, $X$ is paracompact.
:::

:::

::: {.pf-step #part-b-data}
(b) Let $X=\bigcup_{n}\operatorname{Int}X_n$ with each $X_n$ closed and paracompact, and let $\mathcal A$ be an open cover of $X$. For each $n$ there is a family $\mathcal B_n$, open in $X_n$, covering $X_n$, refining $\theset{U\cap X_n\mid U\in\mathcal A}$, and locally finite in $X_n$.

::: pf-proof
$\theset{U\cap X_n\mid U\in\mathcal A}$ is an open cover of $X_n$ in the subspace topology, so paracompactness of $X_n$ gives an open refinement of it that covers $X_n$ and is locally finite in $X_n$.
:::

:::

::: {.pf-step #part-b-sets}
For each $n$ and each $D\in\mathcal B_n$ there is an open $V(D)\subseteq X$ with $D=V(D)\cap X_n$, and the family $\mathcal D_n=\theset{V(D)\cap\operatorname{Int}X_n\mid D\in\mathcal B_n}$ consists of open subsets of $X$ refining $\mathcal A$.

::: pf-proof
$D$ is open in $X_n$, so $D=V(D)\cap X_n$ for some open $V(D)\subseteq X$, by the definition of the subspace topology. The set $V(D)\cap\operatorname{Int}X_n$ is open in $X$ and lies in $V(D)\cap X_n=D$, and $D$ lies in some member of $\mathcal A$ because $\mathcal B_n$ refines the traces of $\mathcal A$.
:::

:::

::: {.pf-step #part-b-cover}
$\mathcal D=\bigcup_{n}\mathcal D_n$ covers $X$.

::: pf-proof
For each $n$, $$\bigcup_{D\in\mathcal B_n}\bigl(V(D)\cap\operatorname{Int}X_n\bigr)=\Bigl(\bigcup_{D\in\mathcal B_n}V(D)\Bigr)\cap\operatorname{Int}X_n\supseteq\Bigl(\bigcup_{D\in\mathcal B_n}D\Bigr)\cap\operatorname{Int}X_n=X_n\cap\operatorname{Int}X_n=\operatorname{Int}X_n,$$ so $\mathcal D$ covers $\bigcup_n\operatorname{Int}X_n=X$.
:::

:::

::: {.pf-step #part-b-locally-finite}
Each $\mathcal D_n$ is locally finite in $X$, so $\mathcal D$ is countably locally finite.

::: pf-proof
The subspace $X_n$ is closed, so step [](#transfer){.pf-ref} makes the family $\mathcal B_n$, locally finite in $X_n$, locally finite in $X$. A member of $\mathcal D_n$ is contained in the corresponding member $D$ of $\mathcal B_n$, so an open set that meets $V(D)\cap\operatorname{Int}X_n$ meets $D$; hence a neighbourhood of a point that meets only finitely many members of $\mathcal B_n$ meets only finitely many members of $\mathcal D_n$.
:::

:::

::: {.pf-step #part-b-done}
(b) $X$ is paracompact.

::: pf-proof
The family $\mathcal D$ is an open refinement of $\mathcal A$ covering $X$ and a countable union of locally finite families, which is condition (1) of Lemma 41.3; $X$ is regular, so condition (4) holds.
:::

:::

:::

:::
