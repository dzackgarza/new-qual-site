---
schema: qual/card@1
id: P-AGH77CONEDEGDROP
kind: problem
title: The cone over $Y$ from a nonsingular point has dimension $r+1$ and smaller degree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Degree
  - Cones
  - Projective Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.7.7 and its induction hint in Hartshorne, together with Proposition I.7.6 and Theorem I.7.7. The proof treats the join as the image of an irreducible incidence variety and uses smoothness at P to rule out the cone-point degeneracy. For the degree drop it uses the characteristic-independent blowup/projection computation, avoiding an unstated fixed-point Bertini theorem in the hinted hyperplane argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: claude
  date: 2026-11-11
  note: >-
    Checked the card against the book: I.7.6(b),(c) for the degree of a
    union of lines, I.7.6(d), II.7.13 and II.7.17.3 for the blowup, the base
    ideal being the maximal ideal of the nonsingular point, J = O(-E) from
    the chart equation t_1 = 0, E^r = (-1)^{r-1} from N_{E/Ytilde} = O(-1),
    and (beta^*H - E)^r = d - 1. Found one gap: the blowup step needs r >= 1
    and the case dim Y = 0 was absent; added step zero-dimensional-case,
    where X is a union of at most d-1 lines through P meeting pairwise only
    in P and I.7.6(b) gives deg X <= d-1. Not checked: the published
    induction in Borcherds, Egbert or Cutrone-Marshburn, none of which
    proves the degree identity under a hyperplane section.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121. Step zero-dimensional-case is removed: its
    "Y is d points, X is a union of lines" is not a variety of degree d > 1,
    and it contradicts step join-irreducible-dim-bound's own conclusion that
    X is irreducible. The hypothesis r >= 1 that the blowup needs is now
    stated where it is used, in step blowup-resolves-projection, from
    irreducibility of Y and Proposition I.7.6(a). The claim in the 2026-11-11
    note and in the remark that the case was "missing" was therefore false.
    Not checked in this pass: the mathematics of the blowup computation and
    the identities (beta^*H - E)^r = d - 1 and delta deg Z = d - 1, which the
    reader accepted.
