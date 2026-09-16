---
schema: qual/card@1
id: T-MORFIBDIM
kind: theorem
title: Fibre dimension and upper semicontinuity
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fibre Dimension
  - Semicontinuity
  - Dimension
relations:
- kind: uses
  target: D-MORFIB
review: draft
prompts:
- State the fibre dimension theorem.
- In what sense is fibre dimension semicontinuous, and in which direction?
- What is Noether normalization?
---

::: {.theorem title="Noether normalization (affine)"}
Let $X \subseteq \AA^{n}$ be an affine variety of dimension $d$.
Then there exists a finite morphism $X \to \AA^{d}$ which is the restriction to $X$ of a linear map $\AA^{n} \to \AA^{d}$.
:::

::: {.theorem title="Noether normalization (projective)"}
Let $X \subseteq \PP^{n}$ be a projective variety of dimension $d$.
Then there exists a finite morphism $X \to \PP^{d}$ which is the restriction to $X$ of a linear projection $\PP^{n} \dashrightarrow \PP^{d}$ with centre a linear subspace $\PP^{k} \subseteq \PP^{n}$ disjoint from $X$, where $k + d = n - 1$.
:::

::: {.theorem title="Fibre dimension"}
Let $f : X \to Y$ be a dominant morphism of integral schemes of finite type over a field, and set $e = \dim X - \dim Y$.
Then every irreducible component of every nonempty fibre $X_y$ has dimension at least $e$, and there is a nonempty open $V \subseteq Y$ with $\dim X_y = e$ for every $y \in V$.
:::

::: {.theorem title="Semicontinuity"}
The function $x \mapsto \dim_x X_{f(x)}$ is **upper** semicontinuous on $X$: the locus where the fibre dimension is at least $n$ is closed.
If $f$ is flat then $\dim_x X_{f(x)} = \dim_x X - \dim_{f(x)} Y$ at every point, so the fibre dimension is locally constant.
:::

::: {.remark}
The direction of the inequality is the part that gets asked, and the mnemonic is that fibres can only jump **up** over special points, never down.
The blowup is the model: fibre dimension $0$ generically, $1$ over the origin, and the jump locus $\ts{0}$ is closed.
It cannot go the other way, because a component of a fibre is cut out by $\dim Y$ equations locally and Krull's height theorem bounds the drop.

The two halves are used differently.
The lower bound is the tool for proving something is nonempty, as in "a morphism from a projective variety of dimension $> e$ to a variety of dimension $e$ has positive-dimensional fibres", which is the engine behind rigidity statements.
The generic equality is the tool for computing dimensions by counting: fibre a parameter space over something known, and $\dim = \dim(\text{base}) + \dim(\text{general fibre})$.

Flatness is exactly the hypothesis that removes the jumping, which is the cleanest statement of what flatness is for.
:::
