---
schema: qual/card@1
id: E-SMI-8000E-AB6
kind: problem
title: $(\QQ,+)$ is not free abelian
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Free Modules
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the statement and Hom(Q,Z) hint with the local 8000e extraction, abelian-groups exercise 6."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved every homomorphism Q→Z vanishes by divisibility, then exhibited a nonzero coordinate projection from every nonzero free abelian group to Z."
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed problem, Smith Math 8000 packet 8000e.pdf page 1,
    abelian-groups problem 6: "Prove that (Q,+) is not a free abelian group, i.e.
    is not isomorpic to a coproduct of either a finite or an infinite number of
    copies of Z. [hint: show that Hom(Q,Z) = {0}, but that Hom(G,Z) is not zero,
    if G is free abelian.]" The card states exactly this with the printed hint.
    The proof was checked: f(1) = n f(1/n) makes f(1) divisible by every n, so
    f(1) = 0, and then b f(a/b) = a f(1) = 0 with Z torsion-free gives f = 0; and
    a nonzero free abelian group has a basis element, whose coordinate projection
    is a nonzero homomorphism to Z, finite support making it well defined for
    infinite index sets as the printed statement requires. Complete; no defect.
---

::: {.exercise}
Prove that $(\QQ,+)$ is not a free abelian group, i.e. is not isomorphic to a coproduct of either a finite or an infinite number of copies of $\ZZ$.

[Hint: show that $\Hom(\QQ,\ZZ) = \{0\}$, but that $\Hom(G,\ZZ)$ is not zero if $G$ is free abelian.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every group homomorphism $\QQ\to\ZZ$ is zero.

::: pf-proof

Let
$$
f:\QQ\longrightarrow\ZZ
$$
be a homomorphism of additive groups and put
$$
m=f(1).
$$
For every positive integer $n$,
$$
1=n\left(\frac1n\right),
$$
so
$$
m=f(1)=n f(1/n).
$$
Thus the integer $m$ is divisible by every positive integer $n$. The only
integer with this property is $0$: if $m\ne0$, take $n>\abs{m}$, which cannot
divide $m$. Hence
$$
f(1)=0.
$$

Now for any rational $a/b$ with $b>0$,
$$
b f(a/b)=f(a)=a f(1)=0.
$$
Since $\ZZ$ is torsion-free,
$$
f(a/b)=0.
$$
Therefore
$$
\boxed{\operatorname{Hom}(\QQ,\ZZ)=0.}
$$

:::

:::

::: {.pf-step #s2}

Every nonzero free abelian group admits a nonzero homomorphism to $\ZZ$.

::: pf-proof

Let
$$
G=\bigoplus_{i\in I}\ZZ e_i
$$
be a nonzero free abelian group. Choose one basis element $e_{i_0}$. Define
$$
\pi_{i_0}:G\longrightarrow\ZZ
$$
by taking the coefficient of $e_{i_0}$:
$$
\pi_{i_0}\left(\sum_{i\in I} n_i e_i\right)=n_{i_0}.
$$
Every element of the direct sum has finite support, so this is well defined.
It is a homomorphism and
$$
\pi_{i_0}(e_{i_0})=1,
$$
so it is nonzero. Hence
$$
G\ne0\text{ free abelian}
\quad\Longrightarrow\quad
\operatorname{Hom}(G,\ZZ)\ne0.
$$
This works for finite or infinite bases alike.

:::

:::

::: pf-step

Conclude that $(\QQ,+)$ is not free abelian.

::: pf-proof

The group $\QQ$ is nonzero. If it were free abelian, step [](#s2){.pf-ref} would
give a nonzero homomorphism
$$
\QQ\longrightarrow\ZZ,
$$
contradicting step [](#s1){.pf-ref}. Therefore
$$
\boxed{(\QQ,+)\text{ is not a free abelian group}.}
$$

:::

:::

:::

:::
