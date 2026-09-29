---
schema: qual/card@1
id: P-JHWCH
kind: problem
title: $\int(f+g)=\int f+\int g$ on $L^+$, countable additivity, and $\mu_f(E_j)\to\mu_f(E)$
  when $E_j\nearrow E$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
  - Continuity of Measure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
a. Prove that if $f, g\in L^+(\RR)$ then 
\[
\int(f +g) = \int f + \int g
.\]
  Extend this to establish that if $\ts{ f_k} \subseteq L^+(\RR^n)$ then
  \[
  \int \sum_k f_k = \sum_k \int f_k
  .\]

b. Let $\ts{E_j}_{j\in \NN} \subseteq \mathcal{M}(\RR^n)$ with $E_j \nearrow E$. 
  Use the countable additivity of $\mu_f$ on \( \mathcal{M}(\RR^n)  \) established above to show that
  \[
  \mu_f(E) = \lim_{j\to \infty } \mu_f(E_j)
  .\]
:::
::: {.solution}
Here $L^+$ is the set of measurable functions with values in $[0,\infty]$, and $\mu_f(A) = \int_A f$ for $f \in L^+$.

::: pf

::: {.pf-step #s1}

For $f, g \in L^+$, $\int (f + g) = \int f + \int g$.

::: pf-proof

::: {.pf-step #s1-1}

The identity holds for nonnegative simple $s = \sum_i a_i \chi_{A_i}$ and $t = \sum_j b_j \chi_{B_j}$, where $(A_i)$ and $(B_j)$ are finite measurable partitions of the domain.

::: pf-proof

$s + t = \sum_{i,j}(a_i + b_j)\chi_{A_i \cap B_j}$, so $\int (s+t) = \sum_{i,j}(a_i + b_j)\,m(A_i \cap B_j)$. Summing over $j$ first in the $a_i$ terms and over $i$ first in the $b_j$ terms gives $\sum_i a_i m(A_i) + \sum_j b_j m(B_j)$.

:::

:::

::: pf-qed

Choose simple $0 \le s_k \uparrow f$ and $0 \le t_k \uparrow g$. Then $s_k + t_k \uparrow f + g$, and the monotone convergence theorem with step [](#s1-1){.pf-ref} gives $\int(f+g) = \lim_k (\int s_k + \int t_k) = \int f + \int g$.

:::

:::

:::

::: {.pf-step #s2}

For $f_k \in L^+$, $\int \sum_k f_k = \sum_k \int f_k$.

::: pf-proof

By step [](#s1){.pf-ref} and induction, $\int\sum_{k=1}^N f_k = \sum_{k=1}^N\int f_k$. The partial sums increase to $\sum_k f_k$, so the monotone convergence theorem gives the claim.

:::

:::

::: pf-step

If $E_j \nearrow E$, then $\mu_f(E_j) \to \mu_f(E)$.

::: pf-proof

Put $E_0 = \emptyset$ and $D_k = E_k \setminus E_{k-1}$. The $D_k$ are disjoint with $\bigcup_k D_k = E$ and $\bigcup_{k \le j} D_k = E_j$. Step [](#s2){.pf-ref} applied to $f\chi_{D_k}$ gives countable additivity of $\mu_f$: $\mu_f(E) = \sum_k \mu_f(D_k)$. Step [](#s1){.pf-ref} gives $\mu_f(E_j) = \sum_{k \le j}\mu_f(D_k)$, the $j$th partial sum, which converges to $\mu_f(E)$.

:::

:::

:::

:::
