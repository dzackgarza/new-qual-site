---
schema: qual/card@1
id: E-SMI-8000E-AB2
kind: problem
title: A short exact sequence ending in free abelian splits
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Exact Sequences
  - Free Modules
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed problem, Smith Math 8000 packet 8000e.pdf page 1,
    abelian-groups problem 2: "prove if 0-->A-->B-->Z^t-->0 is an exact sequence,
    then B is isomorphic to Ax(Z^t) ... Give an example of an exact sequence
    0-->Z^s-->Z^t-->C-->0 that does not split, and where Z^t is not isomorphic
    [by any map], to Z^s x C." The card states both halves with the printed hint.
    The proof was checked: freeness of Z^t makes e_i ↦ b_i a homomorphism s with
    p∘s = id, and Psi(a,z) = i(a) + s(z) is injective because p∘Psi recovers z
    and i is injective, surjective because b - s(p(b)) lies in ker p = im i. The
    example 0 → Z →(·2) Z → Z/2 → 0 is exact, Z × Z/2 has a torsion element while
    Z does not, and every Z/2 → Z is zero, so the sequence does not split. The
    card's s = t = 1, C = Z/2 is a valid instance. Complete; no defect.
---

::: {.exercise}
Prove that if $0 \to A \to B \to \ZZ^t \to 0$ is an exact sequence, then $B$ is isomorphic to $A \times \ZZ^t$.

[Hint: if $b_1,\ldots,b_t$ are preimages of the standard generators of $\ZZ^t$, then the map $A \times \ZZ^t \to B$ induced by the given map $A \to B$, and by sending the generators of $\ZZ^t$ to the elements $b_i$, should be an isomorphism. I.e. this splits the sequence above.]

Give an example of an exact sequence $0 \to \ZZ^s \to \ZZ^t \to C \to 0$ that does not split, and where $\ZZ^t$ is not isomorphic (by any map) to $\ZZ^s \times C$.
:::

::: {.solution}
Write the sequence as $0 \to A \xrightarrow{i} B \xrightarrow{p} \ZZ^t \to 0$, and let $e_1, \ldots, e_t$ be the standard basis of $\ZZ^t$. Since $p$ is surjective, choose $b_i \in B$ with $p(b_i) = e_i$ for each $i$.

::: pf

::: {.pf-step #s1}

The homomorphism $s\colon \ZZ^t \to B$ with $s(e_i) = b_i$ satisfies $p \circ s = \id_{\ZZ^t}$.

::: pf-proof

Since $\ZZ^t$ is free on $e_1, \ldots, e_t$, the formula $s(\sum_i n_i e_i) = \sum_i n_i b_i$ defines a homomorphism. Then $p(s(\sum_i n_i e_i)) = \sum_i n_i p(b_i) = \sum_i n_i e_i$.

:::

:::

::: {.pf-step #s2}

The map $\Psi\colon A \times \ZZ^t \to B$, $\Psi(a, z) = i(a) + s(z)$, is an isomorphism.

::: pf-proof

$\Psi$ is a homomorphism because $i$ and $s$ are. If $\Psi(a, z) = 0$, applying $p$ and using $p \circ i = 0$ and step [](#s1){.pf-ref} gives $z = 0$; then $i(a) = 0$, so $a = 0$ because $i$ is injective. For $b \in B$, the element $b - s(p(b))$ lies in $\ker p = \operatorname{im} i$ by step [](#s1){.pf-ref}, say $b - s(p(b)) = i(a)$; then $b = \Psi(a, p(b))$.

:::

:::

::: {.pf-step #s3}

The sequence $0 \to \ZZ \xrightarrow{\cdot 2} \ZZ \to \ZZ/2 \to 0$ is exact, does not split, and $\ZZ \not\cong \ZZ \times \ZZ/2$.

::: pf-proof

Multiplication by $2$ is injective with image $2\ZZ$, the kernel of the quotient map $\ZZ \to \ZZ/2$. The group $\ZZ$ is torsion-free, while $(0, 1) \in \ZZ \times \ZZ/2$ has order $2$, so no isomorphism $\ZZ \cong \ZZ \times \ZZ/2$ exists. For the same reason every homomorphism $\sigma\colon \ZZ/2 \to \ZZ$ is zero, so the composite $\ZZ/2 \xrightarrow{\sigma} \ZZ \to \ZZ/2$ is zero rather than the identity, and the sequence does not split.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} gives $B \cong A \times \ZZ^t$, and step [](#s3){.pf-ref} gives the required example with $s = t = 1$ and $C = \ZZ/2$.

:::

:::

:::
