---
schema: qual/card@1
id: P-SERIES-A2-02
kind: problem
title: $\limsup$ and $\liminf$ as extreme subsequential limits
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\{a_n\}$ be a sequence of real numbers, and let
\[
S=\{x\in\mathbb R:\text{there is a subsequence }a_{n_k}\to x\}.
\]

(a) Show that $L=\limsup a_n$ if and only if $L=\sup S$.

(b) Formulate and prove the analogous statement for $\liminf a_n$.
:::

::: {.solution}
The unrestricted statement in part (a) is false when
\[
\limsup a_n=+\infty.
\]
For example, if
\[
a_n=n,
\]
then $S=\varnothing$, because no subsequence converges to a finite real
number, while
\[
\limsup a_n=+\infty.
\]
The retained source proof implicitly assumes that the limsup is finite. Under
that intended hypothesis, the theorem is correct.

<1>1. Assume
\[
L
\coloneqq
\limsup_{n\to\infty}a_n
\in\mathbb R.
\]
Then there exists a subsequence
\[
a_{n_k}\to L.
\]

::: {.proof}
By the definition
\[
L
=
\lim_{N\to\infty}
\sup_{n\ge N}a_n,
\]
for every $k\ge1$ and every index $N$ there exists some $n\ge N$ such that
\[
a_n>L-\frac1k.
\]

Choose $n_1$ with
\[
a_{n_1}>L-1.
\]
Inductively, after choosing
\[
n_1<\cdots<n_{k-1},
\]
choose
\[
n_k>n_{k-1}
\]
with
\[
a_{n_k}>L-\frac1k.
\]

Fix $\varepsilon>0$. Since $L$ is the limsup, there is $N$ such that
\[
n\ge N
\quad\Longrightarrow\quad
a_n<L+\varepsilon.
\]
For all sufficiently large $k$,
\[
n_k\ge N
\qquad\text{and}\qquad
\frac1k<\varepsilon.
\]
Hence
\[
L-\varepsilon
<
a_{n_k}
<
L+\varepsilon.
\]
Thus
\[
a_{n_k}\to L.
\]
:::

<1>2. Under the hypothesis of step <1>1,
\[
L\in S.
\]

::: {.proof}
Step <1>1 constructs a subsequence converging to $L$, which is exactly the
definition of membership in $S$.
:::

<1>3. Every $x\in S$ satisfies
\[
x\le L.
\]

::: {.proof}
Let
\[
x\in S.
\]
Choose a subsequence
\[
a_{n_k}\to x.
\]

Fix $\varepsilon>0$. By the definition of limsup, there is $N$ such that
\[
n\ge N
\quad\Longrightarrow\quad
a_n<L+\varepsilon.
\]
For sufficiently large $k$ one has
\[
n_k\ge N,
\]
so
\[
a_{n_k}<L+\varepsilon.
\]
Passing to the limit gives
\[
x\le L+\varepsilon.
\]
Since $\varepsilon>0$ was arbitrary,
\[
x\le L.
\]
:::

<1>4. If
\[
L=\limsup a_n\in\mathbb R,
\]
then
\[
\boxed{
L=\max S=\sup S.
}
\]

::: {.proof}
Step <1>2 gives
\[
L\in S,
\]
so
\[
L\le\sup S.
\]
Step <1>3 gives
\[
x\le L
\qquad
(x\in S),
\]
so
\[
\sup S\le L.
\]
Hence
\[
\sup S=L,
\]
and because $L\in S$, the supremum is attained.
:::

<1>5. Conversely, suppose
\[
S\ne\varnothing
\]
and
\[
L=\sup S\in\mathbb R.
\]
If $L\in S$ and every term of the sequence is eventually at most
\[
L+\varepsilon
\]
for each $\varepsilon>0$, then
\[
\limsup a_n=L.
\]

::: {.proof}
The eventual upper bound gives
\[
\limsup a_n\le L.
\]
Because
\[
L\in S,
\]
there is a subsequence converging to $L$. Every subsequential limit is bounded
above by the limsup, so
\[
L\le\limsup a_n.
\]
Therefore equality holds.
:::

<1>6. In the intended bounded-sequence setting, the condition
\[
L=\sup S
\]
automatically yields
\[
L\in S
\]
and
\[
\limsup a_n=L.
\]

::: {.proof}
Assume $(a_n)$ is bounded. Then every subsequence has a convergent
subsubsequence by Bolzano--Weierstrass, so the set $S$ of subsequential
limits is nonempty and compact.

Hence
\[
L=\sup S
\]
belongs to $S$.

Suppose, for contradiction, that for some $\varepsilon>0$ there are
infinitely many indices $n$ with
\[
a_n>L+\varepsilon.
\]
Choose a subsequence consisting of such terms. Boundedness gives a convergent
subsubsequence
\[
a_{n_{k_j}}\to x.
\]
Then
\[
x\ge L+\varepsilon,
\]
so
\[
x\in S
\]
and
\[
x>L=\sup S,
\]
a contradiction. Thus the sequence is eventually bounded above by
$L+\varepsilon$ for every $\varepsilon>0$.

Apply step <1>5.
:::

<1>7. Therefore, for a bounded real sequence,
\[
\boxed{
\limsup a_n=\max S=\sup S.
}
\]

::: {.proof}
The forward implication is step <1>4. The reverse implication is step <1>6.
:::

<1>8. The analogous statement for the lower limit is
\[
\boxed{
\liminf a_n=\min S=\inf S
}
\]
for every bounded real sequence.

::: {.proof}
Apply step <1>7 to the sequence
\[
b_n=-a_n.
\]
Its set of subsequential limits is
\[
S_b
=
\{-x:x\in S\}.
\]
Also,
\[
\limsup b_n
=
-\liminf a_n.
\]
Therefore
\[
-\liminf a_n
=
\sup S_b
=
\sup\{-x:x\in S\}
=
-\inf S.
\]
Multiplying by $-1$ gives
\[
\liminf a_n=\inf S.
\]
Since $S$ is compact, its infimum is attained, so it is also
\[
\min S.
\]
:::

<1>9. If
\[
\liminf a_n\in\mathbb R
\]
but the sequence is not assumed bounded above, the forward implication
\[
\liminf a_n=\min S
\]
still holds by the same direct argument as steps <1>1--<1>4.

::: {.proof}
Apply those steps to
\[
-a_n.
\]
A finite liminf of $a_n$ is a finite limsup of $-a_n$, so the same
subsequence construction and extremality argument apply.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>7 proves the intended bounded-sequence form of part (a), and step
<1>8 proves the corresponding statement for $\liminf$. The opening
counterexample records why the unrestricted literal statement requires the
missing finiteness/boundedness hypothesis.
:::
:::
