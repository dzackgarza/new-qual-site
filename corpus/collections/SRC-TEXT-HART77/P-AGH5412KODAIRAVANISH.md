---
schema: qual/card@1
id: P-AGH5412KODAIRAVANISH
kind: problem
title: Kodaira vanishing for the cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Intersection Theory
  - Canonical Divisor
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.12, the retained Egbert long-exact-sequence sketch,
    the cubic-surface blowup description, and V.4.8. The retained sketch
    writes X isomorphic to P^2, which is not literal: a smooth cubic surface
    is Bl_6 P^2. What is needed is H^1(X,O_X)=0, which follows because q is
    unchanged under point blowups. By (4.11), an ample D has positive
    intersection with every line and D^2>0; V.4.8 therefore supplies a
    nonsingular irreducible curve C in |D|. Then the exact sequence
    0 -> O_X(-D) -> O_X -> O_C -> 0 closes the argument because
    H^0(O_X)=H^0(O_C)=k and -D is not effective.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete proof against the retained V.4.12 sketch, the cubic
    blowup cohomology, (4.11), and V.4.8. Checked that the smooth effective
    representative exists, that H^0(O_X(-D)) vanishes including the
    nowhere-vanishing-section edge case, and that the restriction k -> k in
    the divisor sequence is an isomorphism.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Two published readings added on a reader's report of issue #121, both
    checked against the sources here. (i) Yang Pi-Yeh, Solution 5.4.12,
    printed p. 111, read in tmp/sources/lfwin-hartshorne-solutions.md (block
    "PDF pages 101-119") and against the folios of the PDF, asserts in its
    second sentence that an ample divisor D on the cubic surface has
    H^0(X, L(D)) = k on the ground that it is very ample; that is false, since
    a very ample D embeds X in P^(h^0-1), so h^0 >= 3 (h^0 = 3 would put the
    surface in P^2). That false k is the source of
    the k -> k in the sequence he then writes, whose true cokernel is O_C. The
    remark now records it. (ii) Egbert's V.4.12, printed p. 292 in the PDF and
    in the MinerU text version tmp/sources/hartshorne-solutions-egbert.md
    (entry 5.4.13, line 12488), is wholly on that one page; his closing step,
    that an effective divisor linearly equivalent to -D must meet some line
    negatively, is no contradiction as it stands, a line in the support of an
    effective divisor meeting it negatively, and the completion is the card's:
    D very ample gives D.C > 0 on every irreducible curve, hence D.E > 0 on
    every nonzero effective E, while E ~ -D gives D.E = -D^2 < 0. The number
    his sentence cites is Theorem 4.11 of the text, whose (iii) with the
    equivalence makes an ample D very ample. COMPLAINTS.md had recorded that step as a
    misuse of (4.11) and the entry as printed pp. 292-293; both are corrected
    there. The card's own proof is unchanged.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Under issue #121 the solution is now a transcription of the published
    argument, one step per printed statement. Read at the printed places:
    Hartshorne, Theorem 4.11 with Lemma 4.12, printed pp. 405--406, whose
    (ii) => (iii) is the easy direction of the Nakai--Moishezon criterion
    Theorem 1.10, printed p. 365, and whose (iv) => (i) runs through the
    minimal-line choice of six skew lines and Lemma 4.12; Hartshorne,
    Corollary 4.13(a),(b), printed p. 406, the numerical translation of 4.11
    and the irreducible nonsingular member, which the book derives from
    Bertini's theorem (II, 8.18) and (III, 7.9.1); Reid, Chapters on Algebraic
    Surfaces, Section 3.9 (numerical 1-connectedness), Lemma 3.11(i),(ii) and
    Section 3.12, printed pp. 72--73, being the route nef-and-big implies
    1-connected implies H^0(O_D) = k implies H^1(O_X(-D)) = 0 on a surface with
    H^1(O_X) = 0. The two structure-sheaf facts were checked against the book
    rather than assumed: II.5.9, printed p. 116, for the ideal sheaf sequence of
    the cubic hypersurface, and Theorem III.5.1(b), printed p. 225, which
    vanishes H^1(P^3,O) and H^2(P^3,O(-3)) and so gives H^0(O_X) = k and
    H^1(O_X) = 0. Checked, not assumed: Theorem 4.11 prints four equivalent
    conditions on a divisor of the cubic surface and Corollary 4.13(b) is
    stated for the classes satisfying (a), so an ample D falls under it; the
    exercise itself is printed on p. 408. What the transcription does not keep
    is this card's earlier independent proof of H^1(O_X) = 0 by the point-blowup
    invariance of q, which is replaced by the projective-space computation
    above; and the earlier sequence through an explicit C with
    H^0(O_C) = k, which is replaced by Reid's 1-connectedness route. No part of
    the exercise is left without a published proof by this transcription.
