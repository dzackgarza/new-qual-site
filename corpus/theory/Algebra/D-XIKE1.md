---
schema: qual/card@1
id: D-XIKE1
kind: definition
title: Outer automorphism group
prompts:
- What is the outer automorphism group of a group?
- When is every automorphism of a group inner?
classification:
  areas: [algebra]
  topics: [Automorphisms, Quotient Groups]
relations:
- kind: uses
  target: PR-IN9ZP
review: draft
---

::: {.definition}
Let $G$ be a group with automorphism group $\Aut(G)$ and [[PR-IN9ZP|inner automorphism group]] $\Inn(G)$.
An \dfn{outer automorphism} of $G$ is a coset of $\Inn(G)$ in $\Aut(G)$, and the \dfn{outer automorphism group} is the quotient group
$$
\Out(G)\coloneqq\Aut(G)/\Inn(G).
$$
:::

::: {.remark}
The quotient is a group because $\Inn(G)$ is normal in $\Aut(G)$: conjugation by an automorphism $\alpha$ sends $c_g$ to $c_{\alpha(g)}$.
Every automorphism of $G$ is inner exactly when $\Out(G)$ is trivial, so $\Out(G)$ measures the automorphisms that no element of $G$ accounts for.
:::
