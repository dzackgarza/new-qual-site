---
schema: qual/card@1
id: D-WYC7C
kind: definition
title: Group actions, orbits, and stabilizers
classification:
  areas:
  - algebra
  topics:
  - groups
relations: []
review: reviewed
---

::: {.definition title="Group action"}
An action of a group $G$ on a set $X$ is a map $G\times X\to X$, written
$(g,x)\mapsto g\cdot x$, such that
$$
e\cdot x=x
\qquad\text{and}\qquad
g\cdot(h\cdot x)=(gh)\cdot x.
$$

For $x\in X$, its **orbit** and **stabilizer** are
$$
G\cdot x=\theset{g\cdot x: g\in G},
\qquad
G_x=\theset{g\in G:g\cdot x=x}.
$$
The fixed-point set is
$X^G=\theset{x\in X:g\cdot x=x\text{ for every }g\in G}$.
:::

Orbits partition $X$. An action is transitive exactly when it has one orbit.
The kernel of the action is the intersection of all point stabilizers.
