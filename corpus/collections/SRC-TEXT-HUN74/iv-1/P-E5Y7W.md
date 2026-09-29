---
schema: qual/card@1
id: P-E5Y7W
kind: problem
title: $\operatorname{Hom}_R(A,B)$ is an abelian group, $\operatorname{End}_R(A)$ is a ring, and $A$ is an $\operatorname{End}_R(A)$-module
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homomorphisms
  - Rings
relations: []
review: draft
---

::: {.problem}
(a) Show that if $A$ and $B$ are $R$-modules over a ring $R$, then the set $\operatorname{Hom}_R(A, B)$ of all $R$-module homomorphisms $A \to B$ is an abelian group under pointwise addition, $$(f + g)(a) = f(a) + g(a) \quad \text{for all } a \in A,$$ with the zero map as identity element.

(b) Show that the set $\operatorname{End}_R(A) = \operatorname{Hom}_R(A, A)$ is a ring with identity under function composition $(f \circ g)(a) = f(g(a))$.

(c) Show that $A$ is a left $\operatorname{End}_R(A)$-module under the action defined by $$f \cdot a = f(a) \quad \text{for all } f \in \operatorname{End}_R(A), \, a \in A.$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) $\operatorname{Hom}_R(A, B)$ is an abelian group under pointwise addition.

::: pf-proof

::: {.pf-step #s1-1}

For $f, g \in \operatorname{Hom}_R(A, B)$, the sum $f+g$ lies in $\operatorname{Hom}_R(A, B)$.

::: pf-proof

For $a_1, a_2 \in A$, using commutativity of addition in $B$,
$$(f + g)(a_1 + a_2) = f(a_1) + f(a_2) + g(a_1) + g(a_2) = (f+g)(a_1) + (f+g)(a_2).$$
For $r \in R$ and $a \in A$,
$$(f + g)(r a) = f(r a) + g(r a) = r f(a) + r g(a) = r (f + g)(a).$$

:::

:::

::: {.pf-step #s1-2}

Addition in $\operatorname{Hom}_R(A, B)$ is associative and commutative.

::: pf-proof

For $f, g, h \in \operatorname{Hom}_R(A, B)$ and $a \in A$, associativity and commutativity of addition in $B$ give $((f + g) + h)(a) = (f + (g + h))(a)$ and $(f + g)(a) = (g + f)(a)$.

:::

:::

::: {.pf-step #s1-3}

The zero map is an identity element, and every $f$ has the additive inverse $-f$, $(-f)(a)=-f(a)$.

::: pf-proof

The zero map $0\colon A \to B$, $0(a) = 0_B$, is $R$-linear and $(f + 0)(a) = f(a)$. The map $-f$ is $R$-linear, since $-f(ra)=-rf(a)=r(-f(a))$, and $(f + (-f))(a) = f(a) - f(a) = 0_B$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref}, [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} verify the abelian group axioms.

:::

:::

:::

::: {.pf-step #s2}

(b) $\operatorname{End}_R(A)$ is a ring with identity under $+$ and $\circ$.

::: pf-proof

::: {.pf-step #s2-1}

For $f, g \in \operatorname{End}_R(A)$, the composite $f\circ g$ lies in $\operatorname{End}_R(A)$.

::: pf-proof

For $a_1, a_2 \in A$ and $r \in R$,
$$(f \circ g)(a_1 + a_2) = f(g(a_1) + g(a_2)) = (f \circ g)(a_1) + (f \circ g)(a_2),$$
$$(f \circ g)(r a) = f(r g(a)) = r f(g(a)) = r (f \circ g)(a).$$

:::

:::

::: {.pf-step #s2-2}

Composition is associative and distributes over addition on both sides.

::: pf-proof

Composition of functions is associative. For $f, g, h \in \operatorname{End}_R(A)$ and $a \in A$, additivity of $f$ gives
$$(f \circ (g + h))(a) = f(g(a) + h(a)) = (f \circ g + f \circ h)(a),$$
and the definition of pointwise addition gives
$$((f + g) \circ h)(a) = f(h(a)) + g(h(a)) = (f \circ h + g \circ h)(a).$$

:::

:::

::: {.pf-step #s2-3}

The identity map $\operatorname{id}_A$ is a multiplicative identity.

::: pf-proof

The map $\operatorname{id}_A$ is $R$-linear and $\operatorname{id}_A \circ f = f \circ \operatorname{id}_A = f$ for all $f \in \operatorname{End}_R(A)$.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref}, $(\operatorname{End}_R(A), +)$ is an abelian group; steps [](#s2-1){.pf-ref}, [](#s2-2){.pf-ref} and [](#s2-3){.pf-ref} verify the remaining ring axioms.

:::

:::

:::

::: pf-step

(c) $A$ is a left $\operatorname{End}_R(A)$-module under $f\cdot a=f(a)$.

::: pf-proof

For $f, g \in \operatorname{End}_R(A)$ and $a, b \in A$:
$$f \cdot (a + b) = f(a) + f(b) = f \cdot a + f \cdot b,$$
$$(f + g) \cdot a = f(a) + g(a) = f \cdot a + g \cdot a,$$
$$(f \circ g) \cdot a = f(g(a)) = f \cdot (g \cdot a),$$
$$\operatorname{id}_A \cdot a = a.$$
These are the axioms of a unitary left module over the ring of step [](#s2){.pf-ref}.

:::

:::

:::

:::
