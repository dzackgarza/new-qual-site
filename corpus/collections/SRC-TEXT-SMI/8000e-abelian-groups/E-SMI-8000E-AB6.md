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
---

::: {.exercise}
Prove that $(\QQ,+)$ is not a free abelian group, i.e. is not isomorphic to a coproduct of either a finite or an infinite number of copies of $\ZZ$.

[Hint: show that $\Hom(\QQ,\ZZ) = \{0\}$, but that $\Hom(G,\ZZ)$ is not zero if $G$ is free abelian.]
:::


::: solution
<1>1. Every group homomorphism $\mathbb Q\to\mathbb Z$ is zero.
::: proof
Let
$$
f:\mathbb Q\longrightarrow\mathbb Z
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
integer with this property is $0$: if $m\ne0$, take $n>|m|$, which cannot
divide $m$. Hence
$$
f(1)=0.
$$

Now for any rational $a/b$ with $b>0$,
$$
b f(a/b)=f(a)=a f(1)=0.
$$
Since $\mathbb Z$ is torsion-free,
$$
f(a/b)=0.
$$
Therefore
$$
\boxed{\operatorname{Hom}(\mathbb Q,\mathbb Z)=0.}
$$
:::

<1>2. Every nonzero free abelian group admits a nonzero homomorphism to $\mathbb Z$.
::: proof
Let
$$
G=\bigoplus_{i\in I}\mathbb Z e_i
$$
be a nonzero free abelian group. Choose one basis element $e_{i_0}$. Define
$$
\pi_{i_0}:G\longrightarrow\mathbb Z
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
\operatorname{Hom}(G,\mathbb Z)\ne0.
$$
This works for finite or infinite bases alike.
:::

<1>3. Conclude that $(\mathbb Q,+)$ is not free abelian.
::: proof
The group $\mathbb Q$ is nonzero. If it were free abelian, step <1>2 would
give a nonzero homomorphism
$$
\mathbb Q\longrightarrow\mathbb Z,
$$
contradicting step <1>1. Therefore
$$
\boxed{(\mathbb Q,+)\text{ is not a free abelian group}.}
$$
:::
:::
