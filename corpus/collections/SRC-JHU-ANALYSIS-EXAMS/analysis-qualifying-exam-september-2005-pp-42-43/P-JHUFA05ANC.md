---
schema: qual/card@1
id: P-JHUFA05ANC
kind: problem
title: "Weak convergence to zero on the circle"
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
3. Let $g _ { n }$ be a sequence of functions in $L ^ { 1 } ( S ^ { 1 } , d \theta )$ where $S ^ { 1 }$ is the unit circle $\{ e ^ { i \theta } : 0 \leq \theta \leq 2 \pi \}$ We say that $g _ { n } \ \to \ 0$ weakly if $\int_{S^1} g_n(e^{i\theta}) f(e^{i\theta})\,d\theta \to 0$ as $n \to \infty$ for all $f \in C ( S ^ { 1 } )$

Question: Suppose that $\left\{ g _ { n } \right\}$ is a sequence in $L ^ { 1 } ( S ^ { 1 } , d \theta )$ and $\int_{S^1} e^{ik\theta} g_n(e^{i\theta})\,d\theta \to 0$ as $n \to \infty$ for all $k \in \mathbb { Z }$ . Need $g _ { n } \to 0$ weakly?
Give either a proof or a counterexample.
:::

::: {.solution}
No. Let $g_n(e^{i\theta})\da ne^{in\theta}$.

::: pf

::: {.pf-step #s1}

For each fixed $k\in\ZZ$, $\int_{S^1}e^{ik\theta}g_n(e^{i\theta})\,d\theta\to0$.

::: pf-proof

The integral is $n\int_0^{2\pi}e^{i(k+n)\theta}\,d\theta$, which is $0$ whenever $n>\abs k$.

:::

:::

::: {.pf-step #s2}

$g_n$ does not converge weakly to $0$.

::: pf-proof

The functional $\Lambda_n(f)\da\int_{S^1}g_nf\,d\theta$ on the Banach space $C(S^1)$ has norm $\norm{g_n}_{L^1}=2\pi n$. If $\Lambda_n(f)\to0$ for every $f$, the uniform boundedness principle would give $\sup_n\norm{\Lambda_n}<\infty$, which is false.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} show that the sequence $g_n$ is a counterexample.

:::

:::

:::
