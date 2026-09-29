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

::: {.problem}
Make the transfer sequence explicit in the case of a trivial covering $\tilde{X} \to X$, where $\tilde{X} = X \times S^0$.
:::

::: {.solution}
**Setup.** The trivial covering $p: X \times S^0 \to X$, $p(x, \epsilon) = x$, is $2$-sheeted. The transfer $\tau: C_n(X) \to C_n(X \times S^0)$ sends each singular simplex $\sigma: \Delta^n \to X$ to the sum of its two lifts, and satisfies $p_\# \tau = 2 \cdot \id$. The transfer sequence is the long exact sequence of the short exact sequence of chain complexes
$$0 \to C_*(X) \xrightarrow{\tau} C_*(X \times S^0) \to C_*(X \times S^0)/\tau C_*(X) \to 0.$$

::: pf

::: {.pf-step #s1}

$C_n(X \times S^0) \cong C_n(X) \oplus C_n(X)$.

::: pf-proof

$X \times S^0 = X \sqcup X$ is the disjoint union of two copies of $X$ (the sheets $\epsilon = 0$ and $\epsilon = 1$), and singular chains split over disjoint unions.

:::

:::

::: {.pf-step #s2}

Under step [](#s1){.pf-ref}, $\tau$ is the diagonal map $\Delta: C_n(X) \to C_n(X) \oplus C_n(X)$, $\sigma \mapsto (\sigma, \sigma)$.

::: pf-proof

the two lifts of $\sigma$ are $(\sigma, 0)$ and $(\sigma, 1)$, so $\tau(\sigma) = (\sigma, 0) + (\sigma, 1) = (\sigma, \sigma)$ in the direct sum.

:::

:::

::: {.pf-step #s3}

The quotient $C_n(X \times S^0)/\tau C_n(X) \cong C_n(X)$.

::: pf-proof

::: pf-step

$\tau C_n(X) = \{(c, c) : c \in C_n(X)\}$.

::: pf-proof

Step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s3-2}

The map $(a, b) \mapsto a - b$ has kernel exactly $\{(c, c)\}$ and is surjective.

::: pf-proof

$(a, b) \mapsto a - b$ vanishes iff $a = b$; and $a \mapsto (a, 0) \mapsto a$ shows surjectivity.

:::

:::

::: pf-step

Hence $C_n(X) \oplus C_n(X) / \{(c,c)\} \cong C_n(X)$ via the difference map.

::: pf-proof

first isomorphism theorem applied to step [](#s3-2){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s4}

The transfer sequence is therefore
$$\cdots \to H_n(X) \xrightarrow{\Delta_*} H_n(X) \oplus H_n(X) \xrightarrow{\delta_*} H_n(X) \to H_{n-1}(X) \to \cdots$$
where $\Delta_*(x) = (x, x)$ and $\delta_*(a, b) = a - b$.

::: pf-proof

apply the long exact sequence in homology to the short exact sequence of steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

The connecting homomorphisms $H_n(X) \to H_{n-1}(X)$ are all zero.

::: pf-proof

$\delta_*$ is surjective (since $(a, 0) \mapsto a$), so the map out of $H_n(X)$ in the sequence is zero.

:::

:::

::: {.pf-step #s6}

Hence the transfer sequence splits into short exact sequences
$$0 \to H_n(X) \xrightarrow{\Delta_*} H_n(X) \oplus H_n(X) \xrightarrow{\delta_*} H_n(X) \to 0$$
for each $n$.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref}; the sequence is exact and the connecting maps vanish.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} make the transfer sequence explicit: it is the split short exact sequence with diagonal inclusion and difference projection.

:::

:::

:::
