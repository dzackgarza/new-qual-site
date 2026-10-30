---
schema: qual/card@1
id: P-UCLARA16F-09
kind: problem
title: Fourier--Laplace transforms of probability measures on $[0,1]$ with polynomial growth
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Zeros
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $\mu$ be a positive Borel measure on $[0,1]$ with $\mu([0,1])=1$.

(a) Show that the function
$$
f(z)=\int_{[0,1]}e^{izt}\,d\mu(t)
$$
is holomorphic on $\CC$.

(b) Suppose that there exists $n\in\NN$ such that
$$
\limsup_{\abs{z}\to\infty}\frac{\abs{f(z)}}{\abs{z}^n}<\infty.
$$
Show that then $\mu$ is equal to the Dirac measure $\delta_0$ at $0$.
:::

::: {.solution}

## Part (a)

For every $k\ge0$, define the moment
$$
m_k
=
\int_{[0,1]}t^k\,d\mu(t).
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\boxed{0\le m_k\le1}.
$$


::: pf-proof

Since $0\le t\le1$,
$$
0\le t^k\le1.
$$
Integrating against the probability measure $\mu$ gives
$$
0\le m_k\le\mu([0,1])=1.
$$

:::

:::

::: {.pf-step #s1-2}

For fixed $z\in\CC$,
$$
e^{izt}
=
\sum_{k=0}^{\infty}
\frac{(izt)^k}{k!}
$$
uniformly for $t\in[0,1]$.


::: pf-proof

For $t\in[0,1]$,
$$
\abs{
\frac{(izt)^k}{k!}
}
\le
\frac{\abs{z}^k}{k!},
$$
and
$$
\sum_{k=0}^{\infty}
\frac{\abs{z}^k}{k!}
=
e^{\abs{z}}<\infty.
$$
Apply the Weierstrass $M$-test.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
f(z)
=
\sum_{k=0}^{\infty}
\frac{i^k m_k}{k!}z^k}.
$$


::: pf-proof

Integrate the uniformly convergent series from step [](#s1-2){.pf-ref} term by term:
$$
\begin{aligned}
f(z)
&=
\int
\sum_{k=0}^{\infty}
\frac{(izt)^k}{k!}\,d\mu(t)\\
&=
\sum_{k=0}^{\infty}
\frac{(iz)^k}{k!}
\int t^k\,d\mu(t).
\end{aligned}
$$

:::

:::

::: pf-step

The series in step [](#s1-3){.pf-ref} has infinite radius of convergence.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\abs{
\frac{i^k m_k}{k!}z^k
}
\le
\frac{\abs{z}^k}{k!},
$$
and the exponential series converges for every $z\in\CC$.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
f\text{ is entire}.}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} represents $f$ by a power series with infinite radius of convergence.

:::

:::

