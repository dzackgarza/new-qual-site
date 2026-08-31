---
schema: qual/card@1
id: P-APASP07F
kind: problem
title: "Schur function products and decomposition of simple S_5 modules"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
(a) Expand the product of Schur functions $s_{(2)} \cdot s_{(1)}$ into a linear combination of Schur functions for all Young diagrams $\lambda$ with three boxes.

(b) Decompose the simple $S_5$-module $V_{(3,2)}$ into a direct sum of simple $S_3 \times S_2$-modules, with $S_3$ permuting the letters $\{1, 2, 3\}$ and $S_2$ permuting the letters $\{4, 5\}$.

(c) Determine the decomposition of $V_{(3,2)}$ as a direct sum of simple $S_3$-modules and give the structure (i.e.\ decomposition into simple matrix algebras) of the commutant of the $S_3$-action on $V_{(3,2)}$.
:::

::: {.solution}
**Goal.** Expand $s_{(2)}s_{(1)}$, decompose $V_{(3,2)}$ as an $S_3 \times S_2$-module and as an $S_3$-module, and describe the commutant.

<1>1. (a) $s_{(2)} \cdot s_{(1)} = s_{(3)} + s_{(2,1)}$.
<2>1. By the Pieri rule, $s_{(2)} s_{(1)}$ is the sum of $s_\lambda$ over all $\lambda$ obtained by adding one box to $(2)$.
::: {.proof}
the Pieri rule: multiplying by $s_{(1)}$ adds a single box in all ways yielding a valid Young diagram.
:::
<2>2. Adding one box to $(2)$ gives $(3)$ and $(2,1)$.
::: {.proof}
the box can go in row 1 (giving $(3)$) or row 2 (giving $(2,1)$).
:::

<1>2. (b) $V_{(3,2)} \downarrow S_3 \times S_2 = (V_{(3)} \boxtimes V_{(1,1)}) \oplus (V_{(2,1)} \boxtimes V_{(2)}) \oplus (V_{(2,1)} \boxtimes V_{(1,1)})$.
<2>1. The multiplicity of $V_\mu \boxtimes V_\nu$ in $V_\lambda \downarrow S_{n_1} \times S_{n_2}$ is the Littlewood–Richardson coefficient $c^\lambda_{\mu\nu}$.
::: {.proof}
the branching rule for $S_{n_1} \times S_{n_2} \le S_{n_1 + n_2}$.
:::
<2>2. For $\lambda = (3,2)$, the pairs $(\mu, \nu)$ with $\mu \vdash 3$, $\nu \vdash 2$, $\mu, \nu \subseteq \lambda$, and $c^{(3,2)}_{\mu\nu} \neq 0$ are $((3), (1,1))$, $((2,1), (2))$, $((2,1), (1,1))$, each with coefficient $1$.
::: {.proof}
compute the skew shapes $(3,2)/\mu$ and count LR tableaux of content $\nu$: $(3,2)/(3)$ is a column of two boxes (content $(1,1)$); $(3,2)/(2,1)$ is two boxes in distinct rows and columns (contents $(2)$ and $(1,1)$ each give one tableau).
:::
<2>3. Dimension check: $\dim V_{(3,2)} = 5 = 1\cdot 1 + 2\cdot 1 + 2\cdot 1$.
::: {.proof}
hook-length formula gives $\dim V_{(3,2)} = 5$, $\dim V_{(3)} = 1$, $\dim V_{(1,1)} = 1$, $\dim V_{(2,1)} = 2$, $\dim V_{(2)} = 1$.
:::

<1>3. (c) $V_{(3,2)} \downarrow S_3 = V_{(3)} \oplus 2 V_{(2,1)}$.
<2>1. Restrict the $S_3 \times S_2$ decomposition to $S_3$ (forgetting the $S_2$ factor).
::: {.proof}
$V_{(3)} \boxtimes V_{(1,1)}$ restricts to $V_{(3)}$; each $V_{(2,1)} \boxtimes V_{(\cdot)}$ restricts to $V_{(2,1)}$.
:::
<2>2. Hence $V_{(3,2)} \downarrow S_3 = V_{(3)} \oplus V_{(2,1)} \oplus V_{(2,1)}$.
::: {.proof}
collect the three terms from <1>2.2.
:::

<1>4. The commutant of the $S_3$-action is $\CC \oplus M_2(\CC)$.
<2>1. The commutant is $\operatorname{End}_{S_3}(V_{(3,2)})$.
::: {.proof}
definition of the commutant.
:::
<2>2. By Schur's lemma and the decomposition $V_{(3)} \oplus 2 V_{(2,1)}$, the commutant is $M_1(\CC) \oplus M_2(\CC)$.
::: {.proof}
$V_{(3)}$ appears with multiplicity $1$ and $V_{(2,1)}$ with multiplicity $2$, so the endomorphism algebra is $\operatorname{End}(V_{(3)}) \oplus \operatorname{End}(\CC^2) = \CC \oplus M_2(\CC)$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>1, <1>2, <1>3, <1>4 answer (a), (b), (c).
:::
:::
