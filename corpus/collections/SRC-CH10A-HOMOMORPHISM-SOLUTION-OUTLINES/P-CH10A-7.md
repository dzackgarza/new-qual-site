---
schema: qual/card@1
id: P-CH10A-7
kind: problem
title: Composition of homomorphisms and their kernels
classification:
  areas:
    - algebra
  topics:
    - Group Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Transcribed the retained solution outline for Gallian, Chapter 10 Part A, Exercise 7, PDF pp.
    1-2 of assets/attachments/Ch10PtASltns.pdf, into numbered steps. The outline proves the
    composition is a homomorphism and that ker phi is contained in ker(sigma phi); the card's
    added description of ker(sigma phi) as phi^{-1}(ker sigma) was kept and turned into steps 3
    and 4, with the strictness criterion proved rather than asserted. Checked: the composition
    computation, the identity argument, the preimage description and the strictness equivalence.
    Not checked: the printed exercise and page in Gallian, which is not retained; the collection
    provenance is the Google Books ISBN link, and the outline's pages are the citation.
---

::: {.problem}
If $\phi$ is a homomorphism from $G$ to $H$ and $\sigma$ is a homomorphism from $H$ to $K$, show that $\sigma\phi$ is a homomorphism from $G$ to $K$. How are $\ker \phi$ and $\ker \sigma\phi$ related?
:::

::: {.solution}

The argument is that of the retained solution outline for Chapter 10, Part A, Exercise 7, in `assets/attachments/Ch10PtASltns.pdf`, restructured into numbered steps, with the exact description of $\ker(\sigma\phi)$ supplied: the outline records only the inclusion and the remark that more elements of $H$ could map to the identity.

::: pf

::: {.pf-step #hom}

$\sigma\phi:G\to K$ is a homomorphism.

::: pf-proof

For $x,y\in G$, $(\sigma\phi)(xy)=\sigma(\phi(x)\phi(y))=\sigma(\phi(x))\sigma(\phi(y))=(\sigma\phi)(x)(\sigma\phi)(y)$, using that $\phi$ and then $\sigma$ are homomorphisms.

:::

:::

::: {.pf-step #incl}

$\ker\phi\subseteq\ker(\sigma\phi)$.

::: pf-proof

If $\phi(x)=e_H$ then $(\sigma\phi)(x)=\sigma(e_H)=e_K$, since a homomorphism carries the identity to the identity.

:::

:::

::: {.pf-step #preimage}

$\ker(\sigma\phi)=\phi^{-1}(\ker\sigma)$.

::: pf-proof

$(\sigma\phi)(x)=e_K$ holds exactly when $\phi(x)\in\ker\sigma$, which is the definition of the preimage.

:::

:::

::: {.pf-step #strict}

The inclusion of step [](#incl){.pf-ref} is strict exactly when $\ker\sigma$ contains an element of $\phi(G)$ other than $e_H$.

::: pf-proof

By step [](#preimage){.pf-ref}, $\ker(\sigma\phi)$ is the full preimage of $\ker\sigma$, and it equals $\ker\phi=\phi^{-1}(e_H)$ exactly when $\ker\sigma\cap\phi(G)=\set{e_H}$; otherwise some $g$ has $\phi(g)\in\ker\sigma$ with $\phi(g)\neq e_H$, and $g\in\ker(\sigma\phi)$ but $g\notin\ker\phi$.

:::

:::

:::

:::
