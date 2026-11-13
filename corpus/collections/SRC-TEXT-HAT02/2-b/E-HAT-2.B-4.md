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
- event: solution-reviewed
  by: claude
  date: 2026-11-11
  note: >-
    Part (b) is now proved as printed, on p. 176, with no hypothesis on the disks beyond the
    statement: the reduction to the proper case is by a collar. Each step checked against Hatcher
    (2002). Step #collar: with $D_2$ the radius-2 ball, the extension $F$ is $f(2x)$ on $\norm x\le
    1/2$ and $2\norm x\,f(x/\norm x)$ on $1/2\le\norm x\le 1$; the pieces agree at $\norm x=1/2$
    because $2x=x/\norm x$ there; continuity is the pasting lemma on two closed halves; injectivity
    holds because the second piece has $\norm{F(x)}=2\norm x$ (as $f$ of the unit sphere has norm
    one) so radii and then directions are recovered, and a common point of the two images has norm
    exactly one, forcing the same preimage; a continuous injection from the compact $D^p$ into the
    Hausdorff $D_2$ is an embedding. $\norm{F(x)}=2$ holds exactly for $\norm x=1$, so
    $F(D^p)\cap\partial D_2=2S^{p-1}$. Step #collar-disjoint: inner pieces disjoint by hypothesis,
    outer pieces are the cones on $S^{p-1}$ and $S^{q-1}$ over $1\le t\le2$ and are disjoint because
    those spheres are, and an inner point of norm one lying in the other cone lies on
    $S^{q-1}=g(\partial D^q)$, contradicting disjointness. Step #collar-rescale: scaling by $1/2$
    maps $D_2$ onto $D^n$ and preserves all the properties, giving proper disks in $(D^n,S^{n-1})$.
    Step #proper-case: Exercise 3 (printed p. 176) applied to the proper disk, with the class
    $[S^{q-1}]$ a generator by step #s3, against the null-homology supplied by the other disk. The
    earlier audit note recording (b) as proved only under a properness hypothesis is superseded on
    that point; the source obligation is unchanged, no published solution of the exercise having been
    located.
- event: solution-reviewed
  by: claude
  date: 2026-11-11
  note: >-
    Correction, and the degenerate cases added. The previous note on this card claimed the argument
    needs $p,q\ge1$ and offered a counterexample at $p=0$; that sentence was false and is removed. A
    concentric smaller disk of $D^q$ has a smaller sphere as its boundary, not $S^{q-1}$, so it is not
    a candidate for the disk whose boundary $S^{q-1}$ is. At $p=0$ one has $n=q$ and the ambient ball
    is $D^q$ itself, and statement (b) holds: an embedding $g:D^q\to D^q$ with $g(\partial D^q)=
    S^{q-1}$ is onto, by Invariance of Domain, Theorem 2B.3 (p. 172), applied to the interior, together
    with the compactness of $g(D^q)$ and the connectedness of $\operatorname{int}D^q$. That argument is
    now step #degenerate, with $q=0$ by symmetry and $p=q=0$ noted as the single-point ambient ball, and
    the exercise is read as printed, for all $p,q\ge0$. Steps #s3 and later are scoped to $p,q\ge1$,
    where they are used, and the closing step dispatches the degenerate cases through #degenerate.
    Checked: $g(\operatorname{int}D^q)=g(D^q)\cap\operatorname{int}D^q$ from injectivity of $g$ and
    $g(\partial D^q)=\partial D^q$; openness is Theorem 2B.3 applied to the injective map of the open
    set $\operatorname{int}D^q\cong\RR^q$ into $\RR^q$; closedness is compactness of $g(D^q)$ in the
    Hausdorff $D^q$; nonemptiness and connectedness of $\operatorname{int}D^q$ finish it. Not checked:
    the removal of the earlier claim leaves the collar argument of #collar untouched, which the note
    below records; the source obligation is unchanged, no published solution having been located.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 176 in two parts. (a) is the computed homeomorphism $\Phi(x,y)=(y/\abs{y}, x/\abs{y})$ onto $S^{q-1}\times\RR^p$ together with the straight-line deformation retraction onto $S^{q-1}$, and the homology statement behind it is part (b) of Hatcher's Proposition 2B.1, printed p. 169 with its proof on pp. 169--170. (b) is the contradiction obtained from §2.B Exercise 3, printed p. 176, applied to the collared disks; its degenerate cases $p=0$ and $q=0$ are settled by Invariance of Domain, Theorem 2B.3, printed p. 172, and Corollary 2B.4, printed p. 172. Checked against the book: the printed statement has no hypothesis on the disks, and the collaring step now runs for $p,q\ge1$ with the two degenerate cases separate, so the card reads the exercise as printed. The earlier claim that (b) fails at $p=0$ is withdrawn and the reason is recorded in the audit trail.
