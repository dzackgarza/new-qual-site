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
Let $f:(a,b)\to\RR$ be continuous and differentiable on $(a,b)\setminus\{c\}$.
If $\lim_{x\to c}f'(x)=d\in\RR$, show that $f$ is differentiable at $c$ and $f'(c)=d$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $x\ne c$ sufficiently close to $c$, there exists $\xi_x$ strictly between $x$ and $c$ such that
$$
\frac{f(x)-f(c)}{x-c}=f'(\xi_x).
$$


::: pf-proof

Fix $x\in(a,b)$ with $x\ne c$. The function $f$ is continuous on the closed interval with endpoints $x$ and $c$, and differentiable in its interior because that interior does not contain $c$. The mean value theorem therefore gives a point $\xi_x$ between $x$ and $c$ such that
$$
f(x)-f(c)=f'(\xi_x)(x-c).
$$
Dividing by $x-c$ gives the formula.

:::

:::

::: {.pf-step #s1-2}

As $x\to c$ with $x\ne c$, one has
$$
\xi_x\to c.
$$


::: pf-proof

Because $\xi_x$ lies between $x$ and $c$,
$$
|\xi_x-c|\le |x-c|.
$$
The right side tends to $0$ as $x\to c$, so the squeeze theorem gives $\xi_x\to c$.

:::

:::

::: {.pf-step #s1-3}

The difference quotient of $f$ at $c$ satisfies
$$
\lim_{x\to c}
\frac{f(x)-f(c)}{x-c}
=d.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\frac{f(x)-f(c)}{x-c}=f'(\xi_x).
$$
By step [](#s1-2){.pf-ref}, $\xi_x\to c$, and by hypothesis,
$$
\lim_{u\to c}f'(u)=d.
$$
Therefore
$$
f'(\xi_x)\to d,
$$
which proves the displayed limit.

:::

:::

::: {.pf-step #s1-4}

The function $f$ is differentiable at $c$ and
$$
\boxed{f'(c)=d}.
$$


::: pf-proof

The limit in step [](#s1-3){.pf-ref} is exactly the definition of the derivative of $f$ at $c$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
