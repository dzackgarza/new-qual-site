---
schema: qual/card@1
id: P-AGH525INVARIANTE
kind: problem
title: Which values of the invariant $e$ occur for ruled surfaces over a curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.2.5, the retained Egbert companion argument for all four
    parts, and the surrounding ruled-surface normalization conventions. The
    proof below replaces the companion's elementary-transform construction in
    (a) by explicit nonsplit normalized extensions. In (b) it makes precise
    the Serre-dual pullback criterion behind the subspaces L_E. Part (c) uses
    the intended incidence variety in P H^1(O_C(-D)); its dimension is at most
    2d-3, strictly below g+d-2 when d<=g. For (d), both the printed exercise
    note and the retained companion cite Nagata's general theorem e>=-g.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.2,
    exercise 2.5, printed page 384, with the printed hint to the proof of (2.15)
    for part (b) and the printed Note for part (d). Checked every step of the
    card: Serre duality in steps s1 and s10; nonspeciality of K+D and of K+D-E
    from degree > 2g-2 for the Riemann-Roch counts of s10 and s11; the pullback
    square of s6 is the identification used in the book's proof of 2.15, and the
    projectivised image of multiplication by the canonical section of O(F) is
    |K+D-F|+F; the incidence variety of s12 sits in Sym^{d-1}C x P(V^*), so its
    dimension is at most 2d-3 against dim P(V^*) = g+d-2, and both the dimension
    and the properness of the image were checked. Searched outside the twelve
    retained sets: Algebraic Geometry II, National Taiwan University, 2020
    Spring, Chapter V homework (tmp/sources/ntu-ag2-chapter5.pdf), which has no entry for Exercise 5 of
    section 2; Yang Pi-Yeh, Hartshorne Solutions, exercise 5.2.5, printed p. 103
    (tmp/sources/lfwin-hartshorne-solutions.pdf), which treats all four parts
    and whose (a) infers a nonzero section from nonnegative degree, an inference
    that fails for e >= g-1, so (a) is not a complete published proof; Egbert,
    PDF pp. 263-264, proves (b) and cites Fuentes-Pedreira and Maruyama for (a)
    and (c). Not checked: Nagata's theorem quoted in step s15 is not in
    tmp/sources, so part (d) rests on the printed Note alone.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Fuentes and Pedreira (arXiv:math/0006204v3) on 2026-11-16. Its Theorem
    3.2, printed p. 15, restates the book's Theorem V.2.12 with the sharper lower
    bound: a decomposable normalized bundle forces e at least zero, and an
    indecomposable one gives -g <= e <= 2g-2, where the book's own proof reaches
    only e >= -2g and sends the stronger restriction to its Exercise 2.5. Its proof is the citation "See [8], V, 2.12 and [15]", so it
    adds no argument of its own and does not reach part (a)'s existence statement
    for every e in the interval from 0 to 2g-2, nor part (c)'s range from -g to
    below zero. The lower bound is Nagata's, cited as the printed Note, as the
    paper's reference [15] and in its introduction, where it says the theorem of
    Segre that e >= -g was proved by Nagata in [15]; that reference is M. Nagata,
    "On self-intersection number of a section on a ruled surface", Nagoya Math.
    J. 37 (1970), 191-196, which is also Hartshorne's own reference [8] for the
    Note, and it is not readable from here. Math StackExchange question 4398506,
    saved as tmp/sources/mse-4398506-hart77-v25-linear-system-notation.md,
    concerns only the notation of part (b). No complete published argument for
    (a) or (c) was located; steps s1 to s3 and s10 to s12 remain the card's.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Fuentes--Pedreira's Theorem 4.12(4), printed pp. 31--32, which Egbert
    cites for part (a), and Nagata's coordinates for part (d), on 2026-11-16.
    Theorem 4.12(4): for a decomposable geometrically ruled surface, an
    elementary transformation at a point x outside both X_0 and X_1, over a point
    P of the base that is a base point of -e, produces an indecomposable surface
    with e' = e - 1 and minimum self-intersection curve X_0'. That is the paper's
    only construction of an indecomposable ruled surface, and it moves the
    invariant down by one from a decomposable surface rather than producing every
    value in 0 <= e <= 2g-2 from one statement; Egbert's citation of it for part
    (a) is therefore a pointer to one step of a construction, not an argument for
    the exercise. The lower bound used everywhere above is e >= -g, not -2g: the
    paper's Theorem 3.2(2), printed p. 15, gives -g <= e <= 2g-2 for an
    indecomposable normalized bundle and cites Hartshorne V.2.12 and its own
    reference [15], and its introduction attributes the theorem e >= -g to Segre
    and its proof to Nagata in [15]. Reference [15] is M. Nagata, "On
    self-intersection number of a section on a ruled surface", Nagoya Math. J. 37
    (1970), 191-196, the same paper Hartshorne's Note cites as his [8]. Nagata's
    statement itself was not read: Project Euclid serves an automated-access check
    for its PDF and Cambridge Core holds the article for subscribers, so part (d)
    still rests on the printed Note, on the paper's Theorem 3.2(2) and on that
    introduction, and it is listed open in COMPLAINTS for that reason. Not
    checked: whether Theorem 4.12(4) iterates, since its hypothesis asks for a
    decomposable surface and its conclusion is an indecomposable one.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Re-read Theorem 4.12(4) against its proof in the text version of Fuentes and
    Pedreira on 2026-11-16 and corrected the earlier reading of it, and made step
    s15 say what it is. That theorem does not need to be iterated: applied once
    to the decomposable surface with invariant e+1 it returns an indecomposable
    surface with invariant (e+1)-1 = e, and the decomposable surfaces of every
    invariant e >= 0 exist by the book's Theorem 2.12(a) and by the paper's own
    Theorem 3.2(1), so one application reaches every 0 <= e <= 2g-2. What the
    theorem asks for and the paper does not construct is the point P of the base
    that is a base point of the linear system of -me; it exists whenever h^0(-me) = 1, the system
    then having the single member -me whose support is its base locus, and in
    general it is a condition on the divisor class. The events above say that the
    theorem is "one step of a construction" and this card's remark said the same;
    both now say that one application suffices given such a P, and the card does
    not claim part (a) closed on the theorem. Step s15 is now what it should have
    been: part (d) is the case g = 2 of the printed Note and of Nagata's paper
    behind it, nothing in tmp/sources proves it, and the book's own argument in
    Theorem 2.12 reaches only e >= -2g, that is e >= -4 at g = 2, the dimension
    count of step s12 covering d <= g only. The events above and the earlier
    step said nothing false about the bound itself but the qed claimed part (d)
    proved, which it is not.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Transcribed all four parts on 2026-11-16 from sources read in their text
    versions, and re-read the printed exercise at Hartshorne, Algebraic
    Geometry (1977), V.2, exercise 2.5, printed p. 384 (PDF p. 399), with its
    hint and its Note. (a) is Gunning, Lectures on vector bundles over Riemann
    surfaces, Theorem 13, printed pp. 71-74, which identifies extension classes
    with a first cohomology group and the split extension with the zero class,
    and Theorem 14, printed pp. 87-90, which parametrizes the indecomposable
    bundles with a given subbundle and determinant by the points of a projective
    space; with phi = O and xi of degree -e the space is P H^1(L^{-1}), nonzero
    by Serre duality once an effective A of degree 2g-2-e is chosen, which is
    the duality half of the book's own proof of Theorem 2.12, printed p. 376.
    The normalization argument of steps s2 and s3 is Example 2.11.6, printed
    p. 375, whose exceptional case M = L(-P) is shown on the card not to arise
    when deg L is at most 0. (b) is Lange-Narasimhan Proposition 1.1, printed
    p. 57, and Lemma 2.3, printed pp. 58-59, whose displayed criterion is the
    kernel of the canonical map H^0(K tensor L)^* to H^0(K tensor L(-D))^*, in
    both directions; the book's proof of Theorem 2.15, printed pp. 377-379,
    uses the normalized implies injective half. Pages were established from the
    PDFs' printed folios, printed page = PDF page + 53 for Lange-Narasimhan.
    (c) is their Corollary 1.2, printed p. 58, applied to line bundles of
    degrees d and 2d with d = -e, so that the extension's subbundle has degree
    d and its twist by the inverse of that subbundle is normalized with
    determinant of degree d; the genus one case e = -1 is Example 2.11.6 and
    Theorem 2.15, printed pp. 375 and 377-378. (d) is Lange, Higher secant
    varieties of curves and the theorem of Nagata on ruled surfaces, §1 Theorem,
    printed p. 266, and §2 Theorem s(E) at most g, printed pp. 267-268, with
    s(E) = c_1(E) - 2 max c_1(L), which for a normalized bundle is
    deg det = -e, giving e at least -g and hence e at least -2 at g = 2. Read
    check: the paper's proof begins by reducing to extensions with quotient of
    degree d > 3 and does not spell the reduction out; its §1 needs only d at
    least 2 when g is at least 2. Not checked: Nagata's own paper, still behind
    an automated-access check; nothing on the card now rests on it.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the card against its sources again on 2026-11-16, after the event
    above of the same date. Four corrections. Gunning's Theorem 13 is now quoted
    with his convention: phi_1 is the subbundle and phi_2 the quotient, and the
    classes lie in H^1(phi_1 phi_2^{-1}), which for the extension 0 to O to E to
    L to 0 is H^1(L^{-1}) directly, not H^1(L) as the previous wording had it.
    Part (b) no longer cites Lemma 2.3: that lemma characterizes a degree-zero
    line bundle M, other than O, being a maximal subbundle of an E with
    s(E) = d, and it is not the criterion of (b); Proposition 1.1, printed
    p. 57, is, and it is now cited alone, with its standing hypothesis d at
    least 2 for g at least 2 of the paper's section 1, so that d = 1 and g = 1
    lie outside it. Step s3 now states the inclusion O = A tensor A^{-1} inside
    E tensor A^{-1} that carries a section of A to one of the twist. The
    hypotheses of the quoted statements are stated where they are used: Gunning
    works over a compact Riemann surface, Lange and Narasimhan over an
    algebraically closed field of characteristic zero (their introduction), and
    part (d)'s paper over an algebraically closed field of arbitrary
    characteristic. Part (d) is now stated as proved: the text version's OCR
    reads "d > 3" in the paper's reduction, while the scan of printed p. 267
    reads "d >= 3", so the earlier claim that the reduction is unargued is
    withdrawn, the case s(E) at most 2 being trivial for g at least 2. The
    remark's step references are renumbered to the present steps, and it no
    longer carries machine paths or says which sources were not read. Not
    checked: (b) at d = 1 and at g = 1, and parts (a), (b), (c) in positive
    characteristic; nothing read supplies them, and the card does not claim
    them.
