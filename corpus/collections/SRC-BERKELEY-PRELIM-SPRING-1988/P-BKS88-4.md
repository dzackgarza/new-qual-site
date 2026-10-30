---
schema: qual/card@1
id: P-BKS88-4
kind: problem
title: Analytic continuation past the boundary of a disc
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 1988 preliminary examination.
---

::: {.problem}
True or false: A function $f(z)$ analytic on $\abs{z-a}<r$ and continuous on $\abs{z-a}\leq r$ extends, for some $\delta>0$, to a function analytic on $\abs{z-a}<r+\delta$? Give a proof or a counterexample.
:::

::: {.solution}
It suffices to take $a=0$ and $r=1$.

::: pf

::: {.pf-step #counterexample-function}
The function
$$
f(z):=\sqrt{1-z},\qquad \abs{z}<1,
$$
with the principal square root, is analytic on $\abs{z}<1$ and extends continuously to $\abs{z}\leq 1$.

::: pf-proof
If $\abs{z}<1$, then $\operatorname{Re}(1-z)>0$. Hence $1-z$ lies in the right half-plane, on which the principal square root is analytic, so $f$ is analytic on the open unit disc. If $\abs{z}\leq 1$, then $\operatorname{Re}(1-z)\geq 0$, and the principal square root is continuous on this closed right half-plane, including at $0$. Thus the same formula defines a continuous function on the closed unit disc.
:::

:::

::: {.pf-step #no-extension}
The function in [](#counterexample-function){.pf-ref} has no analytic extension to any disc $\abs{z}<1+\delta$ with $\delta>0$.

::: pf-proof
Suppose that such an extension $F$ exists. On $\abs{z}<1$ one has
$$
F(z)^2=f(z)^2=1-z.
$$
Both sides are analytic on the connected disc $\abs{z}<1+\delta$, so the identity theorem gives
$$
F(z)^2=1-z
$$
throughout that disc. Evaluating at $z=1$ gives $F(1)=0$. Differentiating the identity and then setting $z=1$ gives
$$
2F(1)F'(1)=-1,
$$
whose left-hand side is $0$, a contradiction.
:::

:::

::: pf-qed
[](#counterexample-function){.pf-ref} and [](#no-extension){.pf-ref} give a counterexample, so the proposed statement is false.
:::

:::

:::
