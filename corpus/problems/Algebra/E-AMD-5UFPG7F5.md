---
schema: qual/card@1
id: E-AMD-5UFPG7F5
kind: exercise
title: An ideal is maximal iff the quotient is a field
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Fields
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that $I\normal R$ is maximal iff $R/I$ is a field.
:::

::: {.solution}
**Goal:** Let $R$ be a commutative ring with identity $1 \neq 0$, and let $I \trianglelefteq R$ be a proper ideal.
Prove that $I$ is a maximal ideal of $R$ if and only if the quotient ring $R/I$ is a field.

<1>1. Preliminaries and the Correspondence Theorem for Ideals: <2>1. $R/I$ is a commutative ring with non-zero identity $1 + I$.
::: {.proof}
Since $R$ is a commutative ring with unity and $I \subsetneq R$ is a proper ideal, the quotient ring $R/I$ is commutative with multiplicative identity $1_{R/I} = 1 + I \neq 0 + I$.
:::
<2>2. By the Lattice Isomorphism Theorem (Correspondence Theorem) for rings, there is an inclusion-preserving bijection between ideals $J$ of $R$ containing $I$ and ideals $\bar{J} = J/I$ of $R/I$.
::: {.proof}
The canonical quotient projection $\pi: R \to R/I$ maps ideals $J \supseteq I$ bijectively to ideals of $R/I$, with inverse map $\bar{J} \mapsto \pi^{-1}(\bar{J})$.
:::
<2>3. A commutative ring $K$ with $1 \neq 0$ is a field if and only if its only ideals are $(0)$ and $K$.
::: {.proof}
If $K$ is a field and $J \neq (0)$ is an ideal, choose non-zero $x \in J$.
:::
Then $1 = x \cdot x^{-1} \in J$, so $J = K$.
Conversely, if the only ideals of $K$ are $(0)$ and $K$, then for any $x \neq 0$, the principal ideal $(x) \neq (0)$, so $(x) = K$.
Hence $1 \in (x)$, meaning there exists $y \in K$ such that $x y = 1$, so every non-zero element has a multiplicative inverse.

<1>2. Direction 1 ($\implies$): If $I$ is maximal, then $R/I$ is a field.
<2>1. Assume $I$ is a maximal ideal of $R$.
::: {.proof}
Hypothesis.
:::
<2>2. The only ideals of $R$ containing $I$ are $I$ and $R$.
::: {.proof}
By definition of a maximal ideal, there is no ideal $J$ such that $I \subsetneq J \subsetneq R$.
:::
<2>3. Under the Correspondence Theorem (<1>1.<2>2), the only ideals of $R/I$ are $I/I = (0)$ and $R/I$.
::: {.proof}
The bijection between ideals of $R$ containing $I$ and ideals of $R/I$ maps $I$ to $(0)$ and $R$ to $R/I$.
:::
Since only $I$ and $R$ exist containing $I$, the only ideals of $R/I$ are $(0)$ and $R/I$.
<2>4. Therefore, $R/I$ is a field.
::: {.proof}
By <1>1.<2>3, a commutative ring with non-zero identity whose only ideals are $(0)$ and the whole ring is a field.
:::
<2>5. Q.E.D.
::: {.proof}
Follows from <2>1 through <2>4.
:::

<1>3. Direction 2 ($\impliedby$): If $R/I$ is a field, then $I$ is maximal.
<2>1. Assume $R/I$ is a field.
::: {.proof}
Hypothesis.
:::
<2>2. The only ideals of $R/I$ are $(0)$ and $R/I$.
::: {.proof}
By <1>1.<2>3, every field has exactly two ideals: $(0)$ and itself.
:::
<2>3. By the Correspondence Theorem (<1>1.<2>2), the only ideals of $R$ containing $I$ are $\pi^{-1}((0)) = I$ and $\pi^{-1}(R/I) = R$.
::: {.proof}
The bijection maps the only two ideals of $R/I$ back to $I$ and $R$.
:::
<2>4. There is no ideal $J$ of $R$ such that $I \subsetneq J \subsetneq R$.
::: {.proof}
Any ideal $J$ with $I \subseteq J \subseteq R$ corresponds to an ideal $J/I$ of $R/I$.
:::
Since $J/I$ must be either $(0)$ or $R/I$, $J$ must be either $I$ or $R$.
<2>5. Therefore, $I$ is a maximal ideal of $R$.
::: {.proof}
By definition of maximal ideal.
:::
<2>6. Q.E.D.
::: {.proof}
Follows from <2>1 through <2>5.
:::

<1>4. Conclusion: $I \trianglelefteq R$ is maximal if and only if $R/I$ is a field.
::: {.proof}
By <1>2 and <1>3.
:::
:::
