---
schema: qual/card@1
id: E-HAT-3.A-5
kind: problem
title: "Tor vanishes for torsionfree modules"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.A, Exercise 5; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.A Exercise 5, printed p. 267. The statement
    matches the print, including its instruction to use "the previous problem" — Exercise 4, which
    is cited. The proof's one unstated step, that a finitely generated torsionfree abelian group is
    free, is now given; the vanishing of Tor on free first arguments is Proposition 3A.5(3)
    (p. 265). The card also records that the conclusion is the torsionfree half of that same
    proposition, which Hatcher proves on pp. 265-266 by the finitely-generated-subgroup argument in
    the second variable rather than by Exercise 4. No published solution of this exercise is in the
    retained sets; recorded in COMPLAINTS.md.
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    The card now states that Hatcher's printed proof of Proposition 3A.5(3) (pp. 265--266) is itself
    a complete published proof of this exercise's conclusion, by the finitely generated subgroup of
    the second variable; the direct-limit argument the exercise asks for is kept and reaches the same
    statement. Re-read the printed proof: an element of $\ker(\varphi\otimes\mathrm{id})$ involves
    finitely many elements of $B$, they lie in a finitely generated torsionfree hence free subgroup
    $B_0$, and $\operatorname{Tor}(A,B_0)=0$ by the free case.
---

::: {.problem}
From the fact that $\operatorname{Tor}(A, B) = 0$ if $A$ is free, deduce that $\operatorname{Tor}(A, B) = 0$ if $A$ is torsionfree by applying the previous problem to the directed system of finitely generated subgroups $A_\alpha$ of $A$.
:::

::: {.solution}
Write the torsionfree abelian group $A$ as the directed union of its finitely generated subgroups:
$$
A=\varinjlim_\alpha A_\alpha,
$$
the index set being the finitely generated subgroups with inclusions, which is directed because two finitely generated subgroups lie in their sum.

Each $A_\alpha$ is finitely generated and torsionfree, hence free abelian: a finitely generated abelian group is a direct sum of copies of $\ZZ$ and of finite cyclic groups, and finite summands would be torsion. Therefore
$$
\operatorname{Tor}(A_\alpha,B)=0
$$
for every $\alpha$, by the hypothesis that Tor vanishes on free first arguments (Proposition 3A.5(3), p. 265).

By Exercise 4, $\operatorname{Tor}$ commutes with direct limits in the first variable, so
$$
\operatorname{Tor}(A,B)
\cong \varinjlim_\alpha\operatorname{Tor}(A_\alpha,B)
=0.
$$
The conclusion is exactly the torsionfree case of Proposition 3A.5(3), and Hatcher prints a complete proof of it on pp. 265--266: for a free resolution $0\to F_1\xrightarrow{\varphi}F_0\to A\to0$ and a torsionfree $B$, an element of $\ker(\varphi\otimes\id)$ involves only finitely many elements of $B$, which lie in a finitely generated torsionfree hence free subgroup $B_0$, and $\operatorname{Tor}(A,B_0)=0$ by the free case, so $\varphi\otimes\id$ is injective. That printed argument is a complete published proof of this exercise's conclusion; the direct-limit route above is the one the exercise asks for, and it reaches the same statement.
:::
