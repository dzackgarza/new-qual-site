---
schema: qual/card@1
id: E-SS3.EX-20
kind: problem
title: $L^2$ norms control sup norms of holomorphic functions on smaller discs
classification:
  areas:
    - complex-analysis
  topics: [Bergman Spaces, Uniform Convergence, Mean Value Property]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
      card's own and the card says so; the printed hint is followed. Each step re-read: the disc of
      radius (r-s)/2 around a point of D_s lies in D_r by the triangle inequality; the mean-value
      property replaces the value by an average; Cauchy-Schwarz converts the square of the average
      into an L^2 bound; and part (b) applies that bound to differences over a finite cover of a
      compact set, giving uniform Cauchy on compacta and, by Weierstrass's theorem, a holomorphic
      limit. The constant is written out as 1/(sqrt(pi)(r-s)/2). Not claimed: any bound with a
      constant independent of r and s, which is impossible.
---

::: {.exercise}
This exercise shows how the mean square convergence dominates the uniform convergence of analytic functions. If $U$ is an open subset of $\CC$ we use the notation
$$
\norm{f}_{L^2(U)} = \left( \int_U \abs{f(z)}^2\, dx\, dy \right)^{1/2}
$$
for the mean square norm, and
$$
\norm{f}_{L^\infty(U)} = \sup_{z \in U} \abs{f(z)}
$$
for the sup norm.

(a) If $f$ is holomorphic in a neighborhood of the disc $D_r(z_0)$, show that for any $0 < s < r$ there exists a constant $C > 0$ (which depends on $s$ and $r$) such that
$$
\norm{f}_{L^\infty(D_s(z_0))} \leq C\norm{f}_{L^2(D_r(z_0))}.
$$

(b) Prove that if $\{f_n\}$ is a Cauchy sequence of holomorphic functions in the mean square norm $\norm{\cdot}_{L^2(U)}$, then the sequence $\{f_n\}$ converges uniformly on every compact subset of $U$ to a holomorphic function.

[Hint: Use the mean-value property.]
:::

::: {.solution}
The statement is Exercise 20 of Stein--Shakarchi, *Complex Analysis* [@SS03, ch. 3, §8, Exercise 20], printed beginning "This exercise shows how the mean square convergence dominates the uniform convergence of analytic functions".

The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 3 Exercise 20, and follows the printed hint to use the mean-value property.

::: pf

