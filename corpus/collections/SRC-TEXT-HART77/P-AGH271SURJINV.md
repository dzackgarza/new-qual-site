---
schema: qual/card@1
id: P-AGH271SURJINV
kind: problem
title: A surjection of invertible sheaves is an isomorphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Invertible Sheaves
  - Locally Ringed Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the statement and stalkwise hint with the retained Hartshorne II.7.1 transcription. The proof identifies each stalk map with multiplication by a unit and glues the unique local inverse images of sections.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $(X, \OO_X)$ be a locally ringed space, and let $f: \mcl \to \mcm$ be a surjective map of invertible sheaves on $X$.
Show that $f$ is an isomorphism.
:::

::: {.hint}
Reduce to a question of modules over a local ring by looking at the stalks.
:::

::: {.solution}
<1>1. For every $x\in X$, the induced homomorphism $f_x:\mcl_x\to\mcm_x$ is an isomorphism of $\OO_{X,x}$-modules.

::: {.proof}
Put $R=\OO_{X,x}$.
The stalks of both invertible sheaves are free $R$-modules of rank one.
Choose generators $e$ and $h$, and write $f_x(e)=ah$ with $a\in R$.
Surjectivity of the sheaf map implies surjectivity on stalks, so there is $b\in R$ with $f_x(be)=h$.
Consequently $ba=1$.
The ring is commutative, so $a$ is a unit with inverse $b$, and $ch\mapsto bce$ is the inverse module map.
:::

<1>2. The stalkwise isomorphisms make $f$ an isomorphism of sheaves.

::: {.proof}
For an open set $U$, any section of $\mcl(U)$ whose image under $f$ is zero has zero germ at every point by step <1>1, and is therefore zero.
Thus $f$ is injective on sections over every open set.

Let $s\in\mcm(U)$.
Surjectivity at each stalk gives local lifts: a lift of the germ at $x$ is represented by a section near $x$, and equality with the germ of $s$ becomes equality of sections after shrinking that neighborhood.
On overlaps, these local lifts agree by injectivity on sections.
They therefore glue to a unique section $t\in\mcl(U)$ with $f(t)=s$.
Uniqueness makes this inverse assignment compatible with restrictions and with the $\OO_X$-module operations.
It defines the inverse sheaf morphism, as in [[P-AGH215ISOINJSURJ]].
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 proves invertibility on every stalk, and step <1>2 constructs the inverse morphism of sheaves.
:::
:::
