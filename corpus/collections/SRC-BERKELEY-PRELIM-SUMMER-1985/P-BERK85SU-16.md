---
schema: qual/card@1
id: P-BERK85SU-16
kind: problem
title: An upper-semicontinuous function on $[0,1]$ is bounded above and attains its maximum
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Upper semicontinuity with epsilon=1 gives a local upper bound near each
    point; compactness produces a finite subcover and hence a global upper
    bound. A maximizing sequence has a convergent subsequence, and upper
    semicontinuity at its limit forces the supremum to equal the value there.
---

::: {.problem}
A function $f:[0,1]\to\mathbb R$ is called upper semicontinuous if for every $x\in[0,1]$ and every $\varepsilon>0$ there exists $\delta>0$ such that
\[
|y-x|<\delta\quad\Longrightarrow\quad f(y)<f(x)+\varepsilon.
\]
Prove that an upper-semicontinuous function on $[0,1]$ is bounded above and attains its maximum at some point of $[0,1]$.
:::

::: {.solution}
<1>1. The function $f$ is bounded above on $[0,1]$.

::: {.proof}
For each $x\in[0,1]$, apply upper semicontinuity with
$\varepsilon=1$. There is an open neighborhood $U_x$ of $x$ in
$[0,1]$ such that
$$
y\in U_x
\quad\Longrightarrow\quad
f(y)<f(x)+1.
$$
The sets $U_x$ cover the compact interval $[0,1]$, so finitely many
of them,
$$
U_{x_1},\ldots,U_{x_m},
$$
already cover $[0,1]$. Set
$$
B=\max_{1\le j\le m}\bigl(f(x_j)+1\bigr).
$$
For any $y\in[0,1]$, choose $j$ with $y\in U_{x_j}$. Then
$$
f(y)<f(x_j)+1\le B.
$$
Thus $f$ is bounded above.
:::

<1>2. Let
$$
M=\sup_{x\in[0,1]}f(x).
$$
There is a sequence $(x_n)$ in $[0,1]$ such that
$$
f(x_n)>M-\frac1n
$$
for every $n\ge1$.

::: {.proof}
Step <1>1 shows that $M$ is finite. By the definition of supremum,
for each $n$ there is some $x_n\in[0,1]$ with
$f(x_n)>M-1/n$.
:::

<1>3. Some subsequence $(x_{n_k})$ converges to a point
$p\in[0,1]$.

::: {.proof}
The interval $[0,1]$ is compact, so every sequence in it has a
convergent subsequence whose limit remains in $[0,1]$.
:::

<1>4. One has
$$
M\le f(p).
$$

::: {.proof}
Fix $\varepsilon>0$. By upper semicontinuity at $p$, there is
$\delta>0$ such that
$$
\abs{y-p}<\delta
\quad\Longrightarrow\quad
f(y)<f(p)+\varepsilon.
$$
Since $x_{n_k}\to p$, for all sufficiently large $k$,
$$
f(x_{n_k})<f(p)+\varepsilon.
$$
On the other hand, step <1>2 gives
$$
f(x_{n_k})>M-\frac1{n_k}.
$$
Letting $k\to\infty$ yields
$$
M\le f(p)+\varepsilon.
$$
Since $\varepsilon>0$ was arbitrary, $M\le f(p)$.
:::

<1>5. The function $f$ attains its maximum at $p$:
$$
\boxed{f(p)=M}.
$$

::: {.proof}
By definition of $M$ as a supremum, $f(p)\le M$. Step <1>4 gives
the reverse inequality, so equality holds.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 proves boundedness above, and step <1>5 proves attainment
of the maximum.
:::
:::
