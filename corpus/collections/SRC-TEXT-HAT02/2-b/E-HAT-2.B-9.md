---
schema: qual/card@1
id: E-HAT-2.B-9
kind: problem
title: "Transfer sequence for trivial coverings"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Make the transfer sequence explicit in the case of a trivial covering $\tilde{X} \to X$, where $\tilde{X} = X \times S^0$.

::: {.solution}
**Setup.** The trivial covering $p: X \times S^0 \to X$, $p(x, \epsilon) = x$, is $2$-sheeted. The transfer $\tau: C_n(X) \to C_n(X \times S^0)$ sends each singular simplex $\sigma: \Delta^n \to X$ to the sum of its two lifts, and satisfies $p_\# \tau = 2 \cdot \id$. The transfer sequence is the long exact sequence of the short exact sequence of chain complexes
$$0 \to C_*(X) \xrightarrow{\tau} C_*(X \times S^0) \to C_*(X \times S^0)/\tau C_*(X) \to 0.$$

<1>1. $C_n(X \times S^0) \cong C_n(X) \oplus C_n(X)$.
::: {.proof}
$X \times S^0 = X \sqcup X$ is the disjoint union of two copies of $X$ (the sheets $\epsilon = 0$ and $\epsilon = 1$), and singular chains split over disjoint unions.
:::

<1>2. Under <1>1, $\tau$ is the diagonal map $\Delta: C_n(X) \to C_n(X) \oplus C_n(X)$, $\sigma \mapsto (\sigma, \sigma)$.
::: {.proof}
the two lifts of $\sigma$ are $(\sigma, 0)$ and $(\sigma, 1)$, so $\tau(\sigma) = (\sigma, 0) + (\sigma, 1) = (\sigma, \sigma)$ in the direct sum.
:::

<1>3. The quotient $C_n(X \times S^0)/\tau C_n(X) \cong C_n(X)$.
<2>1. $\tau C_n(X) = \{(c, c) : c \in C_n(X)\}$.
::: {.proof}
<1>2.
:::
<2>2. The map $(a, b) \mapsto a - b$ has kernel exactly $\{(c, c)\}$ and is surjective.
::: {.proof}
$(a, b) \mapsto a - b$ vanishes iff $a = b$; and $a \mapsto (a, 0) \mapsto a$ shows surjectivity.
:::
<2>3. Hence $C_n(X) \oplus C_n(X) / \{(c,c)\} \cong C_n(X)$ via the difference map.
::: {.proof}
first isomorphism theorem applied to <2>2.
:::

<1>4. The transfer sequence is therefore
$$\cdots \to H_n(X) \xrightarrow{\Delta_*} H_n(X) \oplus H_n(X) \xrightarrow{\delta_*} H_n(X) \to H_{n-1}(X) \to \cdots$$
where $\Delta_*(x) = (x, x)$ and $\delta_*(a, b) = a - b$.
::: {.proof}
apply the long exact sequence in homology to the short exact sequence of <1>1–<1>3.
:::

<1>5. The connecting homomorphisms $H_n(X) \to H_{n-1}(X)$ are all zero.
::: {.proof}
$\delta_*$ is surjective (since $(a, 0) \mapsto a$), so the map out of $H_n(X)$ in the sequence is zero.
:::

<1>6. Hence the transfer sequence splits into short exact sequences
$$0 \to H_n(X) \xrightarrow{\Delta_*} H_n(X) \oplus H_n(X) \xrightarrow{\delta_*} H_n(X) \to 0$$
for each $n$.
::: {.proof}
<1>4 and <1>5; the sequence is exact and the connecting maps vanish.
:::

<1>7. Q.E.D.
::: {.proof}
<1>4–<1>6 make the transfer sequence explicit: it is the split short exact sequence with diagonal inclusion and difference projection.
:::
:::
