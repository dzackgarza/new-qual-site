---
schema: qual/card@1
id: P-BKS10-3A
kind: problem
title: Entire functions with $\abs{f(z)}\le\abs{z}^2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the order-two zero at the origin, the removable quotient f(z)/z^2, and the Liouville argument.
---

::: {.problem}
Suppose $f$ is entire and satisfies
$$
|f(z)|\le |z|^2
$$
for every $z\in\mathbb C$. Find all possibilities for \(f\), and justify your answer.
:::

::: {.solution}
<1>1. One has
$$
f(0)=0
$$
and
$$
f'(0)=0.
$$

::: {.proof}
Evaluating the hypothesis at $z=0$ gives
$$
\abs{f(0)}\leq0,
$$
so $f(0)=0$. Hence
$$
f'(0)
=
\lim_{z\to0}\frac{f(z)-f(0)}{z}
=
\lim_{z\to0}\frac{f(z)}{z}.
$$
For $z\neq0$,
$$
\abs{\frac{f(z)}{z}}
\leq
\abs{z},
$$
so the last limit is $0$.
:::

<1>2. The function
$$
h(z)
\coloneqq
\begin{cases}
f(z)/z^2,&z\neq0,\\
f''(0)/2,&z=0
\end{cases}
$$
is entire.

::: {.proof}
Step <1>1 shows that the Taylor series of $f$ at $0$ has no constant or
linear term. Thus
$$
f(z)
=
z^2
\left(
\frac{f''(0)}{2}
+
\frac{f^{(3)}(0)}{3!}z
+
\cdots
\right),
$$
which proves that the displayed definition removes the apparent
singularity at $0$ and gives an entire function.
:::

<1>3. The entire function $h$ satisfies
$$
\abs{h(z)}\leq1
$$
for every $z\in\CC$.

::: {.proof}
For $z\neq0$, the hypothesis gives
$$
\abs{h(z)}
=
\frac{\abs{f(z)}}{\abs{z}^2}
\leq
1.
$$
By continuity of $h$, the same inequality holds at $z=0$.
:::

<1>4. There is a constant $a\in\CC$ with $\abs{a}\leq1$ such that
$$
f(z)=az^2
$$
for every $z\in\CC$.

::: {.proof}
By step <1>3, $h$ is a bounded entire function. Liouville's theorem implies
that
$$
h(z)=a
$$
for some constant $a$. The same step gives $\abs a\leq1$. Since
$f(z)=z^2h(z)$, the stated formula follows.
:::

<1>5. Conversely, every function
$$
f(z)=az^2
$$
with $\abs{a}\leq1$ satisfies the hypothesis.

::: {.proof}
For every $z\in\CC$,
$$
\abs{f(z)}
=
\abs{a}\,\abs{z}^2
\leq
\abs z^2.
$$
:::

<1>6. The complete list is
$$
\boxed{
f(z)=az^2
\quad\text{with}\quad
a\in\CC, \abs{a}\leq1
}.
$$

::: {.proof}
Step <1>4 shows that every admissible entire function has this form, and
step <1>5 shows that every function of this form is admissible.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required classification.
:::
:::
