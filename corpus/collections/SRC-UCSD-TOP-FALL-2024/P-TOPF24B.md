---
schema: qual/card@1
id: P-TOPF24B
kind: problem
title: Examples separating $\pi_2$ and $H_2$
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card had the right two examples (T^2 and RP^2) with the right
    reasons, but as label-steps with empty proofs over eight nested one-sentence claims. It is
    now five proved steps: the covering R^2 -> T^2 giving pi_2(T^2) = 0; the Kuenneth
    computation of H_2(T^2); the covering S^2 -> RP^2 together with Hurewicz for pi_2(S^2); the
    cellular chain complex of RP^2 with d_2 = x2 and the kernel computed; and the conclusion,
    which now says what the pair of examples shows. Not claimed: a retained solution set; the
    collection's provenance is the examination paper only.
---

::: {.problem}
Give an example
(a) of a space $X$ with $\pi_2(X) = 0$ and $H_2(X) \neq 0$ and
(b) of a space $Y$ with $\pi_2(Y) \neq 0$ and $H_2(Y) = 0$.
:::

::: {.solution}
Throughout $\pi_{n}$ and $H_{n}$ are homotopy and integral singular homology groups, and for a covering map $p\colon\tilde X \to X$ with $\tilde X$ simply connected the induced map $p_{*}\colon\pi_{n}(\tilde X) \to \pi_{n}(X)$ is an isomorphism for every $n \ge 2$. The collection's `provenance` is the Fall 2024 examination paper, and no solutions sheet accompanies it, so the examples below are the card's own.

::: pf

::: {.pf-step #a-pi2}
(a) For $X = T^{2} = S^{1} \times S^{1}$ one has $\pi_{2}(X) = 0$.

::: pf-proof
The universal covering $\RR^{2} \to T^{2}$ is a covering with simply connected total space, so it induces an isomorphism $\pi_{2}(\RR^{2}) \to \pi_{2}(T^{2})$. The space $\RR^{2}$ is contractible, hence all of its homotopy groups vanish, and in particular $\pi_{2}(\RR^{2}) = 0$; so $\pi_{2}(T^{2}) = 0$.

:::

:::

::: {.pf-step #a-h2}
(a) For $X = T^{2}$ one has $H_{2}(X) \cong \ZZ \ne 0$.

::: pf-proof
By the Künneth formula for the product of two circles, $H_{2}(S^{1}\times S^{1}) \cong \bigoplus_{i+j=2}H_{i}(S^{1})\otimes H_{j}(S^{1}) \cong H_{1}(S^{1})\otimes H_{1}(S^{1}) \cong \ZZ\otimes\ZZ \cong \ZZ$, the other summands being zero because $H_{i}(S^{1}) = 0$ for $i \ge 2$. So $T^{2}$ has the required $\pi_{2} = 0$ and $H_{2} \ne 0$.

:::

:::

::: {.pf-step #b-pi2}
(b) For $Y = \RP^{2}$ one has $\pi_{2}(Y) \cong \ZZ \ne 0$.

::: pf-proof
The quotient $S^{2} \to \RP^{2}$ by the antipodal action is a covering with simply connected total space, so it induces an isomorphism $\pi_{2}(S^{2}) \to \pi_{2}(\RP^{2})$, and $\pi_{2}(S^{2}) \cong \ZZ$ by the Hurewicz theorem applied to the simply connected space $S^{2}$, whose $H_{2}(S^{2}) = \ZZ$.

:::

:::

::: {.pf-step #b-h2}
(b) For $Y = \RP^{2}$ one has $H_{2}(Y) = 0$.

::: pf-proof
Give $\RP^{2}$ the CW structure with one cell in each dimension $0, 1, 2$. The cellular chain complex is $0 \to \ZZ \xrightarrow{d_{2}} \ZZ \xrightarrow{d_{1}} \ZZ \to 0$, and $d_{2}$ is multiplication by the degree of the attaching map of the $2$-cell, which is the antipodal map $S^{1} \to S^{1}$ of degree $2$; hence $d_{2} = \times 2$ and $H_{2}(\RP^{2}) = \ker(d_{2}) = \ker(\times 2: \ZZ \to \ZZ) = 0$, while $H_{1} = \coker(d_{2}) = \ZZ/2$ as it must be.

:::

:::

::: pf-step
The examples are $\boxed{X = T^{2}}$ with $\pi_{2}(X) = 0$ and $H_{2}(X) = \ZZ$, and $\boxed{Y = \RP^{2}}$ with $\pi_{2}(Y) = \ZZ$ and $H_{2}(Y) = 0$.

::: pf-proof
Steps [](#a-pi2){.pf-ref} and [](#a-h2){.pf-ref} supply the first example, steps [](#b-pi2){.pf-ref} and [](#b-h2){.pf-ref} the second; together they show that neither $\pi_{2}$ nor $H_{2}$ determines the other in the presence of a nontrivial fundamental group.

:::

:::

:::
:::
