---
schema: qual/card@1
id: P-TOPF23D
kind: problem
title: A fixed-point-free self-map of $S^n$ is homotopic to the antipodal map; a finite group acting freely on $S^{2n}$ has order at most $2$
classification:
  areas:
  - topology
  topics:
  - Fixed Point Theory
  - Antipodal Map
  - Group Actions
  - Spheres
relations: []
review: draft
---

::: {.problem}
Show that a map $f : S^n \to S^n$ which has no fixed points must be homotopic to the antipodal map.
Use this to deduce that a non-trivial finite group acting freely on $S^{2n}$ must be isomorphic to $\ZZ_2$.
:::

::: {.solution}

::: pf

::: pf-step

If $f:S^n\to S^n$ has no fixed point, then
$$H(x,t)=\frac{(1-t)f(x)-tx}{\norm{(1-t)f(x)-tx}}$$
defines a homotopy from $f$ to the antipodal map $x\mapsto-x$.

::: pf-proof

The denominator could vanish only if $(1-t)f(x)=tx$. Since both $f(x)$ and $x$ have norm $1$, this forces $t=1/2$ and $f(x)=x$, contrary to the fixed-point-free hypothesis.

:::

:::

::: {.pf-step #s2}

Therefore every fixed-point-free self-map of $S^n$ has degree
$$(-1)^{n+1}.$$

::: pf-proof

Homotopic maps have the same degree, and the antipodal map on $S^n$ has degree $(-1)^{n+1}$.

:::

:::

::: {.pf-step #s3}

Now let a nontrivial finite group $G$ act freely on $S^{2n}$. Every $g\ne e$ is fixed-point-free, hence
$$\deg g=-1.$$

::: pf-proof

Apply step [](#s2){.pf-ref} with even sphere dimension $2n$.

:::

:::

::: {.pf-step #s4}

There can be at most one nonidentity element of $G$.

::: pf-proof

The degree map $g\mapsto\deg g$ is a homomorphism $G\to\{\pm1\}$, because degree is multiplicative. By step [](#s3){.pf-ref} its kernel is $\{e\}$, so it is injective and $\cardinality{G}\le2$.

:::

:::

::: pf-step

Consequently
$$\boxed{G\cong\ZZ/2.}$$

::: pf-proof

The action is nontrivial, so $G$ has exactly two elements by step [](#s4){.pf-ref}.

:::

:::

:::

:::
