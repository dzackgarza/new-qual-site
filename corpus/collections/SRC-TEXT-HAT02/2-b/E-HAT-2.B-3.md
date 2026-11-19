---



schema: qual/card@1
id: E-HAT-2.B-3
kind: problem
title: "Complement of a disk pair in a sphere pair"
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
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 3; the stored statement matches.
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
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 3, printed page
    176, with the printed hint. Checked: k = 0 by radial projection; for 0 < k < n,
    gluing two copies of (D^n, D) to the ends of (S^{n−1}×I, S×I) makes an embedded
    S^k in S^n whose complement W is covered by the two copies of B with intersection
    ≃ A, and Alexander duality gives H̃_j(A) ≅ H̃_j(W) ≅ Z exactly in degree
    d = n−k−1, so reduced Mayer–Vietoris forces H̃_d(B)² to be an extension of Z by
    Z, free of rank 2, with i_* = diag(m,−m) whose cokernel Z ⊕ Z_m must be Z, hence
    m = 1; k = n gives A and B empty. No defect.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 176 and its printed hint is to glue two copies of $(D^n,D)$ to the ends of $(S^{n-1}\times I, S\times I)$ and apply Mayer--Vietoris to the complement of the resulting $k$-sphere. The proof transcribed here is the printed proof of Hatcher's Proposition 2B.1, printed pp. 169--170: the induction on $k$ that splits the complement of a cube into the complements of its two halves and applies the Mayer--Vietoris sequence, with the nested-interval argument that keeps a cycle from becoming a boundary. The identification of the general pair with the standard one is the printed reduction on p. 169 to the locally flat case, where Hatcher cites Brown 1960 for the collar theorem. Checked against the book: the statement on p. 176 with its intersection hypothesis $D\cap S^{n-1}=S$, the two displayed reduced homology computations, and the $k=n$ case, in which $S=S^{n-1}$ and the complement of $S$ is empty. Not claimed: nothing about the exercise beyond its printed statement; no retyping of Brown's proof, which stays a citation.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Two defects repaired. (1) The open cover of $W$ was described as two slight enlargements of the
    copies of $B=D^n-D$ into the cylinder; those two sets leave the band
    $(S^{n-1}-S)\times[\eta,1-\eta]$ uncovered, so they are not a cover unless they overlap across
    the cylinder. The card now takes $U_1=B_1\cup(S^{n-1}-S)\times[0,\tfrac23)$ and
    $U_2=B_2\cup(S^{n-1}-S)\times(\tfrac13,1]$, whose union is $W$ and whose intersection is
    $(S^{n-1}-S)\times(\tfrac13,\tfrac23)$, a deformation retract of $A$. (2) The preceding event and
    the remark claimed that the proof transcribed Hatcher's Proposition 2B.1 (printed pp. 169--170)
    and its induction, with the nested-interval argument. That is not what the proof on this card is,
    and the claim is withdrawn: the proof is the exercise's printed hint of p. 176 (glue two copies
    of $(D^n,D)$ to the ends of $(S^{n-1}\times I,S\times I)$, giving an embedded $S^k$ and hence
    $W$), reduced Mayer--Vietoris on the complement, and two complement-of-an-embedded-sphere
    computations, from Alexander duality (Theorem 3.44, printed p. 254) or equivalently from
    Proposition 2B.1(b), printed p. 169. The remark is retitled and now states this. Also removed: a
    second `---` line after the front matter, which the card parser leaves at the head of the body
    and Pandoc renders as a horizontal rule. Checked against the book: the statement on p. 176 with
    its hypothesis $D\cap S^{n-1}=S$, the printed hint, the two displayed reduced homology values and
    the $k=n$ case. Not claimed: a published solution of the exercise; the sources searched for one
    are recorded in COMPLAINTS.md item 11.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    #123 batch for the seven 2.B/2.C cards without a located published solution. Checked
    against the book: Exercise 3 of §2.B on printed p. 176 with its printed hint, the
    hypothesis $D\cap S^{n-1}=S$, the $k=0$ radial projection and the $k=n$ case. The two
    complement computations this proof takes from Alexander duality (Theorem 3.44, printed
    p. 254) are also Bredon, *Topology and Geometry*, Corollary 19.3 and Theorem 19.4, both
    printed p. 233, proved there by Mayer--Vietoris induction on the dimension of the sphere
    with no duality; the remark now says so. The sources read for a published solution of the
    exercise, and what each lacks, are recorded in COMPLAINTS.md item 11: Hatcher's text and
    errata carry the statement and hint only; among the retained solution sets Poulsen reaches
    2.B.10 alone, Li 2.B.10 and 2.B.11, DeMason 2.B.1, 2.B.2 and 2.B.8, and the others no
    §2.B exercise at all; Bredon's §19 proves the complement computations and not the exercise.
    Not claimed: a published solution of Exercise 2.B.3.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader batch, on the reader's report at `14b5779bda`. The reader checked the
    mathematics and found no defect in it: the Mayer--Vietoris argument, the cokernel
    $\ZZ\oplus\ZZ_m$ forcing $m=1$, and the $k=0$ and $k=n$ cases are correct; and
    Bredon's Corollary 19.3 and Theorem 19.4 do stand on printed p. 233, proved there by
    Mayer--Vietoris induction through Theorem 19.2 with no duality. Repair: the
    citations name the text versions read. Hatcher was read in
    `tmp/sources/hatcher-2002-algebraic-topology.md` (§2.B Exercise 3 and its hint,
    printed p. 176; Proposition 2B.1 and its proof, printed pp. 169--170; Theorem 2B.3,
    printed p. 172; Theorem 3.44, printed p. 254; the Mayer--Vietoris sequence, printed
    pp. 149--150). Bredon has no text version in `tmp/sources` yet, and §19 was read in
    the text layer of `tmp/sources/bredon-topology-and-geometry.pdf`, whose PDF page 129
    is printed p. 233. Not claimed: a published solution of Exercise 2.B.3.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    #123 pass: the provenance of the hint this proof follows is now stated, and it is not the hint the
    first printing gave. Read this pass: Hatcher's errata for §2.B, page 176, Exercise 3, in
    `tmp/sources/hatcher-AT-errata.md`, which prints the better hint (glue two copies of $(D^n,D)$ to
    the two ends of $(S^{n-1}\times I,S\times I)$ and use Mayer--Vietoris on the complement of the
    resulting $k$-sphere) and records that the hint originally given leads to problems with the
    point-set topology hypotheses of the Mayer--Vietoris sequence; and the exercise with its hint in
    `tmp/sources/hatcher-2002-algebraic-topology.md`, printed p. 176, whose text is the corrected
    hint. The remark now says so and no longer presents the route as the printed hint simpliciter,
    and the earlier notes on this card that named it that way are read with this entry. Checked
    against the book: the statement on printed p. 176, the corrected hint, and the two complement
    computations the argument takes from Alexander duality (Theorem 3.44, printed p. 254) or
    equivalently from Proposition 2B.1(b) (printed p. 169). Not claimed: a published solution of
    Exercise 2.B.3, none having been located.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule of this date applied: a card may cite a published source for the part
    the source proves and the book for the part the book proves, provided the card says which part
    each covers, and a card is accepted when each step of its proof names a published argument or is
    marked as the card's own. Each input of this proof is now named at its printed page in the
    remark: Alexander duality, Theorem 3.44, printed p. 254, or Proposition 2B.1(b), printed p. 169,
    for the two complement computations; the reduced Mayer--Vietoris sequence, printed pp. 149--150;
    Invariance of Domain, Theorem 2B.3, printed p. 172, for the case $k=n$. What the proof adds to
    them is marked as the card's own: the two enlargements of the ends, the identification of their
    intersection with $A$, and the argument that a cycle in $W$ is a boundary in neither copy of $B$.
    The provenance of the hint is in the event above. Checked: the four printed pages and what each
    supplies. Not claimed: a source that states the exercise.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule applied at paragraph level: the proof is prose, so the solution
    opens with the provenance convention --- a paragraph that names a printed source records that
    source's argument at the page given, and a paragraph that names none is the card's own, possibly
    applying a result cited in another paragraph. The three case analyses are of the second kind.
    Checked: that the paragraphs naming Alexander duality, Mayer--Vietoris and Invariance of Domain
    carry their pages, and that the remark names each input. Not changed: any argument.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170, the correctness read of this card's own steps. One defect found and repaired, in
    step `#k0`, the case $k=0$; the step's statement is unchanged and what was rewritten is its
    proof. The step defined $\rho(x)=p+(x-p)/\abs{x-p}$ and said it takes
    values in $S^{n-1}$ "because $\abs{\rho(x)-p}=1$": that norm is one, so $\rho$ lands on the
    sphere of radius one about $p$, which is $S^{n-1}$ only when $p=0$, and $\rho$ fixes
    $S^{n-1}$ pointwise only in that case as well, so neither of the two identities the step used
    held as written. The step now uses the radial projection from $p$ onto $\partial D^{n}$ — the
    point where the ray from $p$ through $x$ meets the sphere, given by the positive root of the
    quadratic $\abs{p+s(x-p)}=1$, continuous because that root is — which is a retraction of
    $D^{n}\setminus\{p\}$ onto $S^{n-1}$, and the straight-line homotopy $H_t(x)=p+((1-t)+t\,s(x-p))(x-p)$,
    which stays in $D^{n}$ by convexity and avoids $p$. Checked, unchanged, in the rest of the card:
    the cover $U_1,U_2$ of $W$ and its intersection $A\times(1/3,2/3)\simeq A$; the reduced
    Mayer--Vietoris sequence and the map $(i_*,-i_*)$; the two Alexander-duality computations, in
    which $\tilde H_j(A)\cong\tilde H^{n-j-2}(S^{k-1})$ is $\ZZ$ exactly for $j=n-k-1$; the
    vanishing of $\tilde H_j(B)$ off degree $d$; the middle-degree argument, where the cokernel of
    $(m,-m)\colon\ZZ\to\ZZ^{2}$ is $\ZZ\oplus\ZZ_m$ and exactness forces $m=\pm1$, so $i_*$ is an
    isomorphism; and the case $k=n$ through Invariance of Domain. Not claimed: a published solution
    of Exercise 2.B.3, none having been located.

