---
schema: qual/card@1
id: P-AGH374COHOMCLASS
kind: problem
title: The cohomology class of a subvariety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Duality
  - Sheaves of Differentials
  - Intersection Theory
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: "Read Exercise III.7.4, the definition and uniqueness of a dualizing sheaf with trace in III.7.1--7.2, the canonical-sheaf identification III.7.11--7.13, and Hartshorne's warning in III.7.14 that the preceding construction gives little explicit information about the trace. The source exercise suppresses a necessary normalization: scaling the trace on a smooth subvariety scales its class. The statement below makes the standard trace/Gysin normalization explicit before proving the four requested assertions."
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step pass against the book. III.7.1(a) printed p. 240 (Fix one
    such isomorphism), III.7.2 p. 241 (the trace is part of the dualizing
    pair), III.7.1.1 pp. 240-241 (the Cech cocycle generator), III.7.12 p.
    246, III.7.13 p. 247 (the duality isomorphism the exercise uses),
    III.7.14 p. 247 (the trace is known only to exist), III.7.14.1(c) p. 247
    (res_P f^-1 df = v_P(f)), Appendix A C1 p. 430 (c_1(L(D)) = D), II.8.18
    p. 179 (Bertini, every characteristic), I.7.7 p. 53 (Bezout), Exercise
    7.3 p. 249. Corrected two steps: in (b) the scalar was transferred from
    H^p(L,Omega^p) to H^p(P^n,Omega^p) by asserting that restriction carries
    the normalized generator to the normalized generator, and is now
    transferred by the projection formula t_Pn(beta cup i_*1) = t_L(i^*beta
    cup 1) with i_*1 spanning H^{n-p}; in (d) the residue input is now
    stated as the Poincare residue with its constant checked against
    III.7.14.1(c) and cross-checked for a hypersurface in P^n, where (b) and
    c(O(d)) = d must agree. Not checked: whether the printed exercise has a
    canonical normalization in the literature; none was found.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second published-solution search for III.7.4(b) and (d) (issue #121);
    nothing complete was located, and the card keeps its own derivation.
    Read this pass: Yang Pi-Yeh, Hartshorne Solutions (9 June 2019),
    Solution 3.7.4, printed p. 75 of tmp/sources/lfwin-hartshorne-solutions.pdf,
    text version tmp/sources/lfwin-hartshorne-solutions.md -- (a) as in
    step s1 here; (b) cuts Y down to its deg Y points by a general linear
    subspace and then asserts that k = H^p(H, Omega^p_H) = H^p(X,
    Omega^p_X) = k is the identity, which is the normalization step s3
    now supplies by the projection formula, and he never moves the count
    from the subspace back to P^n; (d) writes c(L_Y) as a Cech cocycle
    and then sends it by a map H^1(X, Omega_X) -> H^0(X, O_X) whose value
    is written as a sum of coordinate times partial derivatives, which is
    neither a defined map nor the duality pairing. Dongryul Kim, release
    PDF p. 170, lists Exercise 3.7.4 in his "problems I haven't solved".
    Stacks Project tags read: 0FWC, Section 50.22 (de Rham cohomology as
    a Weil cohomology theory, with the trace map Theta on H^{2d} and the
    statement that the cycle class followed by lambda_X is the degree
    map) and 0FLE, Section 50.9 (the dlog first Chern class into
    H^1(X, Omega^1)). 0FWC is a statement about H^{2p}_{dR}; the
    exercise's eta(Y) is the (p,p) Hodge component in H^p(X, Omega^p),
    and no tag read makes that identification. 0FLE supplies only the map
    c of part (c). Math StackExchange 1794757 and its accepted answer by
    the account S.M. (2016-05-22) prove (a) only. Checked against the
    book: the printed exercise, printed pp. 249--250; the trace and
    duality inputs III.7.1, III.7.2, III.7.12--7.14, printed pp. 240--247;
    Appendix A's C1, printed p. 430. Not checked: whether the printed
    exercise admits a normalizing convention in the literature; none was
    found in any of the sources read across both passes.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on the reader's report of this batch, three of substance. (1) The
    statement is the printed exercise again: the normalization paragraph is
    removed from the problem block and stated at the head of the solution,
    which is where a convention the book does not print belongs. (2) Step s3
    no longer applies the trace to the wrong degree: it names 1_V in
    H^{dim V} by t_V(1_V) = 1, observes that every point class on L equals
    1_L by step s1, and defines 1_{P^n} by t_{P^n}(1_{P^n} sm i_*1) = 1, that
    is, as the class pairing to 1 with the class of a linear P^p. The
    previous version defined 1_L by a trace applied to H^0 and 1_{P^n} by a
    trace applied to H^{n-p}, both ill-typed, and never stated the
    identification the transfer uses. (3) Step s6 is no longer circular. It
    states the divisor case (R) as an input, notes that part (d) is its case
    beta = 1, proves (R) in dimension one from the residue theorem and
    III.7.14.1(c) of the book, and says that for n >= 2 Hartshorne supplies no
    such statement (Remark III.7.14 says the trace is known only to exist).
    The withdrawn sentences are those that took the residue formula as the
    definition of the Gysin map by appeal to the problem statement, and the
    "independent check" for a hypersurface in P^n, which compared a class in
    H^1(Omega^1) with a point class. Also corrected: the audit description of
    Yang's (b) and (d) and of Kim's coverage, and the text versions named for
    Kim, MSE 1794757 and the two Stacks tags. Checked against the book in this
    pass: the printed exercise on pp. 249-250, III.7.1(a) p. 240, III.7.2
    p. 241, III.7.12-7.14 pp. 246-247, II.8.18 p. 179, I.7.7 p. 53, Exercise
    III.7.3 p. 249, Appendix A C1 p. 430. Not checked: no source proving (R)
    for n >= 2 was located, and the card does not claim one.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass on the reader's report of this batch, checked against the
    book and its text version. Restored the three events the report names as
    rewritten in place: the note of 2026-09-18 by chatgpt again ends where it
    ended, without the sentence about the 2026-11-16 move of the
    normalization; the note of 2026-11-11 again records the cross-check for a
    hypersurface in P^n as it was written on that date; and the note of
    2026-11-16 again carries the descriptions of Yang, of Kim and of Math
    StackExchange 1794757 written then. What those descriptions got wrong is
    corrected here and not in them: Yang's (b) does move the count back to
    P^n, by citing his own 3.7.3, though that citation is to a different
    identification; his (d) is a computation in homogeneous coordinates
    using Euler's formula, defined for X = P^n only; Kim's source has
    Exercise 3.7.4 on release PDF p. 170 with (a) and (c) proved, (b) a
    fragment and no (d), and his doubt stands in his list of problems he has
    not solved on PDF p. 1, not in a list of corrections; and the MSE answer
    is not recorded as accepted. The cross-check named in the note of
    2026-11-11 is not independent, as the note of 2026-11-16 says: it
    compares a class in H^1(Omega^1) with a class of a point.

    The mathematics of the card is repaired in four places. (1) The head of
    the solution now states four inputs and says which the book proves:
    (N) the trace at points, (G) the adjunction definition of Gysin maps,
    which is forced by the exercise's own definition of eta(Y), (R) the
    divisor case, and (B) base change for a transverse hyperplane section.
    The earlier text claimed the traces are "compatible with the Gysin
    maps", which with (G) is automatic and constrains nothing, and it called
    (R) part of the convention while stating only (N). (2) Step s3's use of
    "1" in H^p(P^n, Omega^p) before 1_{P^n} is defined, and of i^*1 = 1_L,
    is gone: alpha_0 = i_*(1) is the class of the linear subspace and is
    proved nonzero by restricting along the hyperplanes that cut L out, and
    the pairing then goes through (G) alone. (3) Step s5's transition
    convention is flipped to s_i = g_ij s_j, the one Hartshorne's Cech
    differential carries, so that the cocycle is df_j/f_j - df_i/f_i; with
    the earlier convention the constant in (R) is -1, as the reader
    computed. (4) Step s6 now compares the Cech class with the residue trace
    of Remark III.7.14 through the Cech complex of the flasque resolution,
    which is where the sign is decided, and states that (d) for n >= 2 is
    proved relative to (R) and that (R) itself is not proved there; "This
    proves part (d)" is no longer said without that qualification. Step s2's
    base change is named as input (B) instead of being asserted as a fact
    about "the normalized Gysin maps", and the card says that (B) is the
    step the printed hint uses and that no source proving it for n >= 2 was
    located. Checked against the book in this pass, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md: the printed exercise
    on pp. 249-250, the Cech complex of III.4 on p. 218, III.7.1(a) p. 240,
    III.7.1.1 pp. 240-241, III.7.2 p. 241, III.7.12-7.13 pp. 246-247,
    Remark III.7.14 and Theorems III.7.14.1, 7.14.2 on pp. 247-248,
    Exercise III.7.3 p. 249, Appendix A C1 p. 430. Not checked: no source
    proving (R) or (B) for n >= 2 was located.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass on the reader's report of this batch, on the items that the
    second pass left open, and on the audit trail. (i) The proof of
    alpha_0 nonzero introduced by the second pass was invalid and is
    replaced. It restricted alpha_0 along the n-p hyperplanes that cut L out
    and read the restriction as eta_L(L); but those hyperplanes contain L, so
    they do not meet it transversely, step s2 does not apply to the pair
    (L, H_i), and eta_L(L) is the class of L as a subvariety of itself, an
    element of H^0(L, O_L), not the class of degree n-p that a restriction of
    alpha_0 has. The step now proves alpha_0 nonzero by induction on the
    dimension of the linear subspace: for a point the class is nonzero by step
    s1, and for dimension at least one it applies step s2 to a hyperplane H
    with L not contained in H, which does meet L transversely in L cap H, and
    uses that a class with nonzero restriction is nonzero. (ii) The head of
    the solution now separates existence from compatibility. A trace
    satisfying (N) is unique, since H^n(X, Omega^n) is one-dimensional and
    eta(P) is nonzero by step s1, and a trace exists by Proposition III.7.5
    (printed p. 242); what is missing for (b) and (d) is the proof that the
    trace of III.7 satisfies (R) and (B), and the head states that instead of
    calling the consistency of the four inputs a theorem. (iii) The text
    versions of the sources of the event of 2026-11-16 whose note begins
    "Second published-solution search" are named here, because the second
    pass restored that event to a text written before the citations were
    added: tmp/sources/lfwin-hartshorne-solutions.md for Yang Pi-Yeh,
    tmp/sources/hartshorne-solutions-kim.md for Kim,
    tmp/sources/mse-1794757-cohomology-class-of-a-subvariety.md for Math
    StackExchange 1794757, and tmp/sources/stacks-tags/0FWC.md and
    tmp/sources/stacks-tags/0FLE.md for the two Stacks tags. (iv) The
    solution-reviewed event of 2026-11-16 whose note begins "Repairs on the
    reader's report of this batch" is restored as it was written, and this
    event is appended after it rather than put in its place. Checked against
    the book in this pass, in tmp/sources/hartshorne-1977-algebraic-geometry.md
    (printed p. N is PDF p. N+15): the printed exercise on pp. 249-250,
    Proposition III.7.5 on printed p. 242, Corollary III.7.12 on printed
    p. 246, Remark III.7.14 and Theorems III.7.14.1 and 7.14.2 on printed
    pp. 247-248, Exercise III.7.3 on printed p. 249. Not checked: no source
    proving (R) or (B) for n >= 2 was located in the two search passes
    recorded, and III.7.5 and III.7.12 were read in the text version only.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Fourth pass on the reader's report of this batch, on the two inputs. The
    Gysin calculus of the Stacks Project was read at the tags in this pass, at
    https://stacks.math.columbia.edu/tag/0G82 and the tags named: Lemma
    50.23.9 (0G8C) gives gamma^{p,q}(alpha|_Z) = alpha cup gamma^{0,0}(1) for
    a Koszul regular closed immersion of codimension c in a smooth X over a
    base S; Lemma 50.23.10 (0G8D) gives the compatibility of gamma with a
    transverse cartesian square, hence the class-level form of (B); Remark
    50.23.1 with equation (50.23.1.1) (tags 0G83 and 0G84) gives gamma^0_f(1)
    = df/f for a local equation f, which with Section 50.9 (tag 0FLE) is the
    dlog class of a divisor, hence the class identity c_1(L(Y)) cup nu =
    gamma^{n-1,n-1}_Y(nu|_Y) behind (R). Neither lemma compares the abstract
    trace of III.7 with the Gysin class of a point; that comparison,
    t_X(gamma^{0,0}_{P/X}(1)) = 1, is the case of the residue theorem which
    the book proves only for curves (III.7.14.1, printed p. 247), and the head
    of the solution now says so. Checked in this pass: the Stacks pages named,
    read at the site, and III.7.14.1 in
    tmp/sources/hartshorne-1977-algebraic-geometry.md. Not checked: no proof
    of the comparison was found, and the functoriality of gamma for a
    composite of regular immersions was not read in the source.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Fifth pass on the reader's report, on the four items that pass named:
    the trace normalization, the reduction to one point identity, the dlog
    citation, and the text versions of the Stacks tags. (i) The claim that a
    trace satisfying (N) is unique is false and is withdrawn. It is false
    because (N) constrains only the traces of finite reduced k-schemes: with
    t_X replaced by lambda*t_X and every point trace left alone, (N) still
    holds, the pairing scales by lambda, the class eta(P) = j_*(1) of (G)
    scales by lambda^{-1}, and part (a) still reads 1, so part (a) holds for
    every scalar and constrains none. What replaces it is uniqueness up to a
    nonzero scalar, which is Lemma 50.24.3 (tag 0G8I) in the relative form:
    the trace is unique up to precomposition by a unit of H^0(X, O_X), and
    that ring is k for X projective and integral. The scalar is fixed by the
    point comparison t_X(gamma^{0,0}_{P/X}(1)) = 1, which is unique because
    H^n(X, Omega^n) is one-dimensional and the class is nonzero by Lemma
    50.23.11 (tag 0G8E); that is now what the head says, and the inference
    "one fixed trace" that stood after it is rewritten to match.
    (ii) The reduction to the single point identity is incomplete and is no
    longer asserted. Granting t_X(gamma^{0,0}_{P/X}(1)) = 1, applying 0G8C to
    a divisor Y leaves t_X(gamma^{n-1,n-1}_Y(nu|_Y)), and to read that one
    needs the composite functoriality gamma^{0,0}_{P/X} =
    gamma^{n-1,n-1}_{Y/X} o gamma^{0,0}_{P/Y}, not supplied by 0G8C or 0G8D
    and recorded as unread in the fourth pass above. The head now names it as
    the second half of the comparison, says what it would give, and says that
    (R) and (B) stay inputs. (iii) The dlog citation was wrong about the tags.
    Remark 50.23.1 with equation (50.23.1.1) (0G83, 0G84) defines gamma
    through c_{f_1,...,f_c} and carries no formula gamma^0_f(1) = df/f; that
    formula is at the end of the proof of Lemma 50.23.5 (tag 0G88), and
    Section 50.9 (tag 0FLE) defines the dlog class without comparing it with
    gamma. The card now says so, quotes the sentence from 0G88, and states
    the class identity c(L(Y)) cup nu = gamma^{n-1,n-1}_Y(nu|_Y) as an input
    made in the Cech model of steps s5 and s6, not as a theorem of the Stacks
    Project; 0G8D is now described as class-level for gamma, which becomes a
    statement about the trace only through the comparison. (iv) The text
    versions now exist and are named: tmp/sources/stacks-tags/0G82.md for the
    section, and 0G83.md, 0G84.md, 0G88.md, 0G8A.md, 0G8C.md, 0G8D.md,
    0G8E.md, 0G8I.md and 0FLE.md for the environments, each saved from the
    page as served on 2026-11-16 at stacks-project commit
    a04446e57ec1fbc252a871afcec7752fb2807b14, with the LaTeX label of each.
    The fourth pass's event above, which said 0G83 and 0G84 give gamma^0_f(1)
    = df/f and that the class identity and the class-level form of (B) are
    theorems, is a dated event and is left as written; the correction is this
    event. Checked in this pass: Section 50.23 and Section 50.24 as served at
    the site and in the tag files above, and in
    tmp/sources/hartshorne-1977-algebraic-geometry.md (printed p. N is PDF p.
    N+15) III.7.5 printed p. 242, III.7.12 printed p. 246, Remark III.7.14 and
    Theorem III.7.14.1 printed pp. 247-248. Not checked: no proof of the point
    comparison, of (R) or of (B) was found, and the composite functoriality of
    gamma was not located in the Stacks Project; nothing in this pass supplies
    the published solution of (b) and (d) that the exercise still needs.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Sixth pass on the reader's report, on one sentence at the head of the
    solution. That sentence said the point identity is necessary for (R) and
    (B) and not shown to be sufficient. The second half stands. The first is
    withdrawn: no implication between the point identity and those two inputs
    was established in either direction. What the fifth pass showed is that
    sufficiency fails for want of the composite functoriality
    gamma^{0,0}_{P/X} = gamma^{n-1,n-1}_{Y/X} o gamma^{0,0}_{P/Y}; nothing
    there, and nothing in the tags read, derives the point comparison
    t_X(gamma^{0,0}_{P/X}(1)) = 1 from (R) or from (B). The reason is that
    neither input is a statement about a point: (R) constrains the trace
    against the dlog class of a divisor and (B) constrains the square of a
    transverse pair, so the point comparison would have to be carried to them
    by a further identification, which this card does not make. The head now
    says that no implication in either direction is established and that (R)
    and (B) remain inputs. The same claim stands in the fifth-pass record of
    COMPLAINTS.md, which is a dated record and is left as written; the
    correction is a new record there of this date. Checked in this pass: the
    head against the text versions of the two lemmas it names,
    tmp/sources/stacks-tags/0G8C.md (Lemma 50.23.9, the projection formula) and
    tmp/sources/stacks-tags/0G8D.md (Lemma 50.23.10, the transverse square),
    neither of which mentions a trace, and the card's step s6. Not checked: no
    source was searched in this pass, and nothing new is proved here about the
    point comparison, (R) or (B).
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, third pass: the solution's paragraph on the
    composite functoriality of gamma carried a search record. It named the tag
    file tmp/sources/stacks-tags/0G82.md, listed what Section 50.23 holds, and
    said that the fourth pass's audit recorded the composite case as unread. A
    rendered solution carries the mathematics, not which file was read
    (PROSE-11, QUAL-08). The paragraph now states that the composite
    gamma^{0,0}_{P/X} = gamma^{n-1,n-1}_{Y/X} o gamma^{0,0}_{P/Y} is an input
    of this solution, that 0G8C and 0G8D state the class of one Koszul regular
    closed immersion and its compatibility with a transverse square and that
    neither states the composite of two immersions. No mathematical claim
    changes: (R) and (B) remain inputs and no implication between them and the
    point identity is established. The search record is COMPLAINTS.md's
    III.7.4(b),(d) entry. Nothing was re-read in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, fourth pass, on sixteen lines of the same
    solution. Two things are repaired. (i) The status of the class-level halves
    contradicted itself. The paragraph introducing the Gysin calculus said "the
    class-level part of the two inputs is published", while the two paragraphs
    after it make the identity c(L(Y)) cup nu = gamma^{n-1,n-1}_Y(nu|_Y) an
    input, the comparison of the dlog class with gamma^0(1) being nowhere in
    the tags, and the closing paragraph repeated the published claim for both.
    The tags supply the class-level part of (B), the compatibility of gamma with
    a transverse cartesian square, and they supply that part only: the opening
    paragraph now says so and names (R)'s identity as an input, and the closing
    paragraph says which half is published and why the other is not. (ii) The
    search record left in the rendered solution is removed: the inventory of tag
    files the passage was read in, "no tag read performs the comparison", "no
    source read derives" the point comparison, and "the two search passes
    recorded above" for (B). Those statements are COMPLAINTS.md's III.7.4(b),(d)
    entry, which records them. No step, page or tag changes, and (R) and (B)
    remain inputs of this solution.
---

::: {.problem}
Let $X$ be a nonsingular projective variety of dimension $n$ over an algebraically closed field $k$. Let $Y$ be a nonsingular subvariety of codimension $p$, hence of dimension $n-p$. From the natural map $\Omega_X \tensor \mco_Y \to \Omega_Y$ of (II, 8.12) we deduce a map $\Omega_X^{n-p} \to \Omega_Y^{n-p}$. This induces a map on cohomology
$$
H^{n-p}(X, \Omega_X^{n-p}) \to H^{n-p}(Y, \Omega_Y^{n-p})
.$$
Now $\Omega_Y^{n-p} = \omega_Y$ is a dualizing sheaf for $Y$, so we have the trace map
$$
t_Y: H^{n-p}(Y, \Omega_Y^{n-p}) \to k
.$$
Composing, we obtain a linear map $H^{n-p}(X, \Omega_X^{n-p}) \to k$. By (7.13) this corresponds to an element $\eta(Y) \in H^p(X, \Omega_X^p)$, which we call the \dfn{cohomology class of $Y$}.

(a) If $P \in X$ is a closed point, show that $t_X(\eta(P)) = 1$, where $\eta(P) \in H^n(X, \Omega^n)$ and $t_X$ is the trace map.

(b) If $X = \PP^n$, identify $H^p(X, \Omega^p)$ with $k$ by (Ex. 7.3), and show that $\eta(Y) = (\deg Y) \cdot 1$, where $\deg Y$ is the degree of $Y$ as a projective variety (I, §7).

   Hint: cut with a hyperplane $H \subseteq X$, and use Bertini's theorem (II, 8.18) to reduce to the case where $Y$ is a finite set of points.

(c) For any scheme $X$ of finite type over $k$, we define a homomorphism of sheaves of abelian groups $d\log: \mco_X^* \to \Omega_X$ by $d\log(f) = f^{-1} \, df$. Here $\mco_X^*$ is a group under multiplication, and $\Omega_X$ is a group under addition. This induces a map on cohomology
$$
\Pic X = H^1(X, \mco_X^*) \to H^1(X, \Omega_X)
,$$
which we denote by $c$. See (Ex. 4.5).

(d) Returning to the hypotheses above, suppose $p = 1$. Show that $\eta(Y) = c(\mcl(Y))$, where $\mcl(Y)$ is the invertible sheaf corresponding to the divisor $Y$.
:::

::: {.solution}
The printed exercise fixes no normalization of the trace. Serre duality supplies
the trace of a dualizing sheaf only up to a nonzero scalar (III.7.2, printed
p. 241; III.7.14, printed p. 247, says of it that "we know only that it
exists"), and parts (b) and (d) assert numerical identities, so they hold only
for the trace that matches the integers. What this solution uses is the
following, and nothing else.

(N) The trace on $\Spec k$ is the identity, and the trace on a finite reduced
$k$-scheme is the sum of the traces of its points.

(G) For a nonsingular closed immersion $j:Y\hookrightarrow X$ of codimension $p$
the Gysin map
$$
j_*:H^q(Y,\Omega_Y^q)\longrightarrow H^{q+p}(X,\Omega_X^{q+p})
$$
is defined by adjunction with $j^*$ under the Serre pairing
$$
\langle\alpha,\beta\rangle_V=t_V(\alpha\smile\beta),
\qquad
\langle j_*(a),b\rangle_X=\langle a,j^*b\rangle_Y .
$$
This is forced and not a choice: the exercise defines $\eta(Y)$ as the class
whose functional is $b\mapsto t_Y(j^*b)$, so $\eta(Y)=j_*(1)$ with $j_*$ as in
(G). In particular no separate clause "the traces are compatible with Gysin
maps" is a constraint on the trace, because with (G) the identity
$t_X(j_*(a)\smile b)=t_Y(a\smile j^*b)$ holds by definition.

(R) For a nonsingular divisor $\iota:Y\hookrightarrow X$ of a nonsingular
projective $X$ of dimension $n$, and every $\nu\in H^{n-1}(X,\Omega_X^{n-1})$,
$$
t_X\bigl(c(\mcl(Y))\smile\nu\bigr)=t_Y(\restrictionof{\nu}{Y}),
$$
where $c$ is the $d\log$ map of part (c). Equivalently, by (G), the Gysin map
of a divisor is cup product with the $d\log$ class: $\iota_*(\beta)$ pairs with
every $\nu$ as $c(\mcl(Y))\smile\beta$ does, for every lift of $\beta$.

(B) Base change for a transverse hyperplane section: if $H\subseteq X$ is a
nonsingular divisor meeting the nonsingular $Y$ transversely, and $Z=Y\cap H$,
then
$$
i^*j_*=(j_H)_*\,i_Y^*
$$
for the four inclusions of the square of step [](#s2){.pf-ref}; in this
solution $H$ is always a hyperplane of $\PP^n$. This is the compatibility the
printed hint uses when it says to "cut with a hyperplane $H\subseteq X$"; it is
the projection formula for the trace, read for the transverse pair $(Y,H)$.

The class-level part of (B) is published, and it is quoted here as the Stacks
Project states it; the class identity behind (R) is not, for the reason the
paragraph after this one gives. With
$Z\subseteq X$ a Koszul regular closed immersion of codimension $c$ in an $X$
smooth over a base $S$, let
$\gamma^{p,q}:H^q(Z,\Omega_{Z/S}^p)\to H^{q+c}(X,\Omega_{X/S}^{p+c})$ be the
Gysin map of Remark 50.23.7 (tag 0G8A). Then
$$
\gamma^{p,q}(\restrictionof{\alpha}{Z})=\alpha\smile\gamma^{0,0}(1)
\qquad\text{(Lemma 50.23.9, tag 0G8C),}
$$
and $\gamma$ is compatible with a transverse cartesian square (Lemma 50.23.10,
tag 0G8D); both are stated over an arbitrary base scheme and with no
characteristic hypothesis.

The $d\log$ side is not a statement of those tags. Remark 50.23.1 with
equation (50.23.1.1) (tags
0G83 and 0G84) defines $\gamma^p_{f_1,\ldots,f_c}$ through the map
$c_{f_1,\ldots,f_c}$ and says nothing about $df/f$; the formula
$\gamma^0_f(1)=df/f$ is written at the end of the proof of Lemma 50.23.5 (tag
0G88), where the maps are chosen "such that $1$ maps to
$df_1\wedge\cdots\wedge df_c/(f_1\cdots f_c)$". Section 50.9 (tag 0FLE)
defines the $d\log$ class of a line bundle and nowhere compares it with
$\gamma$. Matching the two is a comparison of two classes in
$H^1(X,\Omega_X)$, made by reading both in one Čech model under one transition
convention; step [](#s5){.pf-ref} writes the $d\log$ side out in the convention
of Hartshorne's Čech complex and step [](#s6){.pf-ref} fixes its sign. So the
class identity behind (R),
$$
c(\mathcal L(Y))\smile\nu=\gamma^{n-1,n-1}_Y(\restrictionof{\nu}{Y}),
$$
is an input of this solution and not a theorem of the Stacks Project, and the
class-level half of (B) is likewise a statement about $\gamma$ which becomes a
statement about the trace only through the comparison below.

What those lemmas do not supply is the comparison of the Gysin class with the
trace of III.7, and it has two halves. The first is the point. For $P\in X$ the
classes $\eta(P)$ and $\gamma^{0,0}_{P/X}(1)$ both lie in the one-dimensional
$H^n(X,\Omega_X^n)$, and the second is nonzero: Lemma 50.23.11 (tag 0G8E) says
that for an irreducible smooth proper $X$ of dimension $d$ over a field the
image of $1$ under $\gamma^{0,0}$ from a $k$-rational point is nonzero, and
here $X$ is nonsingular, projective and integral over the algebraically closed
$k$, so every closed point is $k$-rational. The statement that the two classes
agree, equivalently
$$
t_X\bigl(\gamma^{0,0}_{P/X}(1)\bigr)=1,
$$
says that the trace of III.7 is computed by the residue at a point. The book
proves that only for curves (III.7.14.1, printed p. 247).

The second half is the functoriality of $\gamma$ for a composite of regular
immersions. Granting the point identity, (R) still does not follow from 0G8C
alone. Applied with $p=q=n-1$ and $\alpha=\nu$ to the divisor $Y$, 0G8C reads
$\gamma^{n-1,n-1}_Y(\restrictionof{\nu}{Y})=\nu\smile\gamma^{0,0}_Y(1)$, so what
(R) needs is the identity
$$
t_X\bigl(\gamma^{n-1,n-1}_Y(\restrictionof{\nu}{Y})\bigr)
=t_Y(\restrictionof{\nu}{Y}),
$$
and the point identity gives that only through the composite case: for a closed
point $P\in Y$ one needs the Gysin maps of $P\subseteq Y\subseteq X$ to compose,
$$
\gamma^{0,0}_{P/X}=\gamma^{n-1,n-1}_{Y/X}\circ\gamma^{0,0}_{P/Y}.
$$
With that, $t_X\circ\gamma_{Y/X}$ and $t_Y$ agree on the class
$\gamma^{0,0}_{P/Y}(1)$, which spans the one-dimensional
$H^{n-1}(Y,\Omega_Y^{n-1})$ because it is nonzero by 0G8E applied to $Y$, hence
on every $\nu$, and (R) follows from the class identity above. That
functoriality is an input of this solution: 0G8C states the class of one Koszul
regular closed immersion and 0G8D its compatibility with a transverse square,
and neither states the composite of two immersions. The reduction of (R) and
(B) to the single point identity is therefore not made here, and no implication
between them is established in either direction: (R) and (B) remain inputs of
this solution, the point identity is not shown to be sufficient for them, and
it is not shown to be necessary for them either. Neither (R) nor (B) is a
statement about a point: (R) constrains the trace against the $d\log$ class of a
divisor and (B) constrains the square of a transverse pair, and the point
comparison follows from neither: carrying either to a point takes a further
identification, which this card does not make.

(N) is a normalization, and part (a) uses only (N). (R) is the substantive
input, and part (d) is its case $\beta=1$. (B) is the second one, and part (b)
is its consequence. Both are cases of one statement, the compatibility of the
trace of Grothendieck--Serre duality with the Gysin maps of closed immersions of
nonsingular varieties: the divisor case of that compatibility is (R), and its
base-change case for a transverse pair is (B). Neither is a formal consequence
of the definitions (N) and (G); both are properties of the trace that III.7
constructs.

There is no uniqueness in (N). What the duality gives is uniqueness up to a
nonzero scalar: every functional on the $k$-line $H^n(X,\Omega_X^n)$ is a
scalar multiple of every other, which is the relative uniqueness in Lemma
50.24.3 (tag 0G8I), where the trace is
unique up to precomposing by a unit of $H^0(X,\OO_X)$ — and $H^0(X,\OO_X)=k$
for $X$ projective and integral over $k$. (N) fixes the trace at a point and fixes
nothing on $X$ itself: replacing $t_X$ by $\lambda t_X$, with every trace on a
finite reduced $k$-scheme left as it was, keeps (N) satisfied, multiplies the
pairing $\langle\alpha,\beta\rangle_X$ by $\lambda$, and therefore multiplies
the Gysin class $\eta(P)=j_*(1)$ of (G) by $\lambda^{-1}$, so that
$$
t'_X(\eta'(P))=\lambda\,t_X(\lambda^{-1}\eta(P))=t_X(\eta(P))=1 .
$$
Part (a) thus holds for every choice of the scalar and is no constraint on it,
and the identity $t_X(\eta(P))=1$ of step [](#s1){.pf-ref} is the definition of
$\eta(P)$ rather than a discovery about $t_X$.

The scalar is fixed instead by the point comparison above: there is exactly one
trace with $t_X\bigl(\gamma^{0,0}_{P/X}(1)\bigr)=1$, because
$H^n(X,\Omega_X^n)$ is one-dimensional and $\gamma^{0,0}_{P/X}(1)\ne0$ (tag
0G8E). That is the trace for which parts (b) and (d) are stated. It exists:
Proposition III.7.5 (printed p. 242) gives a dualizing sheaf with its trace on
every projective scheme over $k$, and for $X$ nonsingular that sheaf is
$\Omega_X^n$ (III.7.12, printed p. 246). What is missing for parts (b) and (d)
is therefore not existence but the proof that this trace satisfies (R) and (B),
together with the point comparison that singles it out, which is not proved
here either.

Of these, the book proves (R) for curves, and step [](#s6){.pf-ref} derives it
there from the residue description of the trace in Remark III.7.14 (printed
pp. 247--248), sign included. It proves nothing of the kind for $\dim X\ge2$:
Remark III.7.14 says of the trace that "we know only that it exists", and its
residue construction is stated for curves. Neither (R) nor (B) for higher
dimension is proved in this card: the published Gysin calculus supplies the
class-level part of (B), while for (R) the identity
$c(\mathcal L(Y))\smile\nu=\gamma^{n-1,n-1}_Y(\restrictionof{\nu}{Y})$ is an
input, the comparison of the $d\log$ class with $\gamma^0(1)$ not being among
its statements; neither half has the comparison of the trace with the Gysin
class of a point. Parts (b) and (d) are therefore theorems relative
to (R) and (B), and open with respect to the book alone. The remark
below records what the book does and does not determine.

Write $j:Y\hookrightarrow X$ for the closed immersion. We use the normalized Serre pairing
$$
\langle\alpha,\beta\rangle_X
=t_X(\alpha\smile\beta),
$$
between $H^p(X,\Omega_X^p)$ and $H^{n-p}(X,\Omega_X^{n-p})$.
With (G) the Gysin morphism
$$
j_*:H^q(Y,\Omega_Y^q)\longrightarrow H^{q+p}(X,\Omega_X^{q+p})
$$
is characterized by the adjunction identity
$$
\langle j_*(a),b\rangle_X
=\langle a,j^*b\rangle_Y.
$$
In particular, the class defined in the problem is
$$
\eta(Y)=j_*(1).
$$

By the discussion above, (R) and (B) are statements about the trace fixed by
$t_X(\gamma^{0,0}_{P/X}(1))=1$, not about a choice among several; (N) does not
fix that trace, and the point comparison does. What is proved below is that the
exercise's four assertions follow from (N), (G), (R) and (B), and that (R) is a
theorem of the book in dimension one.

::: pf

::: {.pf-step #s1}

For a closed point $P\in X$,
$$
\boxed{t_X(\eta(P))=1}.
$$

::: pf-proof

Here $p=n$, so the functional defining $\eta(P)$ is the composite
$$
H^0(X,\OO_X)\xrightarrow{j^*}H^0(P,\OO_P)
\xrightarrow{t_P}k.
$$
Since $X$ is projective and integral over the algebraically closed field $k$,
$$
H^0(X,\OO_X)=k,
$$
and since $P\cong\Spec k$, the restriction map is the identity on $k$.
By the chosen normalization $t_P=\operatorname{id}_k$, so the functional sends $1$ to $1$.

Under Serre duality, evaluating that functional at $1\in H^0(X,\OO_X)$ is the same as pairing $\eta(P)$ with $1$:
$$
1
=\langle\eta(P),1\rangle_X
=t_X(\eta(P)).
$$
This proves part (a).

:::

:::

::: {.pf-step #s2}

Cohomology classes are compatible with transverse intersection by a nonsingular hyperplane: if $H\subseteq X$ is nonsingular and meets $Y$ transversely, then
$$
i^*\eta_X(Y)=\eta_H(Y\cap H),
$$
where $i:H\hookrightarrow X$.

::: pf-proof

Let $Z=Y\cap H$ and write the transverse Cartesian square
$$
\begin{array}{ccc}
Z&\xrightarrow{j_H}&H\\
\downarrow i_Y&&\downarrow i\\
Y&\xrightarrow{j}&X.
\end{array}
$$
The assertion is (B) of the head of the solution, the base-change identity
$i^*j_*=(j_H)_*i_Y^*$. Both sides are maps
$H^q(Y,\Omega_Y^q)\to H^{q+p}(H,\Omega_H^{q+p})$, and applying it to
$1\in H^0(Y,\OO_Y)$ gives
$$
i^*\eta_X(Y)
=i^*j_*(1)
=(j_H)_*(1)
=\eta_H(Z),
$$
which is the asserted compatibility. This is the one step of part (b) that the
book does not supply: the identity is the base-change (or projection) formula
for the trace of the transverse pair $(Y,H)$, the base-change case of the same
compatibility of which (R) is the divisor case, and the proof of the printed
hint's instruction to cut with a hyperplane is exactly this statement. It is
input (B) of the head of the solution, not derived here from (N) or (R).

:::

:::

::: {.pf-step #s3}

If $X=\PP^n$ and $Y$ has codimension $p$, then
$$
\boxed{\eta(Y)=(\deg Y)\cdot1\in H^p(\PP^n,\Omega_{\PP^n}^p)\cong k}.
$$

::: pf-proof

By Exercise III.7.3,
$$
H^p(\PP^n,\Omega^p)\cong k.
$$
Choose a general linear subspace
$$
L\cong\PP^p\subseteq\PP^n
$$
of complementary dimension to $Y$.
By Bertini's theorem (II, 8.18, printed p. 179), for a general $L$ the scheme $Y\cap L$ is regular of dimension $0$, hence a reduced set of distinct points; by Bézout's theorem (I.7.7, printed p. 53) applied to the $n-p$ successive general hyperplane sections, each meeting the previous one properly with intersection multiplicity $1$ everywhere, the degree of $Y\cap L$ is $\deg Y$. Thus
$$
Z=Y\cap L=\{P_1,\ldots,P_d\},
\qquad d=\deg Y.
$$
Repeated application of step [](#s2){.pf-ref} gives
$$
\eta_L(Z)=i^*\eta_{\PP^n}(Y).
$$

The Gysin map is additive on a disjoint union of points, so
$$
\eta_L(Z)=\sum_{a=1}^d\eta_L(P_a).
$$

Two generators have to be named, and both are fixed by the convention at the
head of the solution. For a nonsingular projective variety $V$ of dimension
$m$, let $1_V\in H^m(V,\Omega_V^m)\cong k$ be the class with $t_V(1_V)=1$.
On $L$, which has dimension $p$, step [](#s1){.pf-ref} says that
$t_L(\eta_L(P))=1$ for every point $P$, so
$$
\eta_L(P)=1_L
$$
for every $P\in Z$: both classes have trace $1$ and $H^p(L,\Omega_L^p)$ is
one-dimensional. Hence
$$
i^*\eta_{\PP^n}(Y)=\eta_L(Z)=d\cdot 1_L
$$
in $H^p(L,\Omega_L^p)$.

The scalar is now read in $H^p(\PP^n,\Omega^p)$. Let
$\alpha_0=i_*(1)\in H^{n-p}(\PP^n,\Omega_{\PP^n}^{n-p})$ be the Gysin
pushforward of the unit class $1\in H^0(L,\OO_L)$; by (G) and the exercise's
definition it is the class $\eta_{\PP^n}(L)$ of the linear subspace. It is
nonzero, and the proof is an induction on the dimension of the linear subspace.
Write $c=n-p$ for its codimension and let $L\subseteq\PP^m$ be a linear
subspace of dimension $e=m-c$; the claim is that
$\eta_{\PP^m}(L)\in H^c(\PP^m,\Omega_{\PP^m}^c)$ is nonzero. If $e=0$, then
$L$ is a point of $\PP^c$, and $\eta_{\PP^c}(L)\ne0$ because
$t_{\PP^c}(\eta_{\PP^c}(L))=1$ by step [](#s1){.pf-ref}. If $e\ge1$, choose a
hyperplane $H\subseteq\PP^m$ with $L\nsubseteq H$; then $L$ meets $H$
transversely in the linear subspace $L'=L\cap H$ of dimension $e-1$ and
codimension $c$ in $H$, so step [](#s2){.pf-ref}, applied to the pair
$(L,H)$ in $\PP^m$, gives
$$
\restrictionof{\eta_{\PP^m}(L)}{H}
=i_H^*\eta_{\PP^m}(L)=\eta_H(L'),
$$
where $i_H:H\hookrightarrow\PP^m$ is the inclusion, and the right hand side is
nonzero by the induction hypothesis; a class with nonzero restriction is
nonzero. With $m=n$ this proves $\alpha_0=\eta_{\PP^n}(L)\ne0$. By Exercise
III.7.3 the space $H^{n-p}(\PP^n,\Omega^{n-p})$ is one-dimensional, so
$\alpha_0$ spans it.

Define $1_{\PP^n}\in H^p(\PP^n,\Omega^p)$ to be the class with
$$
t_{\PP^n}\bigl(1_{\PP^n}\smile \alpha_0\bigr)=1 ,
$$
which exists and is unique because $\alpha_0\ne0$ and the Serre pairing is
nondegenerate: it is the class pairing to $1$ with the class of the linear
$\PP^p$. This is a normalization and not a consequence of the book. Exercise
III.7.3 identifies $H^p(\PP^n,\Omega^p)$ with $k$, but does not say which
generator of the dual space the trace of Serre duality is, and (b) is false by
a scalar for another choice.

By (G) applied to $i:L\hookrightarrow\PP^n$ and to $1\in H^0(L,\OO_L)$, for
every $\beta\in H^p(\PP^n,\Omega^p)$ one has
$$
t_{\PP^n}\bigl(\beta\smile\alpha_0\bigr)
=t_{\PP^n}\bigl(\beta\smile i_*(1)\bigr)
=t_L\bigl(i^*\beta\smile1\bigr)
=t_L(i^*\beta).
$$
With $\beta=\eta(Y)$ this and step [](#s2){.pf-ref} give
$$
t_{\PP^n}\bigl(\eta(Y)\smile \alpha_0\bigr)
=t_L\bigl(i^*\eta(Y)\bigr)
=t_L\bigl(d\cdot1_L\bigr)=d ,
$$
while the definition of $1_{\PP^n}$ gives
$t_{\PP^n}(1_{\PP^n}\smile\alpha_0)=1$. So $\eta(Y)$ and $d\cdot1_{\PP^n}$ pair
equally with $\alpha_0$; since $\alpha_0\ne0$ and the Serre pairing is
nondegenerate, $\beta\mapsto t_{\PP^n}(\beta\smile\alpha_0)$ is injective, and
$$
\eta(Y)=d\cdot1_{\PP^n},
$$
which is part (b) with $d=\deg Y$.

:::

:::

::: {.pf-step #s4}

The rule
$$
d\log(f)=f^{-1}df
$$
is a morphism of sheaves of abelian groups
$$
d\log:\OO_X^*\longrightarrow\Omega_X.
$$

::: pf-proof

For local units $f,g$,
$$
\begin{aligned}
d\log(fg)
&=(fg)^{-1}d(fg)\\
&=f^{-1}g^{-1}(f\,dg+g\,df)\\
&=f^{-1}df+g^{-1}dg\\
&=d\log(f)+d\log(g).
\end{aligned}
$$
The construction commutes with restriction to smaller open sets because Kähler differentiation does.
Therefore it is a morphism from the multiplicative sheaf $\OO_X^*$ to the additive sheaf $\Omega_X$.
Passing to first cohomology and using
$$
\Pic X\cong H^1(X,\OO_X^*)
$$
gives the homomorphism
$$
c:\Pic X\longrightarrow H^1(X,\Omega_X)
$$
required in part (c).

:::

:::

::: {.pf-step #s5}

If $Y\subseteq X$ is a nonsingular divisor with local equations $f_i=0$ on an open cover $(U_i)$, then $c(\mcl(Y))$ is represented by the Čech cocycle
$$
\left\{\frac{df_i}{f_i}-\frac{df_j}{f_j}\right\}_{ij}.
$$

::: pf-proof

The invertible sheaf $\mcl(Y)=\OO_X(Y)$ has local generator $e_i=f_i^{-1}$ on $U_i$.
Use the convention $s_i=g_{ij}s_j$ for the transition functions of a line
bundle, which is the one Hartshorne's Čech complex carries (printed p. 218):
its differential is $(d\alpha)_{i_0i_1}=\alpha_{i_1}-\alpha_{i_0}$, and
$g_{ij}g_{jk}=g_{ik}$ is the multiplicative form of
$(d\alpha)_{ijk}=0$. With $s_i=e_i$ this gives
$f_i^{-1}=g_{ij}f_j^{-1}$, that is
$$
g_{ij}=\frac{f_j}{f_i},
$$
and its image under $d\log$ is
$$
d\log\!\left(\frac{f_j}{f_i}\right)
=\frac{df_j}{f_j}-\frac{df_i}{f_i}.
$$
This is the displayed cocycle. The opposite convention $e_j=g_{ij}e_i$ gives
$g_{ij}=f_i/f_j$ and the cocycle with both signs reversed, which is the class of
the inverse line bundle; the sign matters, and step [](#s6){.pf-ref} checks that
the one used here is the one whose trace is $+1$.

:::

:::

::: {.pf-step #s6}

For a nonsingular divisor $Y\subseteq X$,
$$
\boxed{\eta(Y)=c(\mcl(Y))\in H^1(X,\Omega_X)}.
$$
The two sides are elements of $H^1(X,\Omega_X)$, and they are seen to be equal
by pairing both with every class of $H^{n-1}(X,\Omega_X^{n-1})$; the one input
this uses is the divisor case (R) of the head of the solution, which the book
proves for curves and which for $n\ge2$ is named there as an input and not
proved.

::: pf-proof

Let
$$
\alpha\in H^{n-1}(X,\Omega_X^{n-1}).
$$
By the definition of $\eta(Y)$ and the adjunction identity of the head of the
solution,
$$
\langle\eta(Y),\alpha\rangle_X
=t_X(j_*(1)\smile\alpha)
=t_Y(j^*\alpha).
$$
By step [](#s5){.pf-ref}, $c(\mcl(Y))$ is the Čech class
$$
\left\{\frac{df_j}{f_j}-\frac{df_i}{f_i}\right\}_{ij}
$$
of the cover $(U_i)$ on which $Y$ has local equations $f_i=0$.

**The input (R).** It is the statement (R) of the head of the solution: for
every $\nu\in H^{n-1}(X,\Omega_X^{n-1})$,
$$
t_X\bigl(c(\mcl(Y))\smile\nu\bigr)=t_Y(\restrictionof{\nu}{Y}).
$$
By (G) this is the same as $j_*(\beta)$ pairing with every $\nu$ as
$c(\mcl(Y))\smile\beta$ does, for every $\beta=j^*\nu$; in the classical
language the Gysin map of a divisor is cup product with the $d\log$ class of
$\mcl(Y)$, and $j_*(1)=c(\mcl(Y))$ is the Poincaré residue of the unit class.
Part (d) is the case $\beta=1$ of (R).

(R) is not a consequence of Chapter III for $n\ge2$: Remark III.7.14 (printed
p. 247) says of the trace of a nonsingular projective variety that "we don't
have much information ... We know only that it exists", and its residue
description is stated for curves only. In dimension one (R) is proved in the
book, and the proof has to compare the Čech class with the residue, which is
where the sign lives.

Let $X$ be a curve, $Y=\{P\}$, and take the cover $U_1=X\setminus P$ with
$f_1=1$ and $U_2$ a neighbourhood of $P$ on which $f_2=f$ is a local
parameter. By step [](#s5){.pf-ref} the class $c(\OO(P))$ is
$$
c_{12}=\frac{df_2}{f_2}-\frac{df_1}{f_1}=\frac{df}{f}
\quad\text{on }U_1\cap U_2 .
$$
The trace of Remark III.7.14 is defined on $H^1(X,\Omega_X)$ by the flasque
resolution
$$
0\to\Omega_X\to\Omega_X\tensor\mathcal{K}_X
\to\bigoplus_{P\in X}i_*\bigl(\Omega_K/\Omega_P\bigr)\to0
$$
as the sum of the residues. To read a Čech class in it, take the Čech complex
of that resolution for the cover $\{U_1,U_2\}$: the middle sheaf is constant,
so its Čech complex is acyclic, and the connecting map sends the class of a
family $(\theta_i)$ of rational differentials with
$c_{ij}=\theta_j-\theta_i$ to the principal parts of the $\theta_i$. Hence
$$
t_X(c)=\sum_{P\in X}\operatorname{res}_P(\theta_i),
$$
the index $i$ being any one with $P\in U_i$; the sum is independent of the
choice because two choices differ by a global rational differential, whose
residues sum to $0$ by the residue theorem (III.7.14.2, printed p. 248).

Here $c_{12}=df/f=\theta_2-\theta_1$ with $\theta_1=0$ and $\theta_2=df/f$.
The principal part of $\theta_2$ at $P$ is $df/f$, and Theorem III.7.14.1(c)
(printed p. 247) gives
$$
\operatorname{res}_P\left(\frac{df}{f}\right)=v_P(f)\cdot1=1 .
$$
So $t_X(c(\OO(P)))=+1$, while $t_P(j^*\alpha)=\alpha(P)$ for every
$\alpha\in H^0(X,\OO_X)$; that is (R) in the case at hand, and with it part (d)
in dimension one. With the opposite transition convention of step
[](#s5){.pf-ref} this cocycle would be $-df/f$ and the constant would be
$-1$, so the convention there is what makes the sign come out right.

Granting (R), the two classes pair equally with every $\alpha$:
$$
\langle c(\mcl(Y)),\alpha\rangle_X
=t_X\bigl(c(\mcl(Y))\smile\alpha\bigr)
=t_X\bigl(j_*(1)\smile\alpha\bigr)
=t_Y(j^*\alpha)
=\langle\eta(Y),\alpha\rangle_X .
$$
The Serre pairing is nondegenerate, so
$$
c(\mcl(Y))=\eta(Y).
$$
For $n=1$ this is a theorem of the book. For $n\ge2$ it is part (d) proved
relative to (R), and relative to (R) alone: (R) itself is not proved here.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a) with no input beyond the normalization (N). Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (b) relative to (B) and (R): step [](#s2){.pf-ref} is (B), where the count $\deg Y$ is carried from $L$ back to $\PP^n$, step [](#s3){.pf-ref} uses (B) again to prove $\alpha_0\ne0$ and adds the normalization $1_{\PP^n}$, and (B) is the base-change case of the same trace compatibility of which (R) is the divisor case. Step [](#s4){.pf-ref} proves part (c). Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (d), which is the case $\beta=1$ of (R): in dimension one (R) is proved there from Theorem III.7.14.1, sign included, and for $n\ge2$ (R) is an input the book does not supply.

:::

:::

:::

::: {.remark title="Trace normalization"}
As written in the source, the exercise suppresses a normalization needed to make its numerical assertions canonical, and the printed text supplies no canonical one. The passages are these.

III.7.1(a) is the assertion $H^n(X,\omega_X)\cong k$ for $X=\PP^n_k$, and it continues "Fix one such isomorphism"; the isomorphism is a choice, so the trace $t$ it determines is defined only up to a nonzero scalar. III.7.2 (printed p. 241) makes the trace part of the data: a dualizing sheaf is a *pair* $(\omega_X^\circ,t)$, uniqueness is uniqueness of the pair, and replacing $t$ by $ct$ gives a different pair representing the same functor. Corollary III.7.12 (printed p. 246) then says only that for $X$ projective and nonsingular $\omega_X^\circ$ is *isomorphic* to $\omega_X$; it does not normalize the isomorphism, and the isomorphism its proof produces comes from $\wedge^r(\mathcal I/\mathcal I^2)^\vee$ tensoring, not from a normalization of $t$. Remark III.7.14 (printed p. 247) states the position: "even for a nonsingular projective variety $X$, we don't have much information about the trace map $t:H^n(X,\omega)\to k$. We know only that it exists."

A natural choice does exist on $\PP^n$ and the book records it without using it: Remark III.7.1.1 (printed pp. 240--241) gives the Čech cocycle
$$\alpha=\frac{x_0^n}{x_1\cdots x_n}\,d\Bigl(\frac{x_1}{x_0}\Bigr)\wedge\cdots\wedge d\Bigl(\frac{x_n}{x_0}\Bigr),$$
which "determines a generator of $H^n(X,\omega)$, which is stable under change of variables". That fixes one isomorphism in III.7.1(a), but nothing in the text compares it with the trace on a point or on a divisor.

The other side, part (d), is canonical: Appendix A defines the Chern classes in the Chow ring $A(X)$, with the normalization C1 (printed p. 430), "If $\mathcal E\cong\mathcal L(D)$ for a divisor $D$, $c_t(\mathcal E)=1+Dt$", so $c_1$ of a line bundle is the class of its divisor with no scalar freedom. The exercise's numerical identities can therefore hold only if the trace is normalized to match that integer, which is what the head of the solution states as (N), (G), (R) and (B). None of them is in the printed exercise, whose text says only "Fix one such isomorphism". Part (a) uses (N) alone, with $Y=P$ a closed point: $\eta(P)$ is defined by duality against $t_X$ itself. Part (b) uses (B) in step [](#s2){.pf-ref} to carry the count from the linear $L$ to $\PP^n$, uses (B) again in step [](#s3){.pf-ref} to prove that the class of $L$ is nonzero, and uses the normalization $1_{\PP^n}$ of that step to say which generator of $H^p(\PP^n,\Omega^p)$ the number $\deg Y$ is measured against. Part (d) is the case $\beta=1$ of (R) in step [](#s6){.pf-ref}: the book proves (R) for curves and for $n\ge2$ it is an input, which the card names and does not prove.
:::
