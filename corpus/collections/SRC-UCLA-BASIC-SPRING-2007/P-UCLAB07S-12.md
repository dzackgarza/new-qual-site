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

<1>1. Show that $c_0$ is complete.

<1>2. Is the closed unit ball $\{x\in c_0:\|x\|\le1\}$ compact?
Prove your answer.

<1>3. Is
\[
\left\{x\in c_0:\sum_k k|x_k|\le1\right\}
\]
compact?
Prove your answer.
:::

::: {.solution}
<1>1. Let
\[
(x^{(m)})_{m\ge1}
\]
be a Cauchy sequence in $c_0$ for the supremum norm, where
\[
x^{(m)}
=
\bigl(x_1^{(m)},x_2^{(m)},\ldots\bigr).
\]
Then for each fixed $k$, the real sequence
\[
\bigl(x_k^{(m)}\bigr)_{m\ge1}
\]
is Cauchy.

::: {.proof}
For all $m,\ell$,
\[
\left|
x_k^{(m)}-x_k^{(\ell)}
\right|
\le
\|x^{(m)}-x^{(\ell)}\|_\infty.
\]
Since the right side tends to $0$ as $m,\ell\to\infty$, the coordinate sequence is Cauchy in $\mathbb R$.
:::

<1>2. For each $k$, define
\[
x_k
=
\lim_{m\to\infty}x_k^{(m)}.
\]
Then
\[
x^{(m)}\to x=(x_1,x_2,\ldots)
\]
uniformly in the supremum norm.

::: {.proof}
Let $\varepsilon>0$.
Choose $M$ such that
\[
\|x^{(m)}-x^{(\ell)}\|_\infty<\varepsilon
\]
for all $m,\ell\ge M$.
Fix $m\ge M$ and $k$.
Letting $\ell\to\infty$ in
\[
\left|
x_k^{(m)}-x_k^{(\ell)}
\right|
<\varepsilon
\]
gives
\[
|x_k^{(m)}-x_k|
\le\varepsilon.
\]
Since this holds for every $k$,
\[
\|x^{(m)}-x\|_\infty
\le
\varepsilon.
\]
Thus
\[
x^{(m)}\to x
\]
in the supremum norm.
:::

<1>3. The limit sequence $x$ belongs to $c_0$.

::: {.proof}
Fix $\varepsilon>0$.
By step <1>2, choose $m$ such that
\[
\|x-x^{(m)}\|_\infty<\frac{\varepsilon}{2}.
\]
Since
\[
x^{(m)}\in c_0,
\]
there exists $K$ such that
\[
|x_k^{(m)}|<\frac{\varepsilon}{2}
\]
for all $k\ge K$.
Then
\[
|x_k|
\le
|x_k-x_k^{(m)}|
+
|x_k^{(m)}|
<
\varepsilon
\]
for all $k\ge K$.
Hence
\[
x_k\to0,
\]
so
\[
x\in c_0.
\]
:::

<1>4. Therefore
\[
\boxed{c_0\text{ is complete}.}
\]

::: {.proof}
Every Cauchy sequence in $c_0$ converges in the supremum norm to an element of $c_0$ by steps <1>1--<1>3.
:::

<1>5. For each positive integer $m$, let
\[
e_m
=(0,\ldots,0,1,0,\ldots)
\]
be the sequence with a $1$ in the $m$th coordinate and zeros elsewhere.
Then
\[
\|e_m\|_\infty=1.
\]

::: {.proof}
The largest absolute value of a coordinate of $e_m$ is $1$.
Thus every $e_m$ lies in the closed unit ball of $c_0$.
:::

<1>6. If
\[
m\ne\ell,
\]
then
\[
\|e_m-e_\ell\|_\infty=1.
\]

::: {.proof}
At coordinate $m$,
\[
(e_m-e_\ell)_m=1,
\]
while all coordinates have absolute value at most $1$.
Thus the supremum norm is exactly $1$.
:::

<1>7. The closed unit ball of $c_0$ is not compact.

