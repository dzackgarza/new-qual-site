---
schema: qual/card@1
id: P-AGH433COMPLETEINTERSECTIONCANONICAL
kind: problem
title: The canonical divisor of a complete intersection curve is very ample
classification:
  areas:
  - algebraic-geometry
  topics:
  - Canonical Divisor
  - Very Ample Divisors
  - Embeddings
  - Genus
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.3 together with the complete-intersection adjunction
    formula from II.8.4. The proof identifies the canonical bundle as a
    positive tensor power of the hyperplane bundle and then invokes IV.3.1 for
    the genus-two contradiction.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
If $X$ is a curve of genus $\geq 2$ which is a complete intersection (II, Ex.
8.4) in some $\PP^n$, show that the canonical divisor $K$ is very ample.
Conclude that a curve of genus 2 can never be a complete intersection in any $\PP^n$.
Cf.
(Ex.
5.1).
:::

::: {.solution}
Suppose
$$
X=H_1\cap\cdots\cap H_{n-1}\subset\PP^n
$$
is a nonsingular complete-intersection curve, where
$$
\deg H_i=d_i.
$$

::: pf

::: {.pf-step #s1}

The canonical sheaf of $X$ is
$$
\omega_X
\cong
\OO_X(m),
\qquad
m=\sum_{i=1}^{n-1}d_i-n-1.
$$

::: pf-proof

The complete-intersection adjunction formula of Hartshorne II.8.4(d) gives
$$
\omega_X
\cong
\left(
\omega_{\PP^n}
\tensor
\OO_{\PP^n}\!\left(\sum_i d_i\right)
\right)|_X.
$$
Since
$$
\omega_{\PP^n}\cong\OO_{\PP^n}(-n-1),
$$
this becomes
$$
\omega_X
\cong
\OO_X\!\left(\sum_i d_i-n-1\right)
=\OO_X(m).
$$

:::

:::

::: {.pf-step #s2}

If $g(X)\ge2$, then
$$
m>0.
$$

::: pf-proof

The hyperplane bundle $\OO_X(1)$ has positive degree
$$
\deg X=\prod_i d_i>0.
$$
By step [](#s1){.pf-ref},
$$
2g-2
=
\deg\omega_X
=
m\deg\OO_X(1).
$$
The left-hand side is positive because $g\ge2$, and
$\deg\OO_X(1)>0$.  Hence $m>0$.

:::

:::

::: {.pf-step #s3}

The canonical divisor of $X$ is very ample.

::: pf-proof

The line bundle $\OO_X(1)$ is very ample because it is the restriction of
the hyperplane bundle for the given closed immersion
$$
X\hookrightarrow\PP^n.
$$
By step [](#s2){.pf-ref}, $m\ge1$.  Every positive tensor power of a very ample line
bundle is very ample: the corresponding morphism is the given embedding
followed by the $m$-uple Veronese embedding.  Thus
$$
\omega_X\cong\OO_X(1)^{\tensor m}
$$
is very ample.

:::

:::

::: {.pf-step #s4}

A curve of genus $2$ cannot be a complete intersection in any
$\PP^n$.

::: pf-proof

If $g(X)=2$, then every canonical divisor has degree
$$
\deg K_X=2g-2=2.
$$
If $X$ were a complete intersection, step [](#s3){.pf-ref} would make $K_X$ very ample.
But [[P-AGH431GENUSTWOVERYAMPLE|Exercise IV.3.1]] proves that on a genus-$2$
curve every very ample divisor has degree at least $5$.  This contradicts
$\deg K_X=2$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove that the canonical divisor of a complete-intersection
curve of genus at least $2$ is very ample, and step [](#s4){.pf-ref} proves the genus-$2$
conclusion.

:::

:::

:::
