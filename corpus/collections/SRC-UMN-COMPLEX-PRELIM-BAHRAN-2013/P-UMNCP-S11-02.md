---
schema: qual/card@1
id: P-UMNCP-S11-02
kind: problem
title: Holomorphic idempotent-conjugate functions are constant
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Spring 2011, 2 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let $h$ be holomorphic on a connected open set $V$. Prove that if
$$
h(z)^2=\overline{h(z)}
$$
for every $z\in V$, then $h$ is constant on $V$. Find all possible values of such a function.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $z\in V$,
$$
\abs{h(z)}\in\{0,1\}.
$$


::: pf-proof

Taking absolute values in
$$
h(z)^2=\overline{h(z)}
$$
gives
$$
\abs{h(z)}^2
=
\abs{h(z)}.
$$
If
$$
r=\abs{h(z)}\ge0,
$$
then
$$
r^2=r,
$$
so
$$
r\in\{0,1\}.
$$

:::

:::

::: {.pf-step #s1-2}

The image of $h$ satisfies
$$
h(V)
\subseteq
\{0\}\cup S^1.
$$


::: pf-proof

This is exactly the content of step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The function $h$ is constant on $V$.


::: pf-proof

Suppose $h$ were nonconstant. Since $V$ is connected and open and $h$ is holomorphic, the open mapping theorem would imply that
$$
h(V)
$$
is an open subset of $\CC$.

But step [](#s1-2){.pf-ref} gives
$$
h(V)
\subseteq
\{0\}\cup S^1,
$$
and this set has empty interior in $\CC$. Hence it contains no nonempty open subset. This contradiction shows that $h$ must be constant.

:::

:::

::: {.pf-step #s1-4}

A constant value $c$ is allowed exactly when
$$
c=0
$$
or
$$
c^3=1.
$$


::: pf-proof

A constant function $h\equiv c$ satisfies the hypothesis exactly when
$$
c^2=\overline c.
$$
If $c=0$, this holds.

If $c\ne0$, step [](#s1-1){.pf-ref} gives
$$
\abs{c}=1,
$$
so
$$
\overline c=c^{-1}.
$$
Therefore
$$
c^2=\overline c
$$
is equivalent to
$$
c^2=c^{-1},
$$
hence to
$$
c^3=1.
$$

:::

:::

::: {.pf-step #s1-5}

Thus the complete list of possible values is
$$
\boxed{
0,quad
1,quad
e^{2\pi i/3},quad
e^{4\pi i/3}}.
$$


::: pf-proof

These are $0$ together with the three cube roots of unity from step [](#s1-4){.pf-ref}, and each directly satisfies
$$
c^2=\overline c.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves constancy, and step [](#s1-5){.pf-ref} gives all possible constant values.

:::

:::

:::
