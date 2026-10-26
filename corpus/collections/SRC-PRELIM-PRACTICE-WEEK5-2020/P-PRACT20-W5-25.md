---
schema: qual/card@1
id: P-PRACT20-W5-25
kind: problem
title: Entire $f$, $g$ with $e^f+e^g=1$ are constant
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 25).
---

::: {.problem}
Let $f, g : \CC \to \CC$ be entire. Show that if $e^{f(z)} + e^{g(z)} = 1$ for all $z \in \CC$, then $f$ and $g$ are constant.
:::

::: pf

::: pf-step

The entire function
\[
h=e^f
\]
omits both values $0$ and $1$.


::: pf-proof

The complex exponential never vanishes, so
\[
h(z)=e^{f(z)}\ne0
\]
for every $z$. Also the hypothesis gives
\[
1-h(z)=e^{g(z)}.
\]
The right-hand side never vanishes, so
\[
h(z)\ne1
\]
for every $z$.

:::

:::

::: pf-step

The function $e^f$ is constant.


::: pf-proof

Little Picard's theorem states that a nonconstant entire function can omit at
most one complex value. By step <1>1, the entire function $e^f$ omits two
distinct values, $0$ and $1$. Hence it must be constant.

:::

:::

::: pf-step

The function $f$ is constant.


::: pf-proof

By step <1>2,
\[
e^{f(z)}=c
\]
for some nonzero constant $c$. Differentiating gives
\[
e^{f(z)}f'(z)=0.
\]
Since $e^{f(z)}\ne0$, one has
\[
f'(z)=0
\]
for every $z$. Thus $f$ is constant.

:::

:::

::: pf-step

The function $g$ is constant.


::: pf-proof

By the original identity and step <1>2,
\[
e^{g(z)}=1-c,
\]
which is constant and nonzero. Differentiating as in step <1>3 gives
\[
g'(z)=0
\]
for every $z$, so $g$ is constant.

:::

:::

::: pf-step

Therefore
\[
\boxed{f\text{ and }g\text{ are constant}}.
\]


::: pf-proof

This is exactly steps <1>3 and <1>4.

:::

:::

::: pf-qed

Step <1>5 is the required conclusion.

:::

:::
