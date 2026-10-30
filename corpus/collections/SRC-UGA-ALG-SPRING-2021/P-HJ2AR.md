---
schema: qual/card@1
id: P-HJ2AR
kind: problem
title: Splitting field, Galois group, and correspondence for $x^4+4x^2+64$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Define
$$
f(x) \coloneqq x^4 + 4x^2 + 64 \in \QQ[x]
.$$

a. Find the splitting field $K$ of $f$ over $\QQ$.

b. Find the Galois group $G$ of $f$.

c. Exhibit explicitly the correspondence between subgroups of $G$ and intermediate fields between $\QQ$ and $K$.
:::

::: {.concept}
\envlist

- Useful trick: given $a + \sqrt{b}$, try to rewrite this as $(\sqrt{c} + \sqrt{d})^2$ for some $c, d$ to get a better basis for $\SF(f)$.
:::



::: {.solution}

::: pf

::: {.pf-step #roots}

$f(x)=(x^2-2\sqrt3\,x+8)(x^2+2\sqrt3\,x+8)$, and the roots of $f$ are $\pm\sqrt3\pm i\sqrt5$.

::: pf-proof

$f(x)=(x^2+8)^2-12x^2$, which is a difference of squares with $12x^2=(2\sqrt3\,x)^2$. The quadratic formula gives the roots $\sqrt3\pm i\sqrt5$ of the first factor and $-\sqrt3\pm i\sqrt5$ of the second.

:::

:::

::: {.pf-step #irred}

$f$ is irreducible over $\QQ$.

::: pf-proof

No root of $f$ is real, so $f$ has no linear factor over $\QQ$. A monic quadratic factor over $\QQ$ has two roots of $f$ as its roots. Let $r=\sqrt3+i\sqrt5$. Up to the sign symmetry $x\mapsto-x$, the pairs of roots are $\{r,\bar r\}$, $\{r,-\bar r\}$ and $\{r,-r\}$. Their factors are $x^2-2\sqrt3\,x+8$, $x^2-2i\sqrt5\,x-8$ and $x^2-r^2=x^2+2-2i\sqrt{15}$. None of these has rational coefficients.

:::

:::

::: {.pf-step #field}

$K=\QQ(\sqrt3,\sqrt{-5})$ and $[K:\QQ]=4$.

::: pf-proof

By Step [](#roots){.pf-ref}, every root lies in $\QQ(\sqrt3,i\sqrt5)$. Conversely $\sqrt3=(r+\bar r)/2$ and $i\sqrt5=(r-\bar r)/2$ lie in $K$. The field $\QQ(\sqrt3)\subset\RR$ does not contain $i\sqrt5$, so $[K:\QQ]=[K:\QQ(\sqrt3)][\QQ(\sqrt3):\QQ]=2\cdot2=4$.

:::

:::

::: {.pf-step #group}

$G=\{1,\sigma,\tau,\sigma\tau\}\cong C_2\times C_2$, where
$$
\sigma:\sqrt3\mapsto-\sqrt3,\ \sqrt{-5}\mapsto\sqrt{-5},\qquad
\tau:\sqrt3\mapsto\sqrt3,\ \sqrt{-5}\mapsto-\sqrt{-5}.
$$

::: pf-proof

$K/\QQ$ is a splitting field in characteristic $0$, so it is Galois, and $\cardinality{G}=4$ by Step [](#field){.pf-ref}. Every element of $G$ sends $\sqrt3$ to a root of $x^2-3$ and $\sqrt{-5}$ to a root of $x^2+5$, and it is determined by these two images. This gives at most four automorphisms, so all four sign choices occur. Each nonidentity element has order $2$, so $G\cong C_2\times C_2$.

:::

:::

::: {.pf-step #corr}

The subgroups of $G$ and the intermediate fields correspond as
$$
\begin{aligned}
\{1\}&\leftrightarrow K, &
\langle\sigma\rangle&\leftrightarrow\QQ(\sqrt{-5}), &
\langle\tau\rangle&\leftrightarrow\QQ(\sqrt3),\\
\langle\sigma\tau\rangle&\leftrightarrow\QQ(\sqrt{-15}), &
G&\leftrightarrow\QQ.
\end{aligned}
$$

::: pf-proof

$C_2\times C_2$ has exactly three subgroups of order $2$. Each displayed quadratic field is fixed by the displayed generator: $\sigma$ fixes $\sqrt{-5}$, $\tau$ fixes $\sqrt3$, and $\sigma\tau(\sqrt3\sqrt{-5})=(-\sqrt3)(-\sqrt{-5})=\sqrt{-15}$. By the fundamental theorem of Galois theory, the fixed field of a subgroup of order $2$ has degree $2$ over $\QQ$, so it equals the displayed quadratic field.

:::

:::

::: pf-qed

Steps [](#roots){.pf-ref} and [](#field){.pf-ref} prove part (a), Steps [](#irred){.pf-ref} and [](#group){.pf-ref} prove part (b), and Step [](#corr){.pf-ref} proves part (c).

:::

:::

:::
