---
schema: qual/card@1
id: E-F5K2X
kind: exercise
title: "Forcing a map to be the identity"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Forcing a map to be the identity"}
Let $\psi_a$ be a Blaschke factor and use the Schwarz lemma to prove that $\psi_a \circ \psi_a = \id_\DD$.

#complex/exercise/completed

:::

:::{.solution}
First, $\psi_a$ maps $\DD\to \DD$.
Fix $z\in S^1$, then
\[
\abs{\psi_a(z)} \da 
\abs{a-z\over 1-\bar{a} z}
&= \abs{a-z\over 1-\bar{a} z} \cdot \abs{\bar z}\inv \\
&= \abs{a-z\over \bar{a} - \bar{z}} \\
&= \abs{a-z \over \bar{a-z} } \\
&\da \abs{w \over \bar w } \\
&= \abs{w \over \abs{w}^2/w }\\
&= \abs{w^2 \over \abs{w}^2} \\
&= 1
.\]
$\psi_a$ is holomorphic on $\DD$ since it has a simple pole at $z=1/\bar{a}$, but $\abs{a}<1$ implies $\abs{1/\bar{a}} > 1$.
Let $g\da \psi_a\circ \psi_a$, then $g(0) = 0$ so Schwarz applies.
Since $g(a) = a$ with $a\neq 0$, the 2nd part of Schwarz also applies since $\abs{g(a)} = \abs{a}$ and $g(z) = \lambda z$ is a rotation.
Since $a = g(a) = \lambda a$, this forces $\lambda = 1$, so $g$ is the identity.
:::
