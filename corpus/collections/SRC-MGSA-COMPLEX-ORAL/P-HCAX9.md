---
schema: qual/card@1
id: P-HCAX9
kind: problem
title: Derivatives under compact-uniform convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the card's own argument into Lamport steps; the estimate is correct and is
    kept, including its constant R/(R-r)^2. Made explicit in the restructuring: the exchange
    of limit and integral in the Cauchy formula is licensed by uniform convergence on the
    integration circle, the constant in the derivative estimate is computed from the length
    2 pi R of that circle and the bound |zeta - z| >= R - r, and the passage from "uniform on
    each smaller disc" to "uniform on compact subsets" is the finite subcover of a compact
    set by such discs. The answer to the card's question — what can be said about the f_n' —
    is stated first as the result and then proved. No statement repair. No retained solution
    set covers this problem: the collection's provenance,
    assets/attachments/MGSA_Complex_Analysis_Oral_Questions.pdf, is the question sheet.
---

::: {.problem}
Let $f_n$ be holomorphic on a domain $\Omega$, and suppose $f_n\to F$ uniformly on compact subsets of $\Omega$.
What can be said about the derivatives $f_n'$?
:::

::: {.solution}
No retained solution set covers this problem — the collection's provenance, `assets/attachments/MGSA_Complex_Analysis_Oral_Questions.pdf`, is the question sheet — so the argument is the card's own.

Throughout, $\Omega\subseteq\CC$ is a domain, each $f_n$ is holomorphic on $\Omega$, $f_n\to F$ uniformly on compact subsets of $\Omega$, and $\overline{D(a,R)}=\{z : \abs{z-a}\le R\}$.

::: pf

::: {.pf-step #answer}
$F$ is holomorphic on $\Omega$, and $f_n'\to F'$ uniformly on compact subsets of $\Omega$; more generally $f_n^{(k)}\to F^{(k)}$ there for every fixed $k\ge1$.

::: pf-proof
The three assertions are steps [](#holomorphic){.pf-ref}, [](#derivative){.pf-ref} and [](#higher){.pf-ref} below. The restriction "fixed $k$" is essential in the statement and is what the argument proves: for each $k$ the convergence is locally uniform, with no uniformity in $k$.
:::

:::

::: {.pf-step #holomorphic}
$F$ is holomorphic on $\Omega$.

::: pf-proof
Let $\overline{D(a,R)}\subset\Omega$. For $z$ with $\abs{z-a}<R$ and every $n$, Cauchy's formula gives $f_n(z)=\frac{1}{2\pi i}\int_{\abs{\zeta-a}=R}\frac{f_n(\zeta)}{\zeta-z}\,d\zeta$. The circle $\abs{\zeta-a}=R$ is compact, so $f_n\to F$ uniformly on it, and $\frac{1}{\zeta-z}$ is bounded on it because $\abs{\zeta-z}\ge R-\abs{z-a}>0$; hence the integrands converge uniformly and the limit may be taken under the integral, giving $F(z)=\frac{1}{2\pi i}\int_{\abs{\zeta-a}=R}\frac{F(\zeta)}{\zeta-z}\,d\zeta$ for $\abs{z-a}<R$. A continuous function on an open set that is given locally by such an integral is holomorphic, so $F$ is holomorphic on the interior of every closed disc contained in $\Omega$, that is on $\Omega$.
:::

:::

::: {.pf-step #derivative}
For $\overline{D(a,R)}\subset\Omega$ and $0<r<R$, $\sup_{\abs{z-a}\le r}\abs{f_n'(z)-F'(z)}\le\frac{R}{(R-r)^2}\sup_{\abs{\zeta-a}=R}\abs{f_n(\zeta)-F(\zeta)}$, and the right-hand side tends to $0$.

::: pf-proof
Both $f_n$ and $F$ are holomorphic on a neighbourhood of $\overline{D(a,R)}$, so Cauchy's differentiation formula applies:
$f_n'(z)-F'(z)=\frac{1}{2\pi i}\int_{\abs{\zeta-a}=R}\frac{f_n(\zeta)-F(\zeta)}{(\zeta-z)^2}\,d\zeta$ for $\abs{z-a}<R$.
On the circle and for $\abs{z-a}\le r$ we have $\abs{\zeta-z}\ge R-r$, so the integrand is bounded by $\sup_{\abs{\zeta-a}=R}\abs{f_n-F}/(R-r)^2$; estimating the integral by the length $2\pi R$ of the circle times that bound gives the displayed inequality.
The right-hand side tends to $0$ as $n\to\infty$ because $f_n\to F$ uniformly on the compact circle; the factor $R/(R-r)^2$ does not depend on $n$.
:::

:::

::: {.pf-step #compactsup}
$f_n'\to F'$ uniformly on compact subsets of $\Omega$.

::: pf-proof
Let $K\subset\Omega$ be compact. Each point of $K$ lies in some closed disc $\overline{D(a,R)}\subset\Omega$ — take $R$ smaller than the distance from the point to the complement of $\Omega$ — and the open discs of radius $R/2$ about the same centres cover $K$; by compactness finitely many of them do. For the $j$-th such disc with centre $a_j$ and radius $R_j$, put $r_j=R_j/2$; the disc $\overline{D(a_j,r_j)}$ contains the corresponding open disc, so it contains the part of $K$ in question. Step [](#derivative){.pf-ref} gives, on each of the finitely many closed discs $\overline{D(a_j,r_j)}$, $\sup\abs{f_n'-F'}\le\frac{R_j}{(R_j-r_j)^2}\sup_{\abs{\zeta-a_j}=R_j}\abs{f_n-F}$, and each of those finitely many right-hand sides tends to $0$. So the supremum over $K$ tends to $0$, which is uniform convergence on $K$; $K$ was arbitrary.
:::

:::

::: {.pf-step #higher}
$f_n^{(k)}\to F^{(k)}$ uniformly on compact subsets of $\Omega$, for each fixed $k\ge1$.

::: pf-proof
Cauchy's formula for the $k$-th derivative reads $f^{(k)}(z)=\frac{k!}{2\pi i}\int_{\abs{\zeta-a}=R}\frac{f(\zeta)}{(\zeta-z)^{k+1}}\,d\zeta$. Applying it to $f_n-F$ and estimating as in step [](#derivative){.pf-ref}, with $\abs{\zeta-z}\ge R-r$ on $\abs{z-a}\le r$, gives $\sup_{\abs{z-a}\le r}\abs{f_n^{(k)}(z)-F^{(k)}(z)}\le\frac{k!\,R}{(R-r)^{k+1}}\sup_{\abs{\zeta-a}=R}\abs{f_n(\zeta)-F(\zeta)}$, whose right-hand side tends to $0$; the covering argument of step [](#compactsup){.pf-ref} then gives the assertion. The exponent $k+1$ in the denominator is why the bound is worse for larger $k$, though still convergent for each fixed $k$.
:::

:::

:::
:::
