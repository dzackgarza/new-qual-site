---
schema: qual/card@1
id: P-TOPS17C
kind: problem
title: 'Homology of the mapping torus as the cokernel of $\mathrm{id}-f_*$'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mapping Torus
  - Exact Sequences
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The card asked to prove $H_1(X)\cong H_1(Y)/\operatorname{im}(\operatorname{id}-f_*)$ for any space $Y$, which fails for $Y$ a point. The statement now assumes $Y$ path-connected and adds the summand $\ZZ$.
---

::: {.problem}
Let $Y$ be a path-connected space, let $f : Y \to Y$ be a self-mapping of $Y$, and let $X$ be the mapping torus of $f$, that is, the space obtained from $Y \times I$ by identifying $(y, 1) \sim (f(y), 0)$ for each point $y \in Y$.
Prove that $H_1(X; \ZZ) \cong H_1(Y; \ZZ) / \operatorname{im}(\operatorname{id} - f_*) \oplus \ZZ$, where $f_*$ is the induced map $H_1(Y; \ZZ) \to H_1(Y; \ZZ)$.
:::

::: {.solution}

::: pf

::: {.pf-step #wang-exact-sequence}
There is a Wang exact sequence
$$
H_1(Y)\xrightarrow{\operatorname{id}-f_*}H_1(Y)\longrightarrow H_1(X)\longrightarrow
H_0(Y)\xrightarrow{\operatorname{id}-f_*}H_0(Y).
$$

::: pf-proof
View the mapping torus as the homotopy coequalizer of $\operatorname{id}_Y$ and $f$. Its standard mapping-cone chain model is the cone of $\operatorname{id}-f_*:C_*(Y)\to C_*(Y)$, shifted in the usual way. The associated long exact homology sequence is precisely the displayed Wang sequence.
:::

:::

::: {.pf-step #short-exact-sequence-coker-ker}
Consequently there is a short exact sequence
$$
0\to \operatorname{coker}(\operatorname{id}-f_*:H_1(Y)\to H_1(Y))
\to H_1(X)
\to \ker(\operatorname{id}-f_*:H_0(Y)\to H_0(Y))\to0.
$$

::: pf-proof
Take the exact portion in step [](#wang-exact-sequence){.pf-ref} and identify the kernel and cokernel at the adjacent terms.
:::

:::

::: pf-step
Since $Y$ is path-connected, $f_*$ is the identity on $H_0(Y)\cong\ZZ$, so
$$
\boxed{H_1(X;\ZZ)\cong
H_1(Y;\ZZ)/\operatorname{im}(\operatorname{id}-f_*)\oplus\ZZ.}
$$

::: pf-proof
The kernel on $H_0$ is then all of $\ZZ$. The short exact sequence in step [](#short-exact-sequence-coker-ker){.pf-ref} splits because $\ZZ$ is free abelian.
:::

:::

:::

:::
