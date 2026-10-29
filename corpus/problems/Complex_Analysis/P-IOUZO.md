---
schema: qual/card@1
id: P-IOUZO
kind: problem
title: Polynomial approximation on $\bar\DD$ and entire functions with a vanishing
  Taylor coefficient
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Polynomials
  - Power Series
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: statement-edited
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'Part (b) read "for each z_0 there is at least one coefficient in the expansion ... is zero"; the stray "there is" was removed. The hints to parts (a) and (b) moved from the statement to a hint block.'
---

::: {.problem}
(a) Can every continuous function on $\bar \DD$ be uniformly approximated by polynomials in the variable $z$?

(b) Suppose $f$ is analytic, defined on all of $\CC$, and for each $z_0 \in \CC$ at least one coefficient in the expansion $f(z) = \sum_{n=0}^\infty c_n(z-z_0)^n$ is zero.
Prove that $f$ is a polynomial.

(c) Let $\abs{\alpha}<r<\abs{\beta}$, and let $\gamma$ be the positively oriented circle centered at $0$ of radius $r$. Show that
$$
\int_\gamma \frac{dz}{(z-\alpha)(z-\beta)} =\frac{2\pi i}{\alpha-\beta}.
$$

(d) Assume $f$ is continuous on
$$
\{x+iy:x\ge x_0,\ 0\le y\le b\}
$$
and that $f(x+iy)\to A$ as $x\to+\infty$ uniformly with respect to $y\in[0,b]$. If
$$
\gamma_x=\{x+it:0\le t\le b\},
$$
show that
$$
\lim_{x\to+\infty}\int_{\gamma_x}f(z)\,dz=iAb.
$$

(e) If $f$ is analytic on a region $D$, show that
$$
g(z)=\overline{f(\bar z)}
$$
is analytic on the reflected region $\bar D=\{z:\bar z\in D\}$.
:::

::: {.hint}
(a) Compare with the Weierstrass approximation theorem on a real interval.

(b) Use $c_n n! = f^{(n)}(z_0)$ and a countability argument.
:::

::: {.solution}
(a)

::: pf

::: {.pf-step #limit-is-holomorphic}
A uniform limit on $\bar\DD$ of polynomials in $z$ is holomorphic on $\DD$.

::: pf-proof
A locally uniform limit of holomorphic functions is holomorphic, by Morera's theorem.
:::

:::

::: pf-step
$\boxed{\text{No}}$: $f(z) = \bar z$ is continuous on $\bar\DD$ and is not a uniform limit of polynomials in $z$.

::: pf-proof
The function $\bar z$ is continuous but does not satisfy the Cauchy--Riemann equations at any point, so it is not holomorphic on $\DD$; step [](#limit-is-holomorphic){.pf-ref} excludes it as a uniform limit.
:::

:::

:::

(b)

::: pf

::: {.pf-step #cover}
For $n \ge 0$ let $E_n = \{z \in \CC : f^{(n)}(z) = 0\}$.
Each $E_n$ is closed, and $\CC = \bigcup_{n=0}^{\infty} E_n$.

::: pf-proof
$f^{(n)}$ is continuous, so $E_n$ is closed.
For each $z_0$ some coefficient $c_n = f^{(n)}(z_0)/n!$ is zero, so $z_0 \in E_n$.
:::

:::

::: {.pf-step #interior}
Some $E_n$ has nonempty interior.

::: pf-proof
$\CC$ is a complete metric space, and by step [](#cover){.pf-ref} it is a countable union of the closed sets $E_n$; the Baire category theorem applies.
:::

:::

::: pf-step
$f$ is a polynomial of degree less than $n$.

::: pf-proof
By step [](#interior){.pf-ref} the entire function $f^{(n)}$ vanishes on an open disc, so it vanishes identically by the identity theorem.
Then $c_k = f^{(k)}(0)/k! = 0$ for $k \geq n$, and the Taylor series of $f$ at $0$ is a polynomial of degree less than $n$.
:::

:::

:::

(c)

::: pf

::: {.pf-step #residue}
The only singularity of the integrand inside $\gamma$ is a simple pole at $\alpha$, with residue $\frac1{\alpha-\beta}$.

::: pf-proof
$\abs{\alpha}<r<\abs{\beta}$ places $\alpha$ inside $\gamma$ and $\beta$ outside, and $\alpha \neq \beta$.
The residue at $\alpha$ is $\lim_{z\to\alpha}\frac{1}{z-\beta} = \frac{1}{\alpha-\beta}$.
:::

:::

::: pf-step
$$
\boxed{\int_\gamma\frac{dz}{(z-\alpha)(z-\beta)} =\frac{2\pi i}{\alpha-\beta}}.
$$

::: pf-proof
This is the residue theorem applied with step [](#residue){.pf-ref}.
:::

:::

:::

(d)

::: pf

::: {.pf-step #estimate}
$$
\abs{\int_{\gamma_x}f(z)\,dz-iAb} \le b\sup_{0\le t\le b}\abs{f(x+it)-A}.
$$

::: pf-proof
Parametrize $\gamma_x$ by $z=x+it$, $0\le t\le b$, so that $\int_{\gamma_x}f(z)\,dz=i\int_0^b f(x+it)\,dt$ and $iAb = i\int_0^b A\,dt$.
:::

:::

::: pf-step
$$
\boxed{\lim_{x\to\infty}\int_{\gamma_x}f(z)\,dz=iAb}.
$$

::: pf-proof
The right-hand side of step [](#estimate){.pf-ref} tends to $0$ by the uniform convergence of $f(x+iy)$ to $A$.
:::

:::

:::

(e)

::: pf

::: pf-step
$g$ is complex differentiable at every $z\in\bar D$, with $g'(z)=\overline{f'(\bar z)}$.

::: pf-proof
$\bar D$ is open because conjugation is a homeomorphism.
For $h\ne0$ small enough that $z+h\in\bar D$,
$$
\frac{g(z+h)-g(z)}h
=\overline{
\frac{f(\bar z+\bar h)-f(\bar z)}{\bar h}
}.
$$
As $h\to0$, also $\bar h\to0$, so the right-hand side tends to $\overline{f'(\bar z)}$.
:::

:::

:::
:::
