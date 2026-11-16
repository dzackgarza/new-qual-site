---
schema: qual/card@1
id: E-HAT-3.3-21
kind: problem
title: Compactly supported cohomology and one-point compactification
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
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 21; it matches the printed text. The printed bracketed question about $X=\ZZ\times\RR$ was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: excision identifies $H^n(X^+,U_K;G)$ with $H^n(X,X-K;G)$, cone-shaped
    neighbourhoods are cofinal, and on each of them the point $\infty$ is a homotopy equivalence,
    so the limit is $H^n(X^+,\infty;G)$.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The print says "let $X^+$ be the one-point compactification" without hypotheses; that object is
    a compact Hausdorff compactification only when $X$ is locally compact Hausdorff, which the
    solution now states instead of using silently. The sets $U_K$ were also said to "range over all"
    neighbourhoods of $\infty$, which is false — they are cofinal, and the cofinality is now proved.
    DEFERRED, recorded not dropped: the printed bracketed question for $X=\ZZ\times\RR$ is not
    answered. Its hypothesis fails there, since the complement of a compact set meets infinitely many
    lines in unbounded intervals, and the card says only that; whether the isomorphism still holds is
    open on this card.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The bracketed question is now answered from Stanford Math 215C Solution Set 4, Hatcher 3.3.21,
    printed p.1. H_c^1(Z x R) is countable because cofinal rectangles K_N have finite relative
    cohomology Z^{2N+1}: each of the 2N+1 lines in K_N contributes one H^1(R,R-J_m)=Z summand. In
    contrast the circle retractions give H^1((Z x R)^+) containing Hom of the product of Z over N,
    hence uncountable. So no such isomorphism exists; the earlier lim^1 remark was unnecessary and
    has been removed.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Withdraws the incorrect counterexample and its audit claim. A surjection H_1(X+) to the product
    of Z gives an injection on the corresponding Hom groups, not uncountability; and the Hom group
    of the product is itself countable by Specker's theorem. Frankland, Cohomology of the Hawaiian
    Earring (2017), Theorems 1.2 and 1.3 (p.2) gives H^1(E;Z) equal to the countable direct sum,
    and Theorem 1.4 (p.3) the induced dual iso. Stanford Solution Set 4's false counterexample is
    removed. The definite answer to Hatcher's bracketed question is not established from this
    source and remains deferred.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Answers the bracketed question negatively in degree two with integer coefficients. The
    cofinal-rectangle calculation gives H_c^2(Z x R; Z) = 0. The compactification is the
    Hawaiian earring E, whose H_1 has a Q direct summand by Eda-Kawamura, Theorem 3.1,
    pp.307-310 (also stated as Frankland Theorem 2.1, p.3). Universal coefficients and
    Wiegold's nonzero Ext(Q,Z), pp.341-342, then give H^2(E; Z) != 0, so the natural map is not
    an isomorphism. Replaces the deferred and H^1-only discussion with an argument assembled from
    separately published theorems, not with a published complete exercise solution. The #105
    published-solution obligation stays open; the cone-neighborhood proof in the first part is
    unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read Hatcher pp.243-244 and the complete Eda-Kawamura and Wiegold papers. Checked that
    H^2(E, infinity; Z) agrees with H^2(E; Z) by the pair sequence, that Ext is additive over
    the Q direct summand, and that the cofinal relative intervals make all degree-two compactly
    supported groups vanish. Thus this is a counterexample already for n = 2 and G = Z, not a
    claim that H^1 fails or that no coefficient group could work.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Removed the unsupported assertion that inverse stereographic projection proves the absence
    of a cone neighborhood. The final paragraph now uses the justified implication instead: the
    degree-two contradiction proves that the cone-neighborhood hypothesis of the first part cannot
    hold for Z x R. Eda-Kawamura and Wiegold remain supporting citations only; a complete published
    solution to the exercise has not been located, so the #105 source obligation remains open.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Located and checked the complete published solution of the first part: Stanford Math 215C,
    Solution Set 4, Hatcher 3.3.21, printed p. 1, served at
    http://math.stanford.edu/~ralph/math215c/solution4.pdf and held as
    tmp/sources/stanford-math215c-spring2009-solution4.pdf, 59584 bytes, sha256
    b4c348109162ed7e97309e15f1b153efa363cd0338800e8d251f64f335eef470, the local size matching the
    served content length. Checked its steps: excision of the point infinity out of the open set
    X^+ - K is legitimate because the closure of {infinity} is {infinity}, contained in that open
    set, and gives H^n(X^+, X^+ - K) = H^n(X, X - K); the exact sequence of the pair (X^+, U_K) is
    reduced and legitimate as both entries are nonempty; for K the complement of a cone-shaped
    neighbourhood U_K is a cone, hence contractible with vanishing reduced cohomology, which is
    what makes the restriction H^n(X^+, U_K) -> H^n(X^+, infinity) an isomorphism; the K's of this
    form are cofinal among compact subsets since cone-shaped neighbourhoods can be shrunk inside any
    neighbourhood of infinity, and the isomorphisms are compatible with inclusions, so they pass to
    the direct limit. That is the argument already in steps excision-limit and cone-case, so this
    citation confirms rather than replaces them, and it discharges the published-solution
    obligation for the first part. This supersedes the closing sentence of the previous event,
    which said no complete published solution had been located. NOT used and explicitly rejected in
    the card: the source's paragraph on Z x R, which infers uncountability of H^1 from a surjection
    H_1 -> product of Z, whereas dualizing a surjection gives an injection and Hom(product Z, Z) is
    the countable direct sum by Specker's theorem. The bracketed question therefore still rests on
    the assembled degree-two counterexample from Eda-Kawamura and Wiegold, not on a published
    complete exercise solution, and that narrower obligation stays open.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    Re-read for the published-solution obligation. The card's first part is the complete published solution of Stanford Math 215C, Spring 2009, Solution Set 4, Hatcher §3.3 Exercise 21, printed p. 1: excision to move $H^n(X^+,X^+-K;G)$ to $H^n(X,X-K;G)$, cone-shaped neighbourhoods of $\infty$ as a cofinal system of compact sets, the exact sequence of the pair forcing $\tilde H^m(U_K;G)=0$, and the direct limit over the cofinal system. Checked against the book: the exercise's printed statement on p. 262 with its cone hypothesis, and the definition of compactly supported cohomology. Not claimed: the set's own paragraph on $X=\ZZ\times\RR$ is rejected on the card and the card's counterexample there stands; the citation covers the first part only.
