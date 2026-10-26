---
schema: qual/card@1
id: P-3IDAX
kind: problem
title: Fundamental theorem of algebra
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Polynomials
  - Zeros
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
Prove the Fundamental Theorem of Algebra (using complex analysis).
:::

Let
$$
p(z)=a_nz^n+a_{n-1}z^{n-1}+\cdots+a_0,
\qquad a_n\ne0,
$$
be a nonconstant complex polynomial.

::: pf

::: pf-step

If $p$ has no zero in $\CC$, then $1/p$ is entire.


::: pf-proof

The polynomial $p$ is entire. Under the assumption that $p(z)\ne0$ for
every $z\in\CC$, the reciprocal of $p$ is holomorphic at every point.
Hence $1/p$ is entire.

:::

:::

::: pf-step

There exist $R>0$ and $c>0$ such that
$$
|p(z)|\ge c|z|^n
$$
whenever $|z|\ge R$.


::: pf-proof

For $z\ne0$,
$$
\frac{p(z)}{z^n}
=a_n+\frac{a_{n-1}}z+\cdots+\frac{a_0}{z^n}.
$$
The sum after $a_n$ tends to $0$ as $|z|\to\infty$. Therefore there is
$R>0$ such that, for $|z|\ge R$,
$$
\left|
\frac{a_{n-1}}z+\cdots+\frac{a_0}{z^n}
\right|
\le \frac{|a_n|}{2}.
$$
The reverse triangle inequality then gives
$$
\left|\frac{p(z)}{z^n}\right|
\ge |a_n|-\frac{|a_n|}{2}
=\frac{|a_n|}{2}.
$$
Thus the claim holds with $c=|a_n|/2$.

:::

:::

::: pf-step

Under the assumption of step <1>1, the function $1/p$ is bounded
on $\CC$.


::: pf-proof

By step <1>2, for $|z|\ge R$,
$$
\left|\frac1{p(z)}\right|
\le \frac{1}{c|z|^n}
\le \frac{1}{cR^n}.
$$
On the closed disk $|z|\le R$, the continuous function $|p|$ attains a
minimum. Since $p$ has no zero by assumption, that minimum is a positive
number $m>0$. Hence
$$
\left|\frac1{p(z)}\right|\le\frac1m
$$
for $|z|\le R$. Combining the two regions gives a global bound for
$1/p$.

:::

:::

::: pf-step

The assumption that $p$ has no zero leads to a contradiction.


::: pf-proof

By steps <1>1 and <1>3, the function $1/p$ is bounded and entire.
Liouville's theorem therefore implies that $1/p$ is constant. Hence $p$
is constant, contradicting the hypothesis that $\deg p=n\ge1$.

:::

:::

::: pf-step

Every nonconstant polynomial in $\CC[z]$ has a zero in $\CC$.


::: pf-proof

Step <1>4 proves that a nonconstant complex polynomial cannot be
zero-free. Therefore it has at least one complex root.

:::

:::

::: pf-step

Consequently every nonconstant polynomial in $\CC[z]$ factors
completely into linear factors.


::: pf-proof

Proceed by induction on the degree. Step <1>5 gives a root $\alpha$, so
the factor theorem yields
$$
p(z)=(z-\alpha)q(z)
$$
with $\deg q=\deg p-1$. Repeating the argument inductively gives a
factorization into linear factors. This is the Fundamental Theorem of
Algebra.

:::

:::

::: pf-qed

Steps <1>5--<1>6 prove the Fundamental Theorem of Algebra by complex
analysis.

:::

:::
