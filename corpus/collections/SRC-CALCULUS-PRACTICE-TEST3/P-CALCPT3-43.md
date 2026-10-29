---
schema: qual/card@1
id: P-CALCPT3-43
kind: problem
title: "Conditions forcing a root of $x^n=\\sum_{i<n}a_ix^i$ in $(0,1)$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 43 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction, which reads choice (E) as I and II. The 300 dpi page render reads I and III."
---

::: {.problem}
Let $n$ be an integer greater than $1$.
Which of the following conditions guarantee that the equation
$$x^n=\sum_{i=0}^{n-1}a_ix^i$$
has at least one root in the interval $(0,1)$?

I. $a_0>0$ and $\sum_{i=0}^{n-1}a_i<1$

II. $a_0>0$ and $\sum_{i=0}^{n-1}a_i>1$

III. $a_0<0$ and $\sum_{i=0}^{n-1}a_i>1$

(A) None
(B) I only
(C) II only
(D) III only
(E) I and III
:::

::: {.solution}
Let $f(x)\coloneqq x^n-\sum_{i=0}^{n-1}a_ix^i$, a polynomial whose roots are the roots of the equation. Then $f(0)=-a_0$ and $f(1)=1-\sum_{i=0}^{n-1}a_i$.

::: pf

::: {.pf-step #I}
Condition I guarantees a root in $(0,1)$.

::: pf-proof
Under I, $f(0)<0<f(1)$, so the intermediate value theorem gives $c\in(0,1)$ with $f(c)=0$.
:::

:::

::: {.pf-step #III}
Condition III guarantees a root in $(0,1)$.

::: pf-proof
Under III, $f(0)>0>f(1)$, and the intermediate value theorem applies as in step [](#I){.pf-ref}.
:::

:::

::: {.pf-step #II}
Condition II does not guarantee a root in $(0,1)$.

::: pf-proof
Take $n=2$, $a_0=2$, $a_1=0$. Then $a_0>0$ and $a_0+a_1=2>1$, but $f(x)=x^2-2<0$ for $x\in(0,1)$.
:::

:::

::: pf-step
The answer is $\boxed{\text{I and III}}$, choice (E).

::: pf-proof
By steps [](#I){.pf-ref}, [](#III){.pf-ref}, and [](#II){.pf-ref}, exactly I and III guarantee a root. This rules out (A), (B), and (D), which omit a valid condition, and (C), which names II.
:::

:::

:::

:::
