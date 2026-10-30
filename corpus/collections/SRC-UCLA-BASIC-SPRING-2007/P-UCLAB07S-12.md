---
schema: qual/card@1
id: P-UCLAB07S-12
kind: problem
title: Completeness and compact subsets of c-zero
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Spring 2007.
---
::: {.problem}
Let $c_0$ be the normed space of real sequences $x=(x_1,x_2,\ldots)$ with $x_k\to0$, equipped with the supremum norm.

::: pf

::: pf-step

Show that $c_0$ is complete.

:::

::: pf-step

Is the closed unit ball $\{x\in c_0:\norm{x}\le1\}$ compact?
Prove your answer.

:::

::: pf-step

Is

:::

:::

$$
\left\{x\in c_0:\sum_k k\abs{x_k}\le1\right\}
$$
compact?
Prove your answer.
:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

Let
$$
(x^{(m)})_{m\ge1}
$$
be a Cauchy sequence in $c_0$ for the supremum norm, where
$$
x^{(m)}
=
\bigl(x_1^{(m)},x_2^{(m)},\ldots\bigr).
$$
Then for each fixed $k$, the real sequence
$$
\bigl(x_k^{(m)}\bigr)_{m\ge1}
$$
is Cauchy.

::: pf-proof

For all $m,\ell$,
$$
\abs{
x_k^{(m)}-x_k^{(\ell)}
}
\le
\norm{x^{(m)}-x^{(\ell)}}_\infty.
$$
Since the right side tends to $0$ as $m,\ell\to\infty$, the coordinate sequence is Cauchy in $\RR$.

:::

:::

