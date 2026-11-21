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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Converted from prose to numbered steps under #2, nine of them. The argument is Bredon's,
    Chapter VI §9, Lemma 9.1 and the theorem of that section numbered 9.2, both read in the retained
    file, and the card cites them by chapter, section and number only. Three things the prose left as
    assertions are now proved: that a component with empty boundary needs no argument and that the
    pair sequences split over the components; that $H_{n-1}(M,B;\ZZ)$ is finitely generated, which is
    what lets the tensor vanishing with $\QQ/\ZZ$ force it to be zero, with the group computation
    $A\otimes\QQ/\ZZ\cong(\QQ/\ZZ)^r\oplus T$ written out; and that two $R$-fundamental classes on a
    connected manifold with boundary differ by a unit of $R$. Not checked: no certificate, and no
    source beyond Bredon was read for the collar computation of step #vanish, which is cited and not
    reproduced.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Mechanical LaTeX repair, reported by the whole-corpus gate at this date's tree and made here so
    that the gate is usable again; no mathematics changes. A scripted rewrite split words:
    `isomor\varphism` for "isomorphism" three times and `homomor\varphisms` for "homomorphisms" once.
    The count repaired is 4. Every step and every claim of the argument stands as it stood; only those
    words change. Checked: `qualc.authoring check` on the card, and `varphism` no longer occurs in it.
    Not checked: no source and no step of the argument was re-read in this pass, the repair being
    spelling.
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

- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §3.3. Read against Hatcher, Exercise 31 of §3.3, printed p. 260, and
    the printed page is added, the card having had none. One inference repaired. The step from
    "$H_n(M,B;G)=0$ for every $G$" to the surjectivity of the boundary map said the universal
    coefficient theorem makes $H_{n-1}(M,B;\ZZ)$ torsion-free and that a torsion-free cokernel forces
    surjectivity. Both halves fail: a torsion-free cokernel does not force surjectivity, as the zero
    map $\ZZ$ to $\ZZ$ shows, and the coefficient group $\QQ/\ZZ$ gives more than torsion-freeness. With
    that coefficient the universal coefficient sequence gives
    $H_{n-1}(M,B;\ZZ)$ tensor $\QQ/\ZZ$ equal to zero, and a finitely generated group with that property
    is zero, so $H_{n-1}(M,B;\ZZ)=0$ and the fragment is a short exact sequence whose first map is an
    isomorphism. The step now says this, and derives both that the component is orientable and that
    the boundary map is multiplication by a unit. Checked and unchanged: the triple sequence, the
    excision, the component reduction, the mod-two case where both groups are $\ZZ_2$, and the
    change-of-coefficients argument for general $R$, including the $2R=0$ alternative. Not re-read
    this pass: Bredon's printed pp. 356--357, which supply the vanishing; the event of 2026-11-07
    records that reading.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The solution body wrote its two coefficient rings with a doubled backslash throughout, 34
    tokens, which render as a line break followed by the letters of the macro rather than as the
    ring: every occurrence of the two macros in the argument is restored. The Bredon citation
    named a page of the local file; it now names the chapter, the section and the numbered results,
    Lemma 9.1 and the theorem numbered 9.2 of Chapter VI §9, which are what the argument uses, and
    the retained file is named without a locator. No mathematics changed. Not checked: the conversion
    of this card's prose into numbered steps is not part of this commit and remains the card's next
    item.

---

::: {.problem}
Show that if $M$ is a compact $R$-orientable $n$-manifold, then the boundary map $H_n(M, \partial M; R) \to H_{n-1}(\partial M; R)$ sends a fundamental class for $(M, \partial M)$ to a fundamental class for $\partial M$.
:::

::: {.solution}
The argument is that of the retained source: **Glen E. Bredon, *Topology and Geometry*, Chapter VI §9**, Lemma 9.1 and the theorem of that section numbered 9.2, read in `tmp/sources/bredon-topology-and-geometry.pdf`. Bredon proves the required compatibility $[\partial M]=\partial_*[M]$; the steps below are his argument with the coefficient and disconnected cases made explicit. Throughout, $M$ is a compact $R$-orientable $n$-manifold and $\partial_*$ is the connecting homomorphism of the pair $(M,\partial M)$.

::: pf

