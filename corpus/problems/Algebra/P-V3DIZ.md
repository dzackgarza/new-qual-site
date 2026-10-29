---
schema: qual/card@1
id: P-V3DIZ
kind: problem
title: The torsion submodule of a module over an integral domain
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'Part 2 of the source reads "Prove that the quotient module $M / \operatorname{Tor}(M)$
    is torsion-free." with the integral-domain hypothesis stated only in part 1; the quotient
    is undefined when $\operatorname{Tor}(M)$ is not a submodule, so part (b) now assumes
    $R$ is an integral domain. Parts are relabelled (a)--(c).'
---

::: {.problem}
Let $R$ be a commutative ring and let $M$ be an $R$-module.
An element $x \in M$ is a *torsion element* if there exists a non-zero $r \in R$ such that $rx = 0$ (or equivalently, $\Ann_R(x) \neq (0)$). Let $\operatorname{Tor}(M) = \{x \in M : \Ann_R(x) \neq (0)\}$ denote the set of torsion elements of $M$.

(a) Prove that if $R$ is an integral domain, then $\operatorname{Tor}(M)$ is an $R$-submodule of $M$.

(b) Prove that if $R$ is an integral domain, then the quotient module $M / \operatorname{Tor}(M)$ is torsion-free.

(c) Show by example that $\operatorname{Tor}(M)$ need not be a submodule if $R$ has zero divisors.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) If $R$ is an integral domain, then $\operatorname{Tor}(M)$ is a submodule of $M$.

::: pf-proof

Since $1\neq0$ and $1\cdot0=0$, $0\in\operatorname{Tor}(M)$.
Let $x, y \in \operatorname{Tor}(M)$, with non-zero $r_1, r_2 \in R$ such that $r_1 x = 0$ and $r_2 y = 0$. Since $R$ is an integral domain, $r_1 r_2 \neq 0$, and since $R$ is commutative,
$$
(r_1 r_2)(x + y) = r_2(r_1 x) + r_1(r_2 y) = 0,
$$
so $x+y\in\operatorname{Tor}(M)$. For $c \in R$, $r_1(cx) = c(r_1 x) = 0$, so $cx \in \operatorname{Tor}(M)$.

:::

:::

::: {.pf-step #s2}

(b) If $R$ is an integral domain, then $M / \operatorname{Tor}(M)$ is torsion-free.

::: pf-proof

By step [](#s1){.pf-ref}, the quotient is defined. Let $\bar{x} = x + \operatorname{Tor}(M)$ and suppose $s \bar{x} = \bar{0}$ for some non-zero $s \in R$. Then $sx \in \operatorname{Tor}(M)$, so $t(sx) = 0$ for some non-zero $t \in R$. Since $R$ is an integral domain, $ts \neq 0$, and $(ts)x = 0$, so $x \in \operatorname{Tor}(M)$ and $\bar{x} = \bar{0}$.

:::

:::

::: {.pf-step #s3}

(c) For $R = M = \ZZ/6\ZZ$, $\operatorname{Tor}(M)$ is not closed under addition.

::: pf-proof

The element $[2]$ is torsion because $[3] \cdot [2] = [0]$ with $[3] \neq [0]$, and $[3]$ is torsion because $[2] \cdot [3] = [0]$ with $[2] \neq [0]$. Their sum $[5]$ is a unit of $\ZZ/6\ZZ$, so $\Ann_R([5]) = \{[0]\}$ and $[5] \notin \operatorname{Tor}(M)$.

:::

:::

:::

:::
