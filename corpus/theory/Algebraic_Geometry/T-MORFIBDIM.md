---
schema: qual/card@1
id: T-MORFIBDIM
kind: theorem
title: Fibre dimension and upper semicontinuity
slogan: 'Fibre dimensions can jump only up on special loci: the general fibre has dimension $\dim X-\dim Y$, and larger-fibre loci are closed.'
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
Let $k$ be an infinite field and $X \subseteq \AA^{n}_k$ an affine variety of dimension $d$.
Then there exists a finite morphism $X \to \AA^{d}$ which is the restriction to $X$ of a linear map $\AA^{n} \to \AA^{d}$.
:::

::: {.theorem title="Noether normalization (projective)"}
Let $k$ be an infinite field and $X \subseteq \PP^{n}_k$ a projective variety of dimension $d$.
Then there exists a finite morphism $X \to \PP^{d}$ which is the restriction to $X$ of a linear projection $\PP^{n} \dashrightarrow \PP^{d}$ with centre a linear subspace $\PP^{k} \subseteq \PP^{n}$ disjoint from $X$, where $k + d = n - 1$.
:::

::: {.remark}
The linear forms are chosen from a nonempty Zariski open subset of a space of linear maps, which has $k$-points because $k$ is infinite.
Over a finite field a linear map need not exist: over $\FF_2$, no linear map $\AA^2 \to \AA^1$ restricts to a finite morphism on the irreducible cubic $V(xy(x+y) + 1)$.
Noether normalization still holds over every field if nonlinear maps such as $(x_1 - x_n^{e_1}, \ldots, x_{n-1} - x_n^{e_{n-1}})$ are allowed.
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
Upper semicontinuity means fibre dimension can jump **up** on special loci, never down.
The blowup is the model: fibre dimension $0$ generically, $1$ over the origin, and the jump locus $\theset{0}$ is closed.
It cannot go the other way, because a component of a fibre is cut out by $\dim Y$ equations locally and Krull's height theorem bounds the drop.

The two halves are used differently.
The lower bound proves positive-dimensional fibres in dimension-comparison arguments.
The generic equality gives the dimension formula $\dim X = \dim Y + \dim(\text{general fibre})$.

Flatness removes this jumping by forcing the expected local fibre dimension everywhere.
:::
