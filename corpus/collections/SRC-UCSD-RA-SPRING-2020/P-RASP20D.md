---
schema: qual/card@1
id: P-RASP20D
kind: problem
title: "Packing compact sets with positive measure in a Radon measure space"
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
Let $X$ be a locally compact Hausdorff space and $\mu$ a Radon measure on $X$.
Assume that $\mu(X) = \infty$.
Let $A_n > 0$ ($n = 1, 2, \ldots$). Prove that for each $n \in \mathbb{N}$ there exist a compact subset $K_n$ of $X$, a precompact open subset $U_n$ of $X$, and a function $f_n \in C_c(X, [0,1])$ such that $\mu(K_n) > A_n$ and $K_n \prec f_n \prec U_n$ (i.e., $f_n = 1$ on $K_n$ and $\operatorname{supp}(f_n) \subseteq U_n$), and that all the open subsets $U_n$ ($n = 1, 2, \ldots$) are pairwise disjoint.
:::

::: {.solution}
<1>1. Since $\mu$ is a Radon measure and $\mu(X) = \infty$, for each $n$ there is a compact set $C_n$ with $\mu(C_n) > A_n + \sum_{i<n} \mu(\overline{U_i})$.
::: {.proof}
a Radon measure is inner regular on open sets, so $\mu(X) = \sup\{\mu(K) : K \text{ compact}\} = \infty$; hence we can find compact sets of arbitrarily large measure.
:::

<1>2. We construct the $K_n, U_n, f_n$ inductively, choosing them to be pairwise disjoint.
::: {.proof}
induction on $n$.
:::

<1>3. Inductive step: given disjoint precompact open sets $U_1, \ldots, U_{n-1}$ already chosen, choose a compact $K_n$ disjoint from $\bigcup_{i<n} \overline{U_i}$ with $\mu(K_n) > A_n$.
<2>1. $X \setminus \bigcup_{i<n} \overline{U_i}$ is open and has infinite measure.
::: {.proof}
$\bigcup_{i<n} \overline{U_i}$ is compact (finite union of compact closures of precompact sets), hence has finite measure (Radon measures are finite on compact sets); since $\mu(X) = \infty$, the complement has infinite measure.
:::
<2>2. Hence there is a compact $K_n \subseteq X \setminus \bigcup_{i<n} \overline{U_i}$ with $\mu(K_n) > A_n$.
::: {.proof}
inner regularity of the Radon measure on the open set $X \setminus \bigcup_{i<n} \overline{U_i}$.
:::

<1>4. Choose a precompact open $U_n$ with $K_n \subseteq U_n$ and $U_n$ disjoint from $\bigcup_{i<n} \overline{U_i}$.
::: {.proof}
$X$ is locally compact Hausdorff, so $K_n$ has a precompact open neighborhood; shrink it to avoid the compact set $\bigcup_{i<n} \overline{U_i}$.
:::

<1>5. By Urysohn's lemma, there is $f_n \in C_c(X, [0,1])$ with $f_n = 1$ on $K_n$ and $\operatorname{supp}(f_n) \subseteq U_n$.
::: {.proof}
Urysohn's lemma for locally compact Hausdorff spaces.
:::

<1>6. Hence the $K_n, U_n, f_n$ satisfy all the required conditions, with the $U_n$ pairwise disjoint.
::: {.proof}
<1>3–<1>5 and the induction.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
