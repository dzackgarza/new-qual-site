---
schema: qual/card@1
id: P-BKS82-1
kind: problem
title: Fundamental theorem of algebra
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked directly against the retained PDF because the extracted markdown is unreliable for this source.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the polynomial growth estimate, boundedness of the reciprocal, and the Liouville-theorem contradiction.
---

::: {.problem}
Prove the Fundamental Theorem of Algebra: every nonconstant polynomial with complex coefficients has a complex root.
:::

::: {.solution}
Let
$$
p(z)=a_nz^n+a_{n-1}z^{n-1}+\cdots+a_0,
\qquad
n\ge1,
\qquad
a_n\ne0.
$$

::: pf

::: {.pf-step #growth-estimate}
There is an $R>0$ such that
$$
\abs{p(z)}
\ge
\frac{\abs{a_n}}2\abs{z}^n
$$
whenever $\abs{z}\ge R$.

::: pf-proof
For $z\ne0$,
$$
\frac{p(z)}{a_nz^n}
=
1+
\frac{a_{n-1}}{a_n}z^{-1}
+\cdots+
\frac{a_0}{a_n}z^{-n}.
$$
The terms after $1$ tend to $0$ as $\abs{z}\to\infty$. Hence there is
$R>0$ such that
$$
\abs{
\frac{p(z)}{a_nz^n}-1
}
\le\frac12
$$
for $\abs{z}\ge R$. The reverse triangle inequality then gives
$$
\abs{
\frac{p(z)}{a_nz^n}
}
\ge\frac12,
$$
which is the asserted estimate.
:::

:::

::: {.pf-step #reciprocal-bounded-outside-disk}
Suppose, for contradiction, that $p$ has no zero in $\CC$. Then
$$
f(z)\coloneqq\frac1{p(z)}
$$
is an entire function and is bounded on $\{z:\abs{z}\ge R\}$.

::: pf-proof
The assumption that $p$ has no zero makes $1/p$ holomorphic on all of
$\CC$. By step [](#growth-estimate){.pf-ref}, for $\abs{z}\ge R$,
$$
\abs{f(z)}
=
\frac1{\abs{p(z)}}
\le
\frac{2}{\abs{a_n}\abs{z}^n}
\le
\frac{2}{\abs{a_n}R^n}.
$$
Thus $f$ is bounded outside the open disk of radius $R$.
:::

:::

::: {.pf-step #reciprocal-bounded-everywhere}
Under the assumption in step [](#reciprocal-bounded-outside-disk){.pf-ref}, the entire function $f$ is
bounded on all of $\CC$.

::: pf-proof
The function $f$ is continuous on the compact disk
$$
\{z:\abs{z}\le R\},
$$
so it is bounded there. Step [](#reciprocal-bounded-outside-disk){.pf-ref} gives a bound on the complement of that
disk. Combining the two bounds shows that $f$ is bounded on $\CC$.
:::

:::

::: {.pf-step #no-root-impossible}
The assumption that $p$ has no complex root is impossible.

::: pf-proof
By step [](#reciprocal-bounded-everywhere){.pf-ref} and Liouville's theorem, $f$ is constant. Since
$f=1/p$ never vanishes, its constant value is nonzero, and therefore
$p=1/f$ is constant. This contradicts $n\ge1$.
:::

:::

::: {.pf-step #root-exists}
Every nonconstant polynomial with complex coefficients has a complex
root.

::: pf-proof
If such a polynomial had no complex root, step [](#no-root-impossible){.pf-ref} would give a
contradiction. Therefore it has at least one root in $\CC$.
:::

:::

::: pf-qed
Step [](#root-exists){.pf-ref} is precisely the Fundamental Theorem of Algebra in the form
requested.
:::

:::
:::
