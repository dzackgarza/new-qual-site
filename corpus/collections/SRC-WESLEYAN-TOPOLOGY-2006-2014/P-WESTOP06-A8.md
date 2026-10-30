---
schema: qual/card@1
id: P-WESTOP06-A8
kind: problem
title: A zero-dimensional compactification with the clopen extension property
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Recall the construction and characteristic properties of the Čech--Stone compactification $\beta X$ of a completely regular Hausdorff space $X$.

Let $X$ instead be zero-dimensional Hausdorff. Sketch the analogous construction of a compact zero-dimensional Hausdorff space $zX$ containing $X$ densely such that every continuous map
$$
f:X\to\{0,1\},
$$
with $\{0,1\}$ discrete, extends uniquely to a continuous map
$$
\overline f:zX\to\{0,1\}.
$$
:::

::: {.solution}

Let
$$
\mathcal B=\operatorname{clop}(X)
\qquad\text{and}\qquad
2=\{0,1\}
$$
with $2$ discrete. For $U\in\mathcal B$, write $\chi_U:X\to2$ for its characteristic function.

::: pf

::: {.pf-step #s1-1}

The evaluation map
$$
e:X\longrightarrow 2^{\mathcal B},
\qquad
e(x)(U)=\chi_U(x),
$$
is a topological embedding.


::: pf-proof

Every coordinate $\chi_U$ is continuous because $U$ is clopen, so $e$ is continuous.

To prove injectivity, let $x\ne y$. Since $X$ is Hausdorff, there is an open neighborhood $O$ of $x$ with $y\notin O$. Because the clopen subsets form a basis, there is $U\in\mathcal B$ with
$$
x\in U\subseteq O.
$$
Then $e(x)(U)=1$ and $e(y)(U)=0$, so $e(x)\ne e(y)$.

Finally, the subspace topology induced by $e$ is the original topology of $X$. Indeed, for each $U\in\mathcal B$,
$$
U=e^{-1}\bigl(\{p\in2^{\mathcal B}:p(U)=1\}\bigr),
$$
and the set on the right is a basic clopen cylinder in the product. Thus every member of the clopen basis of $X$ is the inverse image of an open set in $e(X)$. Since $e$ is already continuous, $e:X\to e(X)$ is a homeomorphism.

:::

:::

::: {.pf-step #s1-2}

Define
$$
\boxed{zX=\overline{e(X)}^{\,2^{\mathcal B}}.}
$$
Then $zX$ is compact Hausdorff and contains $X$ densely, after identifying $X$ with $e(X)$.


::: pf-proof

The discrete two-point space $2$ is compact Hausdorff. By Tychonoff's theorem, $2^{\mathcal B}$ is compact Hausdorff. Hence its closed subspace $zX$ is compact Hausdorff. By step [](#s1-1){.pf-ref}, $e(X)$ is a copy of $X$, and it is dense in $zX$ by the definition of $zX$ as its closure.

:::

:::

::: {.pf-step #s1-3}

The space $zX$ is zero-dimensional.


::: pf-proof

The product $2^{\mathcal B}$ has a basis of clopen cylinder sets: a basic cylinder prescribes values in only finitely many coordinates, and each prescribed coordinate condition is clopen because $2$ is discrete. Intersecting these cylinders with the subspace $zX$ gives a clopen basis for $zX$. Hence $zX$ is zero-dimensional.

:::

:::

::: {.pf-step #s1-4}

Every continuous $f:X\to2$ has a continuous extension $\overline f:zX\to2$.


::: pf-proof

Since $2$ is discrete, the set
$$
U=f^{-1}(\{1\})
$$
is clopen in $X$, so $U\in\mathcal B$ and $f=\chi_U$. Let
$$
\pi_U:2^{\mathcal B}\to2
$$
be the $U$-coordinate projection. Define
$$
\overline f=\pi_U\restrict_{zX}.
$$
This map is continuous. For every $x\in X$,
$$
\overline f(e(x))
=\pi_U(e(x))
=e(x)(U)
=\chi_U(x)
=f(x),
$$
so $\overline f$ extends $f$.

:::

:::

::: {.pf-step #s1-5}

The extension in step [](#s1-4){.pf-ref} is unique.


::: pf-proof

Suppose $g,h:zX\to2$ are continuous and agree on the dense subspace $e(X)$. Because $2$ is Hausdorff, the equalizer
$$
\{z\in zX:g(z)=h(z)\}
$$
is closed in $zX$. It contains the dense subset $e(X)$, so it is all of $zX$. Hence $g=h$.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} give a compact zero-dimensional Hausdorff space $zX$ containing $X$ densely, and steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} give the required unique extension of every continuous map $X\to\{0,1\}$.

:::

:::

:::
