---
schema: qual/card@1
id: E-HAT-3.A-2
kind: problem
title: "Tor with $\\QQ/\\ZZ$ and the torsion subgroup"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Converted from prose to numbered steps under #2, six of them, each with its proof, transcribing
    Weibel, *An Introduction to Homological Algebra*, §3.1: Calculation 3.1.1 for the cyclic groups,
    Proposition 3.1.3 for the second variable read through the direct limit, the Balancing Remark for
    the first, Proposition 3.1.4 and Corollary 3.1.5 for the torsionfree equivalence. The colimit
    corollary is cited as Corollary 2.6.16 with the balancing theorem 2.7.2, which is the form the
    first-variable limit needs; the card's earlier paragraph arguing that point is folded into the
    step. Every locator is gone from the body: the passage now cites Lemma 3A.2, Calculation 3.1.1,
    Propositions 3.1.3 and 3.1.4 and Corollaries 2.6.16 and 3.1.5 by number, with no page. Not
    checked: no certificate, and Weibel's printed statements were used as the card already recorded
    them rather than re-read in this pass.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.A, Exercise 2; it matches the printed text. The card originally ended "... torsionfree if $\operatorname{Tor}(A,B)=0$ for all $B$" where the print says "iff"; the missing direction is restored.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.A Exercise 2, printed p. 267. The statement
    matches the print, whose second sentence is "Deduce that $A$ is torsionfree iff
    $\operatorname{Tor}(A,B)=0$ for all $B$"; the card's "iff" is correct. Repaired where the proof
    asserted rather than derived: the four-term sequence is now obtained from the six-term sequence
    of Proposition 3A.5(6) with both vanishing Tor terms named through Proposition 3A.5(3) (p. 265)
    instead of the unexplained "$\QQ$ is flat"; and the identification of $\ker(A\to A\otimes\QQ)$
    with $T(A)$ is now computed in the localisation $S^{-1}A$ at $S=\ZZ\setminus\{0\}$, where
    $a/1=0$ iff $sa=0$ for some $s\in S$. Checked against Hatcher's definition of Tor by free
    resolutions (Lemma 3A.2, p. 263) and against the statement of Proposition 3A.5(3) that
    torsionfree coefficient groups kill Tor. No published solution of this exercise is in the
    retained sets; recorded in COMPLAINTS.md.
