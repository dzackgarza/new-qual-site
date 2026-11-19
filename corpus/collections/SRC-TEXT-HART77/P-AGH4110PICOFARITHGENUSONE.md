---
schema: qual/card@1
id: P-AGH4110PICOFARITHGENUSONE
kind: problem
title: $\Pic^0 X$ is in bijection with $X_{\reg}$ when $p_a(X)=1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Riemann-Roch
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.1.10 and the retained solution transcription. The proof
    uses the corrected target Pic^0, derives degree K=0 from IV.1.9, and makes
    explicit why the unique effective degree-one representative is supported at
    a regular point.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Hartshorne IV Ex. 1.10, printed p. 299 (PDF p. 314), reads "the elements of the group Pic^0 X", so the statement and title that name Pic^0 X are the printed ones; the printed page was re-read in the retained PDF for this check.'

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), IV.1.10,
    printed p. 299 (PDF p. 314 of the checked-in extraction). Published treatment
    located outside the twelve retained sets: R. Vakil, The Rising Sea:
    Foundations of Algebraic Geometry, 21 October 2025 version, Section 19.9,
    printed pp. 555--556, read in tmp/sources/vakil-rising-sea-2025-10-21.md.
    Corrected step mapping, after re-reading the three numbered paragraphs:
    (19.9.1), printed p. 555, gives deg omega_C = 0 and h^0(C, omega_C) = 1 so
    omega_C = O_C, and for deg L > 0 Riemann--Roch with Serre duality gives
    h^0(C, L) = deg L, which is the card's step s1 together with the vanishing of
    step s2; (19.9.2), same page, says that each degree 1 point q gives O_C(q),
    that distinct points give distinct bundles because a degree 1 bundle has one
    section up to scalars, and that every degree 1 bundle is O_C(q) for q the
    divisor of zeros of a section -- that is the card's step s5 (injectivity) and
    the existence half of step s6, not steps s3 and s4 as the earlier version of
    this note said; (19.9.3), printed p. 556, twists the degree 1 bundles by
    O(-p) to get the bijection with Pic^0 and defines the group law, which is the
    card's map Phi and its identification with Pic^0. Vakil's standing hypothesis
    is a curve, i.e. a regular projective geometrically integral scheme of
    dimension 1, while Hartshorne's X is only an integral projective
    locally complete intersection of dimension 1 with p_a = 1 and may be
    singular, and the exercise asks for a bijection onto X_reg. The singular case
    is the card's step s6, whose length-one argument shows O_{X,P}/(a) = k, hence
    a principal maximal ideal and P regular; Vakil supplies nothing for it. The
    earlier version of this note recorded the step mapping wrongly in three places
    and this substitutes for it.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Named the text version of Vakil's book at the three citations of 19.9 and
    19.9.2 in the remark on 2026-11-16, where they cited the PDF alone: it is
    tmp/sources/vakil-rising-sea-2025-10-21.md. No page or claim changes.
- event: source-checked
  by: claude
  date: 2026-11-17
  note: >-
    Printed exercise read again at the marker of PDF p. 314 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, that is printed p. 299:
    an integral projective scheme of dimension 1 over k, locally complete
    intersection, p_a = 1, a fixed P_0 in X_reg, and the bijection onto Pic^0 X.
    Read whole for this check: the solution printed as Exercise 10 of section 1
    of the National Taiwan University Algebraic Geometry II homework set,
    Chapter IV, by Ping-Hsun Chuang, printed pp. 3--4 of
    tmp/sources/ntu-ag2-chapter4.pdf, text version
    tmp/sources/ntu-ag2-chapter4.md, where the heading closes printed p. 3 and
    the proof is on printed p. 4, the folio being the PDF page number; and Math
    Stack Exchange question 4962032 with its comments and its accepted answer
    4978046 by KReiser, 2024-09-29, tmp/sources/mse-4962032.md. Hartshorne
    II.7.4 (printed p. 153, PDF p. 168) and I.6.2A were read in the same text
    version, as were IV.1.8's normalization and the parts of IV.1.9 the card
    cites. Not read: the printed PDFs of Hartshorne or of the NTU set; the
    answer was not checked against any other solution of the exercise.
