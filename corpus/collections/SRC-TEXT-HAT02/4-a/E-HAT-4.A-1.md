---
schema: qual/card@1
id: E-HAT-4.A-1
kind: problem
title: "Homotopies of maps to topological groups are basepoint-preserving"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.A Exercise 1, printed p. 426; the statement
    matches the print. The proof is correct and complete as it stands and needed no repair:
    $F(z,t)=H(z,t)\gamma(t)^{-1}$ with $\gamma(t)=H(z_0,t)$ is continuous because multiplication and
    inversion in a topological group are, has $F(z,0)=f(z)x_0^{-1}=f(z)$ and
    $F(z,1)=g(z)x_0^{-1}=g(z)$, and is basepoint-preserving because
    $F(z_0,t)=\gamma(t)\gamma(t)^{-1}=x_0$. The $L_\gamma R_{\gamma^{-1}}$ normalisation used here is
    the same device Hatcher uses in Example 4A.3 (p. 421) to show that an H-space has trivial action
    of $\pi_1$; the group case does not need the H-space machinery since inverses are available. No
    published solution of this exercise is in the retained sets — none of them covers §4.A at all —
    recorded in COMPLAINTS.md.
---

::: {.problem}
Show directly that if $X$ is a topological group with identity element $x_0$, then any two maps $f, g: (Z, z_0) \to (X, x_0)$ which are homotopic are homotopic through basepoint-preserving maps.
:::

::: {.solution}
::: pf

::: pf-step
Track of the basepoint under the unbased homotopy:

::: pf-proof

::: pf-step
Let $H: Z \times I \to X$ be an unbased homotopy between $f$ and $g$, so $H(z, 0) = f(z)$ and $H(z, 1) = g(z)$ for all $z \in Z$.
:::

::: pf-step
Define the path $\gamma: I \to X$ traced by the basepoint $z_0$:
$$
\gamma(t) = H(z_0, t).
$$
Because $f, g: (Z, z_0) \to (X, x_0)$ are pointed maps, the endpoints of $\gamma$ satisfy:
$$
\gamma(0) = H(z_0, 0) = f(z_0) = x_0, \qquad \gamma(1) = H(z_0, 1) = g(z_0) = x_0.
$$
Thus $\gamma$ is a loop in $X$ based at the identity element $x_0$.
:::

:::

:::

::: pf-step
Construction of the basepoint-preserving homotopy:

::: pf-proof

::: pf-step
Since $X$ is a topological group, multiplication $m: X \times X \to X$ and inversion $i: X \to X$ are continuous.
Define $F: Z \times I \to X$ by:
$$
F(z, t) = H(z, t) \cdot (\gamma(t))^{-1}.
$$
As a composition of continuous functions, $F$ is continuous.
:::

::: pf-step
Check the initial and final time slices:
$$
F(z, 0) = H(z, 0) \cdot (\gamma(0))^{-1} = f(z) \cdot x_0^{-1} = f(z),
$$
$$
F(z, 1) = H(z, 1) \cdot (\gamma(1))^{-1} = g(z) \cdot x_0^{-1} = g(z).
$$
:::

::: pf-step
Check basepoint preservation for all $t \in [0, 1]$:
$$
F(z_0, t) = H(z_0, t) \cdot (\gamma(t))^{-1} = \gamma(t) \cdot (\gamma(t))^{-1} = x_0.
$$
Thus $F(z_0, t) = x_0$ for every $t \in I$.
:::

:::

:::

::: pf-step
Conclusion:
$F: (Z \times I, \{z_0\} \times I) \to (X, x_0)$ is a pointed homotopy between $f$ and $g$.
:::

:::

:::