::: {.pf-step #components}
It suffices to prove the identity on each component of $M$.

::: pf-proof
$M$ is compact, so it has finitely many components. The long exact sequence of the pair is the direct sum of the sequences of the components, and a fundamental class of $(M,\partial M)$ with coefficients $R$ is a tuple of fundamental classes of the components, each local condition being read in one component. A component with empty boundary has $H_n(M_i,\partial M_i;R)=H_n(M_i;R)$ and its class is the class of the closed component itself, so the identity for it says nothing new. Hence it suffices to treat a connected $M$ with $\partial M\ne\varnothing$.
:::

:::

::: {.pf-step #triple}
For a component $A$ of $\partial M$ with $B=\partial M\setminus A$, the exact sequence of the triple $(M,A\cup B,B)$ contains $H_n(M,B;R)\to H_n(M,\partial M;R)\xrightarrow{\partial_A}H_{n-1}(\partial M,B;R)\to H_{n-1}(M,B;R)$, and excision identifies $H_{n-1}(\partial M,B;R)$ with $H_{n-1}(A;R)$.

::: pf-proof
The triple sequence is exact, and the map written $\partial_A$ is the composite of its boundary map with the isomorphism of excision for the pair $(\partial M,B)$ and the subset $A$, whose closure meets $B$ in a closed set contained in the interior of $A$; the triple's third term is the same group. If $c$ is a relative cycle representing $[M]$, then $\partial_Ac$ is represented by the part of $\partial c$ lying in $A$, so $\partial_A$ is surjective exactly when the boundary of the fundamental class has the local behaviour of a fundamental class of $\partial M$ at $A$.
:::

:::

::: {.pf-step #vanish}
$H_n(M,B;G)=0$ for every coefficient group $G$.

::: pf-proof
This is Bredon's collar and orientation-sheaf computation: after excising $M$ minus a collar of $B$, the group is a compactly supported section group of the orientation sheaf over the connected noncompact manifold obtained by removing the collar of $B$, and a compactly supported section over a connected noncompact manifold vanishes in the top degree.
:::

:::

::: {.pf-step #integral}
With integral coefficients and $M$ orientable, $\partial_A\colon H_n(M,\partial M;\ZZ)\to H_{n-1}(A;\ZZ)$ is an isomorphism.

::: pf-proof
Take $G=\QQ/\ZZ$ in step [](#vanish){.pf-ref} and in the universal coefficient sequence of the pair, which reads $0\to H_{n-1}(M,B;\ZZ)\otimes\QQ/\ZZ\to H_n(M,B;\QQ/\ZZ)\to\Tor(H_{n-2}(M,B;\ZZ),\QQ/\ZZ)\to0$; the first term vanishes. The group $H_{n-1}(M,B;\ZZ)$ is finitely generated, since $M$ is a compact manifold and so has the homotopy type of a finite complex, and a finitely generated abelian group $A$ with $A\otimes\QQ/\ZZ=0$ is zero: writing $A=\ZZ^r\oplus T$ gives $A\otimes\QQ/\ZZ\cong(\QQ/\ZZ)^r\oplus T$, which vanishes only for $r=0$ and $T=0$. So $H_{n-1}(M,B;\ZZ)=0$, and step [](#triple){.pf-ref} becomes the short exact sequence $0\to H_n(M,\partial M;\ZZ)\xrightarrow{\partial_A}H_{n-1}(A;\ZZ)\to0$. Both outer groups are $\ZZ$, the first because $[M]$ is a fundamental class and the second because $A$ is a closed connected orientable $(n-1)$-manifold, so $\partial_A$ is an isomorphism and, for each $A$, the component of $\partial[M]$ in $A$ is a generator.
:::

:::

::: {.pf-step #orientable}
If $M$ is orientable then $\partial_*[M]_{\ZZ}=[\partial M]_{\ZZ}$.

::: pf-proof
Step [](#integral){.pf-ref} applied to every component $A$ of $\partial M$ says that $\partial_*[M]_{\ZZ}$ has, in each component of $\partial M$, a generator as its component, which is the local characterisation of a fundamental class of $\partial M$; two classes with the same local generators in every component are equal, since the components of a closed manifold are its path components.
:::

:::

::: {.pf-step #mod2}
With $\ZZ_2$ coefficients the identity holds with no orientability hypothesis.

::: pf-proof
Every compact manifold is $\ZZ_2$-orientable, so $[M]$ and $[\partial M]$ exist over $\ZZ_2$. Steps [](#triple){.pf-ref}, [](#vanish){.pf-ref} and [](#integral){.pf-ref} repeat with $\ZZ_2$ in place of $\ZZ$: both $H_n(M,\partial M;\ZZ_2)$ and $H_{n-1}(A;\ZZ_2)$ are $\ZZ_2$, and the exact sequence begins $0\to\ZZ_2\xrightarrow{\partial_A}\ZZ_2$, so $\partial_A$ is an isomorphism and the boundary of the mod-two fundamental class is the mod-two fundamental class of $\partial M$. This is the unrestricted case Bredon records as the theorem numbered 9.2 of Chapter VI §9.
:::

:::

::: {.pf-step #coefficients}
For an $R$-orientable $M$ the identity holds over $R$: $\partial_*[M]_R=[\partial M]_R$.

::: pf-proof
Change of coefficients is natural for connecting homomorphisms, so a ring map $S\to R$ carries the identity over $S$ to the identity over $R$ and carries fundamental classes to fundamental classes, since the local condition is a statement about images in $H_n(M,M-x;S)\to H_n(M,M-x;R)$. If $M$ is $\ZZ$-orientable, apply $\ZZ\to R$ to step [](#orientable){.pf-ref}. Otherwise an $R$-orientation forces $2R=0$: on the connected orientation double cover of $M$ minus its boundary, the pulled-back orientation is invariant under the deck transformation and is also negated by it, so multiplication by $2$ acts as the identity on the coefficient ring. Then $\ZZ_2\to R$ is defined and step [](#mod2){.pf-ref} applies.
:::

:::

::: {.pf-step #arbitrary}
Every $R$-fundamental class of $(M,\partial M)$ has boundary a fundamental class of $\partial M$, not only those obtained by coefficient change.

::: pf-proof
On a connected $n$-manifold with boundary, two $R$-fundamental classes differ by a unit of $R$: their local classes at a point agree up to that unit, and a class is determined by its local class at one point because the manifold is connected. The same holds on $\partial M$. So an arbitrary fundamental class is $u\,[M]_R$ for a unit $u$, and step [](#coefficients){.pf-ref} gives $\partial_*(u\,[M]_R)=u\,[\partial M]_R$, again a fundamental class.
:::

:::

::: {.pf-step}
If $M$ is a compact $R$-orientable $n$-manifold then $\partial_*$ sends a fundamental class for $(M,\partial M)$ to a fundamental class for $\partial M$.

::: pf-proof
Steps [](#components){.pf-ref}, [](#coefficients){.pf-ref} and [](#arbitrary){.pf-ref} together cover the components with and without boundary, every coefficient ring, and every choice of fundamental class, which is the assertion.
:::

:::

:::
:::
