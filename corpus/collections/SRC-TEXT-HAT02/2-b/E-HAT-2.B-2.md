---
schema: qual/card@1
id: E-HAT-2.B-2
kind: problem
title: "Homology of complements of finite graphs in spheres"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the Alexander-duality and Mayer--Vietoris calculations and all degree shifts.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 2, printed page
    176, with the printed hint. Checked: a finite tree is contractible, so Alexander
    duality (Theorem 3.44, p. 253) makes the complement's reduced homology vanish; in
    general the homology of a connected graph is free with H_0 = Z and H_1 of rank r,
    so the universal coefficient theorem (Theorem 3.2, p. 195) has no Ext term and
    H̃^j(X) ≅ H̃_j(X), giving H̃_i(S^n − X) ≅ H̃_{n−i−1}(X) and H̃_{n−2} ≅ Z^r. No
    defect.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Checked against DeMason, M382C Full Credit HW Problems (2021), Hatcher 2.B.2, pp.70-71: a
    tree is contractible, and induction on edges outside a maximal subtree keeps track of the
    complement and the rank of H_1. The card's Alexander-duality formulation is equivalent and
    applies to every embedded finite graph (compact and locally contractible). Its identification
    of the reduced cohomology with homology uses that H_*(graph) is free, so Ext(H_0(graph),Z)=0.

- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Substituted the actual DeMason induction, rather than retaining an independently derived
    Alexander-duality argument. DeMason pp.70-71 first contracts a leaf to show an embedded tree
    has reduced complement homology zero. Adding each non-tree edge then uses the same reduced
    Mayer-Vietoris pairs through the two endpoint vertices, and at degree n-2 gives a split sequence
    0 -> Z -> H~_{n-2}(S^n-X) -> Z^{r-1} -> 0, hence Z^r. Distinct endpoints and loop-endpoint cases
    are stated, and the source's splitting direction and rank are preserved. The blank following the
    final display is restored and the previous audit item is inside the YAML audit list.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Repaired the actual proof, not the source metadata. In the tree step, the leaf u and attachment
    vertex v are distinguished: with A=S^n-e and B=S^n-T' one has A cap B = S^n-X and A union B =
    S^n-v, exactly the cover in the published argument. For added loop edges, first barycentrically
    subdivide to make endpoints distinct rather than treating the loop's complement as that of a
    disk. The full applicable sequence has left term H_{n-1}(S^{n-1})=Z, not homology of a point,
    and splits to give Z^r. Both statements match pp.70-71 of DeMason.

---

::: {.problem}
Show that $\tilde{H}_i(S^n - X) \approx \tilde{H}_{n-i-1}(X)$ when $X$ is homeomorphic to a finite connected graph.
[First do the case that the graph is a tree.]
:::

::: {.solution}
Use DeMason's proof on pp. 70--71. The homology of a tree has already vanished in reduced degree, so it remains to see how adding edges changes the complement.

::: pf

::: {.pf-step #tree}

If $T\subset S^n$ is an embedded tree with $k$ vertices, then $\widetilde H_i(S^n-T)=0$ for every $i$.

::: pf-proof

Induct on $k$. For $k=1$, remove a point, complementing it in $S^n$; it is homeomorphic to $\RR^n$, hence contractible. For $k=2$, Proposition 2B.1(a) gives vanishing. For the induction, let $T'$ be the tree obtained by collapsing a leaf edge $e$ and let $A=S^n-e$, $B=S^n-T'$. If $u$ is the leaf and $v$ is its attachment vertex, then $e\cap T'=\{v\}$, and $X=e\cup T'$ is the whole embedded tree. Hence $A\cup B=S^n-v\simeq\RR^n$ and $A\cap B=S^n-X$. This matches the source's cover and does not assert a deformation retraction of the whole ambient sphere. Reduced Mayer--Vietoris and the induction hypothesis give $\widetilde H_i(S^n-X)=0$.
:::

:::

::: {.pf-step #loops}

If $X$ is a finite connected graph, contract a maximal subtree. This gives $r\ge0$ independent loop edges, and
$$
\widetilde H_i(S^n-X)\cong
\begin{cases}
\ZZ^r,&i=n-2,\\
0,&\text{otherwise.}
\end{cases}
$$

::: pf-proof

Induct on the number $r$ of edges outside a maximal subtree. Suppose $Y$ is obtained by removing one such edge from $X$. Then $Y$ has $r-1$ such edges already accounted for, and the induction hypothesis gives $\widetilde H_{n-2}(S^n-Y)\cong\ZZ^{r-1}$ and no other nonzero reduced group. If an added edge is a loop, first barycentrically subdivide that edge once. This replaces its image by two intervals, preserves the same embedded subspace $X$ and its complement, and makes its endpoints distinct; then apply the source argument to the subdivided graph. For a non-loop or for one of these subdivided intervals, let the endpoints be the distinct points $w_0,w_1$. Put $A=S^n-e$ and $B=S^n-Y$. The complement of the closed edge has the reduced homology of $D^1$ inside a sphere by the starting case of the induction, so the appropriate terms from $A$ vanish, while the intersection is $S^n-X$ and the union is $S^n-\{w_0,w_1\}\simeq S^{n-1}$. Then the applicable exact terms are
$$
0\to\widetilde H_{n-1}(S^{n-1})=\ZZ
\to\widetilde H_{n-2}(S^n-X)
\to\widetilde H_{n-2}(S^n-Y)=\ZZ^{r-1}
\to\widetilde H_{n-2}(S^{n-1})=0.
$$
The left $\ZZ$ is $H_{n-1}(S^{n-1})$, not the reduced homology of a point. Splitting of $\ZZ^{r-1}$ gives the claimed rank $\widetilde H_{n-2}(S^n-X)\cong\ZZ^r$. Away from $n-1$ and $n-2$ the remainder of the same exact sequence already gives the induced groups, while in degree $n-1$ exactness gives zero.
:::

:::

:::


This is **Kenneth DeMason's proof in *M382C Full Credit HW Problems* (2021)**, Hatcher 2.B.2, printed pp. 70--71. The source uses the tree-first hint: contracts a leaf to a vertex to induct on trees, and then adds edges outside a maximal subtree to obtain the displayed formula from the split Mayer--Vietoris sequence.

:::
