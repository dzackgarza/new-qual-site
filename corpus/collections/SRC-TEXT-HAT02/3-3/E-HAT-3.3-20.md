---
schema: qual/card@1
id: E-HAT-3.3-20
kind: problem
title: Compactly supported $H^0$ of noncompact spaces
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 20; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: for compact $K$ the complement is nonempty, so restriction of locally
    constant functions from a path-connected $X$ to $X-K$ is injective and the relative group
    vanishes; the compactly supported group is the limit of these.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained solution set is cited on the card and none was
    located for this exercise among the retained Hatcher sets, so the argument is the card's own.
    Checked against Hatcher's definition of compactly supported cohomology as the direct limit of
    $H^i(X,X\setminus K;G)$ over compact $K$ (Section 3.3) and against the long exact sequence of a
    pair. Each step re-read: noncompactness makes every complement nonempty; a constant class on
    the path-connected $X$ restricts to a nonzero constant on a nonempty set; exactness makes the
    relative $H^0$ the kernel of that restriction; and a direct limit of zero groups along zero
    maps is zero. Nothing is claimed about $H_c^i$ for $i>0$ or about non-path-connected $X$, where
    the argument fails because the restriction need not be injective.
---

::: {.problem}
Show that $H_c^0(X; G) = 0$ if $X$ is path-connected and noncompact.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Hatcher, Algebraic Topology, Section 3.3, where compactly supported cohomology is defined as the direct limit of the groups $H^i(X,X\setminus K;G)$ over compact $K\subset X$, and against the long exact cohomology sequence of a pair.

::: pf

::: {.pf-step #complement}
For every compact $K\subset X$ the complement $X\setminus K$ is nonempty.

::: pf-proof
If $X\setminus K$ were empty then $X=K$ would be compact, contrary to the hypothesis.
:::

:::

::: {.pf-step #sequence}
For every compact $K\subset X$ the restriction $H^0(X;G)\to H^0(X\setminus K;G)$ is injective, and consequently $H^0(X,X\setminus K;G)=0$.

:::: pf-proof

::: {.pf-step #restriction}
That restriction is injective.

::: pf-proof
$X$ is path-connected, so $H^0(X;G)\cong G$ consists of the constant functions. A class $g\in G$ restricts to the constant function $g$ on the nonempty set $X\setminus K$, by step [](#complement){.pf-ref}; if that restriction is zero then $g=0$. Hence the restriction has trivial kernel.
:::

:::

::: {.pf-step #vanishing}
$H^0(X,X\setminus K;G)=0$.

::: pf-proof
The long exact cohomology sequence of the pair $(X,X\setminus K)$ begins with
$$
0\longrightarrow H^0(X,X\setminus K;G)\longrightarrow H^0(X;G)\longrightarrow H^0(X\setminus K;G),
$$
so exactness makes $H^0(X,X\setminus K;G)$ the kernel of the restriction, which is zero by step [](#restriction){.pf-ref}.
:::

:::

::::

:::

::: {.pf-step #limit}
$H_c^0(X;G)=0$.

::: pf-proof
By definition $H_c^0(X;G)=\varinjlim_{K}H^0(X,X\setminus K;G)$, the direct limit over the compact subsets ordered by inclusion, with the maps induced by inclusions of pairs. Every group in the system is zero by step [](#sequence){.pf-ref}, so every structure map is the zero map, and a direct limit of zero groups is zero.
:::

:::

::: {.pf-step}
$H_c^0(X;G)=0$ whenever $X$ is path-connected and noncompact, as claimed.

::: pf-proof
This is step [](#limit){.pf-ref}. Both hypotheses are used: path-connectedness makes the restriction injective rather than merely having kernel the global sections, and noncompactness places every compact set in a proper position so that the complement is nonempty at every index of the limit.
:::

:::

:::

:::
