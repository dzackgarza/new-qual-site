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

::: problem
Let $u = \sqrt{2 + \sqrt{2}}$, $v = \sqrt{2 - \sqrt{2}}$, and $E = \QQ(u)$.

a. Find (with justification) the minimal polynomial $f(x)$ of $u$ over $\QQ$.

b. Show $v\in E$, and show that $E$ is a splitting field of $f(x)$ over $\QQ$.

c. Determine the Galois group of $E$ over $\QQ$ and determine all of the intermediate fields $F$ such that $\QQ \subset F \subset E$.
:::

::: {.solution}
**Goal.** For $u = \sqrt{2+\sqrt2}$, $v = \sqrt{2-\sqrt2}$, $E = \QQ(u)$: find the minimal polynomial, show $E$ is a splitting field, and determine the Galois group and intermediate fields.

<1>1. (a) The minimal polynomial of $u$ is $f(x) = x^4 - 4x^2 + 2$.
<2>1. $u^2 = 2 + \sqrt2$, so $(u^2 - 2)^2 = 2$, i.e. $u^4 - 4u^2 + 2 = 0$.
::: {.proof}
square $u^2 - 2 = \sqrt2$.
:::
<2>2. $f(x) = x^4 - 4x^2 + 2$ is irreducible over $\QQ$.
::: {.proof}
it is Eisenstein at $p = 2$ (leading coefficient $1$, middle coefficient $-4$ divisible by $2$, constant $2$ divisible by $2$ but not $4$).
:::
<2>3. Hence $f$ is the minimal polynomial of $u$, and $[\QQ(u):\QQ] = 4$.
::: {.proof}
$f$ is monic, irreducible, and has $u$ as a root.
:::

<1>2. (b) $v \in E$ and $E$ is a splitting field of $f$.
<2>1. $uv = \sqrt{(2+\sqrt2)(2-\sqrt2)} = \sqrt{4 - 2} = \sqrt2$.
::: {.proof}
multiply the two radicands.
:::
<2>2. Hence $v = \sqrt2 / u \in \QQ(u) = E$.
::: {.proof}
$\sqrt2 = u^2 - 2 \in E$, so $v = \sqrt2/u \in E$.
:::
<2>3. The roots of $f$ are $\pm u, \pm v$.
::: {.proof}
$f(x) = (x^2 - (2+\sqrt2))(x^2 - (2-\sqrt2))$, so the roots are $\pm\sqrt{2+\sqrt2} = \pm u$ and $\pm\sqrt{2-\sqrt2} = \pm v$.
:::
<2>4. All four roots lie in $E$, so $E$ is the splitting field of $f$.
::: {.proof}
$u \in E$ and $v \in E$ by <1>2.2, so $\pm u, \pm v \in E$.
:::

<1>3. (c) The Galois group is $\ZZ/4$, and the intermediate fields are $\QQ$, $\QQ(\sqrt2)$, $E$.
<2>1. $E/\QQ$ is Galois of degree $4$.
::: {.proof}
$E$ is the splitting field of the separable polynomial $f$ (char $0$), so it is Galois, and $[E:\QQ] = 4$.
:::
<2>2. $\Gal(E/\QQ)$ has order $4$.
::: {.proof}
$|\Gal(E/\QQ)| = [E:\QQ] = 4$.
:::
<2>3. $\Gal(E/\QQ) \cong \ZZ/4$.
::: {.proof}
the Galois group acts transitively on the four roots $\pm u, \pm v$; the automorphism $u \mapsto v$ has order $4$ (it cycles $u \mapsto v \mapsto -u \mapsto -v \mapsto u$), so the group is cyclic of order $4$.
:::
<2>4. The intermediate fields correspond to subgroups of $\ZZ/4$: the whole group (fixed field $\QQ$), the subgroup of order $2$ (fixed field $\QQ(\sqrt2)$), and the trivial subgroup (fixed field $E$).
::: {.proof}
$\ZZ/4$ has subgroups $\theset{0}, \theset{0,2}, \ZZ/4$; the fixed field of $\theset{0,2}$ is $\QQ(\sqrt2)$ (since $\sqrt2 = u^2 - 2$ is fixed by the order-2 automorphism $u \mapsto -u$).
:::

<1>4. Q.E.D.
::: {.proof}
<1>1, <1>2, <1>3 answer (a), (b), (c).
:::
:::