---

::: {.problem}
Use (4.11) to show that if $D$ is any ample divisor on the cubic surface $X$, then $H^1\left(X, \OO_X(-D)\right)=0$.
This is Kodaira's vanishing theorem for the cubic surface (III, 7.15).
:::

::: {.solution}
Let $X\subseteq\PP^3$ be the nonsingular cubic surface and let $D$ be an ample divisor on $X$.

The argument is the printed one. It has three published inputs: the ampleness criterion (4.11) of the book, with its numerical translation and its irreducible nonsingular member, Corollary 4.13; and the connectedness route to the vanishing of Reid's Section 3.12.

::: pf

::: {.pf-step #positive-on-lines}
For an ample $D$ one has
$$
\boxed{D^2>0,\qquad D\cdot L>0\ \text{for every line } L\subseteq X.}
$$

::: pf-proof
This is the implication (ii) $\Rightarrow$ (iii) of Hartshorne's Theorem 4.11, printed p. 405, whose four conditions on a divisor $D$ of the cubic surface are: (i) $D$ is very ample; (ii) $D$ is ample; (iii) $D^2>0$ and $D\cdot L>0$ for every line $L\subseteq X$; (iv) $D\cdot L>0$ for every line $L\subseteq X$. The book obtains (ii) $\Rightarrow$ (iii) from the easy direction of the Nakai--Moishezon criterion, Theorem 1.10, printed p. 365: a divisor $D$ on a surface is ample if and only if $D^2>0$ and $D\cdot C>0$ for every irreducible curve $C$.
:::

:::

::: {.pf-step #very-ample}
$D$ is very ample.

::: pf-proof
Step [](#positive-on-lines){.pf-ref} gives condition (iv) of Theorem 4.11, so (i) holds by the implication (iv) $\Rightarrow$ (i) proved on printed pp. 405--406. That proof runs as follows. Choose six mutually skew lines $E_6',E_5',\ldots,E_1'$: take for $E_6'$ a line on which $D$ is minimal, then for $E_5'$ a line not meeting $E_6'$ on which $D$ is minimal among those, then $E_4',E_3'$ similarly, and finally $E_1',E_2'$ among the three remaining lines, ordered so that $D\cdot E_1'\ge D\cdot E_2'$. The configuration of the $27$ lines is the same for any six mutually skew ones, so by (4.10) the labelling may be changed to make $E_i'=E_i$ for every $i$. Then $D\cdot E_i=b_i$ with $D\sim al-\sum_ib_ie_i$, so $b_1\ge b_2\ge\cdots\ge b_6>0$; and $F_{12}$ was a candidate when $E_3'$ was chosen, so $D\cdot F_{12}\ge D\cdot E_3'$, that is $a-b_1-b_2\ge b_3$. Lemma 4.12, printed p. 405, states that a class with $b_1\ge\cdots\ge b_6>0$ and $a\ge b_1+b_2+b_3$ is very ample, and its proof writes $D$ as a nonnegative combination $\sum_ic_iD_i$ of
$$
D_0=l,\quad D_1=l-e_1,\quad D_2=2l-e_1-e_2,\quad D_3=2l-e_1-e_2-e_3,
$$
$$
D_4=2l-e_1-e_2-e_3-e_4,\quad D_5=3l-e_1-\cdots-e_5,\quad D_6=3l-e_1-\cdots-e_6
$$
with $c_6>0$, each $D_i$ moving in a base-point-free linear system, $D_6$ very ample by (4.6), and uses that a very ample divisor plus one moving in a base-point-free linear system is very ample (II, Ex. 7.5).
:::

:::

::: {.pf-step #nonsingular-curve-in-class}
The linear system $\abs{D}$ contains an irreducible nonsingular curve $C$. In particular $D$ is effective.

::: pf-proof
Corollary 4.13(a), printed p. 406, is the translation of (4.11) into coordinates: $D\sim al-\sum_ib_ie_i$ is ample if and only if $b_i>0$ for each $i$, $a>b_i+b_j$ for each $i,j$, and $2a>\sum_{j\ne i}b_j$ for each $i$. Corollary 4.13(b) then states that in any divisor class satisfying those conditions there is an irreducible nonsingular curve, which the book derives from Bertini's theorem (II, 8.18) and (III, 7.9.1). Since $D$ is ample, its class satisfies the conditions, so $\abs{D}$ contains an irreducible nonsingular curve $C$.
:::

:::

::: {.pf-step #numerically-one-connected}
$D$ is numerically $1$-connected: for every decomposition $D=D_1+D_2$ with $D_1,D_2>0$ effective one has $D_1\cdot D_2\ge1$.

::: pf-proof
This is Lemma 3.11(i) of Reid, printed p. 72, whose statement is that for a nonsingular projective surface and an effective divisor $D$, nef together with $D^2>0$ implies that $D$ is numerically $1$-connected in the sense of Section 3.9, printed p. 72. The hypotheses hold: $D$ is effective by step [](#nonsingular-curve-in-class){.pf-ref}, $D^2>0$ by step [](#positive-on-lines){.pf-ref}, and $D$ is nef because $D\cdot\Gamma>0$ for every curve $\Gamma$, which is Theorem 1.10 again. The proof is Reid's: from $D$ nef, $D\cdot D_i\ge0$ for $i=1,2$; if $D_1\cdot D_2\le0$, then
$$
D_1^2D_2^2\ge(D_1\cdot D_2)^2\ge0,
$$
which contradicts the Hodge index theorem unless $D_1=0$ or $D_2=0$.
:::

:::

::: {.pf-step #structure-sheaf}
$$
\boxed{H^0(X,\OO_X)=k,\qquad H^1(X,\OO_X)=0.}
$$

::: pf-proof
Let $F$ be the cubic form with $X=V(F)\subseteq\PP^3$. The ideal sheaf of $X$ is $\OO_{\PP^3}(-3)$, so
$$
0\longrightarrow\OO_{\PP^3}(-3)\longrightarrow\OO_{\PP^3}\longrightarrow\OO_X\longrightarrow0
$$
is exact: it is the ideal sheaf sequence of a closed subscheme, Hartshorne II.5.9, printed p. 116. Theorem III.5.1(b), printed p. 225, gives $H^i(\PP^3,\OO_{\PP^3}(n))=0$ for $0<i<3$ and all $n$, so that $H^1(\PP^3,\OO_{\PP^3})=0$ and $H^2(\PP^3,\OO_{\PP^3}(-3))=0$, while $H^0(\PP^3,\OO_{\PP^3}(-3))=0$ and $H^0(\PP^3,\OO_{\PP^3})=k$ by (a) of the same theorem. The long exact sequence therefore has $H^1(X,\OO_X)=0$ between two zero groups and $H^0(X,\OO_X)\cong k$ at the other end.
:::

:::

::: {.pf-step #structure-sheaf-of-D}
Let $\OO_D=\OO_X/\OO_X(-D)$ be the structure sheaf of the divisor $D$. Then
$$
\boxed{H^0(X,\OO_D)=k.}
$$

::: pf-proof
Because $D$ is effective, $\OO_D=\OO_X/\OO_X(-D)$ is the structure sheaf of the subscheme $D\subseteq X$, as in Reid's Section 3.9, printed p. 72. Lemma 3.11(ii), printed p. 72, states that a numerically $1$-connected effective divisor has $H^0(\OO_D)=$ constants. Step [](#numerically-one-connected){.pf-ref} supplies the hypothesis, so $H^0(X,\OO_D)$ is one-dimensional over $k$.
:::

:::

::: {.pf-step #vanishing}
$$
\boxed{H^1\left(X,\OO_X(-D)\right)=0.}
$$

::: pf-proof
The sequence
$$
0\longrightarrow\OO_X(-D)\longrightarrow\OO_X\longrightarrow\OO_D\longrightarrow0
$$
is exact, so its long exact cohomology sequence begins
$$
0\longrightarrow H^0(\OO_X(-D))\longrightarrow H^0(\OO_X)\longrightarrow H^0(\OO_D)\longrightarrow H^1(\OO_X(-D))\longrightarrow H^1(\OO_X).
$$
By step [](#structure-sheaf){.pf-ref} the two groups in the middle are $k$, and the map between them sends the constant function $1$ to the constant function $1$, so it is an isomorphism; by the same step $H^1(\OO_X)=0$. Exactness then forces $H^1(X,\OO_X(-D))=0$. This is the argument of Reid's Section 3.12, printed p. 73, carried there for a K3 surface and then stated for any surface with $H^1(\OO_X)=0$: the vanishing holds for an effective divisor that is numerically $1$-connected, in particular for an effective, nef and big divisor.
:::

:::

:::
:::

::: {.remark title="Published solutions"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.4, exercise 4.12, printed p. 408, read in `tmp/sources/hartshorne-1977-algebraic-geometry.md`, whose printed page is its marker minus fifteen.

Igor V. Dolgachev, *Topics in Classical Algebraic Geometry*, was not read for this card. The three sources the proof rests on are the book itself and Reid's Park City notes, and each is used at a numbered statement: Theorem 4.11 with Lemma 4.12 for the passage from ample to very ample, Corollary 4.13 for the numerical translation and the nonsingular member, and Lemma 3.11 with Section 3.12 of Reid for the cohomological step. Reid's Section 3.12 gives the vanishing in the form this exercise asks for, $H^1(\OO_X(-D))=0$ for $D$ effective and $1$-connected on a surface with $H^1(\OO_X)=0$, and derives it, as on this card, from $H^0(\OO_D)=$ constants and the long exact sequence of $0\to\OO_X(-D)\to\OO_X\to\OO_D\to0$; his Section 3.13 then records that the characteristic-zero proofs of the general theorem are Ramanujam's and the Bogomolov--Mumford one, neither of which the cubic surface needs.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.4.12, printed p. 292, is wholly on that one page and takes the same route with the two structure-sheaf facts stated rather than derived: he records $H^0(\OO_X)=k$, $H^1(\OO_X)=0$ and $H^2(\OO_X)=H^0(\OO_X(-3))=p_g=0$, writes "By chapter 1, $H^0(D,\OO_D)=k$" for the divisor $D$, and reads the long exact sequence term by term. His closing step, "Suppose there is an effective divisor linearly equivalent to $-D$. Then by V.4.11, this effective divisor should meet at least one line with negative intersection which is silly", needs a completion. A negative intersection with a line is no contradiction: an effective $E=L+E'$ with $E'\cdot L=0$ has $E\cdot L=-1$, so a line in the support of an effective divisor can meet that divisor negatively. The contradiction is with very ampleness directly: $D$ very ample gives $D\cdot\Gamma>0$ for every irreducible curve $\Gamma$, hence $D\cdot E>0$ for every nonzero effective $E$, while $E\sim-D$ gives $D\cdot E=-D^2<0$, which $D^2>0$ excludes. The number his sentence cites needs care because two results share it: the exercise printed as 4.11 in §4 is the Weyl groups exercise and says nothing about divisors, while **Theorem 4.11** is the criterion. The existence of a nonsingular member of $\abs{D}$, which his entry does not supply, is Corollary 4.13(b) here.

Yang Pi-Yeh, *Hartshorne Solutions*, Solution 5.4.12, printed p. 111, is defective at its second sentence: "Clearly we have $H^0(X,\OO_X)=k$, $H^1(X,\OO_X)=0$. Then for any ample divisor $D$, it is very ample by theorem 4.11., we have $H^0(X,\mathcal L(D))=k$." The inference is false. A very ample divisor $D$ embeds $X$ in $\PP^{h^0(\mathcal L(D))-1}$, so $h^0(\mathcal L(D))\ge3$: the image has dimension $2$ and spans that projective space, and $h^0=3$ would make the image all of $\PP^2$, that is $X\cong\PP^2$. That false $k$ is the second $k$ of the "$k\to k$" he then writes. His next display is a sequence of $\OO_X$-modules, $0\to\mathcal L(-D)\to\OO_X\to\mathcal L(D)\to0$, in which the sheaf that occurs is $\OO_C$ for $C\in\abs{D}$; with the correct sequence the map $k\to k$ is an isomorphism and the vanishing is immediate, which is the last step of this card.
:::
