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

Induct on $k$. For $k=1$, the complement is $\RR^n$ and is contractible. For $k=2$, it is asin~$D^1$ and Proposition 2B.1(a) applies. To delete a leaf edge $e$ with terminal vertex $v$, let $T'$ be the other $k-1$ vertices and their edge set, and take $A=S^n-e$ and $B=S^n-T'$. Their union is $S^n-v\simeq\RR^n$, while their intersection is $S^n-T$. The reduced Mayer--Vietoris sequence and the induction hypothesis give $\widetilde H_i(S^n-T)=0$.
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

Induct on the number $r$ of edges outside a maximal subtree. Suppose $Y$ is obtained by removing one such edge from $X$. Then $Y$ has $r-1$ such edges already accounted for, and the induction hypothesis gives $\widetilde H_{n-2}(S^n-Y)\cong\ZZ^{r-1}$ and no other nonzero reduced group. Let the new edge have endpoints $w_0,w_1$ (allowed to coincide). As in the published solution, put $A=S^n-e$ and $B=S^n-Y$; their intersection is $S^n-X$ and their union is $S^n-\{w_0,w_1\}$ when the endpoints are distinct, or $S^n-w_0$ otherwise. Since $A$ is contractible in the reduced computations, reduced Mayer--Vietoris leaves
$$
0\to\widetilde H_{n-1}(S^{n-1})=\ZZ\to\widetilde H_{n-2}(S^n-X)
\to\widetilde H_{n-2}(S^n-Y)=\ZZ^{r-1}\to0
$$
in degree $n-2$. Splitting gives $\widetilde H_{n-2}(S^n-X)\cong\ZZ^r$. Away from $n-1$ and $n-2$ the earlier induction statement already gives the same groups, while in degree $n-1$ exactness gives zero. If $w_0=w_1$, the endpoint set is a point, so $S^n-w_0\simeq\RR^n$ and the conclusion also holds.
:::

:::

:::


This is **Kenneth DeMason's proof in *M382C Full Credit HW Problems* (2021)**, Hatcher 2.B.2, printed pp. 70--71. The source uses the tree-first hint: contracts a leaf to a vertex to induct on trees, and then adds edges outside a maximal subtree to obtain the displayed formula from the split Mayer--Vietoris sequence.

:::
