---
schema: qual/card@1
id: P-RAF25F
kind: problem
title: "Separability of l^2 and sequential compactness of uncountable subsets"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Separability
  - Sequential Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the official UCSD Fall 2025 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Consider the Hilbert space $\ell^2(\mathbb{N})$ with the usual norm $\|f\|_2 = (\sum_{n \in \mathbb{N}} |f(n)|^2)^{1/2}$.

(1) Prove that $\ell^2(\mathbb{N})$ is separable, i.e., contains a countable dense subset.

(2) Let $S \subset \ell^2(\mathbb{N})$ be an uncountable set.
Prove that $S$ contains a convergent sequence which consists of pairwise distinct elements of $S$.

Hint: Use (1) to first prove that for every $\epsilon > 0$, there exists $\eta \in \ell^2(\mathbb{N})$ such that the set $\{\xi \in S : \|\xi - \eta\|_2 < \epsilon\}$ is uncountable.
:::

::: solution
<1>1. Construct a countable dense subset of $\ell^2(\mathbb N)$.
::: proof
Let $D$ be the set of all finitely supported sequences whose real and imaginary parts are rational numbers. Then $D$ is countable.

Fix $x=(x_n)\in\ell^2$ and $\varepsilon>0$. Choose $N$ so large that
\[
\sum_{n>N}|x_n|^2<\frac{\varepsilon^2}{4}.
\]
Approximate each of the finitely many coordinates $x_1,\dots,x_N$ by complex rational numbers $q_1,\dots,q_N$ so closely that
\[
\sum_{n=1}^N|x_n-q_n|^2<\frac{\varepsilon^2}{4}.
\]
Set
\[
q=(q_1,\dots,q_N,0,0,\dots)\in D.
\]
Then
\[
\|x-q\|_2^2<\frac{\varepsilon^2}{2}<\varepsilon^2.
\]
Thus $D$ is dense, and $\ell^2(\mathbb N)$ is separable.
:::

<1>2. Every uncountable subset has an uncountable part inside some arbitrarily small ball.
::: proof
Let $A\subset\ell^2$ be uncountable and let $\varepsilon>0$. Since $D$ is dense,
\[
\ell^2
=\bigcup_{q\in D}B(q,\varepsilon).
\]
If every set
\[
A\cap B(q,\varepsilon)
\]
were countable, then $A$ would be a countable union of countable sets and hence countable, a contradiction. Therefore for some $q\in D$,
\[
A\cap B(q,\varepsilon)
\]
is uncountable.
:::

<1>3. Build nested uncountable sets of shrinking diameter.
::: proof
Set $S_0=S$. Recursively, having chosen an uncountable set $S_{n-1}$, apply Step 2 with
\[
\varepsilon_n:=2^{-n}
\]
to obtain a ball $B(\eta_n,2^{-n})$ such that
\[
S_n:=S_{n-1}\cap B(\eta_n,2^{-n})
\]
is uncountable.

Then
\[
S_0\supset S_1\supset S_2\supset\cdots
\]
and
\[
\operatorname{diam}(S_n)\le2^{1-n}.
\]
:::

<1>4. Choose a pairwise-distinct convergent sequence from $S$.
::: proof
Choose recursively
\[
x_n\in S_n
\]
so that the $x_n$ are pairwise distinct. This is possible because every $S_n$ is uncountable.

If $m\ge n$, then
\[
x_m\in S_m\subset S_n
\qquad\text{and}\qquad
x_n\in S_n,
\]
so
\[
\|x_m-x_n\|_2
\le\operatorname{diam}(S_n)
\le2^{1-n}.
\]
Hence $(x_n)$ is Cauchy. Since $\ell^2$ is complete, there exists $x\in\ell^2$ such that
\[
x_n\to x.
\]
Thus $S$ contains a convergent sequence of pairwise distinct elements.
:::
:::
