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
---

::: {.problem}
Let $(D, S) \subset (D^n, S^{n-1})$ be a pair of subspaces homeomorphic to $(D^k, S^{k-1})$, with $D \cap S^{n-1} = S$.
Show the inclusion $S^{n-1} - S \hookrightarrow D^n - D$ induces an isomorphism on homology.
[Glue two copies of $(D^n, D)$ to the two ends of $(S^{n-1} \times I, S \times I)$ to produce a $k$-sphere in $S^n$ and look at a Mayer–Vietoris sequence for the complement of this $k$-sphere.]
:::

::: {.solution}
The two results the argument uses are the Mayer--Vietoris sequence of §2.2, printed pp. 149--150 (Hatcher leaves it unnumbered; the reduced form is the display on p. 150), and Alexander duality, Theorem 3.44 (p. 254), applied with $K$ a sphere: for a compact locally contractible $K\subset S^n$ it gives $\widetilde H_j(S^n-K)\cong\widetilde H^{n-j-1}(K)$, and here $K$ is $S\subset S^{n-1}$, a sphere of dimension $k-1$, or $S^k\subset S^n$. The case $k=n$ also uses Invariance of Domain, Theorem 2B.3 (p. 172).

If $k=0<n$, then $D$ is one interior point of $D^n$, and radial projection from that point retracts $D^n\setminus D$ onto $S^{n-1}$. Hence the inclusion induces an isomorphism.

Now suppose $0<k<n$ and put $d=n-k-1\ge0$. Write
$$
A=S^{n-1}\setminus S,\qquad B=D^n\setminus D.
$$
Glue two copies of $(D^n,D)$ to the ends of $(S^{n-1}\times I,S\times I)$. Their ambient union is $S^n$, and the two copies of $D^k$, joined by $S^{k-1}\times I$, form an embedded $S^k$. Let $W$ be its complement. In $W$ the two ends $B_1,B_2$, each a copy of $B$, are joined by the cylinder $A\times I$, and the two open sets that cover $W$ have to overlap across that cylinder: enlargements of $B_1$ and $B_2$ that stop short of each other leave the band $A\times[\eta,1-\eta]$ uncovered. Take instead
$$
U_1=B_1\cup A\times[0,\tfrac23),\qquad U_2=B_2\cup A\times(\tfrac13,1],
$$
open in $W$. Then $U_1\cup U_2=W$, because $\tfrac13<\tfrac23$, and $U_1\cap U_2=A\times(\tfrac13,\tfrac23)$ deformation retracts onto $A=A\times\{\tfrac12\}$. Each $U_i$ deformation retracts onto its copy $B_i$, and the composite $A\hookrightarrow U_i\to B_i$ is homotopic to the inclusion $A=S^{n-1}-S\hookrightarrow D^n-D=B$, because $A$ is the part of $\partial B$ to which the cylinder is attached and the two sets meet along $A\times\{0\}$. So both inclusions induce the map $i_*$ of the statement, and the sign in the Mayer--Vietoris map below is the standard one. Reduced Mayer--Vietoris therefore contains
$$
\cdots\longrightarrow\widetilde H_j(A)
\xrightarrow{(i_*,-i_*)}\widetilde H_j(B)^2
\longrightarrow\widetilde H_j(W)
\longrightarrow\widetilde H_{j-1}(A)\longrightarrow\cdots.
$$
Alexander duality for the embedded spheres $S\subset S^{n-1}$ and $S^k\subset S^n$ gives
$$
\widetilde H_j(A)\cong\widetilde H_j(W)\cong
\begin{cases}\ZZ,&j=d,\\0,&j\ne d.\end{cases}
$$
Thus $\widetilde H_j(B)=0$ for $j\ne d$. In degree $d$, the adjacent groups vanish, so the sequence reduces to
$$
0\longrightarrow\ZZ\xrightarrow{(i_*,-i_*)}
\widetilde H_d(B)^2\longrightarrow\ZZ\longrightarrow0.
$$
The middle group is free of rank two because this sequence splits as a sequence of abelian groups. Hence $\widetilde H_d(B)\cong\ZZ$. After choosing orientations, $i_*$ is multiplication by a positive integer $m$. The cokernel of the diagonal map $(m,-m):\ZZ\to\ZZ^2$ is $\ZZ\oplus\ZZ_m$, while the displayed exact sequence says it is $\ZZ$. Therefore $m=1$, and $i_*$ is an isomorphism. The reduced result gives the ordinary $H_0$ result as well, since both spaces are nonempty.

If $k=n$, then $S=S^{n-1}$ and $A$ is empty. The embedded $D^n$ has its boundary on $\partial D^n$. Invariance of domain makes its interior image open in $\operatorname{int}D^n$; it is also closed there, since the image of the whole disk is compact and its boundary image lies on $\partial D^n$. Hence $D=D^n$, so $B$ is empty too.
:::

::: {.remark title="What the proof is"}
The proof is the route the exercise's hint names, and that hint is the book's own correction of an earlier one: Hatcher, *Algebraic Topology*, errata for §2.B, page 176, Exercise 3, in `tmp/sources/hatcher-AT-errata.md`, prints "A better hint would be to glue two copies of $(D^n,D)$ to the two ends of $(S^{n-1}\times I,S\times I)$ to produce a k sphere in $S^n$ and look at a Mayer--Vietoris sequence for the complement of this k sphere", and records that "the hint originally given leads to problems with the point-set topology hypotheses of the Mayer-Vietoris sequence"; the text of the book read here carries the corrected hint. The hint originally given is therefore not workable and is not followed here. The proof is also not the induction of Proposition 2B.1. Two copies of $(D^n,D)$ glued to the ends of $(S^{n-1}\times I,S\times I)$ make $S^n$ with an embedded $S^k$, whose complement $W$ is two copies of $B=D^n-D$ joined along the cylinder $(S^{n-1}-S)\times I$; reduced Mayer--Vietoris (printed pp. 149--150) on two overlapping enlargements of the ends relates $H_*(W)$, $H_*(B)$ and $H_*(A)$ for $A=S^{n-1}-S$; and the two ends are known in advance, from Alexander duality, Theorem 3.44 (printed p. 254), applied to the embedded spheres $S^k\subset S^n$ and $S^{k-1}\subset S^{n-1}$. Both values are also what Proposition 2B.1(b) (printed p. 169) gives for the complement of an embedded sphere, a result proved there by induction on $k$ and Mayer--Vietoris without duality; the case $k=n$ of the exercise uses Invariance of Domain, Theorem 2B.3 (printed p. 172). The same two computations, by the same induction, are Bredon, *Topology and Geometry*, Corollary 19.3 and Theorem 19.4 (Generalized Jordan Curve Theorem), both printed p. 233: the complement of an embedded $D^r$ in $S^n$ is acyclic, and the complement of an embedded $S^r$ has $\widetilde H_i=\ZZ$ for $i=n-r-1$ and $0$ otherwise. Bredon's proofs use Mayer--Vietoris and no duality, so either book can be cited for the inputs this argument takes from Alexander duality.

Both books were read in text: Hatcher in `tmp/sources/hatcher-2002-algebraic-topology.md`, Bredon in the text layer of `tmp/sources/bredon-topology-and-geometry.pdf`, which has no checked-in text version yet.
:::
