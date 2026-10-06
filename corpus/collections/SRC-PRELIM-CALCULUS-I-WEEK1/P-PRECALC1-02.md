---
schema: qual/card@1
id: P-PRECALC1-02
kind: problem
title: Limit of $\frac{(1+x)^\alpha-1}{x}$ as $x\to0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Evaluate $\operatorname* { l i m } _ { x \to 0 } { \frac { ( 1 + x ) ^ { \alpha } - 1 } { x } }$ for $\alpha \in \mathbb { R }$
:::

::: {.solution}
Define
\[
f(t)=t^\alpha
\]
for \(t>0\).

<1>1. The given limit can be rewritten as
\[
\boxed{
\lim_{x\to0}
\frac{f(1+x)-f(1)}{x}}.
\]

::: {.proof}
Since
\[
f(1+x)=(1+x)^\alpha
\]
and
\[
f(1)=1^\alpha=1,
\]
the quotient is exactly the one in the problem.
:::

<1>2. For \(t>0\),
\[
\boxed{
f(t)=e^{\alpha\log t}}.
\]

::: {.proof}
This is the standard definition of the real power \(t^\alpha\) for
\(t>0\).
:::

<1>3. Therefore
\[
\boxed{
f'(t)=\alpha t^{\alpha-1}}.
\]

::: {.proof}
Differentiate step <1>2:
\[
\begin{aligned}
f'(t)
&=
e^{\alpha\log t}\cdot\frac{\alpha}{t}\\
&=
t^\alpha\frac{\alpha}{t}\\
&=
\alpha t^{\alpha-1}.
\end{aligned}
\]
:::

<1>4. In particular,
\[
\boxed{
f'(1)=\alpha}.
\]

::: {.proof}
Substitute \(t=1\) into step <1>3:
\[
f'(1)
=
\alpha\cdot1^{\alpha-1}
=
\alpha.
\]
:::

<1>5. By the definition of the derivative,
\[
\lim_{x\to0}
\frac{f(1+x)-f(1)}{x}
=
f'(1).
\]

::: {.proof}
This is the difference-quotient definition of the derivative at the point
\(1\).
:::

<1>6. Hence
\[
\boxed{
\lim_{x\to0}
\frac{(1+x)^\alpha-1}{x}
=
\alpha}.
\]

::: {.proof}
Combine steps <1>1, <1>4, and <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the requested limit.
:::
:::
