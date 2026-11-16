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
---

::: {.problem}
Use (4.11) to show that if $D$ is any ample divisor on the cubic surface $X$, then $H^1\left(X, \OO_X(-D)\right)=0$.
This is Kodaira's vanishing theorem for the cubic surface (III, 7.15).
:::

::: {.solution}
Let
$$
X\subseteq\PP^3
$$
be the nonsingular cubic surface and let $D$ be ample.

::: pf

::: {.pf-step #h0-h1-structure-sheaf}
One has
$$
\boxed{
H^0(X,\OO_X)=k,
\qquad
H^1(X,\OO_X)=0.}
$$

::: pf-proof
The cubic surface is
$$
X\cong\operatorname{Bl}_{P_1,\ldots,P_6}\PP^2
$$
for six points in general position [[FE-SRFCUBIC]]. Point blowups of a
nonsingular surface preserve
$$
q=h^1(\OO)
$$
[[FE-SRFBLOW]]. Since
$$
H^1(\PP^2,\OO_{\PP^2})=0,
$$
it follows that
$$
H^1(X,\OO_X)=0.
$$
Also $X$ is integral and projective over the algebraically closed ground
field, so every global regular function is constant:
$$
H^0(X,\OO_X)=k.
$$
:::

:::

::: {.pf-step #nonsingular-curve-in-class}
The divisor class $D$ contains a nonsingular irreducible curve
$$
\boxed{C\in\linearsystem{D}.}
$$

::: pf-proof
The ampleness criterion (4.11) gives
$$
D\cdot L>0
$$
for every one of the $27$ lines on $X$, and
$$
D^2>0.
$$
Thus $D$ satisfies alternative (c) of V.4.8. By
[[P-AGH548IRREDCLASSES]], every such class contains an irreducible
nonsingular curve. Choose one and call it $C$. Then
$$
C\sim D.
$$
:::

:::

::: {.pf-step #h0-negative-d-vanishes}
The line bundle
$$
\OO_X(-D)
$$
has no nonzero global section:
$$
\boxed{H^0(X,\OO_X(-D))=0.}
$$

::: pf-proof
Suppose a nonzero section existed. If it vanished nowhere, it would
trivialize $\OO_X(-D)$, forcing $D\sim0$ and hence $D^2=0$, contrary to
step [](#nonsingular-curve-in-class){.pf-ref}. Thus its zero divisor is a nonzero effective divisor
$$
E\sim-D.
$$
Because $D$ is ample, it has positive intersection with every nonzero
effective curve, hence
$$
D\cdot E>0.
$$
But numerical equivalence gives
$$
D\cdot E
=
-D^2
<0,
$$
since $D^2>0$ by step [](#nonsingular-curve-in-class){.pf-ref}. This contradiction proves the vanishing.
:::

:::

::: {.pf-step #ideal-sheaf-sequence}
The curve $C$ gives an exact sequence
$$
0
\longrightarrow
\OO_X(-D)
\longrightarrow
\OO_X
\longrightarrow
\OO_C
\longrightarrow
0.
$$

::: pf-proof
Since $C$ is an effective Cartier divisor linearly equivalent to $D$, its
ideal sheaf is
$$
\mathcal I_C\cong\OO_X(-C)\cong\OO_X(-D).
$$
The standard ideal-sheaf sequence of $C$ is therefore exactly the displayed
sequence.
:::

:::

::: {.pf-step #h0-oc-restriction-iso}
One has
$$
\boxed{H^0(C,\OO_C)=k,}
$$
and the restriction map
$$
H^0(X,\OO_X)\longrightarrow H^0(C,\OO_C)
$$
is an isomorphism.

::: pf-proof
The curve $C$ is nonsingular and irreducible by step [](#nonsingular-curve-in-class){.pf-ref}, hence integral
and projective. Thus every global regular function on $C$ is constant:
$$
H^0(C,\OO_C)=k.
$$
The restriction map sends the constant function $1$ on $X$ to the constant
function $1$ on $C$. Under the identifications
$$
H^0(X,\OO_X)=k=H^0(C,\OO_C),
$$
it is therefore the identity map on $k$.
:::

:::

::: {.pf-step #h1-negative-d-vanishes}
Consequently
$$
\boxed{H^1(X,\OO_X(-D))=0.}
$$

::: pf-proof
The long exact cohomology sequence of step [](#ideal-sheaf-sequence){.pf-ref} begins
$$
0
\longrightarrow
H^0(X,\OO_X(-D))
\longrightarrow
H^0(X,\OO_X)
\longrightarrow
H^0(C,\OO_C)
\longrightarrow
H^1(X,\OO_X(-D))
\longrightarrow
H^1(X,\OO_X).
$$
By steps [](#h0-h1-structure-sheaf){.pf-ref}, [](#h0-negative-d-vanishes){.pf-ref}, and [](#h0-oc-restriction-iso){.pf-ref} this becomes
$$
0
\longrightarrow
0
\longrightarrow
k
\xrightarrow{\sim}
k
\longrightarrow
H^1(X,\OO_X(-D))
\longrightarrow
0.
$$
Exactness forces
$$
H^1(X,\OO_X(-D))=0.
$$
:::

:::

::: pf-qed
Steps [](#h0-h1-structure-sheaf){.pf-ref}, [](#nonsingular-curve-in-class){.pf-ref}, [](#h0-negative-d-vanishes){.pf-ref}, [](#ideal-sheaf-sequence){.pf-ref} and [](#h0-oc-restriction-iso){.pf-ref} establish the cohomological inputs for the divisor sequence,
and step [](#h1-negative-d-vanishes){.pf-ref} gives the required vanishing.
:::

:::
:::

::: {.remark title="Published solutions"}
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.4.12, printed p. 292, read in
`tmp/sources/hartshorne-solutions-egbert.pdf` and in its MinerU text version
`tmp/sources/hartshorne-solutions-egbert.md` (printed folio = PDF page number; the text version marks the PDF
pages in blocks of twenty, and its entry 5.4.13 at line 12488 is the one printed at p. 292), is wholly on that
one page and takes this card's route. He records $H^0(\OO_X)=k$, $H^1(\OO_X)=0$ and
$H^2(\OO_X)=H^0(\OO_X(-3))=p_g=0$, writes "By chapter 1, $H^0(D,\OO_D)=k$", reads the long exact sequence of
$0\to\OO_X(-D)\to\OO_X\to\OO_D\to0$ term by term, and closes by contradiction: "Suppose there is an effective
divisor linearly equivalent to $-D$. Then by V.4.11, this effective divisor should meet at least one line
with negative intersection which is silly."

His closing step needs a completion, and the completion is the card's. A negative intersection with a line is
no contradiction: an effective $E=L+E'$ with $E'\cdot L=0$ has $E\cdot L=-1$, so a line contained in the support
of an effective divisor can meet that divisor negatively. The contradiction is with very ampleness, directly.
$D$ very ample gives $D\cdot C>0$ for every irreducible curve $C$, hence $D\cdot E>0$ for every nonzero
effective $E$, while $E\sim-D$ gives $D\cdot E=-D^2<0$, which $D^2>0$ excludes. So no effective divisor is
linearly equivalent to $-D$, and the vanishing follows from the exact sequence. The number his sentence cites
needs care because two results share it. The exercise
printed as 4.11 in §4 is the Weyl groups exercise, which says nothing about divisors; the criterion meant is
**Theorem 4.11** of the text, "The following conditions are equivalent, for a divisor $D$ on the cubic surface
$X$: (i) $D$ is very ample; (ii) $D$ is ample; (iii) $D^2>0$, and for every line $L\subseteq X$, $D\cdot L>0$;
(iv) for every line $L\subseteq X$, $D\cdot L>0$." By (iii) with the equivalence, an ample $D$ is very ample,
which is the step used above. What his entry does not supply is the existence of a nonsingular member $C\in\abs{D}$, which step
[](#nonsingular-curve-in-class){.pf-ref} takes from (4.11) and V.4.8.

Yang Pi-Yeh, *Hartshorne Solutions*, text version `tmp/sources/lfwin-hartshorne-solutions.md`, Solution 5.4.12, printed p. 111, is defective at its second sentence:
"Clearly we have $H^0(X,\OO_X)=k$, $H^1(X,\OO_X)=0$. Then for any ample divisor $D$, it is very ample by
theorem 4.11., we have $H^0(X,\mathcal L(D))=k$." The inference is false. A very ample divisor $D$ on the
cubic surface embeds $X$ in $\PP^{h^0(\mathcal L(D))-1}$, so $h^0(\mathcal L(D))\ge3$: the image spans that
projective space and has dimension $2$, and $h^0=3$ would make the image all of $\PP^2$, that is
$X\cong\PP^2$. That false $k$ is
the source of his "$k\to k$". His next display is a sequence of $\OO_X$-modules,
$0\to\mathcal L(-D)\to\OO_X\to\mathcal L(D)\to0$, "i.e."
$0\to H^0(X,\mathcal L(-D))\to k\to k\to H^1(X,\mathcal L(-D))\to0$, in which the second $k$ is his
$h^0(\mathcal L(D))$; the sheaf that occurs there is $\OO_C$ for $C\in\abs{D}$, and the sequence with
$\mathcal L(D)$ as cokernel is not exact. With the correct sequence the map $k\to k$ is an isomorphism and the
vanishing is immediate. His vanishing step itself is the card's: if $s\in H^0(X,\mathcal L(-D))$ were nonzero
with $C=\operatorname{Supp}s$, then for a line $E$ not contained in $C$ one has $C\cdot E\ge0$, hence
$D\cdot E\le0$, against (4.11). Theorem 4.11 is printed on p. 405 and the exercise itself on p. 408, its text being read in
`tmp/sources/hartshorne-1977-algebraic-geometry.md`, where those printed pages are its PDF pages 420 and 423
(printed page = PDF page minus fifteen, the offset that puts V.2.13 on printed p. 385).
:::
