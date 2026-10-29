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
Let $R$ be a commutative ring with identity, and put $P=\bigcap_{\mfp\in\Spec(R)}\mfp$.

::: pf

::: {.pf-step #nilrad-subset-p}
$\operatorname{Nil}(R)\subseteq P$.

::: pf-proof
Let $x^n=0$ with $n\ge1$, and let $\mfp$ be prime.
Then $x^n=0\in\mfp$.
If $x^k\in\mfp$ with $k\ge2$, then $x\cdot x^{k-1}\in\mfp$ gives $x\in\mfp$ or $x^{k-1}\in\mfp$; induction on $k$ gives $x\in\mfp$.
:::

:::

::: {.pf-step #maximal-element-exists}
For $f\in R$ not nilpotent, the family $\mathcal F$ of ideals $I$ with $I\cap\{f^n:n\ge0\}=\varnothing$ has a maximal element $\mfp$.

::: pf-proof
Put $S=\{f^n:n\ge0\}$; since $f$ is not nilpotent, $0\notin S$, so $(0)\in\mathcal F$.
The union of a nonempty chain in $\mathcal F$ is an ideal disjoint from $S$, hence an upper bound in $\mathcal F$.
Zorn's lemma gives a maximal element.
:::

:::

::: {.pf-step #maximal-element-is-prime}
The ideal $\mfp$ of step [](#maximal-element-exists){.pf-ref} is prime and $f\notin\mfp$.

::: pf-proof
Since $1=f^0\in S$, $\mfp\neq R$, and $f=f^1\in S$ gives $f\notin\mfp$.
Let $a,b\notin\mfp$.
By maximality, $\mfp+(a)$ and $\mfp+(b)$ meet $S$: $f^m\in\mfp+(a)$ and $f^n\in\mfp+(b)$ for some $m,n\ge0$.
Then $f^{m+n}\in(\mfp+(a))(\mfp+(b))\subseteq\mfp+(ab)$.
If $ab\in\mfp$, then $f^{m+n}\in\mfp\cap S=\varnothing$, a contradiction; so $ab\notin\mfp$.
:::

:::

::: pf-qed
Step [](#nilrad-subset-p){.pf-ref} gives $\operatorname{Nil}(R)\subseteq P$.
Steps [](#maximal-element-exists){.pf-ref} and [](#maximal-element-is-prime){.pf-ref} show that every non-nilpotent $f$ lies outside some prime ideal, so $P\subseteq\operatorname{Nil}(R)$.
:::

:::

:::
