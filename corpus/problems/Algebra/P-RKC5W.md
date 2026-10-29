---
schema: qual/card@1
id: P-RKC5W
kind: problem
title: $\Inn(G)$ is normal in $\Aut(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Normal Subgroups
relations: []
review: draft
---

::: {.problem}
Show that $\Inn(G)\normal\Aut(G)$.
:::

::: {.solution}
For $g\in G$, let $c_g\in\Inn(G)$ be conjugation by $g$, $c_g(x)\coloneqq gxg^{-1}$.

::: pf

::: {.pf-step #conj}
For $\phi\in\Aut(G)$ and $g\in G$, $\phi c_g\phi^{-1}=c_{\phi(g)}$.

::: pf-proof
For every $x\in G$,
$$
(\phi c_g\phi^{-1})(x)
=\phi\bigl(g\phi^{-1}(x)g^{-1}\bigr)
=\phi(g)x\phi(g)^{-1}
=c_{\phi(g)}(x).
$$
:::

:::

::: pf-step
$\Inn(G)\normal\Aut(G)$.

::: pf-proof
$\Inn(G)$ is a subgroup of $\Aut(G)$, the image of the homomorphism $g\mapsto c_g$. By step [](#conj){.pf-ref}, $\phi\Inn(G)\phi^{-1}\subseteq\Inn(G)$ for every $\phi\in\Aut(G)$, which is normality.
:::

:::

:::
:::