---

::: {.problem}
Let $C$ be a curve of genus $g \geqslant 1$.

(a) Show that for each $0 \leqslant e \leqslant 2 g-2$ there is a ruled surface $X$ over $C$ with invariant $e$, corresponding to an indecomposable $\mathcal{E}$.
Cf.
(2.12).

(b) Let $e<0$, let $D$ be any divisor of degree $d=-e$, and let $\xi \in H^1(\mathcal{L}(-D))$ be a nonzero element defining an extension
$$
0 \rightarrow \OO_C \rightarrow \mathcal{E} \rightarrow \mathcal{L}(D) \rightarrow 0 .
$$
Let $H \subseteq\linearsystem{D+K}$ be the sublinear system of codimension 1 defined by $\ker \xi$, where $\xi$ is considered as a linear functional on $H^0(\mathcal{L}(D+K))$.
For any effective divisor $E$ of degree $d-1$, let $L_E \subseteq\linearsystem{D+K}$ be the sublinear system $\linearsystem{D+K-E}+E$.
Show that $\mathcal{E}$ is normalized if and only if for each $E$ as above, $L_E \nsubseteq H$.
Cf.
proof of $(2.15)$.

(c) Now show that if $-g \leqslant e<0$, there exists a ruled surface $X$ over $C$ with invariant $e$.

