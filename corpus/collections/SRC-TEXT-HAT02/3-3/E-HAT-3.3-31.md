---
schema: qual/card@1
id: E-HAT-3.3-31
kind: problem
title: Boundary map sends fundamental class to fundamental class
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 31; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 31; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: at each boundary point the global class restricts to the local fundamental
    class of a half-ball, whose boundary is the local generator of the induced boundary
    orientation; a class with that property at every point is the fundamental class of
    $\partial M$. Read at the level of that characterisation.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The local half of this proof was a gesture — the image of the relative fundamental class in the
    local relative group was called the local fundamental class of the half-ball, and its local
    boundary the local generator, with no computation behind either claim. The solution now names the
    half-ball N and its flat part N', the two excisions that reduce the global statement to the pair
    (D^n, D^n-1), and the long exact sequence of the contractible pair that makes the boundary map an
    isomorphism there; and it says that M compact makes the boundary compact, so Lemma 3.27(a)
    applies with A equal to the boundary. Not checked: the global sign, which is the one fixed by
    Exercise 30's collar convention.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Replaced the false half-disk computation. Explicitly, for a half-disk N in D^2 or an annulus,
    N and N cap boundary M are contractible, so the previously used H_2(N,N cap boundary M) is 0,
    not R, and H_1(N cap boundary M) = H_1(D^1) = 0, not R; the asserted deformation retraction
    onto N also does not hold. The correct local pair is (D, boundary D), with D a closed half-ball
    and boundary D consisting of both its flat face and curved cap, so H_n(D,boundary D) = R and
    its boundary map is the suspension isomorphism. The new proof uses A = (M-U) union V and
    proves H_n(M,A) = H_n(D,boundary D) via good-pair quotients (Proposition 2.22 p.124), not a
    global excision. It then uses naturality of the triple (M,A,boundary M-V) and excision on the
    boundary sphere to compare with H_{n-1}(boundary M,boundary M-x). The n = 1 local group is
    treated separately using reduced H_0(S^0) and unreduced H_0 of a point.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The lower-right excision is now the actual comparison: deleting boundary M-V from the pair
    (boundary M,boundary M-x) leaves (V,V-x), so H_{n-1}(V,V-x) is excision-isomorphic to
    H_{n-1}(boundary M,boundary M-x), not to H_{n-1}(boundary M,boundary M-V), which would leave
    (V,empty). The comparison is stated as an equality in the common target H_{n-1}(V,V-x), with
    r_D and r_M induced by inclusion and the same excision on boundary D. Unit tracking is
    corrected: over an arbitrary coefficient ring R a generator is u[D] with u in R's unit group,
    not necessarily +-D, and the boundary normalization carries that unit.

- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    SOURCE DEFERRED, NOT VERIFIED. The local excision in the preceding draft maps from
    H_{n-1}(V,V-x) into H_{n-1}(boundary M,boundary M-x) and H_{n-1}(boundary D,boundary D-x);
    it was incorrectly applied to ambient elements in the proposed equality. The asserted chain
    compatibility was also not constructed. That continuation is now removed and marked deferred.
    Sam has no Ex.31 and the Math 538 sheets have no Ex.31, so the required published solution with
    exact page citations is missing locally. Earlier source-corrected events on this card do not
    constitute a completed source-backed proof under the current source requirement.

- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Replaces the deferred compatibility attempt with a complete published proof: J. P. May,
    Concise Course in Algebraic Topology, §21.4, pp.169-170 (project file
    tmp/sources/may-concise-algebraic-topology.pdf). Across the boundary chart U with flat face V
    and interior y, the excisions, the collar pair homotopy equivalence, and the connecting
    isomorphism of the triple (M,M-U^o,M-U) transport the local interior orientation to a generator
    in H_{n-1}(boundary M,boundary M-x). May's next proposition identifies that class with the
    relative fundamental class using a compact collar complement N in the interior oriented manifold.
    Naturality of the diagram, rather than the invalid earlier e_M/e_D square, concludes delta[M]
    equals the unique boundary fundamental class. R-units, not mere signs, are preserved.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    NOT ACCEPTED: the preceding completion claim and the May-based solution are withdrawn. May's
    first displayed identification on p.169 is false for his stated chart. Take M=[0,1], x=0,
    U=[0,epsilon), V={0}, and y in (0,epsilon). Then
    (M^o,M^o-U^o)=((0,1),[epsilon,1)); both spaces are contractible, so its H_1 is zero, whereas
    H_1((0,1),(0,1)-{y})=R. This is not an excision isomorphism, and the closed-half-disk variant
    has the same defect. May's printed inclusion (M-U^o)-{x} to M-U is also not an inclusion in
    that direction: its source contains V-{x}, which its target omits. The last map is not the
    claimed excision either. In addition, the p.170 injectivity argument uses H_n(M^o)=0 without
    excluding closed components of M, although Hatcher's exercise permits them. May's retained
    Errata.pdf contains no p.169 correction. Michael Paluch's Lecture 39, pp.111-112, repeats the
    same chain and is not a repaired source. None of these sources is accepted as supplying the
    compatibility.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Replaces the defective May argument with Glen E. Bredon, Topology and Geometry, Chapter VI,
    Section 9, Lemma 9.1, printed pp.356-357 (PDF page 193 of the retained scan). Bredon proves
    [boundary M]=boundary_*[M] by using the triple (M,A union B,B) for one boundary component A
    at a time, not the false chart chain. The integral argument and its torsion-free cokernel were
    checked against the page image. The solution also checks the mod-2 case, coefficient-change
    naturality for arbitrary R, unit multiples of fundamental classes, and the componentwise
    reduction; closed components therefore need no global injectivity assertion.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read the replacement proof in full. The required compatibility is supplied by Bredon's exact
    sequence and excision to each boundary component. In the integral case the cokernel is
    torsion-free, forcing the map between infinite cyclic groups to be onto; in the mod-2 case the
    exact sequence is 0 to Z_2 to Z_2. Naturality under Z to R, or under Z_2 to R when 2R=0,
    gives the arbitrary-R statement up to the global unit on each connected component. The
    bracketed question on E-HAT-3.3-21 is a separate open item and is unchanged.

