---
schema: qual/card@1
id: P-AMD-2AFAX7LD
kind: problem
title: $S^3 - \{p_0, p_1\} \simeq S^2$
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that $S^3 - \{p_0, p_1\} \simeq S^2$
:::

::: {.solution}
**Goal:** Prove that the complement of two distinct points in the 3-sphere, $S^3 \setminus \{p_0, p_1\}$, is homotopy equivalent to $S^2$.

::: pf

::: {.pf-step #s1}
$S^3 \setminus \{p_0\}$ is homeomorphic to $\mathbb{R}^3$.

::: pf-proof

::: pf-step
Standard stereographic projection from the pole $p_0$ gives a homeomorphism $\phi \colon S^3 \setminus \{p_0\} \to \mathbb{R}^3$.

::: pf-proof
Stereographic projection is a bijection with an explicit formula, and both it and its inverse are continuous, so it is a homeomorphism.
:::

:::

:::

:::

::: pf-step
Under the homeomorphism $\phi$, $S^3 \setminus \{p_0, p_1\}$ is homeomorphic to $\mathbb{R}^3 \setminus \{\phi(p_1)\}$.

::: pf-proof
A homeomorphism $\phi \colon X \to Y$ restricts to a homeomorphism $X \setminus \{x\} \to Y \setminus \{\phi(x)\}$ for any point $x \in X$.
Here $X = S^3 \setminus \{p_0\}$ and $x = p_1 \in X$ since $p_1 \neq p_0$.
:::

:::

::: pf-step
$\mathbb{R}^3 \setminus \{\phi(p_1)\}$ is homeomorphic to $\mathbb{R}^3 \setminus \{0\}$.

::: pf-proof

::: pf-step
Translation by $-\phi(p_1)$, given by $v \mapsto v - \phi(p_1)$, is a homeomorphism of $\mathbb{R}^3$ that maps $\phi(p_1)$ to the origin $0$.
:::

::: pf-step
Restricting this homeomorphism to $\mathbb{R}^3 \setminus \{\phi(p_1)\}$ gives a homeomorphism onto $\mathbb{R}^3 \setminus \{0\}$.
:::

:::

:::

::: pf-step
$\mathbb{R}^3 \setminus \{0\}$ deformation retracts to the unit sphere $S^2$.

::: pf-proof

::: pf-step
Let $r \colon \mathbb{R}^3 \setminus \{0\} \to S^2$ be defined by $r(x) = \frac{x}{\|x\|}$ and let $\iota \colon S^2 \hookrightarrow \mathbb{R}^3 \setminus \{0\}$ be the inclusion.
:::

::: pf-step
The map $r$ is continuous and restricts to the identity on $S^2$ because for any $x \in S^2$, $\|x\| = 1 \implies r(x) = x$.
:::

::: pf-step
Define $H \colon (\mathbb{R}^3 \setminus \{0\}) \times [0, 1] \to \mathbb{R}^3 \setminus \{0\}$ by $H(x, t) = (1-t)x + t \frac{x}{\|x\|}$.
:::

::: pf-step
For all $x \in \mathbb{R}^3 \setminus \{0\}$ and $t \in [0, 1]$, $(1-t) + \frac{t}{\|x\|} > 0$, so $H(x, t) \neq 0$.
Thus $H$ is a well-defined continuous map into $\mathbb{R}^3 \setminus \{0\}$.
:::

::: {.pf-step #s4-5}
$H(x, 0) = x = \operatorname{id}_{\mathbb{R}^3 \setminus \{0\}}(x)$, $H(x, 1) = \iota(r(x))$, and for every $s \in S^2$ and $t \in [0, 1]$, $H(s, t) = s$.

::: pf-proof
The three identities in step [](#s4-5){.pf-ref} are exactly the defining conditions of a strong deformation retraction: $H(\cdot, 0) = \operatorname{id}$, $H(\cdot, 1) = \iota \circ r$, and $H$ fixes $S^2$ pointwise throughout.
:::

:::

:::

:::

::: {.pf-step #s5}
Homotopy equivalence is an equivalence relation preserved under homeomorphisms.

::: pf-proof

::: pf-step
Every homeomorphism is a homotopy equivalence, and a deformation retraction is a homotopy equivalence.
:::

::: pf-step
Composing homotopy equivalences yields a homotopy equivalence: $$S^3 \setminus \{p_0, p_1\} \cong \mathbb{R}^3 \setminus \{\phi(p_1)\} \cong \mathbb{R}^3 \setminus \{0\} \simeq S^2.$$
:::

:::

:::

::: pf-qed
Combining steps [](#s1){.pf-ref} through [](#s5){.pf-ref} establishes $S^3 \setminus \{p_0, p_1\} \simeq S^2$.
:::

:::
:::
