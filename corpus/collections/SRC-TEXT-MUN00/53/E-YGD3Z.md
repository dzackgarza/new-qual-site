---
schema: qual/card@1
id: E-YGD3Z
kind: problem
title: Properties of the total space of a covering
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
    Checked against the located published solution: dbFin, "Section 53: Problem 6 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-53-covering-spaces/problem-6-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-53-covering-spaces/problem-6-solution.txt), and against Munkres, Topology (2000), Section 53
    Exercise 6, printed p. 341, with the definition of a covering map on printed p. 336. dbFin's (a) runs the four separation properties together and its (b) is a sketch whose displayed symbols are corrupted; the card's proof is written out, and it uses the book's own hint, which is correct: for $C$ closed in $B$ with $C\subseteq U$, a limit point of $p^{-1}(C)\cap V_\alpha$ lies in $p^{-1}(C)\subseteq p^{-1}(U)$, hence in some slice, and cannot lie in a different slice because the slices are disjoint open sets, so it lies in $V_\alpha$. The four parts of (a) and the compactness argument in (b) were checked against that hint and against Lemma 31.1(a), Theorem 29.2 and Theorem 26.2; nothing needed repair.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same two parts. The step checked while doing it is the
    completely regular one: Phi is defined by cases on V and off V, and the two cases must agree where the
    open cover's members meet. The card now shows that they do --- the overlap is V minus the closure of N,
    which lies inside V minus N, where phi equals 1 --- and names the local formulation of continuity,
    Theorem 18.2(f), as what the cover is for. It also says why V - N is closed in V, namely that it is the
    trace of the closed set E - N, which is what lets complete regularity of V be applied to it. Part (b)
    now writes the equality p^{-1}(W_b) = union of the preimages over the slices, which needs the slices
    over V to partition p^{-1}(V) and their number to be the fibre cardinality. Checked against Munkres,
    Topology (2000), Section 53 Exercise 6, printed p. 341.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening paragraph carried curation prose onto the rendered
    page: the local path of the retained copy of dbFin's solution, the remark
    that dbFin's part (b) "is a sketch with corrupted symbols", that both parts
    "are written out here", and that one step "is now said rather than left to be
    read off" the source phrase. SEC-7 and QUAL-08 keep provenance, status and
    change narration off a public page, so the paragraph now cites dbFin's
    solution and the book's pages only. The mathematics it narrated is on the
    step that uses it: in step gluing, V cap (E - closure N) = V - closure N lies
    in V - N, which is where phi = 1, so the two pieces of Phi agree on the
    overlap of the open cover. No statement, step or page citation changes, and
    the reading of dbFin's solution and of the book's pages is the one the event
    of 2026-11-11 records.

---

::: {.exercise}

Let $p: E \to B$ be a covering map.

(a) If $B$ is Hausdorff, regular, completely regular, or locally compact Hausdorff, then so is $E$.
[Hint: If $\theset{V_\alpha}$ is a partition of $p^{-1}(U)$ into slices, and $C$ is a closed set of $B$ such that $C \subset U$, then $p^{-1}(C) \cap V_\alpha$ is a closed set of $E$.]

(b) If $B$ is compact and $p^{-1}(b)$ is finite for each $b \in B$, then $E$ is compact.
:::

::: {.solution}
The argument is that of the published solution of dbFin, "Section 53: Problem 6 Solution", for the four separation properties of part (a) and for the compactness of part (b), following the book's own hint. The exercise is Munkres, *Topology* (2000), Section 53, Exercise 6; its hint uses Lemma 31.1, Theorem 18.2(f), Theorem 29.2, and Theorem 33.2. Throughout, $p\colon E\to B$ is a covering map; an evenly covered open set $U\subset B$ has $p^{-1}(U)$ partitioned into slices, each mapped homeomorphically onto $U$ by $p$, and a slice $V$ over $U$ means an open set with $p(V)=U$ on which $p$ is a homeomorphism (Munkres, printed p. 336).

::: pf

