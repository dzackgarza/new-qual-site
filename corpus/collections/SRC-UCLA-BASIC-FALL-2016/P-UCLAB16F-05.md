---
schema: qual/card@1
id: P-UCLAB16F-05
kind: problem
title: Multipliers preserving a finite $\mathbb Q$-span of complex numbers are algebraic
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 5 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
Let $\alpha _ { 1 } , \cdots , \alpha _ { n }$ be complex numbers, and $\begin{array} { r } { V = \{ \sum _ { i = 1 } ^ { n } a _ { i } \alpha _ { i } | a _ { i } \in \mathbb { Q } \} } \end{array}$ be the vector subspace of C spanned by them over the field of rational numbers, $\mathbb { Q }$ . Let $\beta$ be a complex number such that $\beta V \subset V$ where $\beta V = \{ \beta v | v \in V \}$ Show that $\beta$ is the root of a degree n polynomial with rational coefficients.
:::

::: {.solution}
As printed, the statement has the degenerate exception
\[
V=\{0\}.
\]
If
\[
\alpha_1=\cdots=\alpha_n=0,
\]
then
\[
\beta V\subseteq V
\]
for every complex number $\beta$, including transcendental ones.
Assume therefore that
\[
V\ne\{0\},
\]
which is the intended nondegenerate case.

<1>1. The $\mathbb Q$-dimension of $V$ satisfies
\[
1\le \dim_{\mathbb Q}V\le n.
\]

::: {.proof}
The space $V$ is generated over $\mathbb Q$ by the $n$ vectors
\[
\alpha_1,\ldots,\alpha_n,
\]
so its dimension is at most $n$.
The assumption
\[
V\ne\{0\}
\]
gives positive dimension.
:::

<1>2. Choose
\[
0\ne v\in V.
\]
Then for every integer $k\ge0$,
\[
\beta^kv\in V.
\]

::: {.proof}
The case $k=0$ is immediate.
If
\[
\beta^kv\in V,
\]
then the hypothesis
\[
\beta V\subseteq V
\]
gives
\[
\beta^{k+1}v
=
\beta(\beta^kv)
\in V.
\]
Thus the claim follows by induction.
:::

<1>3. Let
\[
d=\dim_{\mathbb Q}V.
\]
Then the $d+1$ vectors
\[
v,\beta v,\beta^2v,\ldots,\beta^dv
\]
are linearly dependent over $\mathbb Q$.

::: {.proof}
All these vectors lie in $V$ by step <1>2.
The vector space $V$ has dimension $d$, so any $d+1$ vectors in it are linearly dependent.
:::

<1>4. There exist rational numbers
\[
c_0,\ldots,c_d,
\]
not all zero, such that
\[
\sum_{k=0}^d c_k\beta^kv=0.
\]

::: {.proof}
This is exactly the linear dependence supplied by step <1>3.
:::

<1>5. Since $v\ne0$,
\[
\sum_{k=0}^d c_k\beta^k=0.
\]

::: {.proof}
Factor the relation in step <1>4 inside the complex numbers:
\[
\left(
\sum_{k=0}^d c_k\beta^k
\right)v
=0.
\]
Because $v$ is a nonzero complex number, division by $v$ gives the displayed scalar equation.
:::

<1>6. Thus $\beta$ is a root of a nonzero polynomial
\[
p(X)=\sum_{k=0}^d c_kX^k
\in\mathbb Q[X]
\]
of degree at most $d\le n$.

::: {.proof}
The coefficients are rational by step <1>4, the polynomial is nonzero because the coefficients are not all zero, and step <1>5 gives
\[
p(\beta)=0.
\]
Its degree is at most $d$, and step <1>1 gives
\[
d\le n.
\]
:::

<1>7. If a polynomial of degree exactly $n$ is required, define
\[
P(X)=X^{\,n-\deg p}p(X).
\]
Then
\[
\deg P=n
\]
and
\[
P(\beta)=0.
\]

::: {.proof}
The exponent
\[
n-\deg p
\]
is a nonnegative integer by step <1>6.
Thus $P\in\mathbb Q[X]$ has degree exactly $n$.
Since
\[
p(\beta)=0,
\]
one also has
\[
P(\beta)=0.
\]
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>7 prove the intended statement under the necessary hypothesis
\[
V\ne\{0\},
\]
while the opening observation records the counterexample in the omitted zero-span case.
:::
:::
