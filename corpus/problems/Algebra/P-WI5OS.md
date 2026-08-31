---
schema: qual/card@1
id: P-WI5OS
kind: problem
title: The center of $S_n$ is trivial for $n\geq 4$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Show that the center of $S_n$ for $n\geq 4$ (and in fact $n \ge 3$) is trivial.
:::

::: solution
**Goal:** Prove that $Z(S_n) = \{e\}$ for all $n \ge 3$.

<1>1. Strategy:
::: {.proof}
<2>1. Let $\sigma \in S_n$ with $\sigma \ne e$.
<2>2. We will construct a permutation $\tau \in S_n$ such that $\sigma \tau \ne \tau \sigma$.
:::

<1>2. Existence of moved elements:
::: {.proof}
<2>1. Since $\sigma \ne e$, there exists some $a \in \{1, \dots, n\}$ such that $\sigma(a) = b \ne a$.
<2>2. Since $n \ge 3$, the set $\{1, \dots, n\} \setminus \{a, b\}$ is non-empty. Let $c \in \{1, \dots, n\} \setminus \{a, b\}$.
:::

<1>3. Case 1: $\sigma(b) \ne a$ (i.e. $a, b, \sigma(b)$ are three distinct elements):
::: {.proof}
<2>1. Let $d = \sigma(b)$, with $d \notin \{a, b\}$.
<2>2. Choose the transposition $\tau = (b \ c)$, where $c \notin \{a, b\}$.
<2>3. Then $(\sigma \tau)(a) = \sigma(\tau(a)) = \sigma(a) = b$.
<2>4. On the other hand, $(\tau \sigma)(a) = \tau(\sigma(a)) = \tau(b) = c$.
<2>5. Since $b \ne c$, we have $\sigma \tau(a) \ne \tau \sigma(a)$, so $\sigma \tau \ne \tau \sigma$.
:::

<1>4. Case 2: $\sigma(b) = a$ (i.e. $(a \ b)$ is a 2-cycle in the disjoint cycle decomposition of $\sigma$):
::: {.proof}
<2>1. Since $n \ge 3$, pick $c \notin \{a, b\}$.
<2>2. Choose $\tau = (a \ c)$.
<2>3. Then $(\sigma \tau)(b) = \sigma(\tau(b)) = \sigma(b) = a$.
<2>4. On the other hand, $(\tau \sigma)(b) = \tau(\sigma(b)) = \tau(a) = c$.
<2>5. Since $a \ne c$, $\sigma \tau(b) \ne \tau \sigma(b)$, so $\sigma \tau \ne \tau \sigma$.
:::

<1>5. Conclusion:
::: {.proof}
In all cases, no non-identity permutation commutes with every transposition in $S_n$. Thus $Z(S_n) = \{e\}$ for all $n \ge 3$.
:::
:::
