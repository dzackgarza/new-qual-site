---
schema: qual/card@1
id: E-HAT-4.2-9
kind: problem
title: "Contractible mapping cone implies homotopy equivalence"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 9 (AT.txt 19358-19361) and correct as it stands. The
    simply connected half is right: a contractible mapping cone makes the cofibration sequence give an
    isomorphism on reduced homology, and the homology Whitehead theorem for simply connected complexes
    finishes. The counterexample is also right, and I checked the point that could go wrong: for the
    constant map A -> pt the mapping cone is the suspension of A, since the mapping cone of A -> pt is CA
    with A x {0} collapsed to the basepoint, which is (A x I)/(A x {0}, A x {1}) = Sigma A -- and that is
    contractible only when A is acyclic, which is why the preceding exercise is needed rather than
    redundant. Acyclic noncontractible complexes exist (for instance an acyclic K(G,1)). Not checked:
    nothing outside this exercise.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, outside the sections already closed. Read against Hatcher, Exercise 9
    of §4.2, printed p. 389. Checked: the cofibration sequence $X\to Y\to C_f$ with $\widetilde H_*(C_f)=0$
    makes $f_*$ an isomorphism on reduced homology, and the homology Whitehead theorem for simply
    connected CW complexes turns that into a homotopy equivalence; and the counterexample: for the
    constant map $A\to*$ with $A$ acyclic and noncontractible the mapping cone is $CA/A\cong\Sigma A$,
    contractible by Exercise 8, while $f$ is not a homotopy equivalence. The example complex cited
    (Hatcher Example 2.38, printed p. 142) has the stated presentation. No defect; the printed page is
    added.
---

::: {.problem}
Show that a map between simply-connected CW complexes is a homotopy equivalence if its mapping cone is contractible.
Use the preceding exercise to give an example where this fails in the nonsimply-connected case.
:::

::: {.solution}
The exercise is §4.2 Exercise 9, printed p. 389.

Let $f:X\to Y$ be a map of simply-connected CW complexes and suppose its mapping cone $C_f$ is contractible. The cofibration sequence
$$
X\xrightarrow f Y\longrightarrow C_f
$$
gives the long exact sequence in reduced homology. Since $\widetilde H_*(C_f)=0$, the map
$$
f_*:H_i(X;\ZZ)\xrightarrow{\cong}H_i(Y;\ZZ)
$$
is an isomorphism for every $i$. The homology Whitehead theorem for simply-connected CW complexes then implies that $f$ is a homotopy equivalence.

The simply-connected hypothesis is essential. Let $A$ be any acyclic, noncontractible CW complex (for example the 2-dimensional complex of Hatcher, Example 2.38, printed p.142, obtained from $S^1\vee S^1$ by attaching two cells by the words $a^5b^{-3}$ and $b^3(ab)^{-2}$, whose $d_2$ has determinant $-1$ (absolute value $1$) so that $\widetilde H_*(A)=0$ while $\pi_1(A)$ is the nontrivial group $\langle a,b\mid a^5=b^3=(ab)^2\rangle$), and take the constant map
$$
f:A\longrightarrow *.
$$
Its mapping cone is
$$
C_f=CA/A\cong\Sigma A.
$$
By the preceding exercise the suspension of an acyclic CW complex is contractible. Thus $C_f$ is contractible, while $f$ is not a homotopy equivalence because $A$ is not contractible. This gives the required nonsimply-connected counterexample.
:::
