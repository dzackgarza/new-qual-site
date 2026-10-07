---
schema: qual/card@1
id: P-WASE4
kind: problem
title: Rouché's theorem implies the Fundamental Theorem of Algebra
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Polynomials
  - Zeros
relations: []
review: draft
---

::: {.problem}
Use Rouche's theorem to prove the Fundamental Theorem of Algebra.
:::

::: {.solution}
Let
$$
p(z)=a_nz^n+a_{n-1}z^{n-1}+\cdots+a_0,
\qquad a_n\ne0,
$$
be a nonconstant polynomial, so $n\ge1$.

<1>1. There is $R>0$ such that on $|z|=R$,
$$
|p(z)-a_nz^n|<|a_nz^n|.
$$

::: {.proof}
For $z\ne0$,
$$
\frac{p(z)-a_nz^n}{a_nz^n}
=\sum_{k=0}^{n-1}\frac{a_k}{a_n}z^{k-n}.
$$
Every exponent $k-n$ is negative, so the right side tends to $0$ as
$|z|\to\infty$. Hence there exists $R>0$ such that
$$
\left|
\frac{p(z)-a_nz^n}{a_nz^n}
\right|<1
$$
whenever $|z|=R$. Multiplying by $|a_nz^n|$ gives the claim.
:::

<1>2. The polynomials $p(z)$ and $a_nz^n$ have the same number of zeros
inside $|z|<R$, counted with multiplicity.

::: {.proof}
Both functions are holomorphic on a neighborhood of the closed disk.
The strict boundary inequality in step <1>1 is exactly the hypothesis of
Rouché's theorem with
$$
f(z)=a_nz^n,
\qquad
g(z)=p(z)-a_nz^n.
$$
Therefore $f$ and $f+g=p$ have the same number of zeros in the disk,
counted with multiplicity.
:::

<1>3. The polynomial $p$ has exactly $n$ zeros in $|z|<R$, counted with
multiplicity.

::: {.proof}
The comparison function $a_nz^n$ has the single zero $z=0$ of
multiplicity $n$. Step <1>2 therefore implies that $p$ also has exactly
$n$ zeros in the disk, counted with multiplicity.
:::

<1>4. Every nonconstant complex polynomial has at least one complex
zero.

::: {.proof}
Since $n\ge1$, step <1>3 gives at least one zero of $p$ in $|z|<R$.
:::

<1>5. Every nonconstant polynomial in $\CC[z]$ factors completely into
linear factors.

::: {.proof}
Proceed by induction on the degree. For degree $1$ the claim is immediate.
For degree $n>1$, step <1>4 gives a root $\alpha\in\CC$. By the factor
theorem,
$$
p(z)=(z-\alpha)q(z)
$$
for a polynomial $q$ of degree $n-1$. The induction hypothesis factors
$q$ completely into linear factors, and hence so does $p$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>4--<1>5 prove the Fundamental Theorem of Algebra using Rouché's
theorem.
:::
:::
