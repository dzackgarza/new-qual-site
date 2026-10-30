---
schema: qual/card@1
id: P-BKS80-5
kind: problem
title: A coefficient inequality forces a holomorphic disk function to be injective
classification: {areas: [prelim], topics: [Complex Analysis]}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the factorization of f(z)-f(w), absolute convergence of the
    resulting quotient series, and the strict disk-radius estimate preventing
    the higher-order terms from cancelling a_1.
---

::: {.problem}
Let
$$
f(z)=\sum_{n=0}^{\infty}a_nz^n
$$
be analytic in the unit disk. Assume $a_1\ne0$ and
$$
\sum_{n=2}^{\infty}n\abs{a_n}\le \abs{a_1}.
$$
Prove that $f$ is injective.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $z,w$ lie in the unit disk and $z\ne w$, then
$$
\frac{f(z)-f(w)}{z-w}
=
a_1
+
\sum_{n=2}^{\infty}
a_n
\sum_{j=0}^{n-1}z^{n-1-j}w^j.
$$

::: pf-proof

For every $n\ge1$,
$$
z^n-w^n
=
(z-w)\sum_{j=0}^{n-1}z^{n-1-j}w^j.
$$
The coefficient hypothesis implies
$$
\sum_{n=2}^{\infty}\abs{a_n}<\infty.
$$
Thus, for fixed $z,w$ in the unit disk, the relevant power series are
absolutely convergent and the identity may be applied term by term to
$f(z)-f(w)$. The $n=0$ terms cancel, giving the displayed formula.

:::

:::

::: {.pf-step #s2}

Put
$$
r\coloneqq\max\{\abs{z},\abs{w}\}<1.
$$
Then the higher-order part in step [](#s1){.pf-ref} satisfies
$$
\abs{
\sum_{n=2}^{\infty}
a_n
\sum_{j=0}^{n-1}z^{n-1-j}w^j
}
<
\abs{a_1}.
$$

::: pf-proof

For $n\ge2$,
$$
\abs{
\sum_{j=0}^{n-1}z^{n-1-j}w^j
}
\le
nr^{n-1}
\le
nr.
$$
Hence
$$
\begin{aligned}
\abs{
\sum_{n=2}^{\infty}
a_n
\sum_{j=0}^{n-1}z^{n-1-j}w^j
}
&\le
r\sum_{n=2}^{\infty}n\abs{a_n}\\
&\le
r\abs{a_1}\\
&<
\abs{a_1},
\end{aligned}
$$
because $r<1$ and $a_1\ne0$.

:::

:::

::: {.pf-step #s3}

For distinct $z,w$ in the unit disk,
$$
f(z)\ne f(w).
$$

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref} and the reverse triangle inequality,
$$
\abs{
\frac{f(z)-f(w)}{z-w}
}
\ge
\abs{a_1}
-
\abs{
\sum_{n=2}^{\infty}
a_n
\sum_{j=0}^{n-1}z^{n-1-j}w^j
}
>
0.
$$
Therefore $(f(z)-f(w))/(z-w)\ne0$, and since $z-w\ne0$, one has
$f(z)-f(w)\ne0$.

:::

:::

::: {.pf-step #s4}

Thus $f$ is injective on the unit disk.

::: pf-proof

Step [](#s3){.pf-ref} is exactly the injectivity condition.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the assertion.

:::

:::

:::
