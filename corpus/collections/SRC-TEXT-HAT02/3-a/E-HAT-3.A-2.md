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
---

::: {.problem}
Show that $\operatorname{Tor}(A, \QQ/\ZZ)$ is isomorphic to the torsion subgroup of $A$.
Deduce that $A$ is torsionfree iff $\operatorname{Tor}(A, B) = 0$ for all $B$.
:::

::: {.solution}
This is the statement of Weibel, *An Introduction to Homological Algebra* (Cambridge Studies in Advanced Mathematics 38, 1994), §3.1, Proposition 3.1.3 and the Remark following Proposition 3.1.4, printed p. 67, where $\operatorname{Tor}_1^\ZZ(\QQ/\ZZ,B)$ is identified with the torsion subgroup of $B$ and balancing of $\operatorname{Tor}$ gives $\operatorname{Tor}_1^\ZZ(A,\QQ/\ZZ)$ as the torsion subgroup of $A$; Corollary 3.1.5 on the same page is the deduction. Weibel's proof is the colimit one: $\QQ/\ZZ$ is the direct limit of its finite subgroups $\ZZ/n$, the groups $\operatorname{Tor}(\ZZ/n,B)\cong B[n]$ are computed from the resolution $0\to\ZZ\xrightarrow{n}\ZZ\to\ZZ/n\to0$ (Calculation 3.1.1, p. 66), and $\operatorname{Tor}$ carries that direct limit to $\varinjlim_n B[n]$, which is the torsion subgroup of $B$ (Corollary 2.6.17, p. 58). The argument below is the exact-sequence route to the same two statements, using the book's own Proposition 3A.5 in place of the colimit formula.

Apply the six-term exact sequence of Proposition 3A.5(6) (p. 265) to the short exact sequence
$$
0\longrightarrow\ZZ\longrightarrow\QQ
\longrightarrow\QQ/\ZZ\longrightarrow0 .
$$
Both end terms of the resulting sequence's left end vanish, since $\operatorname{Tor}(A,\ZZ)=0$ because $\ZZ$ is free and $\operatorname{Tor}(A,\QQ)=0$ because $\QQ$ is torsionfree, by Proposition 3A.5(3) (p. 265). The sequence therefore begins
$$
0\longrightarrow \operatorname{Tor}(A,\QQ/\ZZ)
\longrightarrow A\otimes\ZZ
\longrightarrow A\otimes\QQ .
$$
Under the identification $A\otimes\ZZ\cong A$ the second map is $a\mapsto a\otimes1$. Identify $A\otimes\QQ$ with the localisation $S^{-1}A$ of $A$ at the multiplicative set $S=\ZZ\setminus\{0\}$, by $a\otimes(r/s)\mapsto ra/s$, with inverse $a/s\mapsto a\otimes(1/s)$; under this identification $a\otimes1$ becomes $a/1$. In a localisation $a/1=0$ if and only if $sa=0$ for some $s\in S$, by the defining equivalence of fractions. Hence
$$
\ker\bigl(A\to A\otimes\QQ\bigr)=\{a\in A: sa=0 \text{ for some } s\neq0\}=T(A),
$$
the torsion subgroup, and exactness gives
$$
\boxed{\operatorname{Tor}(A,\QQ/\ZZ)\cong T(A)}.
$$

For the deduction, if $\operatorname{Tor}(A,B)=0$ for every abelian group $B$ then in particular $\operatorname{Tor}(A,\QQ/\ZZ)=0$, so $T(A)=0$ and $A$ is torsionfree. Conversely, if $A$ is torsionfree then $\operatorname{Tor}(A,B)=0$ for every $B$ by Proposition 3A.5(3) (p. 265); Exercise 5 re-derives this same vanishing from Exercise 4 and the free case. So $A$ is torsionfree if and only if $\operatorname{Tor}(A,B)=0$ for all $B$.
:::
