---
schema: qual/card@1
id: P-UCLAB07F-02
kind: problem
title: A limiting derivative implies differentiability at the missing point
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Let $f:(a,b)\to\mathbb R$ be continuous and differentiable on $(a,b)\setminus\{c\}$.
If $\lim_{x\to c}f'(x)=d\in\mathbb R$, show that $f$ is differentiable at $c$ and $f'(c)=d$.
:::

::: {.solution}
<1>1. For every $x\ne c$ sufficiently close to $c$, there exists $\xi_x$ strictly between $x$ and $c$ such that
\[
\frac{f(x)-f(c)}{x-c}=f'(\xi_x).
\]

::: {.proof}
Fix $x\in(a,b)$ with $x\ne c$. The function $f$ is continuous on the closed interval with endpoints $x$ and $c$, and differentiable in its interior because that interior does not contain $c$. The mean value theorem therefore gives a point $\xi_x$ between $x$ and $c$ such that
\[
f(x)-f(c)=f'(\xi_x)(x-c).
\]
Dividing by $x-c$ gives the formula.
:::

<1>2. As $x\to c$ with $x\ne c$, one has
\[
\xi_x\to c.
\]

::: {.proof}
Because $\xi_x$ lies between $x$ and $c$,
\[
|\xi_x-c|\le |x-c|.
\]
The right side tends to $0$ as $x\to c$, so the squeeze theorem gives $\xi_x\to c$.
:::

<1>3. The difference quotient of $f$ at $c$ satisfies
\[
\lim_{x\to c}
\frac{f(x)-f(c)}{x-c}
=d.
\]

::: {.proof}
By step <1>1,
\[
\frac{f(x)-f(c)}{x-c}=f'(\xi_x).
\]
By step <1>2, $\xi_x\to c$, and by hypothesis,
\[
\lim_{u\to c}f'(u)=d.
\]
Therefore
\[
f'(\xi_x)\to d,
\]
which proves the displayed limit.
:::

<1>4. The function $f$ is differentiable at $c$ and
\[
\boxed{f'(c)=d}.
\]

::: {.proof}
The limit in step <1>3 is exactly the definition of the derivative of $f$ at $c$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
