---
schema: qual/card@1
id: E-HAT-4.2-12
kind: problem
title: "Whitehead theorem via universal covers"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.2 Exercise 12, printed p. 390,
    Proposition 4.1 (printed p. 348) and Corollary 4.33 (printed p. 368), and against the
    published solution in Steven V. Sam's Solutions to Hatcher's Algebraic Topology (2008),
    §4.2 Exercise 12, PDF p. 22. The card's steps are correct and are Sam's argument: the
    lift exists because X~ is simply connected, the hypothesis makes f~ a homology
    isomorphism, Whitehead makes f~ a homotopy equivalence, and Proposition 4.1 carries
    the resulting isomorphisms on pi_i down to f_* for i > 1; with pi_1 by hypothesis and
    pi_0 by connectivity, f is a weak equivalence of CW complexes. The card had called the
    argument its own although the set covers the exercise; the citation is now there.
    Statement unchanged.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 12; the stored statement matches.
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
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 12 (AT.txt 19390-19395) and correct as it stands. The lift
    is a homology isomorphism between simply connected CW complexes, so it is a homotopy equivalence by the
    homology Whitehead theorem; being a homotopy equivalence it induces isomorphisms on pi_i for i>=2;
    covering maps are isomorphisms on pi_i for i>=2, so the rectangle identifies f_* on pi_i for i>=2; with
    pi_1 an isomorphism by hypothesis and pi_0 as both are connected, f is a weak homotopy equivalence and
    hence, between CW complexes, a homotopy equivalence. Not checked: the local-coefficient restatement
    offered in the bracket, which the card does not use.

---

::: {.problem}
Show that a map $f: X \to Y$ of connected CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_1$ and if a lift $\tilde{f}: \tilde{X} \to \tilde{Y}$ to the universal covers induces an isomorphism on homology. [The latter condition can be restated in terms of homology with local coefficients as saying that $f_*: H_*(X; \ZZ[\pi_1 X]) \to H_*(Y; \ZZ[\pi_1 Y])$ is an isomorphism; see §3.H.]
:::

::: {.solution}

The proof below is the published one, transcribed and checked against the book: **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), §4.2 Exercise 12**. Sam's argument is exactly the three moves needed — the lift to universal covers is a homotopy equivalence by the homology form of Whitehead's theorem (Corollary 4.33), so $\tilde f_*$ is an isomorphism on every homotopy group, and Proposition 4.1 carries that down through the covering maps to $f_*$ for $i>1$. The card's steps are that argument written out.

Let $f:X\to Y$ be a map of connected CW complexes inducing an isomorphism on $\pi_{1}$, and let $\widetilde f:\widetilde X\to\widetilde Y$ be a lift of $f$ to the universal covers (its existence is part of the data).

::: pf

::: {.pf-step #covers}
$\widetilde X$ and $\widetilde Y$ are simply connected CW complexes, and $\widetilde f$ induces an isomorphism on integral homology in every degree.

::: pf-proof
The universal cover of a connected CW complex is a CW complex, and it is simply connected by construction. A lift of $f$ exists because the composite $\widetilde X\to X\xrightarrow{f}Y$ induces the trivial map on $\pi_{1}$ — the source $\widetilde X$ is simply connected — so the lifting criterion for the covering $\widetilde Y\to Y$ applies. The homology hypothesis on $\widetilde f$ is the one assumed in the problem.
:::

:::

::: {.pf-step #equivalence}
$\widetilde f$ is a homotopy equivalence.

::: pf-proof
$\widetilde X$ and $\widetilde Y$ are simply connected CW complexes and $\widetilde f$ is an isomorphism on integral homology in each degree, so the homology form of Whitehead's theorem makes $\widetilde f$ a weak homotopy equivalence, and a weak equivalence between CW complexes is a homotopy equivalence.
:::

:::

::: {.pf-step #higher}
$f_{*}:\pi_{i}(X)\to\pi_{i}(Y)$ is an isomorphism for every $i\ge2$.

::: pf-proof
The covering maps $p_{X}:\widetilde X\to X$ and $p_{Y}:\widetilde Y\to Y$ induce isomorphisms on $\pi_{i}$ for $i\ge2$, since a covering map is a fibration with discrete fibre and $\pi_{i}$ of a discrete space vanishes for $i\ge1$. The square $p_{Y}\widetilde f=f p_{X}$ commutes, so $f_{*}$ is the composite of two isomorphisms and hence an isomorphism.
:::

:::

::: {.pf-step #conclusion}
$f$ is a homotopy equivalence.

::: pf-proof
$f_{*}$ is an isomorphism on $\pi_{1}$ by hypothesis, on $\pi_{i}$ for $i\ge2$ by step [](#higher){.pf-ref}, and on $\pi_{0}$ because both spaces are connected, so $f$ is a weak homotopy equivalence. Whitehead's theorem then makes $f$ a homotopy equivalence, since $X$ and $Y$ are CW complexes. Hence
$$
\boxed{f\text{ is a homotopy equivalence}.}
$$
The restatement in the problem, that the hypothesis on $\widetilde f$ says $f_{*}:H_{*}(X;\ZZ[\pi_{1}X])\to H_{*}(Y;\ZZ[\pi_{1}Y])$ is an isomorphism in homology with local coefficients, is the version of the same condition in §3.H.
:::

:::

:::
:::
