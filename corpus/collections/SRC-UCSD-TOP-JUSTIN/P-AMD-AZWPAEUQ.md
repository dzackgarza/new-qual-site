---
schema: qual/card@1
id: P-AMD-AZWPAEUQ
kind: problem
title: $H_*(\Sigma\RP^2 \times \RP^2; \ZZ)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Compute $H_*(\Sigma\RP^2 \cross \RP^2; \ZZ)$
:::

::: {.solution}
**Goal:** Compute the integral homology groups $H_k(\Sigma \mathbb{RP}^2 \times \mathbb{RP}^2; \mathbb{Z})$ for all $k \ge 0$.

::: pf

::: pf-step
Compute the homology of the factors $\Sigma \mathbb{RP}^2$ and $\mathbb{RP}^2$.

::: pf-proof

::: pf-step
The homology of the real projective plane $\mathbb{RP}^2$ is:

- $H_0(\mathbb{RP}^2) \cong \mathbb{Z}$,

- $H_1(\mathbb{RP}^2) \cong \mathbb{Z}/2\mathbb{Z}$,

- $H_2(\mathbb{RP}^2) = 0$,

- $H_k(\mathbb{RP}^2) = 0$ for $k \ge 3$.
:::

::: pf-step
By the suspension isomorphism $\widetilde{H}_k(\Sigma X) \cong \widetilde{H}_{k-1}(X)$, the reduced homology of $\Sigma \mathbb{RP}^2$ is:

- $H_0(\Sigma \mathbb{RP}^2) \cong \mathbb{Z}$,

- $H_1(\Sigma \mathbb{RP}^2) \cong \widetilde{H}_0(\mathbb{RP}^2) = 0$,

- $H_2(\Sigma \mathbb{RP}^2) \cong \widetilde{H}_1(\mathbb{RP}^2) \cong \mathbb{Z}/2\mathbb{Z}$,

- $H_3(\Sigma \mathbb{RP}^2) \cong \widetilde{H}_2(\mathbb{RP}^2) = 0$,

- $H_k(\Sigma \mathbb{RP}^2) = 0$ for $k \ge 4$.
:::

::: pf-qed
Standard cellular homology of $\mathbb{RP}^2$ and suspension theorem.
:::

:::

:::

::: pf-step
Apply the Künneth formula for homology.

::: pf-proof

::: pf-step
For topological spaces $A$ and $B$, the Künneth formula over PID $\mathbb{Z}$ gives a split short exact sequence: $$0 \to \bigoplus_{i+j=k} (H_i(A) \otimes_\mathbb{Z} H_j(B)) \to H_k(A \times B) \to \bigoplus_{i+j=k-1} \operatorname{Tor}_1^\mathbb{Z}(H_i(A), H_j(B)) \to 0.$$
:::

::: pf-step
Here $A = \Sigma \mathbb{RP}^2$ and $B = \mathbb{RP}^2$.
:::

::: {.pf-step #s2-3}
Tensor products $H_i(A) \otimes H_j(B)$:

- $k = 0$: $H_0(A) \otimes H_0(B) = \mathbb{Z} \otimes \mathbb{Z} \cong \mathbb{Z}$.

- $k = 1$: $(H_0(A) \otimes H_1(B)) \oplus (H_1(A) \otimes H_0(B)) = (\mathbb{Z} \otimes \mathbb{Z}/2) \oplus (0 \otimes \mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z}$.

- $k = 2$: $(H_0(A) \otimes H_2(B)) \oplus (H_1(A) \otimes H_1(B)) \oplus (H_2(A) \otimes H_0(B)) = 0 \oplus 0 \oplus (\mathbb{Z}/2 \otimes \mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z}$.

- $k = 3$: $(H_2(A) \otimes H_1(B)) \oplus (H_3(A) \otimes H_0(B)) = (\mathbb{Z}/2 \otimes \mathbb{Z}/2) \oplus 0 \cong \mathbb{Z}/2\mathbb{Z}$.

- $k \ge 4$: All tensor terms are 0.
:::

::: {.pf-step #s2-4}
Tor terms $\operatorname{Tor}_1^\mathbb{Z}(H_i(A), H_j(B))$:

- Recall $\operatorname{Tor}(\mathbb{Z}, -) = 0$ and $\operatorname{Tor}(\mathbb{Z}/2, \mathbb{Z}/2) \cong \mathbb{Z}/2\mathbb{Z}$.

- For $i+j = 3$, the only non-zero term is $i = 2, j = 1$: $\operatorname{Tor}_1(H_2(A), H_1(B)) = \operatorname{Tor}_1(\mathbb{Z}/2, \mathbb{Z}/2) \cong \mathbb{Z}/2\mathbb{Z}$.
  This contributes to $k = (i+j) + 1 = 4$.

- For all other $i, j$, at least one factor is free ($\mathbb{Z}$ or $0$), so all other Tor terms vanish.
:::

::: pf-qed
The Künneth formula expresses $H_k(A \times B)$ as the direct sum of the tensor terms over $i + j = k$ and the Tor terms over $i + j = k - 1$; the computations in steps [](#s2-3){.pf-ref} and [](#s2-4){.pf-ref} evaluate each of these terms.
:::

:::

:::

::: {.pf-step #s3}
Combine terms for each dimension $k$.

::: pf-proof

::: {.pf-step #s3-1}
$k = 0$: $H_0 \cong \mathbb{Z}$.
:::

::: {.pf-step #s3-2}
$k = 1$: $H_1 \cong \mathbb{Z}/2\mathbb{Z}$.
:::

::: {.pf-step #s3-3}
$k = 2$: $H_2 \cong \mathbb{Z}/2\mathbb{Z}$.
:::

::: {.pf-step #s3-4}
$k = 3$: $H_3 \cong \mathbb{Z}/2\mathbb{Z}$.
:::

::: {.pf-step #s3-5}
$k = 4$: $H_4 \cong \operatorname{Tor}_1(H_2(A), H_1(B)) \cong \mathbb{Z}/2\mathbb{Z}$.
:::

::: {.pf-step #s3-6}
$k \ge 5$: $H_k = 0$.
:::

::: pf-qed
Each $H_k$ is the direct sum of the tensor terms (from step [](#s2-3){.pf-ref}) and the Tor terms (from step [](#s2-4){.pf-ref}) in that degree; summing them gives the groups listed in steps [](#s3-1){.pf-ref}, [](#s3-2){.pf-ref}, [](#s3-3){.pf-ref}, [](#s3-4){.pf-ref}, [](#s3-5){.pf-ref}, and [](#s3-6){.pf-ref}.
:::

:::

:::

::: pf-step
Conclusion.

::: pf-proof

::: pf-step
The homology groups are: $$H_k(\Sigma \mathbb{RP}^2 \times \mathbb{RP}^2; \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & k = 0, \\ \mathbb{Z}/2\mathbb{Z} & k = 1, 2, 3, 4, \\ 0 & k \ge 5. \end{cases}$$

::: pf-proof
The groups computed in step [](#s3){.pf-ref} assemble into the stated description of $H_k$ for all $k \ge 0$.
:::

:::

:::

:::

:::
:::
