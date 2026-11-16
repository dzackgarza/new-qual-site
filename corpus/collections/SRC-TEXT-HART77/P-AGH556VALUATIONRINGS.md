---
schema: qual/card@1
id: P-AGH556VALUATIONRINGS
kind: problem
title: Classification of valuation rings of the function field of a surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Hartshorne V.5.6 as transcribed here, the retained Andrew Egbert
    companion argument, II.4.12 and its corrected solution, the valuation
    center criterion II.4.5, and V.5.1 on resolving a rational function by
    point blowups. The retained companion identifies the successive-center
    trichotomy but does not prove the hint's decisive assertion in case (3).
    The proof below supplies it: for f in R, resolve [f:1] by finitely many
    point blowups. Blowups away from the center of R are local
    isomorphisms, while a blowup at that center is exactly the next member
    of the valuation's center sequence. Thus some O_{X_i,x_i} is the local
    ring at the center on the resolved model. Since f lies in R, the induced
    Spec R -> P^1 lands in A^1, so f is regular at that center. Hence every
    f in R lies in the union R_0, proving R=R_0.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the complete trichotomy against II.4.12, the proper-center
    criterion, and V.5.1. Checked that a codimension-one center forces
    equality with the corresponding DVR, while a closed center lifts to the
    exceptional curve after each blowup and either becomes divisorial
    (type 2) or yields the infinite type-3 chain. In the infinite case,
    checked the local comparison with an arbitrary finite point-blowup
    resolution of [f:1]: off-center blowups leave the center local ring
    unchanged, on-center blowups advance exactly one A_i, and f in R gives
    an extension Spec R -> A^1 whose uniqueness inside P^1 forces f to be
    regular at the resolved center. Thus f lies in every A_i for i
    sufficiently large, so R=union A_i.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Published solution located for issue #121: Yang Pi-Yeh, Hartshorne
    Solutions, exercise 5.5.6, printed p. 114 of
    tmp/sources/lfwin-hartshorne-solutions.pdf (folios = PDF pages; the printed
    page was located with pdftotext as a locator), read in the MinerU extraction
    tmp/sources/lfwin-hartshorne-solutions.md. It proves all three kinds: by the
    valuation criterion the ring has a center P and dominates O_P; the center's
    dimension is tr.d._k(R/m), so 1 gives a DVR equal to O_P (kind 1) and 0 gives
    the closed-point case, where each blowup puts the next center either on the
    exceptional curve (kind 2) or at a point of it, and the infinite alternative
    gives R = lim O_{P_i} = union O_{P_i} (kind 3). That union identification is
    the step Exercise II.4.12 leaves open and Egbert's entry does not prove; it
    is this card's step union-contained-in-r. The remark now gives the source's
    argument and says which of this card's steps is which. Checked against
    Hartshorne V.5.6, printed p. 299, and against the three kinds as printed in
    Exercise II.4.12.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Correction, on a reader's report of issue #121: the event above is wrong
    where it says Yang's entry "proves all three kinds" and where it maps his
    union to step union-contained-in-r. Re-read in
    tmp/sources/lfwin-hartshorne-solutions.md, Solution 5.5.6 is Egbert's
    V.5.6 entry (printed p. 299) plus one sentence, and that sentence is the
    bare assertion R = lim O_{P_i,X_i} = union O_{P_i,X_i} with no argument;
    his entry does not use the hint, Exercise V.5.1, at all. It therefore
    proves kind (3) no more than Egbert does, and the exercise is proved by
    this card's own steps element-eventually-regular (Exercise V.5.1 places
    each f in R in some A_i) and r-equals-union-type-three (both
    inclusions); step union-contained-in-r proves only R_0 contained in R.
    Two errors in his sentence are now flagged on the remark: the union along
    the inclusions is a direct limit, not the inverse limit his display
    writes first; and his reading of tr.d._k(R/m_R) as the dimension of the
    centre does not separate kind (1) from kind (2), since in kind (2) the
    DVR at the generic point of the exceptional curve has residue
    transcendence degree 1 over k while its centre on X is a closed point.
    V.5.6 is not closed by a published proof.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Checked on a reader's report of issue #121 that returned this page and
    named no false statement on it, and the check found none. Hartshorne
    V.5.6 is printed on p. 420: the marker of its page in
    tmp/sources/hartshorne-1977-algebraic-geometry.md is PDF page 435, and
    435-15=420. Read Exercise II.4.12(3) and the Note after it at printed
    p. 108: the exercise builds R_0, says only that R_0 is a local ring
    dominated by some valuation ring R of K/k, and the Note defers R_0=R
    to this exercise. Read Yang Pi-Yeh's Solution 5.5.6 at page 114 of
    tmp/sources/lfwin-hartshorne-solutions.pdf in the PDF's own text layer
    and in the extraction tmp/sources/lfwin-hartshorne-solutions.md, and
    Egbert's V.5.6 entry at page 299 of
    tmp/sources/hartshorne-solutions-egbert.md: Yang's page is Egbert's
    argument, with the finite-repeat case that Egbert leaves implicit
    written out and the one sentence R = lim O_{P_i,X_i} = union
    O_{P_i,X_i} added, for which no argument is given; and Yang's own
    preface on page 1 of that PDF, dated June 9, 2019, lists "Andrew
    Egbert's solution I googled" among the sources he referred to.
    Searched every other solution set retained in tmp/sources for an entry
    on V.5.6 and found none, and confirmed that the NTU Chapter V homework
    has no Section 5 exercise 6 and that Reid's Chapters on Algebraic
    Surfaces mentions valuation rings only in passing. The remark
    therefore gains the sentence that no published proof of R contained in
    R_0 was located, naming what was searched, and no other claim is
    changed. Not checked: the survey Egbert cites, "Vaqiue Valuations and
    local uniformization, remark 1.14", was neither located in tmp/sources
    nor read, and nothing outside the retained sources was searched afresh
    beyond the search of 2026-11-15 already recorded on this page. The two
    events of 2026-11-15 above had been rewritten in place; both are restored
    to the text they were dated with, and both then give printed p. 299, which
    is Egbert's page and not the book's: the exercise is printed p. 420, and
    the correction is here.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The search-status paragraph is removed from the remark. What it recorded
    --- that no published proof of R contained in R_0 was located, which sets
    were searched, and that the survey Egbert cites was not read --- is the
    entry for V.5.6 in COMPLAINTS.md, which records it, and the card carries
    no process. No mathematical claim changes: the remark still names the two
    published entries and what each does not prove. Not checked: nothing new;
    the card's steps were not re-derived in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Published proof located for issue #121, and the third kind is transcribed
    from it: S. S. Abhyankar, On the valuations centered in a local domain,
    Amer. J. Math. 78 (1956), pp. 321--348, text version
    tmp/sources/abhyankar-1956-valuations-centered-local-domain.md, whose
    printed page is its PDF page plus 320 (checked on the PDF's own text
    layer: Definition 3 stands on printed p. 335 and Proposition 3 on printed
    p. 336). Read and checked: Definition 3, printed p. 335, and Lemma 10,
    printed pp. 334--335, for the identification of the blowup at the centre
    with the first quadratic transform; Proposition 3, printed pp. 336--337,
    that the quadratic sequence along a prime divisor is finite; Lemma 7,
    printed p. 332, Theorem 1, printed p. 330, and Lemma 12, printed
    pp. 337--338, whose two assertions are exactly R contained in the union of
    the successive local rings and the uniqueness of the valuation centred at
    all of them. Steps quadratic-sequence, union-is-valuation-ring and
    union-equals-r replace the steps union-contained-in-r,
    element-eventually-regular and r-equals-union-type-three named in the
    events above: Lemma 12 proves R = union A_i directly, so the card no
    longer carries its own resolution of [f:1] by Exercise V.5.1, and the
    remark names that route as the book's hint instead. Checked against
    Hartshorne V.5.6, printed p. 420, and Exercise II.4.12 with its Note,
    printed p. 108: the three kinds are as printed, and both assertions the
    Note defers to this exercise are what Proposition 3 and Lemma 12 give. Not
    checked: Abhyankar's Lemma 13 and Proposition 5, which the card does not
    use, and no published proof of the third kind beyond the sets already
    recorded here and in COMPLAINTS.md was sought.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The event above, of the same day, had been rewritten in place by commit
    a9eb8698ca; it is restored here to the text it carried when d3d047c189
    wrote it, and this event is its correction. Corrected: the identification
    of Abhyankar's quadratic transform with the local ring of the centre on a
    blowup, which the round had attributed to his Lemma 10. Re-read in
    tmp/sources/abhyankar-1956-valuations-centered-local-domain.md, whose
    markers cover ten pages at a time, printed page = PDF page plus 320:
    Definition 3, printed p. 335, defines the quadratic transform of a regular
    local domain along a valuation, and Lemma 10, printed pp. 334--335,
    proves that transform a regular local domain in which the valuation is
    centred at the maximal ideal. Neither statement mentions a blowup, so the
    identification of that ring with OO_{X_{i+1},x_{i+1}} is no source's, and
    the chart factorisation written for it in this batch was written today.
    It is removed. What stands for the third kind is the card's own proof,
    which was on the card before this batch: steps union-contained-in-r,
    element-eventually-regular and r-equals-union-type-three, the second of
    them resolving [f:1] by Exercise V.5.1 as the printed hint directs. Those
    three steps return to the text they carried at 83d33296ae, and the steps
    quadratic-sequence, union-is-valuation-ring and union-equals-r that the
    round put in their place are withdrawn with the identification they
    rested on. Abhyankar's Proposition 3, printed pp. 336--337, and Lemma 12,
    printed pp. 337--338, stay cited in the remark as what is published for a
    quadratic sequence; his statements are made for the quadratic transforms
    of the local domain along the valuation, which is what Definition 3
    defines.

    Also corrected: the remark said "The classification is Abhyankar's",
    which is false. His Theorem 1, printed p. 330, sorts a valuation centred
    in an n-dimensional local domain by its R-dimension d, rational rank r
    and rank rho, with d+r <= n; the three kinds of Exercise II.4.12 are the
    book's, and no statement of his names them. And kinds (1) and (2) now
    cite the two entries that prove them, Yang Pi-Yeh, solution 5.5.6,
    printed p. 114 of tmp/sources/lfwin-hartshorne-solutions.pdf as read in
    tmp/sources/lfwin-hartshorne-solutions.md, and A. Egbert, V.5.6, printed
    p. 299 of tmp/sources/hartshorne-solutions-egbert.md, in the steps
    codim-one-center-type-one and divisorial-center-type-two; the round had
    dropped their attribution from the remark without putting it anywhere
    else.

    Not checked: Abhyankar's Lemma 13 and Proposition 5, which the card does
    not use; his printed proof of Proposition 3 compresses the passage from
    R_v/M_v algebraic over R_s/M_s to the contradiction, and the card uses the
    proposition as a stated theorem. No published proof of R contained in R_0
    for the third kind was located, in this pass or in the passes the events
    above record.
