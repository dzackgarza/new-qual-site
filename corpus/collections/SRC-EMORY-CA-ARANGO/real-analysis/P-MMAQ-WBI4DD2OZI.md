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
---

::: problem
State and prove Fatou's Lemma on a general measurable space.
:::

::: {.solution}
**Goal:** State and prove Fatou's Lemma on a general measure space.

<1>1. Statement of Fatou's Lemma.
<2>1. Let $(X, \mathcal M, \mu)$ be a measure space and $\{f_n\}$ a sequence of measurable functions with $f_n \geq 0$ for all $n$.
Then $$\int_X \liminf_{n \to \infty} f_n ~d\mu \leq \liminf_{n \to \infty} \int_X f_n ~d\mu.$$ Proof: This is the statement to be proved; both sides may be $+\infty$.
<2>2. Q.E.D. Proof: The statement is recorded for the proof below.

<1>2. Proof.
<2>1. Define $g_k \definedas \inf_{n \geq k} f_n$; then $g_k$ is measurable, $0 \leq g_k \leq f_n$ for all $n \geq k$, and $g_k$ increases to $\liminf_n f_n$ as $k \to \infty$.
Proof: Each $g_k$ is a countable infimum of measurable functions, hence measurable; $g_k \leq f_n$ for $n \geq k$ by definition; the sequence $(g_k)$ is nondecreasing; and $\lim_k g_k = \lim_k \inf_{n \geq k} f_n = \liminf_n f_n$ by definition of $\liminf$.
<2>2. Monotone convergence: $\int_X g_k ~d\mu \uparrow \int_X \liminf_n f_n ~d\mu$.
Proof: $g_k \uparrow \liminf f_n$ pointwise (<2>1) and the $g_k$ are nonnegative, so the monotone convergence theorem applies.
<2>3. For each fixed $k$, $\int_X g_k ~d\mu \leq \int_X f_n ~d\mu$ for every $n \geq k$, hence $\int_X g_k ~d\mu \leq \inf_{n \geq k} \int_X f_n ~d\mu$.
Proof: $g_k \leq f_n$ pointwise for $n \geq k$ (<2>1) and both are nonnegative, so monotonicity of the integral gives the inequality; taking the infimum over $n \geq k$ gives the second.
<2>4. Take the limit as $k \to \infty$: $$\int_X \liminf_n f_n ~d\mu = \lim_k \int_X g_k ~d\mu \leq \lim_k \inf_{n \geq k} \int_X f_n ~d\mu = \liminf_n \int_X f_n ~d\mu.$$ Proof: Left equality by <2>2; inequality by <2>3 (passing to the limit); right equality by definition of $\liminf$ applied to the sequence $\int_X f_n$.
<2>5. Q.E.D. Proof: This proves Fatou's Lemma.
:::
