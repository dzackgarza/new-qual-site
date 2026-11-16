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
---

::: {.problem}
Show that $\operatorname{Tor}(A, \QQ/\ZZ)$ is isomorphic to the torsion subgroup of $A$.
Deduce that $A$ is torsionfree iff $\operatorname{Tor}(A, B) = 0$ for all $B$.
:::

::: {.solution}
Write $\operatorname{Tor}=\operatorname{Tor}_1^{\ZZ}$; Hatcher notes on printed p. 263, immediately after Lemma 3A.2, that $\operatorname{Tor}_n^{\ZZ}(H,G)=0$ for $n>1$ because a free resolution $0\to F_1\to F_0\to H\to0$ always exists, and that $\operatorname{Tor}_1$ is written $\operatorname{Tor}$. So the two groups below are $\operatorname{Tor}_1^{\ZZ}(A,\QQ/\ZZ)$ and $\operatorname{Tor}_1^{\ZZ}(A,B)$. The proof is Weibel, *An Introduction to Homological Algebra* (Cambridge Studies in Advanced Mathematics 38, 1994), §3.1, printed pp. 66--67, in the book's own steps; the §3.1 text is read in `tmp/sources/weibel-03-tor-and-ext.md` and the §2.6--2.7 colimit corollaries in `tmp/sources/weibel-02-derived-functors.md`.

*Cyclic groups.* (Calculation 3.1.1, printed p. 66.) The free resolution $0\to\ZZ\xrightarrow{n}\ZZ\to\ZZ/n\to0$ computes $\operatorname{Tor}_*^{\ZZ}(\ZZ/n,B)$ as the homology of the complex $0\to B\xrightarrow{n}B\to0$, so
$$
\operatorname{Tor}_0^{\ZZ}(\ZZ/n,B)=B/nB,\qquad
\operatorname{Tor}_1^{\ZZ}(\ZZ/n,B)=B[n]:=\{b\in B: nb=0\},\qquad
\operatorname{Tor}_i^{\ZZ}(\ZZ/n,B)=0\ \ (i\ge2).
$$

*The torsion subgroup in the second variable.* (Proposition 3.1.3, printed p. 67.) $\QQ/\ZZ$ is the direct limit of its finite subgroups, each isomorphic to some $\ZZ/n$, and $\operatorname{Tor}$ commutes with direct limits, so
$$
\operatorname{Tor}_1^{\ZZ}(\QQ/\ZZ,B)\cong\varinjlim_n\operatorname{Tor}_1^{\ZZ}(\ZZ/n,B)\cong\varinjlim_n B[n]=\bigcup_n B[n],
$$
which is the torsion subgroup $T(B)$ of $B$. The union is over all $n\ge1$ and not over the primes only: $B[n]$ is the set of elements whose order divides $n$, so every element of finite order lies in some $B[n]$, whereas over the primes alone the union would be only the elements of prime order. The index set is the finite cyclic subgroups of $\QQ/\ZZ$ ordered by divisibility, which is directed.

The colimit corollary Weibel invokes is printed as Corollary 2.6.17, p. 58, in the second variable, $\operatorname{Tor}_*^R(A,\varinjlim B_\alpha)\cong\varinjlim\operatorname{Tor}_*^R(A,B_\alpha)$. The form used here has the colimit in the first variable, which is Corollary 2.6.16 on the same page applied to the left adjoint $-\otimes_\ZZ B$ over $\ZZ$-mod, an abelian category with enough projectives in which filtered colimits are exact (Theorem 2.6.15, p. 57), and whose left derived functors are $\operatorname{Tor}_*^{\ZZ}(-,B)$ (Theorem 2.7.2, the balancing of the two derived functors of the tensor product, p. 58). Weibel cites 2.6.17 for that same first-variable statement in the proof of Proposition 3.1.2, p. 66.

*The first sentence of the exercise.* (Remark (Balancing Tor), printed p. 67.) For a commutative ring $R$, $\operatorname{Tor}_1^R(A,B)\cong\operatorname{Tor}_1^R(B,A)$, because for fixed $B$ both are universal $\delta$-functors over $F(A)=A\otimes_RB=B\otimes_RA$. For $R=\ZZ$ this gives
$$
\operatorname{Tor}_1^{\ZZ}(A,\QQ/\ZZ)\cong\operatorname{Tor}_1^{\ZZ}(\QQ/\ZZ,A)\cong T(A),
$$
the second isomorphism being the Proposition above with $B$ replaced by $A$. The book draws the same conclusion in one sentence in the Remark. This is the exercise's first sentence: $\operatorname{Tor}(A,\QQ/\ZZ)\cong T(A)$. Balancing is the step that matters for it, since the Proposition computes $\operatorname{Tor}$ with $\QQ/\ZZ$ in the first slot and the exercise asks for it in the second.

*The second sentence of the exercise.* (Proposition 3.1.4 and Corollary 3.1.5, printed p. 67.) If $A$ is torsionfree then $A$ is the direct limit of its finitely generated subgroups, each isomorphic to some $\ZZ^m$, so by the same colimit formula
$$
\operatorname{Tor}_n^{\ZZ}(A,B)\cong\varinjlim_m\operatorname{Tor}_n^{\ZZ}(\ZZ^m,B)=0\qquad(n\neq0,\ \text{all } B),
$$
because $\ZZ^m$ is free and hence projective. The book then prints, for every abelian group $A$,
$$
\operatorname{Tor}_1^{\ZZ}(A,-)=0\iff A\text{ is torsionfree}\iff\operatorname{Tor}_1^{\ZZ}(-,A)=0
$$
as Corollary 3.1.5, without a separate proof, and obtains it from Proposition 3.1.4 and the Remark. The two implications the exercise asks for are these: if $A$ is torsionfree then $\operatorname{Tor}(A,B)=0$ for every $B$, which is Proposition 3.1.4 in degree $1$; and if $\operatorname{Tor}(A,B)=0$ for every $B$ then taking $B=\QQ/\ZZ$ gives $T(A)\cong\operatorname{Tor}(A,\QQ/\ZZ)=0$, so $A$ is torsionfree.

Checked against Hatcher, *Algebraic Topology* (2002), §3.A Exercise 2, printed p. 267, read in `tmp/sources/hatcher-2002-algebraic-topology.md`: "Show that $\operatorname{Tor}(A,\QQ/\ZZ)$ is isomorphic to the torsion subgroup of $A$. Deduce that $A$ is torsionfree iff $\operatorname{Tor}(A,B)=0$ for all $B$." Hatcher's $\operatorname{Tor}$ is $\operatorname{Tor}_1^{\ZZ}$ (printed p. 263, where $\operatorname{Tor}_n=0$ for $n>1$ is noted), and the symmetry that the Remark supplies is his Proposition 3A.5(1), printed p. 265.
:::
