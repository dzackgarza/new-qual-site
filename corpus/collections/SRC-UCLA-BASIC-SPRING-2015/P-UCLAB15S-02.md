---
schema: qual/card@1
id: P-UCLAB15S-02
kind: problem
title: Compact embedding between Hölder spaces
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let $f:[0,1]\to\RR$.
We say that $f$ is Hölder continuous of order $\alpha\in(0,1)$ and write $f\in C^\alpha([0,1])$ if
$$
\norm{f}_{C^\alpha}
:=\sup_{x\in[0,1]}\abs{f(x)}
+\sup_{\substack{x,y\in[0,1]\\x\ne y}}
\frac{\abs{f(x)-f(y)}}{\abs{x-y}^\alpha}<\infty.
$$
This defines a norm on $C^\alpha([0,1])$.
Prove that any bounded sequence in $C^{1/2}([0,1])$ admits a convergent subsequence in $C^{1/3}([0,1])$.
:::

::: {.solution}

Let
$$
(f_n)
$$
be bounded in
$$
C^{1/2}([0,1]).
$$
Choose
$$
M>0
$$
such that
$$
\norm{f_n}_{C^{1/2}}\le M
$$
for every $n$.

::: pf

::: {.pf-step #s1-1}

The family $(f_n)$ is uniformly bounded and equicontinuous on $[0,1]$.


::: pf-proof

The norm bound gives
$$
\norm{f_n}_\infty\le M
$$
for every $n$.
It also gives
$$
\abs{f_n(x)-f_n(y)}
\le
M\abs{x-y}^{1/2}
$$
for all $x,y$.
Thus the family has a common Hölder modulus of continuity.

:::

:::

::: {.pf-step #s1-2}

There is a subsequence
$$
(f_{n_j})
$$
that converges uniformly on $[0,1]$ to a continuous function $f$.


::: pf-proof

Apply the Arzelà--Ascoli theorem to step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The limit $f$ belongs to
$$
C^{1/2}([0,1])
$$
and satisfies
$$
[f]_{1/2}\le M,
$$
where
$$
[g]_{1/2}
=
\sup_{x\ne y}
\frac{\abs{g(x)-g(y)}}{\abs{x-y}^{1/2}}.
$$


::: pf-proof

Fix $x,y\in[0,1]$.
Uniform convergence implies pointwise convergence, so
$$
\begin{aligned}
\abs{f(x)-f(y)}
&=
\lim_{j\to\infty}
\abs{f_{n_j}(x)-f_{n_j}(y)}\\
&\le
M\abs{x-y}^{1/2}.
\end{aligned}
$$
Taking the supremum gives the stated bound.

:::

:::

::: {.pf-step #s1-4}

For
$$
g_j=f_{n_j}-f,
$$
one has
$$
\norm{g_j}_\infty\to0
$$
and
$$
[g_j]_{1/2}\le2M.
$$


::: pf-proof

The uniform convergence in step [](#s1-2){.pf-ref} gives
$$
\norm{g_j}_\infty\to0.
$$
Also,
$$
[g_j]_{1/2}
\le
[f_{n_j}]_{1/2}
+
[f]_{1/2}
\le
M+M
=
2M
$$
by the triangle inequality for the Hölder seminorm and step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

If a function $g$ satisfies
$$
\norm{g}_\infty\le \eta
$$
and
$$
[g]_{1/2}\le H,
$$
then
$$
\boxed{
[g]_{1/3}
\le
(2\eta)^{1/3}H^{2/3}.
}
$$


::: pf-proof

Fix
$$
x\ne y
$$
and set
$$
r=\abs{x-y}.
$$
Two estimates hold:
$$
\abs{g(x)-g(y)}
\le
2\eta
$$
and
$$
\abs{g(x)-g(y)}
\le
Hr^{1/2}.
$$
Therefore
$$
\frac{\abs{g(x)-g(y)}}{r^{1/3}}
\le
\min
\left\{
2\eta\,r^{-1/3},
H r^{1/6}
\right\}.
$$
The two expressions are equal when
$$
r^{1/2}
=
\frac{2\eta}{H}.
$$
At that value their common value is
$$
(2\eta)^{1/3}H^{2/3}.
$$
For smaller $r$, the second expression is no larger than that value; for larger $r$, the first expression is no larger.
Thus the displayed bound holds for every pair $x\ne y$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
[g_j]_{1/3}\to0.
$$


::: pf-proof

Apply step [](#s1-5){.pf-ref} with
$$
\eta=\norm{g_j}_\infty
$$
and
$$
H=2M.
$$
By step [](#s1-4){.pf-ref},
$$
\eta\to0.
$$
Hence
$$
[g_j]_{1/3}
\le
\bigl(2\norm{g_j}_\infty\bigr)^{1/3}
(2M)^{2/3}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\norm{f_{n_j}-f}_{C^{1/3}}
\to0.
$$


::: pf-proof

By definition,
$$
\norm{f_{n_j}-f}_{C^{1/3}}
=
\norm{g_j}_\infty
+
[g_j]_{1/3}.
$$
The first term tends to zero by step [](#s1-4){.pf-ref}, and the second by step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Thus every bounded sequence in
$$
C^{1/2}([0,1])
$$
has a subsequence converging in
$$
\boxed{C^{1/3}([0,1])}.
$$


::: pf-proof

The subsequence constructed in step [](#s1-2){.pf-ref} converges in the stronger sense established in step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required compact-embedding statement.

:::

:::

:::