::: {.pf-step #s1-6}

There exist constants $C>0$ and $R_0>0$ such that
$$
\boxed{
\abs{f(z)}
\le
C\abs{z}^n}
$$
whenever $\abs{z}\ge R_0$.


::: pf-proof

This is the definition of finiteness of the stated limsup.

:::

:::

::: {.pf-step #s1-7}

There is a constant $C_1>0$ such that for every $R\ge1$,
$$
\boxed{
\max_{\abs{z}=R}\abs{f(z)}
\le
C_1R^n}.
$$


::: pf-proof

For $R\ge R_0$, use step [](#s1-6){.pf-ref}. For $1\le R\le R_0$, continuity of $f$ on the compact disk $\abs{z}\le R_0$ gives a finite maximum; enlarge $C_1$ to absorb this bounded range.

:::

:::

::: {.pf-step #s1-8}

For every integer $m>n$, Cauchy's estimate gives
$$
\abs{f^{(m)}(0)}
\le
\frac{m!}{R^m}
\max_{\abs{z}=R}\abs{f(z)}.
$$


::: pf-proof

Apply Cauchy's estimate to the entire function $f$ on the circle $\abs{z}=R$.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\abs{f^{(m)}(0)}
\le
m!C_1R^{n-m}
$$
for every $R\ge1$.


::: pf-proof

Substitute step [](#s1-7){.pf-ref} into step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Letting $R\to\infty$,
$$
\boxed{
f^{(m)}(0)=0}
$$
for every $m>n$.


::: pf-proof

Since $m>n$,
$$
R^{n-m}\to0.
$$
The left-hand side of step [](#s1-9){.pf-ref} is independent of $R$, so it must vanish.

:::

:::

::: pf-step

Hence $f$ is a polynomial of degree at most $n$.


::: pf-proof

All Taylor coefficients of degree $>n$ vanish by step [](#s1-10){.pf-ref}, and $f$ is entire.

:::

:::

::: {.pf-step #s1-12}

For every real $x$,
$$
\boxed{\abs{f(x)}\le1}.
$$


::: pf-proof

Since $\abs{e^{ixt}}=1$,
$$
\begin{aligned}
\abs{f(x)}
&=
\abs{
\int e^{ixt}\,d\mu(t)
}\\
&\le
\int \abs{e^{ixt}}\,d\mu(t)\\
&=
\mu([0,1])\\
&=
1.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-13}

Therefore $f$ is constant.


::: pf-proof

A nonconstant polynomial is unbounded on the real axis as $\abs{x}\to\infty$. Step [](#s1-12){.pf-ref} says $f$ is bounded on $\RR$.

:::

:::

::: {.pf-step #s1-14}

Since
$$
f(0)=1,
$$
one has
$$
\boxed{f\equiv1}.
$$


::: pf-proof

$$
f(0)
=
\int 1\,d\mu
=
\mu([0,1])
=
1.
$$
Combine with step [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

Differentiating the power series at $0$,
$$
\boxed{
f'(0)
=
i\int_{[0,1]}t\,d\mu(t)}.
$$


::: pf-proof

From step [](#s1-3){.pf-ref}, the coefficient of $z$ is
$$
im_1
=
i\int t\,d\mu.
$$

:::

:::

::: pf-step

Since $f\equiv1$,
$$
\boxed{
\int_{[0,1]}t\,d\mu(t)=0}.
$$


::: pf-proof

Step [](#s1-14){.pf-ref} gives
$$
f'(0)=0.
$$
Use step [](#s1-15){.pf-ref} and divide by $i$.

:::

:::

::: {.pf-step #s1-17}

For every $\varepsilon>0$,
$$
\boxed{
\mu([\varepsilon,1])=0}.
$$


::: pf-proof

Since $t\ge\varepsilon$ on $[\varepsilon,1]$,
$$
0
=
\int_0^1 t\,d\mu(t)
\ge
\int_{[\varepsilon,1]}t\,d\mu(t)
\ge
\varepsilon\,\mu([\varepsilon,1]).
$$
Thus the measure must vanish there.

:::

:::

::: {.pf-step #s1-18}

Therefore
$$
\boxed{
\mu((0,1])=0}.
$$


::: pf-proof

Since
$$
(0,1]
=
\bigcup_{m=1}^{\infty}
[1/m,1],
$$
and each set in the union has measure zero by step [](#s1-17){.pf-ref}, countable subadditivity gives zero measure to the union.

:::

:::

::: pf-step

Since $\mu([0,1])=1$,
$$
\boxed{
\mu(\{0\})=1}.
$$


::: pf-proof

The complement of $\{0\}$ in $[0,1]$ is $(0,1]$, which has measure zero by step [](#s1-18){.pf-ref}.

:::

:::

::: {.pf-step #s1-20}

Hence
$$
\boxed{
\mu=\delta_0}.
$$


::: pf-proof

A probability measure concentrated entirely at $0$ is the Dirac measure at $0$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (a), and step [](#s1-20){.pf-ref} proves part (b).

:::

:::

:::
