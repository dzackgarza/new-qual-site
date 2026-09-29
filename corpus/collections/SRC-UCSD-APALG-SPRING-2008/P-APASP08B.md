---
schema: qual/card@1
id: P-APASP08B
kind: problem
title: "Nilpotent element of a group algebra has zero Fourier transform"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Group Algebras
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Show that if $f$ is a nilpotent element of the group algebra of a finite group $G$, then $\hat{f} = 0$.
Hint: Use the Fourier transform.
:::

::: {.solution}

::: pf

::: {.pf-step #wedderburn-decomposition}
The group algebra $\mathbb{C}[G]$ decomposes as $\bigoplus_\rho M_{d_\rho}(\mathbb{C})$ via the Fourier transform (Wedderburn decomposition), where $\rho$ runs over the irreducible representations.

::: pf-proof
the Fourier transform is the isomorphism $\mathbb{C}[G] \cong \bigoplus_\rho \operatorname{End}(V_\rho)$.
:::

:::

::: {.pf-step #fourier-transform-definition}
Under this isomorphism, $\hat f$ is the tuple $(\hat f(\rho))_\rho$ of matrices $\hat f(\rho) = \sum_{g} f(g)\rho(g)$.

::: pf-proof
definition of the Fourier transform.
:::

:::

::: {.pf-step #fourier-transform-nilpotent}
If $f$ is nilpotent, then $f^n = 0$ for some $n$, so $\hat f(\rho)^n = \widehat{f^n}(\rho) = 0$ for each $\rho$.

::: pf-proof
the Fourier transform is a ring homomorphism, so $\widehat{f^n} = \hat f^n$.
:::

:::

::: {.pf-step #each-component-nilpotent}
Hence each $\hat f(\rho)$ is a nilpotent matrix.

::: pf-proof
Step [](#fourier-transform-nilpotent){.pf-ref}.
:::

:::

::: {.pf-step #semisimple-has-no-nilpotents}
But $\hat f(\rho)$ is a matrix over $\mathbb{C}$; a nilpotent matrix over $\mathbb{C}$ is not necessarily zero, so we need more: the Fourier transform of a nilpotent element of the *group algebra* must be zero because the group algebra is semisimple (it has no nonzero nilpotent elements).

::: pf-proof
$\mathbb{C}[G]$ is semisimple (Maschke's theorem), so it is a direct sum of matrix algebras, which have no nonzero nilpotent ideals; in fact a direct sum of matrix algebras has no nonzero nilpotent elements at all.
:::

:::

::: {.pf-step #f-is-zero}
Hence $f = 0$, so $\hat f = 0$.

::: pf-proof
Step [](#semisimple-has-no-nilpotents){.pf-ref} (the only nilpotent element of a semisimple algebra is $0$).
:::

:::

::: pf-qed
Step [](#f-is-zero){.pf-ref}.
:::

:::

:::
