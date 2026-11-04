---
schema: qual/card@1
id: E-HAT-3.1-9
kind: problem
title: Degree $d$ maps act on $H^n(S^n;G)$ by multiplication by $d$
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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.1, Exercise 9; it matches the printed text. The card makes the implicit $n>0$ of the degree explicit.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the Kronecker pairing argument: naturality gives
    $\langle f^*\alpha,[S^n]\rangle=\langle\alpha,f_*[S^n]\rangle=d\langle\alpha,[S^n]\rangle$, and
    evaluation on the fundamental class is an isomorphism $H^n(S^n;G)\cong G$, so
    $f^*\alpha=d\alpha$.
---

::: {.problem}
For $n>0$, show that if $f: S^n \to S^n$ has degree $d$ then $f^*: H^n(S^n; G) \to H^n(S^n; G)$ is multiplication by $d$.
:::

::: {.solution}

::: pf

::: pf-step

$H^n(S^n; G) \cong G$ and $H_n(S^n) \cong \ZZ$, with the natural pairing $H^n(S^n; G) \times H_n(S^n) \to G$ given by evaluation.

::: pf-proof

standard computation of the (co)homology of $S^n$.

:::

:::

::: pf-step

Let $\alpha \in H^n(S^n; G)$ and $[S^n] \in H_n(S^n)$ the fundamental class.

::: pf-proof

choose a cohomology class and the fundamental class.

:::

:::

::: {.pf-step #s3}

By naturality of the Kronecker pairing, $\langle f^*\alpha, [S^n] \rangle = \langle \alpha, f_*[S^n] \rangle$.

::: pf-proof

naturality of the evaluation pairing.

:::

:::

::: {.pf-step #s4}

$f_*[S^n] = d[S^n]$ (by definition of degree).

::: pf-proof

the degree $d$ is defined by $f_*[S^n] = d[S^n]$.

:::

:::

::: {.pf-step #s5}

Hence $\langle f^*\alpha, [S^n] \rangle = \langle \alpha, d[S^n] \rangle = d\langle \alpha, [S^n] \rangle$.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Since the pairing with $[S^n]$ identifies $H^n(S^n; G)$ with $G$ (it is an isomorphism), $f^*\alpha = d\alpha$.

::: pf-proof

Step [](#s5){.pf-ref} (the pairing $\alpha \mapsto \langle \alpha, [S^n] \rangle$ is an isomorphism $H^n(S^n;G) \to G$).

:::

:::

::: {.pf-step #s7}

Hence $f^*$ is multiplication by $d$.

::: pf-proof

Step [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

:::
