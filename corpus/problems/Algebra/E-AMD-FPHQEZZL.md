---
schema: qual/card@1
id: E-AMD-FPHQEZZL
kind: problem
title: $\Inn(G)\cong G/Z(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Centralizers and Normalizers
  - Isomorphism Theorems
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured the prose solution into a structured proof under #2 and re-checked every step:
    conjugation by $g$ is an automorphism with inverse conjugation by $g^{-1}$; $\Phi(gh)$
    $=\Phi(g)\circ\Phi(h)$ via $(gh)^{-1}=h^{-1}g^{-1}$; $\ker\Phi=Z(G)$ by the chain of
    equivalences given; $\im\Phi=\Inn(G)$ by definition of the inner automorphism group; and the
    first isomorphism theorem, which needs $\ker\Phi$ normal, a fact about kernels that is used
    rather than proved here. No defect was found in the statement or in the prose argument. The
    card carries no collection and no retained solution set covers this exercise, so the
    argument is the card's own as the solution says. Not claimed: a citation to a publication.
---

::: {.exercise}
Show that $\Inn(G) \cong G / Z(G)$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, and it is the standard computation with the first isomorphism theorem. Write $Z(G)$ for the centre of $G$, and $\Inn(G)$ for its group of inner automorphisms.

::: pf

::: {.pf-step #well-defined}
The formula $\Phi(g)(x)=gxg^{-1}$ defines a function $\Phi\colon G\to\Aut(G)$.

::: pf-proof
For fixed $g\in G$ the map $x\mapsto gxg^{-1}$ is a homomorphism, since $(gxg^{-1})(gyg^{-1})=gxyg^{-1}$, and $x\mapsto g^{-1}xg$ is a two-sided inverse of it; hence $\Phi(g)\in\Aut(G)$. Each $\Phi(g)$ is determined by $g$, so the assignment $g\mapsto\Phi(g)$ is a function from $G$ to $\Aut(G)$.
:::

:::

::: {.pf-step #homomorphism}
$\Phi$ is a homomorphism, that is $\Phi(gh)=\Phi(g)\circ\Phi(h)$ for all $g,h\in G$.

::: pf-proof
Using $(gh)^{-1}=h^{-1}g^{-1}$, for every $x\in G$,
$$
\Phi(gh)(x)=(gh)x(gh)^{-1}=g\bigl(hxh^{-1}\bigr)g^{-1}=\Phi(g)\bigl(\Phi(h)(x)\bigr),
$$
and composition of functions is the group operation in $\Aut(G)$.
:::

:::

::: {.pf-step #kernel}
$\ker\Phi=Z(G)$.

::: pf-proof
For $g\in G$ the following are equivalent: $g\in\ker\Phi$; $\Phi(g)$ is the identity map of $G$; $gxg^{-1}=x$ for every $x\in G$; $gx=xg$ for every $x\in G$, multiplying the previous equation on the right by $g$; and $g\in Z(G)$, the centre being by definition the set of elements commuting with every element of $G$.
:::

:::

::: {.pf-step #image}
$\im\Phi=\Inn(G)$.

::: pf-proof
$\Inn(G)$ is defined as the set of automorphisms of $G$ that are conjugation by an element of $G$, and the values of $\Phi$ are exactly those automorphisms.
:::

:::

::: {.pf-step}
$\boxed{G/Z(G)\cong\Inn(G)}$.

::: pf-proof
The kernel of a homomorphism is normal, so step [](#kernel){.pf-ref} shows $Z(G)\normal G$; the first isomorphism theorem applied to the homomorphism $\Phi$ of step [](#homomorphism){.pf-ref} gives $G/\ker\Phi\cong\im\Phi$, which is $G/Z(G)\cong\Inn(G)$ by steps [](#kernel){.pf-ref} and [](#image){.pf-ref}.
:::

:::

:::
:::
