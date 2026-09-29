---
schema: qual/card@1
id: P-BERK77S-15
kind: problem
title: A compact-space subsequence criterion for convergence
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    If the sequence failed to converge to x, an epsilon-separated
    subsequence would exist; compactness gives it a convergent
    subsubsequence, whose limit must be x, contradicting the separation.
    For noncompact A={0,1,2,...}, the sequence 0,1,0,2,0,3,... has every
    convergent subsequence converging to 0 but does not itself converge.
---

::: {.problem}
Let $A\subset\mathbb R^n$ be compact, let $x\in A$, and let $(x_i)$ be a sequence in $A$ such that every convergent subsequence of $(x_i)$ converges to $x$.

1. Prove that the entire sequence $(x_i)$ converges to $x$.
2. Give an example showing that if $A$ is not compact, the conclusion in part 1 need not hold.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose, for contradiction, that $(x_i)$ does not converge to $x$.
Then there are an $\varepsilon>0$ and a subsequence
$$
(x_{i_k})
$$
such that
$$
\norm{x_{i_k}-x}\geq\varepsilon
$$
for every $k$.

::: pf-proof

Failure of $x_i\to x$ means that there is an $\varepsilon>0$ such that for
every index $N$ there is some $i\geq N$ with
$$
\norm{x_i-x}\geq\varepsilon.
$$
Choose such indices inductively with
$$
i_1<i_2<\cdots.
$$

:::

:::

::: {.pf-step #s2}

The subsequence $(x_{i_k})$ has a convergent subsequence.

::: pf-proof

Every term $x_{i_k}$ lies in the compact set $A$. Sequential compactness of
compact subsets of $\RR^n$ therefore gives indices
$$
k_1<k_2<\cdots
$$
and a point $y\in A$ such that
$$
x_{i_{k_j}}\longrightarrow y.
$$

:::

:::

::: {.pf-step #s3}

The limit in step [](#s2){.pf-ref} must be
$$
y=x.
$$

::: pf-proof

The sequence $(x_{i_{k_j}})$ is a convergent subsequence of the original
sequence $(x_i)$. By the hypothesis of the problem, every such subsequence
converges to $x$. Limits in $\RR^n$ are unique, so $y=x$.

:::

:::

::: {.pf-step #s4}

The original sequence converges to $x$.

::: pf-proof

By step [](#s1){.pf-ref},
$$
\norm{x_{i_{k_j}}-x}\geq\varepsilon
$$
for every $j$. But steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give
$$
x_{i_{k_j}}\longrightarrow x,
$$
so
$$
\norm{x_{i_{k_j}}-x}\longrightarrow0.
$$
This contradiction proves that the supposition in step [](#s1){.pf-ref} was false.
Hence $x_i\to x$.

:::

:::

::: {.pf-step #s5}

For part (2), take
$$
A=\{0,1,2,3,\ldots\}\subset\RR,
\qquad
x=0,
$$
and define
$$
x_{2n}=0,
\qquad
x_{2n-1}=n
$$
for $n\geq1$.

::: pf-proof

The set $A$ is unbounded, hence not compact. The displayed rule defines a
sequence in $A$.

:::

:::

::: {.pf-step #s6}

Every convergent subsequence of the sequence in step [](#s5){.pf-ref} converges
to $0$.

::: pf-proof

Every convergent sequence in $\RR$ is bounded. For any $M>0$, only
finitely many odd-indexed terms
$$
x_{2n-1}=n
$$
lie in $[-M,M]$. Thus a bounded subsequence can contain only finitely many
odd-indexed terms. Every convergent subsequence is therefore eventually
made entirely of the even-indexed terms, all of which equal $0$. Hence it
converges to $0$.

:::

:::

::: {.pf-step #s7}

The full sequence in step [](#s5){.pf-ref} does not converge to $0$.

::: pf-proof

Its odd-indexed subsequence is
$$
1,2,3,\ldots,
$$
which does not converge to $0$. Hence the full sequence cannot converge to
$0$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves part (1), while steps [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} give the required
noncompact counterexample for part (2).

:::

:::

:::
