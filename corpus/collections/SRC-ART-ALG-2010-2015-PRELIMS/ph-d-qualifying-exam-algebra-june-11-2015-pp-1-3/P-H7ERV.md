---
schema: qual/card@1
id: P-H7ERV
kind: problem
title: At most two $F$-conjugates of $L$ when $[K:F]=2$ and $L/K$ is finite Galois
classification:
  areas:
  - prelim
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $F$ be a field of characteristic zero and $\overline{F}$ be an algebraic closure of $F$.
Suppose that $K$ and $L$ are fields, with $F \subseteq K \subseteq L \subseteq \overline{F}$, such that $[K : F] = 2$ and $L/K$ is a finite Galois extension.
Prove that there are at most two fields $M \subseteq \overline{F}$ conjugate to $L$ over $F$ (remember that $M \subseteq \overline{F}$ is conjugate to $L$ over $F$ just in case there is an isomorphism of $L$ onto $M$ which is the identity on $F$).
:::

::: {.solution}

::: pf

::: pf-step

The $F$-conjugates of $L$ are the images $\sigma(L)$ for $\sigma \in \operatorname{Aut}_F(\overline F)$.

::: pf-proof

an $F$-isomorphism $L \to M$ extends to an automorphism of $\overline F$ fixing $F$, so $M = \sigma(L)$ for some $\sigma$.

:::

:::

::: pf-step

$K/F$ is Galois (degree $2$ in characteristic $0$).

::: pf-proof

any degree-$2$ extension in characteristic $0$ is Galois (it is the splitting field of a quadratic).

:::

:::

::: pf-step

Hence $\sigma(K) = K$ for all $\sigma \in \operatorname{Aut}_F(\overline F)$.

::: pf-proof

$K/F$ is Galois, so it is stable under every $F$-automorphism of $\overline F$.

:::

:::

::: {.pf-step #s4}

$L/K$ is Galois, so $\sigma(L)$ depends only on $\sigma|_K$.

::: pf-proof

::: pf-step

For $\sigma \in \operatorname{Aut}_F(\overline F)$, $\sigma(L)$ is a $K$-conjugate of $L$ (since $\sigma(K) = K$).

::: pf-proof

$\sigma|_K$ is an automorphism of $K$, and $\sigma(L)$ is a $K$-conjugate of $L$.

:::

:::

::: pf-step

Since $L/K$ is Galois, $\sigma(L) = L$ for all $\sigma$ fixing $K$.

::: pf-proof

a Galois extension is stable under all $K$-automorphisms of $\overline F$.

:::

:::

::: pf-step

Hence $\sigma(L)$ depends only on $\sigma|_K$.

::: pf-proof

if $\sigma|_K = \tau|_K$, then $\sigma^{-1}\tau$ fixes $K$, so $\sigma^{-1}\tau(L) = L$, i.e. $\sigma(L) = \tau(L)$.

:::

:::

:::

:::

::: {.pf-step #s5}

There are at most two choices for $\sigma|_K$.

::: pf-proof

::: pf-step

$\operatorname{Aut}_F(K)$ has order $2$ (since $[K:F] = 2$ and $K/F$ is Galois).

::: pf-proof

$|\operatorname{Aut}_F(K)| = [K:F] = 2$.

:::

:::

::: pf-step

Hence $\sigma|_K$ is one of at most two automorphisms.

::: pf-proof

$\sigma|_K \in \operatorname{Aut}_F(K)$, which has two elements.

:::

:::

:::

:::

::: {.pf-step #s6}

Hence there are at most two $F$-conjugates of $L$.

::: pf-proof

By step [](#s4){.pf-ref}, $\sigma(L)$ is determined by $\sigma|_K$, and by step [](#s5){.pf-ref} there are at most two such restrictions.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the claim.

:::

:::

:::
