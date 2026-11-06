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
Let $G$ be a group and $X$ a set.

A group action of $G$ on $X$ is a map
$$
G\times X\to X,\qquad (g,x)\mapsto g\cdot x,
$$
such that
$$
e\cdot x=x,
\qquad
(gh)\cdot x=g\cdot(h\cdot x).
$$

The orbit of $x\in X$ is
$$
Gx=\{g\cdot x:g\in G\}.
$$

The stabilizer of $x$ is
$$
G_x=\{g\in G:g\cdot x=x\}.
$$

For $g\in G$, its fixed-point set is
$$
X^g=\{x\in X:g\cdot x=x\}.
$$
The fixed points of the whole action are
$$
X^G=\{x\in X:g\cdot x=x\text{ for every }g\in G\}.
$$
:::
