---
schema: qual/card@1
id: P-AGXGATHSTALKRESTR
kind: problem
title: Stalks are unchanged by restriction to an open neighborhood
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Stalks
  - Restriction
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Gathmann 3.24 in the retained native problem source at revision
    7eafedfc0 and compared it with the current card. The retained source gives
    the problem statement but no worked solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the representative-level construction. Checked well-definedness
    in both directions and that intersecting with the fixed neighborhood U
    does not change a germ at a.
---

::: {.problem}
Let $\mcf$ be a sheaf on a topological space $X$ and $a\in X$.
Show that the stalk $\mcf_a$ is a *local object*: if $U\subset X$ is an open neighborhood of $a$, then $\mcf_a$ is isomorphic to the stalk of $\ro{\mcf}{U}$ at $a$ on $U$ viewed as a topological space.
:::

::: {.solution}
Put
$$
\mcf'=\ro{\mcf}{U}.
$$

<1>1. There is a canonical map
$$
\alpha:\mcf_a\longrightarrow\mcf'_a
$$
defined by restricting a representative to its intersection with $U$.

::: {.proof}
Represent a germ in $\mcf_a$ by a pair
$$
(V,s),
\qquad
a\in V\subseteq X,
\qquad
s\in\mcf(V).
$$
Since $U$ is an open neighborhood of $a$, the set
$$
V\cap U
$$
is an open neighborhood of $a$ in $U$. Define
$$
\alpha([V,s]_a)
=
[V\cap U,\ro{s}{V\cap U}]_a.
$$

If $(V,s)$ and $(W,t)$ determine the same germ in $\mcf_a$, there is an
open neighborhood
$$
N\subseteq V\cap W
$$
of $a$ on which the restrictions of $s$ and $t$ agree. Then
$$
N\cap U
$$
is an open neighborhood of $a$ in $U$ on which the corresponding
restricted representatives agree. Hence $\alpha$ is well defined.
:::

<1>2. There is a canonical map
$$
\beta:\mcf'_a\longrightarrow\mcf_a
$$
that regards a representative in $U$ as the same representative in $X$.

::: {.proof}
Represent a germ in $\mcf'_a$ by
$$
(V,s),
\qquad
a\in V\subseteq U,
\qquad
s\in\mcf'(V)=\mcf(V),
$$
where $V$ is open in $U$. Because $U$ is open in $X$, the set $V$ is also
open in $X$. Define
$$
\beta([V,s]_a)=[V,s]_a.
$$
If two such representatives agree on a neighborhood of $a$ in $U$, that
neighborhood is also open in $X$, so they determine the same germ in
$\mcf_a$. Thus $\beta$ is well defined.
:::

<1>3. The maps $\alpha$ and $\beta$ are inverse isomorphisms.

::: {.proof}
For a representative $(V,s)$ in $U$, one has $V\cap U=V$, so
$$
\alpha\beta([V,s]_a)=[V,s]_a.
$$

For a representative $(V,s)$ in $X$,
$$
\beta\alpha([V,s]_a)
=
[V\cap U,\ro{s}{V\cap U}]_a.
$$
The latter pair is a restriction of $(V,s)$ to another neighborhood of
$a$, so it represents the same germ:
$$
[V\cap U,\ro{s}{V\cap U}]_a=[V,s]_a.
$$
Therefore
$$
\boxed{\mcf_a\cong(\ro{\mcf}{U})_a}.
$$
The construction uses only restriction maps, so it preserves whatever
algebraic structure the sheaf values carry.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 construct the canonical stalk isomorphism and prove that
its two representative-level maps are inverse.
:::
:::