Hint: For any given $D$ in (b), show that a suitable $\xi$ exists, using an argument similar to the proof of (II, 8.18).

(d) For $g=2$, show that $e \geqslant-2$ is also necessary for the existence of $X$.

Note.
It has been shown that $e \geqslant-g$ for any ruled surface (Nagata [8]).

:::

::: {.solution}
Recall that a rank-two bundle $\mathcal E$ on $C$ is normalized when
$$
H^0(C,\mathcal E)\ne0
$$
but $H^0(C,\mathcal E\tensor\mathcal M)=0$ for every invertible sheaf $\mathcal M$ of negative degree, Proposition 2.8, printed p. 372, and that for such a bundle the invariant of $X=\PP(\mathcal E)$ is $e=-\deg\det\mathcal E$, Notation 2.8.1, printed p. 373.

Part (a) is transcribed from Gunning, *Lectures on vector bundles over Riemann surfaces*, Theorem 13, printed pp. 71--74, and Theorem 14, printed pp. 87--90, together with the duality half of Hartshorne's proof of Theorem 2.12, printed p. 376; part (b) from Proposition 1.1, printed p. 57, of Lange and Narasimhan, *Maximal subbundles of rank two vector bundles on curves*, whose statement is the criterion that the printed "Cf. proof of (2.15)" points at, that is the proof of Theorem 2.15, printed pp. 377--379; part (c) from their Corollary 1.2, printed p. 58, with Example 2.11.6, printed p. 375, for genus one; part (d) from Lange, *Higher secant varieties of curves and the theorem of Nagata on ruled surfaces*, §2 Theorem, printed pp. 267--268. Lange and Narasimhan work over an algebraically closed field of characteristic zero and Gunning over a compact Riemann surface; where a quoted statement's hypotheses are narrower than the exercise's, the step that quotes it says so.

