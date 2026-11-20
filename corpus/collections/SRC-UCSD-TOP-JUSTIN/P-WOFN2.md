---
schema: qual/card@1
id: P-WOFN2
kind: problem
title: Homology of two solid tori glued by the identity along the boundary torus
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: This statement is also problem 8 of the official UGA Spring 2008 topology exam; added that missing source appearance.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Twelve steps asserted their claim with no justification and each now carries one: the identity of
    $B^2$ with the disc and of its boundary with $S^1$, the hemisphere decomposition that identifies the
    doubled disc with $S^2$ together with the compact-to-Hausdorff argument, the factoring of the gluing
    through the product, the homology of the circle and the sphere from their CW structures, the vanishing
    of the Tor terms for free groups, the evaluation of the Künneth summands degree by degree, the cover
    by the two solid tori with their homotopy types and their common boundary, the form of the
    Mayer--Vietoris sequence for a cover by two sets whose interiors cover, the isomorphism
    $H_3(M) \cong H_2(T^2)$, the action of $(i_*, j_*)$ on the longitudinal and meridian generators with the
    kernel and cokernel that follow, and the closing agreement of the two computations. Checked while
    writing: the meridian bounds a disc inside each solid torus, which is why it maps to zero while the
    longitude maps to the diagonal; that is the whole content of the kernel and cokernel count. Four
    pf-qed blocks went: one duplicated the claim of the step above it, the two others only pointed back at
    the steps whose results they repeated, and the fourth only said the two computations agree. The four
    container steps carried labels and now state the claim their proofs establish, and the closing step no
    longer opens with "Conclusion.". Sources are cited by numbered statement, the Künneth formula and the
    Mayer--Vietoris sequence; no page reference appears on the card or in its events. The statement is
    unchanged. The collection retains the UCSD 290 problem sheets and no solutions, so the argument is the
    card's own.
---

::: {.problem}
Let $X$ consist of two copies of the solid torus $\DD^2 \times S^1$, glued together by the identity map along the boundary torus $S^1 \times S^1$.
Compute the homology groups of $X$.
:::

::: {.solution}
Let $U_1 = S^1 \times B^2$ and $U_2 = S^1 \times B^2$ be the two solid tori, glued along their boundaries $\partial(S^1 \times B^2) = S^1 \times S^1 = T^2$ via the identity map $\operatorname{id}_{\partial}$, and let $M = U_1 \cup_{T^2} U_2$ denote the space $X$ of the problem.

::: pf

::: pf-step
$M$ is homeomorphic to $S^1 \times S^2$.

::: pf-proof

::: pf-step
$B^2$ is the 2-disk $D^2$, whose boundary is $S^1$.

::: pf-proof
$B^2$ is the closed unit ball in $\RR^2$, and the closed unit ball in the plane is the closed disc of radius $1$, so the two symbols name the same space; its boundary is the set of unit vectors in $\RR^2$, which is $S^1$.
:::

:::

::: pf-step
Gluing two copies of the 2-disk $D^2$ along their common boundary via the identity map yields the 2-sphere $S^2$: $$D^2 \cup_{\operatorname{id}_{S^1}} D^2 \cong S^2.$$

::: pf-proof
Two closed discs glued along their boundary circles by the identity give $S^2$: split $S^2$ into its upper and lower closed hemispheres, each a closed disc whose boundary is the equator, and the gluing restores exactly the points of the equator. The quotient map from the disjoint union is continuous, the quotient is compact as an image of a compact space, and the induced bijection onto $S^2$ goes from a compact space to a Hausdorff space, hence is a homeomorphism.
:::

:::

::: pf-step
Since the gluing map on $S^1 \times \partial B^2$ is $\operatorname{id}_{S^1 \times \partial B^2} = \operatorname{id}_{S^1} \times \operatorname{id}_{S^1}$, the product structure factors through the gluing: $$M = (S^1 \times B^2) \cup_{\operatorname{id}} (S^1 \times B^2) \cong S^1 \times (B^2 \cup_{\operatorname{id}} B^2) \cong S^1 \times S^2.$$

::: pf-proof
The gluing identifies $(x, u)$ in the boundary of the first solid torus with $(x, u)$ in the boundary of the second, because the gluing map is the identity; so two points are identified only when their first coordinates agree. The map to $S^1 \times S^2$ that is the identity on the $S^1$ factor and the disc-gluing quotient on the $B^2$ factor therefore respects the identifications and induces a continuous bijection $M \to S^1 \times S^2$ from a compact space to a Hausdorff space, which is a homeomorphism.
:::

:::

