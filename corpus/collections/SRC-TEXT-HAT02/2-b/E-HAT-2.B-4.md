---
schema: qual/card@1
id: E-HAT-2.B-4
kind: problem
title: "Linking numbers via Mayer--Vietoris"
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
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 4; the stored statement matches.
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
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 4, printed page
    176, with the printed hint. (a) checked: Φ(x,y) = (y/|y|, x/|y|) is a
    homeomorphism S^{p+q−1} − S^{p−1} → S^{q−1} × R^p with inverse
    (v,u)/√(1+|v|²), and contracting the R^p factor gives the deformation retraction.
    (b) checked: [S^{q−1}] generates H̃_{q−1} of the complement of S^{p−1} (Exercise 3
    applied to (D^p,S^{p−1}) ⊂ (D^{p+q},S^{p+q−1}) makes the inclusion an
    isomorphism on H_{q−1}), yet a disjoint D^q is a chain there bounding it, so the
    class would vanish. No defect.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Examined the indexed answer to Math StackExchange question 666444, including its diagram;
    the direct page fetch presented a Cloudflare challenge. Its map f is zero for a reason that
    also destroys the proposed contradiction: with C=D^{p+q}-D^q and
    A=S^{p+q-1}-S^{q-1}, Exercise 3 makes A into C a homology isomorphism in every degree,
    so H_*(C,A)=0. Thus neither that diagram nor the suggested acyclic-pair shortcut supplies a
    complete published proof. Did not alter the checked bounding-chain proof; the complete
    published-solution obligation remains open.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Repaired a hypothesis gap in (b). The previous step applied Exercise 3 to the pair
    (D^p,S^{p-1}) inside (D^{p+q},S^{p+q-1}), but Exercise 3 requires D^p to meet the boundary
    sphere in exactly S^{p-1}, and the hypothesis of (b) does not give that: an embedded disk with
    boundary S^{p-1} can meet the boundary sphere in the interior of the disk, as the arc
    gamma(t) = (t, 1-t^2) in D^2 shows, with endpoints at (+-1,0) in S^1 and
    norm(gamma(t))^2 = t^4 - t^2 + 1 <= 1, equality exactly at t = 0 and t = +-1, so the arc is
    tangent to S^1 at (0,1). Checked replacement: radial contraction z -> z/norm(z) retracts
    D^{p+q} - S^{p-1} onto S^{p+q-1} - S^{p-1}, since a point (x,y) with y nonzero and
    norm <= 1 has last coordinates y((1-t) + t/norm(x,y)) with bracket >= 1 along the segment;
    that retraction is a homotopy equivalence, the inclusion into D^{p+q} - D^p factors it
    because S^{p-1} is contained in D^p, and a map with injective composite is injective. So the
    inclusion into D^{p+q} - D^p is injective on reduced H_{q-1}, which is all the contradiction
    needs, and no properness is used. Parts (a) and (b)'s bounding-chain argument are otherwise
    unchanged. What is not covered: no complete published solution to (a) has been located, so
    that source obligation stays open; no certificate.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Withdraws the repair recorded in the previous event: the radial-contraction step was FALSE and
    has been removed. Read literally, D^{p+q} - S^{p-1} contains the origin, where z/norm(z) is
    undefined, and it contains the points with y = 0 and norm(x) < 1, whose images under the radial
    formula land in the removed sphere S^{p-1}; so the claimed retraction does not exist and the
    claimed homotopy equivalence is unfounded. Worse, without a properness hypothesis the
    inclusion S^{p+q-1} - S^{p-1} into D^{p+q} - D^p is not even a well-defined map, so
    'the inclusion factors it' was circular: it presupposed exactly the condition the event above
    had shown to be unavailable. The tangent-arc example ((t, 1-t^2) in D^2, tangent to S^1 at
    (0,1)) is precisely a case where the inclusion is undefined. What the card now does: it states
    D^p cap S^{p+q-1} = S^{p-1} as an explicit hypothesis, quotes Hatcher's own hint (Exercise 3,
    printed p. 176, whose hypothesis is exactly that intersection condition) to get the isomorphism
    of that inclusion, and closes (b) by factoring the inclusion through the contractible disk D^q.
    The hypothesis boundary itself is the subject of the discussion at Math StackExchange question
    4771220, which assumes S^{p-1} = h(D^p) cap S^{p+q-1}, proves (b) under it, notes that only
    S^{q-1} contained in h'(D^q) is needed of the second disk, and states that the weaker reading
    h(S^{p-1}) = S^{p-1} breaks the argument; that is an unreviewed user discussion, so it is cited
    as the source of the hypothesis analysis, not accepted as a published solution. NOT established:
    (b) for disks that meet the boundary sphere away from S^{p-1}. That case is open on this card
    and is stated as such in the proof. Part (a) is untouched.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Withdraws the framing, not the conditional proof. The previous two events presented the
    properness hypothesis as a repair of a defect in the exercise and read the tangent-arc example
    as showing that the exercise needs the hypothesis. Neither is established: no source proves
    that properness is necessary for the printed statement, and the arc example shows only that
    this particular proof needs it, since it makes the displayed inclusion undefined. The proof now
    says explicitly that step 4 is a conditional result, that it is not offered as a correction to
    Hatcher, and that whether the hypothesis can be dropped is open. Still owed, and recorded as
    owed rather than discharged: a source-backed reduction from an arbitrary embedded disk with
    boundary S^{p-1} to a proper one, or a complete published proof of the printed statement. What
    the search located: for locally flat embeddings the reduction is a consequence of the ambient
    isotopy and collar theorems in Rushing, Topological Embeddings (Chapter 1 defines proper
    embeddings and local flatness; the isotopy extension and collar theorems give the push into the
    interior), which does not cover wild embeddings; and the combinatorial linking-number formalism
    of DeTurck and Gluck, Higher dimensional linking integrals (arXiv:0802.0320), defines the
    linking number of two disjoint null-homologous cycles without any properness hypothesis, but
    presupposes a combinatorial or smooth structure, so it also does not settle the topological
    statement as printed. No complete published solution to (b) in full generality has been
    located. The card is not certified and the source obligation is not closed.
