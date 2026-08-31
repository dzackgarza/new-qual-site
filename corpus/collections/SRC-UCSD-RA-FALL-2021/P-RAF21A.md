---
schema: qual/card@1
id: P-RAF21A
kind: problem
title: "Differentiable with derivative zero off a small exceptional set: when is f constant?"
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Borel Sets
  - Measure Zero Sets
  - Cantor Function
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $f \in C(\mathbb{R})$ and let $A \subseteq \mathbb{R}$ be a Borel set such that $f$ is differentiable at each $x \in \mathbb{R} \setminus A$ and $f'(x) = 0$ for all such $x$.

(a) If $A$ is closed and countable, show that $f$ is constant.

(b) If $A$ has Lebesgue measure $0$, must $f$ be constant?
Prove or find a counterexample.
:::

::: {.solution}
**(a).**

<1>1. $f$ is continuous and differentiable with $f' = 0$ on $\mathbb{R} \setminus A$, where $A$ is closed and countable.
::: {.proof}
hypotheses.
:::

<1>2. $\mathbb{R} \setminus A$ is open, and its connected components are open intervals.
::: {.proof}
$A$ is closed, so its complement is open.
:::

<1>3. On each connected component (interval) of $\mathbb{R} \setminus A$, $f' = 0$, so $f$ is constant on that interval.
::: {.proof}
<1>2 and the mean value theorem (a function with zero derivative on an interval is constant).
:::

<1>4. Since $A$ is countable and $f$ is continuous, the constant values on adjacent intervals must agree (the countable set $A$ cannot separate the values, as $f$ is continuous across the points of $A$).
::: {.proof}
<1>3 and continuity (the values on the two sides of any point of $A$ must be equal, since $f$ is continuous at that point).
:::

<1>5. Hence $f$ is constant on all of $\mathbb{R}$.
::: {.proof}
<1>4.
:::

**(b).**

<1>1. No, $f$ need not be constant.
::: {.proof}
the answer is negative.
:::

<1>2. Counterexample: the Cantor function $f$ (the Devil's staircase).
::: {.proof}
choose the Cantor function.
:::

<1>3. The Cantor function is continuous, and $f'(x) = 0$ for all $x$ outside the Cantor set $C$.
::: {.proof}
the Cantor function is constant on each interval of the complement of $C$, so its derivative is $0$ there.
:::

<1>4. The Cantor set $C$ has Lebesgue measure $0$.
::: {.proof}
$m(C) = 0$.
:::

<1>5. But the Cantor function is not constant (it goes from $0$ to $1$).
::: {.proof}
$f(0) = 0$ and $f(1) = 1$.
:::

<1>6. Hence $f$ is a counterexample: $A = C$ has measure $0$, $f' = 0$ off $A$, but $f$ is not constant.
::: {.proof}
<1>3–<1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>5 (a) and <1>6 (b).
:::
:::
