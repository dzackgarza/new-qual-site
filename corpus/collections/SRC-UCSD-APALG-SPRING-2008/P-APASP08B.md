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

::: problem
Show that if $f$ is a nilpotent element of the group algebra of a finite group $G$, then $\hat{f} = 0$.
Hint: Use the Fourier transform.
:::

::: {.solution}
<1>1. The group algebra $\mathbb{C}[G]$ decomposes as $\bigoplus_\rho M_{d_\rho}(\mathbb{C})$ via the Fourier transform (Wedderburn decomposition), where $\rho$ runs over the irreducible representations.
::: {.proof}
the Fourier transform is the isomorphism $\mathbb{C}[G] \cong \bigoplus_\rho \operatorname{End}(V_\rho)$.
:::

<1>2. Under this isomorphism, $\hat f$ is the tuple $(\hat f(\rho))_\rho$ of matrices $\hat f(\rho) = \sum_{g} f(g)\rho(g)$.
::: {.proof}
definition of the Fourier transform.
:::

<1>3. If $f$ is nilpotent, then $f^n = 0$ for some $n$, so $\hat f(\rho)^n = \widehat{f^n}(\rho) = 0$ for each $\rho$.
::: {.proof}
the Fourier transform is a ring homomorphism, so $\widehat{f^n} = \hat f^n$.
:::

<1>4. Hence each $\hat f(\rho)$ is a nilpotent matrix.
::: {.proof}
<1>3.
:::

<1>5. But $\hat f(\rho)$ is a matrix over $\mathbb{C}$; a nilpotent matrix over $\mathbb{C}$ is not necessarily zero, so we need more: the Fourier transform of a nilpotent element of the *group algebra* must be zero because the group algebra is semisimple (it has no nonzero nilpotent elements).
::: {.proof}
$\mathbb{C}[G]$ is semisimple (Maschke's theorem), so it is a direct sum of matrix algebras, which have no nonzero nilpotent ideals; in fact a direct sum of matrix algebras has no nonzero nilpotent elements at all.
:::

<1>6. Hence $f = 0$, so $\hat f = 0$.
::: {.proof}
<1>5 (the only nilpotent element of a semisimple algebra is $0$).
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
