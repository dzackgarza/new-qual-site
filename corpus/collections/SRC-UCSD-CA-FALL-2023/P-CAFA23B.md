---
schema: qual/card@1
id: P-CAFA23B
kind: problem
title: "Convergence of uniformly bounded analytic functions with convergent coefficients"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $A_N(z) = \sum_{n=0}^{\infty} a_{Nn} z^n$ be a sequence of analytic functions on $\mathbb{D}$ which is uniformly bounded on compact subsets of $\mathbb{D}$.
Let $B(z) = \sum_{n=0}^{\infty} b_n z^n$ be an analytic function on $\mathbb{D}$ such that $\lim_{N \to \infty} a_{Nn} = b_n$ for each $n$.

(a) Prove that $A_N \to B$ as $N \to \infty$, uniformly on compact subsets of $\mathbb{D}$.

(b) Give an example showing that the conclusion in (a) may fail if uniform boundedness is dropped.
:::

::: {.solution}
**Goal.** (a) Uniformly bounded analytic functions with convergent coefficients converge uniformly on compact sets. (b) The conclusion fails without uniform boundedness.

::: pf

::: {.pf-step #s1}

(a) $A_N \to B$ uniformly on compact subsets of $\DD$.

::: pf-proof

::: pf-step

The family $\theset{A_N}$ is normal.

::: pf-proof

uniformly bounded on compact sets implies locally bounded, and Montel's theorem says a locally bounded family of holomorphic functions is normal (every subsequence has a subsequence converging uniformly on compact sets).

:::

:::

::: pf-step

Every convergent subsequence of $\theset{A_N}$ converges to $B$.

::: pf-proof

if $A_{N_k} \to C$ uniformly on compact sets, then the coefficients converge: $a_{N_k, n} \to c_n$ (coefficient of $C$); but $a_{N_k, n} \to b_n$ by hypothesis, so $c_n = b_n$ for all $n$, hence $C = B$.

:::

:::

::: pf-step

Hence the whole sequence $A_N \to B$ uniformly on compact sets.

::: pf-proof

a normal family where every convergent subsequence has the same limit $B$ converges to $B$ (if $A_N \not\to B$, some subsequence stays away from $B$, but that subsequence has a further subsequence converging to $B$, contradiction).

:::

:::

:::

:::

::: {.pf-step #s2}

(b) Counterexample without uniform boundedness.

::: pf-proof

::: pf-step

Take $A_N(z) = N z^N$.

::: pf-proof

$A_N$ is analytic on $\DD$ with $a_{Nn} = N$ if $n = N$ and $0$ otherwise.

:::

:::

::: pf-step

$a_{Nn} \to 0 = b_n$ for each fixed $n$.

::: pf-proof

for fixed $n$, $a_{Nn} = 0$ for all $N > n$, so $a_{Nn} \to 0$.

:::

:::

::: pf-step

So $B(z) = 0$.

::: pf-proof

all coefficients are $0$.

:::

:::

::: pf-step

But $A_N \not\to 0$ uniformly on compact sets.

::: pf-proof

on the compact set $\theset{z : |z| = 1/2}$, $|A_N(z)| = N/2^N \to 0$; instead use $A_N(z) = N z^N$ evaluated at $z = 1 - 1/N$: $|A_N(1 - 1/N)| = N(1 - 1/N)^N \to N/e \to \infty$, so the sequence is not uniformly bounded on the compact set $\theset{1 - 1/N : N \ge 2} \cup \theset{1}$ (which is compact), hence does not converge uniformly to $0$.

:::

:::

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a); step [](#s2){.pf-ref} gives the counterexample for (b).

:::

:::

:::
