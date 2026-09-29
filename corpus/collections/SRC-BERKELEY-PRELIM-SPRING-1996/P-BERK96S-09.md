---
schema: qual/card@1
id: P-BERK96S-09
kind: problem
title: Infinitely many pairwise nonisomorphic quadratic extensions of $\QQ$
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
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified that field isomorphisms fix Q, that the square-root comparison
    forces p/q to be a rational square, and that distinct primes exclude
    this by unique factorization.
---

::: {.problem}
Exhibit infinitely many quadratic extensions of $\mathbb Q$ and prove that they are pairwise nonisomorphic.
:::

::: {.solution}
For each prime number $p$, let
$$
K_p\coloneqq\QQ(\sqrt p).
$$

::: pf

::: {.pf-step #s1}

Each $K_p$ is a quadratic extension of $\QQ$.

::: pf-proof

A prime number $p$ is not a square in $\QQ$. Hence
$$
x^2-p
$$
is irreducible over $\QQ$, so
$$
[K_p:\QQ]=2.
$$

:::

:::

::: {.pf-step #s2}

Every field isomorphism between two fields $K_p$ and $K_q$ fixes
$\QQ$ pointwise.

::: pf-proof

A field isomorphism sends $1$ to $1$, hence fixes the prime field $\QQ$.

:::

:::

::: {.pf-step #s3}

If $p$ and $q$ are distinct primes, then $K_p$ and $K_q$ are not
isomorphic.

::: pf-proof

Suppose that
$$
\varphi:K_p\longrightarrow K_q
$$
is a field isomorphism. By step [](#s2){.pf-ref}, it fixes $\QQ$. Write
$$
\varphi(\sqrt p)=a+b\sqrt q,
\qquad
a,b\in\QQ.
$$
Squaring and using $\varphi(p)=p$ gives
$$
p
=
a^2+b^2q+2ab\sqrt q.
$$
Since $1$ and $\sqrt q$ are linearly independent over $\QQ$,
$$
2ab=0.
$$
If $b=0$, then $p=a^2$, contradicting step [](#s1){.pf-ref}. Thus $a=0$, and therefore
$$
\frac pq=b^2.
$$
But the prime factorization of $p/q$ has exponent $1$ at $p$ and exponent
$-1$ at $q$, whereas every rational square has even exponent at every
prime. This is impossible.

:::

:::

::: {.pf-step #s4}

There are infinitely many pairwise nonisomorphic quadratic extensions
of $\QQ$.

::: pf-proof

There are infinitely many prime numbers. By step [](#s1){.pf-ref} each prime $p$
produces a quadratic extension $K_p$, and step [](#s3){.pf-ref} shows that extensions
coming from distinct primes are nonisomorphic.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the required infinite family.

:::

:::

:::