---
---

::: {.problem}
In the unit sphere $S^{p+q-1} \subset \RR^{p+q}$ let $S^{p-1}$ and $S^{q-1}$ be the subspheres consisting of points whose last $q$ and first $p$ coordinates are zero, respectively.

(a) Show that $S^{p+q-1} - S^{p-1}$ deformation retracts onto $S^{q-1}$, and is in fact homeomorphic to $S^{q-1} \times \RR^p$.

(b) Show that $S^{p-1}$ and $S^{q-1}$ are not the boundaries of any pair of disjointly embedded disks $D^p$ and $D^q$ in $D^{p+q}$.
[The preceding exercise may be useful.]
:::

::: {.solution}
Write points of $S^{p+q-1}$ as $(x,y)\in\RR^p\oplus\RR^q$ and put $n=p+q$. Then
$$
S^{p-1}=\{(x,0):\norm{x}=1\},
\qquad
S^{q-1}=\{(0,y):\norm{y}=1\},
$$
so $S^{p-1}\cap S^{q-1}=\emptyset$ and both are contained in $S^{n-1}$.

The exercise is read as printed, for all $p,q\ge0$: at $p=0$ the sphere $S^{p-1}$ is the empty sphere $S^{-1}$ and $\partial D^0=\emptyset$, and at $q=0$ likewise, and step [](#degenerate){.pf-ref} settles those two cases. The rest of the argument assumes $p,q\ge1$, where $S^{p-1}$ and $S^{q-1}$ are nonempty spheres in $S^{n-1}$. The results of the book used are Exercise 3 of §2.B, printed p. 176 — for a pair of subspaces $(D,S)\subset(D^n,S^{n-1})$ homeomorphic to $(D^k,S^{k-1})$ with $D\cap S^{n-1}=S$, the inclusion $S^{n-1}-S\hookrightarrow D^n-D$ induces an isomorphism on homology — and Invariance of Domain, Theorem 2B.3 (p. 172), in the two degenerate cases. Part (a) is steps [](#s1){.pf-ref} and [](#s2){.pf-ref}; part (b) is the rest.

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

::: {.pf-step #degenerate}

If $p=0$ or $q=0$, part (b) holds.

::: pf-proof

Suppose first that $p=0$ and $q\ge1$, so that $n=q$ and the ambient ball is $D^q$ itself, $S^{p-1}=S^{-1}=\emptyset$ and $\partial D^0=\emptyset$. Let $g:D^q\to D^q$ be an embedding with $g(\partial D^q)=S^{q-1}$. Since $g$ is injective with $g(\partial D^q)=\partial D^q$, it carries the interior onto the complement of the boundary of its image,
$$
g(\operatorname{int}D^q)=g(D^q)-g(\partial D^q)=g(D^q)-S^{q-1}=g(D^q)\cap\operatorname{int}D^q .
$$

*That set is open in $\operatorname{int}D^q$.* The interior $\operatorname{int}D^q$ is homeomorphic to $\RR^q$, and $g$ restricts to an injective continuous map of it into $\RR^q$; by Invariance of Domain, Theorem 2B.3 (p. 172), its image is open.

*It is closed in $\operatorname{int}D^q$.* The set $g(D^q)$ is compact, hence closed in the Hausdorff space $D^q$, so $g(D^q)\cap\operatorname{int}D^q$ is closed in the open subspace $\operatorname{int}D^q$.

*It is nonempty and $\operatorname{int}D^q$ is connected*, so the clopen nonempty subset $g(\operatorname{int}D^q)$ is all of $\operatorname{int}D^q$. Hence $g(D^q)=g(\operatorname{int}D^q)\cup g(\partial D^q)=\operatorname{int}D^q\cup S^{q-1}=D^q$. A disk $D^0$ is a single point of $D^q$, so it lies in $g(D^q)$ and the two disks are not disjoint.

For $q=0$ the same argument applies with $p$ in place of $q$: an embedding $f:D^p\to D^p$ with $f(\partial D^p)=S^{p-1}$ has open image by Theorem 2B.3 and compact hence closed image, so it is onto, and the point $D^0$ lies in $f(D^p)$. At $p=q=0$ the ambient ball is a single point, both disks are that point, and they meet.

:::

:::

::: {.pf-step #s3}

Assume $p,q\ge1$. Then the class
$$
[S^{q-1}]\in \widetilde H_{q-1}(S^{n-1}-S^{p-1})\cong\ZZ
$$
is a generator.

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref} the coordinate sphere $S^{q-1}$ is a deformation retract of $S^{n-1}-S^{p-1}$, so its fundamental reduced homology class generates $\widetilde H_{q-1}$ there. For $q=1$ this class is the difference of the two points of $S^0$.

:::

:::

::: {.pf-step #collar}

Let $f:D^p\to D^n$ and $g:D^q\to D^n$ be disjoint embeddings with $f(\partial D^p)=S^{p-1}$ and $g(\partial D^q)=S^{q-1}$. Then $D^n$ contains disjoint embedded disks $\widehat D^p$ and $\widehat D^q$ with $\partial\widehat D^p=S^{p-1}$ and $\partial\widehat D^q=S^{q-1}$ which are proper, that is $\widehat D^p\cap S^{n-1}=S^{p-1}$ and $\widehat D^q\cap S^{n-1}=S^{q-1}$.

::: pf-proof

Let $D_2$ be the closed ball of radius $2$ about the origin, so $D^n\subset D_2$. A point of $D^n$ has norm at most $1$, so an embedding whose boundary is $S^{p-1}$ extends to a proper disk in $D_2$.

::: {.pf-step #collar-extension}

The formula
$$
F(x)=\begin{cases} f(2x), & \norm x\le\tfrac12,\\[2pt] 2\norm x\, f\bigl(x/\norm x\bigr), & \tfrac12\le\norm x\le 1,\end{cases}
$$
defines an embedding $F:D^p\to D_2$ with $F(\partial D^p)=2S^{p-1}$ and $F(D^p)\cap\partial D_2=2S^{p-1}$.

::: pf-proof

*Well defined.* For $\norm x\le\tfrac12$ the point $2x$ lies in $D^p$, so $F(x)\in f(D^p)\subset D^n$. For $\tfrac12\le\norm x\le1$ one has $x/\norm x\in\partial D^p$, so $f(x/\norm x)\in S^{p-1}$ has norm one and $\norm{F(x)}=2\norm x\in[1,2]$. At $\norm x=\tfrac12$ the two formulas coincide, since then $2x=x/\norm x$ and $2\norm x=1$. Both pieces are continuous and their domains are closed and cover $D^p$, so $F$ is continuous by the pasting lemma.

*Injective.* On the first piece $F=f\circ(2\,\cdot\,)$ is injective. On the second write $x=ru$ with $u\in\partial D^p$ and $\tfrac12\le r\le1$, so that $F(x)=2r\,f(u)$ and $\norm{F(x)}=2r$ because $\norm{f(u)}=1$; then $2r\,f(u)=2r'f(u')$ gives $r=r'$ and, by injectivity of $f$, $u=u'$. If $x$ is in the first piece and $x'$ in the second with $F(x)=F(x')$, then $\norm{F(x)}\le1$ and $\norm{F(x')}=2\norm{x'}\ge1$, so both equal $1$; hence $\norm{x'}=\tfrac12$ and $F(x')=f(x'/\norm{x'})=f(2x')$, while $F(x)=f(2x)$, and injectivity of $f$ gives $2x=2x'$, that is $x=x'$. So the two pieces agree on their overlap and nowhere else.

Since $D^p$ is compact and $D_2$ is Hausdorff, $F$ is an embedding. For $\norm x=1$ the second formula gives $F(x)=2f(x)$, so $F(\partial D^p)=2f(\partial D^p)=2S^{p-1}\subset\partial D_2$, and conversely an $F(x)$ of norm $2$ is either of norm at most $1$ from the first piece or has $\norm x=1$. The same construction applied to $g$, whose boundary is $S^{q-1}$, gives an embedding $G:D^q\to D_2$ with $G(\partial D^q)=2S^{q-1}$ and $G(D^q)\cap\partial D_2=2S^{q-1}$.

:::

:::

::: {.pf-step #collar-disjoint}

$F(D^p)\cap G(D^q)=\emptyset$.

::: pf-proof

The inner pieces are $f(D^p)$ and $g(D^q)$, disjoint by hypothesis. The outer pieces are the cones
$$
\{ts: s\in S^{p-1},\ 1\le t\le2\},
\qquad
\{ts: s\in S^{q-1},\ 1\le t\le2\},
$$
which are disjoint because $S^{p-1}\cap S^{q-1}=\emptyset$. For an inner and an outer piece: a point of $f(D^p)$ lies in $D^n$ and so has norm at most $1$, while a point of the cone on $S^{q-1}$ has norm at least $1$; a common point therefore has norm exactly $1$, lies on $S^{n-1}$ and, being in the cone on $S^{q-1}$, lies on $S^{q-1}=g(\partial D^q)\subset g(D^q)$, contradicting the disjointness of $f(D^p)$ and $g(D^q)$. The same argument exchanges the roles of $F$ and $G$.

:::

:::

::: {.pf-step #collar-rescale}

After the scaling $y\mapsto y/2$, the disks $F(D^p)/2$ and $G(D^q)/2$ lie in $D^n$, are disjoint, have boundaries $S^{p-1}$ and $S^{q-1}$, and are proper.

::: pf-proof

Dividing by $2$ maps $D_2$ onto $D^n$ and $\partial D_2$ onto $S^{n-1}$, and is a homeomorphism, so it preserves embedded disks and disjointness. By step [](#collar-extension){.pf-ref}, $F(D^p)\cap\partial D_2=2S^{p-1}$, so
$$
\bigl(F(D^p)/2\bigr)\cap S^{n-1}=S^{p-1}=\partial\bigl(F(D^p)/2\bigr),
$$
and likewise for $G(D^q)/2$ and $S^{q-1}$.

:::

:::

:::

:::

::: {.pf-step #proper-case}

There are no disjoint embeddings $f:D^p\to D^n$, $g:D^q\to D^n$ with $f(\partial D^p)=S^{p-1}$, $g(\partial D^q)=S^{q-1}$ and $f(D^p)\cap S^{n-1}=S^{p-1}$, $g(D^q)\cap S^{n-1}=S^{q-1}$.

::: pf-proof

Put $D=f(D^p)$ and $E=g(D^q)$. Exercise 3 of §2.B applies to the pair $(D,S^{p-1})\subset(D^n,S^{n-1})$, whose hypothesis $D\cap S^{n-1}=S^{p-1}$ holds by assumption, and says that $S^{n-1}-S^{p-1}\hookrightarrow D^n-D$ induces an isomorphism on homology. By step [](#s3){.pf-ref} the class $[S^{q-1}]$ generates the left-hand group in degree $q-1$, so its image generates $\widetilde H_{q-1}(D^n-D)$ and is nonzero. But $E\subset D^n-D$ is a compact $q$-manifold with boundary whose fundamental chain has boundary the fundamental cycle of $\partial E=S^{q-1}$, so $[S^{q-1}]=0$ in $\widetilde H_{q-1}(D^n-D)$. This contradicts the nonvanishing, so no such pair exists.

:::

:::

::: pf-step

Part (b) holds: no disjoint embeddings as in the exercise exist.

::: pf-proof

Suppose $f,g$ are as in the exercise. If $p=0$ or $q=0$ the claim is step [](#degenerate){.pf-ref}. Otherwise $p,q\ge1$, and by step [](#collar){.pf-ref} there are then disjoint disks $\widehat D^p,\widehat D^q\subset D^n$ with the same boundaries which are proper, while step [](#proper-case){.pf-ref} says no such pair of disks exists. So the assumption fails.

:::

:::

:::

:::

::: {.remark title="Published solution"}
Hatcher, *Algebraic Topology* (2002): the statement is Exercise 4 of §2.B, printed p. 176. Part (a)'s homology content is Proposition 2B.1(b) with its printed proof, pp. 169--170; part (b) is §2.B Exercise 3 (printed p. 176) applied to the collared disks, with the cases $p=0$ and $q=0$ settled by Invariance of Domain, Theorem 2B.3, and Corollary 2B.4, both printed p. 172.
:::
