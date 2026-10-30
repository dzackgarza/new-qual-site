---
schema: qual/card@1
id: P-TIE-F15-10
kind: problem
title: Entire functions with $f(z)\to\infty$ are polynomials
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 10.
---

::: {.problem}
Let $f$ be entire and suppose that $\lim_{z \to \infty} f(z) = \infty$. Show that $f$ is a polynomial.
:::

::: {.solution}

Define
$$
g(w)\coloneqq f(1/w)
$$
for $w\ne0$.

::: pf

::: pf-step

The point $w=0$ is a pole of $g$.


::: pf-proof

The function $g$ is holomorphic on a punctured neighborhood of $0$, because $f$ is entire. Moreover,
$$
\abs{g(w)}
=
\abs{f(1/w)}
\longrightarrow\infty
$$
as $w\to0$, since $1/w\to\infty$. Therefore $0$ is a pole of $g$.

:::

:::

::: {.pf-step #s1-2}

There exists an integer $m\ge0$ such that
$$
w^m g(w)
$$
extends holomorphically to $w=0$.


::: pf-proof

This is the defining local property of a pole of finite order. If the pole has order $m$, then $w^m g(w)$ extends holomorphically across $0$ with nonzero value there.

:::

:::

::: {.pf-step #s1-3}

If
$$
f(z)=\sum_{n=0}^{\infty}c_nz^n,
$$
then
$$
c_n=0
$$
for every $n>m$.


::: pf-proof

Because $f$ is entire, its Taylor series at $0$ converges for every $z\in\CC$. For $w\ne0$,
$$
g(w)
=
f(1/w)
=
\sum_{n=0}^{\infty}c_nw^{-n}.
$$
Thus
$$
w^mg(w)
=
\sum_{n=0}^{\infty}c_nw^{m-n}.
$$
By step [](#s1-2){.pf-ref}, the left-hand side is holomorphic at $0$. A Laurent expansion of a holomorphic function at $0$ has no negative powers. Hence every coefficient of $w^{m-n}$ with $m-n<0$ must vanish. Therefore $c_n=0$ for all $n>m$.

:::

:::

::: {.pf-step #s1-4}

The function $f$ is a polynomial.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\boxed{
f(z)=\sum_{n=0}^{m}c_nz^n.
}
$$
This is a polynomial of degree at most $m$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
