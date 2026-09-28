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
For $g\in G$, let $c_g\in\Inn(G)$ denote conjugation by $g$:
\[
c_g(x)=gxg^{-1}.
\]
Take $\phi\in\Aut(G)$. Then for every $x\in G$,
\[
(\phi c_g\phi^{-1})(x)
=\phi\bigl(g\phi^{-1}(x)g^{-1}\bigr)
=\phi(g)x\phi(g)^{-1}
=c_{\phi(g)}(x).
\]
Thus
\[
\phi c_g\phi^{-1}=c_{\phi(g)}\in\Inn(G).
\]
Hence $\phi\Inn(G)\phi^{-1}\subseteq\Inn(G)$ for every $\phi\in\Aut(G)$. Applying the same inclusion to $\phi^{-1}$ gives equality, so $\Inn(G)\normal\Aut(G)$.
:::
