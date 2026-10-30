---
schema: qual/card@1
id: P-PRACT20-W5-29
kind: problem
title: Contour integral of $\frac{\cosh\pi z}{z(z^2+1)}$ around $\abs{z}=2$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 29).
---

::: {.problem}
Let $C$ be the circle $\abs{z} = 2$, oriented positively. Evaluate $\oint_C \frac{\cosh(\pi z)\,dz}{z(z^2 + 1)}$.
:::

::: {.solution}

Let
$$
F(z)=\frac{\cosh(\pi z)}{z(z^2+1)}
=
\frac{\cosh(\pi z)}{z(z-i)(z+i)}.
$$

::: pf

::: pf-step

The poles of $F$ inside $C$ are the three simple poles
$$
0,\qquad i,\qquad -i.
$$


::: pf-proof

These are exactly the zeros of
$$
z(z^2+1),
$$
and all have modulus less than $2$.

:::

:::

::: {.pf-step #s1-2}

The residue at $0$ is
$$
\operatorname{Res}(F,0)=1.
$$


::: pf-proof

Since the pole is simple,
$$
\operatorname{Res}(F,0)
=
\lim_{z\to0}
\frac{\cosh(\pi z)}{z^2+1}
=1.
$$

:::

:::

::: {.pf-step #s1-3}

The residues at $i$ and $-i$ are both
$$
\frac12.
$$


::: pf-proof

At $i$,
$$
\begin{aligned}
\operatorname{Res}(F,i)
&=
\frac{\cosh(\pi i)}{i(i+i)}\\
&=
\frac{\cos\pi}{i(2i)}\\
&=
\frac{-1}{-2}
=\frac12.
\end{aligned}
$$
At $-i$,
$$
\begin{aligned}
\operatorname{Res}(F,-i)
&=
\frac{\cosh(-\pi i)}{(-i)(-i-i)}\\
&=
\frac{\cos\pi}{(-i)(-2i)}\\
&=
\frac{-1}{-2}
=\frac12.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\oint_C\frac{\cosh(\pi z)}{z(z^2+1)}\,dz
=4\pi i }.
$$


::: pf-proof

By the residue theorem and steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref},
$$
\oint_C F(z)\,dz
=
2\pi i
\left(
1+\frac12+\frac12
\right)
=4\pi i.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value.

:::

:::

:::
