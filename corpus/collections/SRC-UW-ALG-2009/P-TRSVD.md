---
schema: qual/card@1
id: P-TRSVD
kind: problem
title: 'A root extension of an irreducible polynomial: existence, basis, and $\theta^{-1}$;
  irreducibility of $x^3+9x+6$ and the inverse of $1+\theta$'
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Irreducibility Criteria
  - Bases
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $F$ be a field and $p(x)\in F[x]$ an irreducible polynomial.

- Prove that there exists a field extension $K$ of $F$ in which $p(x)$ has a root.

- Determine the dimension of $K$ as a vector space over $F$ and exhibit a vector space basis for $K$.

- If $\theta\in K$ denotes a root of $p(x)$, express $\theta\inv$ in terms of the basis found in part (b).

- Suppose $p(x)=x^3+9x+6$.
  Show $p(x)$ is irreducible over $\mathbb Q$.
  If $\theta$ is a root of $p(x)$, compute the inverse of $(1+\theta)$ in $\mathbb Q(\theta)$.
:::


::: solution
<1>1. There exists an extension field $K/F$ in which $p$ has a root.
::: {.proof}
Let
\[
K=F[x]/(p(x)).
\]
Because $p$ is irreducible, the ideal $(p)$ is maximal in the PID $F[x]$, so $K$ is a field. If
\[
\theta=x+(p)\in K,
\]
then by construction $p(\theta)=0$.
:::

<1>2. If $n=\deg p$, then
\[
[K:F]=n,
\qquad
1,\theta,\theta^2,\ldots,\theta^{n-1}
\]
is an $F$-basis of $K$.
::: {.proof}
Every class in $F[x]/(p)$ has a unique representative of degree $<n$ by Euclidean division by $p$. Hence the displayed powers span. If
\[
a_0+a_1\theta+\cdots+a_{n-1}\theta^{n-1}=0,
\]
then the polynomial $a_0+a_1x+\cdots+a_{n-1}x^{n-1}$ lies in $(p)$. Its degree is $<\deg p$, so it must be zero. Thus the displayed powers are linearly independent.
:::

<1>3. Assume $p(0)\ne0$. Write
\[
p(x)=a_0+a_1x+\cdots+a_nx^n,
\qquad a_0\ne0.
\]
Then
\[
\theta^{-1}
=-\frac{a_1+a_2\theta+\cdots+a_n\theta^{n-1}}{a_0}.
\]
::: {.proof}
Since $p(\theta)=0$,
\[
a_0+\theta(a_1+a_2\theta+\cdots+a_n\theta^{n-1})=0.
\]
Because $a_0\ne0$, necessarily $\theta\ne0$, so division by $\theta$ gives the formula.

As the source problem is written, the hypothesis $p(0)\ne0$ is necessary: if $p(x)=x$, then $p$ is irreducible but its root $\theta=0$ has no inverse.
:::

<1>4. The polynomial
\[
p(x)=x^3+9x+6
\]
is irreducible over $\mathbb Q$.
::: {.proof}
A reducible cubic over a field has a root in that field. Since $p$ is monic with integer coefficients, any rational root must be an integer divisor of $6$. Direct substitution of
\[
\pm1,\ \pm2,\ \pm3,\ \pm6
\]
shows that none is a root. Hence $p$ has no rational root and is irreducible over $\mathbb Q$.
:::

<1>5. If $\theta^3+9\theta+6=0$, then
\[
(1+\theta)^{-1}=\frac{\theta^2-\theta+10}{4}.
\]
::: {.proof}
Using $\theta^3=-9\theta-6$,
\[
\begin{aligned}
(1+\theta)(\theta^2-\theta+10)
&=\theta^3+9\theta+10\\
&=(-9\theta-6)+9\theta+10\\
&=4.
\end{aligned}
\]
Therefore dividing by $4$ gives the inverse.
:::
:::
