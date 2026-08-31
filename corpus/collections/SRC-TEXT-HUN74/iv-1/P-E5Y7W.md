---
schema: qual/card@1
id: P-E5Y7W
kind: problem
title: Hungerford 4.1.7
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

::: problem
(a) Show that if $A$ and $B$ are $R$-modules over a ring $R$, then the set $\operatorname{Hom}_R(A, B)$ of all $R$-module homomorphisms $A \to B$ is an abelian group under pointwise addition,
$$(f + g)(a) = f(a) + g(a) \quad \text{for all } a \in A,$$
with the zero map as identity element.

(b) Show that the set $\operatorname{End}_R(A) = \operatorname{Hom}_R(A, A)$ is a ring with identity under function composition $(f \circ g)(a) = f(g(a))$.

(c) Show that $A$ is a left $\operatorname{End}_R(A)$-module under the action defined by
$$f \cdot a = f(a) \quad \text{for all } f \in \operatorname{End}_R(A), \, a \in A.$$
:::

::: solution
**Goal:** Verify the abelian group axioms for $\operatorname{Hom}_R(A, B)$ in (a), the ring axioms for $\operatorname{End}_R(A)$ in (b), and the left module axioms for $A$ over its endomorphism ring in (c).

<1>1. Part (a): $\operatorname{Hom}_R(A, B)$ is an abelian group under pointwise addition.
    *Proof:*
    <2>1. Closure under addition: Let $f, g \in \operatorname{Hom}_R(A, B)$. For any $a_1, a_2 \in A$ and $r \in R$:
    $$(f + g)(a_1 + a_2) = f(a_1 + a_2) + g(a_1 + a_2) = f(a_1) + f(a_2) + g(a_1) + g(a_2) = (f(a_1) + g(a_1)) + (f(a_2) + g(a_2)) = (f+g)(a_1) + (f+g)(a_2),$$
    using commutativity of addition in the module $B$.
    <2>2. Scalar linearity: For any $r \in R$ and $a \in A$:
    $$(f + g)(r a) = f(r a) + g(r a) = r f(a) + r g(a) = r (f(a) + g(a)) = r (f + g)(a).$$
    Thus $f + g \in \operatorname{Hom}_R(A, B)$.
    <2>3. Associativity: For all $f, g, h \in \operatorname{Hom}_R(A, B)$ and $a \in A$, $((f + g) + h)(a) = (f(a) + g(a)) + h(a) = f(a) + (g(a) + h(a)) = (f + (g + h))(a)$.
    <2>4. Commutativity: For all $f, g \in \operatorname{Hom}_R(A, B)$ and $a \in A$, $(f + g)(a) = f(a) + g(a) = g(a) + f(a) = (g + f)(a)$.
    <2>5. Zero element: The zero map $0: A \to B$ defined by $0(a) = 0_B$ is an $R$-module homomorphism, and $(f + 0)(a) = f(a) + 0_B = f(a)$ for all $a \in A$.
    <2>6. Additive inverses: For $f \in \operatorname{Hom}_R(A, B)$, define $(-f)(a) = -f(a)$. Then $-f \in \operatorname{Hom}_R(A, B)$ and $(f + (-f))(a) = f(a) - f(a) = 0_B$.
    <2>7. Thus $(\operatorname{Hom}_R(A, B), +)$ is an abelian group.

<1>2. Part (b): $\operatorname{End}_R(A)$ is a ring with identity under composition.
    *Proof:*
    <2>1. By Part (a), $(\operatorname{End}_R(A), +)$ is an abelian group.
    <2>2. Closure under composition: Let $f, g \in \operatorname{End}_R(A)$. For any $a_1, a_2 \in A$ and $r \in R$:
    $$(f \circ g)(a_1 + a_2) = f(g(a_1 + a_2)) = f(g(a_1) + g(a_2)) = f(g(a_1)) + f(g(a_2)) = (f \circ g)(a_1) + (f \circ g)(a_2),$$
    $$(f \circ g)(r a) = f(g(r a)) = f(r g(a)) = r f(g(a)) = r (f \circ g)(a).$$
    Thus $f \circ g \in \operatorname{End}_R(A)$.
    <2>3. Associativity of multiplication: Function composition is associative: $((f \circ g) \circ h)(a) = f(g(h(a))) = (f \circ (g \circ h))(a)$.
    <2>4. Left and right distributivity: For all $f, g, h \in \operatorname{End}_R(A)$ and $a \in A$:
    $$(f \circ (g + h))(a) = f((g + h)(a)) = f(g(a) + h(a)) = f(g(a)) + f(h(a)) = (f \circ g)(a) + (f \circ h)(a) = (f \circ g + f \circ h)(a),$$
    $$((f + g) \circ h)(a) = (f + g)(h(a)) = f(h(a)) + g(h(a)) = (f \circ h)(a) + (g \circ h)(a) = (f \circ h + g \circ h)(a).$$
    <2>5. Multiplicative identity: The identity map $\operatorname{id}_A: A \to A$ given by $\operatorname{id}_A(a) = a$ is an $R$-module homomorphism, and satisfies $\operatorname{id}_A \circ f = f \circ \operatorname{id}_A = f$ for all $f \in \operatorname{End}_R(A)$.
    <2>6. Therefore $(\operatorname{End}_R(A), +, \circ)$ is a ring with identity.

<1>3. Part (c): $A$ is a left $\operatorname{End}_R(A)$-module.
    *Proof:*
    <2>1. $A$ is an abelian group under addition.
    <2>2. Linearity in $A$: For any $f \in \operatorname{End}_R(A)$ and $a, b \in A$:
    $$f \cdot (a + b) = f(a + b) = f(a) + f(b) = f \cdot a + f \cdot b.$$
    <2>3. Linearity in $\operatorname{End}_R(A)$: For any $f, g \in \operatorname{End}_R(A)$ and $a \in A$:
    $$(f + g) \cdot a = (f + g)(a) = f(a) + g(a) = f \cdot a + g \cdot a.$$
    <2>4. Associativity of scalar multiplication: For any $f, g \in \operatorname{End}_R(A)$ and $a \in A$:
    $$(f \circ g) \cdot a = (f \circ g)(a) = f(g(a)) = f \cdot (g(a)) = f \cdot (g \cdot a).$$
    <2>5. Identity action: For any $a \in A$:
    $$\operatorname{id}_A \cdot a = \operatorname{id}_A(a) = a.$$
    <2>6. Thus $A$ is a left $\operatorname{End}_R(A)$-module.

<1>4. Conclusion:
    *Proof:*
    $\operatorname{Hom}_R(A, B)$ is an abelian group, $\operatorname{End}_R(A)$ is a ring with identity, and $A$ is a left $\operatorname{End}_R(A)$-module.
:::