::: {.pf-step #p2-s2}

For each $k$, define
$$
x_k
=
\lim_{m\to\infty}x_k^{(m)}.
$$
Then
$$
x^{(m)}\to x=(x_1,x_2,\ldots)
$$
uniformly in the supremum norm.

::: pf-proof

Let $\varepsilon>0$.
Choose $M$ such that
$$
\norm{x^{(m)}-x^{(\ell)}}_\infty<\varepsilon
$$
for all $m,\ell\ge M$.
Fix $m\ge M$ and $k$.
Letting $\ell\to\infty$ in
$$
\abs{
x_k^{(m)}-x_k^{(\ell)}
}
<\varepsilon
$$
gives
$$
\abs{x_k^{(m)}-x_k}
\le\varepsilon.
$$
Since this holds for every $k$,
$$
\norm{x^{(m)}-x}_\infty
\le
\varepsilon.
$$
Thus
$$
x^{(m)}\to x
$$
in the supremum norm.

:::

:::

::: {.pf-step #p2-s3}

The limit sequence $x$ belongs to $c_0$.

::: pf-proof

Fix $\varepsilon>0$.
By step [](#p2-s2){.pf-ref}, choose $m$ such that
$$
\norm{x-x^{(m)}}_\infty<\frac{\varepsilon}{2}.
$$
Since
$$
x^{(m)}\in c_0,
$$
there exists $K$ such that
$$
\abs{x_k^{(m)}}<\frac{\varepsilon}{2}
$$
for all $k\ge K$.
Then
$$
\abs{x_k}
\le
\abs{x_k-x_k^{(m)}}
+
\abs{x_k^{(m)}}
<
\varepsilon
$$
for all $k\ge K$.
Hence
$$
x_k\to0,
$$
so
$$
x\in c_0.
$$

:::

:::

::: {.pf-step #p2-s4}

Therefore
$$
\boxed{c_0\text{ is complete}.}
$$

::: pf-proof

Every Cauchy sequence in $c_0$ converges in the supremum norm to an element of $c_0$ by steps [](#p2-s1){.pf-ref}, [](#p2-s2){.pf-ref} and [](#p2-s3){.pf-ref}.

:::

:::

::: {.pf-step #p2-s5}

For each positive integer $m$, let
$$
e_m
=(0,\ldots,0,1,0,\ldots)
$$
be the sequence with a $1$ in the $m$th coordinate and zeros elsewhere.
Then
$$
\norm{e_m}_\infty=1.
$$

::: pf-proof

The largest absolute value of a coordinate of $e_m$ is $1$.
Thus every $e_m$ lies in the closed unit ball of $c_0$.

:::

:::

::: {.pf-step #p2-s6}

If
$$
m\ne\ell,
$$
then
$$
\norm{e_m-e_\ell}_\infty=1.
$$

::: pf-proof

At coordinate $m$,
$$
(e_m-e_\ell)_m=1,
$$
while all coordinates have absolute value at most $1$.
Thus the supremum norm is exactly $1$.

:::

:::

::: {.pf-step #p2-s7}

The closed unit ball of $c_0$ is not compact.

::: pf-proof

The sequence
$$
(e_m)
$$
lies in the closed unit ball by step [](#p2-s5){.pf-ref}.
By step [](#p2-s6){.pf-ref}, any two distinct terms are distance $1$ apart.
Hence no subsequence is Cauchy, and therefore no subsequence converges.
In a compact metric space every sequence has a convergent subsequence.
Thus
$$
\boxed{
\{x\in c_0:\norm{x}_\infty\le1\}
\text{ is not compact}.
}
$$

:::

:::

::: {.pf-step #p2-s8}

Define
$$
K
=
\left\{
x\in c_0:
\sum_{k=1}^{\infty}
k\abs{x_k}
\le1
\right\}.
$$
Then for every $x\in K$ and every $k$,
$$
\abs{x_k}
\le
\frac1k.
$$

::: pf-proof

Every term in the defining series is nonnegative.
Hence
$$
k\abs{x_k}
\le
\sum_{j=1}^{\infty}j\abs{x_j}
\le1.
$$
Divide by $k$.

:::

:::

::: {.pf-step #p2-s9}

Let
$$
(x^{(m)})
$$
be any sequence in $K$.
There is a subsequence
$$
\bigl(x^{(m_j)}\bigr)
$$
such that for every fixed coordinate $k$,
$$
x_k^{(m_j)}
$$
converges as
$$
j\to\infty.
$$

::: pf-proof

By step [](#p2-s8){.pf-ref},
$$
\abs{x_1^{(m)}}\le1
$$
for all $m$.
Bolzano--Weierstrass gives a subsequence along which the first coordinate converges.

From that subsequence, extract a further subsequence along which the second coordinate converges.
Continue inductively.

Take the diagonal subsequence.
Then for every fixed $k$, its $k$th coordinate converges.

:::

:::

::: {.pf-step #p2-s10}

Let
$$
x_k
=
\lim_{j\to\infty}
x_k^{(m_j)}.
$$
Then
$$
x^{(m_j)}\to x
$$
in the supremum norm.

::: pf-proof

Fix $\varepsilon>0$.
Choose $N$ such that
$$
\frac{2}{N+1}<\frac{\varepsilon}{2}.
$$

By coordinatewise convergence of the finitely many coordinates
$$
1,\ldots,N,
$$
choose $J$ such that for
$$
j\ge J
$$
and
$$
1\le k\le N,
$$
one has
$$
\abs{x_k^{(m_j)}-x_k}
<
\varepsilon.
$$

For
$$
k>N,
$$
step [](#p2-s8){.pf-ref} gives
$$
\abs{x_k^{(m_j)}}
\le
\frac1k
\le
\frac1{N+1}.
$$
Passing to the coordinatewise limit gives
$$
\abs{x_k}
\le
\frac1k
\le
\frac1{N+1}.
$$
Hence
$$
\abs{x_k^{(m_j)}-x_k}
\le
\frac{2}{N+1}
<
\varepsilon.
$$

Thus for all sufficiently large $j$,
$$
\sup_k
\abs{x_k^{(m_j)}-x_k}
<
\varepsilon.
$$
Therefore
$$
x^{(m_j)}\to x
$$
in the supremum norm.

:::

:::

::: {.pf-step #p2-s11}

The limit sequence $x$ belongs to $K$.

::: pf-proof

First, step [](#p2-s8){.pf-ref} passes to the coordinatewise limit:
$$
\abs{x_k}
\le
\frac1k.
$$
Hence
$$
x_k\to0,
$$
so
$$
x\in c_0.
$$

For every positive integer $N$,
$$
\sum_{k=1}^N
k\abs{x_k}
=
\lim_{j\to\infty}
\sum_{k=1}^N
k\abs{x_k^{(m_j)}}
\le1.
$$
The partial sums on the left are nondecreasing in $N$ and bounded above by $1$.
Therefore
$$
\sum_{k=1}^{\infty}k\abs{x_k}
\le1.
$$
Hence
$$
x\in K.
$$

:::

:::

::: {.pf-step #p2-s12}

The set $K$ is compact.

::: pf-proof

Steps [](#p2-s9){.pf-ref}, [](#p2-s10){.pf-ref} and [](#p2-s11){.pf-ref} show that every sequence in $K$ has a subsequence converging in the supremum norm to a point of $K$.
Thus $K$ is sequentially compact.
In metric spaces, sequential compactness is equivalent to compactness.
Therefore
$$
\boxed{K\text{ is compact}.}
$$

:::

:::

::: pf-qed

Step [](#p2-s4){.pf-ref} proves part step [](#p2-s1){.pf-ref}, step [](#p2-s7){.pf-ref} answers part step [](#p2-s2){.pf-ref} negatively, and step [](#p2-s12){.pf-ref} answers part step [](#p2-s3){.pf-ref} affirmatively.

:::

:::

:::
