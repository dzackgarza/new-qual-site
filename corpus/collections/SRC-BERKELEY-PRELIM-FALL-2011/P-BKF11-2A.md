---
schema: qual/card@1
id: P-BKF11-2A
kind: problem
title: An irreducible polynomial whose roots are closed under squaring divides $x^n-1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 2A of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently supplied the closure-under-squaring step via the
    divisibility f(x) | f(x^2), then checked the finite root-orbit argument.
---

::: {.problem}
Let $f(x)$ be an irreducible polynomial over $\QQ$.
Let $a\in\CC$ be a nonzero root such that $a^2$ is also a root.
Prove that for some $n$, the polynomial $f(x)$ divides $x^n-1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The polynomial $f(x)$ divides $f(x^2)$ in $\QQ[x]$.

::: pf-proof

Let $m_a(x)$ be the minimal polynomial of $a$ over $\QQ$. Since
$f(a)=0$, the polynomial $m_a$ divides $f$. Both are nonconstant and
$f$ is irreducible, so $f$ and $m_a$ differ by a nonzero rational
scalar.

The hypothesis that $a^2$ is also a root of $f$ gives
$$
f(a^2)=0.
$$
Thus $a$ is a root of the polynomial $f(x^2)$. By the defining
minimality of $m_a$, one has
$$
m_a(x)\mid f(x^2).
$$
Since $f$ is a nonzero scalar multiple of $m_a$, it follows that
$f(x)\mid f(x^2)$.

:::

:::

::: {.pf-step #s2}

If $b\in\CC$ is any root of $f$, then $b^2$ is also a root of
$f$. Consequently,
$$
a,a^2,a^{2^2},a^{2^3},\ldots
$$
are all roots of $f$.

::: pf-proof

By step [](#s1){.pf-ref}, there is $q(x)\in\QQ[x]$ such that
$$
f(x^2)=f(x)q(x).
$$
If $f(b)=0$, evaluation at $b$ gives
$$
f(b^2)=f(b)q(b)=0.
$$
Starting with the root $a$ and applying this implication repeatedly
proves the final assertion.

:::

:::

::: {.pf-step #s3}

There is a positive integer $N$ such that $a^N=1$.

::: pf-proof

The polynomial $f$ has only finitely many complex roots, whereas
step [](#s2){.pf-ref} gives the infinite sequence of roots
$a^{2^r}$ for $r\ge0$. Hence there exist integers $0\le r<s$ such
that
$$
a^{2^r}=a^{2^s}.
$$
Because $a\ne0$, division by $a^{2^r}$ gives
$$
a^{2^s-2^r}=1.
$$
Thus
$$
N\coloneqq2^s-2^r>0
$$
has the required property.

:::

:::

::: {.pf-step #s4}

For the integer $N$ from step [](#s3){.pf-ref},
$$
\boxed{f(x)\mid x^N-1}.
$$

::: pf-proof

Step [](#s3){.pf-ref} says that $a$ is a root of $x^N-1$. Hence its minimal
polynomial $m_a$ divides $x^N-1$. As in step [](#s1){.pf-ref}, irreducibility of
$f$ and the equality $f(a)=0$ imply that $f$ is a nonzero rational
scalar multiple of $m_a$. Therefore $f$ also divides $x^N-1$ in
$\QQ[x]$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} establishes the required divisibility for the positive
integer $N$.

:::

:::

:::
