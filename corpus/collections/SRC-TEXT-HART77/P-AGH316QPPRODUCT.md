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
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Third-pass reader's report on this card, each item checked against the
    Bertram text version. (1) The source-checked event of 2026-11-16 above was
    rewritten in place by 20b8b3a16b, which appended a correction to it, and
    4ab4e4ef6a then changed the witness inside that appended text; a dated
    event is not edited, so its text at its date is restored here and the
    correction is carried by this event. (2) The remark said "his X is
    irreducible, being a projective space". That is false: his X is the Segre
    variety V(<x_ij x_kl - x_il x_jk>), which he calls a projective variety at
    line 195, not a projective space. Its irreducibility, which Hartshorne's
    varieties require, is the case X = P^m, Y = P^n of step s2, whose affine
    charts are the products U_i x V_j with coordinate rings k[U_i] tensor
    k[V_j] (his Corollary 4.1); the remark now says that. (3) The witness of
    the event of 2026-11-16 that was added by 20b8b3a16b, Y = V(x_0),
    Z = V(y_0) and the point (1:0:..) x (0:1:0:..), is a valid witness to
    Bertram's false display, but not as an instance of the sentence before it:
    that point has a_0 = 1, not a_0 = b_0 = 0. It satisfies the display because
    b_0 = 0 kills the zeroth column, and the zeroth row is the second factor,
    which lies in V(y_0). So 4ab4e4ef6a's premise, that the witness itself
    needed correcting, is wrong; the sentence around it did. The remark and
    COMPLAINTS.md carry the witness that does fit the sentence, Y = V(x_1),
    Z = V(y_1) and (0:1:0:..) x (0:1:0:..), whose zeroth column and zeroth row
    both vanish; both witnesses are valid, and the two files agree on one.
    (4) The every-column-every-row reading of what is true is unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Three points on step s2 and the remark, from checks made on this pass. (1)
    Step s2 said that the identification "does not depend on which standard
    chart of PP^n carries U_alpha or which of PP^m carries V_beta ... and an
    affine variety's coordinate ring is the same on any open set that carries
    it". The last clause is false as stated: an open subset of an affine
    variety has its own coordinate ring, k[x, 1/x] for D(x) in A^1 against
    k[x]. What is true, and what the sentence needs, is that the affine product
    is determined by the two affine varieties themselves, through their
    coordinate rings, and not by the projective charts that carry them; the
    sentence now says that. (2) The remark's witness refutes Bertram's display
    inside his own hypothesis at line 227, which asks that Y and Z be defined
    by homogeneous prime ideals: V(x_1) and V(y_1) are prime, and the remark
    now says so. (3) The zeroth row of that witness is the second factor only
    because a_0 = 1 there; in general it is a_0 b, and
    G_j(a_0 b) = a_0^{deg G_j} G_j(b) = 0 with b in Z. The event of 2026-11-16
    above says "the second factor" of the example it has just given, where
    a_0 = 1, and this note records the general form.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.3.16,
    printed p. 22, all three parts, with (c) starred. Read each source at its
    cited place in its text version and checked it against that statement:
    Caligula's answer 3469579 (the two projections of P^n x P^m are morphisms;
    sigma(pi_1^{-1}(X) cap pi_2^{-1}(Y)) is an intersection of a closed and an
    open set, and the closed case is (b)); Parakee's accepted answer 1527360
    (irreducibility by the fibres of the first projection, with X_A closed
    because X x {y} -> X is a homeomorphism); Harris, Example 2.21, printed
    pp. 28-29 (the categorical product, with the regularity computation in the
    Segre coordinates, for quasi-projective factors); Fnark Man's accepted
    answer 5099544 (the affine-chart route to the same conclusion). Folios
    verified in the copies: Harris printed p. 28 is the page carrying "This
    space does not a priori have the structure of an algebraic variety", and
    Example 2.21 runs onto printed p. 29. Checked against the book: its
    varieties are irreducible (I.3, printed p. 15), so the irreducibility half
    of (a) is part of the question, and Harris's variety need not be
    irreducible, his Example 2.21 not proving it. Not checked: Bertram's
    graded-ring remark, which the card does not use.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the transcription of those sources, step by step, each
    step naming its source, numbered statement and printed page or answer id:
    s1 from answer 3469579 with the Segre-chart formulas as the working out,
    s2 from answers 3469579 and 1527360, s3 from 3469579's display in the
    closed case, s4 from Harris Example 2.21 with answer 5099544 beside it.
    Two things left the card. The irreducibility argument by affine product
    charts, which was the card's own, is replaced by answer 1527360's fibre
    argument; the affine product of I.3.15(c) now enters through answer
    5099544, and the relation to P-AGH315AFFPRODUCT stands on that. And the
    remark's Bertram paragraph, which argued that his Proposition 4.3 covers
    (c) up to irreducibility, is reduced to the erratum on his false display,
    (c) being Harris's. Nothing in the problem statement changes.

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
S\subseteq\PP^N,\qquad N=nm+n+m,
$$
be the Segre variety of [[P-AGH214SEGRE]], with homogeneous coordinates $z_{ij}=x_iy_j$, and let $\sigma:\PP^n\times\PP^m\to S$ be the Segre map; we identify $\PP^n\times\PP^m$ with $S$ through $\sigma$.
Harris, *Algebraic Geometry: A First Course* (1992), Example 2.21, printed p. 28, takes that identification as the definition of the product as a variety: "The Segre embedding, however, gives it one, which we will adopt as a definition of the product as a variety."

