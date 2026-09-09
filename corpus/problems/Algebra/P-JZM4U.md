---
schema: qual/card@1
id: P-JZM4U
kind: problem
title: The class equation
classification:
  areas:
  - algebra
  topics:
  - Class Equation
  - Orbit-Stabilizer
  - Conjugacy
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
State the class equation and derive it from orbit-stabilizer.
:::

::: {.solution}
Let a finite group $G$ act on itself by conjugation,
\[
g\cdot x=gxg^{-1}.
\]
The orbit of $x$ is its conjugacy class, and its stabilizer is its centralizer
\[
C_G(x)=\{g\in G:gx=xg\}.
\]
By orbit-stabilizer,
\[
|\operatorname{Cl}_G(x)|=[G:C_G(x)].
\]

The conjugacy classes partition $G$. The classes of size $1$ are exactly the central elements, because
\[
|\operatorname{Cl}_G(x)|=1
\iff C_G(x)=G
\iff x\in Z(G).
\]
Choosing one representative $x_i$ from each noncentral conjugacy class gives the class equation
\[
|G|=|Z(G)|+\sum_i [G:C_G(x_i)].
\]
:::
