---
schema: qual/card@1
id: P-BKS77-4
kind: problem
title: Fundamental theorem of algebra
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Prove the Fundamental Theorem of Algebra: every nonconstant polynomial with complex coefficients has a complex root.
:::

::: {.solution}
Let
$$
p(z)=a_nz^n+a_{n-1}z^{n-1}+\cdots+a_0,
\qquad
n\geq1,
\qquad
a_n\neq0.
$$

<1>1. One has
$$
|p(z)|\longrightarrow\infty
\qquad
\text{as }|z|\longrightarrow\infty.
$$

::: {.proof}
Factor out the leading term:
$$
p(z)
=
a_nz^n
\left(
1+\frac{a_{n-1}}{a_nz}
+\cdots+
\frac{a_0}{a_nz^n}
\right).
$$
The parenthesized factor tends to $1$ as $|z|\to\infty$. Hence there is $R>0$ such that for $|z|\geq R$ its modulus is at least $1/2$. Therefore
$$
|p(z)|
\geq
\frac{|a_n|}{2}|z|^n
\longrightarrow\infty.
$$
:::

<1>2. If $p$ had no zero in $\mathbb C$, then
$$
f(z)\coloneqq\frac1{p(z)}
$$
would be an entire function.

::: {.proof}
Under the stated assumption, the denominator $p(z)$ is nonzero for every $z\in\mathbb C$. Since $p$ is entire, its reciprocal is holomorphic on all of $\mathbb C$.
:::

<1>3. Under the assumption of step <1>2, the entire function $f=1/p$ is bounded.

::: {.proof}
By step <1>1 there is $R>0$ such that
$$
|p(z)|\geq1
$$
whenever $|z|\geq R$. Hence
$$
|f(z)|\leq1
$$
outside the closed disk $\{|z|\leq R\}$.

On that closed disk, $f$ is continuous, so compactness gives a finite maximum
$$
M\coloneqq\max_{|z|\leq R}|f(z)|.
$$
Thus
$$
|f(z)|\leq\max\{1,M\}
$$
for all $z\in\mathbb C$.
:::

<1>4. The assumption that $p$ has no complex zero is impossible.

::: {.proof}
By steps <1>2--<1>3, $f=1/p$ is a bounded entire function. Liouville's theorem therefore implies that $f$ is constant. Hence $p=1/f$ is constant, contradicting $n\geq1$.
:::

<1>5. Therefore every nonconstant complex polynomial has a complex root.

::: {.proof}
Step <1>4 shows that the contrary assumption leads to a contradiction.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the Fundamental Theorem of Algebra.
:::
:::
