---
schema: qual/card@1
id: P-AGH5413DELPEZZO4
kind: problem
title: The 16 lines on the degree four Del Pezzo surface and its equations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Blowups
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.13, the retained Egbert solution, the degree-four
    Del Pezzo blowup model from V.4.7, and the immediately preceding Kodaira
    vanishing exercise V.4.12. Cross-checked the standard description against
    Dolgachev's treatment of quartic Del Pezzo surfaces. The 16 displayed
    lines are the five exceptional curves, ten transforms of pairwise joining
    lines, and the transform of the conic through all five points. For the
    equations, Riemann--Roch and V.4.12 give h^0(-2K_X)=13, so at least two
    independent quadrics contain the anticanonical image; their degree-four
    complete intersection must equal the degree-four surface X.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Dolgachev read for issue #121, and part (b) left open. In M. I. Dolgachev,
    Topics in Classical Algebraic Geometry (27 September 2010), the complete
    524-page book in tmp/sources/dolgachev-topics-classical-ag.pdf and its MinerU
    text version tmp/sources/dolgachev-topics-classical-ag.md, with printed
    page = PDF page minus ten, Theorem 8.5.1, printed p. 291 with the proof on
    pp. 291--292, proves that an anticanonical model of a weak Del Pezzo surface
    of degree 4 is projectively normal (his Theorem 8.4.5, printed p. 280), that
    h^0(O_X(2)) = 13 (his Lemma 8.3.1, printed p. 272), and that the two
    quadrics of the pencil can be put in the diagonal form sum t_i^2 =
    sum a_i t_i^2 with distinct a_i. Read closely, the proof jumps from the
    dimension count 15 - 13 = 2 to "X is the base locus of a pencil" and then
    uses the base locus as X: it does not show that the two quadrics have no
    common component, nor that the degree-4 complete intersection is X. That is
    the same gap as Egbert's entry, so part (b) stays open on the card's own
    steps quadrics-no-common-component and x-is-complete-intersection, and the
    remark now cites Dolgachev for exactly what he proves. Part (a) is not in his
    book: printed p. 293 uses "the 16 lines on X" without proving the count.
    Egbert's V.4.13, printed pp. 292--294, does settle part (a) modulo one step,
    the adjunction derivation of C^2 = -1 for a line; his other defect is Pic X
    written Z^6 with generators l, e_1, ..., e_6 for a five-point blow-up.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Correction on a reader's report of issue #121: the event above first read
    "Part (b) closed on a published proof", which was wrong, and it also
    attributed the Lazarsfeld citation for Ramanujam's vanishing theorem to
    Lemma 8.3.1, and claimed Egbert's part (a) does not exclude other classes.
    Dolgachev's Lemma 8.3.1 invokes Ramanujam's vanishing theorem by name without
    a reference; the reference to Lazarsfeld, Positivity in Algebraic Geometry I,
    Theorem 4.3.1, is in the proof of his Lemma 8.1.4, printed p. 248. Egbert's
    part (a) does reduce a line to the F_ij and the conic by Schwarz on
    sum b_i = 3a - 1 and sum b_i^2 = a^2 + 1, as the remark now says. Part (b) is
    reopened.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Three citation repairs on a second reader's report of issue #121, each
    re-read in the sources here. (i) The text version of Dolgachev now exists:
    tmp/sources/dolgachev-topics-classical-ag.md is a MinerU extraction of all
    524 PDF pages, marked in blocks of twenty ("PDF pages 301-320" opens at PDF
    p. 301, which is printed p. 291, where Theorem 8.5.1 stands), and it is
    cited beside the PDF here and in the remark.
    (ii) Egbert's V.4.13 entry is printed pp. 292--294, not pp. 292--293: his
    heading "V.4.13 16 Lines" and the intersection theory of the blow-up stand on
    p. 292, the Schwarz count on p. 293, and p. 293 ends with the dimension count
    begun there; p. 294 opens "Note that by Ramanujam vanishing and Serre
    duality, H^1(X, O_X(-2K_X)) = 0." and closes the entry with "Now use star.",
    the star being the one attached on p. 293 to
    "O_X(-2K_X) = O_X(2)  star by tensoring the same thing on both sides". So the
    count 13 is completed on p. 294 by that identification and that vanishing,
    "15 - 13 = 2" is printed nowhere, and the conclusion is never drawn. The
    vanishing is Ramanujam's, named with no reference --- the defect this card's
    remark charges to Dolgachev. Read on the rendered page of
    tmp/sources/hartshorne-solutions-egbert.pdf, whose printed folio is its PDF
    page number: the text version tmp/sources/hartshorne-solutions-egbert.md,
    which was not in the tree when this event was written, is cited in the
    event below.
    (iii) The event above said Egbert's part (a) runs "by Schwarz with
    sum b_i = sum b_i^2"; that equation is not his input. He derives
    sum b_i = 3a - 1 and sum b_i^2 = a^2 + 1 from degree and self-intersection,
    applies (sum b_i)^2 <= 5 sum b_i^2, and gets 4a^2 - 6a - 4 <= 0, whence
    a is 1 or 2; sum b_i = sum b_i^2 = 2 at a = 1 and = 5 at a = 2 are
    consequences used to pin the multiplicities. The event now says so.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Two readings corrected on a reader's report of issue #121, both re-read on
    the rendered page of tmp/sources/hartshorne-solutions-egbert.pdf (its printed
    folio is its PDF page number) and of
    tmp/sources/dolgachev-topics-classical-ag.md. (i) The block marker "PDF pages
    301-320" does not open printed p. 301: it opens PDF p. 301, which is printed
    p. 291, and Theorem 8.5.1 stands at its head. (ii) Egbert's "Now use star."
    is not a truncated dimension count. p. 293 carries, in order, the
    identification "O_X(-2K_X) = O_X(2)  star by tensoring the same thing on both
    sides", the sequence 0 -> H^0(I_X(2)) -> H^0(O(2)) -> H^0(O_X(2)) -> 0, the
    count h^0(O(2)) = 15 and the Riemann-Roch count h^0(-2K_X) - h^1(-2K_X) = 13;
    p. 294 opens "Note that by Ramanujam vanishing and Serre duality,
    H^1(X,O_X(-2K_X)) = 0." and ends the entry "Now use star.", the star being
    that identification. So the count closes on p. 294 through that vanishing, and
    "15 - 13 = 2" appears nowhere: the entry never writes h^0(I_X(2)) = 2 nor draws
    the conclusion. The vanishing is Ramanujam's, named without a reference, which
    is exactly what this card's remark charges to Dolgachev's Lemma 8.3.1. The
    remark and the entry in COMPLAINTS.md now say all of this; the card's own
    steps, and part (b)'s opening on the card's own proof, are unchanged.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Egbert's text version now exists and is cited. tmp/sources/hartshorne-
    solutions-egbert.md is a MinerU extraction of all 304 PDF pages, marked in
    blocks of twenty ("PDF pages 281-300" opens at PDF p. 281), and since his
    printed folio is his PDF page number the printed page of an entry can be
    read off those markers; 5.4.13 (V.4.12) is the entry printed at p. 292 and
    5.4.14 (V.4.13(b)) the one at p. 293. Read there, the V.4.13 entry agrees
    with the rendered page on every point of substance stated in the events
    above: "Pic X ~ Z^6 generated by l, e_1, ..., e_6", the Schwarz count
    4a^2 - 6a - 4 <= 0 with a = 1 and a = 2, the identification
    "O_X(-2K_X) = O_X(2)" and the count h^0 = 13. On the symbol: the copy
    read here (13040 lines) rendered the star of pp. 293--294 as "?" at line
    12563, "Now use ?."; the extraction was regenerated at 21:36 (13038 lines)
    and line 12563 now reads "Now use *.", so the star is carried. Either way
    the closing step's reference is to that identification, and a symbol is
    still read off the page image. Nothing else on these pages differs. The
    remark cites the text version beside the PDF.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Part (b) closed for issue #121 on a published proof that carries the
    decisive step: M. Riman, The Vanishing of the Brauer Group of a del Pezzo
    Surface of Degree 4, PhD dissertation, University of Washington, 2019,
    Theorem 2.2.7, stated on printed p. 19 and proved on printed pp. 20-21
    (printed page = PDF page minus 7; saved as
    tmp/sources/riman-2019-del-pezzo-degree-four.pdf). Read in a pdftotext
    extraction of that PDF, used as a page locator. The steps of the card are
    its proof: h^0(X,O(-2K_X)) = 13 from Riemann-Roch with Kodaira vanishing
    (his (2.2) at m = -2, K^2 = 4); h^0(I_X(2)) >= 15 - 13 = 2 from the
    standard exact sequence; and X = Q cap Q' from deg X = 4 = deg(Q cap Q').
    Two of its passages are garbled and the card records the repairs: the
    exclusion of a reducible quadric, which it does through "Klein's theorem"
    and with "since Q is assumed to be irreducible" written where the argument
    needs the opposite, and the closing degree count, which is asserted. His
    Lemma 2.2.8, printed pp. 19-20, gives the nondegeneracy used in the first
    repair, |-K_X| separating points and tangent vectors. Checked against
    Hartshorne V.4.13(b), printed p. 424 with the construction of X in (4.7),
    printed p. 416: the exercise's X is the anticanonical model of the
    five-point blow-up, so O_X(1) = O_X(H) = O_X(-K_X) and the RR input
    K^2 = 9 - 5 = 4 is the book's. Also read for this card: Dolgachev, Topics in
    Classical Algebraic Geometry, Theorem 8.5.1, printed pp. 291-292, which
    stops at "X is the base locus of a pencil" and is recorded in the remark;
    Yang Pi-Yeh's 5.4.13(b), printed p. 111, which reaches h^0(I_X(2)) = 2 the
    same way but needs the surjectivity of H^0(O_P4(2)) -> H^0(O_X(2)), which
    it does not prove, and then states the conclusion without the degree
    count; and Egbert, whose V.4.13 closes part (b) only through a star.
