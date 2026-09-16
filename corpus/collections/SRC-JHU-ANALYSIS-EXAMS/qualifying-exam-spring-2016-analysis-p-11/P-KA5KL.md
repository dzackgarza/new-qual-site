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
Let $U \subset \mathbb{C}$ be an open set and

$$A^2(U) = \{ f \text{ holomorphic on } U : \int_U |f(z)|^2 \, dx \, dy < \infty \}.$$

Define

$$\langle f, g \rangle = \int_U f(z) \overline{g(z)} \, dx \, dy, \quad \forall f, g \in A^2(U).$$

Prove that $A^2(U)$ is a Hilbert space when equipped with this inner product.
:::

::: solution
Write $dA=dx\,dy$ and $\|f\|_2^2=\int_U|f|^2\,dA$.

<1>1. The formula defines an inner product on the vector space $A^2(U)$.

::: proof
Linear combinations of holomorphic functions are holomorphic,
and
$|af+bg|^2\leq2|a|^2|f|^2+2|b|^2|g|^2$
shows that they remain square integrable. Cauchy–Schwarz
gives $\int_U|f\overline g|\,dA\leq\|f\|_2\|g\|_2$,
so the inner product is well defined [@Fol13]. Linearity
in the first variable and conjugate symmetry follow from
the integral.

If a holomorphic $f$ is nonzero at $a\in U$, continuity
gives a disk of positive area on which $|f|\geq|f(a)|/2$.
Then $\|f\|_2>0$. Hence zero norm implies $f=0$ everywhere,
not just almost everywhere. This proves positive definiteness
for the actual functions in $A^2(U)$.
:::

<1>2. Every compact subset has an $L^2$ point-evaluation bound.

::: proof
For $\overline{D(a,r)}\subset U$, Cauchy's circle formula
and Cauchy–Schwarz imply, for $0<\rho<r$,
$$
|f(a)|^2\leq\frac1{2\pi}\int_0^{2\pi}|f(a+\rho e^{it})|^2\,dt
$$
[@SS03; @Fol13]. Integrating this inequality against
$2\pi\rho\,d\rho$ yields
$\pi r^2|f(a)|^2\leq\int_{D(a,r)}|f|^2\,dA$.
For a nonempty compact $K\subset U$, compactness and
openness give a single $r>0$ with these closed disks
contained in $U$ for every $a\in K$. Thus
$$
\sup_{a\in K}|f(a)|\leq\frac1{\sqrt\pi r}\|f\|_2.
$$
The same estimate holds for differences of functions in $A^2(U)$.
:::

<1>3. The inner-product space is complete.

::: proof
Let $(f_n)$ be Cauchy in this norm. Completeness of
$L^2(U)$ gives an $L^2$ limit $F$, regarded as a measurable
representative of its almost-everywhere class [@Fol13].
Step <1>2 makes $(f_n)$ uniformly Cauchy on every compact
subset of $U$. Pointwise completeness of $\mathbb C$ and
that same estimate give a locally uniform limit $f$.
This limit is holomorphic by the local uniform limit
theorem [@SS03].

At almost every point where $F$ is finite, $f_n\to f$.
Fatou's lemma therefore gives
$$
\int_U|f-F|^2\,dA
\leq\liminf_{n\to\infty}\int_U|f_n-F|^2\,dA=0
$$
[@Fol13]. Hence $f=F$ almost everywhere. It follows that
$f\in A^2(U)$ and $\|f_n-f\|_2=\|f_n-F\|_2\to0$.
Thus every Cauchy sequence converges in $A^2(U)$, proving
that it is a Hilbert space. If $U$ is empty, $A^2(U)$
is the zero vector space, which has the same conclusion.
No connectedness or boundedness of $U$ is needed.
:::
:::
