---
schema: qual/card@1
id: P-AGH531PABLOWUP
kind: problem
title: Invariance of the arithmetic genus under blowing up a nonsingular subvariety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.3.1 and the retained Egbert companion calculation. The
    source states the invariance of arithmetic genus under a blowup of a
    smooth centre. The proof uses vanishing of higher direct images of the
    structure sheaf and the definition p_a=(-1)^dim(chi(O)-1).
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: >-
    V.3.4 concerns Hilbert-Samuel multiplicity, not blowup cohomology.
    Replaced the false cross-reference with the projective birational
    vanishing theorem of Chatzistamatiou and Rulling, Theorem 1.1.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.3,
    exercise 3.1, printed page 394. Checked the reduction: R^j pi_* O = 0 for
    j > 0 and pi_* O = O give H^i(X-tilde, O) = H^i(X, O) by the Leray spectral
    sequence, hence equality of the Euler characteristics and of
    p_a(Z) = (-1)^n (chi(Z,O_Z) - 1), the definition of III.5/IV.1. Searched
    outside the twelve retained sets: Algebraic Geometry II, National Taiwan
    University, 2020 Spring, Chapter V homework, Exercise 1 of section 3, PDF
    p. 9 (tmp/sources/ntu-ag2-chapter5.pdf), proves the vanishing for a centre
    of any codimension by the formal functions theorem over E = P^{r-1};
    Yang Pi-Yeh, Hartshorne Solutions, exercise 5.3.1, printed p. 107
    (tmp/sources/lfwin-hartshorne-solutions.pdf), assumes codimension one and
    is not a proof of the exercise. Not checked: Chatzistamatiou-Rulling
    Theorem 1.1 itself, which is cited and not in tmp/sources; the card's own
    argument needs only that statement.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Published argument located for issue #121 and checked against the book.
    Hartshorne V.3.1, printed p. 394, asks for p_a(X-tilde) = p_a(X) for the
    blowup of a nonsingular subvariety Y of a nonsingular projective variety X
    of any dimension. Step cohomology-invariance now cites the printed
    statement of A. Chatzistamatiou and K. Ruelling, Vanishing of the higher
    direct images of the structure sheaf, Compositio Math. 151 (2015)
    2131-2144, Theorem 1.1, printed p. 1 (a preimage of the published version,
    arXiv:1404.1827v2, was added to tmp/sources as
    chatzistamatiou-rulling-2015-higher-direct-images.pdf): the higher direct
    images of O_X under a projective birational morphism between excellent
    regular schemes vanish. With pi_* O = O_X (the proof of III.11.4) and
    Exercise III.8.1 that gives H^i(X-tilde,O) = H^i(X,O), hence equality of
    the structure-sheaf Euler characteristics and of p_a. Checked: X and
    X-tilde are excellent regular and pi is projective, so the hypotheses
    hold; p_a(Z) = (-1)^n (chi(Z,O_Z) - 1) is the book's definition. Corrected
    against the source: the earlier note on this card said the NTU 2020 entry
    proves the vanishing for a centre of any codimension. It does not. Its
    induction uses H^i(P^{r-1},O(n)) = 0 for i > 0, which is the cohomology of
    a fibre; that is the cohomology of the exceptional divisor only when
    dim Y = 0, and for Y positive-dimensional H^i(E,O_E(n)) =
    H^i(Y,Sym^n(I/I^2)), which is H^1(Y,O_Y) at n = 0. The entry proves the
    monoidal case, and the card's remark now says so. Not checked: the proof
    of Theorem 1.1 itself, a duality argument, was not read; the step uses
    only its statement.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Text version of the cited theorem located in tmp/sources for issue #121.
    Chatzistamatiou-Ruelling, Vanishing of the higher direct images of the
    structure sheaf, arXiv:1404.1827v2, is retained twice: as the PDF named
    above and as the extraction
    tmp/sources/chatzistamatiou-rulling-2015-higher-direct-images.md, which
    runs over the whole preprint, title page to references, and states
    Theorem 1.1 on its first page: a projective and birational morphism between excellent and
    regular schemes has R^i f_* O_X = 0 for i >= 1. The card said tmp/sources
    held no text version of the paper; that is withdrawn, and the remark on
    the preprint page now names the extraction beside the PDF. The page stays
    the preprint's p. 1, the folio its first page prints, and not the
    Compositio 2131 of the journal printing. Checked: the statement of
    Theorem 1.1 was read in the extraction and compared with the PDF text
    layer of its first page, and the two agree wording for wording; the
    extraction's first page marker is PDF pages 1-14 and the PDF has fourteen
    pages. Not checked: no part of the proof of Theorem 1.1 was read, that is
    Sections 2 to 5, a Grothendieck-Serre duality argument; the Compositio
    printing, 151 (2015) 2131-2144, was not consulted, so no page of the
    printed article is given. The event of 2026-11-16 above had been rewritten
    in place; it is restored to the text it was dated with, and this note is
    its correction.
