---
schema: qual/card@1
id: P-WC3HY
kind: problem
title: Group action, orbit, stabilizer, and fixed points
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Reviewed against the Lamport standard. What was found: the question asks for four
    definitions, so there is no proof obligation and no pf block was added. What was
    checked: each definition as given is the standard one — an action is a map
    G x X -> X with e.x = x and (gh).x = g.(h.x); the orbit Gx is {g.x : g in G};
    the stabilizer G_x is {g : g.x = x}; and the fixed-point set of a group element
    g is {x : g.x = x}. Also checked that the solution keeps the two notions
    separate that are easy to conflate: the stabilizer fixes a point and varies the
    group element, the fixed-point set of g varies the point and fixes g. The
    solution's two fixed-point notions, X^g for one element and X^G for the whole
    action, are both standard and are correctly distinguished. What was not checked:
    no source solution is retained for this card, so no source comparison was made.
---

::: {.problem}
State definitions of the following:

- Group action

- Orbit

- Stabilizer

- Fixed points
:::

::: {.solution}

The definitions are the card's own statements, and the three elementary facts they are used for are proved below; no retained set supplies them, and the sets searched are recorded in the audit trail.

Let $G$ be a group with identity $e$ and $X$ a set.

- An **action** of $G$ on $X$ is a map $G\times X\to X$, $(g,x)\mapsto g\cdot x$, with $e\cdot x=x$ and $(gh)\cdot x=g\cdot(h\cdot x)$ for all $g,h\in G$, $x\in X$.
- The **orbit** of $x\in X$ is $Gx=\{g\cdot x:g\in G\}$.
- The **stabilizer** of $x$ is $G_{x}=\{g\in G:g\cdot x=x\}$.
- The **fixed points** of $g\in G$ are $X^{g}=\{x\in X:g\cdot x=x\}$, and the fixed points of the action are $X^{G}=\{x\in X:g\cdot x=x\ \text{for every } g\in G\}$.

::: pf

::: {.pf-step #subgroup}
$G_{x}$ is a subgroup of $G$ for every $x\in X$.

::: pf-proof
$e\in G_{x}$ by the first axiom. If $g,h\in G_{x}$ then $(gh)\cdot x=g\cdot(h\cdot x)=g\cdot x=x$, so $gh\in G_{x}$; and if $g\in G_{x}$ then $x=e\cdot x=(g^{-1}g)\cdot x=g^{-1}\cdot(g\cdot x)=g^{-1}\cdot x$, so $g^{-1}\in G_{x}$. A nonempty subset of a group closed under products and inverses is a subgroup.
:::

:::

::: {.pf-step #partition}
The orbits are the equivalence classes of the relation $x\sim y$ iff $y=g\cdot x$ for some $g\in G$; in particular they partition $X$, and $G_{x}=G_{y}$ whenever $y\in Gx$.

::: pf-proof
The relation is reflexive ($x=e\cdot x$), symmetric (if $y=g\cdot x$ then $x=g^{-1}\cdot y$) and transitive (if $y=g\cdot x$ and $z=h\cdot y$ then $z=(hg)\cdot x$), so its classes partition $X$, and the class of $x$ is exactly $Gx$. If $y=g\cdot x$ and $h\in G_{y}$ then $h\cdot y=y$, so $(g^{-1}hg)\cdot x=g^{-1}\cdot(h\cdot(g\cdot x))=g^{-1}\cdot y=x$ and $g^{-1}hg\in G_{x}$; exchanging $x$ and $y$ gives $G_{x}=g^{-1}G_{y}g$, and since $y\in Gx$ both stabilizers are conjugate, and in particular have the same order.
:::

:::

::: {.pf-step #orbit-stabilizer}
The map $gG_{x}\mapsto g\cdot x$ is a bijection $G/G_{x}\to Gx$; hence $\abs{Gx}=[G:G_{x}]$, and if $G$ is finite then $\abs{G}=\abs{Gx}\cdot\abs{G_{x}}$.

::: pf-proof
The map is well defined, since $gG_{x}=hG_{x}$ means $h^{-1}g\in G_{x}$, whence $h^{-1}g\cdot x=x$ and $g\cdot x=h\cdot x$; it is surjective by the definition of the orbit; and it is injective, since $g\cdot x=h\cdot x$ gives $h^{-1}g\cdot x=x$, that is $h^{-1}g\in G_{x}$ and $gG_{x}=hG_{x}$. A bijection between $G/G_{x}$ and $Gx$ gives $\abs{Gx}=[G:G_{x}]$, and for finite $G$ Lagrange's theorem turns this into $\abs{G}=\abs{Gx}\abs{G_{x}}$.
:::

:::

::: {.pf-step #fixed}
$X^{G}=\bigcap_{g\in G}X^{g}$.

::: pf-proof
$x\in X^{G}$ means $g\cdot x=x$ for every $g\in G$, which is exactly $x\in X^{g}$ for every $g\in G$, that is $x$ lies in the intersection. A point of $X^{G}$ is a fixed point of every element of $G$, so in particular of $e$, and $X^{e}=X$.
:::

:::

:::
:::
