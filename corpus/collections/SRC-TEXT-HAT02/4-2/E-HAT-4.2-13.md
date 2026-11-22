---
schema: qual/card@1
id: E-HAT-4.2-13
kind: problem
title: "Isomorphism on $\\pi_i$ for $i \\leq n$ in $n$-dimensional complexes"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 13; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 13 (AT.txt 19396-19398) and correct as it stands. Checked the
    delicate step: the pair (M_f~, X~) is n-connected, so relative Hurewicz kills H_i for i<=n and
    identifies pi_{n+1} of the pair with H_{n+1} of the pair; pi_{n+1}(M_f~,X~) is a quotient of
    pi_{n+1}(M_f~) because pi_n(X~) -> pi_n(M_f~) is an isomorphism; and that quotient maps to
    H_{n+1}(M_f~) = H_{n+1}(Y~) = 0 by naturality, since Y~ is n-dimensional. Hence H_{n+1} of the pair
    vanishes too, the homology exact sequence gives an isomorphism in degrees <= n, and both sides vanish
    above n, so the lift is a homology isomorphism in all degrees. Then Exercise 12 applies. Also checked
    the low cases the card separates: n=0 gives two points, and n=1 gives contractible universal covers so
    Exercise 12 applies directly. Not checked: nothing outside this exercise.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument above, whose shape is correct.
    Made explicit: the vanishing of $\pi_i$ of the mapping-cylinder pair from the two long
    exact sequences, the surjectivity half of the relative Hurewicz theorem being all that is
    needed in degree $n+1$ (the prose used the isomorphism it does not give), the naturality
    square that kills the Hurewicz images, and the two low-dimensional cases. Cited:
    Proposition 4.1 printed p. 342, the pair sequence printed p. 344, Theorem 4.37 printed
    p. 371, Exercise 12 printed p. 389, the exercise printed p. 390. Not claimed: a retained
    solution set, so the argument is the card's own; and the citation of Corollary 2.34 for
    the vanishing of $H_{>n}$ of an $n$-dimensional CW complex is by chapter and statement,
    the cellular argument on printed p. 139 being the reason.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Correction to this date's earlier note, from a search of the retained sets after the
    proof was written. The card said no retained solution set covers the exercise; Steven
    V. Sam's set does, at Exercise 4.2.13, PDF p. 22, following the same reduction and
    closing with Exercise 4.2.12. The body now cites it and states what the card supplies
    that the set does not: the pair $(M_{\widetilde f},\widetilde X)$ and the relative
    Hurewicz step in degree $n+1$. Mathematics unchanged and re-read; the exercise is on
    printed p. 390.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.2 Exercise 13, Proposition 4.1,
    Theorem 4.37, Theorem 4.5 and Corollary 2.34. Two repairs. (1) Step `conclusion` deduced the
    homotopy equivalence from "Exercise 12 of §4.2", which is a different exercise and is not proved on
    this card, so the proof did not close on its own. It now closes on Corollary 4.33: the lift is a
    homology isomorphism between simply connected CW complexes, hence a homotopy equivalence, hence an
    isomorphism on pi_i for every i >= 2, which transfers to f through the covers, and f is an
    isomorphism on pi_1 by hypothesis; Theorem 4.5 then gives the homotopy equivalence. A first version
    of this repair argued that pi_i(X) = pi_i(Y) = 0 for i > n because both complexes are n-dimensional,
    which is false — S^2 is 2-dimensional and pi_3(S^2) = Z — and it is withdrawn here.
    (2) Step `n-connected` said the pair is "(n-1)-connected" while giving the vanishing for i <= n,
    which is n-connectedness; the wording now matches the claim, and the step relying on it in the
    Hurewicz argument says which degrees follow from the vanishing of pi and which from the isomorphism
    form. The remaining steps are correct as written: the lift to universal covers exists because f_*
    on pi_1 is an isomorphism, the maps on pi_i for 2 <= i <= n agree under the covers, the pair
    sequence makes the relative groups vanish in degrees at most n, and the boundary map in
    pi_{n+1} is killed by the vanishing of H_{n+1} of the n-dimensional cover.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Independent referee read against Hatcher, Algebraic Topology (2002), §4.2 Exercise 13,
    Proposition 1.33, Proposition 4.1, Theorem 4.37, Lemma 2.34 and Corollary 4.33, and
    against Steven V. Sam's solutions, Exercise 4.2.13, whose part the solution block
    transcribes and which is unchanged. Two defects repaired in the card's own step. (1) The
    proof of step `lift` applied the lifting criterion to $f$ itself and concluded that
    $f_*\pi_1(X)=0$; under the hypothesis $f_*\pi_1(X)=\pi_1(Y)$ that is false whenever
    $\pi_1(Y)\ne0$. The criterion applies to the composite $fp_X:\widetilde X\to Y$, whose
    domain is simply connected, and the proof now says so. (2) The proof of step
    `homology-iso` cited "Corollary 2.34" for the vanishing of $H_i$ above the dimension of a
    CW complex; the book has no such corollary, the statement being Lemma 2.34(b), and the
    citation now reads that. The remaining steps were read and are unchanged: the pair
    sequence of the mapping cylinder in `n-connected`, the relative Hurewicz theorem in
    `hurewicz-low` and `hurewicz-degree` with the pair $n$-connected, the boundary map
    vanishing because the map on $\pi_n$ is injective, `homology-iso` and the closing
    Whitehead and Hurewicz applications, and the two low-dimensional cases. Not claimed:
    anything beyond this exercise, and no page locator is written here.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Second pass on the same card, from six reader reports that flagged the low-dimensional
    step. The proof of step `low-dimensions` asserted that "a map whose lift to universal
    covers is a homotopy equivalence is itself a homotopy equivalence", which is false:
    $z\mapsto z^2$ on $S^1$ lifts to $t\mapsto2t$ on $\RR$, a homeomorphism, and is
    not a homotopy equivalence. The step now proves the case $n=1$ from numbered statements:
    the universal covers are connected graphs (Lemma 1A.3) and, being simply connected,
    trees, as the consequence stated after Proposition 1A.2 records; the deformation
    retraction in the proof of Proposition 1A.1 contracts a tree to a vertex, so $\pi_i$
    vanishes above degree $1$ (Proposition 4.1), $f_*$ is an isomorphism on every $\pi_i$,
    and Theorem 4.5 makes $f$ a homotopy equivalence. The clause in the preceding event of
    this date that listed the low-dimensional case among the steps read and left unchanged is
    superseded by this one; the two repairs that event records stand.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Item 8 of the current #163 repair split. Read Hatcher's Theorem 4.37 at its actual
    statement and Sam's §4.2 Exercise 13. Theorem 4.37, applied to the $n$-connected
    mapping-cylinder pair with parameter $n+1$, gives an isomorphism from the quotient
    $\pi'_{n+1}$; composing with the quotient surjection gives the required ordinary
    relative Hurewicz surjection in degree $n+1$. The previous proof attributed that
    surjection to the theorem without the quotient step. Sam's solution also leaves this
    relative-Hurewicz argument implicit, and its last sentence writes $f$ where its
    construction requires $\widetilde f$; the card now records both features rather than
    certifying the compressed source verbatim. The rest of the proof and statement are
    unchanged.