::: {.pf-step #a}

(a) If $B$ is Hausdorff, regular, completely regular or locally compact Hausdorff, then so is $E$.

:::: pf-proof

Assume $B$ has the property in question; the four are taken in turn.

::: {.pf-step #hausdorff}

If $B$ is Hausdorff, then $E$ is Hausdorff.

::: pf-proof

Let $e_{1}\neq e_{2}$ in $E$. If $p(e_{1})\neq p(e_{2})$, choose disjoint open $U_{1}\ni p(e_{1})$ and $U_{2}\ni p(e_{2})$ in $B$; then $p^{-1}(U_{1})$ and $p^{-1}(U_{2})$ are disjoint open sets containing $e_{1}$ and $e_{2}$. If $p(e_{1})=p(e_{2})=b$, choose an evenly covered open set $U$ of $b$; the slices over $U$ partition $p^{-1}(U)$, and each slice contains exactly one point of the fibre $p^{-1}(b)$, so $e_{1}$ and $e_{2}$ lie in distinct slices, which are disjoint open sets.

:::

:::

::: {.pf-step #regular}

If $B$ is regular, then $E$ is regular.

::: pf-proof

Let $e\in E$ and let $O$ be an open neighbourhood of $e$. Choose a slice $V$ over an open $U$ with $e\in V\subset O$, and put $b\coloneqq p(e)$. Regularity of $B$ gives an open $W$ with $b\in W\subset\overline W\subset U$. Then $N\coloneqq V\cap p^{-1}(W)$ is an open neighbourhood of $e$, and
$$
\overline N\subset V\cap p^{-1}(\overline W)\subset V\subset O .
$$
The middle containment uses the hint: $\overline W$ is closed in $B$ and lies in $U$, so $p^{-1}(\overline W)\cap V$ is a closed set of $E$, and it contains $N$, whence it contains $\overline N$; and $p^{-1}(\overline W)\cap V\subset p^{-1}(U)\cap V=V$ because $V$ lies over $U$. So every neighbourhood of a point contains the closure of a neighbourhood, and $E$ has closed one-point sets by step [](#hausdorff){.pf-ref}; with those two, Lemma 31.1(a)  makes $E$ regular.

:::

:::

::: {.pf-step #cr}

If $B$ is completely regular, then $E$ is completely regular.

:::: pf-proof

Let $F$ be a closed subset of $E$ and $e\in E-F$.

::: {.pf-step #neighbourhood}

For closed $F\subset E$ and $e\notin F$ there are a slice $V\ni e$ and an open $N$ with $e\in N$ and $\overline N\subset V-F$.

::: pf-proof

Choose a slice $V$ over an open $U$ with $e\in V$. By step [](#regular){.pf-ref} the space $E$ is regular, so the closed set $F$, which does not contain $e$, and the point $e$ have disjoint open neighbourhoods; taking $N$ inside the one containing $e$ and disjoint from $F$, and shrinking further so that $\overline N\subset V$, gives $\overline N\cap F=\varnothing$, that is $\overline N\subset E-F$.

:::

:::

::: {.pf-step #function}

$V-N$ is closed in $V$, and there is a continuous $\varphi\colon V\to[0,1]$ with $\varphi(e)=0$ and $\varphi=1$ on $V-N$.

::: pf-proof

$N$ is open in $E$, so $E-N$ is closed in $E$, and $V-N=V\cap(E-N)$ is closed in the subspace $V$. The slice $V$ is homeomorphic to $U$, a subspace of the completely regular space $B$, and a subspace of a completely regular space is completely regular (Theorem 33.2); so $V$ is completely regular, and applying it to the point $e$ and the closed set $V-N$, which does not contain $e$, gives such a $\varphi$, with the values $0$ and $1$ interchanged, which the remark on printed p. 211 allows.

:::

:::

::: {.pf-step #gluing}

$\Phi\colon E\to[0,1]$, defined by $\Phi\coloneqq\varphi$ on $V$ and $\Phi\coloneqq1$ off $V$, is continuous, with $\Phi(e)=0$ and $\Phi=1$ on $F$.

::: pf-proof

The sets $V$ and $E-\overline N$ are open: $V$ is a slice, and $\overline N$ is closed. They cover $E$, because $\overline N\subset V$ by step [](#neighbourhood){.pf-ref}. Their intersection is $V\cap(E-\overline N)=V-\overline N$, which lies in $V-N$, so $\varphi=1$ there by step [](#function){.pf-ref}: the restriction of $\Phi$ to $V$ is $\varphi$ and its restriction to $E-\overline N$ is the constant $1$, and the two agree on the overlap. A map continuous on each member of an open cover of its domain is continuous (Theorem 18.2(f)), so $\Phi$ is continuous. Finally $\Phi(e)=\varphi(e)=0$ because $e\in V$, and $\Phi=1$ on $F$ because $F\cap\overline N=\varnothing$ by step [](#neighbourhood){.pf-ref}, so $F\subset E-\overline N$.

:::

:::

::::

:::

::: {.pf-step #locally-compact}

If $B$ is locally compact Hausdorff, then $E$ is locally compact.

::: pf-proof

Let $e\in E$ and choose a slice $V$ over an open $U$ with $e\in V$. By local compactness of $B$ at $p(e)$ and Theorem 29.2  there is an open $W$ with $p(e)\in W$ and $\overline W$ compact and $\overline W\subset U$. Then $V\cap p^{-1}(\overline W)$ is homeomorphic to $\overline W$, hence compact, and it contains the open neighbourhood $V\cap p^{-1}(W)$ of $e$. So $E$ is locally compact at each point, and it is Hausdorff by step [](#hausdorff){.pf-ref}.

:::

:::

::::

:::

::: {.pf-step #b}

(b) If $B$ is compact and every fibre $p^{-1}(b)$ is finite, then $E$ is compact.

:::: pf-proof

Let $\mathcal{U}$ be an open cover of $E$; the aim is a finite subcover.

::: {.pf-step #local-finiteness}

For $b\in B$ and an open cover $\mathcal{U}$ of $E$ there is an open $W_{b}\ni b$ whose preimage $p^{-1}(W_{b})$ is covered by finitely many members of $\mathcal{U}$.

::: pf-proof

Write $p^{-1}(b)=\theset{e_{1},\dots,e_{r}}$, which is finite, and choose $U_{j}\in\mathcal{U}$ with $e_{j}\in U_{j}$. Let $V$ be an evenly covered open neighbourhood of $b$ with slices $V_{1},\dots,V_{r}$ containing $e_{1},\dots,e_{r}$; there are exactly $r$ slices over $V$, because each slice meets the fibre over $b$ in exactly one point. For each $j$ the restriction $\restrictionof{p}{V_{j}}\colon V_{j}\to V$ is a homeomorphism and $U_{j}\cap V_{j}$ is a neighbourhood of $e_{j}$, so there is an open $W_{j}\subset V$ with $b\in W_{j}$ and $\big(\restrictionof{p}{V_{j}}\big)^{-1}(W_{j})\subset U_{j}$. Put $W_{b}\coloneqq\bigcap_{j=1}^{r}W_{j}$, an open neighbourhood of $b$ contained in $V$. Then
$$
p^{-1}(W_{b})=\bigcup_{j=1}^{r}\big(\restrictionof{p}{V_{j}}\big)^{-1}(W_{b})\subset\bigcup_{j=1}^{r}U_{j},
$$
the equality because the slices over $V$ partition $p^{-1}(V)$.

:::

:::

::: {.pf-step #subcover}

Finitely many of the sets $W_{b}$ cover $B$.

::: pf-proof

The sets $W_{b}$, $b\in B$, are open and cover $B$, which is compact, so finitely many of them, say $W_{b_{1}},\dots,W_{b_{m}}$, cover $B$.

:::

:::

::: pf-step

$E$ is compact.

::: pf-proof

Let $\mathcal{U}$ be an open cover of $E$. By step [](#subcover){.pf-ref} the sets $p^{-1}(W_{b_{i}})$, $i=1,\dots,m$, cover $E$, and by step [](#local-finiteness){.pf-ref} each is covered by finitely many members of $\mathcal{U}$. The union of those finitely many finite subcollections is a finite subcollection of $\mathcal{U}$ covering $E$.

:::

:::

::::

:::

::: pf-step

Therefore the four properties pass from $B$ to $E$, and $E$ is compact when $B$ is compact with finite fibres.

::: pf-proof

Part [](#a){.pf-ref} gives the four implications of (a), one at each of steps [](#hausdorff){.pf-ref}, [](#regular){.pf-ref}, [](#cr){.pf-ref} and [](#locally-compact){.pf-ref}; part [](#b){.pf-ref} gives the compactness of $E$ under the two hypotheses of (b). That is the exercise.

:::

:::

:::

:::
