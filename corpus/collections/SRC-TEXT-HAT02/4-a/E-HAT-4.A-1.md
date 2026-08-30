---
schema: qual/card@1
id: E-HAT-4.A-1
kind: exercise
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
---

Show directly that if $X$ is a topological group with identity element $x_0$, then any two maps $f, g: (Z, z_0) \to (X, x_0)$ which are homotopic are homotopic through basepoint-preserving maps.

::: {.solution}
<1>1. Track of the basepoint under the unbased homotopy:
<2>1. Let $H: Z \times I \to X$ be an unbased homotopy between $f$ and $g$, so $H(z, 0) = f(z)$ and $H(z, 1) = g(z)$ for all $z \in Z$.
Proof: hypothesis $f \simeq g$.
<2>2. Define the path $\gamma: I \to X$ traced by the basepoint $z_0$:
\[
\gamma(t) = H(z_0, t).
\]
Because $f, g: (Z, z_0) \to (X, x_0)$ are pointed maps, the endpoints of $\gamma$ satisfy:
\[
\gamma(0) = H(z_0, 0) = f(z_0) = x_0, \qquad \gamma(1) = H(z_0, 1) = g(z_0) = x_0.
\]
Thus $\gamma$ is a loop in $X$ based at the identity element $x_0$.
Proof: pointed map condition on $f$ and $g$.

<1>2. Construction of the basepoint-preserving homotopy:
<2>1. Since $X$ is a topological group, multiplication $m: X \times X \to X$ and inversion $i: X \to X$ are continuous.
Define $F: Z \times I \to X$ by:
\[
F(z, t) = H(z, t) \cdot (\gamma(t))^{-1}.
\]
As a composition of continuous functions, $F$ is continuous.
Proof: continuity of group operations on topological groups.
<2>2. Check the initial and final time slices:
\[
F(z, 0) = H(z, 0) \cdot (\gamma(0))^{-1} = f(z) \cdot x_0^{-1} = f(z),
\]
\[
F(z, 1) = H(z, 1) \cdot (\gamma(1))^{-1} = g(z) \cdot x_0^{-1} = g(z).
\]
Proof: $\gamma(0) = \gamma(1) = x_0$ is the identity element of $X$.
<2>3. Check basepoint preservation for all $t \in [0, 1]$:
\[
F(z_0, t) = H(z_0, t) \cdot (\gamma(t))^{-1} = \gamma(t) \cdot (\gamma(t))^{-1} = x_0.
\]
Thus $F(z_0, t) = x_0$ for every $t \in I$.
Proof: group axiom $g \cdot g^{-1} = e$.

<1>3. Conclusion:
$F: (Z \times I, \{z_0\} \times I) \to (X, x_0)$ is a pointed homotopy between $f$ and $g$. Q.E.D.
Proof: <1>1 and <1>2.
:::
