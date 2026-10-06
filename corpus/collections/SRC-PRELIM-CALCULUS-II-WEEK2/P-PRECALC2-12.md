---
schema: qual/card@1
id: P-PRECALC2-12
kind: problem
title: Convergence of $\sum\frac{1}{n^\alpha(\log n)^\beta}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
For what values of $\alpha , \beta \in \mathbb { R }$ does the series

$$
\sum _ { n = 2 } ^ { \infty } { \frac { 1 } { n ^ { \alpha } \log ( n ) ^ { \beta } } }
$$

converge/diverge?
:::

::: {.solution}
Consider
\[
\sum_{n=2}^{\infty}
\frac1{n^\alpha(\log n)^\beta}.
\]

<1>1. For every \(q>0\) and every \(\varepsilon>0\),
\[
\boxed{
(\log n)^q
\le
n^\varepsilon}
\]
for all sufficiently large \(n\).

::: {.proof}
It suffices to prove
\[
q\log\log n
\le
\varepsilon\log n
\]
eventually. Since
\[
\frac{\log\log n}{\log n}\longrightarrow0,
\]
this inequality holds for all sufficiently large \(n\).
:::

## Case \(\alpha>1\)

<1>2. Suppose \(\alpha>1\) and \(\beta\ge0\). Then, for \(n\ge3\),
\[
\frac1{n^\alpha(\log n)^\beta}
\le
\frac1{n^\alpha}.
\]

::: {.proof}
For \(n\ge3\),
\[
\log n>1,
\]
so
\[
(\log n)^\beta\ge1.
\]
:::

<1>3. Therefore the series converges when
\[
\alpha>1,\qquad \beta\ge0.
\]

::: {.proof}
The comparison series
\[
\sum\frac1{n^\alpha}
\]
converges because \(\alpha>1\). Apply step <1>2.
:::

<1>4. Suppose \(\alpha>1\) and \(\beta<0\). Write
\[
q=-\beta>0
\]
and choose
\[
\varepsilon=\frac{\alpha-1}{2}>0.
\]

::: {.proof}
This choice satisfies
\[
\alpha-\varepsilon
=
\frac{\alpha+1}{2}
>
1.
\]
:::

<1>5. For all sufficiently large \(n\),
\[
\frac1{n^\alpha(\log n)^\beta}
=
\frac{(\log n)^q}{n^\alpha}
\le
\frac1{n^{\alpha-\varepsilon}}.
\]

::: {.proof}
By step <1>1,
\[
(\log n)^q\le n^\varepsilon
\]
eventually. Divide by \(n^\alpha\).
:::

<1>6. Hence the series converges for every
\[
\boxed{\alpha>1}
\]
regardless of \(\beta\).

::: {.proof}
The cases \(\beta\ge0\) and \(\beta<0\) are steps <1>3 and <1>5. In the
second case,
\[
\alpha-\varepsilon>1,
\]
so the comparison \(p\)-series converges.
:::

## Case \(\alpha<1\)

<1>7. Suppose \(\alpha<1\) and \(\beta\le0\). Then, for \(n\ge3\),
\[
\frac1{n^\alpha(\log n)^\beta}
\ge
\frac1{n^\alpha}.
\]

::: {.proof}
If \(\beta\le0\), then
\[
(\log n)^\beta\le1
\]
for \(n\ge3\). Dividing by a number at most \(1\) makes the term at least
\(n^{-\alpha}\).
:::

<1>8. Therefore the series diverges when
\[
\alpha<1,\qquad \beta\le0.
\]

::: {.proof}
The \(p\)-series
\[
\sum n^{-\alpha}
\]
diverges for \(\alpha\le1\). Apply step <1>7.
:::

<1>9. Suppose \(\alpha<1\) and \(\beta>0\). Choose
\[
\varepsilon=\frac{1-\alpha}{2}>0.
\]

