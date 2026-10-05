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
Problem 7. Let $(f_n)$ be a sequence of real-valued functions on $\mathbb R$.
Assume that there is $B<\infty$ such that
\[
|f_n(x)|\le B
\]
for every $n$ and every $x$.
Prove that there is a subsequence $(f_{n_k})$ such that
\[
\lim_{k\to\infty}f_{n_k}(r)
\]
exists for every rational number $r$.
:::

::: {.solution}
Enumerate the rational numbers as
\[
\mathbb Q=\{r_1,r_2,r_3,\ldots\}.
\]

<1>1. The real sequence
\[
\bigl(f_n(r_1)\bigr)_{n\ge1}
\]
has a convergent subsequence.

::: {.proof}
By hypothesis,
\[
|f_n(r_1)|\le B
\]
for every $n$.
Thus the sequence is bounded in the compact interval
\[
[-B,B].
\]
By Bolzano--Weierstrass, it has a convergent subsequence.
:::

<1>2. Choose an infinite index sequence
\[
n^{(1)}_1<n^{(1)}_2<\cdots
\]
such that
\[
f_{n^{(1)}_k}(r_1)
\]
converges.

::: {.proof}
This is the subsequence supplied by step <1>1, written by its indices.
:::

<1>3. From the subsequence in step <1>2, extract a further subsequence
\[
n^{(2)}_1<n^{(2)}_2<\cdots
\]
such that
\[
f_{n^{(2)}_k}(r_2)
\]
converges.

::: {.proof}
The values
\[
f_{n^{(1)}_k}(r_2)
\]
are again bounded by $B$.
Bolzano--Weierstrass therefore yields a convergent subsequence.
Choose its indices as
\[
n^{(2)}_k.
\]
Because it is a subsequence of the stage-1 sequence, convergence at $r_1$ is preserved.
:::

<1>4. Continuing inductively, construct nested subsequences
\[
\bigl(n^{(j)}_k\bigr)_{k\ge1}
\]
such that for every $j$,
\[
f_{n^{(j)}_k}(r_i)
\]
converges as $k\to\infty$ for each
\[
1\le i\le j.
\]

::: {.proof}
Suppose the stage-$j$ subsequence has been chosen.
The real sequence
\[
f_{n^{(j)}_k}(r_{j+1})
\]
is bounded by $B$.
Apply Bolzano--Weierstrass to extract a convergent subsequence.
Call its indices
\[
n^{(j+1)}_k.
\]
Because it is a subsequence of the stage-$j$ sequence, convergence at
\[
r_1,\ldots,r_j
\]
is retained, and by construction convergence at $r_{j+1}$ is added.
:::

<1>5. Define the diagonal sequence of indices by
\[
\boxed{n_k=n^{(k)}_k}.
\]
Then
\[
n_1<n_2<\cdots.
\]

::: {.proof}
At each stage, the sequence
\[
\bigl(n^{(j+1)}_k\bigr)
\]
is a subsequence of
\[
\bigl(n^{(j)}_k\bigr).
\]
In particular, the $k$th term of the stage-$k$ sequence occurs no earlier than the $k$th term of any previous stage, and the diagonal indices can be chosen strictly increasing.
Equivalently, when carrying out the induction in step <1>4, choose each extracted subsequence with its $k$th term larger than the previously chosen diagonal term.
Thus
\[
n_1<n_2<\cdots.
\]
:::

<1>6. Fix
\[
j\ge1.
\]
For every
\[
k\ge j,
\]
the index $n_k$ belongs to the stage-$j$ subsequence.

::: {.proof}
For $k\ge j$, the stage-$k$ sequence is obtained by repeatedly passing to subsequences starting from stage $j$.
Hence
\[
n_k=n^{(k)}_k
\]
is one of the indices in
\[
\bigl(n^{(j)}_\ell\bigr)_{\ell\ge1}.
\]
Thus the tail of the diagonal sequence is a subsequence of the stage-$j$ sequence.
:::

<1>7. For every rational number
\[
r_j,
\]
the limit
\[
\lim_{k\to\infty}f_{n_k}(r_j)
\]
exists.

::: {.proof}
At stage $j$, the sequence
\[
f_{n^{(j)}_k}(r_j)
\]
was chosen to converge.
By step <1>6, the tail
\[
\bigl(f_{n_k}(r_j)\bigr)_{k\ge j}
\]
is a subsequence of that convergent sequence.
Every subsequence of a convergent sequence converges to the same limit.
Hence
\[
f_{n_k}(r_j)
\]
converges.
:::

<1>8. Therefore there exists a subsequence
\[
\boxed{(f_{n_k})}
\]
such that
\[
\boxed{
\lim_{k\to\infty}f_{n_k}(r)
\text{ exists for every }r\in\mathbb Q.
}
\]

::: {.proof}
Every rational number is equal to
\[
r_j
\]
for some $j$.
Apply step <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required diagonal-subsequence conclusion.
:::
:::
