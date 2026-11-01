---
schema: qual/card@1
id: E-SS2.PR-4
kind: problem
title: Converse of Runge's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Runge
  - Polynomial Approximation
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 2, §5.5, exercise 4, read
    from the copy at `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the
    printed exercise; the print's two typographical slips ("if not connected", "polynomial on K")
    are not reproduced here. Nothing else in this card was changed by this check.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Solution written, following the book's own hint. It proves the statement and nothing more: the
    witness function is $1/(z-z_0)$ for $z_0$ in a bounded component of $K^c$, and the contradiction
    is the maximum modulus principle applied on that component. Cited, not reproved: Runge's theorem
    itself (Stein--Shakarchi, Chapter 2, Theorem 5.7) is *not* used anywhere in the proof, since this
    is its converse; the two results invoked are the maximum modulus principle (Chapter 3,
    Theorem 4.5) and compactness of the closure of a bounded component. The proof does not claim
    that $K^c$ connected is necessary for approximation of *every* function, only that one explicit
    holomorphic function fails when $K^c$ is disconnected.
---

::: {.exercise}
Prove the converse to Runge's theorem: if $K$ is a compact set whose complement is not connected, then there exists a function $f$ holomorphic in a neighborhood of $K$ which cannot be approximated uniformly by polynomials on $K$.

[Hint: Pick a point $z_0$ in a bounded component of $K^c$, and let $f(z) = 1/(z - z_0)$. If $f$ can be approximated uniformly by polynomials on $K$, show that there exists a polynomial $p$ such that $\abs{(z - z_0)p(z) - 1} < 1$ on $K$. Use the maximum modulus principle (Chapter 3) to show that this inequality continues to hold for all $z$ in the component of $K^c$ that contains $z_0$.]
:::

::: {.solution}

Let $\Omega=\CC\setminus K$. Since $K$ is compact there is a bounded component of $\Omega$; fix one such component $U$ and a point $z_0\in U$, and put
$$
f(z)=\frac{1}{z-z_0}.
$$
We show that $f$ is holomorphic in a neighborhood of $K$ and admits no uniform approximation on $K$ by polynomials.

::: pf

::: {.pf-step #s1}

There is a component $U$ of $\Omega$ that is bounded, and for it $\overline U$ is compact and $\partial U\subseteq K$.

::: pf-proof

Choose $R>0$ with $K\subseteq D(0,R)$, which is possible because $K$ is compact. The set $\CC\setminus\overline{D(0,R)}$ is connected and is contained in $\Omega$, so it lies in a single component $\Omega_\infty$ of $\Omega$.

Let $U$ be a component of $\Omega$ with $U\ne\Omega_\infty$. If $U$ were unbounded, it would contain a point $z$ with $\abs{z}>R$, and then $z\in\CC\setminus\overline{D(0,R)}\subseteq\Omega_\infty$, so $U$ and $\Omega_\infty$ would be components sharing a point and hence equal, a contradiction. Therefore $U\subseteq\overline{D(0,R)}$, so $U$ is bounded and $\overline U\subseteq\overline{D(0,R)}$ is compact.

Since $\Omega$ is not connected by hypothesis, it has a component other than $\Omega_\infty$, so such a $U$ exists.

Finally $U$ is both open and closed in the open set $\Omega$, hence $\partial U\cap\Omega=\varnothing$: a point of $\Omega$ lying on $\partial U$ would be a limit point of $U$ inside $\Omega$ and therefore a point of $U$, so it would lie in the interior of $U$. Thus
$$
\partial U\subseteq\CC\setminus\Omega=K .
$$

:::

:::

::: {.pf-step #s2}

The function $f$ is holomorphic in a neighborhood of $K$.

::: pf-proof

Since $z_0\in U\subseteq\Omega=\CC\setminus K$ and $K$ is closed, the distance
$$
\delta=\operatorname{dist}(z_0,K)
$$
is positive. The function $f$ is holomorphic on $\CC\setminus\{z_0\}$, which contains the open set $\{z:\abs{z-z_0}>\delta/2\}$, and that set contains $K$ because every $z\in K$ satisfies $\abs{z-z_0}\ge\delta>\delta/2$. Hence $f$ is holomorphic on a neighborhood of $K$.

:::

:::

::: {.pf-step #s3}

If $f$ were the uniform limit on $K$ of a sequence of polynomials, there would be a polynomial $p$ with
$$
\abs{(z-z_0)p(z)-1}<\tfrac12\qquad\text{for all }z\in K .
$$

::: pf-proof

The set $K$ is compact and $z\mapsto\abs{z-z_0}$ is continuous, so
$$
C=\sup_{z\in K}\abs{z-z_0}
$$
is finite and positive, because $z_0\notin K$.

Suppose polynomials $p_n$ converge to $f$ uniformly on $K$. Choose $n$ with $\abs{p_n(z)-f(z)}<1/(2C)$ for all $z\in K$, and set $p=p_n$. Since $(z-z_0)f(z)=1$ for $z\ne z_0$, and $z_0\notin K$, for every $z\in K$
$$
\abs{(z-z_0)p(z)-1}=\abs{z-z_0}\,\abs{p(z)-f(z)}<\abs{z-z_0}\cdot\frac{1}{2C}\le\frac12<1 .
$$

:::

:::

::: {.pf-step #s4}

The function $g(z)=(z-z_0)p(z)-1$ is entire and satisfies $g(z_0)=-1$.

::: pf-proof

It is a polynomial, hence entire. At $z=z_0$ the first term vanishes, so $g(z_0)=-1$.

:::

:::

::: {.pf-step #s5}

$\abs{g}<\tfrac12$ on $\partial U$, hence $\abs{g(z_0)}\le\tfrac12$.

::: pf-proof

By step [](#s1){.pf-ref}, $\partial U\subseteq K$, and by step [](#s3){.pf-ref}, $\abs{g}<\tfrac12$ on $K$; therefore $\abs{g}<\tfrac12$ on $\partial U$.

The set $U$ is a bounded region, and $g$ is entire, so $g$ is holomorphic on $U$ and continuous on $\overline U$. By the maximum modulus principle (Stein--Shakarchi, Chapter 3, Theorem 4.5) applied to the region $U$,
$$
\sup_{z\in\overline U}\abs{g(z)}=\sup_{z\in\partial U}\abs{g(z)}\le\tfrac12 .
$$
Since $z_0\in U\subseteq\overline U$, this gives $\abs{g(z_0)}\le\tfrac12$.

:::

:::

::: pf-step

Contradiction; hence $f$ is not uniformly approximable on $K$ by polynomials.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give simultaneously $\abs{g(z_0)}=1$ and $\abs{g(z_0)}\le\tfrac12$, which is impossible. Therefore $f$ is not the uniform limit on $K$ of any sequence of polynomials, and by step [](#s2){.pf-ref} it is holomorphic in a neighborhood of $K$.

:::

:::

:::

:::
