---
schema: qual/card@1
id: P-TOPF19A
kind: problem
title: 'A map $\RR^n\to\RR^n$ at bounded distance from the identity is surjective'
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Point Theory
relations: []
review: draft
---

::: {.problem}
Let $f : \RR^n \to \RR^n$ be a continuous map.
Suppose that there exists a uniform constant $C$ such that $\norm{f(\vec{x}) - \vec{x}} \leq C$ for any $\vec{x} \in \RR^n$.
(Here $\norm{\cdot}$ denotes the standard norm of a vector.)
Prove that $f$ is surjective.
(It would be helpful to start with the simple case $n = 2$.)
:::

::: {.solution}

::: pf

::: pf-step

Fix $y\in\RR^n$ and choose $R>C+\norm{y}$.

::: pf-proof

We will prove that $y$ lies in the image of the restriction of $f$ to the ball $B_R$.

:::

:::

::: {.pf-step #s2}

On the sphere $S_R^{n-1}$, the maps $x\mapsto f(x)-y$ and $x\mapsto x-y$ are homotopic through maps avoiding $0$.

::: pf-proof

Use the straight-line homotopy
$$H_t(x)=(1-t)(x-y)+t(f(x)-y).$$
For $\norm{x}=R$,
$$\norm{H_t(x)-x}\le \norm{y}+t\norm{f(x)-x}<R,$$
so $H_t(x)\ne0$.

:::

:::

::: {.pf-step #s3}

The normalized boundary map
$$x\longmapsto \frac{f(x)-y}{\norm{f(x)-y}}$$
has degree $1$.

::: pf-proof

By step [](#s2){.pf-ref} it is homotopic to the normalized map $x\mapsto(x-y)/\norm{x-y}$. Since $y\in B_R$, the latter has degree $1$.

:::

:::

::: {.pf-step #s4}

Therefore $f(x)=y$ for some $x\in B_R$.

::: pf-proof

If $f(x)\ne y$ on all of $B_R$, then the normalized map $(f-y)/\norm{f-y}$ would extend from $S_R^{n-1}$ to $B_R$, forcing its boundary degree to be $0$, contradicting step [](#s3){.pf-ref}.

:::

:::

::: pf-step

Since $y$ was arbitrary, $f$ is surjective.

::: pf-proof

Apply step [](#s4){.pf-ref} to every $y\in\RR^n$.

:::

:::

:::

:::
