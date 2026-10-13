---
schema: qual/card@1
id: P-PRACT20-W5-29
kind: problem
title: Contour integral of $\frac{\cosh\pi z}{z(z^2+1)}$ around $|z|=2$
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
\[
F(z)=\frac{\cosh(\pi z)}{z(z^2+1)}
=
\frac{\cosh(\pi z)}{z(z-i)(z+i)}.
\]

<1>1. The poles of $F$ inside $C$ are the three simple poles
\[
0,\qquad i,\qquad -i.
\]

::: {.proof}
These are exactly the zeros of
\[
z(z^2+1),
\]
and all have modulus less than $2$.
:::

<1>2. The residue at $0$ is
\[
\operatorname{Res}(F,0)=1.
\]

::: {.proof}
Since the pole is simple,
\[
\operatorname{Res}(F,0)
=
\lim_{z\to0}
\frac{\cosh(\pi z)}{z^2+1}
=1.
\]
:::

<1>3. The residues at $i$ and $-i$ are both
\[
\frac12.
\]

::: {.proof}
At $i$,
\[
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
\]
At $-i$,
\[
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
\]
:::

<1>4. Therefore
\[
\boxed{
\oint_C\frac{\cosh(\pi z)}{z(z^2+1)}\,dz
=4\pi i }.
\]

::: {.proof}
By the residue theorem and steps <1>2 and <1>3,
\[
\oint_C F(z)\,dz
=
2\pi i
\left(
1+\frac12+\frac12
\right)
=4\pi i.
\]
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested value.
:::
:::
