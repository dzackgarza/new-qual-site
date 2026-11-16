---
schema: qual/card@1
id: P-AGH555ELEMTRANSFORM
kind: problem
title: Ruled surfaces over a fixed curve are linked by elementary transformations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.5.5 as transcribed here, the retained Andrew Egbert
    entry, V.2.5 and the ruled-surface section/bundle conventions. The
    retained entry contains only the sentence that this is a consequence of
    its proof of V.2.5(a), while the printed hint proposes first changing the
    invariant e by elementary transformations and then using decomposability
    for e sufficiently large. The proof below verifies the stated
    self-intersection drop but completes the argument directly at the
    equivalent vector-bundle level: an elementary transform is a length-one
    elementary modification 0 -> F -> E -> k(p) -> 0, and two rank-two
    bundles become lattices in one generic two-dimensional vector space.
    After one harmless line-bundle twist their quotient has finite length,
    so a composition series factors the difference into finitely many such
    elementary modifications.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete proof against the ruled-surface quotient convention
    and the local point-blowup model. Checked that for
    F=ker(E->k(p)) one can choose E_p=Re1+Re2 and F_p=Re1+Rt e2, giving the
    rational map [x:y]->[x:ty]; its graph is the blowup at the corresponding
    fibre point and it contracts the strict transform of that fibre. Its
    inverse has the same form, so elementary transformations reverse.
    Checked also that a generic isomorphism E_eta~=E'_eta extends after an
    effective line-bundle twist to an injection with finite-length torsion
    quotient, whose composition series has k(p)-factors; the inverse images
    are torsion-free rank-two sheaves and hence locally free on the smooth
    curve. Thus every step is an elementary transformation and twisting the
    final bundle does not change its projectivization.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The published-solution remark now says what the two located entries contain.
    Egbert's V.5.5 is one sentence, a cross-reference to his V.2.5(a), on printed
    p. 299 of tmp/sources/hartshorne-solutions-egbert.pdf, whose MinerU text
    version tmp/sources/hartshorne-solutions-egbert.md carries the same sentence
    at its line 12794. Yang Pi-Yeh's Solution
    5.5.5 runs on printed pp. 113--114 of
    tmp/sources/lfwin-hartshorne-solutions.pdf: it opens at the foot of p. 113,
    p. 114 opens with the tail of that page's last sentence ("... we may assume
    E and E' are" / "decomposable with E = O_C + L and E' = O_C + L'"), and four
    whole sentences follow it above 5.5.6, which is Hartshorne V.5.6 --- the one
    asserting fraktur-e-tilde = fraktur-e + P "by definition", the one saying "we
    may blow-up X and X' more and assume fraktur-e = fraktur-e'", the one
    concluding X = X', and the last, "So there is a finite sequence of elementary
    transformations which transform X into X'"; its outline is right and three steps
    are missing or
    wrong: the sign of the elementary transform under Hartshorne's e = -deg
    fraktur-e of (2.8.1), the effect of elm_P on the normalized bundle, which he
    asserts "by definition", and the implicit choice of the points whose classes
    must be matched, which needs Riemann-Roch. There is no complete published
    proof of V.5.5 among the retained sets, so the card's own proof carries it
    and the entry in COMPLAINTS.md now says so.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    One sentence of Yang Pi-Yeh's entry, on a reader's report of issue #121,
    re-read on the printed folio of tmp/sources/lfwin-hartshorne-solutions.pdf.
    The event above called the two sentences at the head of p. 114 his last two.
    Read on the rendered page, p. 114 carries the tail of the sentence begun at
    the foot of p. 113 ("... we may assume E and E' are" / "decomposable with
    E = O_C + L and E' = O_C + L'") and then four whole sentences before 5.5.6:
    the "by definition" sentence, "So we may blow-up X and X' more and assume
    fraktur-e = fraktur-e'", "Hence X = X'", and "So there is a finite sequence
    of elementary transformations which transform X into X'". The page range
    pp. 113--114 is unchanged: the entry opens at the foot of p. 113.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The event above first read "p. 114 therefore carries three sentences of his
    entry, not two", and that was still an undercount: p. 114 carries the tail of
    the p. 113 sentence and four whole sentences. Read the same way, the symbols
    he equates are the fraktur divisor class of Hartshorne (2.8.1) and not the
    integer e: the print reads "If L = L(e), for any P in C_0, by definition,
    elm_P X has e-tilde = e + P" and "assume e = e'", with the e's set in
    fraktur, while the p. 113 line above them, "the new ruled surface
    elm_P X has e-tilde = e + 1", is the integer invariant. The remark now quotes
    the fraktur in both places, and its third gap --- that the classes, not the
    integer, are what must be matched --- is the reading the print supports.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The third gap's quotation made verbatim, on a reader's report of issue #121.
    The remark had paraphrased the sentence as "We may blow up X and X' more and
    assume fraktur-e = fraktur-e'"; the print reads "So we may blow-up X and X'
    more and assume fraktur-e = fraktur-e'", with the hyphen in "blow-up", the
    sentence opening with "So", and the fraktur class. Read in
    tmp/sources/lfwin-hartshorne-solutions.md, the sentence is the eighth of
    Solution 5.5.5 and reads "So we may blow-up X and X0 more and assume e = e'",
    the MinerU text version writing the prime of X' as a zero and the fraktur as
    a plain e; the page image of p. 114 has X' and the fraktur. The card now
    quotes the printed reading and records the text version's two renderings. No
    claim of the card changes.

---

::: {.problem}
Let $C$ be a curve, and let $\pi: X \rightarrow C$ and $\pi^{\prime}: X^{\prime} \rightarrow C$ be two geometrically ruled surfaces over $C$.
Show that there is a finite sequence of elementary transformations (5.7.1) which transform $X$ into $X^{\prime}$.

Hints: First show if $D \subseteq X$ is a section of $\pi$ containing a point $P$, and if $\tilde{D}$ is the strict transform of $D$ by $\operatorname{elm}_P$, then $\widetilde{D}^2=D^2-1$.
Next show that $X$ can be transformed into a geometrically ruled surface $X^{\prime \prime}$ with invariant $e \gg 0$.
Then use (2.12), and study how the ruled surface $\PP(\mathcal{E})$ with $\mathcal{E}$ decomposable behaves under $\operatorname{elm}_P$.
:::

::: {.solution}
Choose rank-two locally free sheaves
$$
\mathcal E,\mathcal E'
$$
on $C$ such that
$$
X=\PP(\mathcal E),
\qquad
X'=\PP(\mathcal E').
$$
We use Hartshorne's quotient convention for projective bundles.