---

::: {.problem}
Let $X$ be the Del Pezzo surface of degree 4 in $\PP^4$ obtained by blowing up 5 points of $\PP^2$ (4.7).

(a) Show that $X$ contains 16 lines.

(b) Show that $X$ is a complete intersection of two quadric hypersurfaces in $\PP^4$ (the converse follows from (4.7.1)).
:::

::: {.solution}
Let
$$
\pi:X\longrightarrow\PP^2
$$
be the blowup of the five points $P_1,\ldots,P_5$ in general position. Write
$L$ for the pullback of a line and $E_i$ for the exceptional curves. The
anticanonical embedding of (4.7) is given by
$$
H=-K_X=3L-E_1-\cdots-E_5,
\qquad
H^2=4.
$$

::: pf

::: {.pf-step #exceptional-curves-lines}
The five exceptional curves $E_i$ are lines in the anticanonical
embedding.

::: pf-proof
The intersection form on the blowup is
$$
L^2=1,
\qquad
L\cdot E_i=0,
\qquad
E_i\cdot E_j=0\ (i\ne j),
\qquad
E_i^2=-1.
$$
Hence
$$
H\cdot E_i=1.
$$
Each $E_i\cong\PP^1$, and the very ample divisor $H$ embeds it as a curve of
degree one in $\PP^4$. Thus every $E_i$ is a line on $X$.
:::

:::

::: {.pf-step #pairwise-join-lines}
For every pair $1\le i<j\le5$, the strict transform of the line through
$P_i$ and $P_j$ is a line on $X$.

::: pf-proof
Because the five points are in general position, the line through $P_i,P_j$
contains none of the other three points. Its strict transform $L_{ij}$ has
class
$$
L-E_i-E_j.
$$
Therefore
$$
H\cdot L_{ij}
=(3L-E_1-\cdots-E_5)\cdot(L-E_i-E_j)
=3-1-1
=1.
$$
The curve $L_{ij}$ is isomorphic to $\PP^1$, so the anticanonical embedding
maps it to a line. There are
$$
\binom52=10
$$
such curves.
:::

:::

::: {.pf-step #conic-transform-line}
The strict transform of the conic through $P_1,\ldots,P_5$ is a line
on $X$.

::: pf-proof
Five points in general position determine a unique conic $Q$. It is
irreducible: if it were the union of two lines, one of those lines would
contain at least three of the five points, contrary to general position.
Thus $Q$ is a nonsingular conic and its strict transform $\widetilde Q$ has
class
$$
2L-E_1-\cdots-E_5.
$$
Consequently
$$
H\cdot\widetilde Q=6-5=1.
$$
Since $\widetilde Q\cong\PP^1$, it is mapped to a line by the anticanonical
embedding.
:::

:::

::: {.pf-step #sixteen-lines-total}
The surface $X$ contains 16 distinct lines.

::: pf-proof
Steps [](#exceptional-curves-lines){.pf-ref}, [](#pairwise-join-lines){.pf-ref} and [](#conic-transform-line){.pf-ref} give respectively
$$
5,
\qquad
10,
\qquad
1
$$
lines. Their divisor classes are respectively
$$
E_i,
\qquad
L-E_i-E_j,
\qquad
2L-E_1-\cdots-E_5,
$$
so they are distinct. Hence $X$ contains
$$
\boxed{5+10+1=16}
$$
lines, and by step [](#no-other-lines){.pf-ref} no further one. This proves part (a).
:::

:::

::: {.pf-step #no-other-lines}
Every line of $X$ is one of the $16$ listed in step [](#sixteen-lines-total){.pf-ref}.

::: pf-proof
A line $C\subseteq X$ satisfies $H\cdot C=1$ and $p_a(C)=0$, so adjunction
with $K_X=-H$ gives
$$
-2=C\cdot(C+K_X)=C^2-H\cdot C=C^2-1,
\qquad\text{hence}\qquad
C^2=-1 .
$$
Write $C\sim aL-\sum_ib_ie_i$. If $C$ is one of the exceptional curves then
$C\sim E_i$. Otherwise $C$ is the strict transform of an irreducible plane
curve of degree $a>0$ with multiplicity $b_i\ge0$ at $P_i$, so
$$
3a-\sum_i b_i=H\cdot C=1,
\qquad
a^2-\sum_i b_i^2=C^2=-1 .
$$
Cauchy--Schwarz for the five numbers $b_1,\ldots,b_5$ gives
$$
(3a-1)^2=\Bigl(\sum_i b_i\Bigr)^2\le5\sum_i b_i^2=5(a^2+1),
$$
that is $4a^2-6a-4\le0$, so $a\in\{1,2\}$ because $a>0$ is an integer.

If $a=1$, then $\sum b_i=2$ and $\sum b_i^2=2$, so exactly two of the $b_i$
equal $1$ and the rest vanish; then $C\sim L-E_i-E_j=L_{ij}$.

If $a=2$, then $\sum b_i=5$ and $\sum b_i^2=5$, whence
$$
\sum_i b_i(b_i-1)=\sum_i b_i^2-\sum_i b_i=0 .
$$
Each $b_i\ge0$ is an integer, so $b_i(b_i-1)\ge0$ with equality only for
$b_i\in\{0,1\}$; thus all five multiplicities equal $1$ and
$C\sim 2L-\sum_ie_i=\widetilde Q$.

Finally, two distinct irreducible curves never have equal class on a smooth
surface, because their intersection number would then be the negative number
$C^2=-1$. So each of these $16$ classes carries exactly one line, and there
are no others.
:::

:::

::: {.pf-step #h0-two-h-thirteen}
One has
$$
\boxed{h^0(X,\OO_X(2H))=13.}
$$

::: pf-proof
The surface $X$ is rational, so
$$
\chi(\OO_X)=1.
$$
Riemann--Roch on a nonsingular projective surface gives, for $D=2H=-2K_X$,
$$
\begin{aligned}
\chi(\OO_X(2H))
&=\chi(\OO_X)+\frac12(2H)\cdot(2H-K_X)\\
&=1+\frac12(2H)\cdot3H\\
&=1+3H^2\\
&=13.
\end{aligned}
$$

By Serre duality,
$$
H^2(X,\OO_X(2H))
\cong
H^0(X,\OO_X(K_X-2H))^*
=H^0(X,\OO_X(-3H))^*
=0,
$$
because $H$ is ample. Also
$$
H^1(X,\OO_X(2H))
\cong
H^1(X,\OO_X(-3H))^*
=0
$$
by [[P-AGH5412KODAIRAVANISH|Exercise V.4.12]], applied to the ample divisor
$3H$. Thus $h^0(X,\OO_X(2H))=\chi(\OO_X(2H))=13$.

This is the published computation: M. Riman, *The Vanishing of the Brauer
Group of a del Pezzo Surface of Degree 4* (University of Washington, 2019),
Theorem 2.2.7, in the proof on printed p. 20, obtains $h^0(X,-2\omega_X)=13$
from his Riemann--Roch formula (2.1) with $m=-2$ and $K_X^2=4$.
:::

:::

::: {.pf-step #two-quadrics-contain-x}
At least two linearly independent quadric hypersurfaces of $\PP^4$
contain $X$.

::: pf-proof
The anticanonical embedding satisfies
$$
\OO_X(1)=\OO_X(H),
$$
so restriction of quadratic forms gives a linear map
$$
H^0(\PP^4,\OO_{\PP^4}(2))
\longrightarrow
H^0(X,\OO_X(2H)).
$$
The source has dimension
$$
\binom{4+2}{2}=15,
$$
whereas step [](#h0-two-h-thirteen){.pf-ref} gives dimension $13$ for the target. Hence the kernel has
dimension at least two. Choose linearly independent quadrics
$$
Q_1,Q_2
$$
from this kernel. Then
$$
X\subseteq Q_1\cap Q_2.
$$

The source states the same count as $h^0(X,\mathcal I_X(2))\ge 15-13$, printed
p. 21, and concludes that $X$ lies in the intersection of two linearly
independent quadrics.
:::

:::

::: {.pf-step #quadrics-no-common-component}
The quadrics $Q_1$ and $Q_2$ have no common hypersurface component.

::: pf-proof
If two independent quadrics in $\PP^4$ have a common hypersurface component,
that component is a hyperplane: their equations have a common linear factor.
Thus their intersection is the union of that hyperplane and a codimension-two
linear space. Since the irreducible surface $X$ is contained in this union, it
would be contained in one of those two linear subspaces. This is impossible:
the complete anticanonical linear system embeds $X$ nondegenerately in
$\PP^4$. Hence $Q_1,Q_2$ form a regular sequence and their intersection is a
pure surface complete intersection.

The source excludes a reducible member instead, and its wording is garbled: it
supposes one quadric $Q$ reducible, invokes "Klein's theorem" for a
factorization $X=Q\cap V$ with $V$ a hypersurface, and writes "since $Q$ is
assumed to be irreducible" where the argument needs the opposite (printed
pp. 20--21). The conclusion is the one above: a reducible quadric is a union of
two hyperplanes, an irreducible surface inside that union lies in one of them,
and $X$ is nondegenerate in $\PP^4$.
:::

:::

::: {.pf-step #x-is-complete-intersection}
One has
$$
\boxed{X=Q_1\cap Q_2}
$$
scheme-theoretically.

::: pf-proof
By step [](#quadrics-no-common-component){.pf-ref}, the complete intersection
$$
Y=Q_1\cap Q_2
$$
is a pure two-dimensional scheme of degree
$$
\deg Y=2\cdot2=4.
$$
On the other hand, the degree of the anticanonically embedded surface is
$$
\deg X=H^2=4.
$$
Step [](#two-quadrics-contain-x){.pf-ref} gives $X\subseteq Y$. Since $Y$ is pure of the same dimension as
the irreducible reduced surface $X$, the component of $Y$ supported on $X$
already contributes at least $\deg X=4$ to the degree of $Y$. Equality of the
degrees leaves neither another two-dimensional component nor a nonreduced
multiplicity along $X$. Thus $Y=X$ as schemes.

This is the source's closing step, "So $X=Q\cap Q'$ in $\PP^4$" (printed
p. 21), which rests on the two degrees being $4$; the source leaves the count
of components implicit, and the paragraph above states it.

Therefore $X$ is the complete intersection of two quadric hypersurfaces in
$\PP^4$, proving part (b).
:::

:::

::: pf-qed
Steps [](#sixteen-lines-total){.pf-ref} and [](#no-other-lines){.pf-ref} prove part (a), and steps [](#h0-two-h-thirteen){.pf-ref}, [](#two-quadrics-contain-x){.pf-ref}, [](#quadrics-no-common-component){.pf-ref} and [](#x-is-complete-intersection){.pf-ref} prove part (b).
:::

:::
:::

::: {.remark title="Published solutions"}
M. I. Dolgachev, *Topics in Classical Algebraic Geometry* (27 September 2010), read in
`tmp/sources/dolgachev-topics-classical-ag.pdf` and in its MinerU text version
`tmp/sources/dolgachev-topics-classical-ag.md`, whose printed page is the PDF page minus ten (the text
version marks the PDF pages in blocks of twenty, so a single printed page is located in the PDF), §8.5.1,
Theorem 8.5.1, printed p. 291 with its proof on pp. 291--292, proves part of part (b) and not all of it. What
it proves: an anticanonical model $X$ of a weak Del Pezzo surface of degree $4$ is projectively normal (his
Theorem 8.4.5, printed p. 280) and has $h^0(\OO_X(2))=13$ (his Lemma 8.3.1, printed p. 272), so that
$h^0(\mathcal I_X(2))=15-13=2$ and $X$ lies in a pencil $t_0Q_0+t_1Q_1=0$ of quadrics; that pencil has exactly five
singular members, by the discriminant count, and taking their singular points as coordinate points puts the
two equations in the diagonal form
$$
\sum_{i=0}^{4}t_i^2=\sum_{i=0}^{4}a_it_i^2=0,\qquad a_i\ne a_j\ (i\ne j).
$$
What it does not prove is the step that identifies the surface with the complete intersection. From
$h^0(\OO_{\PP^4}(2))=15$ and $h^0(\OO_X(2))=13$ it concludes "This implies that $X$ is the base locus of a
pencil $t_0Q_0+t_1Q_1=0$ of quadrics", and the rest of the proof then uses the base locus as $X$; it never
shows that the two quadrics have no common component, nor that their intersection, a scheme of degree
$2\cdot2=4$, is $X$ itself rather than a scheme of degree $4$ containing it. That is the same gap the entry
below leaves, and it is what steps [](#quadrics-no-common-component){.pf-ref} and
[](#x-is-complete-intersection){.pf-ref} supply. **Part (b) is therefore not closed on Dolgachev**: his
theorem is cited here for the projective normality, the dimension count, the existence of the pencil and the
diagonal form, and the degree comparison that finishes part (b) is the card's own.

The hypotheses match, with the exercise's own convention: the five points are in general position
(Hartshorne V.4.7), so $X$ is the degree-four Del Pezzo surface embedded by $\abs{-K}$ with $K^2=9-5=4$,
which is precisely his anticanonical model. One correction to the citation: his Lemma 8.3.1 proves its
dimension count by invoking Ramanujam's vanishing theorem by name, with no reference given, and the reference
to Lazarsfeld, *Positivity in Algebraic Geometry* I, Theorem 4.3.1, stands in the proof of his Lemma 8.1.4,
printed p. 248. The card's own step [](#h0-two-h-thirteen){.pf-ref} reaches the same $h^0=13$ by
Riemann--Roch on the blow-up and needs neither. Part (a), the sixteen lines, is not proved there either: his
§8.5.2 uses "the 16 lines on $X$" at printed p. 293 without an argument for the count, so part (a) rests on
the card's steps [](#sixteen-lines-total){.pf-ref} and [](#no-other-lines){.pf-ref}.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.4.13, printed pp. 292--294, read in
`tmp/sources/hartshorne-solutions-egbert.pdf` and in its MinerU text version
`tmp/sources/hartshorne-solutions-egbert.md` (printed folio = PDF page number, and the text version marks the
PDF pages in blocks of twenty; the star attached on p. 293 appears at its line 12563, as "?" in the extraction
read here and as "*" in the regenerated one), settles part
(a) once one step is added, and leaves part (b) where Dolgachev leaves it. At p. 292 he sets up the
intersection theory of the blow-up; at p. 293 he takes a curve with $\deg C=1$ and $C^2=-1$, writes
$C\sim al-\sum b_ie_i$ with $a>0$ and $b_i\ge0$, and applies the Schwarz inequality
$(\sum b_i)^2\le5\sum b_i^2$ to $3a-\sum b_i=1$ and $a^2-\sum b_i^2=-1$, which gives $4a^2-6a-4\le0$, hence
$a=1$ with two of the $b_i$ equal to $1$ (the curves $F_{ij}$) or $a=2$ with all five equal to $1$ (the
transform of the conic); that is the complete list. The one step missing is the hypothesis $C^2=-1$ itself:
for a line it has to be derived, and by adjunction a curve of degree $1$ is rational, so
$C^2+C\cdot K_X=-2$ with $C\cdot K_X=-\deg C=-1$ gives $C^2=-1$. His Picard group is also written $\ZZ^6$
with generators $l,e_1,\dots,e_6$ for a blow-up of five points, which cannot be right: the rank is
$1+5=6$ with $l,e_1,\dots,e_5$ as generators. Part (b) is set up on p. 293 and
closed on p. 294 only by "Now use $\star$.", the $\star$ being the one attached
on p. 293 to $\OO_X(-2K_X)\cong\OO_X(2)$: the count $h^0(\OO_X(2H))=13$ is
completed there from Ramanujam's vanishing theorem, which he names with no
reference --- the very defect this entry charges to Dolgachev --- and
"$15-13=2$" is printed nowhere, so he never states $h^0(\mathcal I_X(2))=2$ nor
concludes that $X$ is a complete intersection. His surjectivity line, "This ends
in 0 since $H^1(\PP^4,\OO_{\PP^4}(-2))=0$", cites the vanishing of a group the
sequence does not need; what the surjectivity requires is
$H^1(\PP^4,\mathcal I_X(2))=0$.
:::

::: {.remark title="Published solution"}
A published proof of part (b) that carries the decisive step exists. M. Riman,
*The Vanishing of the Brauer Group of a del Pezzo Surface of Degree 4*, PhD
dissertation, University of Washington, 2019, Theorem 2.2.7, stated on printed
p. 19 and proved on printed pp. 20--21 (saved as
`tmp/sources/riman-2019-del-pezzo-degree-four.pdf`), proves that a del Pezzo
surface of degree $4$ is a smooth complete intersection of two quadrics in
$\PP^4$. Its proof is the sequence of steps [](#h0-two-h-thirteen){.pf-ref} to
[](#x-is-complete-intersection){.pf-ref}: Riemann--Roch with Kodaira vanishing
on a del Pezzo surface gives $\chi(\OO_X)=1$ and $h^0(X,\OO_X(-2K_X))=13$
(his equation (2.2) with $m=-2$); the exact sequence
$$
0\longrightarrow\mathcal I_X(2)\longrightarrow\OO_{\PP^4}(2)
\longrightarrow\OO_X(2)\longrightarrow0
$$
then gives $h^0(X,\mathcal I_X(2))\ge15-13=2$, so $X$ lies in the intersection
of two independent quadrics $Q,Q'$; and the conclusion $X=Q\cap Q'$ rests on
$\deg X=4=\deg(Q\cap Q')$. Two passages of it are garbled and are repaired on
the steps: the exclusion of a reducible quadric, which he does through what he
calls Klein's theorem and with "since $Q$ is assumed to be irreducible" written
where the argument needs the opposite, and the closing degree count, which is
asserted rather than counted. His Lemma 2.2.8, printed pp. 19--20, supplies the
nondegeneracy of $X$ in $\PP^4$ that the first repair uses: $\abs{-K_X}$ separates
points and tangent vectors, so the anticanonical map is an embedding. The
embedding is also (4.7) of the book, printed p. 416, which the exercise is
about.
:::
