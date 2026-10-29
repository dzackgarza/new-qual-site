---
schema: qual/card@1
id: P-UCLAB10S-07
kind: problem
title: A bounded sequence of functions converges on the rationals along a subsequence
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
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 7. Let $(f_n)$ be a sequence of real-valued functions on $\RR$.
Assume that there is $B<\infty$ such that
$$
|f_n(x)|\le B
$$
for every $n$ and every $x$.
Prove that there is a subsequence $(f_{n_k})$ such that
$$
\lim_{k\to\infty}f_{n_k}(r)
$$
exists for every rational number $r$.
:::

::: {.solution}

Enumerate the rational numbers as
$$
\QQ=\{r_1,r_2,r_3,\ldots\}.
$$

::: pf

::: {.pf-step #s1-1}

The real sequence
$$
\bigl(f_n(r_1)\bigr)_{n\ge1}
$$
has a convergent subsequence.


::: pf-proof

By hypothesis,
$$
|f_n(r_1)|\le B
$$
for every $n$.
Thus the sequence is bounded in the compact interval
$$
[-B,B].
$$
By Bolzano--Weierstrass, it has a convergent subsequence.

:::

:::

::: {.pf-step #s1-2}

Choose an infinite index sequence
$$
n^{(1)}_1<n^{(1)}_2<\cdots
$$
such that
$$
f_{n^{(1)}_k}(r_1)
$$
converges.


::: pf-proof

This is the subsequence supplied by step [](#s1-1){.pf-ref}, written by its indices.

:::

:::

::: pf-step

From the subsequence in step [](#s1-2){.pf-ref}, extract a further subsequence
$$
n^{(2)}_1<n^{(2)}_2<\cdots
$$
such that
$$
f_{n^{(2)}_k}(r_2)
$$
converges.


::: pf-proof

The values
$$
f_{n^{(1)}_k}(r_2)
$$
are again bounded by $B$.
Bolzano--Weierstrass therefore yields a convergent subsequence.
Choose its indices as
$$
n^{(2)}_k.
$$
Because it is a subsequence of the stage-1 sequence, convergence at $r_1$ is preserved.

:::

:::

::: {.pf-step #s1-4}

Continuing inductively, construct nested subsequences
$$
\bigl(n^{(j)}_k\bigr)_{k\ge1}
$$
such that for every $j$,
$$
f_{n^{(j)}_k}(r_i)
$$
converges as $k\to\infty$ for each
$$
1\le i\le j.
$$


::: pf-proof

Suppose the stage-$j$ subsequence has been chosen.
The real sequence
$$
f_{n^{(j)}_k}(r_{j+1})
$$
is bounded by $B$.
Apply Bolzano--Weierstrass to extract a convergent subsequence.
Call its indices
$$
n^{(j+1)}_k.
$$
Because it is a subsequence of the stage-$j$ sequence, convergence at
$$
r_1,\ldots,r_j
$$
is retained, and by construction convergence at $r_{j+1}$ is added.

:::

:::

::: pf-step

Define the diagonal sequence of indices by
$$
\boxed{n_k=n^{(k)}_k}.
$$
Then
$$
n_1<n_2<\cdots.
$$


::: pf-proof

At each stage, the sequence
$$
\bigl(n^{(j+1)}_k\bigr)
$$
is a subsequence of
$$
\bigl(n^{(j)}_k\bigr).
$$
In particular, the $k$th term of the stage-$k$ sequence occurs no earlier than the $k$th term of any previous stage, and the diagonal indices can be chosen strictly increasing.
Equivalently, when carrying out the induction in step [](#s1-4){.pf-ref}, choose each extracted subsequence with its $k$th term larger than the previously chosen diagonal term.
Thus
$$
n_1<n_2<\cdots.
$$

:::

:::

::: {.pf-step #s1-6}

Fix
$$
j\ge1.
$$
For every
$$
k\ge j,
$$
the index $n_k$ belongs to the stage-$j$ subsequence.


::: pf-proof

For $k\ge j$, the stage-$k$ sequence is obtained by repeatedly passing to subsequences starting from stage $j$.
Hence
$$
n_k=n^{(k)}_k
$$
is one of the indices in
$$
\bigl(n^{(j)}_\ell\bigr)_{\ell\ge1}.
$$
Thus the tail of the diagonal sequence is a subsequence of the stage-$j$ sequence.

:::

:::

::: {.pf-step #s1-7}

For every rational number
$$
r_j,
$$
the limit
$$
\lim_{k\to\infty}f_{n_k}(r_j)
$$
exists.


::: pf-proof

At stage $j$, the sequence
$$
f_{n^{(j)}_k}(r_j)
$$
was chosen to converge.
By step [](#s1-6){.pf-ref}, the tail
$$
\bigl(f_{n_k}(r_j)\bigr)_{k\ge j}
$$
is a subsequence of that convergent sequence.
Every subsequence of a convergent sequence converges to the same limit.
Hence
$$
f_{n_k}(r_j)
$$
converges.

:::

:::

::: {.pf-step #s1-8}

Therefore there exists a subsequence
$$
\boxed{(f_{n_k})}
$$
such that
$$
\boxed{
\lim_{k\to\infty}f_{n_k}(r)
\text{ exists for every }r\in\QQ.
}
$$


::: pf-proof

Every rational number is equal to
$$
r_j
$$
for some $j$.
Apply step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required diagonal-subsequence conclusion.

:::

:::

:::
