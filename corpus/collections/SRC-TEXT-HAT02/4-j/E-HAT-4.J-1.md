---
schema: qual/card@1
id: E-HAT-4.J-1
kind: problem
title: "Reduction of $\\Omega\\Sigma X$ to the connected case"
classification:
  areas:
  - topology
  topics:
  - Homotopy Theory
  - Loop Spaces
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.J Exercise 1, printed p. 475.
    The proof of the printed claim is correct, but the card wrapped it in a qualification
    and a counterexample that are both false. It said the claim fails when a component is
    a point, instancing X = S^1 u {pt} with Sigma X = S^2 v S^1 against
    Sigma(wedge of components) = S^2: that is wrong, because the suspension of a point is
    a point (reduced) or an interval (unreduced), and an interval is contractible, so the
    singleton component contributes nothing on either side and Sigma X = S^2 in both
    readings. Removed: the counterexample step, the "no component is a point" hypothesis
    in the collapse step, and the opening claim that a qualification is needed. Also
    corrected: the step proving Omega Sigma X path-connected justified it by
    reparametrising loops, which gives the group structure and not connectivity; it now
    argues that Sigma X is simply connected, as a wedge of suspensions of path-connected
    CW complexes, so pi_0(Omega Sigma X) = pi_1(Sigma X) = 0. The earlier audit note that
    says the restructure preserved "its qualification" is left as it stands, being the
    record of that day. Statement unchanged.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read on the printed page: Hatcher, Algebraic Topology, Section 4.J, Exercise 1,
    book page 475, read from a 300 dpi render of PDF page 484 (the printed page is
    not marked in the text extraction, whose two layers garble the statement).
    The statement is stored verbatim.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    Proved from the book: the reduced suspension is the smash product with $S^1$
    (Example 0.10, p. 13), and collapsing an interval in a suspension is a homotopy
    equivalence by Proposition 0.17 (p. 15). The one case in which the printed claim
    fails is recorded in the solution: a non-base component consisting of a single
    point leaves an extra $S^1$ summand, and the counterexample is worked out there.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the existing solution into Lamport steps without changing its conclusion, including its qualification: the printed claim holds for every nonconnected CW complex with no single-point component, and $S^1\sqcup\{\mathrm{pt}\}$ is a counterexample in general. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.J Exercise 1, printed p. 475. No retained solution set covers this exercise; the argument is the card's own. Checked: the componentwise computation of $\Sigma X$ as a wedge of the suspension of the based component and the unreduced suspensions of the others; the collapse $S(X_\alpha)\to\Sigma X_\alpha$ as a homotopy equivalence by Proposition 0.17; the distribution of $\Sigma$ over the wedge; and the resulting single path-component.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The card carried its closing step twice, byte for byte, under the same label `conclusion`,
    which the whole-corpus Lamport filter refuses as a duplicate step label. One copy is removed;
    nothing else changes, and the remaining step is the one the card already had.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 484 carries the running head 475, so
    the printed page is the one the card's earlier event claimed. The durable part of the locator is
    that printed page; the file path names this machine's copy and `tmp/sources` does not survive a VM
    reset. No mathematics changed.
---

::: {.problem}
This is Exercise 1 of Section 4.J of Hatcher, *Algebraic Topology* (2002), printed p. 475, read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf` (printed page = PDF page - 9); the statement below is its wording.

Show that $\Omega\Sigma X$ for a nonconnected CW complex $X$ reduces to the connected case by showing that each path-component of $\Omega\Sigma X$ is homotopy equivalent to $\Omega\Sigma(\bigvee_\alpha X_\alpha)$ where the $X_\alpha$'s are the components of $X$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.J Exercise 1, printed p. 475. The printed claim needs no qualification, and the argument below proves it as it stands: the suspension of one point is a point — or, in the unreduced convention, an interval, which is contractible — so a component that is a single point contributes nothing to either side.

::: pf

::: {.pf-step #pieces}
With $*_\alpha\in X_\alpha$ a $0$-cell in each component, $\Sigma X=\Sigma X_{\alpha_0}\vee\bigvee_{\alpha\neq\alpha_0}S(X_\alpha)$, where $S$ denotes the unreduced suspension.

::: pf-proof
The reduced suspension is the smash product $X\wedge S^1$, computed componentwise: the piece of $X_\alpha$ is $X_\alpha\times S^1$ with $X_\alpha\times\{s_0\}$ collapsed and, only for $\alpha=\alpha_0$, also $\{x_0\}\times S^1$. Hence the base component contributes $\Sigma X_{\alpha_0}$ and every other component is left with the one collapse, which is the unreduced suspension. All pieces meet in the single basepoint, so the quotient is their wedge.
:::
:::

::: {.pf-step #collapse}
$S(X_\alpha)\simeq\Sigma X_\alpha$ for every $\alpha\neq\alpha_0$, whether or not the component is a point.

::: pf-proof
For each such $\alpha$ the pair $(S(X_\alpha),\{*_\alpha\}\times I)$ has contractible second term and is a CW pair, so collapsing that interval, which carries $S(X_\alpha)$ to the reduced suspension $\Sigma X_\alpha$, is a homotopy equivalence by Proposition 0.17 (p. 15).
:::
:::

::: {.pf-step #wedge}
$\Sigma X\simeq\bigvee_\alpha\Sigma X_\alpha=\Sigma\big(\bigvee_\alpha X_\alpha\big)$.

::: pf-proof
Apply step [](#collapse){.pf-ref} to each summand of step [](#pieces){.pf-ref}; a wedge of homotopy equivalences is a homotopy equivalence. The reduced suspension of a wedge of based spaces is the wedge of the suspensions, giving the second identity.
:::
:::

::: {.pf-step #loops}
$\Omega\Sigma X\simeq\Omega\Sigma(\bigvee_\alpha X_\alpha)$, which is path-connected; and $\bigvee_\alpha X_\alpha$ is path-connected.

::: pf-proof
$\Omega$ carries the homotopy equivalence of step [](#wedge){.pf-ref} to one of loop spaces. $\Omega\Sigma X$ is path-connected because $\Sigma X$ is simply connected: $\Sigma X_\alpha$ is a suspension of a path-connected CW complex, hence simply connected by van Kampen, and a wedge of simply connected CW complexes is simply connected, so $\pi_0(\Omega\Sigma X)=\pi_1(\Sigma X)=0$. The wedge is path-connected because its components are path-connected and share the basepoint.
:::
:::

::: {.pf-step #conclusion}
Each path-component of $\Omega\Sigma X$ is homotopy equivalent to $\Omega\Sigma(\bigvee_\alpha X_\alpha)$.

::: pf-proof
By step [](#loops){.pf-ref} $\Omega\Sigma X$ has a single path-component, namely itself, and it is homotopy equivalent to $\Omega\Sigma(\bigvee_\alpha X_\alpha)$, which is a connected CW complex, so Theorem 4J.1 (p. 471) applies to it and its conclusion transfers to $\Omega\Sigma X$.
:::
:::

:::
:::
