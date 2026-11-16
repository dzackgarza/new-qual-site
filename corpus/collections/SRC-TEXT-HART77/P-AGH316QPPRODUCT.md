---
schema: qual/card@1
id: P-AGH316QPPRODUCT
kind: problem
title: Products of quasi-projective varieties via the Segre embedding
classification:
  areas:
  - algebraic-geometry
  topics:
  - Products
  - Segre Embedding
  - Quasi-Projective Varieties
relations:
- kind: uses
  target: P-AGH214SEGRE
- kind: uses
  target: P-AGH315AFFPRODUCT
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all three parts with Hartshorne I.3.16. The proof first constructs the two ambient projections on Segre nonzero-entry charts, then uses them to identify X times Y as locally closed; affine product charts supply irreducibility and the categorical universal property.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the Segre chart formulas, locally-closed/projective claims, and local-to-global universal morphism against the source and published discussions of I.3.16.'
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read Bertram, Algebraic Geometry (Math 6130, Utah), Section 4,
    Proposition 4.3 with the paragraphs following, printed pp. 5-6, which
    proves the product of projective spaces is the product in the category
    of prevarieties via the Segre image and the local product-of-rational-
    functions formula, and derives Y x Z closed and U x V open. That closes
    part (c), which the retained sets omit. Checked the card's own steps
    against it: the two projections, local closedness, closedness, and the
    universal property on affine charts. Not checked: Bertram's graded-ring
    remark.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the quoted passage this pass. Printed exercise read: Hartshorne,
    Algebraic Geometry (1977), I.3.16, printed p. 22 (PDF p. 37 of the
    extraction). Bertram, Algebraic Geometry (Math 6130, Utah), Section 4,
    Proposition 4.3 with its proof and the three displays after it, printed
    pp. 5-6, text version tmp/sources/bertram-utah-6130-varieties.md: the
    proposition says the Segre embedding "exhibits the product of projective
    spaces as a projective variety", its proof says the triple is universal "in
    the category of prevarieties", gives the two projections by their formulas,
    and then gives Y x Z = V(<F_i(x_00,...,x_m0), G_j(x_00,...,x_0n)>) for
    closed Y, Z and U x V = Y x Z - pi_2^{-1}(Z-V) - pi_1^{-1}(Y-U) for open
    U, V. Verified each against the card: projections in step s1, local
    closedness and irreducibility in s2, closedness in s3, universality in s4.
    Corrected 2026-11-16 on the reader's report: that Y x Z display was
    recorded above as verified and is false as printed --- it uses only the
    zeroth column and row, so the point of the Segre variety with a_0 = b_0 = 0
    satisfies both sets of generators, F_i(0,...,0) = 0 and G_j(0,...,0) = 0
    since both are homogeneous of positive degree, and need not lie in Y x Z;
    for Y = V(x_0) and Z = V(y_0) the point (1:0:...) x (0:1:0:...) does not
    lie in Y x Z and does satisfy them. The row-and-column reading that is true
    holds the generators in every column and every row. Nor does his
    universality cover subvarieties: it is proved for P^m x P^n, and the
    passage to Y, Z is the one sentence "This extends in a straightforward
    manner to projective varieties".
    Recorded as a gap: Bertram's universality is in prevarieties, so his
    Proposition 4.3 alone does not give (c) in the category of varieties, whose
    objects Hartshorne takes irreducible; the irreducibility of X x Y is this
    card's step s2, and the remark says so.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Three repairs on the local reader's report, each checked against the
    Bertram text version before editing. (1) The card called Bertram the
    complete published argument for (a)--(c). He proves universality for
    W -> P^m x P^n and says only that the case of projective subvarieties
    "extends in a straightforward manner" (line 227 of the text version), so
    (c) for quasi-projective factors is not his. (2) His display
    Y x Z = V(<F_i(x_00,...,x_m0), G_j(x_00,...,x_0n)>) at line 230 is false as
    printed: it uses the zeroth column and row only, so the image point with
    a_0 = b_0 = 0 satisfies both sets of generators and need not lie in
    Y x Z --- for Y = V(x_0), Z = V(y_0) the point (1:0:..) x (0:1:0:..) does
    not lie in Y x Z and does satisfy them. The event of 2026-11-16 above had
    recorded that display as verified against the card; withdrawn. The true
    row-and-column reading holds each F_i in every column and each G_j in
    every row. (3) Step s2's identification of the Segre open with the affine
    product now says that it is the abstract affine product and so does not
    depend on the charts carrying the two factors. Not checked: Bertram's
    graded-ring display Y x Z = mproj(oplus R_d otimes Q_d), which the card
    does not use.

