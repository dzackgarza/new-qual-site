---
schema: qual/card@1
id: P-BKF07-4A
kind: problem
title: A perturbed monotone sequence has a finite limit
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
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained uniform tail-sum/limsup argument.
    Also corrected the selected card's transcription of the sequence
    subscript from *{n>=1} to _{n>=1} against the retained source.
---

::: {.problem}
Let \((a_n)_{n\ge1}\) and \((b_n)_{n\ge1}\) be real sequences.
Suppose
\[
0\le a_{n+1}\le a_n+b_n
\]
for every \(n\ge1\), and suppose \(\sum_{n=1}^\infty b_n\) converges.
Prove that \(\lim_{n\to\infty}a_n\) exists and is finite.
:::

::: {.solution}

::: pf

::: {.pf-step #cauchy-tail-bound}
For every $\epsilon>0$, there exists $N$ such that for all
$m>n\ge N$,
$$
\left|\sum_{j=n}^{m-1}b_j\right|<\epsilon.
$$

::: pf-proof
The series $\sum_{j=1}^{\infty}b_j$ converges, so its sequence of
partial sums is Cauchy. The displayed estimate is exactly the Cauchy
criterion for the tail from $n$ through $m-1$.
:::

:::

::: {.pf-step #telescoping-bound}
If $m>n$, then
$$
a_m
\le
a_n+\sum_{j=n}^{m-1}b_j.
$$

::: pf-proof
Iterate the inequalities
$$
a_{j+1}\le a_j+b_j
$$
for $j=n,n+1,\ldots,m-1$. The intermediate $a_j$ terms telescope,
giving the displayed bound.
:::

:::

::: {.pf-step #am-less-an-eps}
For every $\epsilon>0$, if $N$ is as in step [](#cauchy-tail-bound){.pf-ref}, then
$$
a_m<a_n+\epsilon
$$
whenever $m>n\ge N$.

::: pf-proof
Combine steps [](#cauchy-tail-bound){.pf-ref} and [](#telescoping-bound){.pf-ref}:
$$
a_m
\le
a_n+\sum_{j=n}^{m-1}b_j
\le
a_n+\left|\sum_{j=n}^{m-1}b_j\right|
<
a_n+\epsilon.
$$
:::

:::

::: {.pf-step #an-bounded}
The sequence $(a_n)$ is bounded.

::: pf-proof
The hypothesis gives $a_n\ge0$ for every $n\ge2$, so the sequence is
bounded below. Fix $\epsilon=1$ in step [](#am-less-an-eps){.pf-ref} and the corresponding
$N$. Then every $m>N$ satisfies
$$
a_m<a_N+1.
$$
Together with the finitely many terms $a_1,\ldots,a_N$, this gives an
upper bound.
:::

:::

::: {.pf-step #limsup-liminf-eps}
One has
$$
\limsup_{n\to\infty}a_n
\le
\liminf_{n\to\infty}a_n+\epsilon
$$
for every $\epsilon>0$.

::: pf-proof
Fix $\epsilon>0$ and let $N$ be as in step [](#cauchy-tail-bound){.pf-ref}. For every $n\ge N$,
step [](#am-less-an-eps){.pf-ref} gives
$$
\sup_{m>n}a_m\le a_n+\epsilon.
$$
By step [](#an-bounded){.pf-ref}, both $\limsup a_n$ and $\liminf a_n$ are finite.
Taking $\liminf$ as $n\to\infty$ on the right and using
$$
\lim_{n\to\infty}\sup_{m>n}a_m
=
\limsup_{n\to\infty}a_n
$$
gives the claimed inequality.
:::

:::

::: {.pf-step #limit-exists-finite}
The limit of $(a_n)$ exists and is finite.

::: pf-proof
Letting $\epsilon\downarrow0$ in step [](#limsup-liminf-eps){.pf-ref} gives
$$
\limsup_{n\to\infty}a_n
\le
\liminf_{n\to\infty}a_n.
$$
The reverse inequality always holds, so the two are equal. By step
[](#an-bounded){.pf-ref} their common value is finite. Hence
$$
\boxed{\lim_{n\to\infty}a_n\text{ exists and is finite}}.
$$
:::

:::

::: pf-qed
Step [](#limit-exists-finite){.pf-ref} proves the required conclusion.
:::

:::

:::
