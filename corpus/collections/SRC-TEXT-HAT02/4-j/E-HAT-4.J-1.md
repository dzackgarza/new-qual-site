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
---

::: {.problem}
Show that $\Omega\Sigma X$ for a nonconnected CW complex $X$ reduces to the connected case by showing that each path-component of $\Omega\Sigma X$ is homotopy equivalent to $\Omega\Sigma(\bigvee_\alpha X_\alpha)$ where the $X_\alpha$'s are the components of $X$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.J Exercise 1, printed p. 475. The card proves the printed claim under the stated qualification and records the counterexample to it in general.

::: pf

::: {.pf-step #pieces}
With $*_\alpha\in X_\alpha$ a $0$-cell in each component, $\Sigma X=\Sigma X_{\alpha_0}\vee\bigvee_{\alpha\neq\alpha_0}S(X_\alpha)$, where $S$ denotes the unreduced suspension.

::: pf-proof
The reduced suspension is the smash product $X\wedge S^1$, computed componentwise: the piece of $X_\alpha$ is $X_\alpha\times S^1$ with $X_\alpha\times\{s_0\}$ collapsed and, only for $\alpha=\alpha_0$, also $\{x_0\}\times S^1$. Hence the base component contributes $\Sigma X_{\alpha_0}$ and every other component is left with the one collapse, which is the unreduced suspension. All pieces meet in the single basepoint, so the quotient is their wedge.
:::
:::

::: {.pf-step #collapse}
If no component of $X$ is a point, then $S(X_\alpha)\simeq\Sigma X_\alpha$ for $\alpha\neq\alpha_0$.

::: pf-proof
For such $\alpha$ the pair $(S(X_\alpha),\{*_\alpha\}\times I)$ has contractible second term and is a CW pair, so collapsing that interval, which carries $S(X_\alpha)$ to the reduced suspension $\Sigma X_\alpha$, is a homotopy equivalence by Proposition 0.17 (p. 15).
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
$\Omega$ carries the homotopy equivalence of step [](#wedge){.pf-ref} to one of loop spaces. A loop space is path-connected because loops can be reparametrised to concatenate, and the wedge is path-connected because its components are path-connected and share the basepoint.
:::
:::

::: {.pf-step #conclusion}
Each path-component of $\Omega\Sigma X$ is homotopy equivalent to $\Omega\Sigma(\bigvee_\alpha X_\alpha)$.

::: pf-proof
By step [](#loops){.pf-ref} $\Omega\Sigma X$ has a single path-component, namely itself, and it is homotopy equivalent to $\Omega\Sigma(\bigvee_\alpha X_\alpha)$, which is a connected CW complex, so Theorem 4J.1 (p. 471) applies to it and its conclusion transfers to $\Omega\Sigma X$.
:::
:::

::: {.pf-step #counterexample}
Without the hypothesis that no component is a point the claim fails: $X=S^1\sqcup\{\mathrm{pt}\}$ gives $\Sigma X=S^2\vee S^1$ but $\Sigma(\bigvee_\alpha X_\alpha)=S^2$.

::: pf-proof
For the singleton component, $S(X_\alpha)$ is an interval and $\Sigma X_\alpha$ is a point, so step [](#pieces){.pf-ref} gives $\Sigma X=S^2\vee S^1$ while the wedge of the components is $S^1$ with $\Sigma$ equal to $S^2$. Then $\pi_1$ of $\Omega\Sigma X=\pi_2(S^2\vee S^1)$, which is free abelian on countably many generators, while $\pi_2(S^2)\cong\ZZ$.
:::
:::

:::
:::