Each step names its source by author, numbered statement and printed page --- Harris's Example 2.21 on printed pp. 28--29, and the Math Stack Exchange answers 3469579, 1527360 and 5099544, which have no printed page and are cited by answer id --- and the remark at the end of the card quotes each source at the place cited and names its text version.

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

Answer 3469579: "Let $\pi_1,\pi_2$ be the two projection maps onto the two factors of $\PP^n\times\PP^m$. These maps are morphisms."
The charts on which that is checked are the following.

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

Write $X=U_X\cap Z_X$ and $Y=U_Y\cap Z_Y$ with $U_X\subseteq\PP^n$ and $U_Y\subseteq\PP^m$ open and $Z_X\subseteq\PP^n$ and $Z_Y\subseteq\PP^m$ closed.
Since $\pi_1$ and $\pi_2$ are continuous,
$$
X\times Y=\pi_1^{-1}(X)\cap\pi_2^{-1}(Y),
$$
and answer 3469579 computes its image under $\sigma$ as
$$
\begin{aligned}
\sigma\big(\pi_1^{-1}(X)\cap\pi_2^{-1}(Y)\big)
&=\sigma\big(\pi_1^{-1}(Z_X)\cap\pi_2^{-1}(Z_Y)\big)\\
&\qquad\cap\sigma\big(\pi_1^{-1}(U_X)\cap\pi_2^{-1}(U_Y)\big),
\end{aligned}
$$
"intersection of a closed set and an open set (recall that the Segre map is a homeomorphism)".
So $X\times Y$ is locally closed in $S$, which is locally closed in $\PP^N$.

Irreducibility is answer 1527360.
Suppose $X\times Y=A\cup B$, where $A$ and $B$ are closed subsets of $X\times Y$ and neither of them is $X\times Y$.
For $x\in X$ put
$$
F_x=\{x\}\times Y.
$$
The second projection carries $F_x$ homeomorphically onto $Y$, so $F_x$ is irreducible, and $F_x=(A\cap F_x)\cup(B\cap F_x)$ writes it as the union of two closed subsets; hence $F_x\subseteq A$ or $F_x\subseteq B$.
Put
$$
X_A=\{x\in X:F_x\subseteq A\},
\qquad
X_B=\{x\in X:F_x\subseteq B\}.
$$
Then $X=X_A\cup X_B$, and
$$
X_A=\bigcap_{y\in Y}\pi_1\big((X\times\{y\})\cap A\big),
$$
the two sides having the same elements: $x$ lies in the intersection exactly when $(x,y)\in A$ for every $y\in Y$, which is $F_x\subseteq A$.
For fixed $y$, the set $(X\times\{y\})\cap A$ is closed in $X\times\{y\}$, and $\pi_1$ carries $X\times\{y\}$ homeomorphically onto $X$, so its image is closed in $X$.
An intersection of closed sets is closed, so $X_A$ is closed, and in the same way $X_B$ is closed.
Since $X$ is irreducible and $X=X_A\cup X_B$, one of the two is $X$.
Then every fibre lies in $A$, or every fibre lies in $B$, so that $X\times Y=A$ or $X\times Y=B$, against the choice of $A$ and $B$.
Hence $X\times Y$ is irreducible.
Being irreducible and locally closed in $\PP^N$, it is a quasi-projective variety.

