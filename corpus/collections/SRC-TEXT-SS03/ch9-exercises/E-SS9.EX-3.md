---
schema: qual/card@1
id: E-SS9.EX-3
kind: problem
title: $\sum_{\omega\in\Lambda^*}\abs\omega^{-2}$ diverges
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Lattices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps: the comparison of each lattice point's contribution
    with the integral over its unit square by the mean-value theorem, the summation of the errors
    against the convergent series of |p|^{-3}, the identification of the union of squares with the
    annulus up to an inner region and an outer annulus of width O(1), the polar computation giving
    2 pi log R, and the transport to a general tau through the two-sided comparison supplied by the
    real-linear isomorphism (m,n) -> n + m tau. Supplied the point the prose left implicit: that the
    comparison goes both ways, so divergence of the square-lattice sum implies divergence of the
    tau-lattice sum. Not checked this session: the printed statement page.

---

::: {.exercise}
In contrast with the result in Lemma 1.5, prove that the series
$$
\sum_{n + m\tau \in \Lambda^*} \frac{1}{\abs{n + m\tau}^2} \quad \text{where } \tau \in \halfplane
$$
does not converge. In fact, show that
$$
\sum_{1 \leq n^2 + m^2 \leq R^2} 1/(n^2 + m^2) = 2\pi\log R + O(1) \quad \text{as } R \to \infty.
$$
:::

::: {.solution}

The argument is the card's own; the statement is the exercise stored on the card, and no source text or solution set is retained for it.

For $p=(m,n)\in\ZZ^{2}\setminus\{0\}$ let $Q_{p}=p+[-\tfrac12,\tfrac12]^{2}$ be the unit square centred at $p$, and write $\norm{\cdot}$ for the euclidean norm on $\RR^{2}$.

::: pf

::: {.pf-step #square-estimate}
For $\norm{p}\geq2$ and $x\in Q_{p}$, $\abs{\norm{x}^{-2}-\norm{p}^{-2}}\leq C\norm{p}^{-3}$ with an absolute constant $C$.

::: pf-proof
On $Q_{p}$ we have $\norm{x}\geq\norm{p}-\tfrac12\sqrt2\geq\norm{p}/2\geq1$, so the segment from $x$ to $p$ stays away from the origin and the mean value theorem applies to $r\mapsto r^{-2}$ along it: the difference is at most $\sup_{\xi}\abs{\nabla\norm{\xi}^{-2}}\cdot\norm{x-p}\leq 2\sup_{\xi}\norm{\xi}^{-3}\cdot\tfrac12\sqrt2$, the sup being over points $\xi$ between $x$ and $p$, where $\norm{\xi}\geq\norm{p}/2$. Hence the bound with $C=2\sqrt2$.
:::

:::

::: {.pf-step #integral}
$\int_{Q_{p}}\norm{x}^{-2}dx=\norm{p}^{-2}+O(\norm{p}^{-3})$, and the sum of the error terms over $p$ with $1\leq\norm{p}\leq R$ is bounded independently of $R$.

::: pf-proof
The square has area $1$, so integrating the constant $\norm{p}^{-2}$ over it gives $\norm{p}^{-2}$, and step [](#square-estimate){.pf-ref} bounds the remainder by $C\norm{p}^{-3}$. Summing over $p\neq0$, $\sum_{p\neq0}\norm{p}^{-3}<\infty$ by comparison with $\int_{1}^{\infty}r^{-3}\,r\,dr$, so the total error over any set of $p$ is bounded by the full sum.
:::

:::

::: {.pf-step #annulus}
$\sum_{1\leq\norm{p}\leq R}\norm{p}^{-2}=\int_{1\leq\norm{x}\leq R}\norm{x}^{-2}dx+O(1)$.

::: pf-proof
The union $U_{R}$ of the squares $Q_{p}$ with $1\leq\norm{p}\leq R$ differs from the annulus $A_{R}=\{1\leq\norm{x}\leq R\}$ only inside a fixed bounded region near the origin and inside the annulus $\{R-\sqrt2\leq\norm{x}\leq R+\sqrt2\}$ of width $2\sqrt2$. On the outer annulus $\norm{x}^{-2}\leq(R-\sqrt2)^{-2}$ and the area is $O(R)$, so its integral is $O(1/(R-\sqrt2))\to0$; the inner region contributes a constant. Summing step [](#integral){.pf-ref} over the $p$ in the annulus with the bounded error of that step gives the assertion.
:::

:::

::: {.pf-step #polar}
$\int_{1\leq\norm{x}\leq R}\norm{x}^{-2}dx=2\pi\log R$.

::: pf-proof
In polar coordinates $x=re^{i\theta}$ with Jacobian $r$,
$$
\int_{1\leq\norm{x}\leq R}\frac{dx}{\norm{x}^{2}}=\int_{0}^{2\pi}\!\!\int_{1}^{R}\frac{1}{r^{2}}\,r\,dr\,d\theta=2\pi\int_{1}^{R}\frac{dr}{r}=2\pi\log R.
$$
:::

:::

::: {.pf-step #asymptotic}
$\sum_{1\leq m^{2}+n^{2}\leq R^{2}}\frac{1}{m^{2}+n^{2}}=2\pi\log R+O(1)$.

::: pf-proof
This is steps [](#annulus){.pf-ref} and [](#polar){.pf-ref} combined, the condition $1\leq\norm{p}\leq R$ being $1\leq m^{2}+n^{2}\leq R^{2}$.
:::

:::

::: {.pf-step #tau}
For $\tau=u+it$ with $t>0$ the series $\sum_{n+m\tau\in\Lambda^{*}}\abs{n+m\tau}^{-2}$ diverges.

::: pf-proof
The map $\varphi(m,n)=n+m\tau$ is real-linear and injective, its imaginary part being $mt$ with $t>0$, so it is a bijection $\RR^{2}\to\CC$ and carries $\ZZ^{2}\setminus\{0\}$ onto $\Lambda^{*}$. A real-linear isomorphism has two-sided bounds: there is $c>0$ with $\abs{n+m\tau}\geq c\sqrt{m^{2}+n^{2}}$, the constant being that of the inverse map, as well as $\abs{n+m\tau}\leq C\sqrt{m^{2}+n^{2}}$. Hence
$$
\frac{1}{\abs{n+m\tau}^{2}}\geq\frac{1}{C^{2}(m^{2}+n^{2})},
$$
and summing over $1\leq m^{2}+n^{2}\leq R^{2}$ gives a lower bound $\frac{1}{C^{2}}\bigl(2\pi\log R+O(1)\bigr)\to\infty$ by step [](#asymptotic){.pf-ref}. So the partial sums are unbounded and the series diverges.
:::

:::

:::

:::
