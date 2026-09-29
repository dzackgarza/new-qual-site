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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 3 of Part II of the official UCSD Spring 2009 Applied Algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Verified the contragredient homomorphism, conjugate-character identity, and the irreducible tensor-product criterion via character orthogonality.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $\rho: G \to \operatorname{GL}(V)$ be a representation of the finite group $G$.

(a) Show that the map $\hat{\rho}: g \in G \mapsto \rho(g^{-1})^t$ defines a representation, where $t$ means the transpose of a matrix.

(b) Let $\chi_\rho$ and $\chi_{\hat{\rho}}$ be the characters of $\rho$ and $\hat{\rho}$.
Show that $\chi_{\hat{\rho}}(g) = \overline{\chi_\rho(g)}$ (i.e.\ the complex conjugate) for all $g \in G$.

(c) Let $V$ be a simple $G$-module.
Show: If $W$ is a simple $G$-module such that the trivial representation occurs in $V \otimes W$, then $W$ must be isomorphic to the representation defined in (a).
:::

::: {.solution}
**(a).**

::: pf

::: {.pf-step #p1-s1}
$\hat\rho(gh) = \rho((gh)^{-1})^t = \rho(h^{-1}g^{-1})^t = (\rho(h^{-1})\rho(g^{-1}))^t = \rho(g^{-1})^t \rho(h^{-1})^t = \hat\rho(g)\hat\rho(h)$.

::: pf-proof
$\rho$ is a homomorphism, and $(AB)^t = B^t A^t$.
:::

:::

::: {.pf-step #p1-s2}
$\hat\rho(e) = \rho(e)^t = I$.

::: pf-proof
$\rho(e) = I$.
:::

:::

::: {.pf-step #p1-s3}
Hence $\hat\rho$ is a representation.

::: pf-proof
step [](#p1-s1){.pf-ref} and step [](#p1-s2){.pf-ref}.
:::

:::

:::

**(b).**

::: pf

::: {.pf-step #p2-s1}
$\chi_{\hat\rho}(g) = \operatorname{tr}(\hat\rho(g)) = \operatorname{tr}(\rho(g^{-1})^t) = \operatorname{tr}(\rho(g^{-1}))$.

::: pf-proof
the trace is invariant under transpose.
:::

:::

::: {.pf-step #p2-s2}
$\operatorname{tr}(\rho(g^{-1})) = \chi_\rho(g^{-1})$.

::: pf-proof
definition of character.
:::

:::

::: {.pf-step #p2-s3}
$\chi_\rho(g^{-1}) = \overline{\chi_\rho(g)}$.

::: pf-proof
since $G$ is finite, $\rho(g)$ has finite order, so its eigenvalues are roots of unity; the eigenvalues of $\rho(g^{-1}) = \rho(g)^{-1}$ are the inverses (conjugates) of the eigenvalues of $\rho(g)$, so the traces are conjugate.
:::

:::

::: {.pf-step #p2-s4}
Hence $\chi_{\hat\rho}(g) = \overline{\chi_\rho(g)}$.

::: pf-proof
step [](#p2-s1){.pf-ref}, step [](#p2-s2){.pf-ref}, and step [](#p2-s3){.pf-ref}.
:::

:::

:::

**(c).**

::: pf

::: pf-step
The trivial representation occurs in $V \otimes W$ iff $\langle \chi_V \chi_W, 1 \rangle \neq 0$.

::: pf-proof
the multiplicity of the trivial character in a representation is $\langle \chi, 1 \rangle = \frac{1}{|G|}\sum_g \chi(g)$.
:::

:::

::: pf-step
$\langle \chi_V \chi_W, 1 \rangle = \frac{1}{|G|}\sum_g \chi_V(g)\chi_W(g) = \langle \chi_V, \overline{\chi_W} \rangle$.

::: pf-proof
definition of the inner product, and $\overline{\chi_W(g)} = \chi_W(g^{-1})$.
:::

:::

::: {.pf-step #p3-s3}
Since $V$ and $W$ are simple, $\langle \chi_V, \overline{\chi_W} \rangle \neq 0$ iff $\chi_V = \overline{\chi_W}$.

::: pf-proof
orthogonality of irreducible characters.
:::

:::

::: {.pf-step #p3-s4}
$\overline{\chi_W} = \chi_{\hat W}$ by part (b).

::: pf-proof
(b).
:::

:::

::: {.pf-step #p3-s5}
Hence $\chi_V = \chi_{\hat W}$, so $V \cong \hat W$, i.e. $W \cong \hat V$.

::: pf-proof
step [](#p3-s3){.pf-ref} and step [](#p3-s4){.pf-ref}, and irreducible representations are determined by their characters.
:::

:::

::: pf-qed
step [](#p1-s3){.pf-ref} (a), step [](#p2-s4){.pf-ref} (b), step [](#p3-s5){.pf-ref} (c).
:::

:::
:::