- event: source-corrected
  by: claude
  date: 2026-11-13
  note: >-
    The page in the preceding note is wrong and is corrected here: the exercise is on printed p. 259,
    the last page of §3.3, not p. 262, which is in §3.A. Read again in Hatcher, *Algebraic Topology*
    (2002), printed p. 259 and in the current online text at the same page: the statement there is
    "For a space $X$, let $X^+$ be the one-point compactification. If the added point, denoted
    $\infty$, has a neighborhood in $X^+$ that is a cone with $\infty$ the cone point, show that the
    evident map $H_c^n(X;G)\to H^n(X^+,\infty;G)$ is an isomorphism for all $n$. [Question: Does this
    result hold when $X=\ZZ\times\RR$?]", matching the card. The bracketed part remains as recorded:
    no published solution of it was located, in the retained sets or elsewhere, and the card answers
    it with its own degree-two counterexample. Searched without result for the bracketed part in the
    retained sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C Solution Sets 1--5, the UCR Math
    205B help file, May's *Concise Course*, Bredon, Maxim's Math 752 notes) and in Hatcher's text and
    errata; Hatcher's errata has no entry for §3.3 near this page.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    The degree-one cohomology of the compactification, which the card had only asserted to be
    uncountable-then-countable in a rejected argument, is now cited from a published source, supplied
    by the owner for #123 and read in the text version: Martin Frankland, *Cohomology of the Hawaiian
    Earring* (dated February 22, 2017), Theorem 1.3 and the sentence immediately after it, both on
    printed p. 2 of the note. Theorem 1.3 states that the map $H^1(E;\ZZ)\to\operatorname{Hom}_{\ZZ}
    (\bigoplus_\NN\ZZ,\ZZ)$ dual to $H_1(\iota)$ is injective with image $\bigoplus_\NN\ZZ$, and the
    sentence after it draws the conclusion $H^1(E)\cong\bigoplus_{n\in\NN}\ZZ$, "a free abelian group
    on countably many generators". Read only in degree one and only with integer coefficients, which
    is the part the note proves; the card does not cite it for any other degree. The reading copy is
    `tmp/sources/frankland-2017-cohomology-hawaiian-earring.md`; the PDF already held as
    `tmp/sources/frankland-hawaiian-earring-2017.pdf` is the same note, and Theorem 2.1 of it was
    already cited on this card for the $\QQ$ summand.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Added step "degree-one" to the solution: $H_c^1(\ZZ\times\RR;\ZZ)$ from the card's own cofinal
    rectangle computation, and $H^1((\ZZ\times\RR)^+,\infty;\ZZ)$ from Frankland's Theorem 1.3,
    printed p. 2, together with the exact sequence of the pair $(E,\infty)$. The step's point is
    negative and is what the rejected Stanford paragraph got wrong: both sides in degree one are free
    abelian on countably many generators, so no countability argument in degree one can decide the
    bracketed question, and the card's counterexample has to be, and is, in degree two. The card's
    closing paragraph now also says which part of the exercise is published (the first part, Stanford
    Math 215C Solution Set 4) and which is not (the bracketed question, whose answer here is assembled
    from Eda--Kawamura, Wiegold and Frankland). Not claimed: a published solution of the bracketed
    question; none was located, and the earlier events recording that stand.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    One step of the degree-one comparison was reasoned wrongly and is corrected. It derived the
    isomorphism $H^1(E,\infty;\ZZ)\cong H^1(E;\ZZ)$ from the vanishing of $H^0(E,\infty;\ZZ)$ alone,
    which gives injectivity only; surjectivity of $H^1(E,\infty;\ZZ)\to H^1(E;\ZZ)$ comes from
    $H^1(\{\infty\};\ZZ)=0$, since exactness at $H^1(E;\ZZ)$ identifies the image with the kernel of
    $H^1(E;\ZZ)\to H^1(\{\infty\};\ZZ)$, which is everything. The card now gives both reasons and
    states the resulting short exact sequence $0\to H^1(E,\infty;\ZZ)\to H^1(E;\ZZ)\to0$. The
    conclusion of the step is unchanged. Checked against Hatcher (2002), §3.3 Exercise 21 on printed
    p. 259 and the long exact sequence of a pair in cohomology, and against Frankland's Theorem 1.3
    with the sentence after it on printed p. 2, which supplies the value $H^1(E;\ZZ)\cong
    \bigoplus_{\NN}\ZZ$ used by the step.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    A second complete published solution of the first part is now cited on the card: C. Kottke, *Math
    2420 Problem Set 3 solutions*, Brown University, Spring 2012, Problem 2, printed p. 2 of
    `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.pdf` (5 pp., sha256
    e84fd60496037db45bb18457b7c922233f5912a41b5d067112ba75a8211c22a7). Read at that page and checked
    step by step: the disjoint neighbourhoods $U$ of $K$ and $V$ of $\infty$, $V$ shrunk inside the
    cone neighbourhood so that it deformation retracts to $\infty$, $L=X\setminus V$ compact with
    $K\subset L$, and $H^n(X,X\setminus L)=H^n(X,V)\cong H^n(X^+,V)\cong H^n(X^+,\infty)$ by
    excision of $\infty$ and the deformation retraction, then the direct limit over the cofinal
    family. It agrees with steps excision-limit and cone-case, which transcribe the Stanford set and
    are unchanged. The page claims already on the card were re-read at the sources this pass: Stanford
    Math 215C Solution Set 4, printed p. 1 (59584 bytes, sha256
    b4c348109162ed7e97309e15f1b153efa363cd0338800e8d251f64f335eef470); Frankland, Theorem 1.3 with
    the sentence after it on printed p. 2 and Theorem 2.1 on printed p. 3; Eda--Kawamura, Theorem 3.1
    on printed p. 307, whose third summand is $\bigoplus_\kappa\QQ$ with $\kappa=\cardinality{I^{\NN}}$, hence
    continuum many copies of $\QQ$ for $I=\NN$, which is the $\QQ$ summand the step uses and which the
    extracted text of that paper renders only as a stray glyph; Wiegold, pp. 341--342. The bracketed question
    still has no published solution, and the sources read for it this pass are recorded in
    `COMPLAINTS.md`: the accepted answer to Math Stack Exchange question 4224576 shows only that
    $\infty$ has no cone neighbourhood in the compactification of $\ZZ\times\RR$, which is not the
    question; question 4812778 poses the exercise and has no answers; Kottke's set has no paragraph on
    $\ZZ\times\RR$; and the Stanford set's paragraph is the rejected one. Checked against Hatcher
    (2002), §3.3 Exercise 21 on printed p. 259, and against Hatcher's errata, which carries no entry
    for that page.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Two corrections to the transcription of Kottke's solution and one to the citations. (1) The
    transcription followed the source's own slip in writing $H^n(X,V)$ for a group in which $V$ is an
    open set of $X^+$ containing $\infty$, and so is not a subset of $X$; the card now writes
    $H^n(X,V\setminus\{\infty\})\cong H^n(X^+,V)$ and says that the middle isomorphism is excision of
    the point $\infty$, closed in $X^+$ and contained in the open $V$, hence with closure inside the
    interior of $V$, so that excision is legitimate. The two outer groups are unchanged. (2) The
    duplicate PDF name `tmp/sources/frankland-hawaiian-earring-2017.pdf`, which was cited in step
    earring-degree-two, is the same note as `tmp/sources/frankland-2017-cohomology-hawaiian-earring.md`
    (identical bytes, checked with `md5sum`); the card now cites the text version and no longer names
    the duplicate. Theorem 1.3 with the sentence after it on printed p. 2 and Theorem 2.1 on printed
    p. 3 were re-read in that text version this pass, and the $\QQ$ direct summand is Theorem 2.1's
    $\bigoplus_{\mathfrak c}\QQ$ with $\mathfrak c=2^{\aleph_0}$. (3) Text versions are now named on
    every citation: Hatcher in `tmp/sources/hatcher-2002-algebraic-topology.md`, Frankland in its
    `.md`; Eda--Kawamura, Wiegold, Stanford Solution Set 4 and Kottke have no text version in
    `tmp/sources` and are named as read from their PDF text layers. Checked against Hatcher (2002),
    §3.3 Exercise 21 on printed p. 259, and against the exercise's cone hypothesis, which the
    $X=\ZZ\times\RR$ counterexample is used to show fails. Not claimed: a published solution of the
    bracketed question, which is still absent.