- event: solution-reviewed
  by: claude
  date: 2026-11-11
  note: >-
    The statement is published with a complete proof as Weibel, *An Introduction to Homological
    Algebra* (Cambridge Studies in Advanced Mathematics 38, 1994), §3.1, Proposition 3.1.3 and the
    Remark following Proposition 3.1.4, printed p. 67, with Corollary 3.1.5 on the same page for the
    deduction and Calculation 3.1.1 on p. 66 for $\operatorname{Tor}(\ZZ/n,B)\cong B[n]$; the reading
    copy is `tmp/sources/weibel-03-tor-and-ext.pdf` and the colimit corollary it invokes is
    `tmp/sources/weibel-02-derived-functors.pdf`, printed p. 58. Read there, not from a snippet, on
    2026-11-11, after searching outside the retained sets; COMPLAINTS.md records the search. The
    published proof is the colimit route and is now stated on the card in its own paragraph; the
    card's argument is the exact-sequence route with the same two conclusions, checked step by step
    against Hatcher's Proposition 3A.5(3) and (6) (p. 265) and his definition of $\operatorname{Tor}$
    through free resolutions (Lemma 3A.2, p. 263). Not claimed: that the two proofs are written out
    identically — they are two proofs of the same two statements, and the card says which is which.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    Re-read for the published-solution obligation. The published complete proof is Weibel, *An Introduction to Homological Algebra* (Cambridge Studies in Advanced Mathematics 38, 1994), §3.1: Proposition 3.1.3 and the Remark after Proposition 3.1.4, printed p. 67, identify $\operatorname{Tor}_1^\ZZ(\QQ/\ZZ,B)$ with the torsion subgroup, balancing gives $\operatorname{Tor}(A,\QQ/\ZZ)=T(A)$, Corollary 3.1.5 on the same page is the deduction, and Calculation 3.1.1 on p. 66 computes $\operatorname{Tor}(\ZZ/n,B)\cong B[n]$; the direct-limit corollary Weibel invokes is Corollary 2.6.17, printed p. 58. Checked against the book: Hatcher's Exercise 2 of §3.A on printed p. 267, its `iff', and Proposition 3A.5(3) and (6) on p. 265 which the card's second route uses. Not claimed: that the card's two routes are written the same way; the card states which is Weibel's colimit route and which is its own exact-sequence route, and both conclusions are the same two statements.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The proof is now the transcription of Weibel, *An Introduction to Homological Algebra* (Cambridge
    Studies in Advanced Mathematics 38, 1994), §3.1, printed pp. 66--67: Calculation 3.1.1 on p. 66
    for $\operatorname{Tor}_*^{\ZZ}(\ZZ/n,B)$ from the resolution $0\to\ZZ\to\ZZ\to\ZZ/n\to0$,
    Proposition 3.1.3 on p. 67 with its colimit computation, the Remark (Balancing Tor) on p. 67,
    Proposition 3.1.4 and Corollary 3.1.5 on p. 67. Two points checked against the book and stated on
    the card: the union in Weibel's proof of Proposition 3.1.3 runs over all $n$, not only over the
    primes, since over the primes alone it would be the elements of prime order; and the colimit
    corollary he invokes is printed as Corollary 2.6.17, p. 58, in the *second* variable, while the
    use is the first-variable form, which is Corollary 2.6.16 on the same page applied to
    $-\otimes_\ZZ B$ (whose derived functors are $\operatorname{Tor}_*^{\ZZ}(-,B)$ by Theorem 2.7.2,
    p. 58); Weibel cites 2.6.17 for the same first-variable statement in the proof of Proposition
    3.1.2, p. 66. Corollary 3.1.5 is printed with no proof of its own, so the two implications the
    exercise asks for are written out on the card and marked as that derivation. The card's former
    proof by the six-term sequence of Hatcher's Proposition 3A.5 and the localisation $S^{-1}A$ is
    withdrawn with this rewrite; it reached the same two conclusions. Checked against Hatcher (2002),
    §3.A Exercise 2, printed p. 267, whose Tor is $\operatorname{Tor}_1^{\ZZ}$ by Lemma 3A.2, p. 263.
    Not claimed: that Weibel states Hatcher's exercise, or that a retained solution set contains it.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The display of Calculation 3.1.1 used the letter $n$ for the degree and for the modulus of the
    cyclic group at once, in $\operatorname{Tor}_n^{\ZZ}(\ZZ/n,B)=0\ (n\ge2)$, where the intended
    meaning is that all higher Tor vanish. The degree index is now $i$, so the three values read
    $\operatorname{Tor}_0^{\ZZ}(\ZZ/n,B)=B/nB$, $\operatorname{Tor}_1^{\ZZ}(\ZZ/n,B)=B[n]$ and
    $\operatorname{Tor}_i^{\ZZ}(\ZZ/n,B)=0$ for $i\ge2$. Nothing else changes. Checked against
    Weibel, *An Introduction to Homological Algebra*, Calculation 3.1.1 on printed p. 66, and against
    Hatcher (2002), §3.A Exercise 2 on printed p. 267 with the remark on printed p. 263 that
    $\operatorname{Tor}_n=0$ for $n>1$.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Citations only; the statement and the proof are unchanged. Every citation on this card named a
    PDF. The text versions are now named where the sources are named. Weibel's §3.1 is read in
    `tmp/sources/weibel-03-tor-and-ext.md`, and the colimit corollaries of §2.6--2.7 in
    `tmp/sources/weibel-02-derived-functors.md`; both were opened this pass and do contain the cited
    items --- Calculation 3.1.1, Proposition 3.1.3 and Corollary 3.1.5 in the first, Corollaries
    2.6.16, 2.6.17 and Theorem 2.7.2 in the second. Hatcher is read in
    `tmp/sources/hatcher-2002-algebraic-topology.md`. Checked against Hatcher (2002), §3.A Exercise 2
    on printed p. 267, and against the book's remark on printed p. 263 that $\operatorname{Tor}_n=0$
    for $n>1$. Not claimed: a text version for any other source, this card citing none; nothing was
    read from a rendered page.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    The card's certificate, and where it is. Both sentences of the printed exercise are proved for
    every abelian group $A$ at
    <https://github.com/dzackgarza/lean-categories/blob/5848f0f2f881ba032eb8bb69baa051300498ba6b/LeanCategories/Homological/TorExercise3A2.lean>:
    `torOneQzAddEquivTorsion` is
    $\operatorname{Tor}_1^\ZZ(A,\QQ/\ZZ)\cong\operatorname{torsion}_\ZZ A$ at `TorBridge.torOne`,
    the left derived functor of `tensorLeft B`, and
    `isTorsionFree_iff_forall_subsingleton_torOne` is "$A$ torsionfree iff
    $\operatorname{Tor}_1^\ZZ(A,B)=0$ for every abelian group $B$", both directions. Neither
    hypothesis mentions finiteness: the presentation is $\pi:(A\to_0\ZZ)\to A$, free on $A$ itself,
    and the first statement is read off the kernel of that presentation's syzygy inclusion. Checked
    in this pass by reading that file at that commit rather than the registry row's description of
    it: both declarations are there with those statements, the module imports only Mathlib and the
    repository's own `TorReductions` and `TorExercise3A6`, and the file contains no `sorry` and no
    `axiom`. Not checked in this pass: the file was not re-elaborated here, and the elaboration
    recorded for it --- Lean 4.36.0 at Mathlib `6d97e8ad`, axioms `propext`, `Classical.choice`,
    `Quot.sound`, no `sorryAx` --- is the one section 1's row records. The proof above is Weibel's
    colimit-and-balancing argument; the certificate proves the same two statements without it, so
    the certificate covers the card's claim and not this page's route.
