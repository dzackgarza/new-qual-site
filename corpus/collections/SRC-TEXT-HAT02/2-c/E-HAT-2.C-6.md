---
schema: qual/card@1
id: E-HAT-2.C-6
kind: problem
title: 'Even-genus analog of Lefschetz example: replace central torus by sphere with antipodal map'
classification:
  areas:
  - topology
  topics:
  - Lefschetz Fixed Point Theorem
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.C Exercise 6, printed page
    184, which asks for an even-genus analog of Example 2C.4 (genus 3, p. 181) with
    the central torus replaced by a sphere and f the antipodal map there; the card's
    statement matches. Proof checked: attaching handles in m antipodal pairs with
    matching parametrizations gives a fixed-point-free homeomorphism of the genus 2m
    surface; f_* swaps the rank-two summands of H_1 pairwise, so its trace is 0; and
    on H_2 = Z it is the antipodal map of S^2, of degree -1 (Proposition 2.30,
    p. 134). Then tau(f) = 1 - 0 - 1 = 0, as the fixed-point-free map requires. No
    defect.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Matched the full construction to Daniel Dugger, Involutions on Surfaces, not merely to a
    citation about involutions. Section2.7 pp.11-12 defines the centered antipodal action
    T_g^anti and computes its nonorientable quotient; Proposition2.8 p.12 splits the even-genus
    action into the antipodal sphere and paired handles; Theorem4.1(a) p.18 states freeness in
    even genus. Transcribed this as the card's map. The antipodal interchange of paired handles
    gives the zero diagonal on H_1, and the nonorientable quotient confirms degree-1 on H_2.
    Thus Lefschetz is 1-0-1=0, the complete published even-genus argument matching Hatcher p.184.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Corrected the preceding coverage claim. Dugger supplies the centered antipodal involution,
    its decomposition and quotient, but not a complete solution to Hatcher Exercise 2.C.6:
    the exercise's paired-handle trace computation is assembled by instantiation. No retained
    published exercise solution performs that computation. The mathematics and Dugger citation
    remain, but the complete published-solution obligation remains open.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    Re-read for the source obligation of the card. The exercise is on printed p. 184 and asks for the even-genus analog of Example 2C.4, which the book works out for genus $3$ on printed p. 181; the construction of the involution is Dugger, *Involutions on surfaces*, §2.7, printed pp. 11--12, with Theorem 4.1(a) on p. 18 identifying the even-genus free involution, both already cited on the card. Checked: the printed statement, Example 2C.4's trace computation $\tau(f)=1-0-1$ on p. 181, and the antipodal degree on the central sphere. Not claimed: that a published source works this exercise; the card's own trace computation for the even-genus model is what the citation supports.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    Re-read the printed statement for #123: the exercise is Exercise 6 of §2.C on printed p. 184,
    identical in the current online text ("Do an even-genus analog of Example 2C.4 by replacing the
    central torus by a sphere letting $f$ be a homeomorphism that restricts to the antipodal map on
    this sphere"), and the card states it word for word. The obligation that #123 records is
    unchanged and stays open: Dugger supplies the involution and its quotient, not a solution of
    this exercise, and no published solution of the exercise was located. Searched without result in
    the retained sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C Solution Sets 1--5, the UCR
    Math 205B help file, May, Bredon, Maxim's Math 752 notes) and in Hatcher's text and errata.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Two sentences of the opening paragraph contradicted each other, and the stronger of them is
    false of its source. It said that Dugger's centred antipodal action "is exactly Hatcher's
    requested even-genus analog", and in the same paragraph that the construction "supplies the
    checked model below, but not a complete published solution of Hatcher Exercise 2.C.6". The
    first sentence is withdrawn. What Dugger gives, checked in the text: Proposition 2.8, printed
    p. 12, the equivariant isomorphism $T^{anti}_{2g}=S^2_a\#T_g$; the quotient
    $T^{anti}_g/C_2=N_{g+1}$ on the same page, which is why the involution is orientation
    reversing; and Theorem 4.1(a), printed p. 18, the uniqueness of the free involution in even
    genus. Those identify the involution the exercise asks about, but Dugger works no Lefschetz
    number and does not treat the exercise. The trace computation is the card's own and is
    checked: the $H_1$ trace is zero because the $m$ antipodal pairs of handles are interchanged,
    and $f_*$ on $H_2$ is multiplication by $-1$ because the restriction to the central sphere is
    the antipodal map of $S^2$, of degree $-1$; so $\tau(f)=1-0-1=0$, as a fixed-point-free map
    on an orientable surface requires. Repair: the card carried a second `---` line after its
    front matter, removed. Sources read for a published solution, and what each lacks, are
    recorded in COMPLAINTS.md item 11. Not claimed: a published solution of Exercise 2.C.6.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader batch. The reader accepted the mathematics and named two weak steps and a
    citation defect. (1) The step constructing $f$ said to "attach each pair of handles by
    identical parametrizations", which does not make the antipodal map extend across the pair.
    It now says what the construction is: if one handle is attached by
    $\varphi:S^0\times D^1\to\partial M$, its partner is attached by
    $\alpha\circ\varphi\circ\tau$, the antipodal composite, where $\alpha$ is the involution of
    the surface built so far and $\tau(\epsilon,s)=(1-\epsilon,s)$ reverses the $S^0$ factor,
    and the map that is $\alpha$ on the old surface and $(t,s)\mapsto(1-t,s)$ on $D^1\times D^1$
    then pastes across both handles; the same formula is its own inverse. Checked: at a point
    $\varphi(\epsilon,s)$ of the attaching region the two definitions agree,
    $\alpha\varphi(\epsilon,s)=\varphi_2\tau(\epsilon,s)$. (2) The orientation step was informal:
    it said the extensions across handles "preserve this local orientation-reversing character".
    It now runs through the local degree. For $p$ on the central sphere outside the attaching
    regions, $f$ agrees near $p$ with the antipodal map of $S^2$, whose degree and hence local
    degree is $-1$, so the local degree of $f$ at $p$ is $-1$; a homeomorphism of a connected
    closed orientable surface induces multiplication by its degree on $H_2$, and its degree is
    its local degree at any one point because $f^{-1}(f(p))=\{p\}$; hence $f_*=-1$ on $H_2$. The
    quotient argument from Dugger's nonorientable $T^{\mathrm{anti}}_{2m}/C_2$ is kept as the
    independent confirmation. (3) The citations now name a text version: Hatcher in
    `tmp/sources/hatcher-2002-algebraic-topology.md` (Exercise 6, printed p. 184; Example 2C.4,
    printed p. 181); Dugger has **no** text version in `tmp/sources`, so the card says it was
    read in the text layer of `tmp/sources/dugger-involutions-surfaces-2016.pdf`, PDF page 12 =
    printed p. 12 for Proposition 2.8 and the quotient, PDF page 18 = printed p. 18 for
    Theorem 4.1(a). Checked, unchanged: $\tau(f)=1-0-1=0$. Not claimed: a published solution of
    Exercise 2.C.6.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, second pass on this card: the handle model was wrong, and the two
    sentences above that describe it are withdrawn rather than rewritten. They said that
    $M_{2m}$ is built from $m$ antipodal pairs of handles $D^1\times D^1$ attached along
    $S^0\times D^1$, and that the pasting map is $(t,s)\mapsto(1-t,s)$ on $D^1\times D^1$. A band
    attached along $S^0\times D^1$ adds no genus, and $2m$ of them on a sphere with $2m$ holes give
    genus $m$ ($\chi=2-2m$), not genus $2m$, which needs $\chi=2-4m$; and the formula
    $(t,s)\mapsto(1-t,s)$ read on a single handle fixes $\{1/2\}\times D^1$, contradicting the
    step that $f$ has no fixed point. The model is now a sphere with $m$ antipodal pairs of holes
    and $m$ antipodal pairs of punctured tori, one pair of genus handles for each pair of holes,
    so that $\chi(M_{2m})=(2-2m)-2m=2-4m$ and the genus is $2m$; this is Dugger's
    $T^{\mathrm{anti}}_{2m}=S^2_a\mathbin{\#_{\mathrm{eq}}}T_m$ of Proposition 2.8, printed p. 12.
    The map is stated from each handle to its partner, $f(h_i(y))=h_{i'}(y)$ and
    $f(h_{i'}(y))=h_i(y)$ with $h_{i'}=\alpha\circ h_i$, so no copy of the punctured torus is
    mapped to itself and $f\circ f=\mathrm{id}$. The trace is now computed on a stated basis:
    $H_1(M_{2m};\ZZ)\cong\bigoplus_{i=1}^{2m}H_1(T_i;\ZZ)$ by Mayer--Vietoris, a boundary circle
    of a punctured torus being a commutator, and $f_*$ permutes the $2m$ summands in $m$
    transpositions, so the diagonal vanishes. Unchanged and re-checked: the local-degree step at a
    point $p$ of the sphere region, where $f^{-1}(f(p))=\{p\}$ because $f$ carries punctured tori
    to punctured tori, and $\tau(f)=1-0-1=0$; the exercise as printed on p. 184; and Dugger's lack
    of a text version in `tmp/sources`. Not claimed: a published solution of Exercise 2.C.6. The
    `E-HAT-2.C-6` entry of COMPLAINTS.md is corrected by a new entry of this date.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, second pass: the `source-checked` note of 2026-11-13 says the exercise was
    searched for in "Stanford Math 215C Solution Sets 1--5". `tmp/sources` holds
    `stanford-math215c-spring2009-solution2.pdf`, `-3` and `-4`, and no Solution Set 1 or 5, so the
    range is not what was read. The range is Solution Sets 2--4, and the same wrong range on
    `E-HAT-2.B-5`, `-2.B-7` and `-2.C-1` is corrected by a new event on each of those cards. Nothing
    else in that note changes: the ranges of the other retained sets it lists are as it gives them, no
    retained set reaches §2.C beyond Poulsen's 2.C.2, 2.C.8 and 2.C.9, Li's 2.C.2, 2.C.4 and 2.C.5 and
    DeMason's four, and no published solution of Exercise 2.C.6 was located.
---

::: {.problem}
Do an even-genus analog of Example 2C.4 by replacing the central torus by a sphere letting $f$ be a homeomorphism that restricts to the antipodal map on this sphere.
:::

::: {.solution}
Use the standard centered antipodal action $T_g^{\mathrm{anti}}$ published in **Daniel Dugger, *Involutions on Surfaces*, §2.7, printed pp. 11--12** (`tmp/sources/dugger-involutions-surfaces-2016.pdf`). His Proposition 2.8 gives $T_{2g}^{\mathrm{anti}}\cong S^2_a\mathbin{\#_\mathrm{eq}}T_g$, an antipodal sphere with paired handles, and Theorem 4.1(a), p. 18, identifies this as the free involution in even genus. Write $g=2m$, let $M_{2m}=T_{2m}^{\mathrm{anti}}$, and regard it as a central sphere carrying $m$ antipodal pairs of genus handles, each genus handle a punctured torus glued to one hole of a pair: a pair of them adds two punctured tori to the sphere, so $m$ pairs give genus $2m$, since $\chi(M_{2m})=(2-2m)-2m=2-4m$. Dugger also computes $T_g^{\mathrm{anti}}/C_2\cong N_{g+1}$, so the involution is orientation reversing. The general construction supplies the checked model below, but not a complete published solution of Hatcher Exercise 2.C.6, whose source obligation remains open.

::: pf

::: pf-step

Define a homeomorphism $f:M_{2m}\to M_{2m}$ by the antipodal map on the central sphere and by interchanging the two handles in each antipodal pair.

::: pf-proof

Construct $M_{2m}$ and $f$ together. The surface is a sphere with $m$ antipodal pairs of open disks removed and a punctured torus --- a closed torus with an open disk removed --- glued to each of the $2m$ boundary circles, in charts matched by the antipodal map. Concretely, let $H_1,\dots,H_{2m}$ be disjoint closed disks in $S^2$ with $\alpha(H_i)=H_{i'}$ for the antipodal map $\alpha$ of $S^2$, put $A=S^2-\bigcup_j\operatorname{int}H_j$, and for each pair $\{i,i'\}$ attach two copies of one punctured torus $T$, the first by an embedding $h_i:T\to M_{2m}$ at $\partial H_i$ and the second by $h_{i'}:=\alpha\circ h_i$, which is an attaching chart of the partner because $\alpha$ carries $\partial H_i$ onto $\partial H_{i'}$. Each of the $2m$ punctured tori contributes $-1$ to $\chi$ and the sphere with $2m$ holes contributes $2-2m$, so $\chi(M_{2m})=2-4m$ and the closed orientable surface $M_{2m}$ has genus $2m$. The pieces are genus handles: $m$ pairs of punctured tori, not $m$ pairs of bands, since a band $D^1\times D^1$ attached along $S^0\times D^1$ adds no genus, and a surface built from $2m$ bands would be of genus $m$. This is Dugger's $T^{\mathrm{anti}}_{2m}=S^2_a\mathbin{\#_{\mathrm{eq}}}T_m$, each equivariant connected summand contributing a punctured torus and its mirror image.

Define $f$ by $f=\alpha$ on $A$ and, on the copies of $T$, by
$$
f\bigl(h_i(y)\bigr)=h_{i'}(y),\qquad f\bigl(h_{i'}(y)\bigr)=h_i(y)\qquad(y\in T),
$$
so $f$ carries each handle of a pair onto its partner and not onto itself, and no formula of $f$ is taken on a single copy of $T$ alone. The two clauses agree with $f=\alpha$ on the interface: for $y\in\partial T$ one has $f(h_i(y))=h_{i'}(y)=\alpha(h_i(y))$. The two clauses are inverse to each other and $\alpha$ is its own inverse, so $f\circ f=\operatorname{id}$, and $f$ is a homeomorphism restricting to $\alpha$ on the central sphere.

:::

:::

::: pf-step

The map $f$ has no fixed points.

::: pf-proof

The antipodal map has no fixed point on the central sphere. Every point in an attached handle is carried into the distinct partner handle. Hence no point of the whole surface is fixed.

:::

:::

::: {.pf-step #s3}

On $H_1(M_{2m};\ZZ)$, the map $f_*$ has trace zero.

::: pf-proof

By Mayer--Vietoris for $M_{2m}=A\cup B$, where $B$ is the disjoint union of the $2m$ punctured tori, the boundary circle of a punctured torus is a commutator in that torus and hence zero in $H_1(T;\ZZ)$, while the $2m$ boundary circles generate $H_1(A;\ZZ)$ with the single relation that their sum is zero; hence
$$
H_1(M_{2m};\ZZ)\cong H_1(A;\ZZ)\big/\langle\partial H_j\rangle\ \oplus\ \bigoplus_i H_1(T_i;\ZZ)\cong\bigoplus_{i=1}^{2m}H_1(T_i;\ZZ),
$$
free of rank $4m=2g$, with basis the two standard loops of each punctured torus. The map $f$ carries $T_i$ homeomorphically onto $T_{i'}$ and permutes the $2m$ summands in $m$ transpositions, so relative to this basis the matrix of $f_*$ has zero diagonal and its trace is zero. Writing two generators per handle and interchanging the pairs, as the basis above does, gives the same matrix.

:::

:::

::: {.pf-step #s4}

On $H_2(M_{2m};\ZZ)\cong\ZZ$, the map $f_*$ is multiplication by $-1$.

::: pf-proof

Let $p$ be a point of the central sphere outside the attaching regions, so that a neighbourhood of $p$ in the sphere is a neighbourhood of $p$ in $M_{2m}$ and $f$ is the antipodal map there. The antipodal map of $S^2$ is a homeomorphism of degree $-1$, so its local degree at $p$ is $-1$, and hence the local degree of $f$ at $p$ is $-1$ as well. For a homeomorphism of the connected closed orientable surface $M_{2m}$, the induced map on $H_2$ is multiplication by its degree, and its degree is the local degree at any single point, because $f^{-1}(f(p))=\{p\}$. Hence $f_*$ is multiplication by $-1$ on $H_2(M_{2m};\ZZ)$. Equivalently, Dugger's quotient $T_{2m}^{\mathrm{anti}}/C_2\cong N_{2m+1}$ is nonorientable, so the involution is orientation reversing in the published construction as well.

:::

:::

::: pf-step

Consequently
$$
\tau(f)=1-0+(-1)=0,
$$
as required by the Lefschetz theorem for a fixed-point-free map.

::: pf-proof

The trace on $H_0$ is $1$ because the surface is connected, step [](#s3){.pf-ref} gives the $H_1$ trace, and step [](#s4){.pf-ref} gives the $H_2$ trace.

:::

:::

:::

This gives the even-genus counterpart of Example 2C.4. Additional symmetric pairs of handles increase the genus by two without introducing fixed points.
:::

::: {.remark title="Sources"}
Hatcher, *Algebraic Topology* (2002), read in `tmp/sources/hatcher-2002-algebraic-topology.md`: the exercise is Exercise 6 of §2.C, printed p. 184, and Example 2C.4, the genus-$3$ case it modifies, is printed p. 181 with the trace computation $\tau(f)=1-0-1$. Dugger, *Involutions on surfaces*, was read in the text layer of `tmp/sources/dugger-involutions-surfaces-2016.pdf`, which has no checked-in text version yet: Proposition 2.8 and the quotient $T_g^{\mathrm{anti}}/C_2\cong N_{g+1}$ on PDF page 12 = printed p. 12, and Theorem 4.1(a) on PDF page 18 = printed p. 18. Dugger works no Lefschetz number and does not treat the exercise; the identification of the involution and the trace computation are the card's own.
:::