- event: source-corrected
  by: claude
  date: 2026-11-17
  note: >-
    Reader's report on issue #121, third pass, three repairs in this card and
    one in COMPLAINTS.md. First, the 2026-11-11 source-checked note above had a
    bracketed "[Corrected 2026-11-16 ...]" paragraph inserted into it; the
    bracket is removed and that note is restored to the text it had on its
    date. The correction it carried is the 2026-11-16 source-corrected event
    that follows it. Second, the reason that a variety of dimension 0 is
    excluded is not Proposition I.7.6(a): that proposition says only that the
    degree of a nonempty Y in PP^n is a positive integer (text version
    tmp/sources/hartshorne-1977-algebraic-geometry.md, line 1781, printed
    p. 52, with the definition of the degree of an algebraic set as r! times
    the leading coefficient of its Hilbert polynomial immediately above it). A
    point has degree 1 because its Hilbert polynomial is the constant 1 and
    0! = 1, and the step now says that; the 2026-11-16 note and
    the paragraph of COMPLAINTS.md that repeat the wrong citation are
    corrected in today's entry there. Third, the remark called Borcherds's
    dimension-zero sentence false; it is vacuous, no variety of dimension 0
    having degree greater than 1, and the remark now says so. Nothing in the
    proof changes: r >= 1 is still forced, by d > 1.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Record of a date, on the reader's report of issue #121's fourth pass. The
    event above is dated 2026-11-17 and was written and committed on
    2026-11-16, in 0005c982e3 (committer date 2026-11-16 07:19:12); a record
    carries the day of the commit that lands it, so 2026-11-16 is its date. It
    is left unedited, as a dated event must be, and its content stands: the
    2026-11-11 note is restored to the text it had on its date, a point has
    degree 1 because its Hilbert polynomial is the constant 1, and Borcherds's
    dimension-zero sentence is vacuous rather than false. This event is the
    record of the date, and nothing else on the card changed.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, fifth pass: one date, no mathematics. The
    source-corrected event above is dated 2026-11-17, a day that had not
    happened when it was written and committed, in 0005c982e3 (committer date
    2026-11-16 07:19:12). A record carries the day of the commit that lands
    it, so its date is now 2026-11-16, and its text is untouched. The "Record
    of a date" event below left the date as written; the reader of this pass
    requires the field itself to carry the commit's day. Nothing else on the
    card changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, sixth pass: the fifth-pass note above says
    the source-corrected event "is dated 2026-11-17" in the present tense, and
    no field of this card reads so. The note's sentence is true in the past
    tense, and this event is its correction: the source-corrected event it
    speaks of was dated 2026-11-17, a day that had not happened when
    0005c982e3 wrote and committed it (2026-11-16 07:19:12), and its field
    reads 2026-11-16 now, changed in da22fb231f, the commit that added the
    fifth-pass note. Its text stands, and the fifth-pass note stands as
    written, a dated event being a record of its date. Nothing else on the
    card changes.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121 on in-place edits to dated events; three
    records are restored and nothing else changes. (1) Commit da22fb231f
    (committer date 2026-11-16 09:00:28) changed the third-pass event's date
    from 2026-11-17 to 2026-11-16. The field is restored to 2026-11-17, the day
    its author wrote in 0005c982e3 (committer date 2026-11-16 07:19:12): the
    record carries a day one later than the commit that landed it, and its
    correction is this event rather than an edit of the record. (2) That commit
    also added the "Record of a date" and fifth-pass events, whose text
    c7b68fc6fd and 5675cba726 then rewrote in place. Both are restored to the
    text they were committed with in da22fb231f, the fifth-pass note's closing
    sentence about the record event and the record's statement that the field
    is left unedited included. (3) The fifth-pass note and the sixth-pass event
    after it say the field reads 2026-11-16; that is the state the first
    restoration undoes, and both stand as written, a dated event being a record
    of its date. Nothing in the problem, the solution or the pages changes, and
    no page was re-read.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    A wording defect in the restored fifth-pass note above, recorded rather
    than edited: it calls the "Record of a date" event "below" although
    that event stands above it. The note is a dated record and is not
    touched; the order is the one da22fb231f gave the two events, which added
    both. Nothing else on the card changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.7.7, printed
    p. 55, parts (a) and (b) with the hint "Use induction on dim Y". Read the
    two sources of part (b) at the cited places. Harris, Example 18.16,
    "Degrees of Cones and Projections": the example begins on printed p. 234,
    where the cone over a variety of dimension k and degree d has degree d, and
    the smooth-point paragraph, "it's immediate that a general k-tuple of
    hyperplanes H_i through p will intersect X transversely at p" leading to
    deg(X-bar) = deg(X) - 1, is on printed p. 235; folios verified in the
    retained copy, PDF p. 249 carrying the folio 234 and PDF p. 250 the folio
    235. His letters are not the card's: his X is the base of the cone and his
    Y the cone, and the paragraph assumes that the general line pq through p
    meets X only at p and q. Mumford, Stability of projective varieties:
    printed p. 54 is the first page of §2, which carries Proposition 2.1, and
    printed p. 55 carries Definition 2.2, the two examples after it, 2.3 and
    Proposition 2.5 with its proof; located in the retained copy by the
    contents leaf, which gives §2 on printed p. 54, and by the PDF pages 17 and
    18 that carry those two pieces. For part (a), KReiser's accepted answer
    4656385 to question 4656099 was read at its answer id, which is the place a
    Math Stack Exchange answer is cited by; it proves (a) in full, and the card
    names it at the two statements its first step shares with it.
    Checked against the book: (b) asks only for
    deg X < d, the hint's induction is not part of the statement, and the
    conclusion below gives deg X = deg Z <= d - 1. Not checked in this pass:
    Harris's Example 18.17 on degrees of joins, and Lecture 20, to which he
    defers the case p in X_sing.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Part (b) is now the published chain: X is the cone over Z with vertex P and
    deg X = deg Z by Harris's Example 18.16 on printed p. 234, and
    deg Z <= d - 1 by Mumford's Definition 2.2 and Proposition 2.5 on printed
    p. 55, whose e_L is the multiplicity of the base locus, 1 at the
    nonsingular point P. The condition r >= 1 is not stated in either step
    because neither needs it; the field question the proof earlier raised,
    whether a variety of dimension 0 can have degree greater than 1, is settled
    in the closing step as before. Part (a) keeps its three steps, with answer
    4656385 named at the first and beside the third; its tangent-space route in
    the second and third steps is the card's, and the source-checked event of
    2026-11-11 and the reader of 2026-11-16 accepted both.
    The blow-up computation that used to be steps blowup-resolves-projection,
    exceptional-self-intersection and projection-degree-formula is now the
    remark "The blow-up computation", where its statements are kept with the
    references they carried: the base ideal of the point, the chart reason that
    the inverse image ideal is O(-E), the resolved morphism, (beta^*H - E)^r =
    delta deg Z, E^r = (-1)^{r-1} from the normal bundle O(-1), and
    (beta^*H)^{r-i} E^i = 0. Nothing is asserted there that the removed steps
    did not prove, and the card's proof of (b) no longer rests on it.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on a local reader's report against the sources, four items, and the
    survey of the retained sets removed from the rendered card. (1) Part (a) is
    now answer 4656385 transcribed in two steps, not the card's own argument
    with the answer as a gloss: step join-irreducible-dim-bound is its
    rational map (D(x_0) cap Y) x A^1 -> X with the function-field bound, and
    step point-of-x-not-in-y is its induction on dim Y, with the Jacobian
    choice of H, Theorem I.5.1, Exercise I.3.11, its length lemma, Theorem I.7.7
    and the two cases, quoted. (2) The incidence-variety argument and the
    tangent-space argument that were the card's proof of part (a) are now one
    step, join-equals-y-forces-linear, marked as the card's own, and
    join-dimension-r-plus-one is the one-line conclusion from the two
    transcribed steps. (3) The identification of X with the cone over Z is
    marked as the card's own, with the two nearest printed statements named and
    the reason they do not apply: Harris's Example 3.1 on printed p. 36 defines
    the cone as the union of joins, and his Example 3.10 on printed p. 37
    identifies the cone with the cone over the projection only for p not lying
    on the variety, whereas P does lie on Y. (4) The multiplicity of the
    nonsingular point, which Mumford's Definition 2.2 and Harris's transversality
    sentence give between them but neither states, is marked as the card's own
    and now states what was missing: the multiplicity of a point is that of the
    maximal ideal of the local ring, O_{Y,P} is regular of dimension r, and the
    associated graded ring of a regular local ring is a polynomial ring, so the
    Hilbert-Samuel polynomial is binomial(n+r-1,r) with normalized leading
    coefficient 1. Not checked in this pass: the blow-up remark, unchanged from
    the commit of this date that introduced it.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121 against the book: two repairs, one in the
    statement and one in a letter, and no change of mathematics. (1) The
    statement printed the hint as a line of its own, "*Hint for part 2:* Use
    induction on dim Y.". Hartshorne prints it inside part (b), in brackets, on
    the same line: "(b) Show that deg X < d. [Hint: Use induction on dim Y.]"
    (Algebraic Geometry (1977), I.7.7, printed p. 55, retained copy
    tmp/sources/hartshorne-1977-algebraic-geometry.pdf, PDF p. 70, the folio 55
    at its foot). The statement now carries the book's wording; its hypothesis
    and its two parts are unchanged, and no step changes, the hint's induction
    being KReiser's in step point-of-x-not-in-y rather than the card's. (2) The
    card's own step giving the multiplicity of the nonsingular point as 1 wrote
    the Hilbert-Samuel function as binomial(n+r-1, r), n being the power of the
    maximal ideal; n is the ambient dimension of PP^n in the statement, so the
    letter carried two meanings in one card (NOT-3). The power is now m, the
    maximal ideal is named, and the step says what the normalized leading
    coefficient is instead of only naming it. The mathematics is unchanged:
    O_{Y,P} is regular of dimension r, its associated graded ring is a
    polynomial ring in r variables, the length of O_{Y,P}/m^m is
    binomial(m+r-1, r), and r! times that leading coefficient is 1. The same
    binomial had n in the event above, which introduced the step; that event is
    a dated record and stands as written.
    Not checked in this pass: Mumford's Definition 2.2 and Proposition 2.5 and
    Harris's Example 18.16, whose reading the earlier events record, and the
    blow-up remark; neither changes here.
