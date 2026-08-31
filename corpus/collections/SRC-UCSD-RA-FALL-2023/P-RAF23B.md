---
schema: qual/card@1
id: P-RAF23B
kind: problem
title: "Dilation converges in L^1"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
For $a > 0$, let $(S_a f)(x) = f(x/a)$ for Lebesgue measurable functions $f$ on $\mathbb{R}$.
Then for any $f \in L^1(\mathbb{R}, m)$, $S_a f \to f$ in $L^1$ as $a \to 1$.
:::

::: {.solution}
**Goal.** Show $S_a f \to f$ in $L^1$ as $a \to 1$ for $f \in L^1$.

<1>1. $\|S_a f\|_1 = a \|f\|_1$.
::: {.proof}
$\int |f(x/a)|\,dx = a\int |f(y)|\,dy$ (substitute $y = x/a$).
:::

<1>2. It suffices to prove the result for a dense class (e.g. continuous functions with compact support).
::: {.proof}
the operators $S_a$ are uniformly bounded in $a$ near $1$ (since $\|S_a\| = a \to 1$), so by a standard density argument, convergence on a dense set implies convergence on all of $L^1$.
:::

<1>3. For $f$ continuous with compact support, $S_a f \to f$ in $L^1$.
<2>1. $S_a f$ is supported in a fixed compact set for $a$ near $1$.
::: {.proof}
if $\operatorname{supp} f \subseteq [-M, M]$, then $\operatorname{supp} S_a f \subseteq [-aM, aM]$, which is bounded for $a$ near $1$.
:::
<2>2. $S_a f \to f$ uniformly.
::: {.proof}
$f$ is uniformly continuous, so $|f(x/a) - f(x)| \to 0$ uniformly as $a \to 1$.
:::
<2>3. Hence $S_a f \to f$ in $L^1$.
::: {.proof}
uniform convergence on a fixed compact set implies $L^1$ convergence.
:::

<1>4. Hence $S_a f \to f$ in $L^1$ for all $f \in L^1$.
::: {.proof}
<1>2 and <1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4 is the claim.
:::
:::
