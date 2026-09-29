---
schema: qual/card@1
id: E-F46JG
kind: problem
title: Every topological group is completely regular
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Prove the following.

Theorem.
Every topological group is completely regular.

Proof.
Let $V_0$ be a neighborhood of the identity element $e$, in the topological group $G$.
In general, choose $V_n$ to be a neighborhood of $e$ such that $V_n \cdot V_n \subset V_{n-1}$.
Consider the set of all dyadic rationals $p$, that is, all rational numbers of the form $k/2^n$, with $k$ and $n$ integers.
For each dyadic rational $p$ in $(0, 1]$, define an open set $U(p)$ inductively as follows: $U(1) = V_0$ and $U(\tfrac{1}{2}) = V_1$.
Given $n$, if $U(k/2^n)$ is defined for $0 < k/2^n \leq 1$, define

$$
U(1/2^{n+1}) = V_{n+1},
$$

$$
U((2k+1)/2^{n+1}) = V_{n+1} \cdot U(k/2^n)
$$

for $0 < k < 2^n$.
For $p \leq 0$, let $U(p) = \varnothing$, and for $p > 1$, let $U(p) = G$.
Show that

$$
V_n \cdot U(k/2^n) \subset U((k+1)/2^n)
$$

for all $k$ and $n$.
Proceed as in the Urysohn lemma.

This exercise is adapted from [M-Z], to which the reader is referred for further results on topological groups.
:::

::: {.solution}

::: pf

::: pf-step
We must show $V_n \cdot U(k/2^n) \subset U((k+1)/2^n)$ for all $k$ and $n$.

::: pf-proof
the claim to prove.
:::

:::

::: {.pf-step #n-zero-base-case}
We prove by induction on $n$. For $n = 0$: $U(0) = \varnothing$ and $U(1) = V_0$, so $V_0 \cdot U(0) = \varnothing \subset U(1)$.

::: pf-proof
base case.
:::

:::

::: pf-step
Assume the claim holds for $n$; we prove it for $n+1$.

::: pf-proof
induction step.
:::

:::

::: {.pf-step #even-k-definitions}
For $k$ even, $k = 2j$: $U(k/2^{n+1}) = U(j/2^n)$, and $U((k+1)/2^{n+1}) = U((2j+1)/2^{n+1}) = V_{n+1} \cdot U(j/2^n)$.

::: pf-proof
the definitions.
:::

:::

::: {.pf-step #even-k-conclusion}
Then $V_{n+1} \cdot U(k/2^{n+1}) = V_{n+1} \cdot U(j/2^n) = U((k+1)/2^{n+1})$.

::: pf-proof
Step [](#even-k-definitions){.pf-ref}.
:::

:::

::: {.pf-step #odd-k-definitions}
For $k$ odd, $k = 2j+1$: $U(k/2^{n+1}) = U((2j+1)/2^{n+1}) = V_{n+1} \cdot U(j/2^n)$, and $U((k+1)/2^{n+1}) = U((2j+2)/2^{n+1}) = U((j+1)/2^n)$.

::: pf-proof
the definitions.
:::

:::

::: {.pf-step #odd-k-conclusion}
Then $V_{n+1} \cdot U(k/2^{n+1}) = V_{n+1} \cdot V_{n+1} \cdot U(j/2^n) \subset V_n \cdot U(j/2^n) \subset U((j+1)/2^n) = U((k+1)/2^{n+1})$.

::: pf-proof
Step [](#odd-k-definitions){.pf-ref}, using $V_{n+1} \cdot V_{n+1} \subset V_n$ and the induction hypothesis.
:::

:::

::: {.pf-step #claim-proved-by-induction}
Hence $V_n \cdot U(k/2^n) \subset U((k+1)/2^n)$ for all $k, n$.

::: pf-proof
Steps [](#n-zero-base-case){.pf-ref}, [](#even-k-conclusion){.pf-ref}, [](#odd-k-conclusion){.pf-ref}.
:::

:::

::: {.pf-step #urysohn-construction}
Proceeding as in the Urysohn lemma, this defines a continuous function $f : G \to [0,1]$ with $f(e) = 0$ and $f = 1$ outside $V_0$, separating $e$ from the closed set $G \setminus V_0$.

::: pf-proof
the Urysohn-lemma construction using the nested open sets $U(p)$.
:::

:::

::: {.pf-step #g-completely-regular}
Hence $G$ is completely regular.

::: pf-proof
Step [](#urysohn-construction){.pf-ref} (every point can be separated from a closed set by a continuous function, using translation invariance).
:::

:::

::: pf-qed
Steps [](#claim-proved-by-induction){.pf-ref} and [](#g-completely-regular){.pf-ref}.
:::

:::

:::
