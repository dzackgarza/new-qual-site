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
---

::: {.problem}
Do an even-genus analog of Example 2C.4 by replacing the central torus by a sphere letting $f$ be a homeomorphism that restricts to the antipodal map on this sphere.
:::

::: {.solution}
Use the standard centered antipodal action $T_g^{\mathrm{anti}}$ published in **Daniel Dugger, *Involutions on Surfaces*, §2.7, printed pp. 11--12** (`tmp/sources/dugger-involutions-surfaces-2016.pdf`). His Proposition 2.8 gives $T_{2g}^{\mathrm{anti}}\cong S^2_a\mathbin{\#_\mathrm{eq}}T_g$, an antipodal sphere with paired handles, and Theorem 4.1(a), p. 18, identifies this as the free involution in even genus. Write $g=2m$, let $M_{2m}=T_{2m}^{\mathrm{anti}}$, and regard it as a central sphere with $m$ antipodal pairs of handles. Dugger also computes $T_g^{\mathrm{anti}}/C_2\cong N_{g+1}$, so the involution is orientation reversing. The general construction supplies the checked model below, but not a complete published solution of Hatcher Exercise 2.C.6, whose source obligation remains open.

::: pf

::: pf-step

Define a homeomorphism $f:M_{2m}\to M_{2m}$ by the antipodal map on the central sphere and by interchanging the two handles in each antipodal pair.

::: pf-proof

Choose the attaching disks in antipodal pairs and attach each pair of handles antipodally: if the first handle of a pair has attaching map $\varphi:S^0\times D^1\to\partial M$, its partner is attached by $\alpha\circ\varphi\circ\tau$, where $\alpha$ is the antipodal involution of the surface built so far and $\tau(\epsilon,s)=(1-\epsilon,s)$ reverses the $S^0$ factor. The map that is $\alpha$ on that surface and $(t,s)\mapsto(1-t,s)$ on each handle $D^1\times D^1$ then carries the attaching data of a handle to the attaching data of its partner, so it pastes to a continuous self-map; the same formula is its own inverse, and it restricts to $\alpha$ on the old surface. The resulting map is a homeomorphism.

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

Choose the standard two generators on each handle. The handles occur in $m$ pairs, and $f_*$ swaps the two corresponding rank-two summands for each pair. Relative to this basis the matrix has zero diagonal, so its trace is zero.

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