- event: solution-reviewed
  by: claude
  date: 2026-11-17
  note: >-
    Step s6 now carries a published argument for the singular case. Its
    existence half keeps the card's Euler characteristic computation and names
    the printed NTU solution that runs the same route; the regularity of the
    point supporting the divisor, which Chuang's last sentence asserts and the
    retained Cais set also asserts, is step s6-regular and transcribes
    KReiser's two-case normalization argument, with Hartshorne II.7.4 for the
    one-preimage case, I.6.2A for the dimension of the cotangent space of the
    normal curve, II.Ex.3.8 for the finiteness of the normalization, and
    IV.1.9(c) for the degree zero divisor supported in X_reg. Vakil 19.9 is
    recorded as the regular case only. The card's earlier length-one route
    stays as one sentence of the same step, marked as forcing the same
    conclusion. No claim is weakened: the statement, steps s1--s5, step s7 and
    every earlier audit event stand unchanged.

- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The step that places the point of a degree-zero class in $X_{\reg}$ rested
    on a Mathematics Stack Exchange answer and carried no mark saying so. An
    answer on that site is a user post and not a publication, so the step is now
    marked as the card's own and says that no printed page is cited for that
    argument, which is the two-case one of the answer and is written out in full
    below the sentence. Checked in this pass: the step's own text against the
    answer named on it, and the exercise as printed at Hartshorne IV.1.10,
    printed p. 299 (PDF p. 314 of the checked-in extraction). Not checked in
    this pass: the NTU set the remark also cites was not reopened, and no
    publication was searched for this step; COMPLAINTS.md records the state.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.1.10, printed p. 85,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.1.10, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed
    deg K = p_a - 1 = 0, the reduction of D + P_0 to a divisor on X_reg,
    and the bijection X_reg -> Pic^0 X. Not checked: Yang's Solutions outside printed pp. 84-86; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.1.10 at printed
    p. 85 beside the entry already there. No step, statement or
    hypothesis of the card changes.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Step s6 read for its mathematics: the argument is right and its notation was
    not, and the solution now declares the notation. s6 writes mcl(E) for the
    sheaf of the divisor E = D + P_0 while mcl alone is the given class in
    Pic^0 X, and the symbol is used both ways in the same step: "mcl = mcl(D)",
    then "a section of mcl(E)", then "deg mcl(E) = deg E = 1". Read as
    mcl twisted by O_X(E), that is O_X(2D + P_0), and the conclusion
    mcl = O_X(Z - P_0) fails; read as O_X(E) of the divisor, which is what the
    step's own l(E) = 1 from step s3 forces, the count is right: chi(O_X) = 0,
    chi(O_X(E)) = deg E + 1 - p_a = 1, so the zero-dimensional quotient O_Z(E)
    has length 1 and Z is one closed point. The solution now says at its head
    that mcl(D) is O_X(D) of a divisor and the bare mcl a given sheaf, which is
    Hartshorne's own use of the letter at Example IV.1.3.7, printed p. 297
    (PDF p. 312, folio read), where the map is P -> L(P - P_0), and at IV.1.10,
    printed p. 299, which asks the reader to imitate it. Read and unchanged in
    this pass: steps s1 to s5 and s7, and s6's last line, where Z ~ E = D + P_0
    gives O_X(Z - P_0) = O_X(D) = mcl. Not checked in this pass: the Vakil
    page 555 and the NTU solution's printed p. 4, which the preamble of s5 and
    s6 cite, were not re-opened.
---

::: {.problem}
Let $X$ be an integral projective scheme of dimension 1 over $k$, which is locally complete intersection, and has $p_a=1$.
Fix a point $P_0 \in X_{\reg}$.
Imitate (1.3.7) to show that the map $P \mapsto \mcl(P-P_0)$ gives a one-to-one correspondence between the points of $X_{\reg}$ and the elements of the group $\Pic^0 X$.

This generalizes (II, 6.11.4) and (II, Ex.
6.7).
:::

::: {.solution}
::: pf

