---
schema: qual/card@1
id: P-CDHB5
kind: problem
title: An abelian group is a $\ZZ$-module in a unique way
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Abelian Groups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
review: draft
---
::: {.problem}
Let $A$ be an abelian group, and show $A$ is a $\ZZ\dash$module in a unique way.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There is a $\ZZ$-action on $A$ defined by repeated addition.

::: pf-proof

For $a\in A$, define
$$
n\cdot a=
\begin{cases}
\underbrace{a+\cdots+a}_{n\text{ terms}},&n>0,\\
0,&n=0,\\
-\underbrace{(a+\cdots+a)}_{-n\text{ terms}},&n<0.
\end{cases}
$$

:::

:::

::: {.pf-step #s2}

This action makes $A$ a $\ZZ$-module.

::: pf-proof

For $m,n\in\ZZ$ and $a,b\in A$, repeated addition and the abelian group law give
$$
n\cdot(a+b)=n\cdot a+n\cdot b,
$$
$$
(m+n)\cdot a=m\cdot a+n\cdot a,
$$
and
$$
(mn)\cdot a=m\cdot(n\cdot a).
$$
Also $1\cdot a=a$. Hence all module axioms hold.

:::

:::

::: {.pf-step #s3}

This $\ZZ$-module structure is unique.

::: pf-proof

Let $A$ carry any $\ZZ$-module structure. The module axiom gives $1\cdot a=a$. For $n>0$,
$$
n\cdot a=(\underbrace{1+\cdots+1}_{n\text{ terms}})\cdot a
=\underbrace{a+\cdots+a}_{n\text{ terms}},
$$
and
$$
(-n)\cdot a=-(n\cdot a).
$$
Thus the scalar action is forced to be exactly the action constructed in step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Therefore every abelian group admits $\boxed{\text{a unique }\ZZ\text{-module structure}}$.

::: pf-proof

Existence is step [](#s2){.pf-ref} and uniqueness is step [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
