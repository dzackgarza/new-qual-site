---
schema: qual/card@1
id: P-ALGREV1-08
kind: problem
title: Orders of representatives of the same coset
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Review1.md, true/sometimes/false question 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Classified the assertion as sometimes true, with trivial H as the positive case and H={0,2} in Z4 as a counterexample."
---

::: {.problem}
Classify the following assertion as true, sometimes true, or false: in a factor group $G/H$, if $aH=bH$, then $|a|=|b|$.
:::

::: {.solution}
The assertion is **sometimes true**.

<1>1. It is true when $H$ is trivial.
::: {.proof}
If $H=\{e\}$, then
$$
aH=bH
$$
implies $a=b$. Hence $|a|=|b|$.
:::

<1>2. It can fail when $H$ is nontrivial.
::: {.proof}
Take the additive group
$$
G=\mathbb Z_4
$$
and the subgroup
$$
H=\{0,2\}.
$$
Then
$$
0+H=2+H=H,
$$
but the order of $0$ is $1$ while the order of $2$ is $2$.
Thus equal cosets need not have representatives of equal order.
:::

<1>3. Conclude the classification.
::: {.proof}
Step <1>1 gives cases in which the assertion holds, while step <1>2 gives a
case in which it fails. Therefore the correct classification is
$$
\boxed{\text{sometimes true}.}
$$
:::
:::
