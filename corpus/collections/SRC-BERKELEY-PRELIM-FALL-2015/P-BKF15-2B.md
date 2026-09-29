---
schema: qual/card@1
id: P-BKF15-2B
kind: problem
title: A function starting at $1$ that cannot increase above $1$ stays at most $1$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Statement checked against F15_Exam.pdf problem 2B; restored the lost arrow and the bullets for the last two hypotheses.
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet: each
    connected component of the open superlevel set {f>1} begins at a point
    where f=1, while f'<=0 throughout the component.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the superlevel-set boundary value, the mean-value-theorem
    monotonicity argument including a=0, and the resulting contradiction.
---

::: {.problem}
Let $f \colon [0, \infty) \to \mathbb{R}$ be a function, and assume that:

- $f$ is continuous on $[0, \infty)$;
- $f$ is differentiable on $(0, \infty)$;
- $f'(x) \leq 0$ for all $x > 0$ such that $f(x) > 1$; and
- $f(0) = 1$.

Prove that $f(x) \leq 1$ for all $x \geq 0$.
:::

::: {.solution}
Let
$$
U\coloneqq\{x\in[0,\infty):f(x)>1\}.
$$

::: pf

::: pf-step

The set $U$ is open in $\RR$ and does not contain $0$.

::: pf-proof

Since $f$ is continuous,
$$
U=f^{-1}((1,\infty))
$$
is open in the relative topology of $[0,\infty)$. Also
$$
f(0)=1,
$$
so $0\notin U$. Any relatively open subset of $[0,\infty)$ that does
not contain $0$ is open in $\RR$. Thus $U$ is open in $\RR$.

:::

:::

::: {.pf-step #s2}

If $U$ is nonempty and $(a,b)$ is one of its connected
components, then
$$
f(a)=1.
$$

::: pf-proof

Because $U\subset(0,\infty)$ is open, each component is an open
interval $(a,b)$ with $a\ge0$. Choose a sequence
$$
x_n\in(a,b)
$$
with $x_n\downarrow a$. Then
$$
f(x_n)>1
$$
for all $n$, so continuity gives
$$
f(a)\ge1.
$$

If $f(a)>1$, continuity would give an interval around $a$ on which
$f>1$. This would either put $a$ in $U$ or extend the component to the
left, both impossible. Hence $f(a)=1$.

:::

:::

::: {.pf-step #s3}

On every component $(a,b)$ of $U$, the function $f$ is
nonincreasing on $[a,b)$.

::: pf-proof

Take
$$
a\le x<y<b.
$$
The function $f$ is continuous on $[x,y]$ and differentiable on
$(x,y)$. Every point $c\in(x,y)$ belongs to $U$, so
$$
f(c)>1
$$
and the hypothesis gives
$$
f'(c)\le0.
$$
By the mean value theorem there exists $c\in(x,y)$ such that
$$
f(y)-f(x)=f'(c)(y-x)\le0.
$$
Therefore $f(y)\le f(x)$. This also applies when $x=a$: continuity at
$a$ and differentiability on $(a,y)$ are exactly the hypotheses of
the mean value theorem.

:::

:::

::: {.pf-step #s4}

The set $U$ is empty.

::: pf-proof

Suppose $U\ne\varnothing$, and let $(a,b)$ be a component. For any
$x\in(a,b)$, step [](#s3){.pf-ref} and step [](#s2){.pf-ref} give
$$
f(x)\le f(a)=1.
$$
But $x\in U$ means $f(x)>1$, a contradiction.

:::

:::

::: {.pf-step #s5}

Hence
$$
\boxed{f(x)\le1\quad\text{for every }x\ge0}.
$$

::: pf-proof

By step [](#s4){.pf-ref} there is no $x\ge0$ with $f(x)>1$, which is exactly the
displayed conclusion.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required statement.

:::

:::

:::
