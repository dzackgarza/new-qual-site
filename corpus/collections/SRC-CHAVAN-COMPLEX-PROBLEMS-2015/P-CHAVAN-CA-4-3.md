---
schema: qual/card@1
id: P-CHAVAN-CA-4-3
kind: problem
title: A compact limit of injective holomorphic functions is constant or injective
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $(f_n)$ be a sequence of injective holomorphic functions converging uniformly on compact subsets to a holomorphic function $f$.
Show that either $f$ is constant or $f$ is injective.
:::

::: {.solution}

Let $\Omega$ denote the common domain of the functions.

::: pf

::: {.pf-step #s1-1}

Suppose that $f$ is not injective. Then there are distinct points $z_1,z_2\in\Omega$ such that
$$
f(z_1)=f(z_2).
$$


::: pf-proof

This is exactly the negation of injectivity.

:::

:::

::: {.pf-step #s1-2}

There is an open disk $D$ centered at $z_2$ whose closure is contained in $\Omega$ and which does not contain $z_1$.


::: pf-proof

Since $\Omega$ is open, choose $\varepsilon>0$ such that
$$
\{z:\abs{z-z_2}<\varepsilon\}\subseteq\Omega.
$$
Since $z_1\ne z_2$, choose
$$
0<r<\min\{\varepsilon/2,\abs{z_2-z_1}\}.
$$
Then
$$
D=\{z:\abs{z-z_2}<r\}
$$
has the required properties.

:::

:::

::: {.pf-step #s1-3}

For
$$
g_n(z)=f_n(z)-f_n(z_1),
$$
the function $g_n$ has no zero on $D$ for every $n$.


::: pf-proof

If $g_n(z)=0$ for some $z\in D$, then
$$
f_n(z)=f_n(z_1).
$$
Because $f_n$ is injective, this implies $z=z_1$, contradicting step
[](#s1-2){.pf-ref}. Hence $g_n$ is nowhere zero on $D$.

:::

:::

::: {.pf-step #s1-4}

The sequence $(g_n)$ converges uniformly on compact subsets of $D$ to
$$
g(z)=f(z)-f(z_1).
$$


::: pf-proof

For every compact $K\subset D$,
$$
\sup_{z\in K}\abs{g_n(z)-g(z)}
\le
\sup_{z\in K}\abs{f_n(z)-f(z)}
+\abs{f_n(z_1)-f(z_1)}.
$$
The first term tends to $0$ by compact convergence on $K$, and the
second tends to $0$ by pointwise convergence at $z_1$.

:::

:::

::: {.pf-step #s1-5}

The function $g$ vanishes identically on $D$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
g(z_2)=f(z_2)-f(z_1)=0.
$$
Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} allow Hurwitz's theorem to be applied on the disk
$D$: the compact limit of the nowhere-vanishing holomorphic functions
$g_n$ is either nowhere zero or identically zero. Since $g(z_2)=0$,
the nowhere-zero alternative is impossible. Thus $g\equiv0$ on $D$.

:::

:::

::: {.pf-step #s1-6}

If $f$ is not injective, then $f$ is constant on $\Omega$.


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
f(z)=f(z_1)
$$
for every $z\in D$. Hence the holomorphic function
$f-f(z_1)$ vanishes on the nonempty open set $D$. By the identity
theorem on the domain $\Omega$, it vanishes identically on $\Omega$.
Thus $f$ is constant.

:::

:::

::: {.pf-step #s1-7}

Therefore either $f$ is constant or $f$ is injective.


::: pf-proof

Step [](#s1-6){.pf-ref} shows that failure of injectivity forces constancy. Equivalently,
if $f$ is nonconstant, then it is injective.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required dichotomy.

:::

:::

:::
