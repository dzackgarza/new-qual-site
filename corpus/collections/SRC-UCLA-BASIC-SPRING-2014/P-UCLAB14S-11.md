---
schema: qual/card@1
id: P-UCLAB14S-11
kind: problem
title: Sequential compactness in $C[0,1]$ implies uniform boundedness and equicontinuity
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
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Problem 11. Let $F$ be a set of continuous real-valued functions on $[0,1]$.
Assume that every sequence from $F$ has a subsequence that converges uniformly on $[0,1]$.
Prove both of the following:

(i) $F$ is uniformly bounded: there is $M<\infty$ such that $|f(x)|\leq M$ for all $f\in F$ and all $x\in[0,1]$;

(ii) $F$ is equicontinuous: for every $\varepsilon>0$ there is $\delta>0$ such that for all $f\in F$ and $x,y\in[0,1]$,
$$
|x-y|<\delta\implies |f(x)-f(y)|<\varepsilon.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose first that $F$ is not uniformly bounded. Then for every integer $n\geq1$ there exist
$$
f_n\in F,
\qquad x_n\in[0,1]
$$
such that
$$
|f_n(x_n)|>n.
$$


::: pf-proof

This is exactly the negation of the existence of a common finite bound for all values $|f(x)|$ with $f\in F$ and $x\in[0,1]$.

:::

:::

::: {.pf-step #s1-2}

The sequence $(f_n)$ cannot have a uniformly convergent subsequence.


::: pf-proof

If $f_{n_j}\to f$ uniformly, then for all sufficiently large $j$,
$$
\|f_{n_j}-f\|_\infty<1.
$$
Since the continuous function $f$ is bounded on $[0,1]$, say $\|f\|_\infty=C$, this would imply
$$
\|f_{n_j}\|_\infty\leq C+1.
$$
But step [](#s1-1){.pf-ref} gives
$$
\|f_{n_j}\|_\infty\geq|f_{n_j}(x_{n_j})|>n_j\to\infty,
$$
a contradiction.

:::

:::

::: {.pf-step #s1-3}

Therefore $F$ is uniformly bounded.


::: pf-proof

The hypothesis says every sequence in $F$ has a uniformly convergent subsequence. Step [](#s1-2){.pf-ref} contradicts that hypothesis under the assumption of step [](#s1-1){.pf-ref}. Hence the assumption was false.

:::

:::

::: {.pf-step #s1-4}

Suppose next that $F$ is not equicontinuous. Then there exist $\varepsilon_0>0$, functions $f_n\in F$, and points $x_n,y_n\in[0,1]$ such that
$$
|x_n-y_n|<\frac1n
$$
but
$$
|f_n(x_n)-f_n(y_n)|\geq\varepsilon_0.
$$


::: pf-proof

Negating equicontinuity gives an $\varepsilon_0>0$ such that for every $\delta>0$ there are $f\in F$ and $x,y$ with $|x-y|<\delta$ but $|f(x)-f(y)|\geq\varepsilon_0$. Apply this with $\delta=1/n$.

:::

:::

::: pf-step

By hypothesis, $(f_n)$ has a subsequence $(f_{n_j})$ converging uniformly to some continuous function $f$ on $[0,1]$.


::: pf-proof

This is the assumed sequential compactness property applied to the sequence constructed in step [](#s1-4){.pf-ref}. A uniform limit of continuous functions is continuous.

:::

:::

::: {.pf-step #s1-6}

Since $[0,1]$ is compact, $f$ is uniformly continuous. Hence there exists $\delta>0$ such that
$$
|x-y|<\delta
\quad\Longrightarrow\quad
|f(x)-f(y)|<\varepsilon_0/3.
$$


::: pf-proof

This is the Heine--Cantor theorem applied to the continuous function $f$ on the compact interval.

:::

:::

::: {.pf-step #s1-7}

Choose $j$ sufficiently large that
$$
\|f_{n_j}-f\|_\infty<\varepsilon_0/3
$$
and
$$
1/n_j<\delta.
$$
Then
$$
|f_{n_j}(x_{n_j})-f_{n_j}(y_{n_j})|<\varepsilon_0.
$$


::: pf-proof

Using step [](#s1-6){.pf-ref} and the triangle inequality,
$$
\begin{aligned}
|f_{n_j}(x_{n_j})-f_{n_j}(y_{n_j})|
&\leq |f_{n_j}(x_{n_j})-f(x_{n_j})|\\
&\quad+|f(x_{n_j})-f(y_{n_j})|\\
&\quad+|f(y_{n_j})-f_{n_j}(y_{n_j})|\\
&<\varepsilon_0/3+\varepsilon_0/3+\varepsilon_0/3
=\varepsilon_0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-8}

Step [](#s1-7){.pf-ref} contradicts the construction in step [](#s1-4){.pf-ref}. Therefore $F$ is equicontinuous.


::: pf-proof

Step [](#s1-4){.pf-ref} requires the same quantity to be at least $\varepsilon_0$ for every index, including $n_j$, whereas step [](#s1-7){.pf-ref} makes it strictly smaller than $\varepsilon_0$.

:::

:::

::: {.pf-step #s1-9}

Thus $F$ is both uniformly bounded and equicontinuous.


::: pf-proof

Uniform boundedness is step [](#s1-3){.pf-ref} and equicontinuity is step [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} proves both requested conclusions.

:::

:::

:::
