---
schema: qual/card@1
id: FE-SHFPONE
kind: example
title: Twisting sheaves and a skyscraper sequence on the projective line
classification:
  areas:
  - algebraic-geometry
  topics:
  - Twisting Sheaves
  - Skyscraper Sheaves
  - Exact Sequences
relations:
- kind: uses
  target: D-CB9XS
review: draft
prompts:
- On $\PP^1$, show that $0 \to \OO(-1) \to \OO \to k_{[1:0]} \to 0$ is exact.
- Show that $\OO(d_1) \otimes \OO(d_2) \cong \OO(d_1 + d_2)$ and $\OO(d)^\vee \cong \OO(-d)$.
---

::: {.example title="A skyscraper sequence"}
Let $X = \PP^1_k = \Proj k[x_0, x_1]$ and $p = [1:0]$, the zero of $x_1$.
Multiplication by $x_1$ gives $\OO(-1) \to \OO$, with image the ideal sheaf $\mathcal{I}_p$ of the reduced point $p$.

1. On $D_+(x_1)$, $x_1$ is a unit, so the map is an isomorphism and both $\mathcal{I}_p$ and the quotient are trivial away from $p$.
2. On $D_+(x_0) = \Spec k[t]$ with $t = x_1/x_0$, the map is $k[t] \xrightarrow{t} k[t]$, which is injective with cokernel $k[t]/(t) = k$ supported at $t = 0$, that is, at $p$.
3. So $0 \to \OO(-1) \xrightarrow{x_1} \OO \to k_p \to 0$ is exact on stalks, hence exact, where $k_p$ is the skyscraper sheaf at $p$ with value $k$.
:::

::: {.example title="Tensor products and duals of twists"}
On each chart $D_+(x_i)$ the sheaf $\OO(d)$ is free with generator $x_i^d$, and on overlaps the generators differ by the transition functions $(x_i/x_j)^d$.
Multiplication $\OO(d_1) \otimes \OO(d_2) \to \OO(d_1 + d_2)$, $s \otimes s' \mapsto s s'$, sends the local generator $x_i^{d_1} \otimes x_i^{d_2}$ to the local generator $x_i^{d_1 + d_2}$, so it is an isomorphism.
Taking $d_2 = -d_1$ gives $\OO(d) \otimes \OO(-d) \cong \OO$, and a perfect pairing of invertible sheaves identifies $\OO(-d) \cong \sheafhom(\OO(d), \OO) = \OO(d)^\vee$.
:::
