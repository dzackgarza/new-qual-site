---
schema: qual/card@1
id: P-BKS19-9A
kind: problem
title: For fast-growing $f$, the sum $\sum 1/f(n)$ avoids a given countable set
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
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 recursive construction. Its core finite-prefix argument is correct, but the printed proof has an index mismatch between $g_{n+1}$ and prefixes ending at $f(n)$. The solution below corrects this by defining $g_n(m)$ from the admissible length-$n$ prefixes ending at $m$.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified finiteness of each prefix set, recursive definability of every $g_n$, geometric convergence, the uniform tail bound, and exclusion of each enumerated element of $S$.
---

::: {.problem}
Let $S$ be a countable set of real numbers.
Show that there are functions $g_n:\NN\to\NN$ such that if $f:\NN\to\NN$ satisfies
$$
f(n+1)>g_n(f(n))\qquad\text{for all }n,
$$
then
$$
A=\sum_{n=1}^{\infty}\frac1{f(n)}
$$
converges to a real number that is not in $S$.
:::

::: {.solution}

Take $\NN=\{1,2,\ldots\}$. If $S=\varnothing$, the choice $g_n(m)=2m$ already suffices, so assume $S\neq\varnothing$. Choose a sequence
$$
s_1,s_2,\ldots
$$
whose range is $S$; if $S$ is finite, repeat its elements as necessary.

::: pf

::: {.pf-step #s1-1}

Suppose $g_1,\ldots,g_{n-1}$ have been defined and satisfy
$$
g_j(m)>2m
$$
for every admissible $j,m$. For each $m\in\NN$, let $P_{n,m}$ be the set of numbers
$$
p=\sum_{j=1}^n\frac1{a_j}
$$
arising from sequences $a_1,\ldots,a_n\in\NN$ such that
$$
a_n=m,
\qquad
a_{j+1}>g_j(a_j)\quad(1\leq j<n).
$$
Then $P_{n,m}$ is finite.


::: pf-proof

For every such sequence, the inequalities $g_j(a_j)>2a_j$ imply
$$
a_1<a_2<\cdots<a_n=m.
$$
Thus each of $a_1,\ldots,a_{n-1}$ belongs to the finite set $\{1,\ldots,m-1\}$. Only finitely many length-$n$ sequences can therefore occur, so only finitely many corresponding prefix sums occur.

:::

:::

::: {.pf-step #s1-2}

The functions $g_n:\NN\to\NN$ can be defined recursively so that, for every $m$,
$$
g_n(m)>2m,
$$
and, whenever
$$
D_{n,m}\coloneqq\{|p-s_n|:p\in P_{n,m},\ p\neq s_n\}
$$
is nonempty,
$$
g_n(m)>\frac{2}{\min D_{n,m}}.
$$


::: pf-proof

For fixed $n,m$, step [](#s1-1){.pf-ref} shows that $P_{n,m}$ is finite, hence so is $D_{n,m}$. If $D_{n,m}$ is nonempty, all of its elements are positive, so $\min D_{n,m}>0$. There is therefore an integer larger than both $2m$ and $2/\min D_{n,m}$. Choose $g_n(m)$ to be such an integer. If $D_{n,m}$ is empty, choose any integer larger than $2m$. Starting with $n=1$, where $P_{1,m}=\{1/m\}$, this defines the functions successively for all $n$.

:::

:::

::: {.pf-step #s1-3}

For any $f:\NN\to\NN$ satisfying
$$
f(n+1)>g_n(f(n))
$$
for all $n$, the series
$$
A=\sum_{n=1}^\infty\frac1{f(n)}
$$
converges.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
f(n+1)>g_n(f(n))>2f(n).
$$
Inductively,
$$
f(n)\geq2^{n-1}f(1).
$$
Consequently
$$
0<\sum_{n=1}^\infty\frac1{f(n)}
\leq
\frac1{f(1)}\sum_{n=1}^\infty2^{-(n-1)}
=
\frac2{f(1)},
$$
so the series converges.

:::

:::

::: {.pf-step #s1-4}

For every $n$, if
$$
p_n\coloneqq\sum_{j=1}^n\frac1{f(j)},
\qquad
T_n\coloneqq\sum_{j=n+1}^\infty\frac1{f(j)},
$$
then
$$
0<T_n<\frac{2}{g_n(f(n))}.
$$


::: pf-proof

Put $m=f(n)$. The defining inequality gives $f(n+1)>g_n(m)$. Thereafter step [](#s1-2){.pf-ref} gives
$$
f(n+k)\geq2^{k-1}f(n+1)
\qquad(k\geq1).
$$
Hence
$$
T_n
\leq
\frac1{f(n+1)}\sum_{k=1}^\infty2^{-(k-1)}
=
\frac2{f(n+1)}
<
\frac2{g_n(m)}.
$$
Positivity is immediate because every summand is positive.

:::

:::

::: {.pf-step #s1-5}

For every $n$, one has $A\neq s_n$.


::: pf-proof

Fix $n$ and set $m=f(n)$. The actual first $n$ values $f(1),\ldots,f(n)$ satisfy the defining conditions for $P_{n,m}$, so $p_n\in P_{n,m}$.

If $p_n=s_n$, then step [](#s1-4){.pf-ref} gives $A=p_n+T_n>s_n$.

Suppose $p_n\neq s_n$. Then $D_{n,m}$ is nonempty, and step [](#s1-2){.pf-ref} together with step [](#s1-4){.pf-ref} gives
$$
0<T_n
<
\frac2{g_n(m)}
<
\min D_{n,m}
\leq
|p_n-s_n|.
$$
If $p_n>s_n$, then $A=p_n+T_n>s_n$. If $p_n<s_n$, then
$$
A=p_n+T_n
<p_n+(s_n-p_n)
=s_n.
$$
Thus in every case $A\neq s_n$.

:::

:::

::: {.pf-step #s1-6}

The constructed functions satisfy the required conclusion:
$$
\boxed{A\in\RR\setminus S}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} shows that $A$ converges to a real number. Since the sequence $(s_n)$ has range $S$, step [](#s1-5){.pf-ref} shows that $A$ is unequal to every element of $S$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is exactly the desired conclusion.

:::

:::

:::
