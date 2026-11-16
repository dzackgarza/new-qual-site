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
:::

:::

::: {.pf-step #quadratic-sequence}
If no centre becomes divisorial, the rings
$$
A_i=\OO_{X_i,x_i}
$$
form a strictly ascending sequence of two-dimensional regular local
domains with quotient field $K$, and $A_{i+1}$ is the first quadratic
transform of $A_i$ along the valuation of $R$.

::: pf-proof
Every $x_i$ is a closed point of the nonsingular surface $X_i$, so $A_i$ is
a two-dimensional regular local domain with quotient field $K$.

Write $\mathfrak m_i$ for the maximal ideal of $A_i$ and $\nu$ for the
valuation of $R$. The blowup
$$
\pi_{i+1}:X_{i+1}\longrightarrow X_i
$$
is an isomorphism over $X_i\smallsetminus\{x_i\}$, so
$$
A_i\subseteq A_{i+1}.
$$
The inclusion is strict. Choose a minimal basis $u,v$ of $\mathfrak m_i$
with
$$
\nu(u)\le\nu(v).
$$
Then $\nu(v/u)\ge0$, so $v/u$ is regular at the centre $x_{i+1}$ of $\nu$
on $X_{i+1}$, and
$$
v/u\in A_{i+1}.
$$
On the other hand $v/u\notin A_i$: from $v/u=c\in A_i$ one gets $v=uc$ with
$c\notin\mathfrak m_i$, since $v\notin\mathfrak m_i^2$, so $c$ is a unit and
$(u,v)=(u)$, contrary to $u,v$ being a minimal basis.

Abhyankar defines the first quadratic transform of $A_i$ along $\nu$ to be
$$
A_i[x_2/x_1]_{P},
$$
where $x_1,x_2$ is a minimal basis of $\mathfrak m_i$ with
$\nu(x_1)\le\nu(x_2)$ and $P$ is the contraction of
$\mathfrak m_\nu$ (Definition 3, printed p. 335); by Lemma 10, printed
pp. 334--335, that ring is the local ring of the centre of $\nu$ on the
blowup of $\Spec A_i$ at $\mathfrak m_i$. With $x_1=u$ and $x_2=v$, it is
$A_{i+1}$.
:::

:::

::: {.pf-step #union-is-valuation-ring}
The union
$$
S=\bigcup_{i\ge0}A_i
$$
is the valuation ring of a valuation $\nu'$ of $K$ which has centre
$\mathfrak m_i$ in $A_i$ for every $i$ and is of $A_i$-dimension zero
there.

::: pf-proof
This is Abhyankar's Lemma 12(1), printed p. 337, whose argument runs as
follows. Suppose that $S$ is not a valuation ring. Then Lemma 7, printed
p. 332, supplies a valuation $w$ of $K$ with centre $\mathfrak m_i$ in
$A_i$ and of positive $A_i$-dimension for every $i$. By Theorem 1, printed
p. 330, such a $w$ has $A_0$-dimension $\dim A_0-1=1$, that is, it is a
prime divisor for $A_0$; and Proposition 3, printed pp. 336--337, says
that the quadratic sequence along a prime divisor is finite, whereas
$A_0\subsetneq A_1\subsetneq\cdots$ is infinite. So $S$ is the valuation
ring $R_{\nu'}$ of a valuation $\nu'$ of $K$.

Its maximal ideal is
$$
\mathfrak m_{\nu'}=\bigcup_{i\ge0}\mathfrak m_i
$$
(loc. cit.). Since $A_j$ dominates $A_i$ for $j\ge i$, one has
$$
A_i\cap\mathfrak m_j=\mathfrak m_i
$$
for $j\ge i$, so
$$
A_i\cap\mathfrak m_{\nu'}
=
\bigcup_{j\ge i}(A_i\cap\mathfrak m_j)
=
\mathfrak m_i,
$$
and $\nu'$ has centre $\mathfrak m_i$ in $A_i$. Again by Proposition 3
with Theorem 1, the $A_i$-dimension of $\nu'$ is zero for every $i$.
:::

:::

::: {.pf-step #union-equals-r}
$$
\boxed{R=S=\bigcup_{i\ge0}A_i,}
$$
so $R$ is of type (3) in Exercise II.4.12, and the local ring $R_0$ of the
third construction there is itself a valuation ring.

::: pf-proof
Every $A_i$ is contained in $R$, because $R$ dominates $A_i$, so
$$
S\subseteq R.
$$

Conversely $\nu$ has centre $\mathfrak m_i$ in $A_i$ for every $i$, and
Abhyankar's Lemma 12(2), printed p. 338, says that a valuation of $K$ whose
centre in $A_i$ is $\mathfrak m_i$ for every $i$ is unique. Hence
$\nu=\nu'$, and
$$
R=R_\nu=R_{\nu'}=S.
$$
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
step [](#divisorial-center-type-two){.pf-ref} gives type (2). If this never happens, every center remains closed,
and steps [](#quadratic-sequence){.pf-ref}, [](#union-is-valuation-ring){.pf-ref} and [](#union-equals-r){.pf-ref} give type (3).

These alternatives exhaust all possibilities for points on the exceptional
curve of a nonsingular surface.
:::

:::

::: pf-qed
Steps [](#unique-center-exists){.pf-ref}, [](#center-not-generic-point){.pf-ref}, [](#codim-one-center-type-one){.pf-ref}, [](#successive-centers-on-blowups){.pf-ref} and [](#divisorial-center-type-two){.pf-ref} give the first two valuation types from their centers on
successive smooth models. Steps [](#quadratic-sequence){.pf-ref}, [](#union-is-valuation-ring){.pf-ref} and [](#union-equals-r){.pf-ref} prove the infinite-center case
and the identity $R=R_0$, through Abhyankar's quadratic transforms. Step [](#trichotomy-established){.pf-ref} assembles
the exhaustive trichotomy, with the trivial valuation ring $K$ separately
excluded exactly as in Exercise II.4.12.
:::

:::
:::

::: {.remark title="Published solution"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.5, exercise 5.6, printed p. 420, text version `tmp/sources/hartshorne-1977-algebraic-geometry.md` (printed page = its marker minus 15). Exercise II.4.12, printed p. 108, builds the ring $R_0=\bigcup_i\OO_{x_i,X_i}$ of the third kind, shows only that it is a local ring dominated by some valuation ring of $K/k$, and its Note after the exercise defers to the present one both that $R_0$ is itself a valuation ring and that every valuation ring of $K/k$ is one of the three kinds.

The classification is Abhyankar's. S. S. Abhyankar, *On the valuations centered in a local domain*, Amer. J. Math. 78 (1956), pp. 321--348, text version `tmp/sources/abhyankar-1956-valuations-centered-local-domain.md` (printed page = its PDF page plus 320): Theorem 1, printed p. 330, sorts a valuation centred in an $n$-dimensional local domain by its $R$-dimension $d$, rational rank $r$ and rank $\rho$, with $d+r\le n$, and a valuation of $R$-dimension $n-1$ is real discrete; Definition 3, printed p. 335, defines the quadratic transforms of $R$ along the valuation, and Lemma 10, printed pp. 334--335, identifies each with the local ring of the centre of the valuation on the corresponding blowup; Proposition 3, printed pp. 336--337, proves that the quadratic sequence along a prime divisor is finite and ends in the valuation ring of the valuation itself; and Lemma 12, printed pp. 337--338, proves that a strictly ascending quadratic sequence of two-dimensional regular local domains has a valuation ring as its union, that this is the only valuation centred at the successive maximal ideals, and that it is of $R_i$-dimension zero at every stage. Steps [](#quadratic-sequence){.pf-ref}, [](#union-is-valuation-ring){.pf-ref} and [](#union-equals-r){.pf-ref} transcribe that proof for the third kind, and $R=R_0$ is its Lemma 12(2) applied to the given valuation ring.

The book's hint proposes a second route to the inclusion $R\subseteq R_0$, by resolving $[f:1]$ with Exercise V.5.1 for each $f\in R$; the proof above takes the published route instead.

Two entries of the Hartshorne solution sets identify the first two kinds and do not prove the third. Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.5.6, printed p. 114 of that set (`tmp/sources/lfwin-hartshorne-solutions.pdf`, whose folios are its PDF pages; read in `tmp/sources/lfwin-hartshorne-solutions.md`), is A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.5.6, printed p. 299 of that set, text version `tmp/sources/hartshorne-solutions-egbert.md`, with one sentence added. Both argue kinds (1) and (2) through the centre and its successive blowups, as steps [](#codim-one-center-type-one){.pf-ref} and [](#divisorial-center-type-two){.pf-ref} do, and for kind (3) write only
$$R=\varprojlim\OO_{P_i,X_i}=\bigcup_i\OO_{P_i,X_i},$$
an assertion with no argument, in which the limit is also written in the wrong direction: the union is a direct limit along the inclusions $\OO_{P_i,X_i}\into\OO_{P_{i+1},X_{i+1}}$. Neither uses the book's hint, and neither proves $R\subseteq R_0$; that is what step [](#union-is-valuation-ring){.pf-ref} supplies, by Abhyankar's Lemma 12.

:::
