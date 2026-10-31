---
schema: qual/card@1
id: P-TRIV-LA36
kind: problem
title: Lie--Trotter product formula
classification:
  areas: [prelim]
  topics:
  - Matrix Exponential
  - Lie-Trotter Product Formula
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
Prove that $e^{A+B} = \lim_{N \to \infty} \left(e^{A/N} e^{B/N}\right)^N$, $N \in \RR$.
:::

::: {.remark}
The source writes $N\in\RR$, but the ordinary matrix power
$(e^{A/N}e^{B/N})^N$ used here is defined for positive integer $N$. The limit
is therefore taken along $N\in\NN$.
:::

::: {.solution}

Fix any submultiplicative matrix norm $\norm{\cdot}$.

::: pf

::: {.pf-step #s1-1}

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
\norm{
\sum_{k=2}^{\infty}
\frac{A^k}{k!N^k}
}
\leq
\frac1{N^2}
\sum_{k=2}^{\infty}
\frac{\norm{A}^k}{k!},
$$
which is $O(N^{-2})$. The argument for $B$ is identical.

:::

:::

::: {.pf-step #s1-2}

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

Multiply the two expansions from step [](#s1-1){.pf-ref}:
$$
\left(I+\frac AN+O(N^{-2})\right)
\left(I+\frac BN+O(N^{-2})\right).
$$
The linear terms give $(A+B)/N$, and every remaining nonconstant term is
$O(N^{-2})$.

:::

:::

::: {.pf-step #s1-3}

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
\norm{X_N}\longrightarrow0.
$$


::: pf-proof

This is step [](#s1-2){.pf-ref} rewritten.

:::

:::

::: {.pf-step #s1-4}

For all sufficiently large $N$, the convergent logarithm series gives
$$
\log(I+X_N)
=
X_N
+
O(\norm{X_N}^2).
$$


::: pf-proof

When $\norm{X_N}<1$, define
$$
\log(I+X_N)
=
\sum_{k=1}^{\infty}
\frac{(-1)^{k+1}}{k}X_N^k.
$$
The terms from $k\geq2$ have norm bounded by a constant multiple of
$\norm{X_N}^2$ for $N$ large enough.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
N\log\left(e^{A/N}e^{B/N}\right)
=
A+B+O(N^{-1}).
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref},
$$
\begin{aligned}
\log\left(e^{A/N}e^{B/N}\right)
&=
X_N+O(\norm{X_N}^2)\\
&=
\frac{A+B}{N}+O(N^{-2}).
\end{aligned}
$$
Multiply by $N$.

:::

:::

::: {.pf-step #s1-6}

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
[](#s1-4){.pf-ref} and satisfies
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

::: {.pf-step #s1-7}

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

By step [](#s1-5){.pf-ref},
$$
N\log\left(e^{A/N}e^{B/N}\right)
\longrightarrow
A+B.
$$
The matrix exponential is continuous, so step [](#s1-6){.pf-ref} yields
$$
\left(e^{A/N}e^{B/N}\right)^N
\longrightarrow
e^{A+B}.
$$

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the Lie--Trotter product formula.

:::

:::

:::
