---
schema: qual/card@1
id: P-APASP09F
kind: problem
title: "Contragredient representation and character conjugation"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $\rho: G \to \operatorname{GL}(V)$ be a representation of the finite group $G$.

(a) Show that the map $\hat{\rho}: g \in G \mapsto \rho(g^{-1})^t$ defines a representation, where $t$ means the transpose of a matrix.

(b) Let $\chi_\rho$ and $\chi_{\hat{\rho}}$ be the characters of $\rho$ and $\hat{\rho}$.
Show that $\chi_{\hat{\rho}}(g) = \overline{\chi_\rho(g)}$ (i.e.\ the complex conjugate) for all $g \in G$.

(c) Let $V$ be a simple $G$-module.
Show: If $W$ is a simple $G$-module such that the trivial representation occurs in $V \otimes W$, then $W$ must be isomorphic to the representation defined in (a).
:::

::: {.solution}
**(a).**

<1>1. $\hat\rho(gh) = \rho((gh)^{-1})^t = \rho(h^{-1}g^{-1})^t = (\rho(h^{-1})\rho(g^{-1}))^t = \rho(g^{-1})^t \rho(h^{-1})^t = \hat\rho(g)\hat\rho(h)$.
::: {.proof}
$\rho$ is a homomorphism, and $(AB)^t = B^t A^t$.
:::

<1>2. $\hat\rho(e) = \rho(e)^t = I$.
::: {.proof}
$\rho(e) = I$.
:::

<1>3. Hence $\hat\rho$ is a representation.
::: {.proof}
<1>1 and <1>2.
:::

**(b).**

<1>1. $\chi_{\hat\rho}(g) = \operatorname{tr}(\hat\rho(g)) = \operatorname{tr}(\rho(g^{-1})^t) = \operatorname{tr}(\rho(g^{-1}))$.
::: {.proof}
the trace is invariant under transpose.
:::

<1>2. $\operatorname{tr}(\rho(g^{-1})) = \chi_\rho(g^{-1})$.
::: {.proof}
definition of character.
:::

<1>3. $\chi_\rho(g^{-1}) = \overline{\chi_\rho(g)}$.
::: {.proof}
since $G$ is finite, $\rho(g)$ has finite order, so its eigenvalues are roots of unity; the eigenvalues of $\rho(g^{-1}) = \rho(g)^{-1}$ are the inverses (conjugates) of the eigenvalues of $\rho(g)$, so the traces are conjugate.
:::

<1>4. Hence $\chi_{\hat\rho}(g) = \overline{\chi_\rho(g)}$.
::: {.proof}
<1>1–<1>3.
:::

**(c).**

<1>1. The trivial representation occurs in $V \otimes W$ iff $\langle \chi_V \chi_W, 1 \rangle \neq 0$.
::: {.proof}
the multiplicity of the trivial character in a representation is $\langle \chi, 1 \rangle = \frac{1}{|G|}\sum_g \chi(g)$.
:::

<1>2. $\langle \chi_V \chi_W, 1 \rangle = \frac{1}{|G|}\sum_g \chi_V(g)\chi_W(g) = \langle \chi_V, \overline{\chi_W} \rangle$.
::: {.proof}
definition of the inner product, and $\overline{\chi_W(g)} = \chi_W(g^{-1})$.
:::

<1>3. Since $V$ and $W$ are simple, $\langle \chi_V, \overline{\chi_W} \rangle \neq 0$ iff $\chi_V = \overline{\chi_W}$.
::: {.proof}
orthogonality of irreducible characters.
:::

<1>4. $\overline{\chi_W} = \chi_{\hat W}$ by part (b).
::: {.proof}
(b).
:::

<1>5. Hence $\chi_V = \chi_{\hat W}$, so $V \cong \hat W$, i.e. $W \cong \hat V$.
::: {.proof}
<1>3 and <1>4, and irreducible representations are determined by their characters.
:::

<1>6. Q.E.D.
::: {.proof}
<1>3 (a), <1>4 (b), <1>5 (c).
:::
:::
