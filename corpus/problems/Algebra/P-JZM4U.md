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

::: {.problem}
State the class equation and derive it from orbit-stabilizer.
:::

::: {.solution}
Let a finite group $G$ act on itself by conjugation, $g\cdot x=gxg^{-1}$, and write $\operatorname{Cl}_G(x)$ for the conjugacy class of $x$.

::: pf

::: {.pf-step #orbit-stabilizer}

$\abs{\operatorname{Cl}_G(x)}=[G:C_G(x)]$ for every $x\in G$.

::: pf-proof

The orbit of $x$ is $\operatorname{Cl}_G(x)$ and its stabilizer is the centralizer $C_G(x)=\{g\in G:gx=xg\}$. Apply the orbit-stabilizer theorem.

:::

:::

::: {.pf-step #central}

$\abs{\operatorname{Cl}_G(x)}=1$ if and only if $x\in Z(G)$.

::: pf-proof

By step [](#orbit-stabilizer){.pf-ref}, $\abs{\operatorname{Cl}_G(x)}=1$ if and only if $C_G(x)=G$, that is, $x$ commutes with every element of $G$.

:::

:::

::: pf-step

If $x_1,\ldots,x_k$ represent the noncentral conjugacy classes, then
$$
\boxed{\abs{G}=\abs{Z(G)}+\sum_{i=1}^k[G:C_G(x_i)].}
$$

::: pf-proof

The conjugacy classes partition $G$. By step [](#central){.pf-ref}, the classes of size $1$ are the singletons $\{z\}$ with $z\in Z(G)$, and by step [](#orbit-stabilizer){.pf-ref} the remaining classes have sizes $[G:C_G(x_i)]$.

:::

:::

:::

:::