---

::: {.problem}
For a space $X$, let $X^+$ be the one-point compactification.
If the added point, denoted $\infty$, has a neighborhood in $X^+$ that is a cone with $\infty$ the cone point, show that the evident map $H_c^n(X; G) \to H^n(X^+, \infty; G)$ is an isomorphism for all $n$.
[Question: Does this result hold when $X = \ZZ \times \RR$?]
:::

::: {.solution}
Assume that $X$ is locally compact Hausdorff, so that $X^+$ is a compact Hausdorff space with $X$ open in it.

::: pf

::: {.pf-step #excision-limit}
Excision identifies $H_c^n(X;G)$ with the direct limit of $H^n(X^+,U;G)$ over all neighborhoods $U$ of $\infty$.

::: pf-proof
For a compact $K\subset X$, let $U_K=X^+\setminus K$, an open neighborhood of $\infty$. Excision of the point $\infty$, whose closure lies in the interior of $U_K$, gives
$$
H^n(X^+,U_K;G)\cong H^n(X,X\setminus K;G).
$$
As $K$ ranges over compact subsets of $X$, the neighborhoods $U_K$ are cofinal among the neighborhoods of $\infty$: every neighborhood $U$ of $\infty$ has compact complement $X\setminus U$, and $U_{X\setminus U}\subset U$. Since the direct limit defining $H_c^n(X;G)$ can be taken over this cofinal family,
$$
H_c^n(X;G)\cong\varinjlim_{\infty\in U}H^n(X^+,U;G).
$$
:::

:::

::: {.pf-step #cone-case}
If $\infty$ has a cone neighborhood in $X^+$, then the evident map $H_c^n(X;G)\to H^n(X^+,\infty;G)$ is an isomorphism for all $n$.

::: pf-proof
Inside the cone neighborhood from the hypothesis, every neighborhood of the cone point contains a smaller cone-shaped neighborhood that contracts to the cone point by radial scaling. These contractible neighborhoods are cofinal among the neighborhoods of $\infty$. For each such $U$, the inclusion $\{\infty\}\hookrightarrow U$ is a homotopy equivalence. The map of long exact sequences for the pairs $(X^+,U)$ and $(X^+,\{\infty\})$ therefore shows that restriction is an isomorphism
$$
H^n(X^+,U;G)\xrightarrow{\cong}H^n(X^+,\infty;G).
$$
These isomorphisms commute with restriction to smaller cone neighborhoods. Taking the direct limit and using step [](#excision-limit){.pf-ref} gives the asserted isomorphism $H_c^n(X;G)\cong H^n(X^+,\infty;G)$.
:::

:::

::: {.pf-step #compact-degree-two}
For $X=\ZZ\times\RR$ and integer coefficients, $H_c^2(X;\ZZ)=0$.

::: pf-proof
Let $J_N=[-N-1/2,N+1/2]$ and $K_N=([-N-1/2,N+1/2]^2)\cap X$ for $N\ge1$. These compact rectangles are cofinal among compact subsets of $X$. On each of the $2N+1$ lines meeting $K_N$, the relative cohomology is $H^q(\RR,\RR-J_N;\ZZ)$, which is $\ZZ$ for $q=1$ and zero otherwise. Hence
$$
H^q(X,X-K_N;\ZZ)\cong
\begin{cases}
\ZZ^{2N+1},&q=1,\\
0,&q\ne1.
\end{cases}
$$
In particular, the direct limit in step [](#excision-limit){.pf-ref} vanishes in degree two.
:::

:::

::: {.pf-step #earring-degree-two}
The compactification $E=(\ZZ\times\RR)^+$ has $H^2(E,\infty;\ZZ)\ne0$.

::: pf-proof
Each line becomes a circle in $E$, with all circles sharing $\infty$, and every neighborhood of $\infty$ contains all but finitely many whole circles. Thus $E$ is the Hawaiian earring. The pair sequence gives $H^2(E,\infty;\ZZ)\cong H^2(E;\ZZ)$, and universal coefficients give an injection
$$
\operatorname{Ext}_{\ZZ}(H_1(E;\ZZ),\ZZ)\hookrightarrow H^2(E;\ZZ).
$$
By **K. Eda and K. Kawamura, *The Singular Homology of the Hawaiian Earring*, Theorem 3.1, pp. 307--310** (`tmp/sources/eda-kawamura-hawaiian-earring-2000.pdf`, read from the PDF's text layer, `tmp/sources` holding no text version of it), $H_1(E;\ZZ)$ has a direct summand isomorphic to $\QQ$; this is also stated as Theorem 2.1 of **Martin Frankland, *Cohomology of the Hawaiian Earring*, p. 3**, whose text is the reading copy `tmp/sources/frankland-2017-cohomology-hawaiian-earring.md`. Consequently $\operatorname{Ext}_{\ZZ}(\QQ,\ZZ)$ is a direct summand of the left-hand group above. By **James Wiegold, *Ext(Q,Z) is the additive group of real numbers*, pp. 341--342** (`tmp/sources/wiegold-ext-q-z-1969.pdf`, also read from the PDF's text layer), $\operatorname{Ext}_{\ZZ}(\QQ,\ZZ)\cong\RR\ne0$. The target group is therefore nonzero.
:::

:::

::: {.pf-step #degree-one}

For $X=\ZZ\times\RR$ and integer coefficients, $H_c^1(X;\ZZ)$ and $H^1(X^+,\infty;\ZZ)$ are both free abelian on countably many generators, so degree one does not separate the two sides.

::: pf-proof

Step [](#compact-degree-two){.pf-ref} computes $H^q(X,X\setminus K_N;\ZZ)=\ZZ^{2N+1}$ for $q=1$ and $0$ otherwise, and the family $\{K_N\}$ is cofinal, so the direct limit of step [](#excision-limit){.pf-ref} in degree one is the free abelian group on countably many generators. For the right-hand side, step [](#earring-degree-two){.pf-ref} identifies $X^+$ with the Hawaiian earring $E$, and **Martin Frankland, *Cohomology of the Hawaiian Earring* (2017), Theorem 1.3 with the sentence following it, printed p. 2**, whose text is `tmp/sources/frankland-2017-cohomology-hawaiian-earring.md`, gives

$$
H^1(E;\ZZ)\cong\bigoplus_{n\in\NN}\ZZ,
$$

"a free abelian group on countably many generators": the map $H^1(E;\ZZ)\to\operatorname{Hom}_{\ZZ}(\bigoplus_{\NN}\ZZ,\ZZ)$ induced by $H_1(\iota)$ is injective with image $\bigoplus_{\NN}\ZZ$, and $H^1(E;\ZZ)\cong\operatorname{Hom}_{\ZZ}(H_1(E;\ZZ),\ZZ)$ because $H_0(E;\ZZ)$ is free. The exact sequence of the pair $(E,\infty)$ then gives $H^1(E,\infty;\ZZ)\cong H^1(E;\ZZ)$: the map $H^0(E;\ZZ)=\ZZ\to H^0(\{\infty\};\ZZ)=\ZZ$ is onto, so the image of $H^0(\{\infty\};\ZZ)$ in $H^1(E,\infty;\ZZ)$ is $H^0(\{\infty\};\ZZ)$ modulo the image of $H^0(E;\ZZ)$, which is zero, and $H^1(E,\infty;\ZZ)\to H^1(E;\ZZ)$ is injective by exactness; while $H^1(\{\infty\};\ZZ)=0$ makes it surjective. The tail of that sequence is thus the short exact sequence $0\to H^1(E,\infty;\ZZ)\to H^1(E;\ZZ)\to0$. Both groups are thus free abelian on countably many generators, and no argument in degree one can decide the bracketed question.

:::

:::

::: pf-step
The answer to the bracketed question is no, already for $G=\ZZ$ and $n=2$.

::: pf-proof
Steps [](#compact-degree-two){.pf-ref} and [](#earring-degree-two){.pf-ref} give
$$
\boxed{H_c^2(\ZZ\times\RR;\ZZ)=0,\qquad H^2((\ZZ\times\RR)^+,\infty;\ZZ)\ne0,}
$$
so the evident map cannot be an isomorphism. Consequently the cone-neighborhood hypothesis of step [](#cone-case){.pf-ref} cannot hold here. This counterexample does not depend on the previously rejected countability argument, and it makes no assertion that the degree-one map fails.
:::

:::

:::

The first part is the complete published solution of **Stanford Math 215C, Solution Set 4, Hatcher 3.3.21, printed p. 1**, [`solution4.pdf`](http://math.stanford.edu/~ralph/math215c/solution4.pdf), held locally as `tmp/sources/stanford-math215c-spring2009-solution4.pdf` (59584 bytes, sha256 `b4c348109162ed7e97309e15f1b153efa363cd0338800e8d251f64f335eef470`, matching the served file). Its argument is the one transcribed in steps [](#excision-limit){.pf-ref} and [](#cone-case){.pf-ref}: for compact $K\subset X$ the point $\infty$ is excised, giving $H^n(X^+,X^+\setminus K;G)\cong H^n(X,X\setminus K;G)$; the exact sequence of the pair $(X^+,U_K)$ with $U_K=X^+\setminus K$ has $\widetilde H^m(U_K;G)=0$ for all $m$ when $K$ is the complement of a cone-shaped neighbourhood of $\infty$, so $H^n(X,X\setminus K;G)\cong\widetilde H^n(X^+;G)=H^n(X^+,\infty;G)$; these $K$ are cofinal among compact subsets because cone-shaped neighbourhoods can be shrunk inside any neighbourhood of $\infty$, and the isomorphism passes to the direct limit $H_c^n(X;G)$.

A second, independent complete published solution of the first part is **C. Kottke, *Math 2420 Problem Set 3 solutions*, Brown University, Spring 2012, Problem 2, printed p. 2** (`tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.pdf`, read from the PDF's own text layer, `tmp/sources` holding no text version of it). It states the hypothesis as this card does, for $X$ locally compact Hausdorff, and reaches the same limit by a cofinal family built the other way round. Let $K\subset X$ be compact. Since $X^+$ is Hausdorff there are disjoint open sets $U\supset K$ and $V\ni\infty$; shrinking $V$ inside the cone-shaped neighbourhood of the hypothesis, one may assume that $V$ deformation retracts to $\infty$. Put $L=X\setminus V$. Then $L$ is compact and $K\subset L$, and since $X\setminus L=V\setminus\{\infty\}$,
$$
H^n(X,X\setminus L)=H^n(X,V\setminus\{\infty\})\cong H^n(X^+,V)\cong H^n(X^+,\infty),
$$
the first group by the identity just written, the middle isomorphism by excision of the point $\infty$ — closed in $X^+$ and contained in the open set $V$, so that its closure lies in the interior of $V$ — and the last by the deformation retraction of $V$ onto $\infty$. The source prints the middle group as $H^n(X,V)$; $V$ is an open set of $X^+$ containing $\infty$ and so is not a subspace of $X$, and the excision removes $\infty$ from it. The $L$ so obtained are cofinal among the compact subsets of $X$, so the direct limit over them is $H_c^n(X;G)$, and the isomorphisms are compatible with inclusions, which is the theorem. This solution absorbs each compact set into a larger one instead of using the vanishing of $\widetilde H^m(U_K;G)$; it is the cofinality assertion of step [](#excision-limit){.pf-ref} read backwards.

The closing paragraph of the Stanford set, on $X=\ZZ\times\RR$, is **not** used and must not be: it concludes that $H^1$ of the compactification is uncountable from a surjection $H_1\twoheadrightarrow\prod_\NN\ZZ$, whereas dualizing a surjection gives an injection, and $\operatorname{Hom}(\prod_\NN\ZZ,\ZZ)\cong\bigoplus_\NN\ZZ$ is countable by Specker's theorem. The bracketed question is answered above, in degree two with $G=\ZZ$, by the assembled counterexample.

Which part is published and which is not: the first part of the exercise has two complete published solutions, both cited above, the Stanford set's and Kottke's; the degree-one cohomology of the compactification is published in Frankland's Theorem 1.3, printed p. 2, as step [](#degree-one){.pf-ref} records; and the bracketed question itself has no published solution. The answer given to it on this card is assembled from three published theorems — Eda–Kawamura for the $\QQ$ summand of $H_1(E;\ZZ)$, Wiegold for $\operatorname{Ext}_{\ZZ}(\QQ,\ZZ)\ne0$, and Frankland for the degree-one value — and is not a transcription of any published treatment of the question.

The text versions this card's citations rest on: the exercise and every Hatcher page quoted above are read in `tmp/sources/hatcher-2002-algebraic-topology.md`; Frankland is read in `tmp/sources/frankland-2017-cohomology-hawaiian-earring.md`, the same note as the PDF `tmp/sources/frankland-hawaiian-earring-2017.pdf` (identical bytes), whose duplicate file name is no longer cited; Eda–Kawamura at `tmp/sources/eda-kawamura-hawaiian-earring-2000.pdf` and Wiegold at `tmp/sources/wiegold-ext-q-z-1969.pdf` have no text version in `tmp/sources` and were read from their PDF text layers, as were Stanford's `tmp/sources/stanford-math215c-spring2009-solution4.pdf` and Kottke's `tmp/sources/kottke-brown-math2420-sp12-ps3-solutions.pdf`.

:::