---

::: {.problem}
Use the Segre embedding to identify $\PP^n \times \PP^m$ with its image, and hence give it the structure of a projective variety.
Now let $X \subseteq \PP^n$ and $Y \subseteq \PP^m$ be quasi-projective varieties, and consider $X \times Y \subseteq \PP^n \times \PP^m$.

(a) Show that $X \times Y$ is a quasi-projective variety.

(b) If $X$ and $Y$ are both projective, show that $X \times Y$ is projective.

(c) Show that $X \times Y$ is a product in the category of varieties.
:::

::: {.solution}
Let
$$
S\subseteq\PP^N,
\qquad
N=nm+n+m,
$$
be the Segre variety from [[P-AGH214SEGRE]], with homogeneous coordinates $z_{ij}=x_i y_j$.
We identify the set $\PP^n\times\PP^m$ with $S$.

::: pf

::: {.pf-step #s1}

The two set-theoretic projections
$$
\pi_1:S\to\PP^n,
\qquad
\pi_2:S\to\PP^m
$$
are morphisms.

::: pf-proof

The opens
$$
D_+(z_{ij})\cap S
$$
cover $S$.
On such an open, the inverse construction in [[P-AGH214SEGRE]] recovers the first factor from the $j$th column and the second from the $i$th row:
$$
\pi_1([z_{ab}])=[z_{0j}:\cdots:z_{nj}],
$$
$$
\pi_2([z_{ab}])=[z_{i0}:\cdots:z_{im}].
$$
Because $z_{ij}\ne0$, neither displayed coordinate vector is zero.
Each formula is given by homogeneous linear forms and therefore defines a morphism on the chart.
The rank-one minor equations make these formulas agree on overlaps, so they glue to the stated morphisms.

:::

:::

::: {.pf-step #s2}

The subset $X\times Y\subseteq S$ is a quasi-projective variety, proving (a).

::: pf-proof

Since $X\subseteq\PP^n$ and $Y\subseteq\PP^m$ are locally closed and the projections are continuous,
$$
X\times Y
=
\pi_1^{-1}(X)\cap\pi_2^{-1}(Y)
$$
is locally closed in the projective variety $S$.

It remains to check irreducibility.
Choose affine open covers $\{U_\alpha\}$ of $X$ and $\{V_\beta\}$ of $Y$, refined so that each $U_\alpha$ lies in a standard affine chart of $\PP^n$ and each $V_\beta$ lies in a standard affine chart of $\PP^m$.
Then
$$
U_\alpha\times V_\beta
=
\pi_1^{-1}(U_\alpha)\cap\pi_2^{-1}(V_\beta)
$$
is open in $X\times Y$.
On the corresponding Segre chart $D_+(z_{ij})$, the row-and-column formulas of step [](#s1){.pf-ref} identify this open with the affine product of $U_\alpha$ and $V_\beta$.
That identification is with the abstract affine product of the two affine varieties, and so does not depend on which standard chart of $\PP^n$ carries $U_\alpha$ or which of $\PP^m$ carries $V_\beta$: the formulas are morphisms of the locally closed sets and are inverse to each other, and an affine variety's coordinate ring is the same on any open set that carries it.
It is therefore irreducible by [[P-AGH315AFFPRODUCT]].

Any two nonempty members $U_\alpha\times V_\beta$ and $U_{\alpha'}\times V_{\beta'}$ intersect: irreducibility of $X$ gives
$$
U_\alpha\cap U_{\alpha'}\ne\varnothing,
$$
and irreducibility of $Y$ gives
$$
V_\beta\cap V_{\beta'}\ne\varnothing.
$$
Moreover, their intersection is open in each product chart.
Fix one nonempty chart $U_{\alpha_0}\times V_{\beta_0}$.
For every other nonempty chart $U_\alpha\times V_\beta$, the intersection with the fixed chart is a nonempty open subset of the irreducible variety $U_\alpha\times V_\beta$, hence is dense in that chart.
Therefore every product chart is contained in the closure of the fixed irreducible chart.
The fixed chart is consequently dense in $X\times Y$, and its closure is irreducible.
Hence $X\times Y$ is irreducible.
Being irreducible and locally closed in projective space, it is quasi-projective.

:::

:::

::: {.pf-step #s3}

If $X$ and $Y$ are projective, then $X\times Y$ is projective.

::: pf-proof

In this case $X$ is closed in $\PP^n$ and $Y$ is closed in $\PP^m$.
Therefore
$$
X\times Y=\pi_1^{-1}(X)\cap\pi_2^{-1}(Y)
$$
is closed in $S$.
The Segre variety $S$ is projective by [[P-AGH214SEGRE]], and step [](#s2){.pf-ref} gives irreducibility.
Hence $X\times Y$ is a projective variety, proving (b).

:::

:::

::: {.pf-step #s4}

The restricted projections make $X\times Y$ a categorical product of $X$ and $Y$.

::: pf-proof

The restrictions
$$
p_X:X\times Y\to X,
\qquad
p_Y:X\times Y\to Y
$$
of the morphisms in step [](#s1){.pf-ref} are morphisms by [[P-AGH310SUBVARIETY]].

Now let $Z$ be a variety with morphisms
$$
f:Z\to X,
\qquad
g:Z\to Y.
$$
There is only one possible set map compatible with the projections:
$$
h:Z\to X\times Y,
\qquad
h(z)=(f(z),g(z)).
$$
To show that $h$ is a morphism, fix $z\in Z$.
Choose affine open neighborhoods $U\subseteq X$ of $f(z)$ and $V\subseteq Y$ of $g(z)$, each lying in a standard projective chart.
Then
$$
W=f^{-1}(U)\cap g^{-1}(V)
$$
is an open neighborhood of $z$.
On $W$, the pair $(f,g)$ lands in the affine product $U\times V$ and is a morphism by the universal property proved in [[P-AGH315AFFPRODUCT]].
The identification of that affine product with the corresponding Segre open is an isomorphism by the row-and-column formulas of step [](#s1){.pf-ref}.
Thus $h\restrict_W$ is a morphism.
Since such neighborhoods cover $Z$, $h$ is a morphism globally.

By construction
$$
p_X\circ h=f,
\qquad
p_Y\circ h=g,
$$
and uniqueness follows because these two coordinates determine every point of the Cartesian set $X\times Y$.
This proves (c).

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove (a)--(c), respectively.

:::

:::

:::

::: {.remark title="Published solution"}
The published argument is Aaron Bertram, *Algebraic Geometry* (Math 6130, University of Utah), Section 4, Proposition 4.3 and the paragraphs following it, printed pp. 5--6, text version `tmp/sources/bertram-utah-6130-varieties.md`: the Segre map "exhibits the product of projective spaces as a projective variety", the image is $V(\langle x_{ij}x_{kl}-x_{il}x_{jk}\rangle)$ with the two projections given by $\pi_1(\ldots:a_ib_j:\ldots)=(a_0b_0:\cdots:a_mb_0)$ and $\pi_2(\ldots:a_ib_j:\ldots)=(a_0b_0:\cdots:a_0b_n)$, and universality is proved by taking an open affine $U\subseteq W$ with $p_1(x)=(\varphi_0(x):\cdots:\varphi_m(x))$ and $p_2(x)=(\psi_0(x):\cdots:\psi_n(x))$ in $k(U)$, whereupon the unique set map is $f(x)=(\ldots:\varphi_i(x)\psi_j(x):\ldots)$, a morphism. That universality is proved for $W\to\PP^m\times\PP^n$, that is for the two projective spaces themselves, and it is stated "in the category of prevarieties"; his $X$ is irreducible, being a projective space, so there the prevariety and the variety coincide. For subvarieties he writes one sentence, "This extends in a straightforward manner to projective varieties", and the display that follows it is not correct: for closed $Y=V(\langle F_1,\ldots,F_a\rangle)$ and $Z=V(\langle G_1,\ldots,G_b\rangle)$ it gives
$$
Y\times Z=V(\langle F_i(x_{00},\ldots,x_{m0}),\ G_j(x_{00},\ldots,x_{0n})\rangle),
$$
which holds each $F_i$ in the zeroth column and each $G_j$ in the zeroth row only, so that every point of the Segre variety with $a_0=b_0=0$ satisfies it: $F_i$ and $G_j$ are homogeneous of positive degree, so both sides vanish at the origin of their column and row. That point need not lie in $Y\times Z$ --- for $Y=V(x_0)\subseteq\PP^m$ and $Z=V(y_0)\subseteq\PP^n$ the point $(1:0:\cdots:0)\times(0:1:0:\cdots:0)$ satisfies the display and is not in $Y\times Z$, its first factor lying outside $Y$. The statement that is true holds each $F_i$ under the substitution in every column and each $G_j$ in every row, since on the image of the Segre map a relation $F_i(a)=0$ is equivalent to $b_j^{d_i}F_i(a)=0$ for each nonzero $b_j$. What the source therefore publishes and what was checked against this card is the open case it states last, $U\times V=Y\times Z-\pi_2^{-1}(Z-V)-\pi_1^{-1}(Y-U)$, which is part (a) once $Y\times Z$ is known to be a variety, and the universality of the two projective spaces; parts (a) and (b) for subvarieties are steps [](#s2){.pf-ref} and [](#s3){.pf-ref} here, and part (c) for quasi-projective factors is step [](#s4){.pf-ref} together with the irreducibility of $X\times Y$ that makes it an object of Hartshorne's category, which is step [](#s2){.pf-ref} and is in no source found.

Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), text version `tmp/sources/hartshorne-solutions-borcherds.md`, gives no solution to 3.16.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 3.16, PDF p. 14, text version `tmp/sources/hartshorne-solutions-troiani.md`: for (a) and (b) he writes $X=Z(\mathfrak a)$, $Y=Z(\mathfrak b)$ and forms, for $f_1\in\mathfrak a$ and $f_2\in\mathfrak b$, the polynomial $g(\{z_{ij}\})=\sum_{i,j}\alpha_{ij}z_{ij}$ from the expansion of $f_1(x)f_2(y)$, so that $f_1(P_1)f_2(P_2)=0$ exactly when $g(\psi(P_1,P_2))=0$; he does not treat (c).
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.3.16, PDF p. 36, text version `tmp/sources/hartshorne-solutions-egbert.md`: $X\times Y=(X\times\PP^m)\cap(\PP^n\times Y)=\pi_m^{-1}(X)\cap\pi_n^{-1}(Y)$, and (b) "similar", with no (c).
The proof above constructs the two ambient projections on the Segre charts first, then gets (a) as local closedness together with irreducibility chart by chart, (b) as closedness in the projective variety $S$, and (c) as the affine universal property transported along those charts; the published sets reach (a) and (b) only, and neither writes the projections as morphisms.
Bertram's Proposition 4.3 proves (c) for two projective spaces, so that case is no longer only supplied here; the subvariety case and the irreducibility that Hartshorne's category needs remain the card's, as the entry above says.
:::

::: {.remark}
Part (c) is starred in the source.
:::
