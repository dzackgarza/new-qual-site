---
schema: qual/card@1
id: E-AMD-3LUW3P7R
kind: exercise
title: $\Inn(G)$ is normal in $\Aut(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that $\Inn(G) \normal \Aut(G)$.
:::

::: {.solution}
Let $G$ be a group. Recall that:
- $\Aut(G)$ is the group of all automorphisms of $G$ under composition.
- $\Inn(G) = \{\gamma_g : g \in G\}$, where $\gamma_g \in \Aut(G)$ is the inner automorphism defined by conjugation:
  $$
  \gamma_g(x) = g x g^{-1} \quad \text{for all } x \in G.
  $$

To show that $\Inn(G)$ is a normal subgroup of $\Aut(G)$, we need to verify that for every $\phi \in \Aut(G)$ and every inner automorphism $\gamma_g \in \Inn(G)$, the conjugated automorphism $\phi \circ \gamma_g \circ \phi^{-1}$ is also an inner automorphism in $\Inn(G)$.

Let $x \in G$. Evaluating the composition:
$$
(\phi \circ \gamma_g \circ \phi^{-1})(x) = \phi(\gamma_g(\phi^{-1}(x))) = \phi\left( g \phi^{-1}(x) g^{-1} \right).
$$
Since $\phi$ is a group homomorphism:
$$
\phi\left( g \phi^{-1}(x) g^{-1} \right) = \phi(g) \phi(\phi^{-1}(x)) \phi(g^{-1}) = \phi(g) x (\phi(g))^{-1}.
$$
Since $\phi \in \Aut(G)$ is an automorphism, $\phi(g)$ is an element of $G$.
Setting $h = \phi(g) \in G$, we see that:
$$
(\phi \circ \gamma_g \circ \phi^{-1})(x) = h x h^{-1} = \gamma_h(x) = \gamma_{\phi(g)}(x).
$$
Therefore:
$$
\phi \circ \gamma_g \circ \phi^{-1} = \gamma_{\phi(g)} \in \Inn(G).
$$

Since $\phi \circ \gamma_g \circ \phi^{-1} \in \Inn(G)$ for all $\phi \in \Aut(G)$ and $\gamma_g \in \Inn(G)$, we conclude that:
$$
\Inn(G) \normal \Aut(G).
$$
*(The quotient group $\Aut(G)/\Inn(G)$ is the outer automorphism group $\operatorname{Out}(G)$.)*
:::
