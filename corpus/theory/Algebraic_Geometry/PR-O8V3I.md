---
schema: qual/card@1
id: PR-O8V3I
kind: proposition
title: The orbit-cone correspondence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Orbits
  - Fans
relations:
- kind: uses
  target: D-Q7Q2N
review: draft
prompts:
- State the orbit-cone correspondence.
- Which cone corresponds to a fixed point?
---

::: {.proposition}
For a fan $\Sigma$ in $N_\RR$ with $\dim N = n$, there is an inclusion-reversing bijection
\[
\ts{\text{cones } \sigma \in \Sigma} \longleftrightarrow \ts{T\text{-orbits in } X_\Sigma} , \qquad \sigma \mapsto O(\sigma) = T \cdot x_\sigma ,
\]
under which $\dim O(\sigma) = n - \dim \sigma$, and $\overline{O(\sigma)} = \bigcup_{\tau \supseteq \sigma} O(\tau)$.
:::

::: {.remark}
The distinguished point $x_\sigma$ is the semigroup homomorphism $S_\sigma \to \ts{0,1}$ sending $m$ to $1$ exactly when $m \in \sigma^\perp$, which is the limit of a one-parameter subgroup in the relative interior of $\sigma$.

The two ends of the correspondence are the ones to say aloud: the zero cone gives the dense torus orbit, and a maximal cone of dimension $n$ gives a fixed point.
Rays give the $T$-invariant prime divisors, so $\Sigma(1)$ *is* the set of boundary divisors, and this is the start of every divisor computation on a toric variety:
\[
\ZZ^{\Sigma(1)} \to \Cl(X_\Sigma) \to 0 , \qquad \text{with kernel } M \text{ when } X_\Sigma \text{ has no torus factor} .
\]
The class group is a cokernel of an explicit integer matrix, which is why toric examples can realise prescribed class groups: the cone on $(0,1)$ and $(d,-1)$ has $\Cl = \ZZ/d$.
:::
