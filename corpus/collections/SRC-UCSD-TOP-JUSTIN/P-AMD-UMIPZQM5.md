---
schema: qual/card@1
id: P-AMD-UMIPZQM5
kind: problem
title: A free resolution of $\QQ$ as a $\ZZ$-module
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Modules
relations: []
review: draft
---

::: {.problem}
Find a free resolution of $\QQ$ as a $\ZZ$-module.
:::

::: {.solution}
<1>1. Let
$$
F_0=\bigoplus_{n\ge1}\mathbb Z e_n,
\qquad
F_1=\bigoplus_{n\ge1}\mathbb Z f_n.
$$
Define
$$
\varepsilon:F_0\to\mathbb Q,
\qquad
\varepsilon(e_n)=\frac1{n!},
$$
and
$$
d:F_1\to F_0,
\qquad
d(f_n)=e_n-(n+1)e_{n+1}.
$$
::: {.proof}
Both $F_0$ and $F_1$ are free abelian groups. The formula for $d$ is chosen from the relation
$$
\frac1{n!}=(n+1)\frac1{(n+1)!}.
$$
:::

<1>2. The map $\varepsilon$ is surjective and $\varepsilon d=0$.
::: {.proof}
Every rational number $a/b$ is an integer multiple of $1/n!$ once $n$ is large enough that $b\mid n!$, so $\varepsilon$ is onto. Also
$$
\varepsilon(d(f_n))=\frac1{n!}-(n+1)\frac1{(n+1)!}=0.
$$
:::

<1>3. The map $d$ is injective.
::: {.proof}
If a finite sum $\sum_{n=1}^N c_n f_n$ maps to zero, inspect the coefficient of $e_1$ to obtain $c_1=0$. Then the coefficient of $e_2$ gives $c_2=0$, and inductively every $c_n=0$.
:::

<1>4. We have $\ker\varepsilon=\operatorname{im}d$.
::: {.proof}
Take a finite sum $x=\sum_{n=1}^N a_n e_n\in\ker\varepsilon$. Modulo $\operatorname{im}d$, the relations $e_n=(n+1)e_{n+1}$ imply
$$
x\equiv\left(\sum_{n=1}^N a_n\frac{N!}{n!}\right)e_N.
$$
The condition $\varepsilon(x)=0$ says
$$
0=N!\varepsilon(x)=\sum_{n=1}^N a_n\frac{N!}{n!},
$$
so $x\equiv0$ modulo $\operatorname{im}d$. Thus $x\in\operatorname{im}d$.
:::

<1>5. Therefore
$$
\boxed{0\longrightarrow F_1\xrightarrow{d}F_0\xrightarrow{\varepsilon}\mathbb Q\longrightarrow0}
$$
is a free resolution of $\mathbb Q$ as a $\mathbb Z$-module.
::: {.proof}
Exactness follows from <1>2--<1>4, and both $F_0,F_1$ are free by construction.
:::
:::