---

::: {.problem}
Show that if $M$ is a compact $R$-orientable $n$-manifold, then the boundary map $H_n(M, \partial M; R) \to H_{n-1}(\partial M; R)$ sends a fundamental class for $(M, \partial M)$ to a fundamental class for $\partial M$.
:::

::: {.solution}
Use **Glen E. Bredon, *Topology and Geometry*, Chapter VI, §9, Lemma 9.1, printed pp. 356--357** (PDF page 193 of `tmp/sources/bredon-topology-and-geometry.pdf`). Bredon proves precisely the required compatibility, $[\partial M]=\partial_*[M]$. The following is his argument, with the coefficient and disconnected cases made explicit.

Compactness leaves only finitely many components of $M$. The long exact sequences of the pairs and the local characterization of fundamental classes split over these components, so we may assume that $M$ is connected. A closed component has empty boundary and needs no further argument; in particular, no global injectivity claim is required. Assume now that $\partial M\ne\varnothing$.

First take integral coefficients and suppose that $M$ is orientable. Let $A$ be a component of $\partial M$ and put $B=\partial M\setminus A$. The exact sequence of the triple $(M,A\cup B,B)$ contains
$$
H_n(M,B)\longrightarrow H_n(M,\partial M)
\xrightarrow{\ \partial_A\ }H_{n-1}(\partial M,B)
\longrightarrow H_{n-1}(M,B).
$$
Excision identifies $H_{n-1}(\partial M,B)$ with $H_{n-1}(A)$. If $c$ is a representative relative cycle for $[M]$, then $\partial_A[M]$ is represented by the part of $\partial c$ lying in $A$. Thus surjectivity of $\partial_A$ is exactly what is needed for this boundary component.

Bredon's collar and orientation-sheaf computation gives $H_n(M,B;G)=0$ for every coefficient group $G$: after excision this is a compactly supported section group over the connected noncompact manifold $M^\circ\setminus(B\times(0,1))$. Taking $G=\QQ/\ZZ$ and applying the universal coefficient theorem shows that $H_{n-1}(M,B;\ZZ)$ is torsion-free. The displayed exact sequence therefore becomes
$$
0\longrightarrow H_n(M,\partial M;\ZZ)
\xrightarrow{\ \partial_A\ }H_{n-1}(A;\ZZ)
\longrightarrow \text{a torsion-free group}.
$$
Here $H_n(M,\partial M;\ZZ)\cong\ZZ$, while $H_{n-1}(A;\ZZ)$ is either $\ZZ$ or $0$ according as $A$ is orientable. Since the cokernel is torsion-free, the second group must be $\ZZ$ and $\partial_A$ must be onto. Hence $\partial_A$ is multiplication by $\pm1$. Doing this for every $A$ proves Bredon's identity
$$
\partial_*[M]_{\ZZ}=[\partial M]_{\ZZ}.
$$

The same argument with $\ZZ_2$ coefficients requires no orientability hypothesis. Both $H_n(M,\partial M;\ZZ_2)$ and $H_{n-1}(A;\ZZ_2)$ are $\ZZ_2$, so the beginning of the exact sequence is $0\to\ZZ_2\to\ZZ_2$ and $\partial_A$ is an isomorphism. This is the unrestricted $\ZZ_2$ case that Bredon also records in Theorem 9.2 on p. 357. Thus the mod-$2$ fundamental class satisfies the same boundary identity.

For general $R$, use naturality of connecting homomorphisms under change of coefficients. If $M$ is $\ZZ$-orientable, apply $\ZZ\to R$ to Bredon's identity. Otherwise, an $R$-orientation forces $2R=0$: on the connected orientation double cover of $M^\circ$, the pullback orientation is invariant under the deck transformation but is also negated by it. Apply $\ZZ_2\to R$ to the mod-$2$ identity instead. In either case coefficient change preserves the local-generator condition, so it carries fundamental classes to fundamental classes and commutes with $\partial_*$. On a connected component, any two $R$-fundamental classes differ by a global unit of $R$. Therefore every $R$-fundamental class, not merely one obtained by coefficient change, has boundary equal to an $R$-fundamental class of $\partial M$. Summing over the components of $M$ gives
$$
\boxed{\partial_*[M]_{R}=[\partial M]_{R}.}
$$
:::
