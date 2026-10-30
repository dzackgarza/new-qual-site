---
schema: qual/card@1
id: P-APAS26H
kind: problem
title: Convolution algebra of an odd-order group has a subalgebra not of subgroup type
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: 'Solution rewritten: the previous argument was vague and garbled; the new one uses
    the averaging idempotent and a dimension parity count.'
---

::: {.problem}
Let $G$ be a nontrivial finite group of odd order.
Show that the convolution algebra $\mathcal{C}(G)$ contains a subalgebra $\mathcal{B}$ not isomorphic to $\mathcal{C}(H)$ for any subgroup $H \le G$.

Note: On this exam, an algebra is a finite-dimensional complex vector space equipped with an associative, bilinear, unital multiplication and an antilinear, antimultiplicative, involutive conjugation; algebra homomorphisms respect multiplication, conjugation, and units.
:::

::: {.solution}
Write $\delta_g$ for the indicator function of $g\in G$, so that $\delta_g*\delta_h=\delta_{gh}$, the unit is $\delta_e$, and $\delta_g^*=\delta_{g^{-1}}$.

::: pf

::: {.pf-step #idempotent}
The element $p=\frac1{\cardinality{G}}\sum_{g\in G}\delta_g$ satisfies $p*p=p=p^*$ and $p\ne0,\delta_e$.

::: pf-proof
For every $h\in G$, $\delta_h*p=p$, because $g\mapsto hg$ permutes $G$. Averaging over $h$ gives $p*p=p$. Inversion permutes $G$, so $p^*=p$. The coefficient of $\delta_e$ in $p$ is $1/\cardinality{G}$, and the coefficients of $p$ are all equal, so $p\ne0$; since $G$ is nontrivial, $p$ has a nonzero coefficient away from $e$, so $p\ne\delta_e$.
:::

:::

::: {.pf-step #subalgebra}
$\mathcal{B}=\operatorname{span}\{p,\ \delta_e-p\}$ is a subalgebra of $\mathcal{C}(G)$ isomorphic to $\CC\oplus\CC$, and $\dim\mathcal{B}=2$.

::: pf-proof
By step [](#idempotent){.pf-ref}, $p$ and $q=\delta_e-p$ are nonzero self-adjoint idempotents with $p+q=\delta_e$ and $p*q=q*p=p-p*p=0$. Hence $\mathcal{B}$ contains the unit, is closed under convolution and conjugation, and $ap+bq\mapsto(a,b)$ is an isomorphism onto $\CC\oplus\CC$ with componentwise operations. Linear independence of $p$ and $q$ follows from $p*q=0$ with $p,q\ne0$.
:::

:::

::: {.pf-step #subgroups}
For a subgroup $H\le G$, $\dim\mathcal{C}(H)=\cardinality{H}$ is odd.

::: pf-proof
$\mathcal{C}(H)$ has the basis $\{\delta_h:h\in H\}$, and $\cardinality{H}$ divides the odd number $\cardinality{G}$ by Lagrange's theorem.
:::

:::

::: pf-qed
An isomorphism preserves dimension. By steps [](#subalgebra){.pf-ref} and [](#subgroups){.pf-ref}, $\dim\mathcal{B}=2$ is even and $\dim\mathcal{C}(H)$ is odd for every $H\le G$, so $\mathcal{B}$ is isomorphic to no $\mathcal{C}(H)$.
:::

:::

:::
