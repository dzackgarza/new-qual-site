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
::: pf

::: pf-step
Compute the homology of the factors $\Sigma \RP^2$ and $\RP^2$.

::: pf-proof

::: pf-step
The homology of the real projective plane $\RP^2$ is:

- $H_0(\RP^2) \cong \ZZ$,

- $H_1(\RP^2) \cong \ZZ/2\ZZ$,

- $H_2(\RP^2) = 0$,

- $H_k(\RP^2) = 0$ for $k \ge 3$.
:::

::: pf-step
By the suspension isomorphism $\widetilde{H}_k(\Sigma X) \cong \widetilde{H}_{k-1}(X)$, the reduced homology of $\Sigma \RP^2$ is:

- $H_0(\Sigma \RP^2) \cong \ZZ$,

- $H_1(\Sigma \RP^2) \cong \widetilde{H}_0(\RP^2) = 0$,

- $H_2(\Sigma \RP^2) \cong \widetilde{H}_1(\RP^2) \cong \ZZ/2\ZZ$,

- $H_3(\Sigma \RP^2) \cong \widetilde{H}_2(\RP^2) = 0$,

- $H_k(\Sigma \RP^2) = 0$ for $k \ge 4$.
:::

::: pf-qed
Standard cellular homology of $\RP^2$ and suspension theorem.
:::

:::

:::

::: pf-step
Apply the Künneth formula for homology.

::: pf-proof

::: pf-step
For topological spaces $A$ and $B$, the Künneth formula over PID $\ZZ$ gives a split short exact sequence: $$0 \to \bigoplus_{i+j=k} (H_i(A) \otimes_\ZZ H_j(B)) \to H_k(A \times B) \to \bigoplus_{i+j=k-1} \operatorname{Tor}_1^\ZZ(H_i(A), H_j(B)) \to 0.$$
:::

::: pf-step
Here $A = \Sigma \RP^2$ and $B = \RP^2$.
:::

::: {.pf-step #s2-3}
Tensor products $H_i(A) \otimes H_j(B)$:

- $k = 0$: $H_0(A) \otimes H_0(B) = \ZZ \otimes \ZZ \cong \ZZ$.

- $k = 1$: $(H_0(A) \otimes H_1(B)) \oplus (H_1(A) \otimes H_0(B)) = (\ZZ \otimes \ZZ/2) \oplus (0 \otimes \ZZ) \cong \ZZ/2\ZZ$.

- $k = 2$: $(H_0(A) \otimes H_2(B)) \oplus (H_1(A) \otimes H_1(B)) \oplus (H_2(A) \otimes H_0(B)) = 0 \oplus 0 \oplus (\ZZ/2 \otimes \ZZ) \cong \ZZ/2\ZZ$.

- $k = 3$: $(H_2(A) \otimes H_1(B)) \oplus (H_3(A) \otimes H_0(B)) = (\ZZ/2 \otimes \ZZ/2) \oplus 0 \cong \ZZ/2\ZZ$.

- $k \ge 4$: All tensor terms are 0.
:::

::: {.pf-step #s2-4}
Tor terms $\operatorname{Tor}_1^\ZZ(H_i(A), H_j(B))$:

- Recall $\operatorname{Tor}(\ZZ, -) = 0$ and $\operatorname{Tor}(\ZZ/2, \ZZ/2) \cong \ZZ/2\ZZ$.

- For $i+j = 3$, the only non-zero term is $i = 2, j = 1$: $\operatorname{Tor}_1(H_2(A), H_1(B)) = \operatorname{Tor}_1(\ZZ/2, \ZZ/2) \cong \ZZ/2\ZZ$.
  This contributes to $k = (i+j) + 1 = 4$.

- For all other $i, j$, at least one factor is free ($\ZZ$ or $0$), so all other Tor terms vanish.
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
$k = 0$: $H_0 \cong \ZZ$.
:::

::: {.pf-step #s3-2}
$k = 1$: $H_1 \cong \ZZ/2\ZZ$.
:::

::: {.pf-step #s3-3}
$k = 2$: $H_2 \cong \ZZ/2\ZZ$.
:::

::: {.pf-step #s3-4}
$k = 3$: $H_3 \cong \ZZ/2\ZZ$.
:::

::: {.pf-step #s3-5}
$k = 4$: $H_4 \cong \operatorname{Tor}_1(H_2(A), H_1(B)) \cong \ZZ/2\ZZ$.
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
The homology groups are: $$H_k(\Sigma \RP^2 \times \RP^2; \ZZ) \cong \begin{cases} \ZZ & k = 0, \\ \ZZ/2\ZZ & k = 1, 2, 3, 4, \\ 0 & k \ge 5. \end{cases}$$

::: pf-proof
The groups computed in step [](#s3){.pf-ref} assemble into the stated description of $H_k$ for all $k \ge 0$.
:::

:::

:::

:::

:::
:::
