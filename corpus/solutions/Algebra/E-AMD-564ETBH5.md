---
schema: qual/card@1
id: E-AMD-564ETBH5
kind: exercise
title: $a+\nilrad{R}$ nilpotent implies $a\in\nilrad{R}$
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Ideals
  - Rings
relations: []
review: draft
---

::: exercise
Let $R$ be a commutative ring and let $\operatorname{Nil}(R)$ denote its nilradical. Show that if $a + \operatorname{Nil}(R)$ is nilpotent in the quotient ring $R/\operatorname{Nil}(R)$, then $a \in \operatorname{Nil}(R)$.
:::

::: solution
**Goal:** Prove that if $a + \operatorname{Nil}(R)$ is nilpotent in $R/\operatorname{Nil}(R)$, then $a \in \operatorname{Nil}(R)$, so that the quotient ring $R/\operatorname{Nil}(R)$ contains no non-zero nilpotent elements.

<1>1. Definition of the nilradical and quotient multiplication:
    *Proof:*
    <2>1. The nilradical $\operatorname{Nil}(R)$ is the ideal of all nilpotent elements in $R$:
    $$\operatorname{Nil}(R) = \{x \in R : x^k = 0 \text{ for some positive integer } k \ge 1\}.$$
    <2>2. Multiplication in the quotient ring $R/\operatorname{Nil}(R)$ is defined on cosets by $(x + \operatorname{Nil}(R))(y + \operatorname{Nil}(R)) = x y + \operatorname{Nil}(R)$.
    <2>3. By induction, $(a + \operatorname{Nil}(R))^n = a^n + \operatorname{Nil}(R)$ for all integers $n \ge 1$.

<1>2. Translating nilpotence in the quotient:
    *Proof:*
    <2>1. Since $a + \operatorname{Nil}(R)$ is nilpotent in $R/\operatorname{Nil}(R)$, there exists an integer $n \ge 1$ such that
    $$(a + \operatorname{Nil}(R))^n = 0 + \operatorname{Nil}(R) = \operatorname{Nil}(R).$$
    <2>2. Combining with <1>1 gives $a^n + \operatorname{Nil}(R) = \operatorname{Nil}(R)$, which is equivalent to $a^n \in \operatorname{Nil}(R)$.

<1>3. Deducing $a \in \operatorname{Nil}(R)$:
    *Proof:*
    <2>1. Since $a^n \in \operatorname{Nil}(R)$, the definition of the nilradical implies that there exists an integer $m \ge 1$ such that
    $$(a^n)^m = 0.$$
    <2>2. By the power laws in the ring $R$, $a^{n m} = (a^n)^m = 0$.
    <2>3. Since $n \ge 1$ and $m \ge 1$, the product $N = n m$ is a positive integer ($N \ge 1$).
    <2>4. Since $a^N = 0$, $a$ is a nilpotent element of $R$.
    <2>5. Therefore $a \in \operatorname{Nil}(R)$.

<1>4. Conclusion:
    *Proof:*
    Every nilpotent element in $R/\operatorname{Nil}(R)$ is the zero coset $\operatorname{Nil}(R)$, so $\operatorname{Nil}(R/\operatorname{Nil}(R)) = \{0\}$.
:::