---

::: {.problem}
Let $X$ be a nonsingular projective variety of any dimension, let $Y$ be a nonsingular subvariety, and let $\pi: \tilde{X} \rightarrow X$ be obtained by blowing up $Y$.
Show that $p_a(\tilde{X})=p_a(X)$.
:::

::: {.solution}
Put
$$
n=\dim X.
$$
Since a blowup is birational,
$$
\dim\widetilde X=n.
$$

::: pf

::: {.pf-step #cohomology-invariance}
For every $i\ge0$,
$$
\boxed{
H^i(\widetilde X,\OO_{\widetilde X})
\cong
H^i(X,\OO_X).}
$$

::: pf-proof
The blowup of a nonsingular variety along a nonsingular centre is
nonsingular, and the blowup morphism $\pi$ is projective and birational.
Both varieties are excellent because they are of finite type over $k$.
Chatzistamatiou--Rülling, *Vanishing of the higher direct images of the
structure sheaf*, Compositio Math. 151 (2015) 2131--2144,
[Theorem 1.1, p. 1 of arXiv:1404.1827v2](https://arxiv.org/abs/1404.1827),
states that a projective birational morphism between excellent regular schemes
has vanishing higher direct images of the structure sheaf, and it therefore
gives
$$
R^j\pi_*\OO_{\widetilde X}=0\qquad(j>0).
$$
Since $X$ is normal and $\pi$ is proper and birational,
$$
\pi_*\OO_{\widetilde X}=\OO_X.
$$
The Leray spectral sequence now gives the displayed isomorphisms.

The theorem's page is that of the preprint: the retained copy
`tmp/sources/chatzistamatiou-rulling-2015-higher-direct-images.pdf` is
arXiv:1404.1827v2, whose first page carries Theorem 1.1 and the footer "1",
and its text version is the extraction
`tmp/sources/chatzistamatiou-rulling-2015-higher-direct-images.md`, which
runs over those same fourteen pages and carries Theorem 1.1 on its first one,
under the marker the extraction writes for PDF pages 1--14. The journal
printing in Compositio Math. 151 (2015) 2131--2144 was not consulted, so this
citation gives no page of the printed article.
:::

:::

::: {.pf-step #euler-char-invariance}
The structure-sheaf Euler characteristic is unchanged:
$$
\boxed{
\chi(\widetilde X,\OO_{\widetilde X})
=
\chi(X,\OO_X).}
$$

::: pf-proof
By definition,
$$
\chi(Z,\OO_Z)
=
\sum_{i\ge0}(-1)^i
\dim_k H^i(Z,\OO_Z)
$$
for a projective variety $Z$.  Step [](#cohomology-invariance){.pf-ref} identifies every summand for
$Z=\widetilde X$ with the corresponding summand for $Z=X$, so the two
alternating sums agree.
:::

:::

::: {.pf-step #arithmetic-genus-equal}
The arithmetic genera agree:
$$
\boxed{p_a(\widetilde X)=p_a(X).}
$$

::: pf-proof
For a nonempty projective scheme of dimension $n$, the arithmetic genus is
[[D-COHEULER]]
$$
p_a(Z)=(-1)^n\bigl(\chi(Z,\OO_Z)-1\bigr).
$$
The varieties $X$ and $\widetilde X$ have the same dimension $n$, and step
[](#euler-char-invariance){.pf-ref} gives equality of their structure-sheaf Euler characteristics.
Substitution into the displayed definition gives
$$
p_a(\widetilde X)
=
(-1)^n\bigl(\chi(\widetilde X,\OO_{\widetilde X})-1\bigr)
=
(-1)^n\bigl(\chi(X,\OO_X)-1\bigr)
=
p_a(X).
$$
:::

:::

::: pf-qed
Steps [](#cohomology-invariance){.pf-ref}, [](#euler-char-invariance){.pf-ref} and [](#arithmetic-genus-equal){.pf-ref} prove the asserted invariance of the arithmetic genus under
blowing up a nonsingular centre.
:::

:::
:::

::: {.remark title="Published solution"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.3, exercise 3.1, text version `tmp/sources/hartshorne-1977-algebraic-geometry.md` (its marker `PDF page 409`; printed page = PDF page $-15$).

Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 1 of §3 (solution by Shuang-Yen Lee), text version `tmp/sources/ntu-ag2-chapter5.md` (whose page markers are coarse, `PDF pages 1-20`, so the page was read off the PDF), writes the formal-functions reduction for a centre of codimension $r$: by Exercise III.8.1 it suffices to have $\pi_*\OO_{\widetilde X}=\OO_X$, which is the proof of III.11.4, and $R^i\pi_*\OO_{\widetilde X}=0$ for $i>0$. Outside the centre $\pi$ is an isomorphism; at a point $y\in Y$ the formal functions theorem identifies the stalk of $R^i\pi_*\OO_{\widetilde X}$ with $\varprojlim H^i(E_n,\OO_{E_n})$, where $E$ is the exceptional divisor, $E_n$ its $n$th infinitesimal neighbourhood, and $\mathcal I^n/\mathcal I^{n+1}\cong\operatorname{Sym}^n(\mathcal I/\mathcal I^2)\cong\OO_E(n)$. Its induction then invokes $H^i(\PP^{r-1},\OO(n))=0$ for $i>0$ and $n\ge0$, which is the cohomology of a fibre. That is the cohomology of $E$ only when $\dim Y=0$, where indeed $E\cong\PP^{r-1}$; for $Y$ positive-dimensional $E$ is a $\PP^{r-1}$-bundle over $Y$ and $H^i(E,\OO_E(n))=H^i(Y,\operatorname{Sym}^n(\mathcal I/\mathcal I^2))$, which need not vanish --- for $Y$ a curve of positive genus and $n=0$ it is $H^i(Y,\OO_Y)$, nonzero for $i=1$. The entry therefore proves the monoidal case, $\dim Y=0$, which is (3.4) itself, and not the exercise; its closing sentence $p_a(\widetilde X)=p_a(X)$ inherits the gap. Steps [](#cohomology-invariance){.pf-ref} to [](#arithmetic-genus-equal){.pf-ref} reach the conclusion for a centre of any codimension through $R^j\pi_*\OO_{\widetilde X}=0$ for $j>0$, which is Chatzistamatiou--Rülling's theorem.

Yang Pi-Yeh, *Hartshorne Solutions*, text version `tmp/sources/lfwin-hartshorne-solutions.md`, exercise 5.3.1, writes "since $\operatorname{codim}(Y,X)=1$, $\mathcal I/\mathcal I^2$ is an invertible sheaf on $Y$" and then covers $E$ by $\PP^1_A$'s; the exercise has $Y$ of any codimension, and a codimension-one blowup is an isomorphism, so the argument does not cover the case it is aimed at.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.3.1: the whole of his solution is "This follows from 3.4, which says that $H^i(\widetilde X)\approx H^i(X)$ and the fact that $p_a$ is calculated from the Euler characteristic". Result (3.4) and its corollary (3.5) are the monoidal case, where the centre is a point; the exercise blows up a nonsingular subvariety of any codimension, and the invariance of $H^i(X,\OO_X)$ is then the vanishing of the higher direct images of $\OO_{\widetilde X}$ under a projective birational morphism of regular schemes, proved by Chatzistamatiou and Rülling, *Vanishing of the higher direct images of the structure sheaf*, Compositio Math. 151 (2015) 2131--2144, Theorem 1.1. Steps [](#cohomology-invariance){.pf-ref} to [](#arithmetic-genus-equal){.pf-ref} are that reduction, with $p_a(Z)=(-1)^n(\chi(Z,\OO_Z)-1)$.
:::
