---
schema: qual/card@1
id: P-CASP25E
kind: problem
title: "Bounded holomorphic sequence converging on a convergent sequence converges uniformly on compact subsets"
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Uniform Convergence
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source allowed repeated z_m, and z_m = 0 with f_n(z) = (-1)^n z is a counterexample; the statement now takes the z_m distinct.'
---

::: {.problem}
Let $f_n : \DD \to \CC$ be a bounded sequence of holomorphic functions, and let $\{z_m\}_{m \geq 1}$ be a sequence of distinct points in $\DD$ that converges in $\DD$.
Assume that $\lim_{n \to \infty} f_n(z_m)$ exists for all $m \geq 1$.
Show that the sequence $\{f_n\}$ converges uniformly on compact subsets of $\DD$.
:::

::: {.solution}
Let $z_m \to z_\ast \in \DD$, and $\abs{f_n} \le M$ on $\DD$ for all $n$.

::: pf

::: {.pf-step #montel}

Every subsequence of $(f_n)$ has a further subsequence converging uniformly on compact subsets of $\DD$ to a holomorphic function.

::: pf-proof

The family is uniformly bounded, so it is normal by Montel's theorem, and locally uniform limits of holomorphic functions are holomorphic.

:::

:::

::: {.pf-step #unique-limit}

All the limits in step [](#montel){.pf-ref} are one function $g$.

::: pf-proof

If $f_{n_k} \to g_1$ and $f_{n'_k} \to g_2$ locally uniformly, then $g_1(z_m) = \lim_n f_n(z_m) = g_2(z_m)$ for every $m$. The $z_m$ are distinct and converge to $z_\ast \in \DD$, so $z_\ast$ is an accumulation point in $\DD$ of the set where $g_1 = g_2$, and the identity theorem gives $g_1 = g_2$ on the connected set $\DD$.

:::

:::

::: pf-qed

Suppose $(f_n)$ does not converge to $g$ uniformly on some compact $K \subseteq \DD$. Then there are $\eps > 0$ and a subsequence with $\sup_K \abs{f_{n_k} - g} \ge \eps$ for all $k$. By step [](#montel){.pf-ref} it has a further subsequence converging locally uniformly, and by step [](#unique-limit){.pf-ref} its limit is $g$, so $\sup_K$ of the difference tends to $0$, a contradiction.

:::

:::

:::
