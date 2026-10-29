---
schema: qual/card@1
id: P-PRACT20-W5-11
kind: problem
title: Kernels of homomorphisms are normal subgroups
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 11).
---

::: {.problem}
Let $G$ be a group and $H \subset G$ be a subgroup. $H$ is said to be a normal subgroup of $G$ if $ghg^{-1} \in H$ whenever $h \in H$ and $g \in G$. If $\phi : G \to G'$ is a homomorphism (where $G'$ is some other arbitrary group), show that $\ker \phi$ is a normal subgroup of $G$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The set
$$
\ker\phi=\{x\in G:\phi(x)=e_{G'}\}
$$
is a subgroup of $G$.


::: pf-proof

The identity belongs to the kernel because
$$
\phi(e_G)=e_{G'}.
$$
If $x,y\in\ker\phi$, then
$$
\phi(xy^{-1})
=\phi(x)\phi(y)^{-1}
=e_{G'}e_{G'}^{-1}
=e_{G'}.
$$
Thus $xy^{-1}\in\ker\phi$. By the subgroup test,
$$
\ker\phi\le G.
$$

:::

:::

::: {.pf-step #s1-2}

For every $h\in\ker\phi$ and every $g\in G$,
$$
ghg^{-1}\in\ker\phi.
$$


::: pf-proof

Since $h\in\ker\phi$,
$$
\phi(h)=e_{G'}.
$$
Therefore
$$
\begin{aligned}
\phi(ghg^{-1})
&=\phi(g)\phi(h)\phi(g)^{-1}\\
&=\phi(g)e_{G'}\phi(g)^{-1}\\
&=e_{G'}.
\end{aligned}
$$
Hence $ghg^{-1}$ belongs to the kernel.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{\ker\phi\trianglelefteq G}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} shows that the kernel is a subgroup, and step [](#s1-2){.pf-ref} verifies the
defining conjugation condition for normality.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
