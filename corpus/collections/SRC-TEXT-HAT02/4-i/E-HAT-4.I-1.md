---
schema: qual/card@1
id: E-HAT-4.I-1
kind: problem
title: "Suspension of a retract splits as a wedge"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.I, Exercise 1 and Proposition 4I.3; the stored statement matches the corrected current source.
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
---

::: {.problem}
If a connected CW complex $X$ retracts onto a subcomplex $A$, show that $\Sigma X \simeq \Sigma A \lor \Sigma(X/A)$.
[One approach: Show the map $\Sigma r + \Sigma q: \Sigma X \to \Sigma A \lor \Sigma(X/A)$ induces an isomorphism on homology, where $r: X \to A$ is the retraction and $q: X \to X/A$ is the quotient map.]
:::

::: {.solution}
Let
$$
r:X\to A
$$
be a retraction and
$$
q:X\to X/A
$$
the quotient map. Let $j_A$ and $j_Q$ be the two wedge inclusions. Suspending and using the pinch map of $\Sigma X$ to add maps into the same target gives
$$
F=(j_A\circ\Sigma r)+(j_Q\circ\Sigma q):\Sigma X\longrightarrow
\Sigma A\vee\Sigma(X/A).
$$
We show that $F$ is a homology isomorphism.

Since $r\circ i=\operatorname{id}_A$, the inclusion
$$
i_*:\widetilde H_*(A)\to\widetilde H_*(X)
$$
is split injective, with splitting $r_*$. The long exact sequence of the pair $(X,A)$ (Theorem 2.16, p. 117) therefore breaks into split short exact sequences
$$
0\longrightarrow\widetilde H_j(A)
\stackrel{i_*}{\longrightarrow}
\widetilde H_j(X)
\stackrel{q_*}{\longrightarrow}
\widetilde H_j(X/A)\longrightarrow0.
$$
Hence
$$
(r_*,q_*):\widetilde H_j(X)\xrightarrow{\cong}
\widetilde H_j(A)\oplus\widetilde H_j(X/A).
\tag{1}
$$
Under the suspension isomorphisms, $F_*$ is exactly the map (1). Thus $F$ induces an isomorphism on all reduced homology groups.

Both $\Sigma X$ and
$$
\Sigma A\vee\Sigma(X/A)
$$
are simply connected CW complexes because $X$ is connected. The homology version of Whitehead's theorem (Corollary 4.33, p. 367) therefore gives
$$
\boxed{\Sigma X\simeq\Sigma A\vee\Sigma(X/A).}
$$
:::