:::

:::

::: {.pf-step #s2}
$H_k(S^1 \times S^2;\ZZ) \cong \ZZ$ for $k = 0, 1, 2, 3$ and is zero for $k \ge 4$.

::: pf-proof

::: pf-step
The homology groups of the circle $S^1$ and the sphere $S^2$ are:

- $H_0(S^1) \cong \ZZ$, $H_1(S^1) \cong \ZZ$, $H_k(S^1) = 0$ for $k \ge 2$.

- $H_0(S^2) \cong \ZZ$, $H_2(S^2) \cong \ZZ$, $H_k(S^2) = 0$ for $k \neq 0, 2$.

::: pf-proof
$S^1$ has a CW structure with one $0$-cell and one $1$-cell, so its cellular chain complex has $\ZZ$ in degrees $0$ and $1$ and the boundary is zero, giving $H_0 = H_1 = \ZZ$ and nothing above. $S^2$ has one $0$-cell and one $2$-cell with zero boundary, giving $H_0 = H_2 = \ZZ$ and nothing in degree $1$; a sphere of dimension $n \ge 0$ has reduced homology only in degree $n$.
:::

:::

::: pf-step
Since all homology groups of $S^1$ and $S^2$ are free abelian groups, all Tor terms $\operatorname{Tor}_1^\ZZ(H_i(S^1), H_j(S^2))$ vanish.

::: pf-proof
A free abelian group has the two-term free resolution $0 \to F \to F \to 0$ with the identity as the map, so the higher derived functors of the tensor product vanish on it; hence $\operatorname{Tor}_1^\ZZ(F, G) = 0$ for every $F$ free and every $G$, and the groups here are free, so every Tor term in the sequence vanishes.
:::

:::

::: {.pf-step #s2-3}
The Künneth formula gives an isomorphism $H_k(M) \cong \bigoplus_{i+j=k} (H_i(S^1) \otimes_\ZZ H_j(S^2))$ for each $k \ge 0$:

- $k = 0$: $H_0(S^1) \otimes H_0(S^2) = \ZZ \otimes \ZZ \cong \ZZ$.

- $k = 1$: $(H_1(S^1) \otimes H_0(S^2)) \oplus (H_0(S^1) \otimes H_1(S^2)) = (\ZZ \otimes \ZZ) \oplus 0 \cong \ZZ$.

- $k = 2$: $(H_0(S^1) \otimes H_2(S^2)) \oplus (H_1(S^1) \otimes H_1(S^2)) \oplus (H_2(S^1) \otimes H_0(S^2)) = (\ZZ \otimes \ZZ) \oplus 0 \oplus 0 \cong \ZZ$.

- $k = 3$: $(H_1(S^1) \otimes H_2(S^2)) = \ZZ \otimes \ZZ \cong \ZZ$.

- $k \ge 4$: All terms are 0, so $H_k(M) = 0$.

::: pf-proof
The Künneth short exact sequence is $0 \to \bigoplus_{i+j=k} H_i(S^1)\otimes H_j(S^2) \to H_k(S^1\times S^2) \to \bigoplus_{i+j=k-1}\operatorname{Tor}_1(H_i(S^1), H_j(S^2)) \to 0$; the Tor summands vanish by the previous step, so the first map is an isomorphism. Evaluating: in degree $0$ only $(0,0)$ contributes, in degree $1$ only $(1,0)$, in degree $2$ only $(0,2)$ since $H_1(S^2) = 0$, in degree $3$ only $(1,2)$, and every pair with $i+j = k \ge 4$ has $H_i(S^1) = 0$ or $H_j(S^2) = 0$, so the group is zero.
:::

:::

:::

:::

::: {.pf-step #s3}
The Mayer--Vietoris sequence for the cover by the two solid tori gives the same groups.

::: pf-proof

::: pf-step
Let $A = S^1 \times B^2$ and $B = S^1 \times B^2$.

::: pf-proof
The two solid tori $S^1 \times B^2$ are the two halves of which $M$ is the union, glued along their boundaries; this names them so that the Mayer--Vietoris sequence can be applied to the cover $\{A, B\}$ of $M$.
:::

:::

::: pf-step
$A \simeq S^1$, $B \simeq S^1$, and $A \cap B \cong S^1 \times S^1 = T^2$.

::: pf-proof
Each solid torus deformation retracts onto its core circle $S^1 \times \{0\}$, through $(x, y, t) \mapsto (x, (1-t)y)$, so $A$ and $B$ are homotopy equivalent to $S^1$. Their intersection is the common boundary, which is $S^1 \times \partial B^2 = S^1 \times S^1 = T^2$ because the gluing is along the whole boundary.
:::

:::

::: pf-step
The Mayer-Vietoris long exact sequence is: $$0 \to H_3(M) \xrightarrow{\partial} H_2(T^2) \xrightarrow{(i_*, j_*)} H_2(A) \oplus H_2(B) \to H_2(M) \xrightarrow{\partial} H_1(T^2) \xrightarrow{(i_*, j_*)} H_1(A) \oplus H_1(B) \to H_1(M) \to \widetilde{H}_0(T^2) \to 0.$$

::: pf-proof
For $M$ the union of two subspaces whose interiors cover it, Mayer--Vietoris gives the exact sequence $\cdots \to H_n(A \cap B) \to H_n(A)\oplus H_n(B) \to H_n(M) \to H_{n-1}(A\cap B) \to \cdots$. Since $A$, $B$ and $A \cap B$ are path-connected, the degree-zero terms can be replaced by reduced homology, which vanishes there, so the sequence can be written beginning at $H_3(M)$ and ending at $\widetilde H_0(T^2) \to 0$; inserting the groups computed above gives the displayed sequence.
:::

:::

::: pf-step
$H_2(A) = H_2(B) = 0$, so $0 \to H_3(M) \xrightarrow{\partial} H_2(T^2) \cong \ZZ \to 0 \implies H_3(M) \cong \ZZ$.

::: pf-proof
$A$ and $B$ are homotopy equivalent to $S^1$, whose homology vanishes above degree $1$, so $H_2(A) = H_2(B) = 0$; the segment of the sequence $H_2(A)\oplus H_2(B) \to H_2(M) \to H_1(T^2) \to H_1(A)\oplus H_1(B)$ then begins with a zero group, and the hypothesis of exactness at $H_3(M)$ and at $H_2(T^2)$ makes $\partial$ an isomorphism between them, with $H_2(T^2) \cong \ZZ$.
:::

:::

::: pf-step
The map $(i_*, j_*) \colon H_1(T^2) \cong \ZZ^2 \to H_1(A) \oplus H_1(B) \cong \ZZ^2$ maps the longitudinal circle generator $(1, 0) \mapsto (1, 1)$ and the meridian circle generator $(0, 1) \mapsto (0, 0)$.

- Thus $\ker(i_*, j_*) \cong \ZZ$ (generated by the meridian $(0, 1)$) and $\operatorname{coker}(i_*, j_*) \cong \ZZ$.

- From $0 \to H_2(M) \xrightarrow{\partial} \ker(i_*, j_*) \to 0$, we get $H_2(M) \cong \ZZ$.

- From $0 \to \operatorname{coker}(i_*, j_*) \to H_1(M) \to 0$, we get $H_1(M) \cong \ZZ$.

::: pf-proof
The longitudinal circle of $T^2 = \partial(S^1 \times B^2)$ is the curve $S^1 \times \{u\}$ for a boundary point $u$, and it is the core circle of both solid tori, so it represents the generator of $H_1(A)$ and the generator of $H_1(B)$ at once, which is the pair $(1,1)$. The meridian is $\{x\} \times \partial B^2$, which bounds the disc $\{x\} \times B^2$ inside each solid torus, so it is null-homotopic there and maps to $(0,0)$. The kernel of $(i_*, j_*)$ is therefore the $\ZZ$ spanned by the meridian and its cokernel the $\ZZ$ spanned by the class of $(1,1)$, and exactness gives $H_2(M) \cong \ker$ and $H_1(M) \cong \operatorname{coker}$.
:::

:::

:::

:::

::: pf-step
The homology of $M$ is $\ZZ$ in degrees $0, 1, 2, 3$ and zero above.

::: pf-proof

::: pf-step
The homology groups of $M$ are: $$H_0(M; \ZZ) \cong \ZZ, \quad H_1(M; \ZZ) \cong \ZZ, \quad H_2(M; \ZZ) \cong \ZZ, \quad H_3(M; \ZZ) \cong \ZZ,$$ and $H_k(M; \ZZ) = 0$ for all $k \ge 4$.

::: pf-proof
The Künneth computation gives $\ZZ$ in degrees $0$, $1$, $2$, $3$ and zero above, and the Mayer--Vietoris computation gives the same four groups through $\ker$ and $\operatorname{coker}$ of the map on $H_1(T^2)$; the two independent computations agree, and $M$ is connected so $H_0 \cong \ZZ$ in both. A compact $3$-manifold has no homology in degrees above $3$.
:::

:::

:::

:::

:::
:::