---

::: {.problem}
Show that a map between connected $n$-dimensional CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_i$ for $i \leq n$. [Pass to universal covers and use homology.]
:::

::: {.solution}
The published solution is **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), §4.2 Exercise 13**: the passage to universal covers, the reduction to proving that $\widetilde f$ is a homology isomorphism, and the closing appeal to Exercise 4.2.12 are that solution's. What the card supplies is the step the set elides: the absolute Hurewicz theorem does not apply to $\widetilde X$, whose own homotopy groups need not vanish below $n$, so the argument runs through the relative Hurewicz theorem for the mapping-cylinder pair, Theorem 4.37, and needs its surjectivity in degree $n+1$. Sam's last sentence writes $f$ where his construction requires $\widetilde f$; that slip is not reproduced. The statement is Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 13, and the hint followed is the exercise's own.

Throughout $f:X\to Y$ is a map of connected $n$-dimensional CW complexes inducing isomorphisms $f_*:\pi_i(X)\to\pi_i(Y)$ for $i\le n$, and $p_X:\widetilde X\to X$, $p_Y:\widetilde Y\to Y$ are the universal covers.

::: pf

::: {.pf-step #lift}
$f_*$ is an isomorphism on $\pi_1$, so $f$ lifts to a map of universal covers $\widetilde f:\widetilde X\to\widetilde Y$ with $p_Y\widetilde f=fp_X$, and $\widetilde f_*:\pi_i(\widetilde X)\to\pi_i(\widetilde Y)$ is an isomorphism for $2\le i\le n$.

::: pf-proof
Choose basepoints with $f(x_0)=y_0$. The composite $fp_X:\widetilde X\to Y$ carries $\pi_1(\widetilde X)=0$ into $p_{Y*}\pi_1(\widetilde Y)=0$, so the lifting criterion (Proposition 1.33), applied to $fp_X$, gives $\widetilde f:\widetilde X\to\widetilde Y$ with $p_Y\widetilde f=fp_X$; its hypotheses hold, $\widetilde X$ being path-connected and locally path-connected. For $i\ge2$ the covering projection induces an isomorphism $\pi_i(\widetilde X)\cong\pi_i(X)$ and likewise for $Y$ (Proposition 4.1), so $\widetilde f_*$ is the conjugate of $f_*$ and is an isomorphism in the stated range.

:::

:::

::: {.pf-step #low-dimensions}
The claim holds for $n\le1$.

::: pf-proof
For $n=0$ a connected $0$-dimensional CW complex is a point, so $f$ is a homeomorphism. For $n=1$ the universal covers $\widetilde X$ and $\widetilde Y$ are connected graphs by Lemma 1A.3, and being simply connected they are trees, as the consequence stated after Proposition 1A.2 records; the deformation retraction constructed in the proof of Proposition 1A.1 then contracts each onto a vertex, so both are contractible. Hence $\pi_i(\widetilde X)=\pi_i(\widetilde Y)=0$ for $i\ge2$, and Proposition 4.1 gives $\pi_i(X)=\pi_i(Y)=0$ for $i\ge2$. With $f_*$ an isomorphism on $\pi_1$ by hypothesis, $f_*$ is an isomorphism on every $\pi_i$, and Whitehead's theorem (Theorem 4.5) makes $f$ a homotopy equivalence. The lift $\widetilde f$ is a map between contractible spaces and so is itself a homotopy equivalence, but that alone does not give the conclusion: $z\mapsto z^2$ on $S^1$ lifts to $t\mapsto2t$ on $\RR$, a homeomorphism, and is not a homotopy equivalence.

:::

:::

::: {.pf-step #n-connected}
For $n\ge2$ the pair $(M_{\widetilde f},\widetilde X)$, where $M_{\widetilde f}$ is the mapping cylinder of $\widetilde f$, is $n$-connected: $\pi_i(M_{\widetilde f},\widetilde X)=0$ for $i\le n$.

::: pf-proof
The pair is path connected. Its homotopy exact sequence (§4.1) reads
$$
\pi_i(\widetilde X)\xrightarrow{\ \widetilde f_*\ }\pi_i(\widetilde Y)\to\pi_i(M_{\widetilde f},\widetilde X)\to\pi_{i-1}(\widetilde X)\xrightarrow{\ \widetilde f_*\ }\pi_{i-1}(\widetilde Y)
$$
for $i\ge2$, using $M_{\widetilde f}\simeq\widetilde Y$. For $2\le i\le n$ both outer maps are isomorphisms by step [](#lift){.pf-ref}, so the middle group is zero; for $i=1$ the pair is simply connected relative to $\widetilde X$ because $\widetilde X$ is, and $\pi_1$ of the pair vanishes whenever the inclusion induces a surjection on $\pi_1$.

:::

:::

::: {.pf-step #hurewicz-low}
$H_i(M_{\widetilde f},\widetilde X;\ZZ)=0$ for $i\le n$.

::: pf-proof
The relative Hurewicz theorem (Theorem 4.37) applies to the $n$-connected pair of step [](#n-connected){.pf-ref}, whose spaces are simply connected, so the $\pi_1$-action is trivial; it gives $H_i(M_{\widetilde f},\widetilde X)=0$ for $i<n$, and $H_n(M_{\widetilde f},\widetilde X)=0$ as well because $\pi_n(M_{\widetilde f},\widetilde X)=0$ and the Hurewicz map is an isomorphism in degree $n$. So $H_i(M_{\widetilde f},\widetilde X)=0$ for $i\le n$.

:::

:::

::: {.pf-step #hurewicz-degree}
$H_{n+1}(M_{\widetilde f},\widetilde X;\ZZ)=0$.

::: pf-proof
Apply Theorem 4.37 with parameter $n+1$ to the pair of step [](#n-connected){.pf-ref}, which is $n$-connected. It gives an isomorphism $h':\pi'_{n+1}(M_{\widetilde f},\widetilde X)\to H_{n+1}(M_{\widetilde f},\widetilde X)$, where $\pi'_{n+1}$ is the quotient of $\pi_{n+1}$ defined immediately before the theorem; here the quotient is in fact $\pi_{n+1}$ itself because $\widetilde X$ is simply connected. In every case the quotient map $q:\pi_{n+1}\to\pi'_{n+1}$ is surjective and the ordinary relative Hurewicz map is $h=h'q$, so
$$
h:\pi_{n+1}(M_{\widetilde f},\widetilde X)\longrightarrow H_{n+1}(M_{\widetilde f},\widetilde X)
$$
is surjective. It is therefore enough to show that every element of the source dies. Exactness of the pair sequence, with $\pi_n(\widetilde X)\to\pi_n(M_{\widetilde f})$ an isomorphism by step [](#lift){.pf-ref}, shows that every element of $\pi_{n+1}(M_{\widetilde f},\widetilde X)$ is the image of an element of $\pi_{n+1}(M_{\widetilde f})$, and naturality of the Hurewicz map makes the diagram
$$
\begin{array}{ccc}
\pi_{n+1}(M_{\widetilde f})&\longrightarrow&\pi_{n+1}(M_{\widetilde f},\widetilde X)\\
\downarrow&&\downarrow\\
H_{n+1}(M_{\widetilde f})&\longrightarrow&H_{n+1}(M_{\widetilde f},\widetilde X)
\end{array}
$$
commute. Since $M_{\widetilde f}\simeq\widetilde Y$ and $\widetilde Y$ is an $n$-dimensional CW complex, $H_{n+1}(M_{\widetilde f})=H_{n+1}(\widetilde Y)=0$, so the image of every element is zero.

:::

:::

::: {.pf-step #homology-iso}
$\widetilde f_*:H_i(\widetilde X)\to H_i(\widetilde Y)$ is an isomorphism for all $i$.

::: pf-proof
The long exact sequence of the pair $(M_{\widetilde f},\widetilde X)$, with $M_{\widetilde f}\simeq\widetilde Y$, contains
$$
H_{i+1}(M_{\widetilde f},\widetilde X)\to H_i(\widetilde X)\to H_i(\widetilde Y)\to H_i(M_{\widetilde f},\widetilde X) .
$$
For $i\le n$ the outer groups vanish by step [](#hurewicz-low){.pf-ref} and step [](#hurewicz-degree){.pf-ref} (the latter for $i=n$), so the middle map is an isomorphism for $i\le n$. For $i>n$ both $\widetilde X$ and $\widetilde Y$ are $n$-dimensional CW complexes, so both groups vanish (Lemma 2.34(b), or the cellular complex of §2.2), and the map between two zero groups is an isomorphism.

:::

:::

::: {.pf-step #conclusion}
$f$ is a homotopy equivalence.

::: pf-proof
Step [](#homology-iso){.pf-ref} says that $\widetilde f:\widetilde X\to\widetilde Y$ is a homology isomorphism, and $\widetilde X,\widetilde Y$ are simply connected CW complexes, so $\widetilde f$ is a homotopy equivalence by the homology form of Whitehead's theorem (Corollary 4.33). It follows that $\widetilde f_*:\pi_i(\widetilde X)\to\pi_i(\widetilde Y)$ is an isomorphism for every $i\ge2$, and the covering projections identify $\pi_i(\widetilde X)$ with $\pi_i(X)$ and $\pi_i(\widetilde Y)$ with $\pi_i(Y)$ in that range, with $f_*$ the conjugate of $\widetilde f_*$; so $f_*$ is an isomorphism on $\pi_i$ for $i\ge2$. On $\pi_1$ it is an isomorphism by hypothesis. Hence $f$ is a weak homotopy equivalence between CW complexes, and Whitehead's theorem (Theorem 4.5) makes it a homotopy equivalence.

:::

:::

:::
:::
