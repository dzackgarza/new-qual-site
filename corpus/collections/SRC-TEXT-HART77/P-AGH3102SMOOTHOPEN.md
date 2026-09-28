---
schema: qual/card@1
id: P-AGH3102SMOOTHOPEN
kind: problem
title: Smoothness spreads out from a smooth fibre
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Flat Morphisms
  - Openness of Smoothness
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.10.2 with the local criterion for smoothness and the
    openness of the smooth locus. The proof uses properness only to make the
    image of the nonsmooth locus closed in the base.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $f: X \to Y$ be a proper, flat morphism of varieties over $k$.
Suppose that for some point $y \in Y$ the fibre $X_y$ is smooth over $k(y)$.
Show that there is an open neighborhood $U$ of $y$ in $Y$ such that $f: f^{-1}(U) \to U$ is smooth.
:::

::: {.solution}
Let
$$
V=\{x\in X:f\text{ is smooth at }x\}.
$$

<1>1. Every point of the fibre $X_y$ lies in $V$.

::: {.proof}
Because $X$ and $Y$ are varieties, $f$ is locally of finite presentation.
It is flat everywhere by hypothesis.

Fix $x\in X_y$. The local fibre of $f$ at $x$ is the local ring of the
$k(y)$-scheme $X_y$ at $x$. Since $X_y$ is smooth over $k(y)$, it is
geometrically regular at $x$.
Thus at $x$ the morphism $f$ is flat, locally of finite presentation, and has
geometrically regular fibre. By the local criterion for smoothness
[[D-MORSM|for smooth morphisms]], $f$ is smooth at $x$.

Therefore
$$
X_y\subseteq V.
$$
:::

<1>2. The subset $V$ is open in $X$.

::: {.proof}
For a morphism locally of finite presentation, the locus where the morphism is
smooth is open [@Har10a, Chapter III, §10]. Hence $V\subseteq X$ is open.
Equivalently,
$$
Z=X\setminus V
$$
is closed.
:::

<1>3. The image $f(Z)$ is closed in $Y$ and does not contain $y$.

::: {.proof}
The morphism $f$ is proper, so it is closed. Since $Z$ is closed in $X$,
$$
f(Z)\subseteq Y
$$
is closed.

If $y\in f(Z)$, then some point of the fibre $X_y$ would lie in $Z$,
contradicting step <1>1. Therefore
$$
y\notin f(Z).
$$
:::

<1>4. The required neighborhood is
$$
U=Y\setminus f(Z).
$$

::: {.proof}
By step <1>3, $U$ is an open neighborhood of $y$.
Moreover, by definition of $U$,
$$
f^{-1}(U)\cap Z=\varnothing,
$$
so
$$
f^{-1}(U)\subseteq V.
$$
Thus $f$ is smooth at every point of $f^{-1}(U)$, which says precisely that
the restricted morphism
$$
f:f^{-1}(U)\longrightarrow U
$$
is smooth.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 show that the smooth locus contains the whole fibre over
$y$, and steps <1>3--<1>4 use properness to remove the image of its complement
from the base.
:::
:::
