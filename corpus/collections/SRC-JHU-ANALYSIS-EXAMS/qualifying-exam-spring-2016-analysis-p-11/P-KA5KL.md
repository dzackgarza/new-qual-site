---
schema: qual/card@1
id: P-KA5KL
kind: problem
title: Bergman space is a Hilbert space
classification:
  areas:
  - complex-analysis
  topics:
  - Bergman Space
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the arbitrary open set, area norm and inner product with Spring 2016 problem 4 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the distinction between actual holomorphic functions and L2 classes, derived the compact point-evaluation bound, and used Fatou to identify the holomorphic limit with the L2 limit."
---

::: {.problem}
Let $U \subset \CC$ be an open set and

$$A^2(U) = \{ f \text{ holomorphic on } U : \int_U \abs{f(z)}^2 \, dx \, dy < \infty \}.$$

Define

$$\langle f, g \rangle = \int_U f(z) \overline{g(z)} \, dx \, dy, \quad \forall f, g \in A^2(U).$$

Prove that $A^2(U)$ is a Hilbert space when equipped with this inner product.
:::

::: {.solution}
Write $dA=dx\,dy$ and $\norm{f}_2^2=\int_U\abs{f}^2\,dA$.

::: pf

::: pf-step

The formula defines an inner product on the vector space $A^2(U)$.

::: pf-proof

Linear combinations of holomorphic functions are holomorphic,
and
$\abs{af+bg}^2\leq2\abs{a}^2\abs{f}^2+2\abs{b}^2\abs{g}^2$
shows that they remain square integrable. Cauchy–Schwarz
gives $\int_U\abs{f\overline g}\,dA\leq\norm{f}_2\norm{g}_2$,
so the inner product is well defined [@Fol13]. Linearity
in the first variable and conjugate symmetry follow from
the integral.

If a holomorphic $f$ is nonzero at $a\in U$, continuity
gives a disk of positive area on which $\abs{f}\geq\abs{f(a)}/2$.
Then $\norm{f}_2>0$. Hence $\norm{f}_2=0$ implies $f(a)=0$ at
every $a\in U$, which is positive definiteness.

:::

:::

::: {.pf-step #s2}

Every compact subset has an $L^2$ point-evaluation bound.

::: pf-proof

For $\overline{D(a,r)}\subset U$, Cauchy's circle formula
and Cauchy–Schwarz imply, for $0<\rho<r$,
$$
\abs{f(a)}^2\leq\frac1{2\pi}\int_0^{2\pi}\abs{f(a+\rho e^{it})}^2\,dt
$$
[@SS03; @Fol13]. Integrating this inequality against
$2\pi\rho\,d\rho$ yields
$\pi r^2\abs{f(a)}^2\leq\int_{D(a,r)}\abs{f}^2\,dA$.
For a nonempty compact $K\subset U$, compactness and
openness give a single $r>0$ with these closed disks
contained in $U$ for every $a\in K$. Thus
$$
\sup_{a\in K}\abs{f(a)}\leq\frac1{\sqrt\pi r}\norm{f}_2.
$$
The same estimate holds for differences of functions in $A^2(U)$.

:::

:::

::: pf-step

The inner-product space is complete.

::: pf-proof

Let $(f_n)$ be Cauchy in this norm. Completeness of
$L^2(U)$ gives an $L^2$ limit $F$, regarded as a measurable
representative of its almost-everywhere class [@Fol13].
Step [](#s2){.pf-ref} makes $(f_n)$ uniformly Cauchy on every compact
subset of $U$. Pointwise completeness of $\CC$ and
that same estimate give a locally uniform limit $f$.
This limit is holomorphic by the local uniform limit
theorem [@SS03].

At almost every point where $F$ is finite, $f_n\to f$.
Fatou's lemma therefore gives
$$
\int_U\abs{f-F}^2\,dA
\leq\liminf_{n\to\infty}\int_U\abs{f_n-F}^2\,dA=0
$$
[@Fol13]. Hence $f=F$ almost everywhere. It follows that
$f\in A^2(U)$ and $\norm{f_n-f}_2=\norm{f_n-F}_2\to0$.
Thus every Cauchy sequence converges in $A^2(U)$, proving
that it is a Hilbert space.

:::

:::

:::

:::
