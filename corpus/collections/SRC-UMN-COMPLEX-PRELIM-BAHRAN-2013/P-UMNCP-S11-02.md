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
Let \(h\) be holomorphic on a connected open set \(V\). Prove that if
\[
h(z)^2=\overline{h(z)}
\]
for every \(z\in V\), then \(h\) is constant on \(V\). Find all possible values of such a function.
:::

::: {.solution}
<1>1. For every $z\in V$,
$$
|h(z)|\in\{0,1\}.
$$

::: {.proof}
Taking absolute values in
$$
h(z)^2=\overline{h(z)}
$$
gives
$$
|h(z)|^2
=
|h(z)|.
$$
If
$$
r=|h(z)|\ge0,
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

<1>2. The image of $h$ satisfies
$$
h(V)
\subseteq
\{0\}\cup S^1.
$$

::: {.proof}
This is exactly the content of step <1>1.
:::

<1>3. The function $h$ is constant on $V$.

::: {.proof}
Suppose $h$ were nonconstant. Since $V$ is connected and open and $h$ is holomorphic, the open mapping theorem would imply that
$$
h(V)
$$
is an open subset of $\CC$.

But step <1>2 gives
$$
h(V)
\subseteq
\{0\}\cup S^1,
$$
and this set has empty interior in $\CC$. Hence it contains no nonempty open subset. This contradiction shows that $h$ must be constant.
:::

<1>4. A constant value $c$ is allowed exactly when
$$
c=0
$$
or
$$
c^3=1.
$$

::: {.proof}
A constant function $h\equiv c$ satisfies the hypothesis exactly when
$$
c^2=\overline c.
$$
If $c=0$, this holds.

If $c\ne0$, step <1>1 gives
$$
|c|=1,
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

<1>5. Thus the complete list of possible values is
$$
\boxed{
0,quad
1,quad
e^{2\pi i/3},quad
e^{4\pi i/3}}.
$$

::: {.proof}
These are $0$ together with the three cube roots of unity from step <1>4, and each directly satisfies
$$
c^2=\overline c.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>3 proves constancy, and step <1>5 gives all possible constant values.
:::
:::
