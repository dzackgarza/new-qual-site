---
schema: qual/card@1
id: E-SMI-8000E-CY8
kind: problem
title: A transitive subgroup of $S_p$ containing a transposition is $S_p$
classification:
  areas:
  - algebra
  topics:
  - Symmetric Group
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Prove that if $H$ is a transitive subgroup of $S(n)$, any two of the equivalence classes defined in [[E-SMI-8000E-CY7]] have the same number of elements.
Hence a transitive subgroup of $S(p)$, where $p$ is prime, either contains no 2-cycles or all 2-cycles.
Thus a transitive subgroup of $S(p)$ containing one 2-cycle — e.g. a subgroup containing a 2-cycle and a $p$-cycle — is all of $S(p)$.
[Hint: use [[E-SMI-8000E-CY6]] and [[E-SMI-8000E-CY7]].]
:::

::: {.solution}
Let $\Omega = \{1, 2, \dots, n\}$, and let $\sim$ be the equivalence relation of [[E-SMI-8000E-CY7]]: $i \sim j$ if $i = j$ or $(i\,j) \in H$.

::: pf

::: {.pf-step #s1}

For every $\sigma \in H$ and every equivalence class $B$, the set $\sigma(B)$ is an equivalence class.

::: pf-proof

If $i \sim j$ with $i \ne j$, then $(\sigma(i)\,\sigma(j)) = \sigma (i\,j) \sigma^{-1} \in H$ because $H$ is closed under products and inverses, so $\sigma(i) \sim \sigma(j)$. Hence $\sigma$ maps each class into a class. Applying the same argument to $\sigma^{-1} \in H$ shows that $\sigma(B)$ is a whole class.

:::

:::

::: {.pf-step #s2}

If $H$ is transitive, all equivalence classes have the same number of elements.

::: pf-proof

Let $B$ and $B'$ be classes, and pick $x \in B$ and $y \in B'$. By transitivity there is $\sigma \in H$ with $\sigma(x) = y$. By step [](#s1){.pf-ref}, $\sigma(B)$ is the class containing $y$, namely $B'$. Since $\sigma$ is a bijection of $\Omega$, $|B'| = |\sigma(B)| = |B|$.

:::

:::

::: {.pf-step #s3}

If $n = p$ is prime and $H$ is transitive, then $H$ contains either no $2$-cycles or all $2$-cycles.

::: pf-proof

By step [](#s2){.pf-ref} the classes have a common size $m$, and $p = km$ where $k$ is the number of classes. Hence $m = 1$ or $m = p$. If $m = 1$, every class is a singleton, so $(i\,j) \notin H$ for all $i \ne j$. If $m = p$, there is one class, so $(i\,j) \in H$ for all $i \ne j$.

:::

:::

::: {.pf-step #s4}

A transitive subgroup $H \le S(p)$ containing a $2$-cycle is $S(p)$.

::: pf-proof

By step [](#s3){.pf-ref}, $H$ contains every $2$-cycle, and the $2$-cycles generate $S(p)$ ([[E-SMI-8000E-CY3]]).

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} are the three assertions. A subgroup containing a $p$-cycle $(a_1\,a_2\,\cdots\,a_p)$ is transitive on $\Omega$, since powers of the $p$-cycle carry $a_1$ to every $a_i$; so step [](#s4){.pf-ref} applies to a subgroup containing a $2$-cycle and a $p$-cycle.

:::

:::

:::