::: {.proof}
The sequence
\[
(e_m)
\]
lies in the closed unit ball by step <1>5.
By step <1>6, any two distinct terms are distance $1$ apart.
Hence no subsequence is Cauchy, and therefore no subsequence converges.
In a compact metric space every sequence has a convergent subsequence.
Thus
\[
\boxed{
\{x\in c_0:\|x\|_\infty\le1\}
\text{ is not compact}.
}
\]
:::

<1>8. Define
\[
K
=
\left\{
x\in c_0:
\sum_{k=1}^{\infty}
k|x_k|
\le1
\right\}.
\]
Then for every $x\in K$ and every $k$,
\[
|x_k|
\le
\frac1k.
\]

::: {.proof}
Every term in the defining series is nonnegative.
Hence
\[
k|x_k|
\le
\sum_{j=1}^{\infty}j|x_j|
\le1.
\]
Divide by $k$.
:::

<1>9. Let
\[
(x^{(m)})
\]
be any sequence in $K$.
There is a subsequence
\[
\bigl(x^{(m_j)}\bigr)
\]
such that for every fixed coordinate $k$,
\[
x_k^{(m_j)}
\]
converges as
\[
j\to\infty.
\]

::: {.proof}
By step <1>8,
\[
|x_1^{(m)}|\le1
\]
for all $m$.
Bolzano--Weierstrass gives a subsequence along which the first coordinate converges.

From that subsequence, extract a further subsequence along which the second coordinate converges.
Continue inductively.

Take the diagonal subsequence.
Then for every fixed $k$, its $k$th coordinate converges.
:::

<1>10. Let
\[
x_k
=
\lim_{j\to\infty}
x_k^{(m_j)}.
\]
Then
\[
x^{(m_j)}\to x
\]
in the supremum norm.

::: {.proof}
Fix $\varepsilon>0$.
Choose $N$ such that
\[
\frac{2}{N+1}<\frac{\varepsilon}{2}.
\]

By coordinatewise convergence of the finitely many coordinates
\[
1,\ldots,N,
\]
choose $J$ such that for
\[
j\ge J
\]
and
\[
1\le k\le N,
\]
one has
\[
|x_k^{(m_j)}-x_k|
<
\varepsilon.
\]

For
\[
k>N,
\]
step <1>8 gives
\[
|x_k^{(m_j)}|
\le
\frac1k
\le
\frac1{N+1}.
\]
Passing to the coordinatewise limit gives
\[
|x_k|
\le
\frac1k
\le
\frac1{N+1}.
\]
Hence
\[
|x_k^{(m_j)}-x_k|
\le
\frac{2}{N+1}
<
\varepsilon.
\]

Thus for all sufficiently large $j$,
\[
\sup_k
|x_k^{(m_j)}-x_k|
<
\varepsilon.
\]
Therefore
\[
x^{(m_j)}\to x
\]
in the supremum norm.
:::

<1>11. The limit sequence $x$ belongs to $K$.

::: {.proof}
First, step <1>8 passes to the coordinatewise limit:
\[
|x_k|
\le
\frac1k.
\]
Hence
\[
x_k\to0,
\]
so
\[
x\in c_0.
\]

For every positive integer $N$,
\[
\sum_{k=1}^N
k|x_k|
=
\lim_{j\to\infty}
\sum_{k=1}^N
k|x_k^{(m_j)}|
\le1.
\]
The partial sums on the left are nondecreasing in $N$ and bounded above by $1$.
Therefore
\[
\sum_{k=1}^{\infty}k|x_k|
\le1.
\]
Hence
\[
x\in K.
\]
:::

<1>12. The set $K$ is compact.

::: {.proof}
Steps <1>9--<1>11 show that every sequence in $K$ has a subsequence converging in the supremum norm to a point of $K$.
Thus $K$ is sequentially compact.
In metric spaces, sequential compactness is equivalent to compactness.
Therefore
\[
\boxed{K\text{ is compact}.}
\]
:::

<1>13. Q.E.D.

::: {.proof}
Step <1>4 proves part <1>1, step <1>7 answers part <1>2 negatively, and step <1>12 answers part <1>3 affirmatively.
:::
:::
