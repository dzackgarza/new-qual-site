---
schema: qual/card@1
id: E-AMD-NY3QKBRB
kind: problem
title: Kernel of conjugation $G\to\Aut(G)$ is $Z(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Centralizers and Normalizers
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The four steps of the equivalence chain each asserted their claim with no justification and now carry
    one: the kernel as a preimage of the identity automorphism, the passage from equality of maps to a
    pointwise identity, the cancellation of $g\inverseof{g}$ after multiplying by $g$, and the definition
    of the centre. Also removed the closing pf-qed, which said only that the single step above is the
    equality of subsets, which STYLE-08 does not admit. The statement is unchanged. The card stands alone,
    with no collection provenance and no retained published solution, so the argument is the card's own.
---

::: {.exercise}
Let $G$ be a group. Show that the kernel of the map $G\to \Aut(G)$ given by $g\mapsto (h\mapsto gh\inverseof{g})$ is $Z(G)$.
:::

::: {.solution}
Write $\varphi: G \to \Aut(G)$ for the map $\varphi(g) = c_g$, where $c_g(h) = gh\inverseof{g}$.

::: pf

::: {.pf-step #kernel-iff-center}
$g \in \ker \varphi$ if and only if $g \in Z(G)$.

::: pf-proof

::: {.pf-step #kernel-set}
$\ker \varphi = \theset{ g \in G \st c_g = \id_G }$, since the identity of $\Aut(G)$ is the identity automorphism.

::: pf-proof
By definition $\ker \varphi = \{g \in G : \varphi(g) = e\}$, where $e$ is the identity of $\Aut(G)$. The group $\Aut(G)$ has composition as its operation, so its identity is the identity map $\id_G$ of $G$, and therefore $\varphi(g) = e$ is the same condition as $c_g = \id_G$.
:::

:::

::: {.pf-step #pointwise}
$c_g = \id_G$ says $gh\inverseof{g} = h$ for every $h \in G$.

::: pf-proof
Two maps $G \to G$ are equal exactly when they agree at every point. The map $c_g$ sends $h$ to $gh\inverseof{g}$ and the identity map sends $h$ to $h$, so $c_g = \id_G$ says $gh\inverseof{g} = h$ for every $h \in G$.
:::

:::

::: {.pf-step #commutes}
Multiplying on the right by $g$, this is equivalent to $gh = hg$ for every $h \in G$.

::: pf-proof
Right multiplication by $g$ is a bijection of $G$, so $gh\inverseof{g} = h$ if and only if $gh\inverseof{g}\,g = hg$, and $g\inverseof{g}$ is the identity, so the left-hand side is $gh$. Hence the condition of step [](#pointwise){.pf-ref} is equivalent to $gh = hg$ for every $h \in G$.
:::

:::

::: {.pf-step #center}
That is the defining condition for $g \in Z(G)$.

::: pf-proof
The centre is $Z(G) = \{g \in G : gh = hg \text{ for every } h \in G\}$ by definition, and the condition established in step [](#commutes){.pf-ref} is exactly membership in that set.
:::

:::

:::

:::

:::

:::
