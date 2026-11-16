---
schema: qual/card@1
id: P-AGH67PUNCTUREDLINE
kind: problem
title: The number of punctures of $\AA^1 \sm \theset{P_1, \ldots, P_r}$ is an isomorphism invariant
classification:
  areas:
  - algebraic-geometry
  topics:
  - Automorphisms
  - Affine Varieties
  - Nonsingular Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.6.7 and the preceding automorphism exercise I.6.6 in the Hartshorne source. The proof computes the unit group of a punctured affine line and also extends any isomorphism to P^1, giving the sharper projective-equivalence criterion and the cross-ratio obstruction to the converse.
- event: solution-written
  by: chatgpt
  date: 2026-09-18

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.6.7, printed
    p. 47 (PDF p. 62 of the checked-in extraction; Proposition 6.7 is the
    different statement on printed p. 42). A. Shichijo, R.Hartshorne
    "Algebraic Geometry" 演習問題への解答 (2020/March), Chapter 1 section 6,
    Exercise 6.7, printed pp. 5--6, read in the MinerU extraction
    tmp/sources/shitijyou-ch1-section6.md. Its r = s direction: A^1 - {P_i} is
    P^1 - {P_i, infinity}, the isomorphism gives a birational map
    phi': P^1 --> P^1, and phi' extends to an automorphism phi'-bar, whence
    phi'-bar carries the omitted finite sets to one another and s = t. The card
    keeps its own proof of r = s through the unit group and states the source's
    route beside it, in step r-equals-s, with three defects recorded:
    (1) the extension step is referred to the source's own Exercise 6.3 block,
    whose footnote cites Corollary I.6.12, not Exercise I.6.8, which is a
    different statement (that a nonsingular projective curve is determined by its
    function field); (2) its displayed identity phi'-bar({P_n}) = P^1 -
    phi'-bar(P^1 - {P_n}) = {Q_n} omits infinity, the omitted sets being
    {P_n} union {infinity} and {Q_n} union {infinity}; (3) the converse is an
    assertion: an element of PGL(1) is determined by the images of three points
    and A^1 is infinite, "so one can choose {P_n}, {Q_n} not carried to each
    other by any element" -- which is the claim at issue, with the footnote
    replacing the argument by a configuration in A^3. The card's own proof of
    r = s through the unit group, and its cross-ratio counterexample to the
    converse, stand.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Step r-equals-s now carries the source's route as a paragraph after the
    card's unit-group proof, in Shichijo's own words as far as the two set
    identities go and with the missing infinity written in; the card's proof is
    unchanged, no step is transcribed from the source, and the converse keeps the
    card's cross-ratio obstruction because the source's version is an assertion.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    The closing paragraph of the published-solution remark was wrong about the
    extension automorphism and is corrected. It said that the automorphism of P^1
    produced in the step carries infinity to infinity, and inferred that the
    finite set it moves has r+1 elements. What the step proves is that the
    automorphism carries the (r+1)-point set {infinity} union P bijectively onto
    {infinity} union Q; it need not fix infinity, and the statement of the step
    (printed as the two (r+1)-point subsets) already says so. The conclusion is
    unchanged and now rests on the right statement: an isomorphism of the
    punctured lines requires those two (r+1)-point subsets to be in one
    PGL(2)-orbit, and for r = 3 they are four-point sets, where step
    converse-fails' cross ratio separates them. Checked against Borcherds p. 8, text version `tmp/sources/hartshorne-solutions-borcherds.md`,
    Egbert p. 55, text version `tmp/sources/hartshorne-solutions-egbert.md` and Cutrone--Marshburn p. 25, text version `tmp/sources/hartshorne-solutions-cutrone-marshburn.md`: all three state the threshold
    r <= 3, which is what makes the count matter.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121. Step converse-fails now proves what it
    used to assert: that an element of PGL(1) fixing infinity, 0 and 1 is the
    identity, hence that an element is determined by three values, hence
    invariance of the cross ratio, and then the six values of the orderings
    from the three transposition computations (ab), (ac) and (cd), which
    generate the orderings and give the substitutions 1/lambda and 1-lambda.
    The threshold for the converse is r <= 2, not r <= 3: the retained sets'
    r <= 3 is one too high because the four-point sets of step converse-fails
    are already separated by the cross ratio. Vakil, The Rising Sea
    (21 October 2025), text version
    tmp/sources/vakil-rising-sea-2025-10-21.md, prints the uniqueness of the
    normalizing automorphism in 19.9.7 (line 13770) and the six values in
    (19.9.7.1) (line 13797); his Exercise 19.9.B (line 13774) leaves the
    classification of four ordered points, and Exercise 19.9.C the S_4 action
    on the cross ratio, to the reader. Not checked in this pass: the card's
    own proof of r = s, which the reader accepted, and the Math Stack Exchange
    search for a thread on the converse, which the reader ran and which agrees
    with the record kept in COMPLAINTS.md.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, third pass, one mislabel and no change of
    mathematics. The 2026-11-16 note above names the three transpositions
    (ab), (ac) and (cd); the second of the three computations is not (ac). The
    orderings computed are [b,a,c,d], which is (ab), then [a,c,b,d], which is
    (bc), then [a,b,d,c], which is (cd), and the three adjacent transpositions
    (ab), (bc), (cd) generate the orderings. The 2026-11-16 note is left as
    written, since a dated event is a record of its date; the solution now
    names (bc), and the three values 1/lambda, 1-lambda and 1/lambda, with the
    normalizing maps that produce them, are unchanged and were re-read. The
    invariance of the cross ratio, the six-value orbit and the threshold r <= 2
    are as the reader accepted them.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Four further repairs on the same pass, none of them on the reader's list.
    First, and the only mathematical one: the invariance of the cross ratio was
    proved with the wrong composite. The normalizing transformation of the
    definition of [phi a, phi b, phi c, phi d] is the unique element carrying
    phi a, phi b, phi c to infinity, 0, 1, and that is rho o phi^{-1}, not
    rho o phi: rho o phi carries phi^{-1}a, phi^{-1}b, phi^{-1}c there and
    equals rho only when phi is the identity. Step converse-fails now says so
    and concludes [phi a, phi b, phi c, phi d] = rho(d) = [a,b,c,d] directly.
    The invariance itself, the six values and r <= 2 are unchanged, and the
    reader accepted all three.
    Second, the paragraph of the published-solution remark that begins "All
    three retained sets" follows five named sources, the last three of which
    are Egbert, Cutrone--Marshburn and Shichijo, and Shichijo states no
    threshold; the three meant are Borcherds, Egbert and Cutrone--Marshburn
    and they are now named.
    Third, the quotation from Cutrone--Marshburn on PDF p. 25 was punctuated
    as the card needed it: its text version
    tmp/sources/hartshorne-solutions-cutrone-marshburn.md, line 425, reads
    "under Aut P^1 . Any isomorphism between P^1 and P^1 fixes at most 2
    points", and the card had turned the full stop into a semicolon and the
    capital into a lower-case letter inside quotation marks. Restored.
    Fourth, the line of COMPLAINTS.md that records this card's converse said
    that all located sets state a threshold; Shichijo asserts the converse
    without one, and the three that do state it state it as r <= 3, which the
    card refutes at r = 3. The line now names them.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Record of a date, on the reader's report of issue #121's fourth pass. The
    two events above were written and committed on 2026-11-16, in a9d902a1a9
    (committer date 2026-11-16 07:15:38) for the (bc) mislabel and in
    27598ae933 (2026-11-16 07:30:29) for the four repairs, and both date fields
    said 2026-11-17, a day that had not happened; a record carries the day of
    the commit that lands it, so both say 2026-11-16 now, and their text stands:
    the three transpositions are (ab), (bc), (cd), the normalizing map of
    [phi a, phi b, phi c, phi d] is rho o phi^{-1}, and the threshold line and
    the Cutrone--Marshburn quotation are as they state. This event records the
    dates, and nothing else on the card changed.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, fifth pass: two dates, no mathematics. The
    two source-corrected events above are dated 2026-11-17, a day that had not
    happened when they were written and committed: the (bc) mislabel in
    a9d902a1a9 (committer date 2026-11-16 07:15:38) and the four further
    repairs in 27598ae933 (committer date 2026-11-16 07:30:29). A record
    carries the day of the commit that lands it, so both are dated 2026-11-16
    now, and their text is untouched. Nothing else on the card changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, sixth pass: the fifth-pass note above says
    the two source-corrected events "are dated 2026-11-17" in the present
    tense, and neither field of this card reads so. The note's sentence is
    true in the past tense, and this event is its correction: the two events
    it speaks of were dated 2026-11-17, a day that had not happened when
    a9d902a1a9 (2026-11-16 07:15:38) and 27598ae933 (2026-11-16 07:30:29)
    wrote and committed them, and their fields read 2026-11-16 now, changed
    in 2e7631a711, the commit that added the fifth-pass note. Their text
    stands, and the fifth-pass note stands as written, a dated event being a
    record of its date. Nothing else on the card changes.

