---
schema: qual/card@1
id: P-UCLAB13F-03
kind: problem
title: Length of graphs of monotone functions
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
Let $\gamma:[0,1]\to\RR^2$ be continuous and one-to-one, and define
$$
L(\gamma)=\sup\left\{\sum_{j=1}^{n-1}\norm{\gamma(t_{j+1})-\gamma(t_j)}:0\le t_1<\cdots<t_n\le1,\ n<\infty\right\}.
$$

(a) If $f$ is continuous and nondecreasing on $[0,1]$ and $\gamma(t)=(t,f(t))$, prove
$$
L(\gamma)\le 1+f(1)-f(0).
$$

(b) Show that there exists continuous nondecreasing $f$ on $[0,1]$ with $f(0)=0$, $f(1)=1$, and $L(\gamma)=2$ for $\gamma(t)=(t,f(t))$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
$$
0\le t_1<\cdots<t_n\le1.
$$
If $f$ is nondecreasing, then for every $j$,
$$
\norm{\gamma(t_{j+1})-\gamma(t_j)}
\le
(t_{j+1}-t_j)
+
\bigl(f(t_{j+1})-f(t_j)\bigr).
$$


::: pf-proof

Since both coordinate increments are nonnegative,
$$
\begin{aligned}
\norm{\gamma(t_{j+1})-\gamma(t_j)}
&=
\sqrt{
(t_{j+1}-t_j)^2
+
(f(t_{j+1})-f(t_j))^2
}\\
&\le
(t_{j+1}-t_j)
+
(f(t_{j+1})-f(t_j)),
\end{aligned}
$$
using
$$
\sqrt{a^2+b^2}\le a+b
$$
for $a,b\ge0$.

:::

:::

::: {.pf-step #s1-2}

For every such partition,
$$
\sum_{j=1}^{n-1}
\norm{\gamma(t_{j+1})-\gamma(t_j)}
\le
1+f(1)-f(0).
$$


::: pf-proof

Sum the estimate from step [](#s1-1){.pf-ref}:
$$
\begin{aligned}
\sum_{j=1}^{n-1}
\norm{\gamma(t_{j+1})-\gamma(t_j)}
&\le
\sum_{j=1}^{n-1}(t_{j+1}-t_j)\\
&\quad+
\sum_{j=1}^{n-1}
\bigl(f(t_{j+1})-f(t_j)\bigr).
\end{aligned}
$$
Both sums telescope:
$$
\sum_{j=1}^{n-1}(t_{j+1}-t_j)
=
t_n-t_1
\le1,
$$
and
$$
\sum_{j=1}^{n-1}
\bigl(f(t_{j+1})-f(t_j)\bigr)
=
f(t_n)-f(t_1)
\le
f(1)-f(0).
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{L(\gamma)\le1+f(1)-f(0)}.
$$


::: pf-proof

The length is the supremum of the partition sums appearing in step [](#s1-2){.pf-ref}, all of which satisfy the same upper bound.

:::

:::

::: {.pf-step #s1-4}

For part (b), let $f$ be the Cantor--Lebesgue function on $[0,1]$.
Then $f$ is continuous and nondecreasing, with
$$
f(0)=0,
\qquad
f(1)=1.
$$


::: pf-proof

Recall the standard Cantor-function construction.
On the middle-third Cantor set, write
$$
x=0.a_1a_2a_3\cdots{}_3,
\qquad
a_j\in\{0,2\},
$$
and define
$$
f(x)
=
0.\frac{a_1}{2}\frac{a_2}{2}\frac{a_3}{2}\cdots{}_2.
$$
Extend $f$ constantly across every complementary middle-third interval.
This gives the classical Cantor--Lebesgue function, which is continuous, nondecreasing, and has the stated endpoint values.

:::

:::

::: {.pf-step #s1-5}

At stage $k$ of the Cantor construction, there are $2^k$ closed basic intervals, each of length
$$
3^{-k},
$$
and on each such interval the Cantor function increases by exactly
$$
2^{-k}.
$$
The complementary gaps created by stages at most $k$ have total length
$$
1-\left(\frac23\right)^k,
$$
and $f$ is constant on each of them.


::: pf-proof

After $k$ stages, the Cantor construction leaves $2^k$ intervals, each obtained by choosing left or right thirds $k$ times, so each has length $3^{-k}$.
The total remaining length is therefore
$$
2^k3^{-k}
=
\left(\frac23\right)^k,
$$
so the removed gaps have total length
$$
1-\left(\frac23\right)^k.
$$

The binary description of the Cantor function shows that changing from the left endpoint to the right endpoint of one stage-$k$ basic interval changes the binary value by exactly $2^{-k}$.

:::

:::

::: {.pf-step #s1-6}

Let $P_k$ be the partition consisting of all endpoints of the stage-$k$ basic intervals and all gaps between them.
Then the corresponding polygonal sum for the graph of $f$ is
$$
L_k
=
1-\left(\frac23\right)^k
+
2^k
\sqrt{3^{-2k}+2^{-2k}}.
$$


::: pf-proof

Across every removed gap, $f$ is constant, so the graph increment has length equal to the horizontal length of that gap.
The total contribution from all gaps is therefore
$$
1-\left(\frac23\right)^k.
$$

Across each of the $2^k$ surviving basic intervals, the horizontal increment is $3^{-k}$ and the vertical increment is $2^{-k}$ by step [](#s1-5){.pf-ref}.
Thus each contributes
$$
\sqrt{3^{-2k}+2^{-2k}},
$$
giving the displayed total.

:::

:::

::: {.pf-step #s1-7}

The quantity in step [](#s1-6){.pf-ref} satisfies
$$
L_k
=
1-\left(\frac23\right)^k
+
\sqrt{
1+\left(\frac23\right)^{2k}
}
\longrightarrow2.
$$


::: pf-proof

Compute
$$
\begin{aligned}
2^k\sqrt{3^{-2k}+2^{-2k}}
&=
\sqrt{
\left(\frac{2}{3}\right)^{2k}
+1
}.
\end{aligned}
$$
Since
$$
\left(\frac23\right)^k\to0,
$$
the first term tends to $1$ and the square-root term tends to $1$.

:::

:::

::: {.pf-step #s1-8}

For the Cantor function,
$$
L(\gamma)\ge2.
$$


::: pf-proof

By definition, $L(\gamma)$ is the supremum over all partition sums.
Each $L_k$ from step [](#s1-6){.pf-ref} is one such partition sum.
Hence
$$
L(\gamma)\ge L_k
$$
for every $k$.
Taking $k\to\infty$ and using step [](#s1-7){.pf-ref} gives
$$
L(\gamma)\ge2.
$$

:::

:::

::: {.pf-step #s1-9}

For the Cantor function,
$$
L(\gamma)\le2.
$$


::: pf-proof

Apply part (a), proved in step [](#s1-3){.pf-ref}, using
$$
f(0)=0,
\qquad
f(1)=1.
$$
Then
$$
L(\gamma)
\le
1+1-0
=2.
$$

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{L(\gamma)=2}
$$
for the graph of the Cantor--Lebesgue function.


::: pf-proof

Combine steps [](#s1-8){.pf-ref} and [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and steps [](#s1-4){.pf-ref} through [](#s1-10){.pf-ref} give the required example for part (b).

:::

:::

:::
