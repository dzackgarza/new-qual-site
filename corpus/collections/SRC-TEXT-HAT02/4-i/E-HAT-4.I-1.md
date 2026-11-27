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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.I Exercise 1, printed p. 462, including the bracketed hint, which is the route the card takes. No retained solution set covers this exercise; the argument is the card's own. Checked: that the retraction splits the inclusion on homology; that the long exact sequence of $(X,A)$ therefore breaks into split short exact sequences, so $(r_*,q_*)$ is an isomorphism; that suspending identifies $F_*$ with that isomorphism; and that both sides are simply connected so Whitehead applies.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 471 carries the running head 462, so
    the printed page is the one the card's earlier event claimed. The durable part of the locator is
    that printed page; the file path names this machine's copy and `tmp/sources` does not survive a VM
    reset. No mathematics changed.
- event: source-corrected
  by: chatgpt
  date: 2026-11-27
  note: >-
    The author's PDF confirms the statement and hint as §4.I Exercise 1.
    The page and local-copy locators in the November 18 and 19 events
    are superseded by that numbered citation (issue #186). The mathematical
    statement and proof are unchanged.
---

::: {.problem}
[@Hat02, §4.I, Exercise 1]

If a connected CW complex $X$ retracts onto a subcomplex $A$, show that $\Sigma X \simeq \Sigma A \lor \Sigma(X/A)$.
[One approach: Show the map $\Sigma r + \Sigma q: \Sigma X \to \Sigma A \lor \Sigma(X/A)$ induces an isomorphism on homology, where $r: X \to A$ is the retraction and $q: X \to X/A$ is the quotient map.]
:::

::: {.solution}
We use the map suggested in the exercise's hint.

::: pf

::: {.pf-step #split}
$i_*:\widetilde H_j(A)\to\widetilde H_j(X)$ is split injective, with splitting $r_*$.

::: pf-proof
$r\circ i=\mathrm{id}_A$ because $r$ is a retraction, so $r_*\circ i_*=\mathrm{id}$ on reduced homology; a map with a left inverse is injective and the identity $r_*\circ i_*=\mathrm{id}$ exhibits the splitting.
:::
:::

::: {.pf-step #les}
For each $j$ there is a split short exact sequence $0\to\widetilde H_j(A)\xrightarrow{i_*}\widetilde H_j(X)\xrightarrow{q_*}\widetilde H_j(X/A)\to0$.

::: pf-proof
In the long exact sequence of the pair $(X,A)$ [@Hat02, Theorem 2.16] the connecting map vanishes because $i_*$ is injective, so the sequence breaks into short exact sequences; each is split by step [](#split){.pf-ref}, using that a retraction makes the connecting map zero.
:::
:::

::: {.pf-step #iso}
$(r_*,q_*):\widetilde H_j(X)\to\widetilde H_j(A)\oplus\widetilde H_j(X/A)$ is an isomorphism for every $j$.

::: pf-proof
A split short exact sequence presents the middle group as the direct sum of the outer two, via the map whose components are the splitting and the surjection; here those components are $r_*$ and $q_*$.
:::
:::

::: {.pf-step #F}
For $F=(j_A\circ\Sigma r)+(j_Q\circ\Sigma q):\Sigma X\to\Sigma A\vee\Sigma(X/A)$, the induced map $F_*$ is the isomorphism of step [](#iso){.pf-ref} under the suspension isomorphisms, hence $F$ is a homology isomorphism.

::: pf-proof
Suspension is natural, so $(\Sigma r)_*$ and $(\Sigma q)_*$ correspond under the suspension isomorphisms to $r_*$ and $q_*$; the wedge inclusions $j_A,j_Q$ induce the inclusions of the two summands into the direct sum of reduced homology of the wedge. Adding the two maps uses the pinch map of $\Sigma X$, so $F_*$ is precisely the map with components $r_*$ and $q_*$.
:::
:::

::: {.pf-step #whitehead}
$\Sigma X\simeq\Sigma A\vee\Sigma(X/A)$.

::: pf-proof
$X$ is connected, so $\Sigma X$ and $\Sigma A\vee\Sigma(X/A)$ are simply connected CW complexes; a map between simply connected CW complexes inducing an isomorphism on all homology groups is a homotopy equivalence [@Hat02, Corollary 4.33], which step [](#F){.pf-ref} supplies.
:::
:::

:::
:::
