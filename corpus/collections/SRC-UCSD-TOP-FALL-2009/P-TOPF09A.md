---
schema: qual/card@1
id: P-TOPF09A
kind: problem
title: "Fundamental group of a topological group is abelian"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Topological Groups
relations: []
review: draft
---

::: {.problem}
Show that the fundamental group, based at the identity, of a topological group $G$ is abelian.
:::

::: {.solution}

::: pf

::: pf-step

On based loops $\alpha,\beta:I\to G$ at the identity $e$, there are two products: concatenation $\alpha*\beta$ and pointwise multiplication
$$
(\alpha\cdot\beta)(t)=\alpha(t)\beta(t).
$$

::: pf-proof

Pointwise multiplication is again a loop at $e$ because $\alpha(0)=\alpha(1)=\beta(0)=\beta(1)=e$.

:::

:::

::: pf-step

These operations satisfy the interchange law
$$
(\alpha*\beta)\cdot(\gamma*\delta)\simeq
(\alpha\cdot\gamma)*(\beta\cdot\delta)
$$
through based loops.

::: pf-proof

Using the standard half-interval parametrization of concatenation, both sides are represented by the same loop: on the first half multiply $\alpha$ with $\gamma$, and on the second half multiply $\beta$ with $\delta$. Any difference from reparametrization is a based homotopy.

:::

:::

::: pf-step

Both operations have the constant loop as unit on homotopy classes.

::: pf-proof

This is immediate for pointwise multiplication; for concatenation the constant loop is a unit up to the standard reparametrization homotopy.

:::

:::

::: {.pf-step #s4}

By the Eckmann--Hilton argument, the two products agree on $\pi_1(G,e)$ and are commutative.

::: pf-proof

For classes $x,y$ and common unit $1$,
$$
x*y=(x\cdot1)*(1\cdot y)=(x*1)\cdot(1*y)=x\cdot y,
$$
and similarly
$$
x*y=x\cdot y=(1*x)\cdot(y*1)=(1\cdot y)*(x\cdot1)=y*x.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{\pi_1(G,e)\text{ is abelian}.}
$$

::: pf-proof

The group operation on $\pi_1$ is concatenation, which is commutative by step [](#s4){.pf-ref}.

:::

:::

:::

:::
