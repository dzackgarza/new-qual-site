---
schema: qual/card@1
id: E-QWNYJ
kind: problem
title: Countable products of separable spaces are separable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Amit Rajaraman, "Munkres Solutions" (MA 406
    course notes, last updated 31 March 2021), Exercise 4.30.10, printed p. 13
    (tmp/sources/munkres-solutions-amitrajaraman-ma406.pdf), checked against Munkres, Topology
    (2000), Section 30 Exercise 10, printed p. 194. His construction is the one on the card: a
    point of the product is in D when every coordinate is in the chosen countable dense set and
    all but finitely many coordinates equal the chosen base point, which is a countable union of
    countable sets, and density is read off a basis element that restricts finitely many
    coordinates. What was added: the empty-factor case, which he does not mention and which the
    card settles first. "Doug's World", printed p. 3, leaves Problem 30.10 with an empty solution.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the construction into numbered steps: the empty-factor case, the choice of the
    countable dense sets and basepoints, the countability of D as a countable union over finite F of
    countable products, and density against a basic open set that restricts finitely many
    coordinates. All mathematics is the earlier transcription's; nothing needed correction. Not
    re-read this session: the Rajaraman page, printed p. 13, and Munkres printed p. 194.
---

::: {.exercise}

Show that if $X$ is a countable product of spaces having countable dense subsets, then $X$ has a countable dense subset.
:::

::: {.solution}

The construction is that of **Amit Rajaraman, "Munkres Solutions" (MA 406 course notes, last updated 31 March 2021), Exercise 4.30.10, printed p. 13** (`tmp/sources/munkres-solutions-amitrajaraman-ma406.pdf`), with the empty-factor case added. The statement was checked against Munkres, *Topology* (2000), §30 Exercise 10, printed p. 194.

Let $X=\prod_{n=1}^{\infty}X_{n}$ carry the product topology, in which a basis consists of the sets $\prod U_{n}$ with $U_{n}$ open in $X_{n}$ and $U_{n}=X_{n}$ for all but finitely many $n$.

::: pf

::: {.pf-step #empty}
If some factor $X_{n}$ is empty, then $X$ is empty and separable.

::: pf-proof
A product with an empty factor is empty, having no element. The empty set is countable and dense in itself: its closure is empty, which is the whole space.
:::

:::

::: {.pf-step #data}
Otherwise each $X_{n}$ is nonempty, has a countable dense subset $D_{n}$, and one may choose a point $a_{n}\in D_{n}$.

::: pf-proof
Each $X_{n}$ has a countable dense subset by hypothesis, and a dense subset of a nonempty space is nonempty, since otherwise its closure would be empty. So $D_{n}\neq\varnothing$ and one element $a_{n}$ of it is chosen for each $n$, one choice from each of countably many specified nonempty countable sets.
:::

:::

::: {.pf-step #countable}
$D=\{x\in X\mid x_{n}\in D_{n}\ \text{for all }n,\ x_{n}=a_{n}\ \text{for all but finitely many }n\}$ is countable.

::: pf-proof
For a finite $F\subset\ZZ_{+}$ put $D_{F}=\{x\in X\mid x_{n}\in D_{n}\text{ for }n\in F,\ x_{n}=a_{n}\text{ for }n\notin F\}$, which is in bijection with $\prod_{n\in F}D_{n}$ and so is countable, a finite product of countable sets being countable. Then $D=\bigcup_{F}D_{F}$ over the countably many finite subsets $F$ of $\ZZ_{+}$, so $D$ is a countable union of countable sets.
:::

:::

::: {.pf-step #dense}
$D$ is dense in $X$.

::: pf-proof
Let $V=\prod U_{n}$ be a nonempty basic open set, with $F=\{n\mid U_{n}\neq X_{n}\}$ finite and every $U_{n}$ nonempty. For $n\in F$ the set $D_{n}$ is dense, so $D_{n}\cap U_{n}\neq\varnothing$; pick $d_{n}\in D_{n}\cap U_{n}$. Define $x$ by $x_{n}=d_{n}$ for $n\in F$ and $x_{n}=a_{n}$ otherwise; then $x\in D$ and $x_{n}\in U_{n}$ for every $n$, so $x\in V$. Hence every nonempty basic open set, and therefore every nonempty open set, meets $D$.
:::

:::

::: {.pf-step}
$X$ has a countable dense subset.

::: pf-proof
In the case of step [](#empty){.pf-ref} the space is empty and separable; otherwise the set $D$ of step [](#countable){.pf-ref} is countable and dense by step [](#dense){.pf-ref}.
:::

:::

:::

:::
