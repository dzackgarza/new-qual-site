---
schema: qual/card@1
id: P-BKS07-1B
kind: problem
title: Continuous functions with integer periods form a vector space; prime minimal periods give independence
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
---

::: {.problem}
If $c \in \RR$, say that a real-valued function $f \colon \RR \to \RR$ is periodic with period $c$ if it satisfies $f(x + c) = f(x)$ for all $x \in \RR$.

(a) Let $V$ be the set of continuous real-valued functions $f$ having a positive integer as a period.
Prove that $V$ is a vector space.

(b) Let $p_{1} < p_{2} < \cdots < p_{n} < \cdots$ be the sequence of prime numbers, and for each $i$, let $f_{i}$ be a function whose minimal positive period is $p_{i}$. Prove that the functions $f_{1}, f_{2}, \ldots$ are linearly independent in $V$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $c$ and $d$ are periods of a function $f$, then every integer combination $mc+nd$ is a period of $f$.

::: pf-proof

From $f(x+c)=f(x)$ for all $x$, replacing $x$ by $x-c$ gives $f(x-c)=f(x)$. By induction, $f(x+mc+nd)=f(x)$ for all $m,n\in\ZZ$.

:::

:::

::: {.pf-step #s2}

Part (a) holds.

::: pf-proof

$V$ is a subset of the vector space of all functions $\RR\to\RR$. The zero function has period $1$, and $\lambda f$ has every period of $f$. If $f,g\in V$ have positive integer periods $c,d$, then by step [](#s1){.pf-ref} both have period $cd$, so $f+g$ is a continuous function with period $cd$.

:::

:::

::: {.pf-step #s3}

Part (b) holds.

::: pf-proof

Suppose $a_1f_1+\cdots+a_nf_n=0$ with $a_n\ne0$. Then $f_n=-a_n^{-1}\sum_{i<n}a_if_i$, which has period $N=p_1\cdots p_{n-1}$ by step [](#s1){.pf-ref}. Since $\gcd(N,p_n)=1$, there are integers $m,l$ with $mN+lp_n=1$, so $1$ is a period of $f_n$ by step [](#s1){.pf-ref}. Because $1<p_n$, this contradicts the minimality of $p_n$. So every finite linear relation among the $f_i$ is trivial.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove parts (a) and (b).

:::

:::

:::
