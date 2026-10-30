---
schema: qual/card@1
id: P-AMH-ALG-SG16-20
kind: problem
title: The ideal $(6,x+1)$ in $\ZZ[x]$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
Let $R=\ZZ[x]$ be the ring of polynomials (in one variable) with integer coefficients.
Note that the constant polynomial $6$ and the degree one polynomial $x+1$ are both elements of $R$.
Define
$$
I=\{6f+(x+1)g\mid f,g\in R\}.
$$
Prove that $I$ is an ideal of $R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
The set $I$ is nonempty.

::: pf-proof
Taking $f=g=0$ gives
$$
6f+(x+1)g=0,
$$
so $0\in I$.
:::

:::

::: {.pf-step #s1-2}
The set $I$ is closed under subtraction.

::: pf-proof
Let $a,b\in I$.  Then there exist
$f_1,f_2,g_1,g_2\in R$ such that
$$
a=6f_1+(x+1)g_1,
\qquad
b=6f_2+(x+1)g_2.
$$
Therefore
$$
\begin{aligned}
a-b
&=6(f_1-f_2)+(x+1)(g_1-g_2).
\end{aligned}
$$
Since $f_1-f_2,g_1-g_2\in R$, this expression has the defining form of an
element of $I$.  Hence $a-b\in I$.
:::

:::

::: {.pf-step #s1-3}
The set $I$ absorbs multiplication by arbitrary elements of $R$.

::: pf-proof
Let $a\in I$ and $h\in R$.  Write
$$
a=6f+(x+1)g
$$
with $f,g\in R$.  Since $R=\ZZ[x]$ is commutative,
$$
ha=ah
=6(hf)+(x+1)(hg).
$$
Because $hf,hg\in R$, the right-hand side belongs to $I$.  Thus both $ha$ and
$ah$ lie in $I$.
:::

:::

::: pf-step
Therefore $I$ is an ideal of $R$.

::: pf-proof
Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give the additive-subgroup condition by the subtraction
criterion, and step [](#s1-3){.pf-ref} gives the absorption condition.  Hence $I$ is an
ideal.
:::

:::

:::

:::
