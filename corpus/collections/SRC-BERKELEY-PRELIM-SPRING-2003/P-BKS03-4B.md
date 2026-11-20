---
schema: qual/card@1
id: P-BKS03-4B
kind: problem
title: A nonabelian simple group embeds normally in its automorphism group
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Transcribed from the retained solution sheet — Berkeley preliminary examination, Spring
    2003, solutions, assets/attachments/s03solution.pdf, Problem 4B on PDF p. 5 — and
    restructured into steps. The sheet's last sentence says 'so B is normal in G', which is a
    slip: B is a subgroup of A = Aut(G), and the computation shows alpha B alpha^{-1} = B for
    alpha in A, so the card's 'normal in A' is the correct reading and is kept. Added: the
    verification of the homomorphism law c_{gh} = c_g c_h, and the explicit kernel argument for
    injectivity, which the sheet compressed into 'thus an injection since G is simple'.
---

::: {.problem}
Suppose $G$ is a nonabelian simple group and $A=\operatorname{Aut}(G)$.
Show that $A$ contains a normal subgroup isomorphic to $G$.
:::

::: {.solution}
The argument is the retained solution sheet's: **Berkeley preliminary examination, Spring 2003, solutions** (`assets/attachments/s03solution.pdf`), Problem 4B. Throughout $G$ is nonabelian and simple, $A \coloneqq \Aut(G)$, and $c_{g} \in A$ is conjugation by $g$, $c_{g}(h) = ghg^{-1}$.

::: pf

::: {.pf-step #hom}
$g \mapsto c_{g}$ is a homomorphism $G \to A$, and $c_{g}$ is an automorphism of $G$ for every $g$.

::: pf-proof
For $x \in G$, $c_{gh}(x) = (gh)x(gh)^{-1} = g(hxh^{-1})g^{-1} = c_{g}\bigl(c_{h}(x)\bigr)$, so $c_{gh} = c_{g}\circ c_{h}$ and the map is a homomorphism. Each $c_{g}$ is a group homomorphism with inverse $c_{g^{-1}}$, hence an automorphism.

:::

:::

::: {.pf-step #nontrivial}
The homomorphism $g \mapsto c_{g}$ is not the trivial homomorphism.

::: pf-proof
$G$ is nonabelian, so there are $g, x \in G$ with $gx \ne xg$, that is $c_{g}(x) \ne x$; then $c_{g}$ is not the identity automorphism.

:::

:::

::: {.pf-step #injective}
The homomorphism $g \mapsto c_{g}$ is injective.

::: pf-proof
Its kernel is a normal subgroup of $G$, being the kernel of a homomorphism, and it is not all of $G$ by step [](#nontrivial){.pf-ref}. Simplicity of $G$ leaves only the trivial subgroup, so the kernel is trivial and the homomorphism is injective.

:::

:::

::: {.pf-step #image}
$B \coloneqq \theset{c_{g} \mid g \in G}$ is a subgroup of $A$ isomorphic to $G$.

::: pf-proof
It is the image of a homomorphism, hence a subgroup, and step [](#injective){.pf-ref} makes the homomorphism an isomorphism onto its image.

:::

:::

::: {.pf-step #normal}
$B$ is normal in $A$.

::: pf-proof
Let $\alpha \in A$ and $g, h \in G$. Since $\alpha$ is a homomorphism, $\alpha\bigl(c_{g}(h)\bigr) = \alpha(ghg^{-1}) = \alpha(g)\alpha(h)\alpha(g)^{-1} = c_{\alpha(g)}\bigl(\alpha(h)\bigr)$, so $\alpha\circ c_{g} = c_{\alpha(g)}\circ\alpha$ and therefore $\alpha\circ c_{g}\circ\alpha^{-1} = c_{\alpha(g)}$, which lies in $B$. So $\alpha B\alpha^{-1} \subseteq B$ for every $\alpha \in A$, which is normality.

:::

:::

::: pf-step
$A$ contains a normal subgroup isomorphic to $G$, namely $B = \Inn(G)$.

::: pf-proof
Step [](#image){.pf-ref} gives the isomorphism $G \cong B$ and step [](#normal){.pf-ref} the normality of $B$ in $A$.

:::

:::

:::
:::
