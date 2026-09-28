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
For $n\in\mathbb Z$ and $a\in A$ put
\[
n\cdot a=
\begin{cases}
\underbrace{a+\cdots+a}_{n\text{ times}},&n>0,\\
0,&n=0,\\
-(\underbrace{a+\cdots+a}_{(-n)\text{ times}}),&n<0.
\end{cases}
\]

<1>1. This rule is a $\mathbb Z$-module structure on $A$.

::: {.proof}
Since $A$ is abelian, expanding sums gives $n\cdot(a+b)=n\cdot a+n\cdot b$ and $(m+n)\cdot a=m\cdot a+n\cdot a$, and regrouping repeated addition gives $(mn)\cdot a=m\cdot(n\cdot a)$. By definition $1\cdot a=a$.
:::

<1>2. Every $\mathbb Z$-module structure on $A$ agrees with the rule of step <1>1.

::: {.proof}
Let $A$ carry a $\mathbb Z$-module structure. The module axioms give $1\cdot a=a$ and, by distributivity over $1+\cdots+1$,
\[
n\cdot a=\underbrace{(1\cdot a)+\cdots+(1\cdot a)}_{n\text{ times}}
\]
for $n>0$. Also $0\cdot a=(0+0)\cdot a=0\cdot a+0\cdot a$, so $0\cdot a=0$, and $n\cdot a+(-n)\cdot a=0\cdot a=0$, so $(-n)\cdot a=-(n\cdot a)$.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 gives existence and step <1>2 gives uniqueness of the $\mathbb Z$-module structure on $A$.
:::
:::
