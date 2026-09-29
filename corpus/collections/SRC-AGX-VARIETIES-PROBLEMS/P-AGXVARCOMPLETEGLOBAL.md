---
schema: qual/card@1
id: P-AGXVARCOMPLETEGLOBAL
kind: problem
title: Global regular functions on a connected complete variety are constant
classification:
  areas:
  - algebraic-geometry
  topics:
  - Complete Varieties
  - Global Sections
  - Regular Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the recorded Zaidenberg source. Its standing convention is that k is
    algebraically closed of characteristic zero, Remark 7.8 identifies complete
    varieties as the abstract analogue of projective varieties, and Exercise
    8.5 states that every regular function on a projective variety is constant.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the source's standing hypothesis on k explicit so the standalone
    statement has the field assumption needed for O_X(X)=k.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the closed-graph/closed-projection argument for the image in P^1,
    finiteness of a proper closed subset of P^1, connectedness of the image,
    and use of algebraic closedness to identify its unique closed point with
    an element of k.
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic zero.
Show that if $X$ is a connected complete $k$-variety, then
$$
\OO_X(X)=k,
$$
i.e. every global regular function is constant.
:::

::: {.solution}
Let
$$
f\in\OO_X(X).
$$
Regard $f$ as a morphism
$$
f:X\longrightarrow\AA^1_k,
$$
and let
$$
j:\AA^1_k\hookrightarrow\PP^1_k
$$
be the standard open immersion.

::: pf

::: {.pf-step #image-is-closed}
The image
$$
(j\circ f)(X)
$$
is closed in $\PP^1_k$.

::: pf-proof
Because $X$ is complete, for every $k$-variety $Y$ the projection
$$
\operatorname{pr}_2:X\times_k Y\longrightarrow Y
$$
is a closed map.

Take $Y=\PP^1_k$.
Since $\PP^1_k$ is separated, the graph
$$
\Gamma_{j\circ f}
\subseteq
X\times_k\PP^1_k
$$
is closed.
Its image under $\operatorname{pr}_2$ is exactly
$$
\operatorname{pr}_2(\Gamma_{j\circ f})
=(j\circ f)(X).
$$
The projection is closed by completeness of $X$, so this image is closed in $\PP^1_k$.
:::

:::

::: {.pf-step #image-is-finite}
The image $(j\circ f)(X)$ is finite.

::: pf-proof
By construction,
$$
(j\circ f)(X)\subseteq j(\AA^1_k)
=
\PP^1_k\setminus\{\infty\}.
$$
Hence the closed subset $(j\circ f)(X)$ from step [](#image-is-closed){.pf-ref} is a proper closed subset of $\PP^1_k$.

Every proper closed subset of $\PP^1_k$ is finite: it is contained in the zero locus of a nonzero homogeneous polynomial in two variables, and such a zero locus has only finitely many points on $\PP^1_k$.
Therefore $(j\circ f)(X)$ is finite.
:::

:::

::: {.pf-step #image-is-single-point}
The image $(j\circ f)(X)$ consists of one point.

::: pf-proof
A morphism is continuous in the Zariski topology, so the image of the connected space $X$ is connected.

By step [](#image-is-finite){.pf-ref}, $(j\circ f)(X)$ is a proper closed subset of $\PP^1_k$, hence a finite union of closed points.
Since $k$ is algebraically closed, those closed points are $k$-rational.
A finite union of closed points has the discrete induced topology, and a finite discrete space is connected only when it has one point.
Hence
$$
(j\circ f)(X)=\{a\}
$$
for some
$$
a\in\AA^1(k)=k.
$$
:::

:::

::: {.pf-step #f-is-constant}
Every $f\in\OO_X(X)$ is the constant function $a$ from step [](#image-is-single-point){.pf-ref}.

::: pf-proof
The open immersion $j$ is injective on points.
Since
$$
(j\circ f)(X)=\{a\},
$$
one has
$$
f(X)=\{a\}\subseteq\AA^1_k.
$$
Therefore
$$
f=a
$$
as a global regular function.
:::

:::

::: {.pf-step #global-sections-equal-k}
Consequently,
$$
\boxed{\OO_X(X)=k.}
$$

::: pf-proof
Constant functions give the canonical inclusion
$$
k\hookrightarrow\OO_X(X).
$$
Step [](#f-is-constant){.pf-ref} shows that every global regular function lies in its image.
Therefore the inclusion is an equality.
:::

:::

::: pf-qed
Step [](#global-sections-equal-k){.pf-ref} is the desired conclusion.
:::

:::

:::
