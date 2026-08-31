---
schema: qual/card@1
id: E-AMD-A3SS4EYY
kind: exercise
title: A ring in which every non-unit is nilpotent is local
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Nilpotence
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that if $R\neq 0$ is a ring in which every non-unit is nilpotent then $R$ is local.
:::

::: {.solution}
**Goal:** Let $R$ be a non-zero commutative ring with identity $1 \neq 0$.
Suppose that every non-unit in $R$ is nilpotent.
Prove that $R$ is a local ring (i.e., $R$ has a unique maximal ideal).

<1>1. Definitions and characterization of local rings: <2>1. A non-zero commutative ring $R$ is local if and only if the set of non-units $N = R \setminus R^\times$ is an ideal of $R$.
::: {.proof}
If $N$ is an ideal, then every proper ideal $I \subsetneq R$ consists solely of non-units, so $I \subseteq N$, making $N$ the unique maximal ideal.
:::
Conversely, if $R$ is local with unique maximal ideal $\mathfrak{m}$, then every non-unit is contained in $\mathfrak{m}$, so $N = \mathfrak{m}$, which is an ideal.
<2>2. The nilradical $\operatorname{Nil}(R) = \{x \in R \mid \exists k \ge 1 \text{ such that } x^k = 0\}$ is an ideal of $R$.
::: {.proof}
Standard ring theory result: In any commutative ring, the sum of two nilpotents is nilpotent (by the Binomial Theorem, if $x^n = 0$ and $y^m = 0$, $(x+y)^{n+m-1} = 0$), and any multiple $r x$ of a nilpotent is nilpotent ($(r x)^n = r^n x^n = 0$).
:::

<1>2. Equivalence of non-units and the nilradical: <2>1. By hypothesis, every non-unit in $R$ is nilpotent, so $N = R \setminus R^\times \subseteq \operatorname{Nil}(R)$.
::: {.proof}
Direct restatement of the problem hypothesis.
:::
<2>2. Every nilpotent element is a non-unit, so $\operatorname{Nil}(R) \subseteq N = R \setminus R^\times$.
::: {.proof}
If $x \in \operatorname{Nil}(R)$ were a unit, there would exist $u \in R$ such that $x u = 1$.
:::
Then $1 = 1^k = (x u)^k = x^k u^k = 0 \cdot u^k = 0$, which contradicts $1 \neq 0$ in the non-zero ring $R$.
<2>3. Therefore, $N = \operatorname{Nil}(R)$.
::: {.proof}
By mutual inclusion in <2>1 and <2>2.
:::

<1>3. Deducing that $R$ is local: <2>1. Since $N = \operatorname{Nil}(R)$ and $\operatorname{Nil}(R)$ is an ideal of $R$ (<1>1.<2>2), $N = R \setminus R^\times$ is an ideal of $R$.
::: {.proof}
Follows from <1>2.<2>3. <2>2. By the characterization in <1>1.<2>1, $R$ is a local ring with unique maximal ideal $\mathfrak{m} = \operatorname{Nil}(R)$.
:::
::: {.proof}
The set of non-units is an ideal.
:::
<2>3. Q.E.D.
::: {.proof}
Follows from <2>1 and <2>2.
:::

<1>4. Conclusion: Any non-zero commutative ring in which every non-unit is nilpotent is a local ring.
::: {.proof}
By <1>3.
:::
:::
