---
schema: qual/card@1
id: P-AGH4312NODALCURVESEXIST
kind: problem
title: Existence of plane curves of degree $d$ with exactly $r$ nodes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Embeddings
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.12 together with the generic-projection results of
    IV.3 and the plane-curve genus formula. The proof below uses the classical
    Severi deformation argument: start from a maximally nodal rational plane
    curve, prove by normalization and Riemann--Roch that its nodes impose
    independent degree-d conditions, and then smooth any prescribed subset of
    the nodes. This gives all requested pairs, including the quintic cases that
    do not arise by projecting a smooth degree-five space curve.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    A complete published proof of IV.3.12 in arbitrary characteristic was
    located for this batch, and the printed exercise read again with it:
    Hartshorne, Algebraic Geometry (1977), IV Ex. 3.12, printed p. 316, and
    Remark 3.11.1, printed pp. 314-315, which states the same result as
    Severi's with Harris's proof in characteristic zero. Read at its cited
    places in the text version
    tmp/sources/christ-he-tyomkin-2020-severi-problem-arbitrary-characteristic.md:
    the Main Theorem and the paragraph after it on printed pp. 2-3, Lemma 2.6
    and Proposition 2.7 on printed p. 6, Theorem 5.1 and Corollary 5.3 on
    printed p. 22, Definition 6.2 and Proposition 6.3 on printed p. 29,
    Theorem 7.1 with its proof on printed pp. 32-34, and Lemmas 7.2 and 7.3 on
    printed p. 33; and G.-M. Greuel and E. Shustin, Plane algebraic curves with
    prescribed singularities, Theorem 2.1 with its proof, printed pp. 17-18, in
    the text version
    tmp/sources/greuel-shustin-2020-plane-curves-prescribed-singularities.md.
    Checked against the book: the exercise asks for d = 2,3,4,5 and
    0 <= r <= (d-1)(d-2)/2, which is the pair (d, g) with g = (d-1)(d-2)/2 - r
    and 0 <= g <= that bound, so the Main Theorem with the nodality of a
    general member answers it, and the node count is the book's own
    computation in Remark 3.11.1. The chapter's ground field is an
    algebraically closed field and the paper's theorem holds over any of them,
    so no hypothesis is added and none is lost. Not checked: the two sources
    of the paper's degeneration theorem, Theorem 4.6 and Theorem 5.1, whose
    proofs in Sections 4 and 5 are cited on the card at their pages and not
    reproduced; and Greuel-Shustin's [22, Corollary 6.3] and [30, Corollary
    4.3.6], the modern treatments of Severi's T-smoothness they invoke, which
    are not in tmp/sources.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the transcription of the published proof, one step per
    published move, each naming its numbered statement and printed page: steps
    severi-variety and main-theorem for the definition and the Main Theorem,
    step main-theorem-proof for its deduction from Theorem 7.1, step
    theorem-seven-one for Theorem 7.1 and its two halves, step nodal for the
    nodality of the general member (Zariski's theorem as the paper states it),
    step nodes-counted for the count from the book's Remark 3.11.1, and step
    conclusion for the exercise's finite list. The former four-step proof, the
    maximally nodal rational curve obtained by projecting a rational normal
    curve and the independent smoothing of its nodes, leaves the card and
    remains readable at commit 574af010f7; the remark's account of Egbert's
    entry 4.3.22 is replaced by the two published proofs named above, which
    supersede it for this exercise. Nothing in the problem statement changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's report, and four repairs of
    rendered text against the sources. (i) Step theorem-seven-one's account of
    similar markings left out their condition: Christ-He-Tyomkin, proof of
    Theorem 7.1, in the text version
    tmp/sources/christ-he-tyomkin-2020-severi-problem-arbitrary-characteristic.md
    at line 725, fixes three different components L, L', L'' of C_0, sets
    p := L cap L', q := L' cap L'' and r := L cap L'', and calls mu^tau
    similar to mu for the transposition tau switching q and r only when p is
    not in mu. The step now states that condition, with the three components
    and the three nodes named. (ii) The quotation of the proof of Theorem 2.1
    in G.-M. Greuel and E. Shustin, *Plane algebraic curves with prescribed
    singularities*, dropped "(see Figure 1)" from the middle of the
    quoted sentence without an ellipsis; it is restored, read at line 509 of
    tmp/sources/greuel-shustin-2020-plane-curves-prescribed-singularities.md.
    (iii) The remark's sentence "Their proof is over C, and it does not extend
    to characteristic p as it stands" carried a judgement of the source that
    nothing read supports; it is replaced by the theorem's own statement, "The
    bound (26) is necessary and sufficient for the existence of a complex
    plane irreducible curve of degree d with n nodes as its only
    singularities", which is over C as the sentence before now says. (iv) The
    paraphrase of Hartshorne's Remark 3.11.1 closed "in characteristic zero",
    which the printed remark does not say: in the text version
    tmp/sources/hartshorne-1977-algebraic-geometry.md the remark stands at
    lines 9822-9839, between the markers of PDF pages 329 and 330, that is on
    printed pp. 314-315, and it ends at "but a complete proof was given only
    recently by Joe Harris" with no hypothesis on the field. The clause is
    dropped. Checked in this pass: the three passages named, at the lines
    given, and the four places on the card. Not read in this pass: the printed
    book and the printed paper themselves, which were not reopened; no step
    was re-derived, and the two other sources of the paper's degeneration
    theorem remain unread as before.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.3.12, printed p. 89,
    rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.3.12, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed the smooth diagonal curve, the single node of $xyz^{d-2}+x^d+y^d$ at $d=3,4,5$ (lowest term $xy$ at $(0:0:1)$), $\frac12(d-1)(d-2)=3$ at $d=4$ and $6$ at $d=5$ for the projected rational normal curve, and the singular loci of the five explicit quartics and quintics by SymPy: the printed points hold for $(4,2)$, $(5,2)$ and $(5,5)$, fail for $(5,3)$ (off the curve) and $(5,4)$ (a triple point).
    Not checked: Yang's Solutions outside printed p. 89; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.3.12 at printed
    p. 89 beside the entries already there. No step, statement or
    hypothesis of the card changes.
---

::: {.problem}
For each value of $d=2,3,4,5$ and $r$ satisfying $0 \leq r \leq \frac{1}{2}(d-1)(d-2)$, show that there exists an irreducible plane curve of degree $d$ with $r$ nodes and no other singularities.
:::


::: {.solution}

Put
$$
\delta_d\coloneqq\frac{(d-1)(d-2)}{2},
$$
so that the exercise asks for an irreducible plane curve of degree $d$ with exactly $r$ nodes and no other singularities, for $d=2,3,4,5$ and $0\le r\le\delta_d$.
The proof is that of Karl Christ, Xiang He and Ilya Tyomkin, *On the Severi problem in arbitrary characteristic*.
It holds over any algebraically closed ground field, so the chapter's ground field $k$ needs no further hypothesis.
Over $\CC$ the same statement is proved from Severi's construction in G.-M. Greuel and E. Shustin, *Plane algebraic curves with prescribed singularities*, Theorem 2.1, printed pp. 17--18.

::: pf

::: {.pf-step #severi-variety}

For integers $d\ge1$ and $1-d\le g\le\delta_d$, the Severi variety $V_{g,d}$ of plane curves of degree $d$ and geometric genus $g$ is a locally closed subset of $\abs{\OO_{\PP^2}(d)}$ of pure dimension $3d+g-1$, and its irreducible part $V^{\mathrm{irr}}_{g,d}$ is its locally closed subset of irreducible curves.

::: pf-proof

Christ--He--Tyomkin, Lemma 2.6 and Proposition 2.7, printed p. 6, prove the two assertions: $V_{g,d}$ is locally closed in $\abs{\OO_{\PP^2}(d)}$, and every irreducible component of it has dimension $3d+g-1$.
The paper restates them in the form quoted, in its §5, printed p. 22: "the Severi variety parameterizing curves of degree $d$ and geometric genus $g$ is a locally closed subset $V_{g,d}\subseteq\abs{\OO_{\PP^2}(d)}$ of pure dimension $3d+g-1$".
Here $V_{g,d}$ parameterizes the reduced curves of degree $d$ whose geometric genus is $g$, so its member $[C]$ has $C$ of degree $d$ with geometric genus exactly $g$; $V^{\mathrm{irr}}_{g,d}$ is the locally closed subset of those $C$ that are irreducible.

:::

:::

::: {.pf-step #main-theorem}

Christ--He--Tyomkin, Main Theorem, printed p. 2: for integers $d\ge1$ and $0\le g\le\delta_d$, the variety $V^{\mathrm{irr}}_{g,d}$ is irreducible of dimension $3d+g-1$ over any algebraically closed ground field. In particular it is nonempty, so irreducible plane curves of degree $d$ and geometric genus $g$ exist.

::: pf-proof

The statement is the Main Theorem of the paper, printed p. 2, in its own notation: "Let $d\ge1$ and $0\le g\le\binom{d-1}{2}$ be integers. Then the Severi variety $V^{\mathrm{irr}}_{g,d}$ is irreducible of dimension $3d+g-1$ over any algebraically closed ground field."
The stated dimension $3d+g-1$ is at least $0$, and a set of dimension $3d+g-1$ is nonempty, so irreducible plane curves of degree $d$ and geometric genus $g$ exist.

:::

:::

::: {.pf-step #main-theorem-proof}

The Main Theorem is deduced in the paper from Theorem 7.1 on decorated Severi varieties, which is its §7.

::: pf-proof

The deduction, printed p. 32, is the display of the paper's §7 and reads, with $\delta=\delta_d-g$: "By Proposition 6.3 (3), $\overline{V}^{\mathrm{irr}}_{g,d}$ is the image of $\overline{U}^{\mathrm{irr}}_{d,\delta}$ under the natural projection to $\abs{\OO_{\PP^2}(d)}$. By Theorem 7.1, $U^{\mathrm{irr}}_{d,\delta}$ is non-empty and irreducible, and hence so is $V^{\mathrm{irr}}_{g,d}$. Finally, by Proposition 2.7, the Severi variety $V_{g,d}$ is either empty or equidimensional of dimension $3d+g-1$. Thus, $\dim(V^{\mathrm{irr}}_{g,d})=3d+g-1$, which completes the proof of the Main Theorem."
The decorated Severi variety $U_{d,\delta}$ is defined at Definition 6.2, printed p. 29, as the incidence locus of a degree-$d$ curve with $\delta$ marked nodes, and Proposition 6.3, printed p. 29, is quoted there for the projection.

:::

:::

::: {.pf-step #theorem-seven-one}

Christ--He--Tyomkin, Theorem 7.1, printed p. 32: the decorated Severi variety $U^{\mathrm{irr}}_{d,\delta}$ is either empty or irreducible, and it is empty if and only if $\delta>\delta_d$. The nonemptiness half is proved through Theorem 6.1(2) and Proposition 6.3(3), and the irreducibility half through Lemmas 7.2 and 7.3, printed p. 33.

::: pf-proof

The statement is Theorem 7.1, printed p. 32.
Its proof, printed pp. 32--34, has two halves.

For $\delta>\delta_d$: "If $\delta>\binom{d-1}{2}$, then $U^{\mathrm{irr}}_{d,\delta}=\emptyset$ since the geometric genus of any plane curve of degree $d$ with $\delta$ nodes is at most $\binom{d-1}{2}-\delta<0$, and hence none of such curves is irreducible."

For $\delta\le\delta_d$: the paper takes for $C_0$ the union of $d$ general lines, whose nodes number $\binom{d}{2}=\delta_d+(d-1)$, picks an irreducible component $L$ of $C_0$ and a $\delta$-element set $\vec\mu$ of nodes disjoint from $L$, which exists because $\delta\le\binom{d}{2}-(d-1)$; the curve $C_0\setminus\vec\mu$ is connected because $L$ meets every other component, so $\vec\mu$ is an irreducible marking, and "Thus, by Theorem 6.1 (2), $V^{\mathrm{irr}}_{g,d}$ is not empty, and hence so is $U^{\mathrm{irr}}_{d,\delta}$ by Proposition 6.3 (3)."

For the irreducibility: the paper fixes three different components $L,L',L''$ of $C_0$, sets $p\coloneqq L\cap L'$, $q\coloneqq L'\cap L''$ and $r\coloneqq L\cap L''$, and calls $\vec\mu^\tau$ similar to $\vec\mu$ when $\tau$ is the transposition switching $q$ and $r$ and $p\notin\mu$; $\sim$ is the transitive closure of similarity, and $\vec\mu$ is irreducible exactly when $\vec\mu^\tau$ is; Lemma 7.2, printed p. 33, states that any two irreducible markings are equivalent, and Lemma 7.3, printed p. 33, that equivalent markings give points of one irreducible component of $U_{d,\delta}$. The proof then closes, printed p. 33: "by the lemmas, there exists a unique irreducible component $U\subseteq U_{d,\delta}$ that contains $[C_0;p_1,\ldots,p_\delta]$ for any irreducible marking", and any irreducible component $U'$ of $U^{\mathrm{irr}}_{d,\delta}$ has $\phi(\overline{U'})$ containing $C_0$ by Theorem 5.1, printed p. 22, so $U'$ contains such a point and $U'=U$.

:::

:::

::: {.pf-step #nodal}

For each $d\ge1$ and $0\le g\le\delta_d$ there is an irreducible plane curve $C$ of degree $d$ whose only singularities are nodes and whose geometric genus is $g$: the general member of $V^{\mathrm{irr}}_{g,d}$ is nodal.

::: pf-proof

Christ--He--Tyomkin state this as a property of the general member, in the paragraph following the Main Theorem, printed p. 3: "since there is a dense open subset $U$ of $V^{\mathrm{irr}}_{g,d}$ that parameterizes nodal curves".
They prove it as Zariski's theorem, Corollary 5.3(2), printed p. 22: "if $\dim(V)=3d+g-1$, then for a general $[C]\in V$, the curve $C$ is nodal", applied to $V=V^{\mathrm{irr}}_{g,d}$, which is of that dimension by step [](#main-theorem){.pf-ref}.
The proof of Corollary 5.3, printed p. 22, obtains it from Theorem 5.1, printed p. 22, together with the openness of the nodal locus.

:::

:::

::: {.pf-step #nodes-counted}

A nodal irreducible plane curve of degree $d$ and geometric genus $g$ has exactly $\delta_d-g$ nodes, and its singularities are exactly those nodes.

::: pf-proof

Let $C$ be such a curve and $\widetilde C\to C$ its normalization, of genus $g$.
The arithmetic genus of a plane curve of degree $d$ is $p_a=\frac12(d-1)(d-2)=\delta_d$, and each node lowers the genus of the normalization by exactly $1$, so
$$
g=\delta_d-\#\{P\in C:P\text{ a node}\},
$$
that is, the number of nodes is $\delta_d-g$.
This is the computation of Hartshorne, Remark 3.11.1, printed p. 314, where "the genus $g$ of its normalization $\widetilde X$ is given by $g=\frac12(d-1)(d-2)-r$ because of (Ex. 1.8)", $r$ being the number of nodes.
Since nodes are the only singularities of $C$ by step [](#nodal){.pf-ref}, the nodes are exactly the singular points of $C$.

:::

:::

::: {.pf-step #conclusion}

For each $d=2,3,4,5$ and each integer $r$ with $0\le r\le\delta_d$ there is an irreducible plane curve of degree $d$ with exactly $r$ nodes and no other singularities.
$$
\boxed{\text{for }d=2,3,4,5\text{ and }0\le r\le\delta_d\text{ there is such a curve}}
$$

::: pf-proof

Fix $d\in\{2,3,4,5\}$ and $0\le r\le\delta_d$, and put $g\coloneqq\delta_d-r$, so that $0\le g\le\delta_d$ and $d\ge1$.
By step [](#main-theorem){.pf-ref} the variety $V^{\mathrm{irr}}_{g,d}$ is irreducible of dimension $3d+g-1$, and by step [](#nodal){.pf-ref} it has a dense open subset of nodal curves; choose a nodal $[C]$ in it.
The curve $C$ is irreducible of degree $d$ and has only nodes as singularities, and by step [](#nodes-counted){.pf-ref} the number of its nodes is $\delta_d-g=r$.
That is the curve the exercise asks for.
For $d=2$ one has $\delta_2=0$, and the curve is a nonsingular conic.

:::

:::

:::

:::

::: {.remark title="Published solution"}

The exercise is a finite case of the Severi problem, and the two published proofs of it differ in characteristic.
Christ--He--Tyomkin, *On the Severi problem in arbitrary characteristic*, prove the Main Theorem quoted in step [](#main-theorem){.pf-ref} over any algebraically closed field; their §5 proves Theorem 5.1 and Zariski's theorem by tropical degeneration, and §7 the decorated Severi varieties.

G.-M. Greuel and E. Shustin, *Plane algebraic curves with prescribed singularities*, Theorem 2.1, printed pp. 17--18, prove the statement over $\CC$ by Severi's construction, in four sentences: "given $n$ and $d$ satisfying (26), we take the union of $d$ straight lines in general position, which is a curve with $\frac{d(d-1)}{2}$ nodes (the maximum by (27)). Then choose some line and deform the curve by smoothing out all $d-1$ intersection points of this line with the other lines, obtaining an irreducible, rational curve with $\frac{(d-1)(d-2)}{2}$ nodes (see Figure 1). Finally, we take another deformation by smoothing out $\frac{(d-1)(d-2)}{2}-n$ nodes and obtain an irreducible curve of degree $d$ with $n$ nodes as desired."
Their bound (26) is $n\le\frac{(d-1)(d-2)}{2}$, and the deformation they use is Severi's: "the germ of the family of curves of degree $d$ having a node in a neighborhood of an arbitrary singular point of $C$, is a smooth hypersurface germ in $\OO_{\PP^2}(d)\cong\PP^{d(d+3)/2}$, and, moreover, all these germs intersect transversally at $C$", for which they cite [22, Corollary 6.3] and [30, Corollary 4.3.6]. Their theorem is stated for complex plane curves: "The bound (26) is necessary and sufficient for the existence of a complex plane irreducible curve of degree $d$ with $n$ nodes as its only singularities", and the argument above is its proof.

Hartshorne states the same result in the text, immediately before the exercise, as Severi's: Remark 3.11.1, printed pp. 314--315, records that for all $d,r$ with $0\le r\le\frac12(d-1)(d-2)$ the set $V_{d,r}$ is "irreducible and nonempty of dimension $\frac12d(d+3)-r$, but a complete proof was given only recently by Joe Harris".


Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.3.12, printed p. 89, answers the exercise case by case rather than by the Severi theory: for $r=0$ it takes $x^d+y^d+z^d$, smooth over $\CC$ for $d=2,3,4,5$; for $r=1$ it takes $xyz^{d-2}+x^d+y^d$, whose only singular point is $(0:0:1)$, an ordinary node; for the maximum $r=\frac12(d-1)(d-2)$ at $d=4$ and $d=5$ it projects the rational normal curve of degree $d$ from $\PP^d$ to a plane curve $Y$ of the same degree $d$, which by the genus formula carries $\frac12(d-1)(d-2)$ nodes; and for the remaining five pairs $(d,r)=(4,2),(5,2),(5,3),(5,4),(5,5)$ it writes an explicit quartic or quintic and lists its nodes. Two of these steps are not established as printed. The projection in the third case has to be a general one: the count $\frac12(d-1)(d-2)$ is the number of nodes of a general plane projection of the rational normal curve, and the entry says only 'we may project it into $\PP^2$', which for a special centre gives fewer nodes or worse singularities. And the five explicit curves are asserted, not computed: 'has only two nodes' and the rest come with no singularity computation, the entry closing with 'Mathematica is Power, France is Bacon'. Checked here by exact symbolic computation on the printed strings, read at 600 dpi: for $(d,r)=(4,2)$, $(5,2)$ and $(5,5)$ the listed points are on the curve, are singular, are the whole singular locus, and have nondegenerate quadratic part --- two, two and five ordinary nodes as claimed. Two of the lines do not survive that check and are recorded rather than copied: $(5,3)$ lists $(\frac{1-\sqrt3}{2}:1:1)$ and $(-\frac{1-\sqrt3}{2}:1:1)$, and neither point is on the quintic, where the two nodes are at $(-\frac12\pm\frac{\sqrt3}{2}i:1:1)$ --- the printed coordinates are their real parts; and $(5,4)$ lists four nodes including $(1:0:0)$, which is on the curve and singular but has multiplicity three there, its lowest term being $z(y^2-yz+z^2)$, so that curve has three nodes and a triple point, not four nodes.
:::