::: {.proof}
Then
\[
\alpha+\varepsilon
=
\frac{\alpha+1}{2}
<
1.
\]
:::

<1>10. For all sufficiently large \(n\),
\[
(\log n)^\beta
\le
n^\varepsilon.
\]

::: {.proof}
Apply step <1>1 with
\[
q=\beta.
\]
:::

<1>11. Hence, eventually,
\[
\frac1{n^\alpha(\log n)^\beta}
\ge
\frac1{n^{\alpha+\varepsilon}}.
\]

::: {.proof}
Use step <1>10:
\[
n^\alpha(\log n)^\beta
\le
n^{\alpha+\varepsilon}.
\]
Taking reciprocals reverses the inequality.
:::

<1>12. Therefore the series diverges for every
\[
\boxed{\alpha<1}
\]
regardless of \(\beta\).

::: {.proof}
The case \(\beta\le0\) is step <1>8. If \(\beta>0\), step <1>11 compares
from below with the divergent \(p\)-series
\[
\sum\frac1{n^{\alpha+\varepsilon}},
\]
whose exponent satisfies
\[
\alpha+\varepsilon<1.
\]
:::

## Case \(\alpha=1\)

<1>13. Let
\[
f(x)=\frac1{x(\log x)^\beta},
\qquad x\ge2.
\]
For sufficiently large \(x\), \(f(x)\) is positive and decreasing.

::: {.proof}
Positivity is clear for \(x>1\). Differentiate:
\[
f'(x)
=
-\frac{(\log x)+\beta}
{x^2(\log x)^{\beta+1}}.
\]
For sufficiently large \(x\),
\[
\log x+\beta>0,
\]
so \(f'(x)<0\).
:::

<1>14. By the integral test,
\[
\sum_{n=2}^{\infty}
\frac1{n(\log n)^\beta}
\]
has the same convergence behavior as
\[
\int_2^\infty
\frac{dx}{x(\log x)^\beta}.
\]

::: {.proof}
Apply the integral test to the eventually positive decreasing function from
step <1>13. Finitely many initial terms do not affect convergence.
:::

<1>15. With
\[
u=\log x,
\]
the integral becomes
\[
\int_{\log2}^{\infty}
u^{-\beta}\,du.
\]

::: {.proof}
Since
\[
du=\frac{dx}{x},
\]
substitution gives
\[
\frac{dx}{x(\log x)^\beta}
=
u^{-\beta}\,du.
\]
:::

<1>16. The integral
\[
\int_{\log2}^{\infty}
u^{-\beta}\,du
\]
converges if and only if
\[
\boxed{\beta>1}.
\]

::: {.proof}
This is the \(p\)-integral
\[
\int_A^\infty u^{-p}\,du,
\]
which converges exactly when \(p>1\). Here \(p=\beta\).
:::

<1>17. Therefore, when
\[
\alpha=1,
\]
the series converges exactly for
\[
\boxed{\beta>1}
\]
and diverges for
\[
\boxed{\beta\le1}.
\]

::: {.proof}
Combine steps <1>14--<1>16.
:::

<1>18. Altogether,
\[
\boxed{
\sum_{n=2}^{\infty}
\frac1{n^\alpha(\log n)^\beta}
\text{ converges}
\iff
\left[
\alpha>1
\right]
\text{ or }
\left[
\alpha=1,\ \beta>1
\right].}
\]

::: {.proof}
Step <1>6 handles \(\alpha>1\), step <1>12 handles \(\alpha<1\), and step
<1>17 handles the boundary case \(\alpha=1\).
:::

<1>19. Equivalently, the series diverges exactly when
\[
\boxed{
\alpha<1
\quad\text{or}\quad
\alpha=1,\ \beta\le1}.
\]

::: {.proof}
This is the complementary parameter region to step <1>18.
:::

<1>20. Q.E.D.

::: {.proof}
Steps <1>18--<1>19 give the complete convergence/divergence classification.
:::
:::
