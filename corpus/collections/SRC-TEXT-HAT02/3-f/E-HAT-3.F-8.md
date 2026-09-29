---
schema: qual/card@1
id: E-HAT-3.F-8
kind: problem
title: "Bockstein sequence on Moore spaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Show that for a Moore space $M(G, n)$ the Bockstein long exact sequence in cohomology associated to the short exact sequence of coefficient groups $0 \to A \to B \to C \to 0$ reduces to an exact sequence

$$0 \to \operatorname{Hom}(G,A) \to \operatorname{Hom}(G,B) \to \operatorname{Hom}(G,C) \to \operatorname{Ext}(G,A) \to \operatorname{Ext}(G,B) \to \operatorname{Ext}(G,C) \to 0.$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For a Moore space $M(G, n)$, $\widetilde H_n(M(G,n)) = G$ and $\widetilde H_i(M(G,n)) = 0$ for $i \neq n$.

::: pf-proof

definition of a Moore space.

:::

:::

::: {.pf-step #s2}

By the universal coefficient theorem, $H^n(M(G,n); A) \cong \operatorname{Hom}(G, A)$ and $H^{n+1}(M(G,n); A) \cong \operatorname{Ext}(G, A)$, with all other cohomology groups (in positive degrees) zero.

::: pf-proof

Step [](#s1){.pf-ref} and the universal coefficient theorem.

:::

:::

::: {.pf-step #s3}

The Bockstein long exact sequence associated to $0 \to A \to B \to C \to 0$ is
$$\cdots \to H^i(M; A) \to H^i(M; B) \to H^i(M; C) \xrightarrow{\beta} H^{i+1}(M; A) \to \cdots.$$

::: pf-proof

the long exact sequence in cohomology from a short exact sequence of coefficients.

:::

:::

::: {.pf-step #s4}

Since $H^i(M(G,n); \cdot) = 0$ except for $i = n$ and $i = n+1$, the long exact sequence collapses to the exact sequence
$$0 \to H^n(M;A) \to H^n(M;B) \to H^n(M;C) \to H^{n+1}(M;A) \to H^{n+1}(M;B) \to H^{n+1}(M;C) \to 0.$$

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} (all other terms vanish).

:::

:::

::: {.pf-step #s5}

Substituting step [](#s2){.pf-ref}, this is exactly
$$0 \to \operatorname{Hom}(G,A) \to \operatorname{Hom}(G,B) \to \operatorname{Hom}(G,C) \to \operatorname{Ext}(G,A) \to \operatorname{Ext}(G,B) \to \operatorname{Ext}(G,C) \to 0.$$

::: pf-proof

Step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref}.

:::

:::

:::