---
---

::: {.problem}
In the unit sphere $S^{p+q-1} \subset \RR^{p+q}$ let $S^{p-1}$ and $S^{q-1}$ be the subspheres consisting of points whose last $q$ and first $p$ coordinates are zero, respectively.

(a) Show that $S^{p+q-1} - S^{p-1}$ deformation retracts onto $S^{q-1}$, and is in fact homeomorphic to $S^{q-1} \times \RR^p$.

(b) Show that $S^{p-1}$ and $S^{q-1}$ are not the boundaries of any pair of disjointly embedded disks $D^p$ and $D^q$ in $D^{p+q}$.
[The preceding exercise may be useful.]
:::

::: {.solution}
Write points of $S^{p+q-1}$ as $(x,y)\in\RR^p\oplus\RR^q$. Then
$$
S^{p-1}=\{(x,0):\norm{x}=1\},
\qquad
S^{q-1}=\{(0,y):\norm{y}=1\}.
$$

::: pf

::: {.pf-step #s1}

There is a homeomorphism
$$
S^{p+q-1}-S^{p-1}\cong S^{q-1}\times\RR^p.
$$

::: pf-proof

On the complement one has $y\ne0$. Define
$$
\Phi(x,y)=\left(\frac y{\norm{y}},\frac x{\norm{y}}\right).
$$
Its inverse is
$$
\Phi^{-1}(u,v)=\frac{(v,u)}{\sqrt{1+\norm{v}^2}}.
$$
These formulas are continuous and inverse to one another.

:::

:::

::: {.pf-step #s2}

Hence $S^{p+q-1}-S^{p-1}$ deformation retracts onto the coordinate sphere $S^{q-1}$.

::: pf-proof

Under the homeomorphism in step [](#s1){.pf-ref}, contract the $\RR^p$ factor linearly to $0$. The subspace $S^{q-1}$ corresponds exactly to $S^{q-1}\times\{0\}$.

:::

:::

::: {.pf-step #s3}

Suppose, for contradiction, that there are disjoint embedded disks
$$
D^p,D^q\subset D^{p+q}
$$
with boundaries the two coordinate spheres $S^{p-1}$ and $S^{q-1}$.
Then the class
$$
[S^{q-1}]\in \widetilde H_{q-1}(S^{p+q-1}-S^{p-1})\cong\ZZ
$$
is a generator.

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref} the coordinate $S^{q-1}$ is a deformation retract of the complement, so its fundamental reduced homology class generates $\widetilde H_{q-1}$. For $q=1$ this class is the difference of the two points of $S^0$.

:::

:::

::: {.pf-step #s4}

Assume that $D^p$ meets the boundary sphere exactly in $S^{p-1}$, that is $D^p\cap S^{p+q-1}=S^{p-1}$. Under this hypothesis the inclusion
$$
S^{p+q-1}-S^{p-1}\hookrightarrow D^{p+q}-D^p
$$
is defined and induces an isomorphism on reduced homology in every degree.

::: pf-proof

The hypothesis is what makes the inclusion a map at all: a point of $S^{p+q-1}-S^{p-1}$ lies outside $S^{p-1}$, so it must not lie in $D^p$, and that is exactly the statement that $D^p\cap S^{p+q-1}=S^{p-1}$.

Given it, Exercise 3 applies to the pair $(D^p,S^{p-1})\subset(D^{p+q},S^{p+q-1})$: the pair is homeomorphic to $(D^p,S^{p-1})$, and the intersection condition $D^p\cap S^{p+q-1}=S^{p-1}$ is the hypothesis of that exercise, so the inclusion of the boundary complement into the complement of the disk is an isomorphism on homology in every degree.

This step is a conditional result, not a proof of the exercise as printed: it assumes the disk is proper, in the sense that it meets the ambient boundary exactly in its own boundary. That condition is stronger than the exercise's wording, which speaks only of disks with the given boundaries, and it is not a consequence of the boundary alone: for $p=q=1$ the arc $\gamma(t)=(t,1-t^2)$ in $D^2$ has endpoints $(\pm1,0)\in S^1$ and also meets $S^1$ at $\gamma(0)=(0,1)$, tangentially, since $\norm{\gamma(t)}^2=t^4-t^2+1\le1$ with equality only at $t=0$ and $t=\pm1$. Such a disk is not proper, and for it the inclusion displayed above is not even defined.

What that example shows is only that this proof needs the hypothesis. It does not show that the printed statement requires it, it is not offered as a correction to the exercise, and whether properness can be dropped is open on this card. The reduction from an arbitrary embedded disk with boundary $S^{p-1}$ to a proper one is not carried out here; in the locally flat case such a reduction is supplied by the ambient isotopy and collar theorems of the topological-embeddings literature (Rushing, *Topological Embeddings*, where proper embeddings and local flatness are defined in Chapter 1 and the isotopy extension theorem is stated), while wild embeddings are not covered by those theorems, and no source giving the reduction, or a proof of the printed statement without it, has been located.

Nothing is required of $D^q$ beyond $S^{q-1}\subset D^q\setminus\partial D^q$; this asymmetric requirement is the one identified in the source discussion cited in the audit record.

:::

:::

::: pf-step

But $[S^{q-1}]$ maps to zero in $\widetilde H_{q-1}(D^{p+q}-D^p)$, a contradiction.

::: pf-proof

The disk $D^q$ is disjoint from $D^p$ by assumption, so it is a singular $q$-chain in $D^{p+q}-D^p$ whose boundary is $S^{q-1}$; thus the image of the generator $[S^{q-1}]$ of step [](#s3){.pf-ref} is zero.

Equivalently, the composite
$$
S^{q-1}\longrightarrow D^q\longrightarrow D^{p+q}-D^p
$$
is the inclusion of step [](#s4){.pf-ref}, which is an isomorphism on $\widetilde H_{q-1}$ by that step, while $\widetilde H_{q-1}(D^q)=0$ because $D^q$ is contractible. An isomorphism cannot factor through a zero group, and $\widetilde H_{q-1}(S^{q-1})\cong\ZZ$ for $q\ge1$.

Either way the assumption that such disjoint disks exist is contradictory.

:::

:::

:::

Therefore, on the hypothesis of step [](#s4){.pf-ref} that the disk $D^p$ meets the boundary sphere exactly in $S^{p-1}$, the two coordinate spheres cannot bound disjoint embedded disks in $D^{p+q}$.
:::
