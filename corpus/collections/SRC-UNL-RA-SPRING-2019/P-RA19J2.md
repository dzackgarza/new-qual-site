---
schema: qual/card@1
id: P-RA19J2
kind: problem
title: Boundedness and closedness of the self-maps of $[0,1]$ in $C_b([0,1])$
classification:
  areas:
  - real-analysis
  topics:
  - Function Spaces
  - Compactness
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Consider the following subset of the metric space $(C_b([0,1]),\rho_\infty)$: $$A:=\{f\in C_b([0,1]):f([0,1])\subseteq[0,1]\}.$$

(a) Determine whether $A$ is bounded, and if so what is its diameter.

(b) Determine whether $A$ is closed in $C_b([0,1])$.

(c) Determine whether $A$ is compact in $C_b([0,1])$.
:::

:::: {.solution}
**Goal:** For $A = \{f \in C_b([0,1]) : f([0,1]) \subseteq [0,1]\}$ in $(C_b[0,1], \rho_\infty)$: (a) bounded?
diameter?
(b) closed?
(c) compact?

<1>1. (a) $A$ is bounded, with diameter $1$.
<2>1. $\rho_\infty(f,g) \le 1$ for all $f, g \in A$.
Proof: $f(x), g(x) \in [0,1]$ for all $x$, so $|f(x) - g(x)| \le 1$.
<2>2. The diameter is exactly $1$.
Proof: the constant functions $0$ and $1$ are in $A$ and $\rho_\infty(0, 1) = 1$.
<2>3. Q.E.D. Proof: <2>1 and <2>2.

<1>2. (b) $A$ is closed in $C_b[0,1]$.
<2>1. Let $f_n \in A$ with $f_n \to f$ uniformly (in $\rho_\infty$); show $f \in A$.
<2>2. $f(x) \in [0,1]$ for every $x$.
Proof: $f(x) = \lim_n f_n(x)$ and each $f_n(x) \in [0,1]$, a closed set.
<2>3. Q.E.D. Proof: <2>2 shows $f([0,1]) \subseteq [0,1]$, so $f \in A$; $A$ is closed.

<1>3. (c) $A$ is NOT compact.
<2>1. $A$ is closed (by <1>2) and bounded (by <1>1), but not equicontinuous.
<2>2. The sequence $f_n(x) = x^n$ lies in $A$ and has no uniformly convergent subsequence.
Proof: each $f_n$ maps $[0,1]$ into $[0,1]$; any subsequence converges pointwise to the discontinuous limit $f(x) = 0$ on $[0,1)$, $f(1) = 1$, so no subsequence converges uniformly (a uniform limit of continuous functions is continuous).
<2>3. Arzelà–Ascoli: a subset of $C[0,1]$ is compact iff closed, bounded, and equicontinuous; $A$ fails equicontinuity.
Proof: <2>2 exhibits a sequence without a convergent subsequence, so $A$ is not sequentially compact, hence not compact.
<2>4. Q.E.D. Proof: <2>2–<2>3 show $A$ is not compact.
:::
