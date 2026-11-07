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

---

::: {.problem}
Show that if $M$ is a compact $R$-orientable $n$-manifold, then the boundary map $H_n(M, \partial M; R) \to H_{n-1}(\partial M; R)$ sends a fundamental class for $(M, \partial M)$ to a fundamental class for $\partial M$.
:::

::: {.solution}
Use the collar existence theorem (Hatcher Proposition 3.42, p. 249), since $M$ is compact, and the boundary-orientation argument in **J. P. May, *Concise Course in Algebraic Topology*, §21.4, "Poincaré duality for manifolds with boundary", printed pp. 169--170**, held at `tmp/sources/may-concise-algebraic-topology.pdf`. In particular, the definition at the start of that section says that $M$ being $R$-orientable means that its interior $M^\circ=M\setminus\partial M$ is $R$-orientable as a manifold without boundary.

Fix $x\in\partial M$ and let $U$ be a half-disk boundary chart around $x$, with $U\cong D^n_+=\{(u_1,\dots,u_n)\in D^n:u_n\ge0\}$. Let $V=U\cap\partial M$ be its flat face and choose an interior point $y\in U^\circ=U\setminus V$. May's sequence of identifications is
$$
H_n(M^\circ,M^\circ-U^\circ)
\xrightarrow[\cong]{\operatorname{exc}}
H_n(M^\circ,M^\circ-y)
\cong H_n(M,M-y),
$$
with the unique class in the first term restricting to the orientation at $y$. The boundary homomorphism for the triple $(M,M-U^\circ,M-U)$ then gives
$$
\delta_x:H_n(M^\circ,M^\circ-y)
\xrightarrow{\ \cong\ }H_{n-1}(M-U^\circ,M-U).
$$
The left isomorphism is excision. The inclusion $(M-U^\circ)-\{x\}\hookrightarrow M-U$ is a homotopy equivalence, which identifies its bottom group with
$$
H_{n-1}(\partial M,\partial M-x).
$$
Finally, excising $M^\circ-U^\circ$ identifies this last group with
$$
H_{n-1}(\partial M,\partial M-V).
$$
These are the precise identifications in **May's Proposition**, p. 169. The homomorphism $\delta$ of the triple is an isomorphism because
$$
H_*(M,M-U)=0.
$$
Consequently, $\delta_x$ carries the given local orientation at $y$ to a generator (a unit multiple, not merely a sign) of $H_{n-1}(\partial M,\partial M-x)$.

For the relative fundamental class itself, May's next proposition (p. 170) proceeds as follows. Let $N$ be the part of $M$ outside a collar. Then $N$ is compact in $M^\circ$, and the collar gives May's natural identification
$$
H_n(M,\partial M;R)\cong H_n(M^\circ,M^\circ-N;R).
$$
As in May's displayed argument: $N$ is compact in the noncompact oriented manifold $M^\circ$, so Lemma 3.27(a) (p. 236) supplies a unique class in $H_n(M^\circ,M^\circ-N;R)$ restricting to the chosen orientation at every interior point. Its image $[M]\in H_n(M,\partial M;R)$ is the relative fundamental class. Since a compact collar also identifies $H_n(M)$ and $H_n(M^\circ)$, the vanishing theorem of Proposition 3.29 gives $\delta:H_n(M,\partial M)\hookrightarrow H_{n-1}(\partial M)$.

At this point naturality is the content of May's naturality diagram, not a newly asserted excision: the boundary of $[M]$ restricts under $\delta_x$ exactly to the unique generator determined by the induced boundary orientation from Exercise 30. This holds for every $x\in\partial M$, and there is only one class with this local restriction. Since $\partial M$ is compact, Lemma 3.27(a) applied to $\partial M$ identifies that section as $[\partial M]$; uniqueness gives
$$
\boxed{\partial[M]=[\partial M].}
$$
:::
