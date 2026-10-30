---
schema: qual/card@1
id: P-UCLARA14S-06
kind: problem
title: Hamel spanning and weakly null unit vectors in Hilbert space
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Weak Convergence
  - Baire Category
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
Let $H$ be a Hilbert space and $(a_n)$ a sequence with $\norm{a_n}=1$ for every $n$.

(a) Show that if $(a_n)$ spans $H$ linearly, then $H$ is finite-dimensional.

(b) Show that if
$$
\langle a_n,\xi\rangle\to0\qquad\text{for every }\xi\in H,
$$
then $0$ belongs to the closed convex hull of $\{a_n:n\ge1\}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For each $N\ge1$, let
$$
S_N
\coloneqq
\operatorname{span}\{a_1,\dots,a_N\}.
$$
If $H$ is infinite dimensional, then every $S_N$ is closed and nowhere dense in $H$.


::: pf-proof

Each $S_N$ is finite dimensional, hence closed. If some $S_N$ had nonempty interior, then because $S_N$ is a linear subspace it would contain a ball about $0$. Scalar dilation would then imply that $S_N$ contains every vector of $H$, so
$$
S_N=H.
$$
That would make $H$ finite dimensional, contrary to the assumption. Thus every $S_N$ has empty interior; being closed, it is nowhere dense.

:::

:::

::: {.pf-step #s1-2}

If $(a_n)$ spans $H$ linearly, then
$$
H
=
\bigcup_{N=1}^\infty S_N.
$$


::: pf-proof

Every vector in the algebraic span of the sequence is a finite linear combination of the $a_n$, hence belongs to $S_N$ for some sufficiently large $N$. The hypothesis says that this algebraic span equals $H$.

:::

:::

::: {.pf-step #s1-3}

If $(a_n)$ spans $H$ linearly, then
$$
\boxed{H\text{ is finite dimensional}.}
$$


::: pf-proof

Suppose $H$ were infinite dimensional. By step [](#s1-1){.pf-ref}, each $S_N$ would be nowhere dense, while step [](#s1-2){.pf-ref} would write the complete metric space $H$ as a countable union of nowhere dense sets. This contradicts the Baire category theorem.

:::

:::

::: pf-step

Assume now that
$$
\langle a_n,\xi\rangle\longrightarrow0
\qquad
(\xi\in H).
$$
Fix $\varepsilon>0$. There exist an integer $r\ge1$ and indices
$$
n_1<n_2<\cdots<n_r
$$
such that
$$
\frac1r<\frac{\varepsilon^2}{2}
$$
and
$$
\abs{\langle a_{n_i},a_{n_j}\rangle}
<
\frac{\varepsilon^2}{2}
\qquad
(i\ne j).
$$


::: pf-proof

Choose $r$ so large that $1/r<\varepsilon^2/2$. Set
$$
n_1=1.
$$
Suppose $n_1<\cdots<n_k$ have been chosen. For each fixed $j\le k$, the weak convergence hypothesis applied to
$$
\xi=a_{n_j}
$$
gives
$$
\langle a_n,a_{n_j}\rangle\to0.
$$
Since there are only finitely many previous vectors, choose $n_{k+1}>n_k$ sufficiently large that
$$
\abs{\langle a_{n_{k+1}},a_{n_j}\rangle}
<
\frac{\varepsilon^2}{2}
$$
for every $j\le k$. Continue until $r$ indices have been selected.

:::

:::

::: {.pf-step #s1-5}

The convex combination
$$
c
\coloneqq
\frac1r
\sum_{j=1}^r a_{n_j}
$$
satisfies
$$
\norm{c}<\varepsilon.
$$


::: pf-proof

Using $\norm{a_{n_j}}=1$,
$$
\begin{aligned}
\norm{c}^2
&=
\frac1{r^2}
\norm{
\sum_{j=1}^r a_{n_j}
}^2\\
&=
\frac1{r^2}
\left(
r
+
2\operatorname{Re}
\sum_{1\le i<j\le r}
\langle a_{n_i},a_{n_j}\rangle
\right)\\
&\le
\frac1r
+
\frac{2}{r^2}
\binom r2
\frac{\varepsilon^2}{2}\\
&<
\frac{\varepsilon^2}{2}
+
\frac{r-1}{r}\frac{\varepsilon^2}{2}\\
&<
\varepsilon^2.
\end{aligned}
$$
Hence $\norm{c}<\varepsilon$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
0\in
\overline{\operatorname{conv}}
\{a_n:n\ge1\}
}.
$$


::: pf-proof

For every $\varepsilon>0$, step [](#s1-5){.pf-ref} produces a convex combination of the $a_n$ lying in the open ball $B(0,\varepsilon)$. Thus every neighborhood of $0$ meets the convex hull, which is exactly the assertion that $0$ belongs to its closure.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-6){.pf-ref} proves part (b).

:::

:::

:::
