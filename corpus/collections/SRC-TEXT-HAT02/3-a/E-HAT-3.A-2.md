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
---

::: {.problem}
Show that $\operatorname{Tor}(A, \QQ/\ZZ)$ is isomorphic to the torsion subgroup of $A$.
Deduce that $A$ is torsionfree iff $\operatorname{Tor}(A, B) = 0$ for all $B$.
:::

::: {.solution}
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
