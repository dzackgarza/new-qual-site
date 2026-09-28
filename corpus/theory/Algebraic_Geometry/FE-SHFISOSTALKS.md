---
schema: qual/card@1
id: FE-SHFISOSTALKS
kind: example
title: Sheaves with isomorphic stalks, and pushforwards of locally constant sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Stalks
  - Direct Image Functor
relations:
- kind: uses
  target: D-VJFAP
review: draft
prompts:
- Give an example of two sheaves with isomorphic stalks at every point that are not isomorphic.
- Is the pushforward of a locally constant sheaf always locally constant?
---

::: {.example title="Isomorphic stalks, nonisomorphic sheaves"}
Let $X = Y = S^1 \subset \CC$ be the unit circle, and let $f \colon X \to Y$ be the two-sheeted covering map $f(z) = z^2$.
Let $\mcf = \ul{\ZZ}_X$ be the constant sheaf with value $\ZZ$ on $X$.

1. Every $y \in Y$ has arbitrarily small connected open neighbourhoods $V$ with $f^{-1}(V) = U_1 \amalg U_2$, each $U_i$ connected and mapped homeomorphically onto $V$.
   So $(f_* \mcf)(V) = \mcf(U_1) \oplus \mcf(U_2) \cong \ZZ^2$, the restriction maps between such neighbourhoods are isomorphisms, and $(f_* \mcf)_y \cong \ZZ^2$.

2. Let $\mcg = \ul{\ZZ^2}_Y$ be the constant sheaf.
   Its stalks are also $\ZZ^2$ at every point.

3. $\Gamma(Y, \mcg) \cong \ZZ^2$ because $Y$ is connected, while $\Gamma(Y, f_* \mcf) = \mcf(X) \cong \ZZ$ because $X$ is connected.
   Since $\ZZ \not\cong \ZZ^2$, the sheaves $f_* \mcf$ and $\mcg$ are not isomorphic, although all their stalks are isomorphic.
:::

::: {.remark}
By step 1, $f_* \mcf$ restricts to a constant sheaf on each such $V$, so it is a locally constant sheaf.
It is not constant: going once around $Y$ exchanges the two sheets, and its global sections are the invariants $(\ZZ^2)^{\ZZ/2} \cong \ZZ$.
So this example shows that stalks do not determine a sheaf; it does not show that pushforward destroys local constancy, because the pushforward of a locally constant sheaf along a finite covering map is locally constant.

A morphism of sheaves $\phi \colon \mcf \to \mcg$ is an isomorphism exactly when every stalk map $\phi_x$ is an isomorphism.
The hypothesis is a single morphism $\phi$ inducing the stalk isomorphisms; isomorphisms between stalks chosen separately at each point do not suffice.
:::

::: {.example title="A pushforward of a locally constant sheaf that is not locally constant"}
Let $j \colon U = (0, \infty) \hookrightarrow \RR$ be the inclusion and $\mcf = \ul{\ZZ}_U$.
For an open interval $I \subseteq \RR$, $(j_* \mcf)(I) = \mcf(I \cap (0, \infty))$, which is $\ZZ$ if $I$ meets $(0,\infty)$ and $0$ otherwise.
So $(j_* \mcf)_x = \ZZ$ for $x \geq 0$ and $(j_* \mcf)_x = 0$ for $x < 0$.
Every neighbourhood of $0$ contains points of both kinds, and a locally constant sheaf has isomorphic stalks at all points of a connected neighbourhood, so $j_* \mcf$ is not locally constant.
:::
