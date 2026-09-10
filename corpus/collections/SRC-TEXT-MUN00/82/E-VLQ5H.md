---
schema: qual/card@1
id: E-VLQ5H
kind: problem
title: The uncountable fundamental group of the infinite earring
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise}

Let $X$ be the infinite earring (see Example 1 of §80). Show that $X$ is a compact Hausdorff space with a countable basis whose fundamental group is uncountable.
[Hint: Let $r_n: X \to C_n$ be a retraction. Given a sequence $a_1, a_2, \ldots$ of zeros and ones, show there exists a loop $f$ in $X$ such that, for each $n$, the element $(r_n)_*[f]$ is trivial if and only if $a_n = 0$.]
:::

::: {.solution}
Let the infinite earring be
\[
X=\bigcup_{n\ge1}C_n,
\]
where the circles \(C_n\) are tangent at the common point \(p\) and have radii tending to \(0\).

The set \(X\) is bounded. It is closed in \(\mathbb R^2\): away from \(p\), only finitely many circles meet a sufficiently small neighborhood, and each is closed; the only possible accumulation point of the family is \(p\in X\). Hence \(X\) is compact. As a subspace of \(\mathbb R^2\), it is Hausdorff and second countable.

For each \(n\), let
\[
r_n:X\to C_n
\]
be the retraction equal to the identity on \(C_n\) and sending every other circle to \(p\). It is continuous: continuity is obvious away from \(p\), and near \(p\) all sufficiently small circles lie in any prescribed neighborhood of \(p\).

Now let \(a=(a_1,a_2,\ldots)\in\{0,1\}^{\mathbb N}\). Divide \([0,1]\) into intervals
\[
I_n=[1-2^{-(n-1)},\,1-2^{-n}]
\]
accumulating at \(1\). On \(I_n\), let \(f_a\) traverse \(C_n\) once if \(a_n=1\), and stay at \(p\) if \(a_n=0\); set \(f_a(1)=p\). This defines a continuous loop because \(\operatorname{diam}(C_n)	o0\).

For each \(n\),
\[
(r_n)_*[f_a]=
\begin{cases}
0,&a_n=0,\\
1\in\pi_1(C_n,p)\cong\mathbb Z,&a_n=1.
\end{cases}
\]
Therefore if \(a\ne b\), choose \(n\) with \(a_n\ne b_n\). Then
\[
(r_n)_*[f_a]\ne(r_n)_*[f_b],
\]
so \([f_a]\ne[f_b]\) in \(\pi_1(X,p)\). Thus
\[
\{0,1\}^{\mathbb N}\hookrightarrow\pi_1(X,p).
\]
The left side is uncountable, hence \(\pi_1(X,p)\) is uncountable.
:::
