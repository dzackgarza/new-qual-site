---
schema: qual/card@1
id: E-AMD-UEHZOJ3K
kind: problem
title: Nilradical is the intersection of all prime ideals
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Prime Ideals
  - Ideals
relations: []
review: draft
---

::: {.exercise}
Show that the nilradical of a commutative ring $R$ is equal to the intersection of all prime ideals of $R$.
:::

::: {.solution}
Let $R$ be a commutative ring with identity, and put $P=\bigcap_{\mathfrak p\in\operatorname{Spec}(R)}\mathfrak p$.

<1>1. $\operatorname{Nil}(R)\subseteq P$.

::: {.proof}
Let $x^n=0$ with $n\ge1$, and let $\mathfrak p$ be prime.
Then $x^n=0\in\mathfrak p$.
If $x^k\in\mathfrak p$ with $k\ge2$, then $x\cdot x^{k-1}\in\mathfrak p$ gives $x\in\mathfrak p$ or $x^{k-1}\in\mathfrak p$; induction on $k$ gives $x\in\mathfrak p$.
:::

<1>2. For $f\in R$ not nilpotent, the family $\mathcal F$ of ideals $I$ with $I\cap\{f^n:n\ge0\}=\varnothing$ has a maximal element $\mathfrak p$.

::: {.proof}
Put $S=\{f^n:n\ge0\}$; since $f$ is not nilpotent, $0\notin S$, so $(0)\in\mathcal F$.
The union of a nonempty chain in $\mathcal F$ is an ideal disjoint from $S$, hence an upper bound in $\mathcal F$.
Zorn's lemma gives a maximal element.
:::

<1>3. The ideal $\mathfrak p$ of step <1>2 is prime and $f\notin\mathfrak p$.

::: {.proof}
Since $1=f^0\in S$, $\mathfrak p\neq R$, and $f=f^1\in S$ gives $f\notin\mathfrak p$.
Let $a,b\notin\mathfrak p$.
By maximality, $\mathfrak p+(a)$ and $\mathfrak p+(b)$ meet $S$: $f^m\in\mathfrak p+(a)$ and $f^n\in\mathfrak p+(b)$ for some $m,n\ge0$.
Then $f^{m+n}\in(\mathfrak p+(a))(\mathfrak p+(b))\subseteq\mathfrak p+(ab)$.
If $ab\in\mathfrak p$, then $f^{m+n}\in\mathfrak p\cap S=\varnothing$, a contradiction; so $ab\notin\mathfrak p$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 gives $\operatorname{Nil}(R)\subseteq P$.
Steps <1>2 and <1>3 show that every non-nilpotent $f$ lies outside some prime ideal, so $P\subseteq\operatorname{Nil}(R)$.
:::
:::
