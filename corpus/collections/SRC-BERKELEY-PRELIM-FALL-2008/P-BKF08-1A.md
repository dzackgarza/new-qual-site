---
schema: qual/card@1
id: P-BKF08-1A
kind: problem
title: A convergent rational series whose partial sums are Cauchy in every $p$-adic metric
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 1A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked convergence and the preservation of p^m-divisibility
    after adding and reducing finite tail sums.
---

::: {.problem}
Find a sequence $(r_n)$ of positive rational numbers such that $\sum_{n=0}^{\infty}r_n$ converges and, for every prime $p$ and every positive integer $m$, the integer $p^m$ divides the numerator of $s_k-s_j$ (written in lowest terms) for all sufficiently large $k$ and $j$, where
\[
s_k=\sum_{n=0}^k r_n.
\]
:::

::: {.solution}
Define
$$
r_n\coloneqq\frac{n!}{(n!+1)^2}
\qquad(n\ge0).
$$

<1>1. Each $r_n$ is a positive rational number, and
$$
0<r_n\le\frac1{n!}.
$$

::: {.proof}
Positivity is immediate. Since $(n!+1)^2\ge(n!)^2$,
$$
r_n
=\frac{n!}{(n!+1)^2}
\le\frac{n!}{(n!)^2}
=\frac1{n!}.
$$
:::

<1>2. The series
$$
\sum_{n=0}^\infty r_n
$$
converges.

::: {.proof}
By step <1>1,
$$
0\le r_n\le\frac1{n!}.
$$
The series $\sum_{n=0}^\infty1/n!$ converges, so the comparison test
gives convergence of $\sum r_n$.
:::

<1>3. Fix a prime $p$ and an integer $m\ge1$. If
$$
n\ge p^m,
$$
then
$$
p^m\mid n!
\qquad\text{and}\qquad
p\nmid n!+1.
$$

::: {.proof}
For $n\ge p^m$, the factor $p^m$ occurs among
$1,2,\ldots,n$, hence divides $n!$. Consequently
$$
n!+1\equiv1\pmod p,
$$
so $p$ does not divide $n!+1$.
:::

<1>4. If $k>j\ge p^m-1$, then $s_k-s_j$ can be written as
$$
s_k-s_j=\frac{A}{B}
$$
with
$$
p^m\mid A
\qquad\text{and}\qquad
p\nmid B.
$$

::: {.proof}
One has
$$
s_k-s_j
=\sum_{n=j+1}^k\frac{n!}{(n!+1)^2}.
$$
Every index in this sum satisfies $n\ge p^m$. By step <1>3, each
numerator $n!$ is divisible by $p^m$, while every denominator
$(n!+1)^2$ is prime to $p$.

Take
$$
B=\prod_{n=j+1}^k(n!+1)^2.
$$
Then $p\nmid B$. After putting the sum over this common denominator,
each summand in the resulting numerator is $n!$ times a product of
denominators prime to $p$, and hence is divisible by $p^m$. Their sum
$A$ is therefore divisible by $p^m$.
:::

<1>5. The numerator of $s_k-s_j$ in lowest terms is divisible by
$p^m$ whenever $k,j$ are sufficiently large.

::: {.proof}
Assume first that $k>j\ge p^m-1$ and use the representation
$A/B$ from step <1>4. Let
$$
d=\gcd(A,B).
$$
Because $p\nmid B$, one also has $p\nmid d$. Hence division by $d$
cannot remove any factor of $p$ from $A$, so
$$
p^m\mid\frac{A}{d}.
$$
But $(A/d)/(B/d)$ is $s_k-s_j$ in lowest terms.

If $j>k$, apply the same argument to $s_j-s_k$; changing the sign of
the numerator does not affect divisibility. If $j=k$, the difference
is $0$, whose numerator is divisible by every $p^m$.
:::

<1>6. Thus the sequence
$$
\boxed{
r_n=\frac{n!}{(n!+1)^2}
}
$$
has all the required properties.

::: {.proof}
Step <1>2 gives convergence of the series, and step <1>5 gives the
required eventual divisibility for every prime $p$ and every
$m\ge1$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 completes the construction.
:::
:::
