---
schema: qual/card@1
id: P-63TON
kind: problem
title: A monic in $R[x]$ factoring into nonconstant monics in $F[x]$ with a factor
  outside $R[x]$ implies $R$ is not a UFD; $\ZZ[2\sqrt{2}]$ is not a UFD
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Polynomials
  - Integral Domains
relations: []
review: draft
---

::: problem
(a) Let $R$ be an integral domain with fraction field $F$. Suppose that $p(x), a(x), b(x) \in F[x]$ are non-constant monic polynomials such that $p(x) = a(x) b(x)$ with $p(x) \in R[x]$ and $a(x) \notin R[x]$. Prove that $R$ is not a unique factorization domain (UFD). (You may assume Gauss's Lemma.)

(b) Prove that $\mathbb{Z}[2\sqrt{2}]$ is not a UFD.
:::

::: solution
**Goal:** Prove that integral domains admitting non-integral monic factorizations in their fraction field are not UFDs via Gauss's Lemma, and apply this to $x^2 - 2$ over $\mathbb{Z}[2\sqrt{2}]$.

<1>1. Part (a): $R$ is not a UFD.
::: {.proof}
    <2>1. Suppose for contradiction that $R$ is a UFD.
    <2>2. Gauss's Lemma for UFDs states that if a monic polynomial $p(x) \in R[x]$ factors as $p(x) = a(x) b(x)$ for non-constant monic polynomials $a(x), b(x) \in F[x]$, then there exist elements $c, d \in F^\times$ such that
    $$c a(x) \in R[x], \quad d b(x) \in R[x], \quad \text{and} \quad c d = 1.$$
    <2>3. Because $a(x)$ is monic, the leading coefficient of the polynomial $c a(x)$ is $c \cdot 1 = c$.
    <2>4. Since $c a(x) \in R[x]$, its leading coefficient must lie in $R$, so $c \in R$.
    <2>5. Similarly, because $b(x)$ is monic, the leading coefficient of $d b(x)$ is $d$. Since $d b(x) \in R[x]$, $d \in R$.
    <2>6. Since $c, d \in R$ and $c d = 1$, $c$ is an invertible element of $R$ ($c \in R^\times$).
    <2>7. Because $c \in R^\times$, its inverse $c^{-1} = d \in R$.
    <2>8. Multiply $c a(x) \in R[x]$ by $c^{-1} \in R$:
    $$a(x) = c^{-1} (c a(x)) \in R[x].$$
    <2>9. This contradicts the hypothesis that $a(x) \notin R[x]$.
    <2>10. Therefore, $R$ is not a UFD.

:::

<1>2. Part (b): $\mathbb{Z}[2\sqrt{2}]$ is not a UFD.
::: {.proof}
    <2>1. Set $R = \mathbb{Z}[2\sqrt{2}] = \{u + 2v\sqrt{2} \mid u, v \in \mathbb{Z}\}$.
    <2>2. The fraction field of $R$ is $F = \mathbb{Q}(\sqrt{2})$.
    <2>3. Define $p(x) = x^2 - 2$. Since $-2 \in R$, $p(x) \in R[x]$, and $p(x)$ is monic.
    <2>4. In $F[x] = \mathbb{Q}(\sqrt{2})[x]$, $p(x)$ factors into monic linear polynomials:
    $$p(x) = (x - \sqrt{2})(x + \sqrt{2}) =: a(x) b(x),$$
    where $a(x) = x - \sqrt{2}$ and $b(x) = x + \sqrt{2}$.
    <2>5. Check whether $a(x) \in R[x]$:
        - The constant term of $a(x)$ is $-\sqrt{2}$.
        - If $-\sqrt{2} \in R$, then $-\sqrt{2} = u + 2v\sqrt{2}$ for some $u, v \in \mathbb{Z}$.
        - Equating rational and irrational parts gives $u = 0$ and $2v = -1 \implies v = -1/2 \notin \mathbb{Z}$, a contradiction.
        - Thus $-\sqrt{2} \notin R$, which implies $a(x) \notin R[x]$.
    <2>6. All hypotheses of Part (a) hold for $p(x) = x^2 - 2 \in R[x]$ and $a(x) = x - \sqrt{2} \in F[x] \setminus R[x]$.
    <2>7. Therefore, by Part (a), $\mathbb{Z}[2\sqrt{2}]$ is not a UFD.

:::

<1>3. Conclusion:
::: {.proof}
    Monics factoring in $F[x]$ with non-integral factors contradict Gauss's Lemma for UFDs, so $\mathbb{Z}[2\sqrt{2}]$ is not a UFD via $x^2 - 2 = (x - \sqrt{2})(x + \sqrt{2})$.
:::
:::

