---
schema: qual/card@1
id: P-UNL871F13-PS3.1B
kind: problem
title: Coordinate projections from arbitrary products are open maps
classification:
  areas: [topology]
  topics: [Product Topology]
relations: []
review: draft
---

::: {.problem}
Let $\{X_\alpha\}_{\alpha\in I}$ be topological spaces and give
$$
\prod_{\alpha\in I}X_\alpha
$$
the product topology.
For every $\beta\in I$, prove that the coordinate projection
$$
\pi_\beta:\prod_{\alpha\in I}X_\alpha\longrightarrow X_\beta
$$
is an open map.
:::

::: {.solution}

::: pf

::: pf-step

A basis for the product topology consists of sets
$$
B
=
\prod_{\alpha\in I}U_\alpha,
$$
where each
$$
U_\alpha\subseteq X_\alpha
$$
is open and
$$
U_\alpha=X_\alpha
$$
for all but finitely many $\alpha$.


::: pf-proof

This is the standard basis for the product topology.

:::

:::

::: {.pf-step #s1-2}

For such a basis element,
$$
\pi_\beta(B)
=
U_\beta.
$$


::: pf-proof

If
$$
x=(x_\alpha)_{\alpha\in I}
\in B,
$$
then
$$
x_\beta\in U_\beta,
$$
so
$$
\pi_\beta(B)
\subseteq
U_\beta.
$$

Conversely, let
$$
y\in U_\beta.
$$
For every
$$
\alpha\ne\beta,
$$
choose
$$
x_\alpha\in U_\alpha
$$
whenever $U_\alpha$ is nonempty.
Since $B$ itself is nonempty whenever this basis element contributes to an
open set, such choices exist.
Set
$$
x_\beta=y.
$$
Then
$$
x=(x_\alpha)\in B
$$
and
$$
\pi_\beta(x)=y.
$$
Thus
$$
U_\beta
\subseteq
\pi_\beta(B).
$$

:::

:::

::: {.pf-step #s1-3}

Therefore the projection of every product-basic open set is open in
$$
X_\beta.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\pi_\beta(B)
=
U_\beta,
$$
and $U_\beta$ is open by construction.

:::

:::

::: {.pf-step #s1-4}

Let
$$
O
\subseteq
\prod_{\alpha\in I}X_\alpha
$$
be open.
Then
$$
\pi_\beta(O)
$$
is open in $X_\beta$.


::: pf-proof

Write $O$ as a union of basis elements:
$$
O
=
\bigcup_{j\in J}B_j.
$$
Images commute with unions, so
$$
\pi_\beta(O)
=
\bigcup_{j\in J}
\pi_\beta(B_j).
$$
Each set
$$
\pi_\beta(B_j)
$$
is open by step [](#s1-3){.pf-ref}.
Hence their union is open.

:::

:::

::: {.pf-step #s1-5}

Consequently
$$
\boxed{
\pi_\beta:
\prod_{\alpha\in I}X_\alpha
\longrightarrow
X_\beta
\text{ is an open map}.
}
$$


::: pf-proof

Step [](#s1-4){.pf-ref} verifies the definition of an open map.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