::: {.pf-step #parta}
For holomorphic $f$ near $D_{r}(z_{0})$ and $0<s<r$ there is $C>0$ with $\norm{f}_{L^{\infty}(D_{s}(z_{0}))}\le C\norm{f}_{L^{2}(D_{r}(z_{0}))}$.

:::: pf-proof

::: {.pf-step #inside}
With $\rho=\tfrac12(r-s)>0$, the closed disc $\overline{D_{\rho}(z)}$ lies in $D_{r}(z_{0})$ for every $z\in D_{s}(z_{0})$.

::: pf-proof
If $\abs{w-z}\le\rho$ then $\abs{w-z_{0}}\le\abs{w-z}+\abs{z-z_{0}}<\rho+s=\tfrac12(r-s)+s=\tfrac12(r+s)<r$.
:::

:::

::: {.pf-step #meanvalue}
$f(z)=\dfrac{1}{\pi\rho^{2}}\int_{D_{\rho}(z)}f(w)\,dA(w)$.

::: pf-proof
This is the mean-value property of holomorphic functions: the value at the centre is the average over the disc.
:::

:::

::: {.pf-step #bound}
$\abs{f(z)}^{2}\le\dfrac{1}{\pi\rho^{2}}\norm{f}^{2}_{L^{2}(D_{r}(z_{0}))}$.

::: pf-proof
$\abs{f(z)}^{2}\le\frac{1}{\pi^{2}\rho^{4}}\bigl(\int_{D_{\rho}(z)}\abs{f}\bigr)^{2}$ by step [](#meanvalue){.pf-ref}, and Cauchy--Schwarz bounds the square of the integral by $\pi\rho^{2}\int_{D_{\rho}(z)}\abs{f}^{2}$. Since $D_{\rho}(z)\subseteq D_{r}(z_{0})$ by step [](#inside){.pf-ref}, the last integral is at most $\norm{f}^{2}_{L^{2}(D_{r}(z_{0}))}$.
:::

:::

::: {.pf-step}
$\norm{f}_{L^{\infty}(D_{s}(z_{0}))}\le C\norm{f}_{L^{2}(D_{r}(z_{0}))}$ with $C=(\sqrt{\pi}\rho)^{-1}$.

::: pf-proof
Taking square roots in step [](#bound){.pf-ref} and then the supremum over $z\in D_{s}(z_{0})$ gives the inequality with $C=1/(\sqrt{\pi}\rho)$, which depends only on $s$ and $r$.
:::

:::

:::

:::

::: {.pf-step #partb}
If $\{f_{n}\}$ is Cauchy in $\norm{\cdot}_{L^{2}(U)}$ then it converges uniformly on compact subsets of $U$ to a holomorphic function.

:::: pf-proof

::: {.pf-step #cover}
For $K\Subset U$ there are finitely many discs $D_{s_{j}}(z_{j})$ with $K\subseteq\bigcup_{j}D_{s_{j}}(z_{j})$, $\overline{D_{r_{j}}(z_{j})}\subset U$ and $0<s_{j}<r_{j}$.

::: pf-proof
Every point of the compact $K$ has a disc around it whose closure lies in $U$; shrink radii to get $0<s_{j}<r_{j}$ with $\overline{D_{r_{j}}(z_{j})}\subset U$. Compactness extracts a finite subcover.
:::

:::

::: {.pf-step #uniformcauchy}
$\norm{f_{n}-f_{m}}_{L^{\infty}(K)}\le C_{K}\norm{f_{n}-f_{m}}_{L^{2}(U)}$ with $C_{K}$ independent of $n,m$.

::: pf-proof
On each $D_{s_{j}}(z_{j})$, step [](#parta){.pf-ref} applied to the holomorphic $f_{n}-f_{m}$ gives a bound by $C_{j}\norm{f_{n}-f_{m}}_{L^{2}(D_{r_{j}}(z_{j}))}\le C_{j}\norm{f_{n}-f_{m}}_{L^{2}(U)}$; take the maximum of the $C_{j}$ over the finite cover.
:::

:::

::: {.pf-step #limit}
$\{f_{n}\}$ converges uniformly on $K$ to a function $f$, and $f$ is holomorphic on $U$.

::: pf-proof
Step [](#uniformcauchy){.pf-ref} shows $\{f_{n}\}$ is uniformly Cauchy on $K$, hence uniformly convergent there; a uniform limit of continuous functions is continuous. Covering $U$ by an exhaustion of compact sets gives a pointwise limit $f$ on $U$, and on each compact subset the convergence is uniform; by Weierstrass's theorem a locally uniform limit of holomorphic functions is holomorphic.
:::

:::

:::

:::

::: {.pf-step}
Parts (a) and (b) hold.

::: pf-proof
Step [](#parta){.pf-ref} is (a) with $C=1/(\sqrt{\pi}\,\tfrac12(r-s))$, and step [](#partb){.pf-ref} is (b):
$$
\boxed{\norm{f}_{L^{\infty}(D_{s}(z_{0}))}\le\frac{1}{\sqrt{\pi}\,\tfrac12(r-s)}\norm{f}_{L^{2}(D_{r}(z_{0}))},\qquad L^{2}\text{-Cauchy}\implies\text{locally uniform convergence to a holomorphic limit}.}
$$
The constant blows up as $s\to r$, which is unavoidable: the sup norm on the whole of $D_{r}$ is not controlled by the mean square norm there.
:::

:::

:::
:::
