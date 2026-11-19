---
schema: qual/card@1
id: P-FKAJJ
kind: problem
title: Orbit-stabilizer bijection $G/G_x\simeq G\cdot x$, and nontriviality of $Z(G)$
  for finite $p$-groups
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Group Actions
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-18
  note: Read against the UGA Algebra Qualifying Exam, Spring 2016, Problem 4; both parts match.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The statement and title wrote $p\dash$group, from an extraction of the source's
    "$p$-group"; corrected to $p$-group in both. No mathematical change.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    No retained solution set covers this examination. Structured the card's own proof:
    well-definedness, surjectivity and injectivity of $gG_x\mapsto g\cdot x$; then the
    conjugation action, the identification of fixed points with $Z(G)$ and of stabilizers
    with centralizers, and the class-equation divisibility argument.
---

::: {.problem}
Let $G$ be a finite group acting on a set $X$.
For $x\in X$, let $G_x$ be the stabilizer of $x$ and $G\cdot x$ be the orbit of $x$.

a. Prove that there is a bijection between the left cosets $G/G_x$ and $G\cdot x$.

b. Prove that the center of every finite $p$-group $G$ is nontrivial by considering that action of $G$ on $X=G$ by conjugation.
:::

::: {.solution}

No retained solution set covers this examination; the argument below is the card's own.

::: pf

::: {.pf-step #well-defined}
The map $\Phi(gG_x)=g\cdot x$ is well defined.

::: pf-proof
If $gG_x=hG_x$, then $h^{-1}g\in G_x$, so $(h^{-1}g)\cdot x=x$ and hence $g\cdot x=h\cdot x$.
:::
:::

::: {.pf-step #bijection}
$\Phi$ is a bijection $G/G_x\to G\cdot x$.

::: pf-proof
Surjectivity is the definition of the orbit. If $g\cdot x=h\cdot x$, then $(h^{-1}g)\cdot x=x$, so $h^{-1}g\in G_x$ and $gG_x=hG_x$; hence $\Phi$ is injective. Therefore $\cardinality{G\cdot x}=[G:G_x]$.
:::
:::

::: {.pf-step #conjugation-action}
For the conjugation action of $G$ on $X=G$, the fixed points are exactly $Z(G)$ and the stabilizer of $x$ is the centralizer $C_G(x)$.

::: pf-proof
$g\cdot x=x$ means $gxg^{-1}=x$, that is $gx=xg$; the elements fixing every $x$ are exactly the central elements. The stabilizer consists of those $g$ with $gxg^{-1}=x$, which is the definition of $C_G(x)$.
:::
:::

::: {.pf-step #class-equation}
Every non-singleton conjugacy class has size divisible by $p$.

::: pf-proof
For $x\notin Z(G)$, the class has $\cardinality{G\cdot x}=[G:C_G(x)]$ by step [](#bijection){.pf-ref}; a subgroup of a $p$-group has index a power of $p$, and the index exceeds $1$ for a non-central element, so $p$ divides the class size.
:::
:::

::: {.pf-step #center-nontrivial}
$Z(G)$ is nontrivial.

::: pf-proof
The class equation
$$
\cardinality G=\cardinality{Z(G)}+\sum_i\cardinality{\mathcal C_i}
$$
sums the non-central classes, each divisible by $p$ by step [](#class-equation){.pf-ref}. Since $p$ divides $\cardinality G$, it divides $\cardinality{Z(G)}$. The identity lies in $Z(G)$, so $\cardinality{Z(G)}\ge p$ and $Z(G)\ne\{e\}$.
:::
:::

:::
:::
