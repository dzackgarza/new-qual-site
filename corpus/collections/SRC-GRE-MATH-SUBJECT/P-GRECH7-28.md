---
schema: qual/card@1
id: P-GRECH7-28
kind: problem
title: Which condition is not a metric axiom
classification:
  areas: [prelim]
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 28 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Suppose X is a nonempty set for which $\delta: X \times X \to \RR$ is a real-valued function defined on ordered pairs of points on X. Which of the following is NOT a property of the metric function $\delta$?

(A) $\delta(x, y) \ge 0$
(B) $\delta(x, z) \le \delta(x, y) + \delta(y, z)$
(C) $\delta(x, y) = \delta(y, x)$
(D) $\delta(x, y) = 0 \leftrightarrow x = y$
(E) $\delta(x, z) = \delta(x, y) + \delta(y, z)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Properties (A), (C), and (D) are metric axioms.


::: pf-proof

By definition, a metric is nonnegative,
$$
\delta(x,y)\ge0,
$$
symmetric,
$$
\delta(x,y)=\delta(y,x),
$$
and separates points,
$$
\delta(x,y)=0\iff x=y.
$$
These are exactly (A), (C), and (D).

:::

:::

::: {.pf-step #s1-2}

Property (B) is the triangle inequality and is also a metric axiom.


::: pf-proof

Every metric satisfies
$$
\delta(x,z)\le\delta(x,y)+\delta(y,z)
$$
for all $x,y,z\in X$, which is precisely statement (B).

:::

:::

::: {.pf-step #s1-3}

Property (E) is not required of a metric and can fail.


::: pf-proof

Take $X=\RR$ with the usual metric $\delta(s,t)=\abs{s-t}$, and choose
$$
x=0,\qquad y=1,\qquad z=0.
$$
Then
$$
\delta(x,z)=0,
$$
whereas
$$
\delta(x,y)+\delta(y,z)=1+1=2.
$$
Thus equality in the triangle inequality need not hold.

:::

:::

::: {.pf-step #s1-4}

Therefore the condition that is not a metric property is
$$
\boxed{\delta(x,z)=\delta(x,y)+\delta(y,z)},
$$
so the answer is (E).


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} identify (A)--(D) as metric axioms, while step [](#s1-3){.pf-ref} gives a metric violating (E).

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required choice.

:::

:::

:::