---
::: {.problem}
Let $Y$ be a variety of dimension $r$ and degree $d > 1$ in $\PP^n$.
Let $P \in Y$ be a nonsingular point.
Define $X$ to be the closure of the union of all lines $PQ$, where $Q \in Y$ and $Q \neq P$.

(a) Show that $X$ is a variety of dimension $r + 1$.

(b) Show that $\deg X < d$. [Hint: Use induction on $\dim Y$.]
:::

::: {.solution}
For a reduced projective algebraic set $W\subseteq\PP^n$ and a point $P\in W$, write
$$
J_P(W)=\overline{\bigcup_{Q\in W\setminus\{P\}}\overline{PQ}}
$$
for the join of $P$ with $W$.
Thus the variety in the problem is $X=J_P(Y)$.

::: pf

::: {.pf-step #join-irreducible-dim-bound}
The join $X$ is irreducible and has dimension at most $r+1$.

::: pf-proof
Answer 4656385: "Without loss of generality, suppose $P\in D(x_0)$ and consider the rational map $Y\times\PP^1\to X$ given on $(D(x_0)\cap Y)\times\AA^1$ by $(Q,t)\mapsto P+Qt$.
This surjects on to an open dense set of the collection of points $R$ which are on a line of the form $\overline{PQ}$ for $Q\neq P$, of which $X$ is the closure.
As $Y\times\PP^1$ is irreducible, $(D(x_0)\cap Y)\times\AA^1$ is irreducible, the image of $(D(x_0)\cap Y)\times\AA^1$ is irreducible, and the closure of its image is irreducible, so $X$ is irreducible and this rational map from $Y\times\PP^1$ is dominant.
Thus we have an inclusion of function fields $k(X)\hookrightarrow k(Y\times\PP^1)$, so $\dim X\le\dim Y+1$."
That is the whole of this step, $X$ irreducible and $\dim X\le r+1$.

:::

:::

::: {.pf-step #point-of-x-not-in-y}

$X\setminus Y$ is nonempty, so $\dim X>r$.

::: pf-proof

Answer 4656385: "On the other hand, $Y\subset X$, so $\dim X\ge\dim Y$. All we need to do in order to show that $\dim X=\dim Y+1$ is to find a point in $X$ not in $Y$", and he does that by induction on $\dim Y$.

If $\dim Y=1$, then "for any $Q\in Y$ distinct from $P$, the intersection $\overline{PQ}\cap Y$ is a proper subset of $\overline{PQ}$. If it is not, then $\overline{PQ}\subset Y$, and by irreducibility, $Y=\overline{PQ}$, which is a linear variety. But by exercise I.7.6, this implies $Y$ has degree one, which is not the case." So the line $\overline{PQ}$ contains a point of $X$ that is not in $Y$.

If $\dim Y>1$, then $r<n$, "otherwise $Y=\PP^n$, which is linear, contradicting the fact that $\deg Y>1$". After a change of coordinates he takes $P=[1:0:\cdots:0]$ and works in $U_0$, where "$Y\cap U_0$ is cut out by an ideal $(g_1,\cdots,g_m)\subset k[x_1,\cdots,x_n]$, and the Jacobian criterion says that $P$ is smooth if the Jacobian matrix at $P$, $\frac{\partial(g_1,\cdots,g_m)}{\partial(x_1,\cdots,x_n)}(P)$, has rank $n-r$"; since $r<n$ he chooses $(a_1,\cdots,a_n)$ so that appending that row gives rank $n-r+1$, sets $f=\sum a_ix_i$, $\overline f=\sum a_iX_i$ and $H=V(\overline f)$, and shows that $H\cap Y$ is smooth at $P$: the Jacobian of $(g_1,\cdots,g_m,f)$ has rank $n-r+1$, so by Theorem I.5.1 the local ring $(k[x_1,\cdots,x_n]/(g_1,\cdots,g_m,f))_{\mathfrak m_P}$ is regular, hence a domain, hence $(f)_{\mathfrak m_P}$ is radical, and the local ring of $H\cap Y$ at $P$ is that regular local ring. "In particular, there is only one irreducible component of $Y\cap H$ through $P$ by exercise I.3.11, the fact that regular local rings are domains, and the correspondence between irreducible components and minimal primes"; call it $Z$.

His lemma computes the intersection multiplicity from the affine open. For a noetherian graded ring $S$, a graded $S$-module $M$ with a minimal homogeneous prime $\mathfrak p$, and a homogeneous $f\in S_1$ with $f\notin\mathfrak p$, the length of $M_{(\mathfrak p)}$ over $S_{(\mathfrak p)}$ equals the length of $M_{\mathfrak p}$ over $S_{\mathfrak p}$; he proves it by showing that $M\mapsto M_{(f)}$ is exact on graded modules and that $M_{(\mathfrak p)}=(M_{(f)})_{\mathfrak p'}$, and then reads both lengths off the filtration of Proposition I.7.4. Hence "$i(Y,H;Z)$ is equal to the length of $(k[Y\cap U_0]/(f))_{I_{Z\cap U_0}}$ over $k[Y\cap U_0]_{I_{Z\cap U_0}}$", and that length is one, because localizing further at $I_{Z\cap U_0}$ gives $k[Z\cap U_0]_{I_{Z\cap U_0}}$, of length one over itself.

"By an application of theorem I.7.7", if $Y\cap H$ is irreducible then it "is a variety of dimension $r-1$ and degree $d$ with a smooth point $P$", and the induction applies to it; if $Y\cap H$ is reducible, with $Z=Z_1$ the component through $P$ and $Z_2$ another component, he takes $Q\in Z_2\setminus Z_1$, notes that $Y\cap\overline{PQ}=(Y\cap H)\cap\overline{PQ}$ is the union of the closed sets $\overline{PQ}\cap Z_j$, and concludes that it is a proper subset of $\overline{PQ}$, "as no $Z_j$ with $j>1$ contains $P$, and $Z_1$ doesn't contain $Q$". So again there is a point of $X$ outside $Y$.

:::

:::

::: {.pf-step #join-dimension-r-plus-one}

$$
\boxed{\dim X=r+1}.
$$

::: pf-proof

Steps [](#join-irreducible-dim-bound){.pf-ref} and [](#point-of-x-not-in-y){.pf-ref} give $\dim X\le r+1$ and $\dim X>r$, hence $\dim X=r+1$, which is part (a).
The card's own shorter route to the inequality $\dim X>r$, which replaces the induction of step [](#point-of-x-not-in-y){.pf-ref}, is step [](#join-equals-y-forces-linear){.pf-ref}.

:::

:::

::: {.pf-step #join-equals-y-forces-linear}

The card's own route: the equality $X=Y$ would force $Y$ to be a linear variety.

::: pf-proof

This step is the card's own, and nothing here is taken from a source.
Assume $X=Y$.
Then for every $Q\in Y\setminus\{P\}$ the whole line $\overline{PQ}$ lies in $Y$.
Its tangent direction at $P$ is therefore contained in the projective tangent space $T_PY$.
Consequently every point $Q\in Y$ belongs to the linear subspace $T_PY\subseteq\PP^n$.

Because $P$ is nonsingular and $\dim Y=r$, the projective tangent space has dimension $r$.
Thus
$$
Y\subseteq T_PY\cong\PP^r.
$$
Both are irreducible closed subsets of dimension $r$, so $Y=T_PY$.
Hence $Y$ is linear, of degree one by [[P-AGH76DEGONELINEAR|Exercise I.7.6]], which contradicts $d>1$; therefore $\dim X>r$, and with step [](#join-irreducible-dim-bound){.pf-ref} this gives part (a) again.

:::

:::

::: {.pf-step #cone-degree-equals-projection-degree}
Projection from $P$ exhibits $X$ as the cone over an $r$-dimensional projective variety $Z$, and
$$
\deg X=\deg Z.
$$

::: pf-proof
Choose homogeneous coordinates with
$$
P=[1:0:\cdots:0]
$$
and let $H_0=V(x_0)\cong\PP^{n-1}$.
Projection from $P$ is the rational map
$$
\rho:Y\dashrightarrow H_0,
\qquad
[x_0:x_1:\cdots:x_n]\longmapsto[x_1:\cdots:x_n],
$$
and $Z$ is the closure of its image.
Step [](#join-dimension-r-plus-one){.pf-ref} gives $\dim X=r+1$, hence $\dim Z=r$.

That $X$ is the cone over $Z$ is the card's own. Harris defines the cone over a variety with vertex $p$ as the union of the joins $\overline{qp}$ (Example 3.1, printed p. 36) and, for $p$ not lying on the variety, identifies it with the cone over the projection of that variety from $p$ (Example 3.10, printed p. 37); here $P$ does lie on $Y$, so his statement does not apply as it stands. The identification is this. Every line through $P$ and a point of $Y\setminus\{P\}$ meets $H_0$ in the projected point, so the union of those lines lies in the cone over $\rho(Y\setminus\{P\})$ with vertex $P$. Conversely, a point of that cone lies on a line $\overline{Pz}$ with $z\in Z$, and $z$ is a limit of points of $\rho(Y\setminus\{P\})$, so the point is a limit of points of those lines and lies in their closure. Hence
$$
X=J_P(Y)
$$
is the cone over $Z$ with vertex $P$.

The degree identity is Harris, Example 18.16, printed p. 234: "Let $X\subset\PP^{n-1}\subset\PP^n$ be a variety of dimension $k$ and degree $d$, $p\in\PP^n$ any point not lying on $\PP^{n-1}$, and $Y=\overline{pX}$ the cone with vertex $p$ over $X$. Then, inasmuch as the general hyperplane section of $Y$ is projectively equivalent to $X$, we see that the degree of $Y$ is equal to the degree $d$ of $X$."
His cone is our $X$, built over his $X$, which is our $Z$ with $k=r$; the vertex $P$ does not lie on the hyperplane $H_0$ that carries $Z$, and a general hyperplane of $\PP^n$ not through $P$ cuts the cone in a variety projectively equivalent to $Z$.
Hence $\deg X=\deg Z$.

:::

:::

::: {.pf-step #projection-degree-drop}

$$
\deg Z\le d-1.
$$

::: pf-proof

This is Mumford, *Stability of projective varieties* (1977), Proposition 2.5, printed p. 55, in the notation of his 2.3 on the same page.
Let $A\subseteq\Gamma(\PP^n,\OO(1))$ be the space of hyperplanes through $P$, let $\mathcal I_A$ be the ideal sheaf generated by its sections, so that the base locus is $Y\cap L_A=Y\cap\{P\}=\{P\}$, and let $p_A(Y)$ be the image of the blow-up of $Y$ along $\mathcal I_A$ under the projection, counted as a cycle with each point of the image taken with multiplicity the degree of the map over it.
Proposition 2.5 states
$$
e_L(\mathcal I_A)=\deg Y-\deg p_A(Y).
$$
By Definition 2.2 on printed p. 55, $e_L(\mathcal I_A)$ is the normalized leading coefficient of $\chi(L^n/\mathcal I_A^nL^n)$, and the examples following that definition say that when $Z$ is set-theoretically a point $x$, then $P$ "is the Hilbert-Samuel polynomial of $\mathcal I$ as an ideal of $\OO_{x,X}$ and $e(\mathcal I)$ is its multiplicity there", independently of $L$.
So $e_L(\mathcal I_A)$ is the multiplicity of $Y$ at $P$.

That this multiplicity is $1$ is the card's own step: neither source states it. The multiplicity of a point is the multiplicity of the maximal ideal of the local ring, and $\OO_{Y,P}$ is a regular local ring of dimension $r$ with maximal ideal $\mathfrak m$, because $P$ is nonsingular; the associated graded ring of a regular local ring is a polynomial ring in $r$ variables, so the length of $\OO_{Y,P}/\mathfrak m^m$ is $\binom{m+r-1}{r}$ for every $m\ge1$, a polynomial in $m$ whose leading coefficient is $1/r!$ and whose normalized leading coefficient is therefore $1$. Harris's account of the same count on printed p. 235 is geometrical: "it's immediate that a general $k$-tuple of hyperplanes $H_i$ through $p$ will intersect $X$ transversely at $p$".

Since the underlying variety of the cycle $p_A(Y)$ is $Z$ and its multiplicities are the degrees of the projection, $\deg p_A(Y)\ge\deg Z$.
Hence
$$
d=\deg Y=\deg p_A(Y)+1\ge\deg Z+1,
$$
which is the claim.

:::

:::

::: {.pf-step #degree-drop-conclusion}

$$
\boxed{\deg X<d}.
$$

::: pf-proof

Steps [](#cone-degree-equals-projection-degree){.pf-ref} and [](#projection-degree-drop){.pf-ref} give
$$
\deg X=\deg Z\le d-1<d,
$$
the last inequality because $d>1$.
This is part (b).

:::

:::

::: pf-qed

Steps [](#join-irreducible-dim-bound){.pf-ref}, [](#point-of-x-not-in-y){.pf-ref} and [](#join-dimension-r-plus-one){.pf-ref} prove part (a).
Steps [](#cone-degree-equals-projection-degree){.pf-ref}, [](#projection-degree-drop){.pf-ref} and [](#degree-drop-conclusion){.pf-ref} prove part (b), whose hypothesis $d>1$ forces $r\ge1$: a variety is irreducible by the book's conventions, so a variety of dimension $0$ is a single point, of degree $1$ because its Hilbert polynomial is the constant $1$.

:::

:::
:::

::: {.remark title="The blow-up computation"}
The inequality $\deg Z\le d-1$ also has a computation that produces the factor. Blow up the nonsingular point $P$: let $\beta:\widetilde Y=\Bl_PY\to Y$ be the blow-up and $E$ its exceptional divisor. The restrictions of $x_1,\ldots,x_n$ to $Y$ have base locus exactly $\{P\}$, so on the blow-up they generate the invertible sheaf
$$
\OO_{\widetilde Y}(\beta^*H-E),
$$
$H$ being the hyperplane class, and the resolved projection $\widetilde\rho:\widetilde Y\to Z$ is the morphism these sections define ([@Har77, Theorem II.7.1] applied to the base ideal, which is the ideal sheaf of the point $P$; its inverse image ideal is invertible, and is $\OO_{\widetilde Y}(-E)$, by [@Har77, Proposition II.7.13] and [@Har77, Example II.7.17.3]).
On the chart of the blow-up where local parameters $t_1,\ldots,t_r$ at $P$ satisfy $t_i=t_1y_i$ for $i\ge2$, the inverse image ideal is $(t_1)$, and the exceptional divisor meets that chart in $\{t_1=0\}$, whose ring is $\OO_{Y,P}/(t_1,\ldots,t_r)[y_2,\ldots,y_r]$; so the divisor cut out by the ideal is $E$ with multiplicity one.

Both $\widetilde Y$ and $Z$ are $r$-dimensional projective varieties, so $\widetilde\rho$ is generically finite of some degree $\delta=[K(Y):K(Z)]\ge1$, and for a generically finite morphism of $r$-dimensional projective varieties the top self-intersection of the pullback of a hyperplane is $\delta$ times the degree of the target: intersecting with $r$ general hyperplanes and pulling back counts each of the $\deg Z$ points $\delta$ times. Hence
$$
(\beta^*H-E)^r=\delta\deg Z.
$$
On the other side $H^r=d$; since $P$ is nonsingular and $r\ge1$, $E\cong\PP^{r-1}$ with normal bundle $\OO_E(-1)$, so
$$
E^r=\deg c_1(\OO_{\PP^{r-1}}(-1))^{r-1}=(-1)^{r-1},
$$
while $(\beta^*H)^{r-i}E^i=0$ for $0<i<r$, because $\beta^*\OO_Y(H)$ is trivial on $E$, the map $E\to Y$ being constant. Therefore
$$
(\beta^*H-E)^r=H^r+(-1)^rE^r=d-1,
$$
and $\deg Z=(d-1)/\delta\le d-1$: Mumford's identity with the multiplicity of the base point computed as the degree of $\widetilde\rho$.
:::

::: {.remark title="Published solution"}
Part (a) is KReiser's, accepted answer 4656385 to Mathematics Stack Exchange question 4656099, *Hartshorne Chapter 1 Exercise 7.7 (a)*, transcribed in steps [](#join-irreducible-dim-bound){.pf-ref} and [](#point-of-x-not-in-y){.pf-ref}, which reproduce its quotations of Theorem I.5.1, Exercise I.3.11, Proposition I.7.4, Theorem I.7.7 and Exercise I.7.6.
Part (b) is Joe Harris, *Algebraic Geometry: A First Course*, Graduate Texts in Mathematics 133, Springer, 1992, Example 18.16, printed pp. 234--235, for the degree of a cone and for the degree of the projection of a variety from one of its smooth points, and David Mumford, *Stability of projective varieties*, L'Enseignement Mathématique 23 (1977), Definition 2.2 and Proposition 2.5, printed p. 55, for the same count as the degree of the variety minus the degree of its projection, with the multiplicity of the base locus as the correction term.
The two steps that are the card's own are marked as such: the identification of $X$ with the cone over $Z$, and the multiplicity $1$ of the nonsingular point.
:::