::: pf

::: {.pf-step #elementary-transform-as-kernel}
Let $p\in C$, let
$$
q:\mathcal E\otimes k(p)\twoheadrightarrow k(p)
$$
be a one-dimensional quotient, and let
$$
\mathcal F
=
\ker\!\left(
\mathcal E\longrightarrow
\mathcal E\otimes k(p)
\xrightarrow{q}
k(p)
\right).
$$
Then $\mathcal F$ is locally free of rank two, and
$$
\boxed{
\operatorname{elm}_{P}\PP(\mathcal E)
\cong
\PP(\mathcal F),
}
$$
where $P\in\PP(\mathcal E_p)$ is the point represented by $q$.

::: pf-proof
Away from $p$, the inclusion
$$
\mathcal F\hookrightarrow\mathcal E
$$
is an isomorphism. Since $\mathcal F$ is a torsion-free coherent sheaf on
the nonsingular curve $C$, it is locally free.

It remains to identify the birational map near $p$. Let
$$
R=\OO_{C,p}
$$
be the discrete valuation ring, choose a uniformizer $t$, and choose a basis
$e_1,e_2$ of $\mathcal E_p$ such that $q$ is reduction modulo $t$ followed
by projection to the $e_2$-coordinate. Then
$$
\mathcal E_p=Re_1\oplus Re_2,
\qquad
\mathcal F_p=Re_1\oplus Rt e_2.
$$

With quotient coordinates $[x:y]$ on $\PP(\mathcal E)$ and $[u:v]$ on
$\PP(\mathcal F)$, restriction of a quotient of $\mathcal E$ to
$\mathcal F$ gives the rational map
$$
[x:y]\dashrightarrow[x:ty].
$$
The point at which it is undefined is
$$
t=0,\qquad[x:y]=[0:1],
$$
namely $P$.

On the chart $y\ne0$, put
$$
z=x/y.
$$
Then the map is
$$
(t,z)\dashrightarrow[z:t]\in\PP^1.
$$
The closure of its graph is the blowup of the $(t,z)$-plane at the origin.
On that blowup, the strict transform of the old fibre $t=0$ maps to the
single point $[1:0]$, while the exceptional curve maps isomorphically to the
new fibre. Thus the resolved birational map is exactly: blow up $P$ and
contract the strict transform of the fibre through $P$. This is the
elementary transformation of (5.7.1), and its target is $\PP(\mathcal F)$.
:::

:::

::: {.pf-step #inverse-is-elementary-transform}
The inverse of an elementary transformation is again an elementary
transformation.

::: pf-proof
In the local coordinates of step [](#elementary-transform-as-kernel){.pf-ref}, the generic inverse of
$$
[x:y]\dashrightarrow[x:ty]
$$
is
$$
[u:v]\dashrightarrow[tu:v].
$$
On the new fibre $t=0$, this inverse is undefined only at
$$
[u:v]=[1:0].
$$
Resolving it blows up that point and contracts the strict transform of the
new fibre, exactly the same elementary-transformation construction. Hence
the operation is reversible by another elementary transformation.
:::

:::

::: {.pf-step #section-self-intersection-drops}
If $D\subseteq X$ is a section containing the centre $P$ and
$\widetilde D$ is its transform under $\operatorname{elm}_P$, then
$$
\boxed{\widetilde D^{\,2}=D^2-1.}
$$

::: pf-proof
Let
$$
b:Z\longrightarrow X
$$
be the blowup at $P$, with exceptional curve $E$, and let $F$ be the ruling
fibre through $P$. Since $D$ is a section, $D$ and $F$ are smooth and meet
transversely at $P$.

The strict transform $\bar D$ therefore satisfies the usual blowup formula
$$
\bar D^{\,2}=D^2-1.
$$
The strict transforms $\bar D$ and $\bar F$ are disjoint, because the blowup
separates their two tangent directions at $P$.

The elementary transformation next contracts the $(-1)$-curve $\bar F$.
Because $\bar D$ is disjoint from $\bar F$, the contraction is an
isomorphism in a neighbourhood of $\bar D$, and the pullback of its image
$\widetilde D$ is exactly $\bar D$. Hence
$$
\widetilde D^{\,2}
=
\bar D^{\,2}
=
D^2-1.
$$
This is the first calculation requested in the hint.
:::

:::

::: {.pf-step #injective-comparison-map}
Let
$$
K=k(C)
$$
be the function field. After identifying the generic fibres
$$
\mathcal E_\eta
\cong
\mathcal E'_\eta
\cong
K^2,
$$
there is an effective divisor $A$ on $C$ and an injective morphism
$$
\boxed{
\varphi:\mathcal E
\hookrightarrow
\mathcal E'(A)
}
$$
whose cokernel is a finite-length torsion sheaf.

::: pf-proof
Choose any $K$-linear isomorphism
$$
\varphi_\eta:\mathcal E_\eta\xrightarrow{\sim}\mathcal E'_\eta.
$$
Viewed in local trivializations, its matrix entries are rational functions
on $C$. They have only finitely many poles. Choose an effective divisor
$A$ whose multiplicities are large enough to clear all those poles. Then
$\varphi_\eta$ extends to a morphism
$$
\varphi:\mathcal E\longrightarrow\mathcal E'(A).
$$

The map is an isomorphism at the generic point. Its kernel is therefore a
torsion subsheaf of the locally free sheaf $\mathcal E$, hence is zero.
Thus $\varphi$ is injective.

Source and target have the same rank, so the cokernel
$$
\mathcal T=\operatorname{coker}\varphi
$$
has rank zero. On the noetherian projective curve $C$, a coherent rank-zero
sheaf is supported on finitely many closed points and has finite length.
:::

:::

::: {.pf-step #composition-series-of-torsion}
There are rank-two locally free sheaves
$$
\mathcal F_0,\mathcal F_1,\ldots,\mathcal F_N
$$
with
$$
\mathcal F_0=\mathcal E'(A),
\qquad
\mathcal F_N=\mathcal E,
$$
such that for every $0\le i<N$ there is an exact sequence
$$
\boxed{
0
\longrightarrow
\mathcal F_{i+1}
\longrightarrow
\mathcal F_i
\longrightarrow
k(p_i)
\longrightarrow
0
}
$$
for some point $p_i\in C$.

::: pf-proof
The finite-length torsion sheaf
$$
\mathcal T=\mathcal E'(A)/\mathcal E
$$
from step [](#injective-comparison-map){.pf-ref} has a composition series
$$
\mathcal T=\mathcal T_0
\supset
\mathcal T_1
\supset
\cdots
\supset
\mathcal T_N=0
$$
whose successive quotients are simple torsion sheaves. Since the ground
field is algebraically closed, every such simple quotient is
$$
\mathcal T_i/\mathcal T_{i+1}\cong k(p_i)
$$
for some closed point $p_i$.

Let $\mathcal F_i$ be the inverse image of $\mathcal T_i$ under
$$
\mathcal E'(A)\twoheadrightarrow\mathcal T.
$$
Then
$$
\mathcal F_0=\mathcal E'(A),
\qquad
\mathcal F_N=\mathcal E,
$$
and the successive quotients are the displayed skyscraper sheaves.

Each $\mathcal F_i$ is a torsion-free coherent sheaf of rank two on the
nonsingular curve $C$, hence is locally free of rank two.
:::

:::

::: {.pf-step #each-step-is-elementary-transform}
For every $0\le i<N$,
$$
\PP(\mathcal F_{i+1})
$$
is obtained from
$$
\PP(\mathcal F_i)
$$
by one elementary transformation.

::: pf-proof
The quotient in step [](#composition-series-of-torsion){.pf-ref},
$$
\mathcal F_i\twoheadrightarrow k(p_i),
$$
induces a nonzero one-dimensional quotient of the fibre
$$
\mathcal F_i\otimes k(p_i).
$$
Let
$$
P_i\in\PP((\mathcal F_i)_{p_i})
$$
be the corresponding point. By construction,
$$
\mathcal F_{i+1}
=
\ker\bigl(\mathcal F_i\to k(p_i)\bigr).
$$
Step [](#elementary-transform-as-kernel){.pf-ref} therefore gives
$$
\operatorname{elm}_{P_i}\PP(\mathcal F_i)
\cong
\PP(\mathcal F_{i+1}).
$$
:::

:::

::: {.pf-step #finite-sequence-to-twisted-target}
There is a finite sequence of elementary transformations taking
$$
\PP(\mathcal E)
$$
to
$$
\PP(\mathcal E'(A)).
$$

::: pf-proof
Step [](#each-step-is-elementary-transform){.pf-ref} gives a finite sequence
$$
\PP(\mathcal E'(A))
=
\PP(\mathcal F_0)
\dashrightarrow
\PP(\mathcal F_1)
\dashrightarrow
\cdots
\dashrightarrow
\PP(\mathcal F_N)
=
\PP(\mathcal E),
$$
in which every arrow is an elementary transformation.

By step [](#inverse-is-elementary-transform){.pf-ref}, every arrow can be reversed by another elementary
transformation. Reversing the finite sequence therefore gives elementary
transformations from $\PP(\mathcal E)$ to $\PP(\mathcal E'(A))$.
:::

:::

::: {.pf-step #twist-invariance-of-projective-bundle}
Twisting by a line bundle does not change a projective bundle:
$$
\boxed{
\PP(\mathcal E'(A))
\cong
\PP(\mathcal E')
}
$$
over $C$.

::: pf-proof
For every $C$-scheme $T$, tensoring with the pullback of $\OO_C(A)$ gives a
bijection between invertible quotients of $\mathcal E'_T$ and invertible
quotients of
$$
\mathcal E'_T\otimes\OO_T(A).
$$
This identifies the two projective-bundle functors and hence gives an
isomorphism
$$
\PP(\mathcal E')
\xrightarrow{\sim}
\PP(\mathcal E'(A)).
$$
Equivalently, this is the standard identity
$$
\PP(\mathcal E'\otimes\mathcal L)\cong\PP(\mathcal E')
$$
for an invertible sheaf $\mathcal L$.
:::

:::

::: {.pf-step #full-sequence-x-to-xprime}
There is a finite sequence of elementary transformations transforming
$X$ into $X'$:
$$
\boxed{
X=\PP(\mathcal E)
\dashrightarrow
\cdots
\dashrightarrow
\PP(\mathcal E'(A))
\cong
\PP(\mathcal E')=X'.
}
$$

::: pf-proof
Step [](#finite-sequence-to-twisted-target){.pf-ref} supplies the finite elementary-transformation sequence from
$\PP(\mathcal E)$ to $\PP(\mathcal E'(A))$, and step [](#twist-invariance-of-projective-bundle){.pf-ref} identifies the
latter ruled surface over $C$ with $X'$. Thus the two given geometrically
ruled surfaces are connected by finitely many elementary transformations.
:::

:::

::: pf-qed
Steps [](#elementary-transform-as-kernel){.pf-ref}, [](#inverse-is-elementary-transform){.pf-ref} and [](#section-self-intersection-drops){.pf-ref} identify the geometric elementary transformation with a
length-one modification of the defining rank-two bundle and verify the
self-intersection calculation from the hint. Steps [](#injective-comparison-map){.pf-ref}, [](#composition-series-of-torsion){.pf-ref} and [](#each-step-is-elementary-transform){.pf-ref} factor the
difference between the two bundles into finitely many such modifications,
and steps [](#finite-sequence-to-twisted-target){.pf-ref}, [](#twist-invariance-of-projective-bundle){.pf-ref} and [](#full-sequence-x-to-xprime){.pf-ref} reverse the resulting chain and remove the harmless
line-bundle twist.
:::

:::
:::

::: {.remark title="Published solutions"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.5, exercise 5.5, printed p. 419, text version `tmp/sources/hartshorne-1977-algebraic-geometry.md` (printed page = its marker minus 15).

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.5.5, printed p. 299 of
`tmp/sources/hartshorne-solutions-egbert.pdf`, read in its MinerU text version
`tmp/sources/hartshorne-solutions-egbert.md` (entry `5.5.6` at line 12786; printed folio = PDF page
number) --- his numbering is one ahead, so his "5.5.6" is this
exercise --- says only "Consequence of my proof of exc V.2.5.a". That is a cross-reference, not a proof.

Yang Pi-Yeh, *Hartshorne Solutions*, Solution 5.5.5, printed pp. 113--114 of
`tmp/sources/lfwin-hartshorne-solutions.pdf`, read in `tmp/sources/lfwin-hartshorne-solutions.md` --- the
entry opens at the foot of p. 113; p. 114 opens with the tail of p. 113's last sentence and then
carries the decisive passage, the display
$\tilde{\mathfrak e}=\mathfrak e+P$ and the conclusion "assume $\mathfrak e=\mathfrak e'$. Hence $X\cong X'$",
followed by its final sentence "So there is a finite sequence of elementary transformations
which transform $X$ into $X'$" --- is the nearest published argument, and its outline is the right one. He writes the printed hint's formula
$C'\cdot D'=C\cdot D+ac-a\,\mu_P(D)-c\,\mu_P(C)$ for $C\sim aC_0+bf$ and $D\sim cC_0+df$, which gives
$C'\cdot D'=C\cdot D-1$ when $a=c=1$ and $P\in C\cap D$; hence $\operatorname{elm}_P X$ at $P\in C_0$ has invariant
$e+1$, and finitely many such transformations make $e,e'>2g-2$. There (2.12)(b) makes both bundles
decomposable, $\mathcal E=\OO_C\oplus\mathcal L$ and $\mathcal E'=\OO_C\oplus\mathcal L'$, and further
transformations at points of $C_0$ change the divisor class $\mathfrak e$ of $\mathcal L$ by the class of
the underlying point of $C$; since those points range over $C$, the classes $\mathfrak e$ and
$\mathfrak e'$ can be made equal, after which $\mathcal E\cong\mathcal E'$ and $X\cong X'$. As printed the
entry has three gaps, and they are the three points a reader of it would have to supply.

First, the sign. Notation (2.8.1) sets $e=-\deg\mathfrak e$, where $\mathfrak e$ is the divisor class with
$\mathcal L(\mathfrak e)\cong\bigwedge^2\mathcal E$; the elementary transform replaces $\mathcal E$ by the
kernel of $\mathcal E\to k(P)$, whose determinant is $(\bigwedge^2\mathcal E)(-P)$, so
$$\mathfrak e\longmapsto\mathfrak e-P,$$
not $\mathfrak e+P$ as he writes. With the sign of (2.8.1) that gives $e\mapsto e+1$, the drop the hint
shows, while his $+P$ would give $e-1$.

Second, his step "for any $P\in C_0$, by definition, $\operatorname{elm}_P X$ has
$\tilde{\mathfrak e}=\mathfrak e+P$" asserts the effect on the normalized bundle instead of proving it. The
computation is the card's step [](#elementary-transform-as-kernel){.pf-ref}: with $P\in C_0$ lying over
$q\in C$, the kernel of $\mathcal E\to k(P)$ is $\OO_C\oplus\mathcal L(-q)$, so the splitting survives the
transformation and only the class of the second summand drops by $q$; the new section, the transform of
$C_0$, is the image of $\mathcal L(-q)$ and has normal bundle $\mathcal L(-q)$, of degree $-e-1$, which is
the self-intersection calculation of step [](#section-self-intersection-drops){.pf-ref}.

Third, the choice of divisors is implicit. His sentence is, verbatim, "So we may blow-up $X$ and $X'$ more and
assume $\mathfrak e=\mathfrak e'$" (printed p. 114; the MinerU text version writes the second surface as
"X0", its rendering of the prime), and it is not
enough: what must be made equal are the classes, and a transformation at $P$ over $q$ subtracts the class
of $q$, so after $m$ of them at points over $q_1,\dots,q_m$ the class is $\mathfrak e-A$ with
$A=q_1+\dots+q_m$ effective, and likewise $\mathfrak e'-A'$. The classes agree exactly when
$A-A'=\mathfrak e-\mathfrak e'$, which is solvable because the degree of $A$ may be chosen freely and every
class of degree $\ge2g-1$ on a curve of genus $g$ is effective, by Riemann--Roch; Yang states neither the
equation nor the effectivity. With those three steps supplied his argument is complete, and none of them
is in his text, so this card's obligation under issue #121 is not discharged by it. The proof above is
independent of his: it works at the level of the bundles, from a generic isomorphism to a composition
series of the cokernel, and takes from the printed hints only the self-intersection drop
(step [](#section-self-intersection-drops){.pf-ref}) and the reduction to a finite sequence at the end.
:::
