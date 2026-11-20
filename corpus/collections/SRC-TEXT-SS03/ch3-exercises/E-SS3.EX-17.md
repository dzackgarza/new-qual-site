---
schema: qual/card@1
id: E-SS3.EX-17
kind: problem
title: Image of a non-constant holomorphic map containing the unit disc
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Open Mapping Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the two arguments already on the card, both of which are
    correct. Added: the reason a holomorphic function of constant modulus on a domain is
    constant (empty interior of the circle, open mapping theorem), the statement of Rouché's
    theorem with the comparison function g = -w_0 and the check |g| < |f| on the circle, the
    note that the zeros are counted with multiplicity, and the explicit link to the exercise's
    hint in part (a). No statement was changed. Not claimed: a retained solution set; the
    collection's provenance is the Stein--Shakarchi textbook, and the argument is the card's
    own.
---

::: {.exercise}
Let $f$ be non-constant and holomorphic in an open set containing the closed unit disc.

(a) Show that if $\abs{f(z)} = 1$ whenever $\abs{z} = 1$, then the image of $f$ contains the unit disc.
[Hint: One must show that $f(z) = w_0$ has a root for every $w_0 \in \DD$. To do this, it suffices to show that $f(z) = 0$ has a root (why?). Use the maximum modulus principle to conclude.]

(b) If $\abs{f(z)} \geq 1$ whenever $\abs{z} = 1$ and there exists a point $z_0 \in \DD$ such that $\abs{f(z_0)} < 1$, then the image of $f$ contains the unit disc.
:::

::: {.solution}
The statement is Exercise 17 of [@SS03, ch. 3 (p. 106)], printed beginning "Let $f$ be non-constant and holomorphic in an open set containing the closed unit disc".

Throughout $\DD = \theset{\abs{z} < 1}$, $f$ is holomorphic and non-constant on an open set containing the closed disc, and $f(\DD) \supseteq \DD$ is what both parts assert. The exercise is Exercise 17 of Stein--Shakarchi, *Complex Analysis*, Chapter 3.

::: pf

::: {.pf-step #a-zero}
(a) Under the hypothesis $\abs{f} = 1$ on $\abs{z} = 1$, the function $f$ has a zero in $\DD$.

::: pf-proof
Suppose not. Then $1/f$ is holomorphic on a neighbourhood of the closed disc, and $\abs{1/f} = 1$ on the circle. The maximum modulus principle applied to $f$ gives $\abs{f} \le 1$ on $\DD$, and applied to $1/f$ gives $\abs{1/f} \le 1$, that is $\abs{f} \ge 1$, on $\DD$; hence $\abs{f} \equiv 1$ on $\DD$. A holomorphic function with constant modulus on a domain is constant: its image lies in the unit circle, which has empty interior, so $f$ is constant by the open mapping theorem (or by the maximum modulus principle applied to $f - f(z_{0})$ at an interior point where the modulus is maximal). That contradicts the hypothesis that $f$ is non-constant.

:::

:::

::: {.pf-step #a-rouche}
(a) For every $w_{0} \in \DD$ the function $f - w_{0}$ has a zero in $\DD$.

::: pf-proof
On the circle $\abs{z} = 1$ one has $\abs{w_{0}} < 1 = \abs{f(z)}$, so the hypothesis of Rouché's theorem is met with $g \coloneqq -w_{0}$, $\abs{g} < \abs{f}$ there. Hence $f$ and $f - w_{0}$ have the same number of zeros in $\DD$, counted with multiplicity; step [](#a-zero){.pf-ref} makes that number at least $1$.

:::

:::

::: {.pf-step #a}
(a) $f(\DD) \supseteq \DD$.

::: pf-proof
By step [](#a-rouche){.pf-ref}, for each $w_{0} \in \DD$ there is $z \in \DD$ with $f(z) = w_{0}$, which is the assertion. The hint's reduction is exactly this: it suffices to know that $f$ has one zero, because Rouché transports the count to every translate $f - w_{0}$ with $\abs{w_{0}} < 1$.

:::

:::

::: {.pf-step #b-zero}
(b) Under the hypothesis $\abs{f} \ge 1$ on $\abs{z} = 1$ and $\abs{f(z_{0})} < 1$ for some $z_{0} \in \DD$, the function $f$ has a zero in $\DD$.

::: pf-proof
Were $f$ zero-free on $\DD$, then $1/f$ would be holomorphic on $\DD$ and, since $\abs{f} \ge 1$ on the boundary circle, continuous on the closed disc with $\abs{1/f} \le 1$ there. The maximum modulus principle would give $\abs{1/f} \le 1$ on $\DD$, that is $\abs{f} \ge 1$ on $\DD$, contradicting $\abs{f(z_{0})} < 1$.

:::

:::

::: {.pf-step #b}
(b) $f(\DD) \supseteq \DD$.

::: pf-proof
Let $w_{0} \in \DD$. On the circle $\abs{w_{0}} < 1 \le \abs{f(z)}$, so Rouché's theorem with $g = -w_{0}$ gives that $f - w_{0}$ has as many zeros in $\DD$ as $f$, and step [](#b-zero){.pf-ref} makes that number at least $1$. Hence $w_{0} \in f(\DD)$, and $w_{0}$ was arbitrary in $\DD$.

:::

:::

:::
:::