---

::: {.problem}
Let $X$ be a surface with function field $K$.
Show that every valuation ring $R$ of $K / k$ is one of the three kinds described in (II, Ex.
4.12).

Hint: In case (3), let $f \in R$.
Use (Ex.
5.1) to show that for all $i \gg 0$, $f \in \OO_{X_i}$, so in fact $f \in R_0$.
:::

::: {.solution}
Under the standing hypotheses of Chapter V, $X$ is a nonsingular projective
surface over the algebraically closed field $k$. Put
$$
K=k(X).
$$

Exercise II.4.12 explicitly excludes the trivial valuation ring $K$ itself
from its three surface types. We therefore prove the assertion for
$$
R\subsetneq K;
$$
the ring $K$ is the separate trivial case.

::: pf

::: {.pf-step #unique-center-exists}
The valuation ring $R$ has a unique center
$$
x_0\in X.
$$

::: pf-proof
Since $X$ is projective, it is proper over $k$. The valuation-center
criterion [[P-AGH245VALCENTER|Exercise II.4.5]] says that every valuation
ring of $K/k$ has a unique center on a proper model. Equivalently, the
generic-point map
$$
\Spec K\longrightarrow X
$$
extends uniquely to
$$
\Spec R\longrightarrow X,
$$
and the image of the closed point is $x_0$.
:::

:::

::: {.pf-step #center-not-generic-point}
The center $x_0$ is not the generic point of $X$.

::: pf-proof
If $x_0=\eta_X$, then domination gives
$$
\OO_{X,\eta_X}=K\subseteq R.
$$
Since already $R\subseteq K$, this would force
$$
R=K,
$$
contrary to the nontriviality assumption.

Because $\dim X=2$, step [](#center-not-generic-point){.pf-ref} leaves two possibilities: $x_0$ is the
generic point of an irreducible curve, or $x_0$ is a closed point.
:::

:::

::: {.pf-step #codim-one-center-type-one}
If $x_0$ has codimension one, then
$$
\boxed{R=\OO_{X,x_0},}
$$
so $R$ is of type (1) in Exercise II.4.12.

::: pf-proof
Since $X$ is nonsingular and $x_0$ has codimension one,
$$
\OO_{X,x_0}
$$
is a one-dimensional regular local domain, hence a discrete valuation ring
with fraction field $K$.

The assertion that $x_0$ is the center means precisely that $R$ dominates
$\OO_{X,x_0}$. A valuation ring dominating another valuation ring of the
same fraction field is equal to it [[P-AGH2412VALEX]]. Hence
$$
R=\OO_{X,x_0}.
$$
This is the first surface construction in Exercise II.4.12.

Yang Pi-Yeh, solution 5.5.6, printed p. 114, and Egbert, V.5.6, printed
p. 299, argue this case the same way: $X$ is projective and hence proper, the
valuation criterion gives $\Spec R\to X$ whose closed-point image is the
centre $P$ of $\nu$, and $R$ dominates $\OO_P$; a centre of dimension one
leaves two discrete valuation rings, so $R=\OO_P$.

Assume from now on that $x_0$ is closed.
:::

:::

::: {.pf-step #successive-centers-on-blowups}
As long as the center $x_i$ of $R$ on $X_i$ is closed, define
$$
X_{i+1}=\Bl_{x_i}X_i.
$$
Then $R$ has a unique center
$$
x_{i+1}\in X_{i+1},
$$
and
$$
\boxed{x_{i+1}\in E_{i+1},}
$$
where $E_{i+1}$ is the exceptional curve of
$$
X_{i+1}\longrightarrow X_i.
$$

::: pf-proof
The blowup of a nonsingular projective surface at a closed point is again a
nonsingular projective surface. Hence step [](#unique-center-exists){.pf-ref} applies to every $X_i$ and
gives a unique center $x_{i+1}$ on $X_{i+1}$.

The morphism
$$
X_{i+1}\longrightarrow X_i
$$
is proper and the induced maps
$$
\Spec R\longrightarrow X_{i+1}\longrightarrow X_i
$$
and
$$
\Spec R\longrightarrow X_i
$$
agree on the generic point. By uniqueness of the center on $X_i$, the
closed point $x_{i+1}$ maps to $x_i$. Therefore
$$
x_{i+1}\in\pi_{i+1}^{-1}(x_i)=E_{i+1}.
$$
:::

:::

::: {.pf-step #divisorial-center-type-two}
If for some $n\ge1$ the center $x_n$ is the generic point of
$E_n$, then
$$
\boxed{R=\OO_{X_n,x_n},}
$$
and $R$ is of type (2) in Exercise II.4.12.

::: pf-proof
The surface $X_n$ is nonsingular, so the local ring at the generic point of
the irreducible curve $E_n$ is a DVR:
$$
\OO_{X_n,x_n}.
$$
The valuation ring $R$ dominates this DVR because $x_n$ is its center.
As in step [](#codim-one-center-type-one){.pf-ref}, domination between valuation rings of the same fraction
field forces equality.

The composite birational morphism
$$
X_n\longrightarrow X
$$
maps the exceptional curve $E_n$ to the original closed point $x_0$.
Thus $R$ is exactly the local ring at the generic point of a curve on a
birational model which is contracted to a closed point of $X$, the second
construction of Exercise II.4.12.

Yang Pi-Yeh, solution 5.5.6, printed p. 114, and Egbert, V.5.6, printed
p. 299, reach this case the same way: the closed centre is blown up, and the
centre of $\nu$ on the blowup is either the exceptional curve, which is what
this step computes, or a point of it, where one repeats.
:::

:::

::: {.pf-step #union-contained-in-r}
If no center ever becomes divisorial, then every $x_i$ is closed and
the construction gives an infinite chain
$$
X=X_0
\longleftarrow
X_1
\longleftarrow
X_2
\longleftarrow
\cdots
$$
of blowups at the successive centers of $R$. Put
$$
A_i=\OO_{X_i,x_i},
\qquad
R_0=\bigcup_{i\ge0}A_i.
$$
Then
$$
\boxed{R_0\subseteq R.}
$$

::: pf-proof
By definition of center, $R$ dominates every $A_i$, so
$$
A_i\subseteq R
$$
for all $i$. Hence their union is contained in $R$.

Moreover the transition maps are local inclusions
$$
A_i\hookrightarrow A_{i+1},
$$
because $x_{i+1}$ lies above $x_i$. Thus this is precisely the third
construction of Exercise II.4.12, except that it remains to prove the
assertion promised there:
$$
R_0=R.
$$
:::

:::

::: {.pf-step #element-eventually-regular}
Let
$$
f\in R.
$$
There is an index $N$ such that, for every $i\ge N$,
$$
\boxed{f\in A_i=\OO_{X_i,x_i}.}
$$

::: pf-proof
The case $f=0$ is immediate, so assume
$$
f\in K^\times.
$$
Regard $f$ as the rational map
$$
\varphi_f:X\dashrightarrow\PP^1,
\qquad
x\longmapsto[f(x):1].
$$
Exercise V.5.1 [[P-AGH551RESOLVERATFN]] gives a finite sequence of point
blowups
$$
Y_m
\xrightarrow{g_m}
Y_{m-1}
\longrightarrow
\cdots
\longrightarrow
Y_1
\xrightarrow{g_1}
Y_0=X
$$
such that $\varphi_f$ extends to a morphism
$$
\psi:Y_m\longrightarrow\PP^1.
$$

For each $j$, let $y_j$ be the unique center of $R$ on $Y_j$. We compare the
local rings at these centers with the sequence
$$
A_0\subset A_1\subset A_2\subset\cdots.
$$

Suppose the point blown up by
$$
g_j:Y_j\longrightarrow Y_{j-1}
$$
is not $y_{j-1}$. Then $g_j$ is an isomorphism on a neighbourhood of
$y_{j-1}$, and therefore
$$
\OO_{Y_j,y_j}\cong\OO_{Y_{j-1},y_{j-1}}.
$$

Suppose instead that $g_j$ blows up $y_{j-1}$. Under any identification
$$
\OO_{Y_{j-1},y_{j-1}}\cong A_i
$$
already obtained, this is the blowup at the center $x_i$ of $R$. The center
$y_j$ selected by $R$ on that blowup is therefore the same infinitely near
point as $x_{i+1}$, and
$$
\OO_{Y_j,y_j}\cong A_{i+1}.
$$

Starting from
$$
\OO_{Y_0,y_0}=\OO_{X,x_0}=A_0
$$
and proceeding through the finite sequence of blowups, we obtain some
$N\le m$ with
$$
\OO_{Y_m,y_m}\cong A_N
$$
inside the common function field $K$.

It remains to see that $f$ is regular at $y_m$. Because
$$
f\in R,
$$
the $k$-algebra map
$$
k[t]\longrightarrow R,
\qquad
t\longmapsto f,
$$
defines a morphism
$$
\Spec R\longrightarrow\AA^1\subset\PP^1
$$
whose restriction to $\Spec K$ is the rational map $[f:1]$.

On the other hand, the center morphism
$$
\Spec R\longrightarrow Y_m
$$
followed by $\psi$ gives another extension to $\PP^1$ of the same
generic-point map. Since $\PP^1$ is separated, the two extensions agree.
Consequently
$$
\psi(y_m)\in\AA^1,
$$
and the affine coordinate $t$ pulls back near $y_m$ to the rational function
$f$. Hence
$$
f\in\OO_{Y_m,y_m}=A_N.
$$
Since
$$
A_N\subseteq A_{N+1}\subseteq A_{N+2}\subseteq\cdots,
$$
the same element belongs to $A_i$ for every $i\ge N$, exactly as asserted
in the hint.
:::

:::

::: {.pf-step #r-equals-union-type-three}
In the infinite closed-center case,
$$
\boxed{R=R_0=\bigcup_{i\ge0}\OO_{X_i,x_i}.}
$$
Thus $R$ is of type (3) in Exercise II.4.12.

::: pf-proof
Step [](#union-contained-in-r){.pf-ref} gives
$$
R_0\subseteq R.
$$
Conversely, step [](#element-eventually-regular){.pf-ref} shows that every element
$$
f\in R
$$
belongs to some $A_N$, hence to $R_0$. Therefore
$$
R\subseteq R_0.
$$
The two inclusions give equality.

In particular, the local union $R_0$ in the third construction is itself a
valuation ring; no additional dominating valuation ring is needed. This is
the assertion deferred from Exercise II.4.12 to the present exercise.
:::

:::

::: {.pf-step #trichotomy-established}
Every nontrivial valuation ring of $K/k$ is one of the three kinds
from Exercise II.4.12.

::: pf-proof
By steps [](#unique-center-exists){.pf-ref} and [](#center-not-generic-point){.pf-ref}, its center on $X$ is either divisorial or closed.
The divisorial case is type (1) by step [](#codim-one-center-type-one){.pf-ref}.

Starting from a closed center, step [](#successive-centers-on-blowups){.pf-ref} gives successive centers on point
blowups. If one of them becomes the generic point of the exceptional curve,
step [](#divisorial-center-type-two){.pf-ref} gives type (2). If this never happens, every center remains closed
and steps [](#union-contained-in-r){.pf-ref}, [](#element-eventually-regular){.pf-ref} and [](#r-equals-union-type-three){.pf-ref} give type (3).

These alternatives exhaust all possibilities for points on the exceptional
curve of a nonsingular surface.
:::

:::

::: pf-qed
Steps [](#unique-center-exists){.pf-ref}, [](#center-not-generic-point){.pf-ref}, [](#codim-one-center-type-one){.pf-ref}, [](#successive-centers-on-blowups){.pf-ref} and [](#divisorial-center-type-two){.pf-ref} give the first two valuation types from their centers on
successive smooth models. Steps [](#union-contained-in-r){.pf-ref}, [](#element-eventually-regular){.pf-ref} and [](#r-equals-union-type-three){.pf-ref} prove the infinite-center case
and the essential equality $R=R_0$ using Exercise V.5.1. Step [](#trichotomy-established){.pf-ref} assembles
the exhaustive trichotomy, with the trivial valuation ring $K$ separately
excluded exactly as in Exercise II.4.12.
:::

:::
:::

::: {.remark title="Published solutions"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.5, exercise 5.6, printed p. 420. Exercise II.4.12, printed p. 108, builds the ring $R_0=\bigcup_i\OO_{x_i,X_i}$ of the third kind, shows that it is a local ring dominated by some valuation ring of $K/k$, and its Note after the exercise defers to the present one both that $R_0$ is itself a valuation ring and that every valuation ring of $K/k$ is one of the three kinds.

Kinds (1) and (2) are published twice. Yang Pi-Yeh, *Hartshorne Solutions*, solution 5.5.6, printed p. 114, and A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.5.6, printed p. 299, argue from the centre: $X$ is projective and therefore proper, so the valuation criterion gives $\varphi:\Spec R\to X$ whose closed-point image is the centre $P$ of $\nu$, and $R$ dominates $\OO_P$; a centre of dimension one leaves two discrete valuation rings, so $R=\OO_P$, which is kind (1); a closed centre is blown up, and the centre on the blowup is either the exceptional curve, which is kind (2), or a point of it, where one repeats. Steps [](#codim-one-center-type-one){.pf-ref} and [](#divisorial-center-type-two){.pf-ref} transcribe that argument.

Kind (3) is proved above by the route the printed hint names, with Exercise V.5.1: for $f\in R$ the rational map $[f:1]$ is resolved by point blowups, and comparing the centres of $\nu$ along that resolution with the rings $\OO_{X_i,x_i}$ places $f$ in some $A_i$ (step [](#element-eventually-regular){.pf-ref}); with $R_0\subseteq R$ (step [](#union-contained-in-r){.pf-ref}) this gives $R=R_0$ (step [](#r-equals-union-type-three){.pf-ref}). What is published for the union itself is S. S. Abhyankar, *On the valuations centered in a local domain*, Amer. J. Math. 78 (1956), pp. 321--348: Definition 3, printed p. 335, defines the first quadratic transform of a regular local domain along a valuation; Lemma 10, printed pp. 334--335, proves that transform a regular local domain of dimension at most that of the domain, with the valuation centred at its maximal ideal; Proposition 3, printed pp. 336--337, proves that a quadratic sequence along a prime divisor is finite; and Lemma 12, printed pp. 337--338, proves of a strictly ascending quadratic sequence of two-dimensional regular local domains that its union is the valuation ring of a valuation centred at the successive maximal ideals and of $R_i$-dimension zero at every stage (part (1)), and that a valuation with those centres is unique (part (2)). Those statements are made for the quadratic transforms of the local domain along the valuation, as Definition 3 defines them.

His Theorem 1, printed p. 330, sorts a valuation centred in an $n$-dimensional local domain by its $R$-dimension $d$, rational rank $r$ and rank $\rho$, with $d+r\le n$, and a valuation of $R$-dimension $n-1$ is real discrete. That is a classification by $(d,r,\rho)$; the three kinds of Exercise II.4.12 are the book's.
:::