Throughout, $\mcl(D)$ denotes the invertible sheaf $\mco_X(D)$ associated to a divisor $D$, which is the notation of Hartshorne's Example IV.1.3.7, printed p. 297, and the bare $\mcl$ a given invertible sheaf; so $\mcl(E)$ in step [](#s6){.pf-ref} is $\mco_X(E)$ of the divisor $E$, not the class $\mcl$ twisted by $\mco_X(E)$.

::: {.pf-step #s1}

The canonical divisor $K$ from Exercise IV.1.9 satisfies
$$
\deg K=0,
\qquad
\ell(K)=1.
$$

::: pf-proof

Since $p_a(X)=1$, the singular-curve Riemann--Roch formula
[[P-AGH419RRSINGULAR|Exercise IV.1.9]] gives, for $D=0$,
$$
\ell(0)-\ell(K)
=
1-p_a(X)
=
0.
$$
Because $\ell(0)=h^0(X,\mco_X)=1$, this gives $\ell(K)=1$.

Apply the same formula with $D=K$:
$$
\ell(K)-\ell(0)
=
\deg K+1-p_a(X)
=
\deg K.
$$
The left-hand side is zero, so $\deg K=0$.

:::

:::

::: {.pf-step #s2}

An invertible sheaf of negative degree on $X$ has no nonzero global
section.

::: pf-proof

Let $\mcl$ be invertible and suppose
$$
0\ne s\in H^0(X,\mcl).
$$
Since $X$ is integral, multiplication by $s$ gives an injection
$$
0
\longrightarrow
\mco_X
\xrightarrow{s}
\mcl
\longrightarrow
\mct
\longrightarrow
0,
$$
where $\mct$ is supported in dimension zero. Therefore
$$
\deg\mcl
=
\chi(\mcl)-\chi(\mco_X)
=
\chi(\mct)
=
\length(\mct)
\ge0.
$$
Thus a line bundle of negative degree cannot have a nonzero section.

:::

:::

::: {.pf-step #s3}

If $E$ is a divisor supported in $X_{\reg}$ with $\deg E=1$, then
$$
\ell(E)=1.
$$

::: pf-proof

Exercise IV.1.9 gives
$$
\ell(E)-\ell(K-E)
=
\deg E+1-p_a(X)
=
1.
$$
By step [](#s1){.pf-ref},
$$
\deg(K-E)=-1.
$$
Hence step [](#s2){.pf-ref} gives $\ell(K-E)=0$, and therefore $\ell(E)=1$.

:::

:::

::: {.pf-step #s4}

The assignment
$$
\Phi:X_{\reg}\longrightarrow\Pic^0X,
\qquad
P\longmapsto[\mcl(P-P_0)]
$$
is well defined.

::: pf-proof

The divisor $P-P_0$ has degree zero. By Exercise IV.1.9(a),
$$
\deg\mcl(P-P_0)=0.
$$
Thus $\mcl(P-P_0)$ lies in $\Pic^0X$.

:::

:::

::: {.pf-step #s5}

The map $\Phi$ is injective.

::: pf-proof

In the regular case this is R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, 21 October 2025 version [@Vak25, §19.9.2], text version `tmp/sources/vakil-rising-sea-2025-10-21.md`, printed p. 555: distinct degree 1 points determine distinct degree 1 line bundles, "as a degree 1 line bundle has only one section, up to scalar multiples". The card's version of it, which needs no regularity hypothesis beyond $P,Q\in X_{\reg}$, runs as follows.

Suppose
$$
\mcl(P-P_0)\cong\mcl(Q-P_0)
$$
for $P,Q\in X_{\reg}$. Tensoring by $\mcl(P_0)$ gives
$$
\mcl(P)\cong\mcl(Q).
$$
Thus $P$ and $Q$ are linearly equivalent effective divisors.

By step [](#s3){.pf-ref},
$$
\ell(P)=1,
$$
so the complete linear system $\abs{P}$ has dimension zero and contains
only the divisor $P$. Since $Q\in\abs{P}$, we obtain $Q=P$.

:::

:::

::: {.pf-step #s6}

The map $\Phi$ is surjective.

::: pf-proof

The existence half of the argument is the one given for a regular curve in R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, 21 October 2025 version [@Vak25, §19.9.2], text version `tmp/sources/vakil-rising-sea-2025-10-21.md`, printed p. 555: a degree $1$ invertible sheaf has a section, and the divisor of zeros of a nonzero section is supported at a single degree $1$ point. It is also the route of the solution printed for this exercise as Exercise 10 of §1 of *Algebraic Geometry II*, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), Chapter IV, by Ping-Hsun Chuang, printed p. 4 of `tmp/sources/ntu-ag2-chapter4.pdf`, text version `tmp/sources/ntu-ag2-chapter4.md`. That the point supporting the divisor is a regular point of $X$ is asserted and not argued in that solution's last sentence; step [](#s6-regular) proves it, transcribing KReiser's answer 4978046.

Let $[\mcl]\in\Pic^0X$. By Exercise IV.1.9(c), choose a divisor $D$
supported in $X_{\reg}$ such that
$$
\mcl\cong\mcl(D).
$$
Since $\mcl$ has degree zero, Exercise IV.1.9(a) gives
$$
\deg D=0.
$$
Put
$$
E=D+P_0.
$$
Then $E$ is supported in $X_{\reg}$ and has degree one. Step [](#s3){.pf-ref} gives
$$
\ell(E)=1,
$$
so choose a nonzero section
$$
s\in H^0(X,\mcl(E)).
$$

Because $X$ is integral, $s$ defines an effective Cartier divisor $Z$ and
an exact sequence
$$
0
\longrightarrow
\mco_X
\xrightarrow{s}
\mcl(E)
\longrightarrow
\mco_Z(E)
\longrightarrow
0.
$$
By Exercise IV.1.9(a),
$$
\deg\mcl(E)=\deg E=1.
$$
Taking Euler characteristics in the displayed sequence therefore gives
$$
\length(Z)=1.
$$

Hence $Z$ is supported at a single closed point $P$, and
$$
\mcl\cong\mcl(D)\cong\mco_X(Z-P_0).
$$

::: {.pf-step #s6-regular}

$P$ is a regular point of $X$.

::: pf-proof

This step is the card's own. Its argument is the two-case one of KReiser, answer 4978046 (https://math.stackexchange.com/a/4978046), posted 2024-09-29 to Math Stack Exchange question 4962032, "Hartshorne Exercise IV.1.10: making sure a point is nonsingular" (asked by François Gatine on 2024-08-23), which is a user answer and not a publication, so no printed page is cited for it; it is stated there for a non-regular point $Q$ with $\mcl\cong\mco_X(Q-P_0)$, here $Q$ is $P$ and that identification is the one displayed above, and the two ingredients the answer leaves to the reader are supplied below.

Let $\nu:\widetilde X\to X$ be the normalization (II, Ex. 3.8). Since $X$ is of finite type over $k$, $\nu$ is finite, and $\widetilde X$ is a normal integral curve, finite over the projective $X$ and hence projective, so a nonsingular one. Because $\mco_{X,P_0}$ is a discrete valuation ring and so integrally closed (I.6.2A), $\nu$ is an isomorphism over $X_{\reg}$; hence $\nu^{-1}(P_0)$ is a single point and $\deg\nu^*\mco_X(P_0)=1$. Since $\nu$ induces an isomorphism of function fields, the map of local rings $\mco_{X,P}\to\mco_{\widetilde X,\widetilde P}$ is injective for each $\widetilde P$ above $P$. Suppose that $P$ is not regular, and let $a\in\mco_{X,P}$ be a local equation of $Z$ at $P$.

If $P$ has more than one preimage $P_1,\ldots,P_n$, $n\geq2$, then a rational function with a zero or a pole at $P$ has one at each $P_i$, so
$$
\nu^*\mco_X(Z)\cong\mco_{\widetilde X}(c_1P_1+\cdots+c_nP_n)
$$
with every $c_i>0$, and
$$
\deg\nu^*\mcl=\deg\nu^*\mco_X(Z)-1\geq n-1>0.
$$

If $P$ has exactly one preimage $\widetilde P$, then $\mco_{X,P}\to\mco_{\widetilde X,\widetilde P}$ sends $\mm_P$ into $\mm_{\widetilde P}^2$. Otherwise the image of $\mm_P$ in $\mm_{\widetilde P}/\mm_{\widetilde P}^2$ is nonzero; that $k$-vector space is one-dimensional, because $\mco_{\widetilde X,\widetilde P}$ is an integrally closed noetherian local domain of dimension one and hence a regular local ring (I.6.2A); so $\mm_P\to\mm_{\widetilde P}/\mm_{\widetilde P}^2$ is surjective. The other two hypotheses of II.7.4 hold as well: the two residue fields are both $k$, closed points of schemes of finite type over the algebraically closed field $k$ having residue field $k$ (I.1.3A), and $\mco_{\widetilde X,\widetilde P}$ is a finitely generated $\mco_{X,P}$-module by the finiteness of $\nu$. Lemma II.7.4 then makes $\mco_{X,P}\to\mco_{\widetilde X,\widetilde P}$ surjective, hence an isomorphism, and $\mco_{X,P}$ would be a discrete valuation ring and $P$ a regular point, contrary to the supposition. So $\nu^*(a)\in\mm_{\widetilde P}^2$, and
$$
\deg\nu^*\mcl=\deg\nu^*\mco_X(Z)-1\geq2-1>0.
$$

In either case $\deg\nu^*\mcl>0$. On the other hand $\mcl\in\Pic^0X$, so by Exercise IV.1.9(c) there is a divisor $D_0$ with support in $X_{\reg}$, of degree zero, with $\mcl\cong\mco_X(D_0)$; since $\nu$ is an isomorphism above $X_{\reg}$,
$$
\deg\nu^*\mcl=\deg\nu^*\mco_X(D_0)=\deg D_0=0,
$$
a contradiction. Hence $P\in X_{\reg}$.

The Euler characteristic computation of step [](#s6){.pf-ref} forces the same conclusion in one line: $\mco_{X,P}/(a)=\mco_{Z,P}$ has length $\length(Z)=1$, so $(a)$ is a maximal ideal, hence $(a)=\mm_P$ is principal, and $P$ is regular by I.6.2A. The two-case argument is written out because it is the published one and because it uses neither that computation nor the principal ideal criterion.

:::

:::

By step [](#s6-regular){.pf-ref}, $P\in X_{\reg}$, so $Z=P$ as effective Cartier
divisors and
$$
\mcl(E)\cong\mco_X(P).
$$
Since $E=D+P_0$,
$$
\mcl
\cong
\mcl(D)
\cong
\mco_X(P-P_0)
=
\Phi(P).
$$
Thus $\Phi$ is surjective.

:::

:::

::: {.pf-step #s7}

Therefore
$$
\boxed{
X_{\reg}\xrightarrow{\sim}\Pic^0X,
\qquad
P\longmapsto\mcl(P-P_0).
}
$$

::: pf-proof

Step [](#s4){.pf-ref} makes the map well defined, step [](#s5){.pf-ref} proves injectivity, and
step [](#s6){.pf-ref} proves surjectivity.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required one-to-one correspondence with $\Pic^0X$.

:::

:::

:::

::: {.remark title="Published solution"}
The solution printed for this exercise is Exercise 10 of §1 of *Algebraic Geometry II*, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), Chapter IV, by Ping-Hsun Chuang, printed p. 4 of `tmp/sources/ntu-ag2-chapter4.pdf`, text version `tmp/sources/ntu-ag2-chapter4.md`. It takes $\deg K=p_a-1$ from Exercise IV.1.9 read with Serre duality for the dualizing sheaf of a locally complete intersection, obtains $\ell(D+P_0)=1$ and $\ell(K-D-P_0)=0$ for $[\mcl(D)]\in\Pic^0X$, and concludes that a unique effective $R$ satisfies $R\sim D+P_0$. Its final sentence passes from that $R$ to the bijection $X_{\reg}\to\Pic^0X$: that the point supporting $R$ is a regular point of $X$ is asserted there and not argued.

The argument for that step is KReiser's, answer 4978046 (https://math.stackexchange.com/a/4978046), posted 2024-09-29 to Math Stack Exchange question 4962032, "Hartshorne Exercise IV.1.10: making sure a point is nonsingular" (asked by François Gatine on 2024-08-23), an accepted answer to a question that asks for this step alone. It normalizes $X$ and splits on the number of points above the point of the divisor: with two or more, a function with a zero or a pole at that point has one at each of them, so the pullback of $\mco_X(P-P_0)$ has positive degree; with one, the local criterion II.7.4 applied to the finite normalization rules out the surjectivity of $\mm_P$ onto $\mm_{\widetilde P}/\mm_{\widetilde P}^2$, since that would make $\mco_{X,P}\to\mco_{\widetilde X,\widetilde P}$ an isomorphism and $P$ a regular point, so the local equation of $P$ pulls back into $\mm_{\widetilde P}^2$, the pullback of $\mco_X(P)$ has multiplicity at least $2$ at $\widetilde P$, and the pullback of $\mco_X(P-P_0)$ has positive degree again; while a line bundle of degree zero is $\mco_X(D_0)$ for a divisor $D_0$ supported in $X_{\reg}$ (IV.1.9(c)), whose pullback has degree zero. The two ingredients the answer leaves to the reader are supplied in step [](#s6-regular){.pf-ref}: that $\mm_{\widetilde P}/\mm_{\widetilde P}^2$ is one dimensional, from I.6.2A, and that the pullback of a Cartier divisor supported in $X_{\reg}$ has degree zero, from $\nu$ being an isomorphism over $X_{\reg}$. The argument uses neither $p_a=1$ nor the locally complete intersection hypothesis, so it places the point of every degree zero class in $X_{\reg}$ on any integral projective curve.

R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, 21 October 2025 version [@Vak25, §19.9], text version `tmp/sources/vakil-rising-sea-2025-10-21.md`, printed pp. 555--556, gives the bijection $\Pic^0 C\leftrightarrow$ degree 1 points for a regular curve $C$ of genus 1: (19.9.1) $\omega_C\cong\mco_C$ and $h^0(C,\mcl)=\deg\mcl$ for $\deg\mcl>0$; (19.9.2) every degree 1 bundle is the divisor of a point, and distinct points give distinct bundles because a degree 1 bundle has one section up to scalars; (19.9.3) twisting by $\mco(-p)$ gives the bijection. Steps [](#s5){.pf-ref} and the existence half of step [](#s6){.pf-ref} transcribe that. Vakil's curve is regular, so his §19.9 does not cover the exercise's $X$, which is only a locally complete intersection with $p_a=1$ and may be singular; the point of the divisor of zeros is put in $X_{\reg}$ by step [](#s6-regular){.pf-ref}, and that argument is not his.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.1.10, printed pp. 209--210, text version `tmp/sources/hartshorne-solutions-egbert.md` (entry 4.1.14), takes $\deg K_X=p_a-1$ from IV.1.9(d), so a divisor of degree zero has $K_X-D-P_0$ of degree $-1$ and hence no sections, and concludes that $\dim\linearsystem{D+P_0}=\deg D=0$; the resulting assignment of degree-one divisors to points of $\Pic^0 X$ is the bijection with which the card identifies $\Pic^0 X$ for $p_a=1$.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.1.10, printed p. 85, argues in the pattern of (1.3.7): with $p_a=1$ the canonical divisor has degree $p_a-1=0$ by the previous exercise, so for a degree-zero $D$ the divisor $D+P_0$ corresponds to an invertible sheaf of a divisor supported on $X_{\reg}$, and on $X_{\reg}$ the degree-zero divisor $D_0-P_0$ corresponds to some $P-P_0$ by (II, 1.3.7); hence $D\sim P-P_0$ for a regular point $P$, and conversely every such difference is a degree-zero invertible sheaf, so $X_{\reg}\to\Pic^0X$ is a bijection.
:::
