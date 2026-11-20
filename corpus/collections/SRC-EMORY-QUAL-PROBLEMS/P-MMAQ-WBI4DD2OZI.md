---
schema: qual/card@1
id: P-MMAQ-WBI4DD2OZI
kind: problem
title: Fatou's lemma
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Fatou
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Real Analysis (2) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMRA2, whose solution repeats this tail-infimum argument."
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The closing step of the Fatou argument carried its justification as a run-in "Proof:" inside the
    claim, which STYLE-07 forbids, so the claim is now the displayed identity and the proof derives its
    three relations. Sources are cited by numbered statement: the monotone convergence theorem and the
    definition of the lower limit of a sequence. No page reference is written in the body of this card or
    in the event above. The statement is unchanged.
---

::: {.problem}
State and prove Fatou's Lemma on a general measurable space.
:::

::: {.solution}
**Fatou's lemma.** Let $(X, \mathcal M, \mu)$ be a measure space and $\{f_n\}$ a sequence of measurable functions with $f_n \geq 0$ for all $n$.
Then $$\int_X \liminf_{n \to \infty} f_n ~d\mu \leq \liminf_{n \to \infty} \int_X f_n ~d\mu,$$ where both sides may be $+\infty$.

::: pf

::: pf-step
Proof of Fatou's lemma.

::: pf-proof

::: {.pf-step #s1-1}
Define $g_k \coloneqq \inf_{n \geq k} f_n$; then $g_k$ is measurable, $0 \leq g_k \leq f_n$ for all $n \geq k$, and $g_k$ increases to $\liminf_n f_n$ as $k \to \infty$.

::: pf-proof
Each $g_k$ is a countable infimum of measurable functions, hence measurable; $g_k \leq f_n$ for $n \geq k$ by definition; the sequence $(g_k)$ is nondecreasing; and $\lim_k g_k = \lim_k \inf_{n \geq k} f_n = \liminf_n f_n$ by definition of $\liminf$.
:::

:::

::: {.pf-step #s1-2}
Monotone convergence: $\int_X g_k ~d\mu \uparrow \int_X \liminf_n f_n ~d\mu$.

::: pf-proof
$g_k \uparrow \liminf f_n$ pointwise (step [](#s1-1){.pf-ref}) and the $g_k$ are nonnegative, so the monotone convergence theorem applies.
:::

:::

::: {.pf-step #s1-3}
For each fixed $k$, $\int_X g_k ~d\mu \leq \int_X f_n ~d\mu$ for every $n \geq k$, hence $\int_X g_k ~d\mu \leq \inf_{n \geq k} \int_X f_n ~d\mu$.

::: pf-proof
$g_k \leq f_n$ pointwise for $n \geq k$ (step [](#s1-1){.pf-ref}) and both are nonnegative, so monotonicity of the integral gives the inequality; taking the infimum over $n \geq k$ gives the second.
:::

:::

::: {.pf-step #s1-4}
$$\int_X \liminf_n f_n ~d\mu = \lim_k \int_X g_k ~d\mu \leq \lim_k \inf_{n \geq k} \int_X f_n ~d\mu = \liminf_n \int_X f_n ~d\mu.$$

::: pf-proof
The functions $g_k$ increase to $\liminf_n f_n$ pointwise, by the definition of $g_k$ as the pointwise infimum over $n \ge k$, so the monotone convergence theorem identifies the limit of their integrals with the integral of the pointwise lower limit, which is the left equality. The inequality is step [](#s1-3){.pf-ref} passed to the limit in $k$, which preserves a non-strict inequality of extended real numbers. The right-hand side is $\lim_k \inf_{n\ge k}\int_X f_n\,d\mu$, which is the definition of the lower limit of the sequence of integrals.
:::

:::

::: pf-qed
The inequality of step [](#s1-4){.pf-ref} is the conclusion of Fatou's lemma.
:::

:::

:::

:::
:::
