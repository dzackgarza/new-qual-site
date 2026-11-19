---
schema: qual/card@1
id: P-CASP26D
kind: problem
title: "Holomorphic function on the upper half-plane with real boundary values and polynomial growth is a Laurent polynomial"
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Boundary Values
  - Reflection Principle
  - Growth Estimates
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked: the reflection is legitimate
    because f is continuous up to each open interval of R minus 0 and real there, so Schwarz
    reflection applies on each interval and the pieces glue; the reflected function inherits the
    bound since |f(conj z)| <= |z|^N + |z|^{-N}. Cauchy's estimate on |z| = r gives
    |a_k| <= (r^N + r^{-N}) r^{-k}, which tends to 0 as r -> infinity when k > N (both exponents
    negative) and as r -> 0 when k < -N (both positive), so the Laurent series is finite in both
    directions; and comparing F(z) = conj F(conj z) coefficient by coefficient in the variable
    conj z gives a_k = conj(a_k). The prose asserted the last two points without their estimates;
    both are now steps. Statement unchanged; the card says the argument is its own.
---

::: {.problem}
Let $f$ be holomorphic on the upper half-plane $H = \{z \in \CC : \operatorname{Im} z > 0\}$.
Assume that

(i) $f$ extends continuously to $\overline{H} \setminus \{0\}$,

(ii) $f(x) \in \RR$ for all $x \in \RR \setminus \{0\}$,

(iii) there exists an integer $N > 0$ such that $\abs{f(z)} \leq \abs{z}^N + \abs{z}^{-N}$ for all $z \in H$.

Prove that there are constants $a_k \in \RR$ such that $f(z) = \sum_{k=-N}^{N} a_k z^k$.
:::

::: {.solution}
Reflect across the real axis: since $f$ is continuous up to $\RR\setminus\{0\}$ and real there, the Schwarz reflection principle gives a holomorphic $F$ on $\CC\setminus\{0\}$ agreeing with $f$ on $H$ and satisfying $F(\bar z)=\overline{F(z)}$ and the same growth bound. Cauchy's estimate on the circle $\abs z=r$ bounds the Laurent coefficient $a_k$ by $(r^N+r^{-N})r^{-k}$, which vanishes as $r\to\infty$ for $k>N$ and as $r\to0$ for $k<-N$, so all but $N$ terms on each side vanish; the reflection symmetry then makes the remaining coefficients real. The argument is this card's own: no retained solution set covers this exam.

::: pf

::: {.pf-step #reflect}
There is a holomorphic $F\colon\CC\setminus\{0\}\to\CC$ with $F=f$ on $H$, $F(\bar z)=\overline{F(z)}$ for all $z\ne0$, and $\abs{F(z)}\le\abs z^N+\abs z^{-N}$ on $\CC\setminus\{0\}$.

::: pf-proof
On each open interval of $\RR\setminus\{0\}$ the function $f$ is continuous up to the interval and real-valued there, so the Schwarz reflection principle extends $f$ holomorphically across it; the extensions from the upper half-plane glue to a holomorphic function on a neighbourhood of $\RR\setminus\{0\}$ in $\CC\setminus\{0\}$. Define $F(z)=f(z)$ for $\Im z>0$ and $F(z)=\overline{f(\bar z)}$ for $\Im z<0$. On the real axis minus $0$ the two prescriptions agree, since $f$ is real there, so $F$ is holomorphic on $\CC\setminus\{0\}$. The symmetry $F(\bar z)=\overline{F(z)}$ holds in each half-plane by construction and on the axis by reality. The bound passes to the reflection because $\abs{\overline{f(\bar z)}}=\abs{f(\bar z)}\le\abs{\bar z}^N+\abs{\bar z}^{-N}=\abs z^N+\abs z^{-N}$.
:::

:::


::: {.pf-step #laurent}
$F$ has a Laurent expansion $F(z)=\sum_{k\in\ZZ}a_kz^k$ on $\CC\setminus\{0\}$, and for every $r>0$ its coefficients satisfy $\abs{a_k}\le(r^N+r^{-N})r^{-k}$.

::: pf-proof
$F$ is holomorphic on the annulus $0<\abs z<\infty$, so it has a Laurent expansion there with $a_k=\dfrac1{2\pi i}\oint_{\abs z=r}F(z)z^{-k-1}\dz$ for every $r>0$; the Laurent expansion about $0$ in an annulus containing the circle gives the same coefficients in every such annulus. Estimating the integral by the maximum of the integrand on $\abs z=r$ gives $\abs{a_k}\le r^{-k}\max_{\abs z=r}\abs{F}\le r^{-k}(r^N+r^{-N})$ by step [](#reflect){.pf-ref}.
:::

:::


::: {.pf-step #tails}
$a_k=0$ for $\abs k>N$.

::: pf-proof
Let $k>N$. The bound of step [](#laurent){.pf-ref} reads $\abs{a_k}\le r^{N-k}+r^{-N-k}$ with both exponents negative, so the right side tends to $0$ as $r\to\infty$; the left side does not depend on $r$, hence $a_k=0$. Let $k<-N$. The same bound reads $\abs{a_k}\le r^{N-k}+r^{-N-k}$ with both exponents positive, so the right side tends to $0$ as $r\to0$; hence $a_k=0$ again.
:::

:::


::: {.pf-step #poly}
$F(z)=\sum_{k=-N}^{N}a_kz^k$ for every $z\ne0$.

::: pf-proof
By step [](#tails){.pf-ref} the Laurent series of step [](#laurent){.pf-ref} has finitely many nonzero terms, all with $\abs k\le N$; a Laurent series with finitely many terms equals its sum as a finite sum at every point of the annulus, so the identity holds on $\CC\setminus\{0\}$.
:::

:::


::: {.pf-step #real}
$a_k\in\RR$ for every $k$.

::: pf-proof
By steps [](#poly){.pf-ref} and [](#reflect){.pf-ref}, for $z\ne0$,
$$
\sum_{k=-N}^{N}\overline{a_k}\,\overline{z}^{k}=\overline{F(z)}=F(\bar z)=\sum_{k=-N}^{N}a_k\overline{z}^{k}.
$$
Since $\overline{z}\ne0$ ranges over $\CC\setminus\{0\}$ and a Laurent polynomial has unique coefficients, comparing coefficients gives $a_k=\overline{a_k}$ for each $k$, that is $a_k\in\RR$.
:::

:::


::: {.pf-step #conclusion}
There are real constants $a_{-N},\dots,a_N$ with $f(z)=\sum_{k=-N}^{N}a_kz^k$ on $H$.

::: pf-proof
On the upper half-plane $F=f$ by step [](#reflect){.pf-ref}, and there $F$ is the finite sum of step [](#poly){.pf-ref} with real coefficients by step [](#real){.pf-ref}. So $f$ has the asserted form.
:::

:::

:::
:::
