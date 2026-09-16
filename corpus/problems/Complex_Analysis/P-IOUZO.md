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
---

::: {.problem}
- Can every continuous function on $\bar \DD$ be uniformly approximated by polynomials in the variable $z$?

> Hint: compare to Weierstrass for the real interval.

- Suppose $f$ is analytic, defined on all of $\CC$, and for each $z_0 \in \CC$ there is at least one coefficient in the expansion $f(z) = \sum_{n=0}^\infty c_n(z-z_0)^n$ is zero.
  Prove that $f$ is a polynomial.

> Hint: use the fact that $c_n n! = f^{(n)}(z_0)$ and use a countability argument.

- Let $|\alpha|<r<|\beta|$, and let $\gamma$ be the positively oriented circle
  centered at $0$ of radius $r$. Show that
  \[
  \int_\gamma \frac{dz}{(z-\alpha)(z-\beta)}
  =\frac{2\pi i}{\alpha-\beta}.
  \]

- Assume $f$ is continuous on
  \[
  \{x+iy:x\ge x_0,\ 0\le y\le b\}
  \]
  and that $f(x+iy)\to A$ as $x\to+\infty$ uniformly with respect to
  $y\in[0,b]$. If
  \[
  \gamma_x=\{x+it:0\le t\le b\},
  \]
  show that
  \[
  \lim_{x\to+\infty}\int_{\gamma_x}f(z)\,dz=iAb.
  \]

- If $f$ is analytic on a region $D$, show that
  \[
  g(z)=\overline{f(\bar z)}
  \]
  is analytic on the reflected region $\bar D=\{z:\bar z\in D\}$.
:::

::: {.solution}
**Part 1.**

<1>1. No, not every continuous function on $\bar\DD$ is uniformly approximable by polynomials in $z$.
<2>1. A uniform limit of holomorphic polynomials on $\bar\DD$ is holomorphic on the interior $\DD$.
::: {.proof}
a uniform limit of holomorphic functions is holomorphic (Morera's theorem).
:::
<2>2. But there are continuous functions on $\bar\DD$ that are not holomorphic on $\DD$.
::: {.proof}
e.g. $f(z) = \bar z$ is continuous on $\bar\DD$ but not holomorphic.
:::
<2>3. Hence $\bar z$ (or any such function) cannot be uniformly approximated by polynomials in $z$.
::: {.proof}
<2>1 and <2>2.
:::

<1>2. Q.E.D. (part 1).
::: {.proof}
<1>1.
:::

**Part 2.**

<1>1. For each $n \ge 0$, let $E_n = \{z \in \CC : f^{(n)}(z) = 0\}$.
::: {.proof}
define the zero sets of the derivatives.
:::

<1>2. Each $E_n$ is closed, and $\CC = \bigcup_{n=0}^{\infty} E_n$.
::: {.proof}
$f^{(n)}$ is continuous so $E_n$ is closed; the hypothesis says that for each $z_0$ some coefficient $c_n = f^{(n)}(z_0)/n!$ is zero, i.e. $f^{(n)}(z_0) = 0$ for some $n$, so $z_0 \in E_n$.
:::

<1>3. By the Baire category theorem, some $E_n$ has nonempty interior.
::: {.proof}
$\CC$ is a complete metric space and is the countable union of the closed sets $E_n$, so one of them has nonempty interior.
:::

<1>4. Hence $f^{(n)} \equiv 0$ on $\CC$.
::: {.proof}
$f^{(n)}$ is entire and vanishes on a set with nonempty interior (an open disk), so by the identity theorem it vanishes identically.
:::

<1>5. Therefore $f$ is a polynomial of degree at most $n-1$.
::: {.proof}
$f^{(n)} \equiv 0$ implies $f$ is a polynomial of degree $< n$.
:::

<1>6. Q.E.D. (part 2).
::: {.proof}
<1>5.
:::

**Part 3.** Since $|\alpha|<r<|\beta|$, the integrand has exactly one pole
inside $\gamma$, namely the simple pole at $\alpha$. Its residue is
\[
\operatorname{Res}_{z=\alpha}
\frac1{(z-\alpha)(z-\beta)}
=\frac1{\alpha-\beta}.
\]
Therefore the residue theorem gives
\[
\boxed{\int_\gamma\frac{dz}{(z-\alpha)(z-\beta)}
=\frac{2\pi i}{\alpha-\beta}}.
\]

**Part 4.** Parametrize $\gamma_x$ by $z=x+it$, $0\le t\le b$. Then
\[
\int_{\gamma_x}f(z)\,dz=i\int_0^b f(x+it)\,dt.
\]
Hence
\[
\left|\int_{\gamma_x}f(z)\,dz-iAb\right|
\le b\sup_{0\le t\le b}|f(x+it)-A|.
\]
The right-hand side tends to $0$ by the assumed uniform convergence, so
\[
\boxed{\lim_{x\to\infty}\int_{\gamma_x}f(z)\,dz=iAb}.
\]

**Part 5.** Let $z\in\bar D$. For small $h\ne0$ with $z+h\in\bar D$,
\[
\frac{g(z+h)-g(z)}h
=\frac{\overline{f(\bar z+\bar h)-f(\bar z)}}h
=\overline{
\frac{f(\bar z+\bar h)-f(\bar z)}{\bar h}
}.
\]
As $h\to0$, also $\bar h\to0$, so the last expression tends to
$\overline{f'(\bar z)}$. Thus $g$ is complex differentiable at every point
of $\bar D$, with
\[
\boxed{g'(z)=\overline{f'(\bar z)}}.
\]
:::
