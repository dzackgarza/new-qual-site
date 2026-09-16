---
schema: qual/card@1
id: D-ALGSTACK
kind: definition
title: Algebraic stacks, substacks, smooth stacks, and orbifolds
classification:
  areas:
  - algebraic-geometry
  topics:
  - Algebraic Stacks
  - Deligne-Mumford Stacks
  - Orbifolds
relations:
- kind: uses
  target: D-ALGSPACE
- kind: uses
  target: D-MORLOCAL
- kind: related-to
  target: T-MGSMOOTH
review: draft
prompts:
- What is a locally closed substack?
- What is a smooth stack?
- What is an orbifold?
---

Let $S$ be a scheme and $\Sch_{/S}$ the category of $S$-schemes with the étale topology ([[D-ETFPPF]]).

::: {.definition title="Stack"}
A \dfn{stack} over $S$ is a category $\mathcal{X}$ with a functor $p \colon \mathcal{X} \to \Sch_{/S}$ such that

1. $\mathcal{X}$ is fibred in groupoids: for every morphism $T' \to T$ and object $\xi$ over $T$ there is a pullback $\xi|_{T'}$ over $T'$, unique up to unique isomorphism, and every morphism lying over an identity is an isomorphism;

2. for all objects $\xi, \eta$ over $T$, the presheaf $\operatorname{Isom}(\xi, \eta) \colon (T' \to T) \mapsto \{\text{isomorphisms } \xi|_{T'} \to \eta|_{T'} \text{ over } T'\}$ is a sheaf on $(\Sch_{/T})_{\mathrm{et}}$;

3. every descent datum is effective: for an étale covering $\{T_i \to T\}$, objects $\xi_i$ over $T_i$ with isomorphisms $\varphi_{ij} \colon \xi_j|_{T_{ij}} \to \xi_i|_{T_{ij}}$ satisfying $\varphi_{ij} \circ \varphi_{jk} = \varphi_{ik}$ on $T_{ijk}$ come from an object $\xi$ over $T$.

A $1$-morphism $\mathcal{Y} \to \mathcal{X}$ of stacks is \dfn{representable} if for every $S$-scheme $T$ and $T \to \mathcal{X}$, the $2$-fibre product $\mathcal{Y} \times_{\mathcal{X}} T$ is an algebraic space ([[D-ALGSPACE]]).
For a class $P$ of morphisms of algebraic spaces that is stable under base change and étale local on the target ([[D-MORLOCAL]]), a representable $\mathcal{Y} \to \mathcal{X}$ has $P$ if every such base change $\mathcal{Y} \times_{\mathcal{X}} T \to T$ has $P$.
:::

::: {.definition title="Algebraic and Deligne--Mumford stacks"}
A stack $\mathcal{X}$ over $S$ is \dfn{algebraic} if its diagonal $\mathcal{X} \to \mathcal{X} \times_S \mathcal{X}$ is representable and there are a scheme $U$ and a representable, smooth, surjective morphism $U \to \mathcal{X}$, a \dfn{smooth atlas}.
It is \dfn{Deligne--Mumford} if moreover it has an atlas $U \to \mathcal{X}$ that is étale.
:::

::: {.definition title="Substacks"}
A \dfn{substack} of a stack $\mathcal{X}$ is a full subcategory $\mathcal{Z} \subseteq \mathcal{X}$ closed under isomorphisms and pullbacks.
It is an \dfn{open}, \dfn{closed} or \dfn{locally closed substack} if the inclusion $\mathcal{Z} \to \mathcal{X}$ is representable by open immersions, closed immersions or immersions: for every $S$-scheme $T$ and object of $\mathcal{X}$ over $T$, the base change $\mathcal{Z} \times_{\mathcal{X}} T \to T$ is an open, closed or locally closed immersion of schemes.
:::

::: {.definition title="Smooth stack"}
An algebraic stack $\mathcal{X}$ over $S$ is \dfn{smooth over $S$} if for some smooth atlas $U \to \mathcal{X}$ the composite $U \to S$ is smooth.
:::

::: {.remark}
Smoothness of $U \to S$ does not depend on the choice of smooth atlas.
:::

::: {.definition title="Orbifold"}
An \dfn{orbifold} over $\CC$ is a smooth, separated Deligne--Mumford stack of finite type over $\CC$ whose stabilizer group at a general point is trivial.
:::

::: {.example}
The weighted projective line $\PP(1,2)$ is the quotient stack $[(\AA^2 \setminus \{0\}) / \GG_m]$ for the action $\lambda \cdot (x, y) = (\lambda x, \lambda^2 y)$ over $\CC$.
The atlas $\AA^2 \setminus \{0\} \to \PP(1,2)$ is smooth, and the stabilizers are finite and reduced: a point $(x, y)$ with $x \neq 0$ has trivial stabilizer, while $(0, 1)$ has stabilizer $\{\lambda : \lambda^2 = 1\} = \mu_2$.
So $\PP(1,2)$ is a smooth separated Deligne--Mumford stack with trivial generic stabilizer, an orbifold with one point of stabilizer $\mu_2$.
The moduli stacks $\mathcal{M}_g$ of smooth curves of genus $g \geq 2$ are smooth Deligne--Mumford stacks ([[T-MGSMOOTH]]).
:::
