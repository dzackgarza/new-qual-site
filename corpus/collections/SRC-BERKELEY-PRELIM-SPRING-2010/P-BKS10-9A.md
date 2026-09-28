---
schema: qual/card@1
id: P-BKS10-9A
kind: problem
title: Solutions of $xy'+y=x$ for $x>0$
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
  note: Independently checked the product-rule integration and the converse substitution.
---

::: {.problem}
Find all solutions of
$$
xy'+y=x
$$
for $x>0$.
:::

::: {.solution}
<1>1. The differential equation is equivalent to
$$
(xy)'=x.
$$

::: {.proof}
By the product rule,
$$
(xy)'=xy'+y.
$$
Thus the given equation
$$
xy'+y=x
$$
is exactly the displayed derivative identity.
:::

<1>2. Every solution on $(0,\infty)$ has the form
$$
\boxed{
y(x)=\frac{x}{2}+\frac{C}{x}
}
$$
for some constant $C\in\RR$.

::: {.proof}
Integrating the identity in step <1>1 on the connected interval
$(0,\infty)$ gives
$$
xy
=
\frac{x^2}{2}+C
$$
for some constant $C$. Since $x>0$, division by $x$ gives
$$
y(x)=\frac{x}{2}+\frac{C}{x}.
$$
:::

<1>3. Every function displayed in step <1>2 is a solution.

::: {.proof}
For
$$
y(x)=\frac{x}{2}+\frac{C}{x},
$$
one has
$$
y'(x)=\frac12-\frac{C}{x^2}.
$$
Therefore
$$
xy'(x)+y(x)
=
x\left(\frac12-\frac{C}{x^2}\right)
+
\frac{x}{2}+\frac{C}{x}
=
x.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 give exactly all solutions on $x>0$.
:::
:::
