---
schema: qual/card@1
id: P-UCLAB14S-10
kind: problem
title: Arzelà–Ascoli from boundedness and equicontinuity
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
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Let $F$ be a set of continuous real-valued functions on $[0,1]$.
Assume that

(i) $F$ is uniformly bounded: there is $M<\infty$ such that $\abs{f(x)}\leq M$ for all $f\in F$ and all $x\in[0,1]$; and

(ii) $F$ is equicontinuous: for every $\varepsilon>0$ there is $\delta>0$ such that for all $f\in F$ and $x,y\in[0,1]$,
$$
\abs{x-y}<\delta\implies \abs{f(x)-f(y)}<\varepsilon.
$$

Prove that every sequence from $F$ has a subsequence that converges uniformly on $[0,1]$.
:::

::: {.solution}

Let $(f_n)$ be an arbitrary sequence in $F$. The proof first obtains convergence on a countable dense set and then upgrades it to uniform convergence using equicontinuity.

::: pf

::: pf-step

Enumerate the rational points of $[0,1]$ as
$$
\QQ\cap[0,1]=\{q_1,q_2,q_3,\ldots\}.
$$


::: pf-proof

The rational numbers are countable, and $\QQ\cap[0,1]$ is dense in $[0,1]$.

:::

:::

::: {.pf-step #s1-2}

There is a subsequence $(f_{n_j})$ such that, for every $m\geq1$, the scalar sequence
$$
f_{n_j}(q_m)
$$
converges as $j\to\infty$.


::: pf-proof

Uniform boundedness gives
$$
\abs{f_n(q_1)}\leq M
$$
for all $n$, so Bolzano--Weierstrass gives a subsequence converging at $q_1$. From that subsequence choose a further subsequence converging at $q_2$, and continue inductively. Let $(f_{n_j})$ be the diagonal subsequence, whose $j$th term is the $j$th term of the $j$th nested subsequence. For fixed $m$, all sufficiently late diagonal terms belong to the subsequence chosen at stage $m$, so their values at $q_m$ converge.

:::

:::

::: {.pf-step #s1-3}

Fix $\varepsilon>0$. By equicontinuity, choose $\delta>0$ such that for every $f\in F$,
$$
\abs{x-y}<\delta
\quad\Longrightarrow\quad
\abs{f(x)-f(y)}<\varepsilon/3.
$$


::: pf-proof

Apply hypothesis (ii) with $\varepsilon/3$ in place of $\varepsilon$.

:::

:::

::: {.pf-step #s1-4}

Choose finitely many rational points
$$
q_{m_1},\ldots,q_{m_N}
$$
such that every $x\in[0,1]$ lies within distance $\delta$ of at least one of them.


::: pf-proof

The intervals
$$
(q-\delta,q+\delta),
\qquad q\in\QQ\cap[0,1],
$$
form an open cover of the compact interval $[0,1]$. Compactness gives a finite subcover, yielding the stated rational points.

:::

:::

::: {.pf-step #s1-5}

There exists $J$ such that whenever $j,k\geq J$,
$$
\abs{f_{n_j}(q_{m_i})-f_{n_k}(q_{m_i})}<\varepsilon/3
\qquad(i=1,\ldots,N).
$$


::: pf-proof

For each of the finitely many points $q_{m_i}$, step [](#s1-2){.pf-ref} says the scalar sequence $f_{n_j}(q_{m_i})$ converges and hence is Cauchy. Choose a Cauchy threshold $J_i$ for error $\varepsilon/3$, and take
$$
J=\max_iJ_i.
$$

:::

:::

::: {.pf-step #s1-6}

For every $j,k\geq J$ and every $x\in[0,1]$,
$$
\abs{f_{n_j}(x)-f_{n_k}(x)}<\varepsilon.
$$


::: pf-proof

Choose $q_{m_i}$ with $\abs{x-q_{m_i}}<\delta$ using step [](#s1-4){.pf-ref}. Then
$$
\begin{aligned}
\abs{f_{n_j}(x)-f_{n_k}(x)}
&\leq \abs{f_{n_j}(x)-f_{n_j}(q_{m_i})}\\
&\quad+\abs{f_{n_j}(q_{m_i})-f_{n_k}(q_{m_i})}\\
&\quad+\abs{f_{n_k}(q_{m_i})-f_{n_k}(x)}.
\end{aligned}
$$
The first and third terms are $<\varepsilon/3$ by step [](#s1-3){.pf-ref}, and the middle term is $<\varepsilon/3$ by step [](#s1-5){.pf-ref}. Their sum is $<\varepsilon$.

:::

:::

::: {.pf-step #s1-7}

Thus $(f_{n_j})$ is Cauchy in the supremum norm on $C([0,1])$.


::: pf-proof

Step [](#s1-6){.pf-ref} says precisely that for every $\varepsilon>0$ there is $J$ such that
$$
\norm{f_{n_j}-f_{n_k}}_\infty<\varepsilon
$$
whenever $j,k\geq J$.

:::

:::

::: {.pf-step #s1-8}

Since $C([0,1])$ is complete in the supremum norm, there is a continuous function $f$ such that
$$
\norm{f_{n_j}-f}_\infty\longrightarrow0.
$$


::: pf-proof

The space $C([0,1])$ with the supremum norm is a Banach space. Therefore the Cauchy sequence from step [](#s1-7){.pf-ref} converges in that norm to some element $f\in C([0,1])$. Convergence in the supremum norm is exactly uniform convergence.

:::

:::

::: {.pf-step #s1-9}

Hence every sequence in $F$ has a uniformly convergent subsequence.


::: pf-proof

The original sequence $(f_n)$ was arbitrary, and steps [](#s1-2){.pf-ref} through [](#s1-8){.pf-ref} construct the required subsequence.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the desired Arzela--Ascoli conclusion.

:::

:::

:::
