---
schema: qual/card@1
id: P-BKF87-3
kind: problem
title: Existence of a logarithmically renormalized singular-integral limit
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Show that the limit
\[
\lim_{t\to0^+}\left(
\int_0^1\frac{dx}{(x^4+t^4)^{1/4}}+\log t
\right)
\]
exists and is finite.
:::

::: {.solution}
<1>1. For $t>0$, putting $R=1/t$ gives
$$
\int_0^1\frac{dx}{(x^4+t^4)^{1/4}}+\log t
=
\int_0^R\frac{du}{(1+u^4)^{1/4}}-\log R.
$$

::: {.proof}
Make the substitution
$$
x=tu.
$$
Then
$$
dx=t\,du
$$
and
$$
(x^4+t^4)^{1/4}
=
t(1+u^4)^{1/4}.
$$
Therefore
$$
\int_0^1\frac{dx}{(x^4+t^4)^{1/4}}
=
\int_0^{1/t}\frac{du}{(1+u^4)^{1/4}}.
$$
Since $\log t=-\log(1/t)$, the displayed identity follows.
:::

<1>2. For $u\geq1$,
$$
\left|
\frac1{(1+u^4)^{1/4}}-\frac1u
\right|
\leq
\frac1{4u^5}.
$$

::: {.proof}
For $u\geq1$,
$$
\frac1{(1+u^4)^{1/4}}
=
\frac1u(1+u^{-4})^{-1/4}.
$$
Let
$$
\psi(s)=(1+s)^{-1/4}
$$
for $s\in[0,1]$. Since
$$
\abs{\psi'(s)}
=
\frac14(1+s)^{-5/4}
\leq
\frac14,
$$
the mean value theorem gives
$$
\abs{\psi(s)-1}\leq\frac{s}{4}.
$$
Taking $s=u^{-4}$ and multiplying by $1/u$ gives the claimed estimate.
:::

<1>3. The improper integral
$$
\int_1^\infty
\left(
\frac1{(1+u^4)^{1/4}}-\frac1u
\right)\,du
$$
converges absolutely.

::: {.proof}
By step <1>2, the absolute value of the integrand is bounded on $[1,\infty)$ by
$$
\frac1{4u^5}.
$$
Since
$$
\int_1^\infty\frac{du}{u^5}<\infty,
$$
the comparison test gives absolute convergence.
:::

<1>4. For every $R\geq1$,
$$
\int_0^R\frac{du}{(1+u^4)^{1/4}}-\log R
=
\int_0^1\frac{du}{(1+u^4)^{1/4}}
+
\int_1^R
\left(
\frac1{(1+u^4)^{1/4}}-\frac1u
\right)\,du.
$$

::: {.proof}
Split the first integral at $1$ and use
$$
\log R=\int_1^R\frac{du}{u}.
$$
Combining the two integrals over $[1,R]$ gives the displayed identity.
:::

<1>5. The limit in the problem exists and is finite.

::: {.proof}
As $t\to0^+$, one has $R=1/t\to\infty$. By step <1>4, the expression in step <1>1 tends to
$$
\int_0^1\frac{du}{(1+u^4)^{1/4}}
+
\int_1^\infty
\left(
\frac1{(1+u^4)^{1/4}}-\frac1u
\right)\,du.
$$
The first integral is finite because its integrand is continuous on $[0,1]$, and the second is finite by step <1>3. Hence the required limit exists and is finite.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves the assertion.
:::
:::
