---
schema: qual/card@1
id: P-CDHB5
kind: problem
title: An abelian group is a $\ZZ$-module in a unique way
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Abelian Groups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: problem
Let $A$ be an abelian group, and show $A$ is a $\ZZ\dash$module in a unique way.
:::

::: solution
**Theorem.**  
Every abelian group $(A,+)$ admits exactly one $\mathbb Z$-module structure.

*Proof.*

1. For $n\in\mathbb Z$ and $a\in A$ define
   \[
   n\cdot a=
   \begin{cases}
   \underbrace{a+\cdots+a}_{n\text{ times}},&n>0,\\
   0,&n=0,\\
   -(\underbrace{a+\cdots+a}_{(-n)\text{ times}}),&n<0.
   \end{cases}
   \]
2. Check module axioms from the abelian law:
   - $n\cdot(a+b)=n\cdot a+n\cdot b$ and $(m+n)\cdot a=m\cdot a+n\cdot a$ by expanding sums.
   - $(mn)\cdot a=m\cdot(n\cdot a)$ by regrouping repeated addition.
   - $1\cdot a=a$ by definition and $0\cdot a=0$ as the empty sum.
3. This defines a $\mathbb Z$-module structure on $A$.
4. For uniqueness, let $A$ carry any $\mathbb Z$-module structure. Module axioms give
   $1\cdot a=a$ and, by repeated addition,
   \[
   n\cdot a=\underbrace{(1\cdot a)+\cdots+(1\cdot a)}_{n\text{ times}},
   \]
   while for $n>0$, $(-n)\cdot a=-(n\cdot a)$.
5. These formulas force the same action as in step 1 for every integer $n$, so no other action is possible.

Hence $A$ is a $\mathbb Z$-module in a unique way.
:::
