---
schema: qual/card@1
id: P-WESRA14-5
kind: problem
title: 'Subsequence and finite-measure converse for the source’s convergence-in-measure definition'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md. The source uses the name “convergence in measure” for the displayed exceptional-set-uniform definition (usually called almost uniform convergence). The card preserves the source definition rather than silently replacing it with the standard one.
---

::: {.problem}
The source defines that measurable $f_n$ converge *in measure* to $f$ if for every $\varepsilon>0$ there are $N$ and a measurable $B$ with $\mu(B)<\varepsilon$ such that
\[
|f_n(x)-f(x)|<\varepsilon
\]
for every $n\ge N$ and every $x\notin B$.

(a) Under this definition, prove that some subsequence converges to $f$ almost everywhere.

(b) If $\mu(X)<\infty$ and $f_n\to f$ almost everywhere, prove convergence in the displayed source sense.
:::

The displayed source definition is the usual notion of **almost uniform
convergence**, not the standard definition of convergence in measure.
The proof below follows the source's displayed definition literally.

::: pf

::: pf-step

Assume the displayed source convergence.
For each
\[
k\ge1,
\]
choose an integer
\[
N_k
\]
and a measurable set
\[
B_k
\]
such that
\[
\mu(B_k)<2^{-k}
\]
and
\[
|f_n(x)-f(x)|
<
2^{-k}
\]
for every
\[
n\ge N_k
\]
and every
\[
x\notin B_k.
\]


::: pf-proof

Apply the source definition with
\[
\varepsilon=2^{-k}.
\]

:::

:::

::: pf-step

For
\[
m\ge1,
\]
define
\[
E_m
\coloneqq
\bigcup_{k=m}^{\infty}B_k.
\]
Then
\[
\mu(E_m)
<
2^{1-m}.
\]


::: pf-proof

By countable subadditivity,
\[
\begin{aligned}
\mu(E_m)
&\le
\sum_{k=m}^{\infty}
\mu(B_k)\\
&<
\sum_{k=m}^{\infty}
2^{-k}\\
&=
2^{1-m}.
\end{aligned}
\]

:::

:::

::: pf-step

Let
\[
E
\coloneqq
\bigcap_{m=1}^{\infty}E_m.
\]
Then
\[
\mu(E)=0.
\]


::: pf-proof

The sets
\[
E_1\supseteq E_2\supseteq\cdots
\]
decrease.
Also
\[
\mu(E_1)<2<\infty.
\]
By continuity from above,
\[
\mu(E)
=
\lim_{m\to\infty}
\mu(E_m).
\]
Step <1>2 gives
\[
0
\le
\mu(E_m)
<
2^{1-m}
\longrightarrow
0.
\]
Therefore
\[
\mu(E)=0.
\]

:::

:::

::: pf-step

If
\[
x\notin E,
\]
then there exists
\[
m
\]
such that
\[
x\notin B_k
\]
for every
\[
k\ge m.
\]


::: pf-proof

Since
\[
x\notin
\bigcap_{m=1}^{\infty}E_m,
\]
there exists some
\[
m
\]
with
\[
x\notin E_m.
\]
But
\[
E_m
=
\bigcup_{k=m}^{\infty}B_k.
\]
Hence
\[
x\notin B_k
\]
for all
\[
k\ge m.
\]

:::

:::

::: pf-step

For every
\[
x\notin E,
\]
the full sequence satisfies
\[
f_n(x)\to f(x).
\]


::: pf-proof

Fix
\[
x\notin E
\]
and let $m$ be as in step <1>4.

Let
\[
\eta>0.
\]
Choose
\[
k\ge m
\]
such that
\[
2^{-k}<\eta.
\]
Since
\[
x\notin B_k,
\]
step <1>1 gives
\[
|f_n(x)-f(x)|
<
2^{-k}
<
\eta
\]
for every
\[
n\ge N_k.
\]
This is exactly
\[
f_n(x)\to f(x).
\]

:::

:::

::: pf-step

Therefore the source convergence implies almost-everywhere
convergence of the full sequence, and in particular some subsequence
converges almost everywhere.


::: pf-proof

By step <1>3,
\[
\mu(E)=0.
\]
By step <1>5,
\[
f_n(x)\to f(x)
\]
for every
\[
x\in X\setminus E.
\]
Thus the whole sequence converges almost everywhere.
Any subsequence therefore also converges almost everywhere.

:::

:::

::: pf-step

Now assume
\[
\mu(X)<\infty
\]
and
\[
f_n(x)\to f(x)
\]
for almost every
\[
x\in X.
\]
Fix
\[
\varepsilon>0.
\]


::: pf-proof

These are the hypotheses of Egorov's theorem.

:::

:::

::: pf-step

By Egorov's theorem, there exists a measurable set
\[
B\subseteq X
\]
such that
\[
\mu(B)<\varepsilon
\]
and
\[
f_n\to f
\]
uniformly on
\[
X\setminus B.
\]


::: pf-proof

Egorov's theorem states that on a finite-measure space, almost-everywhere
convergence of measurable functions is almost uniform.
Apply it with exceptional-set measure bound
\[
\varepsilon.
\]

:::

:::

::: pf-step

Uniform convergence on
\[
X\setminus B
\]
gives an integer
\[
N
\]
such that
\[
|f_n(x)-f(x)|
<
\varepsilon
\]
for every
\[
n\ge N
\]
and every
\[
x\in X\setminus B.
\]


::: pf-proof

This is the definition of uniform convergence, using the tolerance
\[
\varepsilon.
\]

:::

:::

::: pf-step

Hence
\[
f_n
\]
converges to $f$ in the displayed source sense.


::: pf-proof

For the given
\[
\varepsilon>0,
\]
step <1>8 supplies a measurable exceptional set
\[
B
\]
with
\[
\mu(B)<\varepsilon,
\]
and step <1>9 supplies
\[
N
\]
such that the required estimate holds for all
\[
n\ge N
\]
outside $B$.
This is exactly the source's displayed definition.

:::

:::

::: pf-qed

Step <1>6 proves part (a), in the stronger form of convergence of the full
sequence almost everywhere.
Steps <1>7--<1>10 prove part (b) by Egorov's theorem.

:::

:::
