---
schema: qual/card@1
id: P-TIE-F15-05
kind: problem
title: Cauchy's integral formula for an exterior region
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 5.
---

::: {.problem}
(Cauchy's formula for “exterior” region) Let $\gamma$ be a piecewise smooth simple closed curve with interior $\Omega_1$ and exterior $\Omega_2$.
Assume $f'(z)$ exists in an open set containing $\gamma$ and $\Omega_2$, and
\[
\lim_{z\to\infty}f(z)=A.
\]
Show that
\[
\frac{1}{2\pi i}\int_\gamma \frac{f(\xi)}{\xi-z}\,d\xi
=
\begin{cases}
A, & z\in\Omega_1,\\
-f(z)+A, & z\in\Omega_2.
\end{cases}
\]
:::

::: {.solution}
Take the standard positive orientation on $\gamma$. For sufficiently large $R$, let
$$
C_R\coloneqq\{\xi:\abs{\xi}=R\}
$$
with positive orientation, chosen so that $\gamma$ and the fixed point $z$ lie inside $C_R$.

<1>1. For every fixed $z\in\CC$,
$$
\lim_{R\to\infty}
\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi
=
2\pi iA.
$$

::: {.proof}
For $R>\abs{z}$,
$$
\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi
=
A\int_{C_R}\frac{d\xi}{\xi-z}
+
\int_{C_R}\frac{f(\xi)-A}{\xi-z}\,d\xi.
$$
Since $z$ lies inside $C_R$,
$$
\int_{C_R}\frac{d\xi}{\xi-z}=2\pi i.
$$
For the error term,
$$
\begin{aligned}
\abs{
\int_{C_R}\frac{f(\xi)-A}{\xi-z}\,d\xi
}
&\le
\frac{2\pi R}{R-\abs{z}}
\sup_{\abs{\xi}=R}\abs{f(\xi)-A}.
\end{aligned}
$$
Because $f(\xi)\to A$ as $\xi\to\infty$, the supremum tends to $0$, while
$$
\frac{R}{R-\abs{z}}\longrightarrow1.
$$
Hence the error term tends to $0$, proving the claim.
:::

<1>2. If $z\in\Omega_1$, then
$$
\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi
=
2\pi iA.
$$

::: {.proof}
Choose $R$ as above. The function
$$
\xi\longmapsto\frac{f(\xi)}{\xi-z}
$$
is analytic on the region between $\gamma$ and $C_R$: the only possible singularity at $\xi=z$ lies in the interior region $\Omega_1$, which is outside this annular domain. Cauchy--Goursat on the annulus therefore gives
$$
\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi
-
\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi
=0.
$$
Thus the integral over $\gamma$ equals the integral over $C_R$. Letting $R\to\infty$ and using step <1>1 gives the result.
:::

<1>3. If $z\in\Omega_2$, then
$$
\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi
=
2\pi i\left(A-f(z)\right).
$$

::: {.proof}
Choose $R$ so large that $z$ lies between $\gamma$ and $C_R$. On this annular region,
$$
\xi\longmapsto\frac{f(\xi)}{\xi-z}
$$
has exactly one singularity, a simple pole at $\xi=z$, with residue $f(z)$. The residue theorem applied to the annulus gives
$$
\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi
-
\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi
=
2\pi i f(z).
$$
Therefore
$$
\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi
=
\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi
-
2\pi i f(z).
$$
Letting $R\to\infty$ and applying step <1>1 yields
$$
\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi
=
2\pi iA-2\pi i f(z).
$$
:::

<1>4. Hence
$$
\boxed{
\frac{1}{2\pi i}
\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi
=
\begin{cases}
A,&z\in\Omega_1,\\
-f(z)+A,&z\in\Omega_2.
\end{cases}
}
$$

::: {.proof}
Divide the identity in step <1>2 or step <1>3 by $2\pi i$, according to the location of $z$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required exterior Cauchy formula.
:::
:::