---

::: {.problem}
Show that $\operatorname{Tor}(A, \QQ/\ZZ)$ is isomorphic to the torsion subgroup of $A$.
Deduce that $A$ is torsionfree iff $\operatorname{Tor}(A, B) = 0$ for all $B$.
:::

::: {.solution}
Write $\operatorname{Tor}=\operatorname{Tor}_1^{\ZZ}$. Hatcher records, immediately after Lemma 3A.2, that $\operatorname{Tor}_n^{\ZZ}(H,G)=0$ for $n>1$ because a free resolution $0\to F_1\to F_0\to H\to0$ always exists, and that $\operatorname{Tor}_1$ is written $\operatorname{Tor}$; so the two groups below are $\operatorname{Tor}_1^{\ZZ}(A,\QQ/\ZZ)$ and $\operatorname{Tor}_1^{\ZZ}(A,B)$. The argument is Weibel, *An Introduction to Homological Algebra* (Cambridge Studies in Advanced Mathematics 38, 1994), §3.1, in the book's own steps, read in `tmp/sources/weibel-03-tor-and-ext.md` and, for the colimit corollaries of §2.6 and the balancing of §2.7, in `tmp/sources/weibel-02-derived-functors.md`.

::: pf

::: {.pf-step #cyclic}
For $n\ge1$ and any $B$, $\operatorname{Tor}_0^{\ZZ}(\ZZ/n,B)=B/nB$, $\operatorname{Tor}_1^{\ZZ}(\ZZ/n,B)=B[n]\coloneqq\{b\in B:nb=0\}$, and $\operatorname{Tor}_i^{\ZZ}(\ZZ/n,B)=0$ for $i\ge2$.

::: pf-proof
This is Weibel's Calculation 3.1.1. The free resolution $0\to\ZZ\xrightarrow{n}\ZZ\to\ZZ/n\to0$ computes $\operatorname{Tor}_*^{\ZZ}(\ZZ/n,B)$ as the homology of $0\to B\xrightarrow{n}B\to0$, which is $B/nB$ in degree $0$, the kernel $B[n]$ in degree $1$, and zero above.
:::

:::

::: {.pf-step #torsion-second}
$\operatorname{Tor}_1^{\ZZ}(\QQ/\ZZ,B)\cong T(B)$, the torsion subgroup of $B$.

::: pf-proof
$\QQ/\ZZ$ is the direct limit of its finite cyclic subgroups, indexed by the finite cyclic subgroups ordered by divisibility, and $\operatorname{Tor}$ commutes with direct limits: Corollary 2.6.16, applied to the left adjoint $-\otimes_\ZZ B$ in $\ZZ$-mod, whose left derived functors are $\operatorname{Tor}_*^{\ZZ}(-,B)$ by the balancing theorem 2.7.2. So $\operatorname{Tor}_1^{\ZZ}(\QQ/\ZZ,B)\cong\varinjlim_n\operatorname{Tor}_1^{\ZZ}(\ZZ/n,B)\cong\varinjlim_nB[n]=\bigcup_{n\ge1}B[n]=T(B)$, by step [](#cyclic){.pf-ref}. The union is over all $n\ge1$ rather than the primes, since $B[n]$ is the set of elements of order dividing $n$.
:::

:::

::: {.pf-step #first}
$\operatorname{Tor}^{\ZZ}(A,\QQ/\ZZ)\cong T(A)$, the torsion subgroup of $A$.

::: pf-proof
This is Weibel's Proposition 3.1.3 with $B$ replaced by $A$, that $\operatorname{Tor}_1^{\ZZ}(\QQ/\ZZ,B)\cong T(B)$ for every $B$; step [](#torsion-second){.pf-ref} is the same statement with the roles of the variables kept apart. The book draws the conclusion in one sentence in its Remark on the Proposition.
:::

:::

::: {.pf-step #torsionfree}
If $A$ is torsionfree then $\operatorname{Tor}_n^{\ZZ}(A,B)=0$ for every $n\ne0$ and every $B$.

::: pf-proof
A torsionfree abelian group is the direct limit of its finitely generated subgroups, each isomorphic to some $\ZZ^m$; by the same colimit formula of step [](#torsion-second){.pf-ref}, $\operatorname{Tor}_n^{\ZZ}(A,B)\cong\varinjlim_m\operatorname{Tor}_n^{\ZZ}(\ZZ^m,B)$, and each term vanishes for $n\ne0$ because $\ZZ^m$ is free and hence projective. This is Weibel's Proposition 3.1.4.
:::

:::

::: {.pf-step #converse}
If $\operatorname{Tor}^{\ZZ}(A,B)=0$ for every $B$ then $A$ is torsionfree.

::: pf-proof
Take $B=\QQ/\ZZ$. Step [](#first){.pf-ref} identifies $\operatorname{Tor}^{\ZZ}(A,\QQ/\ZZ)$ with $T(A)$, so the hypothesis gives $T(A)=0$, which says that no nonzero element of $A$ has finite order. This is the converse half of Weibel's Corollary 3.1.5, which the book prints for both variables without a separate proof, deriving it from Proposition 3.1.4 and the Remark.
:::

:::

::: {.pf-step}
$\operatorname{Tor}(A,\QQ/\ZZ)\cong T(A)$, and $A$ is torsionfree if and only if $\operatorname{Tor}(A,B)=0$ for all $B$.

::: pf-proof
The first assertion is step [](#first){.pf-ref}; the two implications of the equivalence are steps [](#torsionfree){.pf-ref} and [](#converse){.pf-ref}.
:::

:::

:::

:::

