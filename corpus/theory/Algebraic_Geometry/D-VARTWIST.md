---
schema: qual/card@1
id: D-VARTWIST
kind: definition
title: Twists of a variety, and quadratic twists of elliptic curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Twists
  - Elliptic Curves
  - Base Change
relations:
- kind: related-to
  target: D-CRVMOD
review: draft
prompts:
- What is a twist of a variety?
- When is the quadratic twist of an elliptic curve isomorphic to the curve?
---

::: {.definition title="Twist"}
Let $X$ be a variety over a field $k$.
A \dfn{twist} of $X$ is a variety $T$ over $k$ such that $T \times_k \Spec K \cong X \times_k \Spec K$ as $K$-varieties for some field extension $K/k$.
:::

::: {.example title="Quadratic twists"}
Let $k$ be a field of characteristic not $2$, $f \in k[x]$ a monic cubic without repeated roots, $E \colon y^2 = f(x)$, and $d \in k^\times$.
The \dfn{quadratic twist} $E_d \colon d y^2 = f(x)$ is a twist of $E$: over $K = k(\sqrt{d})$, the substitution $y \mapsto \sqrt{d}\, y$ is an isomorphism $E_d \times_k K \to E \times_k K$.
:::

::: {.proposition}
Let $E$ and $d$ be as above.
If $d \in (k^\times)^2$, then $E_d \cong E$ over $k$.
If $j(E) \neq 0, 1728$ and $d \notin (k^\times)^2$, then $E_d \not\cong E$ over $k$.
:::

::: {.example}
The hypothesis on $j$ is needed.
For $E \colon y^2 = x^3 - x$, with $j(E) = 1728$, and $d = -1$, the twist $E_{-1} \colon -y^2 = x^3 - x$ is isomorphic to $E$ over every field $k$ of characteristic not $2$, by $(x, y) \mapsto (-x, y)$, whether or not $-1$ is a square in $k$.
:::