---

::: {.problem}
Let $P_1, \ldots, P_r, Q_1, \ldots, Q_s$ be distinct points of $\AA^1$.
If
$$
\AA^1 \sm \theset{P_1, \ldots, P_r} \cong \AA^1 \sm \theset{Q_1, \ldots, Q_s},
$$
show that $r = s$.
Is the converse true?
:::

::: {.solution}
Write $P_i=p_i\in k$ and $Q_j=q_j\in k$ in the affine coordinate $x$.

::: pf

::: pf-step
The coordinate ring of
$$
U=\AA^1\setminus\{P_1,\ldots,P_r\}
$$
is
$$
A_U=k[x,(x-p_1)^{-1},\ldots,(x-p_r)^{-1}].
$$

::: pf-proof
Put
$$
g(x)=\prod_{i=1}^r(x-p_i).
$$
Then $U=D(g)\subseteq\Spec k[x]$, so
$$
\Gamma(U,\OO_U)=k[x,g^{-1}].
$$
Because the linear factors $x-p_i$ are pairwise coprime, inverting their product is equivalent to inverting each factor separately.
This gives the displayed description.
:::

:::

::: {.pf-step #unit-group-structure}
The unit group of $A_U$ is
$$
A_U^\times
=k^\times\,(x-p_1)^{\ZZ}\cdots(x-p_r)^{\ZZ},
$$
and therefore
$$
A_U^\times/k^\times\cong\ZZ^r.
$$

::: pf-proof
The polynomial ring $k[x]$ is a unique factorization domain.
An element of its localization at the multiplicative system generated by the $x-p_i$ is a unit exactly when every irreducible factor of its numerator and denominator belongs to that multiplicative system.
Thus every unit has a unique expression
$$
c\prod_{i=1}^r(x-p_i)^{n_i},
\qquad c\in k^\times, n_i\in\ZZ.
$$
Modulo the constant units, the exponent vector $(n_1,\ldots,n_r)$ identifies the quotient with the free abelian group $\ZZ^r$.
:::

:::

::: {.pf-step #r-equals-s}
If
$$
\AA^1\setminus\{P_1,\ldots,P_r\}
\cong
\AA^1\setminus\{Q_1,\ldots,Q_s\},
$$
then $r=s$.

::: pf-proof
An isomorphism of the two $k$-varieties induces an isomorphism of their coordinate rings and hence of their unit groups.
It fixes the subgroup $k^\times$ of constant units.
Step [](#unit-group-structure){.pf-ref} therefore gives an isomorphism
$$
\ZZ^r\cong A_U^\times/k^\times
\cong A_V^\times/k^\times\cong\ZZ^s.
$$
Free abelian groups of finite rank are isomorphic only when their ranks agree.
Hence
$$
\boxed{r=s}.
$$

A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 6, Exercise 6.7, printed pp. 5--6, reaches the same conclusion by another route: $\AA^1\sm\theset{P_1,\ldots,P_r}=\PP^1\sm(\theset{P_1,\ldots,P_r}\union\theset{\infty})$, the isomorphism gives a birational map $\PP^1\dashrightarrow\PP^1$, and that map extends to an automorphism $\bar\phi'$, which then carries the omitted sets to one another. His extension step is referred to his own Exercise 6.3 block, which rests on Corollary I.6.12; it is not Exercise I.6.8, which says that a nonsingular projective curve is determined by its function field. His displayed identity
$$
\bar\phi'(\theset{P_n})=\PP^1-\bar\phi'(\PP^1-\theset{P_n})=\PP^1-(\PP^1-\theset{Q_n})=\theset{Q_n}
$$
omits $\infty$: the sets exchanged are $\theset{P_n}\union\theset{\infty}$ and $\theset{Q_n}\union\theset{\infty}$, as step [](#isomorphism-iff-fractional-linear-equivalent){.pf-ref} states them.
:::

:::

::: {.pf-step #isomorphism-iff-fractional-linear-equivalent}
More precisely, the two punctured lines are isomorphic if and only if the two $(r+1)$-point subsets
$$
\{\infty,P_1,\ldots,P_r\},
\qquad
\{\infty,Q_1,\ldots,Q_r\}
$$
of $\PP^1$ are carried to one another by a fractional linear transformation.

::: pf-proof
Let $\phi:U\to V$ be an isomorphism.
Both $U$ and $V$ are nonsingular quasi-projective curves, hence abstract nonsingular curves by Proposition I.6.7, and $\PP^1$ is projective, so Proposition I.6.8, which is stated for abstract nonsingular curves, applies to them.
Apply Proposition I.6.8 successively at the finitely many omitted points to extend the composite
$$
U\xrightarrow{\phi}V\hookrightarrow\PP^1
$$
to a morphism $\bar\phi:\PP^1\to\PP^1$.
Doing the same for $\phi^{-1}$ gives a morphism $\bar\psi:\PP^1\to\PP^1$.
The composites $\bar\psi\bar\phi$ and $\bar\phi\bar\psi$ agree with the identity on dense open subsets, hence everywhere.
Thus $\bar\phi$ is an automorphism of $\PP^1$.
By [[P-AGH66AUTP1|Exercise I.6.6]], it is fractional linear.

Since $\bar\phi$ restricts to a bijection $U\to V$, it carries the complement of $U$ in $\PP^1$ bijectively to the complement of $V$.
This proves necessity.
Conversely, any fractional linear transformation carrying one displayed finite subset to the other restricts to an isomorphism of their complements.
:::

:::

::: {.pf-step #converse-fails}
The converse to $r=s$ is false in general.

::: pf-proof
Take $r=s=3$ and let $\lambda\in k\setminus\{0,1\}$; put
$$
S_\lambda=\{\infty,0,1,\lambda\}\subseteq\PP^1.
$$
Write $[a,b,c,d]$ for the image of $d$ under the unique fractional linear transformation carrying $a,b,c$ to $\infty,0,1$, the uniqueness being the case that fixes $\infty$, $0$ and $1$: such a transformation is $x\mapsto(\alpha x+\beta)/(\gamma x+\delta)$, fixing $\infty$ forces $\gamma=0$, then fixing $0$ forces $\beta=0$, and then fixing $1$ forces $\alpha=\delta$.

So an element of $\PGL(1)$ is determined by its values at three distinct points, and $[\phi a,\phi b,\phi c,\phi d]=[a,b,c,d]$ for every fractional linear $\phi$: the composite $\rho\circ\phi^{-1}$, where $\rho$ carries $a,b,c$ to $\infty,0,1$, carries $\phi a,\phi b,\phi c$ to $\infty,0,1$, so it is the normalizing transformation used in the definition of $[\phi a,\phi b,\phi c,\phi d]$, and it carries $\phi d$ to $\rho(d)$.

The cross ratios of the other orderings are computed with $\rho$ normalizing $(a,b,c)$, so that $\rho(d)=[a,b,c,d]=\lambda$:
$$
[b,a,c,d]=\frac{1}{\rho(d)}=\frac1\lambda,
\qquad
[a,c,b,d]=1-\rho(d)=1-\lambda,
\qquad
[a,b,d,c]=\frac{\rho(c)}{\lambda}=\frac1\lambda
$$
where the three right-hand sides use that $x\mapsto1/\rho(x)$ carries $b,a,c$ to $\infty,0,1$, that $x\mapsto1-\rho(x)$ carries $a,c,b$ to $\infty,0,1$, and that $x\mapsto\rho(x)/\lambda$ carries $a,b,d$ to $\infty,0,1$. The transpositions $(ab)$, $(bc)$ and $(cd)$ generate the group of all orderings of the four points, so every ordering of $S_\lambda$ is reached by a composite of them, and the substitutions $\lambda\mapsto1/\lambda$ and $\lambda\mapsto1-\lambda$ generate the six-element group
$$
\lambda,\quad1-\lambda,\quad\lambda^{-1},\quad
(1-\lambda)^{-1},\quad
\frac{\lambda}{\lambda-1},\quad
\frac{\lambda-1}{\lambda}.
$$
So the cross ratios of the orderings of a four-point subset of cross ratio $\lambda$ are exactly these six values, which form the orbit of $\lambda$ under a group; hence $\mu$ lies in the set attached to $\lambda$ exactly when $\lambda$ lies in the set attached to $\mu$.

Because the algebraically closed field $k$ is infinite, choose $\mu\in k\setminus\{0,1\}$ outside the six values attached to $\lambda$.
Then no fractional linear transformation carries $S_\lambda$ to $S_\mu$: such a transformation would make $\lambda$ the cross ratio of an ordering of $S_\mu$, hence one of the six values attached to $\mu$, and then $\mu$ would be one of the six values attached to $\lambda$.
By step [](#isomorphism-iff-fractional-linear-equivalent){.pf-ref},
$$
\AA^1\setminus\{0,1,\lambda\}
\not\cong
\AA^1\setminus\{0,1,\mu\},
$$
although both have three punctures.
Thus equality of the numbers of punctures is necessary but not sufficient.
:::

:::

::: pf-qed
Step [](#r-equals-s){.pf-ref} proves the required invariant, while steps [](#isomorphism-iff-fractional-linear-equivalent){.pf-ref} and [](#converse-fails){.pf-ref} answer the converse question.
:::

:::
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), text version `tmp/sources/hartshorne-solutions-borcherds.md`, Exercise 6.7, PDF p. 8: "any map from one curve to the other can be extended to a map from $\PP^1$ to $\PP^1$, so the points $P_i$ must be mapped to the points $Q_j$, so $r=s$"; and "the converse is true if and only if $r\le3$, because any set of at most $3$ distinct points in $\PP^1$ can be mapped to any other set of the same size under $\operatorname{Aut}(\PP^1)$, but this is not true for sets of $4$ or more points".
William Troiani, *Hartshorne Exercise Solutions* (October 2020), text version `tmp/sources/hartshorne-solutions-troiani.md`, stops at §I.5 and gives no solution to 6.7.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise I.6.7, PDF p. 55: "we can extend any map between the two curves to a map $\PP^1\to\PP^1$; since $P_i$ must map to $Q_j$ thus $r=s$. The converse is only true for $r\le3$ by virtue of the fact that mobius transformations can take at most $3$ distinct points in $\PP^1$ to any other $3$ distinct points."
Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, text version `tmp/sources/hartshorne-solutions-cutrone-marshburn.md`, Exercise I.6.7, PDF p. 25: the same extension argument giving the equality of the two numbers of punctures; "the converse is not true for $r>3$ since any set of at most $3$ points in $\PP^1$ can be mapped to any other set of the same size under $\operatorname{Aut}\PP^1$. Any isomorphism between $\PP^1$ and $\PP^1$ fixes at most $2$ points, so if $r>3$, the map must be the identity isomorphism".
A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 6, Exercise 6.7, printed pp. 5--6, answers $r=s$ by extending the birational map $\PP^1\dashrightarrow\PP^1$ to an automorphism, referred to his own Exercise 6.3 block and Corollary I.6.12 rather than to Exercise I.6.8; his displayed exchange of the omitted sets leaves out $\infty$, as step [](#r-equals-s){.pf-ref} records. For the converse he argues that an element of $\operatorname{PGL}(1)$ is determined by the images of three points and that, $\AA^1$ being infinite, one may choose the two finite sets outside the reach of any one element, which is the assertion and not a proof; the footnote replaces it by a configuration in $\AA^3$.

Borcherds, Egbert and Cutrone--Marshburn answer $r=s$ as step [](#r-equals-s){.pf-ref} does, and all three state the threshold for the converse as $r\le3$, which is one too high: the automorphism of $\PP^1$ produced in step [](#isomorphism-iff-fractional-linear-equivalent){.pf-ref} carries the $(r+1)$-point set $\{\infty\}\cup P$ onto $\{\infty\}\cup Q$ as a set --- it carries $\infty$ to whatever point of $\{\infty\}\cup Q$ is the image of $\infty$, and need not fix it --- so what the isomorphism of punctured lines requires is that these two $(r+1)$-point subsets of $\PP^1$ be carried to one another by a fractional linear transformation. For $r=3$ they are four-point sets, and the cross ratio obstructs the converse already there; so the converse of $r=s$ holds for $r\le2$, where $3$-transitivity of $\PGL(1)$ carries $\{\infty\}\cup P$ to $\{\infty\}\cup Q$, and fails for $r\ge3$. Cutrone--Marshburn's premise, that a non-identity automorphism of $\PP^1$ fixes at most two points, is true; the inference drawn from it is not, since an isomorphism carrying $\{\infty\}\cup P$ to $\{\infty\}\cup Q$ need not fix either set pointwise, and on four points it acts by a permutation of them. Step [](#converse-fails){.pf-ref} is the counterexample the sets lack. Recorded in COMPLAINTS.md for the converse half.
:::
