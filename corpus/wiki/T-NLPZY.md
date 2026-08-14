---
schema: qual/card@1
id: T-NLPZY
kind: theorem
title: "Fundamental Theorem of Galois Theory"
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - field-extensions
  - normal-subgroups
relations: []
review: draft
---

::: {.theorem title="Fundamental Theorem of Galois Theory"}
Let $L/k$ be a Galois extension, then there is a correspondence:
\[
\correspond{\text{Subgroups } H \leq \Gal(L/k)}
&\mapstofrom
\correspond{\text{Fields }  F \text{ such}\\ \text{that } L/F/k} \\
H &\rightarrow \correspond{E^H \definedas ~\text{The fixed field of $H$}} \\
\correspond{\Gal(L/F) \definedas \theset{ \sigma \in \Gal(L/k) \suchthat \sigma(F) = F}} &\leftarrow F
\]

- This is contravariant with respect to subgroups/subfields.

- $[F: k] = [G: H]$, so degrees of extensions over the base field correspond to indices of subgroups.

- $[K : F] = \abs{H}$

- $L/F$ is Galois and $Gal(K/F) = H$

- $F/k$ is Galois $\iff H$ is normal, and $\Gal(F/k) = \Gal(L/k)/H$.

- The compositum $F_1 F_2$ corresponds to $H_1 \intersect H_2$.

- The subfield $F_1 \intersect F_2$ corresponds to $H_1 H_2$.
:::
