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
---

::: {.problem}
Show that $\operatorname{Tor}(A, \QQ/\ZZ)$ is isomorphic to the torsion subgroup of $A$.
Deduce that $A$ is torsionfree if $\operatorname{Tor}(A, B) = 0$ for all $B$.
:::

::: {.solution}
Use the short exact sequence
\[
0\longrightarrow\ZZ\longrightarrow\QQ
\longrightarrow\QQ/\ZZ\longrightarrow0.
\]
Since $\QQ$ is flat over $\ZZ$, tensoring with an abelian group $A$ yields the exact segment
\[
0\longrightarrow \operatorname{Tor}(A,\QQ/\ZZ)
\longrightarrow A\otimes\ZZ
\longrightarrow A\otimes\QQ.
\]
Identifying $A\otimes\ZZ$ with $A$, the last map is the canonical localization map
\[
A\longrightarrow A\otimes\QQ.
\]
Its kernel consists exactly of the torsion elements of $A$: if $na=0$ then $a\otimes1=(na)\otimes(1/n)=0$, while if $a\otimes1=0$ in the localization then some nonzero integer kills $a$. Therefore
\[
\boxed{\operatorname{Tor}(A,\QQ/\ZZ)\cong T(A)}.
\]

Consequently, if $\operatorname{Tor}(A,B)=0$ for every abelian group $B$, then in particular
\[
\operatorname{Tor}(A,\QQ/\ZZ)=0,
\]
so $T(A)=0$ and $A$ is torsionfree.
:::