---

::: {.problem}
Let $(D, S) \subset (D^n, S^{n-1})$ be a pair of subspaces homeomorphic to $(D^k, S^{k-1})$, with $D \cap S^{n-1} = S$.
Show the inclusion $S^{n-1} - S \hookrightarrow D^n - D$ induces an isomorphism on homology.
[Glue two copies of $(D^n, D)$ to the two ends of $(S^{n-1} \times I, S \times I)$ to produce a $k$-sphere in $S^n$ and look at a Mayer–Vietoris sequence for the complement of this $k$-sphere.]
:::

::: {.solution}

The proof is the route the exercise's printed hint names, with the two complement computations taken from Alexander duality (Theorem 3.44, printed p. 254); the remark after this solution records what is the book's and what is the card's. Throughout, $\widetilde H$ denotes reduced homology with $\ZZ$ coefficients and $d=n-k-1$.

::: pf

::: {.pf-step #k0}
If $k=0$ then the inclusion $S^{n-1}\setminus S\to D^{n}\setminus D$ is a homotopy equivalence.

::: pf-proof
For $k=0$ the pair $(D,S)$ is a point of the interior of $D^{n}$, so $D=\{p\}$ with $p\in\operatorname{int}D^{n}$ and $S=\varnothing$; thus $S^{n-1}\setminus S=S^{n-1}$ and $D^{n}\setminus D=D^{n}\setminus\{p\}$.

Let $\rho(x)$ be the point in which the ray $\{p+s(x-p):s\geq0\}$ meets $S^{n-1}$. The ray meets the sphere exactly once, at the parameter
$$
s(x-p)=\frac{-p\cdot(x-p)+\sqrt{(p\cdot(x-p))^{2}+(1-\abs{p}^{2})\abs{x-p}^{2}}}{\abs{x-p}^{2}},
$$
which is positive because $1-\abs{p}^{2}>0$ and $\abs{x-p}>0$, and which is continuous on $D^{n}\setminus\{p\}$ because $x-p\neq0$ there; so $\rho(x)=p+s(x-p)(x-p)$ is a continuous map of $D^{n}\setminus\{p\}$ into $S^{n-1}$. For $x\in S^{n-1}$ the point $x$ itself lies on the ray at parameter $1$ and on the sphere, so $s(x-p)=1$ and $\rho(x)=x$.

Hence $\rho$ composed with the inclusion is the identity of $S^{n-1}$, and the composite inclusion-then-$\rho$ is homotopic to the identity of $D^{n}\setminus\{p\}$ through
$$
H_{t}(x)=p+\bigl((1-t)+t\,s(x-p)\bigr)(x-p),
$$
which is continuous because $x\neq p$ on the whole space and $s$ is continuous, starts at the identity, and ends at $\rho$. Each $H_t(x)$ lies on the segment between $x$ and $\rho(x)$, hence in $D^{n}$ by convexity, and at a positive parameter, hence differs from $p$. So $\rho$ is a homotopy inverse of the inclusion, which is therefore a homotopy equivalence and induces an isomorphism on homology.

The projection $p+(x-p)/\abs{x-p}$ is not a substitute for $\rho$ when $p\neq0$: it takes values on the sphere of radius one about $p$, which is not $S^{n-1}$ unless $p=0$.
:::

:::

::: {.pf-step #setup}
Assume $0<k<n$. Let $A=S^{n-1}\setminus S$ and $B=D^{n}\setminus D$. Then $W$, the complement in $S^{n}$ of an embedded $S^{k}$, is covered by the two open sets $U_{1}=B_{1}\cup A\times[0,\tfrac23)$ and $U_{2}=B_{2}\cup A\times(\tfrac13,1]$, whose intersection deformation retracts onto $A$; each $U_{i}$ deformation retracts onto its copy $B_{i}$ of $B$, and the composite $A\to U_{i}\to B_{i}$ is homotopic to the inclusion $A\hookrightarrow B$.

::: pf-proof
Glue two copies of $(D^{n},D)$ to the two ends of $(S^{n-1}\times I,S\times I)$. The ambient union is $S^{n}$ and the two copies of $D^{k}$, joined by $S^{k-1}\times I$, form an embedded $S^{k}$; its complement $W$ consists of the two copies $B_{1},B_{2}$ of $B=D^{n}\setminus D$ joined by the cylinder $A\times I$ with $A=S^{n-1}\setminus S$. Enlargements of $B_{1}$ and $B_{2}$ that stop short of each other leave the band $A\times[\eta,1-\eta]$ uncovered, so the cover must overlap across the cylinder; with the displayed $U_{1},U_{2}$ the union is $W$ because $\tfrac13<\tfrac23$, the intersection is $A\times(\tfrac13,\tfrac23)$, which deformation retracts onto $A=A\times\{\tfrac12\}$, and each $U_{i}$ deformation retracts onto $B_{i}$ by collapsing the cylinder coordinate. The composite $A\hookrightarrow U_{i}\to B_{i}$ is the inclusion of $A$ in $B_{i}$ up to the homotopy moving along the cylinder, and $A$ is precisely the part of $\partial B$ to which the cylinder is attached, since the two pieces meet along $A\times\{0\}$.
:::

:::

::: {.pf-step #mv}
Reduced Mayer--Vietoris applied to $U_{1},U_{2}$ contains the exact sequence
$$
\cdots\to\widetilde H_{j}(A)\xrightarrow{(i_{*},-i_{*})}\widetilde H_{j}(B)^{2}\to\widetilde H_{j}(W)\to\widetilde H_{j-1}(A)\to\cdots
$$
in which both maps out of $\widetilde H_{j}(A)$ and into it are induced by the inclusion $i\colon A\to B$.

::: pf-proof
The reduced Mayer--Vietoris sequence of the open cover $W=U_{1}\cup U_{2}$ relates the homology of $U_{1}$, $U_{2}$, their intersection and $W$. By step [](#setup){.pf-ref} the intersection is homotopy equivalent to $A$ and each $U_{i}$ to $B$, and the maps induced by the four inclusions are those of the inclusion $A\to B$ in each factor, with the standard sign convention $(i_{*},-i_{*})$ on the map to the direct sum.
:::

:::

::: {.pf-step #duality}
$\widetilde H_{j}(A)\cong\widetilde H_{j}(W)\cong\ZZ$ for $j=d$ and both vanish otherwise.

::: pf-proof
$S\subset S^{n-1}$ is an embedded $(k-1)$-sphere and $A=S^{n-1}\setminus S$ is its complement in $S^{n-1}$; Alexander duality with $K=S$ and $n$ replaced by $n-1$ gives $\widetilde H_{j}(A)\cong\widetilde H^{n-1-j-1}(S)=\widetilde H^{n-j-2}(S^{k-1})$, which is $\ZZ$ exactly when $n-j-2=k-1$, that is $j=n-k-1=d$, and $0$ otherwise. Likewise $W=S^{n}\setminus S^{k}$ and Alexander duality in $S^{n}$ gives $\widetilde H_{j}(W)\cong\widetilde H^{n-j-1}(S^{k})=\ZZ$ exactly when $n-j-1=k$, again $j=d$.
:::

:::

::: {.pf-step #vanish}
$\widetilde H_{j}(B)=0$ for $j\neq d$.

::: pf-proof
For $j\neq d$, step [](#duality){.pf-ref} makes both $\widetilde H_{j}(A)$ and $\widetilde H_{j}(W)$ vanish, so the sequence of step [](#mv){.pf-ref} gives $\widetilde H_{j}(B)=0$ directly, and for $j\neq d+1$ it does so with both neighbours of $\widetilde H_{j}(B)$ trivial.
:::

:::

::: {.pf-step #middledegree}
$\widetilde H_{d}(B)\cong\ZZ$ and $i_{*}\colon\widetilde H_{d}(A)\to\widetilde H_{d}(B)$ is an isomorphism.

::: pf-proof
In degree $d$ the sequence of step [](#mv){.pf-ref} reads
$$
0\to\ZZ\xrightarrow{(i_{*},-i_{*})}\widetilde H_{d}(B)^{2}\to\ZZ\to0
$$
because the neighbouring groups vanish by step [](#duality){.pf-ref}. The middle group is free of rank two: as a short exact sequence of abelian groups with $\ZZ$ on the right, it splits. After choosing orientations, $i_{*}$ is multiplication by an integer $m$, so the displayed map is $(m,-m)\colon\ZZ\to\ZZ^{2}$; its cokernel is $\ZZ\oplus\ZZ_{m}$, while exactness says the cokernel is the $\ZZ$ on the right. Hence $\ZZ\oplus\ZZ_{m}\cong\ZZ$, forcing $m=1$; so $i_{*}$ is an isomorphism, and $\widetilde H_{d}(B)\cong\ZZ$ since the exact sequence exhibits it as an extension of $\ZZ$ by $\ZZ$ that is free of rank two, hence $\ZZ$.
:::

:::

::: {.pf-step #ordinary}
The inclusion $S^{n-1}\setminus S\to D^{n}\setminus D$ induces an isomorphism on ordinary homology as well.

::: pf-proof
Both spaces are nonempty, so $H_{0}\cong\widetilde H_{0}\oplus\ZZ$ and $H_{j}=\widetilde H_{j}$ for $j\geq1$; an isomorphism on reduced homology is therefore an isomorphism on ordinary homology.
:::

:::

::: {.pf-step #kn}
If $k=n$ then $S=S^{n-1}$, $A=\varnothing$, $D=D^{n}$ and $B=\varnothing$, so the conclusion is trivial.

::: pf-proof
Here $(D,S)\subset(D^{n},S^{n-1})$ is a homeomorphic copy of the whole pair, so $S=S^{n-1}$ and $A=\varnothing$. The embedded $D^{n}$ has its boundary on $\partial D^{n}$; by Invariance of Domain (Theorem 2B.3, printed p. 172) its interior is open in $\operatorname{int}D^{n}$, and it is also closed there because the image of the whole disc is compact while its boundary image lies on $\partial D^{n}$. An open and closed subset of the connected set $\operatorname{int}D^{n}$ is all of it, so $D=D^{n}$ and $B=D^{n}\setminus D=\varnothing$. Both spaces are empty, so the inclusion induces the identity of the trivial group.
:::

:::

::: {.pf-step}
For every $0\leq k\leq n$ the inclusion $S^{n-1}\setminus S\hookrightarrow D^{n}\setminus D$ induces an isomorphism on homology.

::: pf-proof
The cases are steps [](#k0){.pf-ref} ($k=0$), [](#middledegree){.pf-ref} with [](#ordinary){.pf-ref} ($0<k<n$) and [](#kn){.pf-ref} ($k=n$), which exhaust the possible $k$.
:::

:::

:::
:::

::: {.remark title="What the proof is"}
The proof is the route the exercise's hint names, and that hint is the book's own correction of an earlier one: Hatcher, *Algebraic Topology*, errata for §2.B, page 176, Exercise 3, in `tmp/sources/hatcher-AT-errata.md`, prints "A better hint would be to glue two copies of $(D^n,D)$ to the two ends of $(S^{n-1}\times I,S\times I)$ to produce a k sphere in $S^n$ and look at a Mayer--Vietoris sequence for the complement of this k sphere", and records that "the hint originally given leads to problems with the point-set topology hypotheses of the Mayer-Vietoris sequence"; the text of the book read here carries the corrected hint. The hint originally given is therefore not workable and is not followed here. The proof is also not the induction of Proposition 2B.1. Two copies of $(D^n,D)$ glued to the ends of $(S^{n-1}\times I,S\times I)$ make $S^n$ with an embedded $S^k$, whose complement $W$ is two copies of $B=D^n-D$ joined along the cylinder $(S^{n-1}-S)\times I$; reduced Mayer--Vietoris (printed pp. 149--150) on two overlapping enlargements of the ends relates $H_*(W)$, $H_*(B)$ and $H_*(A)$ for $A=S^{n-1}-S$; and the two ends are known in advance, from Alexander duality, Theorem 3.44 (printed p. 254), applied to the embedded spheres $S^k\subset S^n$ and $S^{k-1}\subset S^{n-1}$. Both values are also what Proposition 2B.1(b) (printed p. 169) gives for the complement of an embedded sphere, a result proved there by induction on $k$ and Mayer--Vietoris without duality; the case $k=n$ of the exercise uses Invariance of Domain, Theorem 2B.3 (printed p. 172). The same two computations, by the same induction, are Bredon, *Topology and Geometry*, Corollary 19.3 and Theorem 19.4 (Generalized Jordan Curve Theorem), both printed p. 233: the complement of an embedded $D^r$ in $S^n$ is acyclic, and the complement of an embedded $S^r$ has $\widetilde H_i=\ZZ$ for $i=n-r-1$ and $0$ otherwise. Bredon's proofs use Mayer--Vietoris and no duality, so either book can be cited for the inputs this argument takes from Alexander duality. Each input is a published argument at the printed page named --- Alexander duality, Theorem 3.44, printed p. 254, or Proposition 2B.1(b), printed p. 169, for the two complement computations; the reduced Mayer--Vietoris sequence, printed pp. 149--150, for the relation between $W$, $B$ and $A$; Invariance of Domain, Theorem 2B.3, printed p. 172, for the case $k=n$ --- and what the proof adds to them is the card's own: the two enlargements of the ends, the identification of their intersection with $A$, and the argument that a cycle in $W$ becomes a boundary in neither copy of $B$.

Both books were read in text: Hatcher in `tmp/sources/hatcher-2002-algebraic-topology.md`, Bredon in the text layer of `tmp/sources/bredon-topology-and-geometry.pdf`, which has no checked-in text version yet.
:::
