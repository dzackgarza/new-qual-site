---
schema: qual/card@1
id: T-MORFIBDIM
kind: theorem
title: Fibre dimension and upper semicontinuity
slogan: 'The largest fibre component through a point is upper semicontinuous on the source; the local fibre dimension is not, and for a closed map the fibre dimension is upper semicontinuous on the target.'
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
Then there exists a finite morphism $X \to \PP^{d}$ which is the restriction to $X$ of a linear projection $\PP^{n} \dashrightarrow \PP^{d}$ with centre a linear subspace $\PP^{c} \subseteq \PP^{n}$ disjoint from $X$, where $c + d = n - 1$.
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
Let $f\colon X\to Y$ be a morphism of finite type between schemes locally of finite type over a field.
The function
$$
x\longmapsto \max\theset{\dim Z \st Z \text{ an irreducible component of } X_{f(x)} \text{ with } x\in Z}
$$
is upper semicontinuous on $X$: for every integer $r$, the locus
$$
\theset{x\in X\st \text{some irreducible component } Z \text{ of } X_{f(x)} \text{ has } x\in Z \text{ and } \dim Z\geq r}
$$
is closed [@Vak25, Theorem 12.4.3(a)] [@Har77, Exercise II.3.22(d)].
The local dimension $\dim_x X_{f(x)}=\krulldim\OO_{X_{f(x)},x}$ is a different function, and it is not upper semicontinuous in general.

If $f$ is flat, then
$$
\dim_x X_{f(x)}=\dim_x X-\dim_{f(x)}Y
$$
[@Har77, Proposition III.9.5]: this is a pointwise formula, and $\dim_x X$ and $\dim_{f(x)}Y$ are local dimensions, so the left-hand side varies with $x$ and is not constant in general.
What is constant under flatness is the component dimension: if $Y$ is irreducible and every irreducible component of $X$ has dimension $\dim Y+n$, then every irreducible component of every fibre has dimension $n$ [@Har77, Corollary III.9.6].

If $f$ is closed, in particular if $f$ is proper, then the function $y\mapsto\dim X_y$ is upper semicontinuous on $Y$: the locus $\theset{y\st\dim X_y\geq r}$ is the image under the closed map $f$ of the corresponding closed locus in $X$ [@Vak25, Theorem 12.4.3(b)].
:::

::: {.remark}
Upper semicontinuity on the source means the largest fibre component through a point can jump up on closed special loci.
The blowup is the model: fibre dimension $0$ generically, $1$ over the origin, and the jump locus $\theset{0}$ is closed.
It cannot go the other way, because a component of a fibre is cut out by $\dim Y$ equations locally and Krull's height theorem bounds the drop.

The two halves are used differently.
The lower bound proves positive-dimensional fibres in dimension-comparison arguments.
The generic equality gives the dimension formula $\dim X = \dim Y + \dim(\text{general fibre})$.

For a flat finite-type morphism with $X$ equidimensional and $Y$ irreducible, the largest fibre-component dimension is constant, so this source-side jumping disappears; the local dimension can still vary from point to point of $X$, as the flat formula shows.
Equidimensionality is needed: for $X=\AA^1_k\sqcup\AA^2_k$ mapping to $\AA^1_k$ by the identity on the first component and the projection on the second, the morphism is flat, $X$ is not equidimensional, and the fibre-component dimension is $0$ on the first component and $1$ on the second.
:::
