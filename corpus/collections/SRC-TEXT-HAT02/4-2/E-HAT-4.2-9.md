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

---

::: {.problem}
Show that a map between simply-connected CW complexes is a homotopy equivalence if its mapping cone is contractible.
Use the preceding exercise to give an example where this fails in the nonsimply-connected case.
:::

::: {.solution}
Let $f:X\to Y$ be a map of simply-connected CW complexes and suppose its mapping cone $C_f$ is contractible. The cofibration sequence
$$
X\xrightarrow f Y\longrightarrow C_f
$$
gives the long exact sequence in reduced homology. Since $\widetilde H_*(C_f)=0$, the map
$$
f_*:H_i(X;\ZZ)\xrightarrow{\cong}H_i(Y;\ZZ)
$$
is an isomorphism for every $i$. The homology Whitehead theorem for simply-connected CW complexes then implies that $f$ is a homotopy equivalence.

The simply-connected hypothesis is essential. Let $A$ be any acyclic, noncontractible CW complex (for example an acyclic $K(G,1)$ for a nontrivial acyclic group $G$), and take the constant map
$$
f:A\longrightarrow *.
$$
Its mapping cone is
$$
C_f=CA/A\cong\Sigma A.
$$
By the preceding exercise the suspension of an acyclic CW complex is contractible. Thus $C_f$ is contractible, while $f$ is not a homotopy equivalence because $A$ is not contractible. This gives the required nonsimply-connected counterexample.
:::
