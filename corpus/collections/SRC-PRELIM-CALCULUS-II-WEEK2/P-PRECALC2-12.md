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
For what values of $\alpha , \beta \in \RR$ does the series

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

::: pf

::: {.pf-step #s1-1}

For every \(q>0\) and every \(\varepsilon>0\),
\[
\boxed{
(\log n)^q
\le
n^\varepsilon}
\]
for all sufficiently large \(n\).


::: pf-proof

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

:::

::: {.pf-step #s1-2}

Suppose \(\alpha>1\) and \(\beta\ge0\). Then, for \(n\ge3\),
\[
\frac1{n^\alpha(\log n)^\beta}
\le
\frac1{n^\alpha}.
\]


::: pf-proof

For \(n\ge3\),
\[
\log n>1,
\]
so
\[
(\log n)^\beta\ge1.
\]

:::

:::

::: {.pf-step #s1-3}

Therefore the series converges when
\[
\alpha>1,\qquad \beta\ge0.
\]


::: pf-proof

The comparison series
\[
\sum\frac1{n^\alpha}
\]
converges because \(\alpha>1\). Apply step [](#s1-2){.pf-ref}.

:::

:::

::: pf-step

Suppose \(\alpha>1\) and \(\beta<0\). Write
\[
q=-\beta>0
\]
and choose
\[
\varepsilon=\frac{\alpha-1}{2}>0.
\]


::: pf-proof

This choice satisfies
\[
\alpha-\varepsilon
=
\frac{\alpha+1}{2}
>
1.
\]

:::

:::

::: {.pf-step #s1-5}

For all sufficiently large \(n\),
\[
\frac1{n^\alpha(\log n)^\beta}
=
\frac{(\log n)^q}{n^\alpha}
\le
\frac1{n^{\alpha-\varepsilon}}.
\]


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
(\log n)^q\le n^\varepsilon
\]
eventually. Divide by \(n^\alpha\).

:::

:::

::: {.pf-step #s1-6}

Hence the series converges for every
\[
\boxed{\alpha>1}
\]
regardless of \(\beta\).


::: pf-proof

The cases \(\beta\ge0\) and \(\beta<0\) are steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref}. In the
second case,
\[
\alpha-\varepsilon>1,
\]
so the comparison \(p\)-series converges.

:::

:::

::: {.pf-step #s1-7}

Suppose \(\alpha<1\) and \(\beta\le0\). Then, for \(n\ge3\),
\[
\frac1{n^\alpha(\log n)^\beta}
\ge
\frac1{n^\alpha}.
\]


::: pf-proof

If \(\beta\le0\), then
\[
(\log n)^\beta\le1
\]
for \(n\ge3\). Dividing by a number at most \(1\) makes the term at least
\(n^{-\alpha}\).

:::

:::

::: {.pf-step #s1-8}

Therefore the series diverges when
\[
\alpha<1,\qquad \beta\le0.
\]


::: pf-proof

The \(p\)-series
\[
\sum n^{-\alpha}
\]
diverges for \(\alpha\le1\). Apply step [](#s1-7){.pf-ref}.

:::

:::

::: pf-step

Suppose \(\alpha<1\) and \(\beta>0\). Choose
\[
\varepsilon=\frac{1-\alpha}{2}>0.
\]


::: pf-proof

Then
\[
\alpha+\varepsilon
=
\frac{\alpha+1}{2}
<
1.
\]

:::

:::

::: {.pf-step #s1-10}

For all sufficiently large \(n\),
\[
(\log n)^\beta
\le
n^\varepsilon.
\]


::: pf-proof

Apply step [](#s1-1){.pf-ref} with
\[
q=\beta.
\]

:::

:::

::: {.pf-step #s1-11}

Hence, eventually,
\[
\frac1{n^\alpha(\log n)^\beta}
\ge
\frac1{n^{\alpha+\varepsilon}}.
\]


::: pf-proof

Use step [](#s1-10){.pf-ref}:
\[
n^\alpha(\log n)^\beta
\le
n^{\alpha+\varepsilon}.
\]
Taking reciprocals reverses the inequality.

:::

:::

::: {.pf-step #s1-12}

Therefore the series diverges for every
\[
\boxed{\alpha<1}
\]
regardless of \(\beta\).


::: pf-proof

The case \(\beta\le0\) is step [](#s1-8){.pf-ref}. If \(\beta>0\), step [](#s1-11){.pf-ref} compares
from below with the divergent \(p\)-series
\[
\sum\frac1{n^{\alpha+\varepsilon}},
\]
whose exponent satisfies
\[
\alpha+\varepsilon<1.
\]

:::

:::

::: {.pf-step #s1-13}

Let
\[
f(x)=\frac1{x(\log x)^\beta},
\qquad x\ge2.
\]
For sufficiently large \(x\), \(f(x)\) is positive and decreasing.


::: pf-proof

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

:::

::: {.pf-step #s1-14}

By the integral test,
\[
\sum_{n=2}^{\infty}
\frac1{n(\log n)^\beta}
\]
has the same convergence behavior as
\[
\int_2^\infty
\frac{dx}{x(\log x)^\beta}.
\]


::: pf-proof

Apply the integral test to the eventually positive decreasing function from
step [](#s1-13){.pf-ref}. Finitely many initial terms do not affect convergence.

:::

:::

::: {.pf-step #s1-15}

With
\[
u=\log x,
\]
the integral becomes
\[
\int_{\log2}^{\infty}
u^{-\beta}\,du.
\]


::: pf-proof

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

:::

::: {.pf-step #s1-16}

The integral
\[
\int_{\log2}^{\infty}
u^{-\beta}\,du
\]
converges if and only if
\[
\boxed{\beta>1}.
\]


::: pf-proof

This is the \(p\)-integral
\[
\int_A^\infty u^{-p}\,du,
\]
which converges exactly when \(p>1\). Here \(p=\beta\).

:::

:::

::: {.pf-step #s1-17}

Therefore, when
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


::: pf-proof

Combine steps [](#s1-14){.pf-ref} through [](#s1-16){.pf-ref}.

:::

:::

::: {.pf-step #s1-18}

Altogether,
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


::: pf-proof

Step [](#s1-6){.pf-ref} handles \(\alpha>1\), step [](#s1-12){.pf-ref} handles \(\alpha<1\), and step
[](#s1-17){.pf-ref} handles the boundary case \(\alpha=1\).

:::

:::

::: {.pf-step #s1-19}

Equivalently, the series diverges exactly when
\[
\boxed{
\alpha<1
\quad\text{or}\quad
\alpha=1,\ \beta\le1}.
\]


::: pf-proof

This is the complementary parameter region to step [](#s1-18){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-18){.pf-ref} through [](#s1-19){.pf-ref} give the complete convergence/divergence classification.

:::

:::

:::
