---
schema: qual/card@1
id: P-TRIV-LA36
kind: problem
title: Lie--Trotter product formula
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 36, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed the difficulty-glyph residue from Linear Algebra Problem 36 on page 5 of the source PDF.
---

::: {.problem}
"Trotter product formula".
Consider $n \times n$ complex matrices $A$, $B$.
Prove that $e^{A+B} = \lim_{N \to \infty} \left(e^{A/N} e^{B/N}\right)^N$, $N \in \mathbb{R}$.
:::

::: {.remark}
The source writes $N\in\mathbb R$, but the ordinary matrix power
$(e^{A/N}e^{B/N})^N$ used here is defined for positive integer $N$. The limit
is therefore taken along $N\in\mathbb N$.
:::

Fix any submultiplicative matrix norm $\|\cdot\|$.

::: pf

::: pf-step

As $N\to\infty$,
$$
e^{A/N}
=
I+\frac AN+O(N^{-2})
$$
and
$$
e^{B/N}
=
I+\frac BN+O(N^{-2}).
$$


::: pf-proof

From the exponential series,
$$
e^{A/N}
=
I+\frac AN
+
\sum_{k=2}^{\infty}
\frac{A^k}{k!N^k}.
$$
Using submultiplicativity,
$$
\left\|
\sum_{k=2}^{\infty}
\frac{A^k}{k!N^k}
\right\|
\leq
\frac1{N^2}
\sum_{k=2}^{\infty}
\frac{\|A\|^k}{k!},
$$
which is $O(N^{-2})$. The argument for $B$ is identical.

:::

:::

::: pf-step

Hence
$$
e^{A/N}e^{B/N}
=
I
+
\frac{A+B}{N}
+
O(N^{-2}).
$$


::: pf-proof

Multiply the two expansions from step <1>1:
$$
\left(I+\frac AN+O(N^{-2})\right)
\left(I+\frac BN+O(N^{-2})\right).
$$
The linear terms give $(A+B)/N$, and every remaining nonconstant term is
$O(N^{-2})$.

:::

:::

::: pf-step

Put
$$
X_N
=
e^{A/N}e^{B/N}-I.
$$
Then
$$
X_N
=
\frac{A+B}{N}
+
O(N^{-2})
$$
and
$$
\|X_N\|\longrightarrow0.
$$


::: pf-proof

This is step <1>2 rewritten.

:::

:::

::: pf-step

For all sufficiently large $N$, the convergent logarithm series gives
$$
\log(I+X_N)
=
X_N
+
O(\|X_N\|^2).
$$


::: pf-proof

When $\|X_N\|<1$, define
$$
\log(I+X_N)
=
\sum_{k=1}^{\infty}
\frac{(-1)^{k+1}}{k}X_N^k.
$$
The terms from $k\geq2$ have norm bounded by a constant multiple of
$\|X_N\|^2$ for $N$ large enough.

:::

:::

::: pf-step

Therefore
$$
N\log\left(e^{A/N}e^{B/N}\right)
=
A+B+O(N^{-1}).
$$


::: pf-proof

By steps <1>3--<1>4,
$$
\begin{aligned}
\log\left(e^{A/N}e^{B/N}\right)
&=
X_N+O(\|X_N\|^2)\\
&=
\frac{A+B}{N}+O(N^{-2}).
\end{aligned}
$$
Multiply by $N$.

:::

:::

::: pf-step

For sufficiently large $N$,
$$
\left(e^{A/N}e^{B/N}\right)^N
=
\exp\left(
N\log\left(e^{A/N}e^{B/N}\right)
\right).
$$


::: pf-proof

Set
$$
Y_N=e^{A/N}e^{B/N}=I+X_N.
$$
For $N$ large, $\log Y_N$ is defined by the convergent series from step
<1>4 and satisfies
$$
e^{\log Y_N}=Y_N.
$$
Since $\log Y_N$ commutes with itself,
$$
Y_N^N
=
\left(e^{\log Y_N}\right)^N
=
e^{N\log Y_N}.
$$

:::

:::

::: pf-step

Taking $N\to\infty$ gives
$$
\boxed{
\lim_{N\to\infty}
\left(e^{A/N}e^{B/N}\right)^N
=
e^{A+B}.
}
$$


::: pf-proof

By step <1>5,
$$
N\log\left(e^{A/N}e^{B/N}\right)
\longrightarrow
A+B.
$$
The matrix exponential is continuous, so step <1>6 yields
$$
\left(e^{A/N}e^{B/N}\right)^N
\longrightarrow
e^{A+B}.
$$

:::

:::

::: pf-qed

Step <1>7 is the Lie--Trotter product formula.

:::

:::