::: pf

::: {.pf-step #s1}
Fix
$$
0\le e\le2g-2.
$$
There is an invertible sheaf $\mathcal L$ of degree $-e$ with
$$
\Ext^1_C(\mathcal L,\OO_C)\ne0 .
$$

::: pf-proof
Choose an effective divisor $A$ of degree $2g-2-e$ and put $\mathcal L=\OO_C(A-K_C)$; then $\deg\mathcal L=-e$ and
$$
\Ext^1_C(\mathcal L,\OO_C)\cong H^1(C,\mathcal L^{-1})=H^1\qty(C,\OO_C(K_C-A)),
$$
which is Theorem 13 of Gunning, printed pp. 71--74. In his notation an extension $0\to\OO(\varphi_1)\to\OO(\Phi)\to\OO(\varphi_2)\to0$ has $\varphi_1$ the subbundle and $\varphi_2$ the quotient, and its classes are the elements of $H^1(C,\OO(\varphi_1\varphi_2^{-1}))$; for $\varphi_1=\OO_C$ and $\varphi_2=\mathcal L$ that group is $H^1(C,\OO_C(\mathcal L^{-1}))$, the group of the extension above. Serre duality gives
$$
H^1\qty(C,\OO_C(K_C-A))^\vee\cong H^0(C,\OO_C(A)),
$$
which is nonzero because $A$ is effective. This is the duality step of the proof of Theorem 2.12, printed p. 376, read in the other direction: there $H^1(\mathcal L^\vee)\ne0$ forces $\deg\mathcal L^\vee\le2g-2$, which for the present $\mathcal L$ is the inequality $e\le2g-2$.

:::

:::

::: {.pf-step #s2}
A nonzero class of step [](#s1){.pf-ref} defines a normalized extension
$$
0\longrightarrow\OO_C
\longrightarrow\mathcal E
\longrightarrow\mathcal L
\longrightarrow0 .
$$

::: pf-proof
The argument is that of Example 2.11.6, printed p. 375. The inclusion of $\OO_C$ gives $H^0(C,\mathcal E)\ne0$. Let $\mathcal M$ have negative degree and tensor the sequence by it:
$$
0\longrightarrow\mathcal M
\longrightarrow\mathcal E\tensor\mathcal M
\longrightarrow\mathcal L\tensor\mathcal M
\longrightarrow0 .
$$
Both end terms have negative degree, $\deg\mathcal L\tensor\mathcal M=-e+\deg\mathcal M<0$ because $e\ge0$, so $H^0(\mathcal M)=H^0(\mathcal L\tensor\mathcal M)=0$ and the long exact sequence gives $H^0(C,\mathcal E\tensor\mathcal M)=0$. The exceptional case the book separates at $\mathcal M=\mathcal L(-P)$, where the end term is $\OO_C$ and the coboundary is the class $\xi$, does not arise here, since $\mathcal L\tensor\mathcal M\cong\OO_C$ forces $\deg\mathcal M=e\ge0$.

:::

:::

::: {.pf-step #s3}
The bundle $\mathcal E$ of step [](#s2){.pf-ref} is indecomposable.

::: pf-proof
Gunning, Theorem 13, printed pp. 71--74, attaches the split extension to the zero class, so a nonzero class gives a nonsplit sequence. Suppose then that $\mathcal E\cong\mathcal A\oplus\mathcal B$ with $\mathcal A,\mathcal B$ invertible. Since $H^0(C,\mathcal E)\ne0$, one summand, say $\mathcal A$, has a nonzero section and hence $\deg\mathcal A\ge0$; normalization bounds $\deg\mathcal A\le0$ because the inclusion $\OO_C=\mathcal A\tensor\mathcal A^{-1}\subseteq\mathcal E\tensor\mathcal A^{-1}$ carries a nonzero section of $\mathcal A$ to one of $\mathcal E\tensor\mathcal A^{-1}$, and $\deg\mathcal A^{-1}<0$. So $\mathcal A\cong\OO_C$ and $\mathcal B\cong\det\mathcal E\cong\mathcal L$. If $\mathcal L$ is not trivial then $H^0(C,\mathcal L)=0$, since $\deg\mathcal L=-e\le0$, so the injection $\OO_C\to\OO_C\oplus\mathcal L$ lands in the first summand and splits; if $\mathcal L\cong\OO_C$ it is a nonzero constant vector, and a constant change of basis splits it as well. Either way the extension splits, contradicting the choice of a nonzero class.

:::

:::

::: {.pf-step #s4}
For every $0\le e\le2g-2$ there is an indecomposable $\mathcal E$ with
$$
-\deg\det\mathcal E=e,
$$
so that $X=\PP(\mathcal E)$ is a ruled surface with invariant $e$. This proves part (a).

::: pf-proof
By step [](#s2){.pf-ref} the bundle is normalized, so the invariant of $\PP(\mathcal E)$ is $-\deg\det\mathcal E$ by Notation 2.8.1, printed p. 373, and $\deg\det\mathcal E=\deg\mathcal L=-e$; step [](#s3){.pf-ref} gives indecomposability. Theorem 14 of Gunning, printed pp. 87--90, is the existence statement in this form: for line bundles $\varphi$ and $\xi$ with $c(\varphi)\ge\frac12c(\xi)$ and determinant $\xi$, the indecomposable bundles with subbundle $\varphi$ and determinant $\xi$ are parametrized by the points of $\PP H^1(C,\OO(\varphi^2\xi^{-1}))$, which for $\varphi=\OO_C$ and $\xi=\mathcal L$ is $\PP H^1(C,\mathcal L^{-1})$, nonempty by step [](#s1){.pf-ref}; the bundle produced there is the extension of step [](#s2){.pf-ref}, whose normalization and indecomposability are steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}
For part (b), the class $\xi$ of the extension
$$
0\longrightarrow\OO_C\longrightarrow\mathcal E\longrightarrow\OO_C(D)\longrightarrow0
$$
is a nonzero linear functional on $V=H^0(C,\OO_C(K_C+D))$, and the subsystem $H\subseteq\linearsystem{D+K}$ of codimension one is $\PP(\ker\xi)$.

::: pf-proof
The identification of extension classes with $H^1(C,\OO_C(-D))$ is Gunning, Theorem 13, printed pp. 71--74, and the duality $H^1(C,\OO_C(-D))^\vee\cong H^0(C,\OO_C(K_C+D))$ is Serre duality; that is the interpretation the exercise states, and the book's proof of Theorem 2.15 uses the class in exactly this form, as an element of $H^1(\mathcal L(-P-Q))$ dual to $H^0(\mathcal L(P+Q))$, printed p. 378.

:::

:::

::: {.pf-step #s6}
For an effective divisor $F$ with $\deg F\le d-1$, pulling the extension back along $\OO_C(D-F)\hookrightarrow\OO_C(D)$ gives a class
$$
\beta_F(\xi)\in H^1(C,\OO_C(F-D)),
$$
and
$$
\boxed{\beta_F(\xi)=0\iff L_F\subseteq H},
\qquad
L_F=\linearsystem{K_C+D-F}+F.
$$

::: pf-proof
This is the criterion of Lange and Narasimhan, Proposition 1.1, printed p. 57, in its two directions. The inclusion is multiplication by a section $s_F$ of $\OO_C(F)$, so under Serre duality the dual of $\beta_F$ is
$$
H^0(C,\OO_C(K_C+D-F))\xrightarrow{\cdot s_F}H^0(C,\OO_C(K_C+D)),
$$
whose projective image is $L_F$; hence the pullback splits exactly when $\xi$ annihilates that image, that is when $L_F\subseteq H$. Proposition 1.1 states them as the equivalence of $\mathrm{(i)}$ and $\mathrm{(ii)}$ for one extension $0\to\OO_X\to E\to L\to0$: the class lies in the span of an effective divisor $D$ exactly when $L(-D)$ is a subsheaf of $E$, which is the splitting of the pullback. Its §1 assumes $d\ge2$ when $g\ge2$, and it works over an algebraically closed field of characteristic zero; the cases $d=1$ and $g=1$ are outside it, and steps [](#s7){.pf-ref} and [](#s8){.pf-ref} use only the pullback square.

:::

:::

::: {.pf-step #s7}
If an effective divisor $E$ of degree $d-1$ satisfies $L_E\subseteq H$, then $\mathcal E$ is not normalized.

::: pf-proof
Step [](#s6){.pf-ref} gives $\beta_E(\xi)=0$, so the pullback
$$
0\longrightarrow\OO_C\longrightarrow\mathcal E_E\longrightarrow\OO_C(D-E)\longrightarrow0
$$
splits, and the splitting followed by $\mathcal E_E\to\mathcal E$ embeds $\OO_C(D-E)$ in $\mathcal E$; its inverse has degree $-1$, so a negative twist of $\mathcal E$ has a nonzero section. This is the implication the book uses in the proof of Theorem 2.15, printed p. 378: normalization makes the map $\gamma$ injective, which is the statement that no $L_E$ lies in $H$.

:::

:::

::: {.pf-step #s8}
Conversely, if $\mathcal E$ is not normalized, some effective divisor $E$ of degree $d-1$ satisfies $L_E\subseteq H$.

::: pf-proof
There is a line bundle $\mathcal M$ of negative degree and a nonzero morphism $\mathcal M^{-1}\to\mathcal E$; saturating its image gives a subbundle $\mathcal A\hookrightarrow\mathcal E$ of positive degree $a$. Its composite with the quotient $\mathcal E\to\OO_C(D)$ is nonzero, since a zero composite would factor $\mathcal A$ through $\OO_C$, whereas a nonzero section of $\mathcal A^{-1}$ would impose a negative twist on $\mathcal E$. A nonzero map $\mathcal A\to\OO_C(D)$ has an effective zero divisor $F$, so $\mathcal A\cong\OO_C(D-F)$ with $\deg F=d-a\le d-1$, and the inclusion already lifts to $\mathcal E$, so the pullback splits and $L_F\subseteq H$ by step [](#s6){.pf-ref}. Choosing an effective $T$ of degree $a-1$ and setting $E=F+T$ gives $\deg E=d-1$ and $L_E\subseteq L_F\subseteq H$. This is the converse implication of Proposition 1.1 of Lange and Narasimhan, printed p. 57, under its hypothesis $d\ge2$; steps [](#s7){.pf-ref} and [](#s8){.pf-ref} prove part (b).

:::

:::

::: {.pf-step #s9}
If $-g\le e<0$ and $g\ge2$, there is a ruled surface over $C$ with invariant $e$. This is part (c) for $g\ge2$.

::: pf-proof
Put $d=-e$, so $1\le d\le g$, and let $L_1,L_2$ be line bundles with $\deg L_1=d$ and $\deg L_2=2d$. Corollary 1.2 of Lange and Narasimhan, printed p. 58, applies with $0<c_1(L_2)-c_1(L_1)=d\le g$ and produces an extension
$$
0\longrightarrow L_1\longrightarrow\mathcal E\longrightarrow L_2\longrightarrow0
$$
whose maximal subbundle degree is $d$, and its proof is a dimension count: $\dim\mathrm{Sec}_{d-2}(X)\le2d-3<g+d-2=\dim\PP$ in the notation of its §1, which is the count the exercise's hint asks for. Tensoring by $L_1^{-1}$ gives
$$
0\longrightarrow\OO_C\longrightarrow\mathcal E\tensor L_1^{-1}\longrightarrow L_2L_1^{-1}\longrightarrow0,
$$
in which the maximal subbundle degree has dropped to $0$; so $\mathcal E\tensor L_1^{-1}$ is normalized, having a nonzero section and no nonzero section after a negative twist. Its determinant is $L_2L_1^{-1}$ of degree $d$, so $\PP(\mathcal E\tensor L_1^{-1})$ has invariant $-d=e$ by Notation 2.8.1, printed p. 373. Corollary 1.2 is stated for $g\ge2$ over an algebraically closed field of characteristic zero; the genus-one case is step [](#s10){.pf-ref}.

:::

:::

::: {.pf-step #s10}
If $g=1$ and $-g\le e<0$, that is $e=-1$, there is a ruled surface over $C$ with invariant $e$.

::: pf-proof
This is Example 2.11.6, printed p. 375, which constructs $\mathcal E$ as an extension $0\to\OO_C\to\mathcal E\to\mathcal L(P)\to0$ with $\xi\ne0$, shows it normalized by the long exact sequence of the twisted sequence, and concludes that $\PP(\mathcal E)$ is an elliptic ruled surface with $e=-1$; the proof of Theorem 2.15, printed pp. 377--378, repeats the construction and shows that it is the only one. Steps [](#s9){.pf-ref} and [](#s10){.pf-ref} prove part (c).

:::

:::

::: {.pf-step #s11}
For $g=2$ the inequality
$$
e\ge-2
$$
holds for every ruled surface over $C$. This is part (d), and more generally $e\ge-g$.

::: pf-proof
Let $\mathcal E$ be the normalized bundle of $X$, so that $e=-\deg\det\mathcal E$ by Notation 2.8.1. Lange, *Higher secant varieties of curves and the theorem of Nagata on ruled surfaces*, §2, printed pp. 267--268, defines
$$
s(\mathcal E)=c_1(\mathcal E)-2\max c_1(\mathcal L),
$$
the maximum over the sublinebundles $\mathcal L\subseteq\mathcal E$, and proves the Theorem $s(\mathcal E)\le g$. His proof is the dimension theorem of §1, printed p. 266, that the $n$-secant variety of a nondegenerate curve in $\PP^N$ has dimension $\min(2n-1,N)$, applied to $C$ embedded by $\linearsystem{K_C\otimes L}$ together with the §2 Lemma that a class lying in $\mathrm{Sec}_n(C)$ forces $s(\mathcal E)\le2n-d$; the maximum is $0$ for a normalized bundle, since $H^0(\mathcal E)\ne0$ gives a subbundle of nonnegative degree and normalization excludes a positive one, so $s(\mathcal E)=\deg\det\mathcal E=-e$ and $-e\le g$. At $g=2$ this is $e\ge-2$, which is the bound the printed Note attributes to Nagata and which the book's own proof of Theorem 2.12 does not reach, arriving only at $e\ge-2g$. The paper's proof supposes an exact sequence $0\to\OO_C\to\mathcal E\to L\to0$ with $\deg L=d\ge3$, printed p. 267; for $g\ge2$ the case $s(\mathcal E)\le2$ already satisfies the conclusion, and for $d\ge3$ the lemma gives $s(\mathcal E)\le2\floor{(d+g)/2}-d\le g$. The paper states its field as an algebraically closed field of arbitrary characteristic.

:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove part (a), steps [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} prove part (b), steps [](#s9){.pf-ref} and [](#s10){.pf-ref} prove part (c), and step [](#s11){.pf-ref} proves part (d).

:::

:::

:::

::: {.remark title="Published solution"}
(a) Gunning's Theorem 13, printed pp. 71--74, identifies the extensions of one line bundle by another with a first cohomology group, and his Theorem 14, printed pp. 87--90, parametrizes the indecomposable bundles with a given subbundle $\varphi$ and determinant $\xi$ by the points of $\PP H^1(C,\OO(\varphi^2\xi^{-1}))$; with $\varphi=\OO_C$ and $\xi$ of degree $-e$ that space is $\PP H^1(C,\mathcal L^{-1})$, nonempty by Serre duality, which is steps [](#s1){.pf-ref} to [](#s4){.pf-ref}. Gunning works over a compact Riemann surface.

(b) Lange and Narasimhan, Proposition 1.1, printed p. 57, is the criterion the printed "Cf. proof of (2.15)" points at, and the book's proof of Theorem 2.15, printed pp. 377--379, runs one direction of it: normalization makes the map $\gamma$ injective. Their Proposition 1.1 assumes $d\ge2$ when $g\ge2$, so the cases $d=1$ and $g=1$ lie outside it, and their field is an algebraically closed field of characteristic zero.

(c) Their Corollary 1.2, printed p. 58, gives for $g\ge2$ and $0<c_1(L_2)-c_1(L_1)=s\le g$ an extension with $s(E)=s$; with line bundles of degrees $d$ and $2d$, $d=-e$, its twist by the inverse of the subbundle has invariant $e$. Their proof is the dimension count $\dim\mathrm{Sec}_{s-2}(X)\le2s-3<g+s-2=\dim\PP$ that the exercise's hint asks for, over a field of characteristic zero.

(d) Lange, *Higher secant varieties of curves and the theorem of Nagata on ruled surfaces*, §2, printed pp. 267--268, proves $s(E)\le g$ for every rank-two bundle, over an algebraically closed field of arbitrary characteristic; for a normalized bundle $s(E)=\deg\det E=-e$, so $e\ge-g$, and $e\ge-2$ at $g=2$. That is the bound the printed Note attributes to Nagata [8].

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.5. Part (b) he proves: with $\xi\in H^1(\mathcal L(-D))$ the class of the extension and $\gamma:H^0(\mathcal L(D+K-E))\to H^1(\mathcal L(-E))$, injectivity of $\gamma$ is equivalent to $\mathcal E$ being normalized, and he runs the commutative square with $H^0(\OO_C)\to H^1(\mathcal L(-D))\to H^1(\mathcal L(-E))$ in both directions. For (a) he writes "This will get us all invariants for this problem with the help of thm V.2.12. This is F,P thm 4.12.4", a citation to Fuentes--Pedreira's Theorem 4.12(4), printed pp. 31--32, which takes a decomposable surface and an elementary transformation at a point outside $X_0$ and $X_1$ over a base point $P$ of $-\mfe$ and returns an indecomposable surface with invariant $e-1$; one application to the decomposable surface of invariant $e+1$ gives an indecomposable surface of invariant $e$, the base point $P$ being the one condition the theorem asks for. For (c) he writes "By proof of (a), I only need to find one with invariant $-g$ ... This is given by 3.13 in Maruyama", a citation to Maruyama. Part (d) he answers "By Theorem 1 in Nagata 'Self-intersection number'", which is the source of the printed Note, and step [](#s11){.pf-ref} now gives that bound from Lange's Theorem instead.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.5, printed p. 103, treats all four parts. For (a) it argues that $\Ext^1(\mathcal L,\OO_C)\cong H^0(C,\omega_C\tensor\mathcal L)$ "and $\deg\omega_C\tensor\mathcal L=2g-2-e\ge0$, hence $\Ext^1$ is nontrivial": a line bundle of nonnegative degree on a curve of genus $g$ need not have a section, and the correct bound is $h^0\ge\deg-g+1=g-1-e$, which is negative for $e\ge g-1$. Step [](#s1){.pf-ref} avoids the issue by taking $\mathcal L=\OO_C(A-K_C)$ with $A$ effective, so that $H^0(\OO_C(A))\ne0$ directly. Its (b) is the square of step [](#s6){.pf-ref} written out; its (c) is the dimension count of step [](#s9){.pf-ref}; its (d) is garbled ("all $\ker\xi$ form the Grassmannian $G^{d+1}_d$, which has dimension $d$ ... so we have $d\le2(d-1)$").

Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework solutions, has no entry for Exercise 5 of §2.
:::