:::

:::

::: {.pf-step #s3}

If $X$ and $Y$ are projective, then $X\times Y$ is projective.

::: pf-proof

In this case $X$ is closed in $\PP^n$ and $Y$ is closed in $\PP^m$, that is $X=Z_X$ and $Y=Z_Y$ in the notation of step [](#s2){.pf-ref}, with $U_X=\PP^n$ and $U_Y=\PP^m$.
The second factor in the display of answer 3469579 is then $\sigma(\PP^n\times\PP^m)$, which is all of $S$, so that display says that $X\times Y$ is the first factor, the image under $\sigma$ of $\pi_1^{-1}(X)\cap\pi_2^{-1}(Y)$; hence $X\times Y$ is closed in $S$.
The Segre variety $S$ is projective by [[P-AGH214SEGRE]], and step [](#s2){.pf-ref} gives irreducibility.
Hence $X\times Y$ is a projective variety, proving (b).

:::

:::

::: {.pf-step #s4}

The restricted projections make $X\times Y$ a categorical product of $X$ and $Y$.

::: pf-proof

Harris, Example 2.21, printed pp. 28--29: "this is actually a categorical product, i.e., the projection maps $\pi_X:X\times Y\to X$ and $\pi_Y:X\times Y\to Y$ are regular and the variety $X\times Y$, together with these projection maps, satisfies the conditions for a product in the category of quasi-projective varieties and regular maps. What this means is that given an arbitrary variety $Z$ and a pair of maps $\alpha:Z\to X$ and $\beta:Z\to Y$, there is a unique map $\alpha\times\beta:Z\to X\times Y$ whose compositions with the projections $\pi_X$ and $\pi_Y$ are $\alpha$ and $\beta$, respectively.
It is not hard to see that this is the case: to begin with, the map $\alpha\times\beta$ is certainly uniquely determined by $\alpha$ and $\beta$; we have to check simply that it is regular.
This we do locally: say $r_0\in Z$ is any point, mapping via $\alpha$ and $\beta$ to points $p\in X$ and $q\in Y$.
Suppose $p$ lies in the open set $Z_0\ne0$ in $\PP^n$, so that in a neighborhood of $r_0$ the map $\alpha$ is given by
$$
\alpha:r\mapsto[1,f_1(r),\ldots,f_n(r)],
$$
with $f_1,\ldots,f_n$ regular functions of $r$ on $Z$, and say $\beta$ is given similarly by $\beta(r)=[1,g_1(r),\ldots,g_m(r)]$.
Then in a neighborhood of $r_0$ the map $\alpha\times\beta:Z\to X\times Y\subset\PP^{nm+n+m}$ is given by
$$
\alpha\times\beta:r\mapsto[1,\ldots,f_i(r),\ldots,g_j(r),\ldots,f_i(r)g_j(r),\ldots]
$$
and so is regular."

The restrictions
$$
p_X:X\times Y\to X,
\qquad
p_Y:X\times Y\to Y
$$
of step [](#s1){.pf-ref} are those projections, and the coordinates in the display are the coordinates $z_{ij}$ of the Segre embedding, so the composite is regular exactly where the source says it is.

Answer 5099544 reaches the same conclusion through the affine case: "we can use that the product of affine varieties is a product in the category of affine varieties (exercise 3.15(c)) and that any variety is covered by open affine subsets", so that for $Z$ a variety and $\phi:Z\to X$, $\psi:Z\to Y$ morphisms, the map $z\mapsto(\phi(z),\psi(z))$ "is a morphism of varieties because it is a morphism on any open affine subset of $Z$ by exercise 3.15(c). Uniqueness is clear", Exercise I.3.15(c) being [[P-AGH315AFFPRODUCT]].

This proves (c).

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove (a), (b) and (c), respectively.

:::

:::

:::

::: {.remark title="Published solution"}
The sources, with their text versions under `tmp/sources/`, and the place each is used.

Math Stack Exchange answers, cited by answer id because they have no printed page.

- Caligula, answer 3469579 to question 3469514, *Product of quasi-projective varieties is quasi-projective*: the two projections of $\PP^n\times\PP^m$ "are morphisms", and $\sigma(\pi_1^{-1}(X)\cap\pi_2^{-1}(Y))$ is an "intersection of a closed set and an open set (recall that the Segre map is a homeomorphism)", which is steps [](#s1){.pf-ref} and [](#s2){.pf-ref} in their first halves and step [](#s3){.pf-ref} once $X$ and $Y$ are closed. Text version `tmp/sources/mse-3469514-hart-i316-product-quasiprojective.md`.
- Parakee, accepted answer 1527360 to question 1527108, *The product of quasi-projective varieties is a quasi-projective variety*: the second half of step [](#s2){.pf-ref}. Its argument is that a fibre $\{x_i\}\times Y$ "is isomorphic to $Y$, hence irreducible", that therefore each fibre lies in $A$ or in $B$, and that $X_A=\bigcap_{y_i\in Y}\pi_1((X\times\{y_i\})\cap A)$ is closed; a comment on the answer asks for the closedness, which the homeomorphism $X\times\{y\}\to X$ supplies, and the same comment proposes replacing $\pi_1$ by $\pi_1^{-1}$, which is not needed, $\pi_1$ itself being the right map. Text version `tmp/sources/mse-1527108-hart-i316-product-quasiprojective-irreducible.md`.
- Fnark Man, accepted answer 5099544 to question 5099541, *Product of varieties is categorical product (Hartshorne)*: the affine-chart route to part (c) in step [](#s4){.pf-ref}. Text version `tmp/sources/mse-5099541-hart-i316c-categorical-product.md`.

Joe Harris, *Algebraic Geometry: A First Course*, Graduate Texts in Mathematics 133, Springer, 1992, Example 2.21, printed pp. 28--29: the definition of the product as the Segre image, the categorical product with the regularity computation in the coordinates $[1,\ldots,f_i,\ldots,g_j,\ldots,f_ig_j,\ldots]$, which is the main text of step [](#s4){.pf-ref}. Text version `tmp/sources/harris-1992-algebraic-geometry-first-course-pp17-36.md`.

Aaron Bertram, *Algebraic Geometry* (Math 6130, University of Utah), Section 4, Proposition 4.3 with the paragraphs following it, printed pp. 5--6, text version `tmp/sources/bertram-utah-6130-varieties.md`, is not used above and does not serve: his universality is stated "in the category of prevarieties" and proved for $W\to\PP^m\times\PP^n$, the extension to subvarieties being one sentence, and the display that follows it,
$$
Y\times Z=V(\langle F_i(x_{00},\ldots,x_{m0}),\ G_j(x_{00},\ldots,x_{0n})\rangle),
$$
is false as printed, since it holds each $F_i$ in the zeroth column and each $G_j$ in the zeroth row only: for $Y=V(x_1)\subseteq\PP^m$ and $Z=V(y_1)\subseteq\PP^n$ with $m,n\ge1$, both ideals prime, the point $(0:1:0:\cdots:0)\times(0:1:0:\cdots:0)$ has $a_0=b_0=0$, so its zeroth column and zeroth row vanish and it satisfies the display, while it lies outside $Y\times Z$. The true statement holds each $F_i$ under the substitution in every column, and each $G_j$ in every row, since on the image of the Segre map $F_i(a)=0$ is equivalent to $b_j^{d_i}F_i(a)=0$ for each nonzero $b_j$.

Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), text version `tmp/sources/hartshorne-solutions-borcherds.md`, gives no solution to 3.16; William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 3.16, PDF p. 14, and Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.3.16, PDF p. 36, prove (a) and (b) only --- Troiani by a bihomogeneous polynomial vanishing at the pair of points, Egbert by $X\times Y=(X\times\PP^m)\cap(\PP^n\times Y)$ --- and neither treats (c).
:::

::: {.remark}
Part (c) is starred in the source.
:::
