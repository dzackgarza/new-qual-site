---
schema: qual/card@1
id: P-JOGCB
kind: problem
title: Minimal polynomial of $\sqrt{2+\sqrt{2}}$; $\QQ(\sqrt{2+\sqrt{2}})$ as splitting
  field containing $\sqrt{2-\sqrt{2}}$; Galois group and intermediate fields
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---
::: {.problem}
Let $u = \sqrt{2 + \sqrt{2}}$, $v = \sqrt{2 - \sqrt{2}}$, and $E = \QQ(u)$.

a. Find (with justification) the minimal polynomial $f(x)$ of $u$ over $\QQ$.

b. Show $v\in E$, and show that $E$ is a splitting field of $f(x)$ over $\QQ$.

c. Determine the Galois group of $E$ over $\QQ$ and determine all of the intermediate fields $F$ such that $\QQ \subset F \subset E$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The minimal polynomial of $u$ is
$$
\boxed{f(x)=x^4-4x^2+2}.
$$

::: pf-proof

::: pf-step

$u^2 = 2 + \sqrt2$, so $(u^2 - 2)^2 = 2$, i.e. $u^4 - 4u^2 + 2 = 0$.

::: pf-proof

square $u^2 - 2 = \sqrt2$.

:::

:::

::: pf-step

$f(x) = x^4 - 4x^2 + 2$ is irreducible over $\QQ$.

::: pf-proof

it is Eisenstein at $p = 2$ (leading coefficient $1$, middle coefficient $-4$ divisible by $2$, constant $2$ divisible by $2$ but not $4$).

:::

:::

::: pf-step

Hence $f$ is the minimal polynomial of $u$, and $[\QQ(u):\QQ] = 4$.

::: pf-proof

$f$ is monic, irreducible, and has $u$ as a root.

:::

:::

:::

:::

::: {.pf-step #s2}

The element $v$ belongs to $E$, and $E$ is the splitting field of $f$ over $\QQ$.

::: pf-proof

::: pf-step

$uv = \sqrt{(2+\sqrt2)(2-\sqrt2)} = \sqrt{4 - 2} = \sqrt2$.

::: pf-proof

multiply the two radicands.

:::

:::

::: {.pf-step #s2-2}

Hence $v = \sqrt2 / u \in \QQ(u) = E$.

::: pf-proof

$\sqrt2 = u^2 - 2 \in E$, so $v = \sqrt2/u \in E$.

:::

:::

::: pf-step

The roots of $f$ are $\pm u, \pm v$.

::: pf-proof

$f(x) = (x^2 - (2+\sqrt2))(x^2 - (2-\sqrt2))$, so the roots are $\pm\sqrt{2+\sqrt2} = \pm u$ and $\pm\sqrt{2-\sqrt2} = \pm v$.

:::

:::

::: pf-step

All four roots lie in $E$, so $E$ is the splitting field of $f$.

::: pf-proof

$u \in E$ and $v \in E$ by step [](#s2-2){.pf-ref}, so $\pm u, \pm v \in E$.

:::

:::

:::

:::

::: {.pf-step #s3}

The Galois group and the complete list of intermediate fields are
$$
\boxed{\Gal(E/\QQ)\cong C_4,\qquad
\QQ\subset\QQ(\sqrt2)\subset E}.
$$

::: pf-proof

::: pf-step

$E/\QQ$ is Galois of degree $4$.

::: pf-proof

$E$ is the splitting field of the separable polynomial $f$ (char $0$), so it is Galois, and $[E:\QQ] = 4$.

:::

:::

::: pf-step

$\Gal(E/\QQ)$ has order $4$.

::: pf-proof

$\cardinality{\Gal(E/\QQ)} = [E:\QQ] = 4$.

:::

:::

::: pf-step

$\Gal(E/\QQ) \cong \ZZ/4$.

::: pf-proof

Since $f$ is the minimal polynomial of $u$ and $E$ is its splitting field, the assignment $\sigma(u)=v$ extends to an automorphism. One has $\sigma(\sqrt2)=v^2-2=-\sqrt2$, so $\sigma(v)=\sigma(\sqrt2/u)=-\sqrt2/v=-u$. Thus $\sigma$ has order four, and the Galois group of order four is cyclic.

:::

:::

::: pf-step

The intermediate fields correspond to subgroups of $\ZZ/4$: the whole group (fixed field $\QQ$), the subgroup of order $2$ (fixed field $\QQ(\sqrt2)$), and the trivial subgroup (fixed field $E$).

::: pf-proof

$\ZZ/4$ has subgroups $\theset{0}, \theset{0,2}, \ZZ/4$; the fixed field of $\theset{0,2}$ is $\QQ(\sqrt2)$ (since $\sqrt2 = u^2 - 2$ is fixed by the order-2 automorphism $u \mapsto -u$).

:::

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove parts (a), (b), and (c), respectively.

:::

:::

:::
