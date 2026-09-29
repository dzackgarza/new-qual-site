---
schema: qual/card@1
id: P-AZOFF-E10
kind: problem
title: Uniform convergence of $\sum\sin(nz)/2^n$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Liouville, FTA, and power series, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Liouville, FTA, and power series, Problem 10, of Azoff Problems by Topic.pdf, which reads Im z < ln 2; added an erratum remark with a counterexample and the corrected region.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    The retained PDF really asks for uniform convergence on Im z < ln 2,
    which is false; for example the terms do not tend to zero at z=-2i.
    The problem now asks for uniform convergence on every closed substrip
    |Im z|<=c with 0<=c<ln 2, and hence local uniform convergence on the
    maximal open strip |Im z|<ln 2.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    On |Im z|<=c, the exponential formula for sine gives
    |sin(nz)|<=e^(nc), so the nth summand is bounded by
    (e^c/2)^n. Since e^c/2<1, the Weierstrass M-test gives uniform
    convergence; compact subsets of the open strip lie in such a substrip.
---

::: {.problem}
For every real number $c$ with $0\leq c<\ln 2$, prove that the series
$$
\sum_{n=1}^\infty \frac{\sin(nz)}{2^n}
$$
converges uniformly on
$$
\{z:\abs{\operatorname{Im}z}\leq c\}.
$$
Deduce that the series converges locally uniformly on
$$
\{z:\abs{\operatorname{Im}z}<\ln2\}.
$$
:::

::: {.solution}
Fix $c$ with
$$
0\leq c<\ln2
$$
and set
$$
q=\frac{e^c}{2}.
$$
Then $0<q<1$.

::: pf

::: {.pf-step #s1}

If $\abs{\operatorname{Im}z}\leq c$, then for every integer
$n\geq1$,
$$
\abs{\sin(nz)}\leq e^{nc}.
$$

::: pf-proof

Write $z=x+iy$. Using
$$
\sin(nz)
=
\frac{e^{inz}-e^{-inz}}{2i},
$$
one has
$$
\abs{e^{inz}}=e^{-ny},
\qquad
\abs{e^{-inz}}=e^{ny}.
$$
Hence
$$
\begin{aligned}
\abs{\sin(nz)}
&\leq
\frac{e^{-ny}+e^{ny}}2\\
&=
\cosh(ny)\\
&\leq
e^{n\abs{y}}\\
&\leq
e^{nc}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The series converges uniformly on
$$
\{z:\abs{\operatorname{Im}z}\leq c\}.
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
\abs{\frac{\sin(nz)}{2^n}}
\leq
\left(\frac{e^c}{2}\right)^n
=
q^n
$$
throughout the closed strip. Since $0<q<1$, the numerical geometric series
$$
\sum_{n=1}^{\infty}q^n
$$
converges. The Weierstrass M-test therefore gives uniform convergence on the
closed strip.

:::

:::

::: {.pf-step #s3}

The series converges locally uniformly on
$$
S=\{z:\abs{\operatorname{Im}z}<\ln2\}.
$$

::: pf-proof

Let $K\subseteq S$ be compact. The continuous function
$z\mapsto\abs{\operatorname{Im}z}$ attains a maximum $c_K$ on $K$.
Because $K\subseteq S$,
$$
c_K<\ln2.
$$
Set
$$
c=\frac{c_K+\ln2}{2}.
$$
Then
$$
c_K<c<\ln2,
$$
and
$$
K\subseteq\{z:\abs{\operatorname{Im}z}\leq c\},
$$
so step [](#s2){.pf-ref} gives uniform convergence on the larger closed strip, hence on
$K$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves the corrected uniform-convergence statement for every
closed substrip, and step [](#s3){.pf-ref} gives the stated local uniform convergence.

:::

:::

:::

::: {.remark}
Erratum: the statement is false as written in the source.
For $z = iy$ we have $\abs{\sin(nz)} = \sinh(n\abs{y})$, so at $z = -2i$ the terms have modulus $\sinh(2n)/2^n \to \infty$ and the series diverges, although $\operatorname{Im}(-2i) < \ln 2$.
Even on the strip $\{\abs{\operatorname{Im} z} < \ln 2\}$, where the series converges, the convergence is not uniform: at $z = iy$ with $0 < y < \ln 2$ the terms are $i\sinh(ny)/2^n$, with $\sinh(ny)/2^n \ge (e^{y}/2)^n/4$ for $ny \ge 1$, and $e^y/2 \to 1$ as $y \to \ln 2$, so no tail is uniformly small.
The correct statement is that the series converges uniformly on $\{z : \abs{\operatorname{Im} z} \le c\}$ for each $0\le c < \ln 2$, hence locally uniformly on $\{z : \abs{\operatorname{Im} z} < \ln 2\}$.
:::
