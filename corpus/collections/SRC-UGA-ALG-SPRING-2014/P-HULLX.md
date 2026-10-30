---
schema: qual/card@1
id: P-HULLX
kind: problem
title: Groups of order $p^m n$ are not simple for sufficiently large $m$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $p, n$ be integers such that $p$ is prime and $p$ does not divide $n$.
Find a real number $k = k (p, n)$ such that for every integer $m\geq k$, every group of order $p^m n$ is not simple.
:::

::: {.solution}

Assume $n$ is a positive integer, as required for $p^m n$ to be a group order.

::: pf

::: {.pf-step #s1-1}

An admissible bound is
$$
\boxed{k(p,n)=\lfloor\log_p((n-1)!)\rfloor+1}.
$$


::: pf-proof

For every integer $m\geq k(p,n)$, one has $p^m>(n-1)!$, hence $p^mn>n!$. This applies also when $n=1$, when the bound equals one.

:::

:::

::: {.pf-step #s1-2}

A simple group $G$ of order $p^m n$ with $m\geq1$ and $p\nmid n$ would embed into $S_r$ for some integer $r$ dividing $n$.


::: pf-proof

Let $r$ be the number of Sylow $p$-subgroups. If $r=1$, its unique Sylow $p$-subgroup is a proper nontrivial normal subgroup, contradicting simplicity. Therefore $r>1$. Conjugation on the Sylow $p$-subgroups yields a nontrivial homomorphism $G\to S_r$. Its kernel is normal and proper, so simplicity makes the kernel trivial. By Sylow's theorem $r$ divides $n$.

:::

:::

::: {.pf-step #s1-3}

No group of order $p^m n$ with $m\geq k(p,n)$ is simple.


::: pf-proof

If such a group were simple, step [](#s1-2){.pf-ref} would give an embedding $G\hookrightarrow S_r$ with $r\leq n$, hence $p^mn=\cardinality{G}\leq r!\leq n!$. This contradicts the strict inequality $p^mn>n!$ from step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref} give the requested bound and establish its asserted property.

:::

:::

:::
