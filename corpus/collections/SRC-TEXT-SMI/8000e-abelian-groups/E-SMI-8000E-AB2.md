---
schema: qual/card@1
id: E-SMI-8000E-AB2
kind: exercise
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
---

::: {.exercise}
Prove that if $0 \to A \to B \to \ZZ^t \to 0$ is an exact sequence, then $B$ is isomorphic to $A \times \ZZ^t$.

[Hint: if $b_1,\ldots,b_t$ are preimages of the standard generators of $\ZZ^t$, then the map $A \times \ZZ^t \to B$ induced by the given map $A \to B$, and by sending the generators of $\ZZ^t$ to the elements $b_i$, should be an isomorphism. I.e. this splits the sequence above.]

Give an example of an exact sequence $0 \to \ZZ^s \to \ZZ^t \to C \to 0$ that does not split, and where $\ZZ^t$ is not isomorphic (by any map) to $\ZZ^s \times C$.
:::

::: {.solution}
<1>1. Let $p: B \to \ZZ^t$ be the surjection, and let $e_1, \ldots, e_t$ be the standard generators of $\ZZ^t$.
::: {.proof}
setup.
:::

<1>2. Choose $b_i \in B$ with $p(b_i) = e_i$ for each $i$.
::: {.proof}
$p$ is surjective.
:::

<1>3. Define $s: \ZZ^t \to B$ by $s(\sum_i n_i e_i) = \sum_i n_i b_i$.
::: {.proof}
definition.
:::

<1>4. $s$ is a homomorphism with $p \circ s = \id_{\ZZ^t}$.
::: {.proof}
$p(s(\sum n_i e_i)) = p(\sum n_i b_i) = \sum n_i p(b_i) = \sum n_i e_i$.
:::

<1>5. Hence the sequence splits, and $B \cong A \oplus \ZZ^t$.
::: {.proof}
a short exact sequence $0 \to A \to B \to \ZZ^t \to 0$ with a splitting $s$ (i.e. $p \circ s = \id$) gives $B \cong A \oplus \ZZ^t$ (the map $A \oplus \ZZ^t \to B$, $(a, z) \mapsto i(a) + s(z)$, is an isomorphism).
:::

<1>6. Example of a non-splitting sequence: $0 \to \ZZ \xrightarrow{\cdot 2} \ZZ \to \ZZ/2 \to 0$.
::: {.proof}
the map $\ZZ \to \ZZ$ is multiplication by $2$, and the quotient is $\ZZ/2$.
:::

<1>7. This sequence does not split, and $\ZZ \not\cong \ZZ \times \ZZ/2$.
::: {.proof}
if it split, then $\ZZ \cong \ZZ \oplus \ZZ/2$, but $\ZZ$ is torsion-free while $\ZZ \oplus \ZZ/2$ has a $\ZZ/2$ torsion summand, a contradiction.
:::

<1>8. Q.E.D.
::: {.proof}
<1>5 and <1>7.
:::
:::
