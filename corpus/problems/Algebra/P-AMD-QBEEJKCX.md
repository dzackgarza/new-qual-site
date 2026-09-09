---
schema: qual/card@1
id: P-AMD-QBEEJKCX
kind: problem
title: The nilradical is the intersection of all prime ideals, i.e.
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---


::: {.problem}
Prove that the nilradical of a commutative ring $R$ is the intersection of all prime ideals:
\[
\sqrt{(0)}=\bigcap_{\mathfrak p\in\operatorname{Spec}(R)}\mathfrak p.
\]
:::

::: {.solution}
<1>1. Every nilpotent element belongs to every prime ideal.
::: {.proof}
Let $x\in R$ be nilpotent, so $x^n=0$ for some $n\ge1$, and let $\mathfrak p$ be prime. Since
\[
x^n=0\in\mathfrak p,
\]
primality implies $x\in\mathfrak p$. Hence
\[
\sqrt{(0)}\subseteq\bigcap_{\mathfrak p\in\operatorname{Spec}(R)}\mathfrak p.
\]
:::

<1>2. If $x$ is not nilpotent, there exists a prime ideal not containing $x$.
::: {.proof}
Assume $x$ is not nilpotent and set
\[
S=\{1,x,x^2,\ldots\}.
\]
Then $0\notin S$. Consider the set of ideals of $R$ disjoint from $S$, ordered by inclusion. It is nonempty because $(0)$ is disjoint from $S$. The union of a chain of such ideals is again an ideal disjoint from $S$, so Zorn's lemma gives a maximal ideal $\mathfrak p$ among those disjoint from $S$.

We show that $\mathfrak p$ is prime. Suppose $ab\in\mathfrak p$ but $a,b\notin\mathfrak p$. By maximality, both larger ideals $\mathfrak p+(a)$ and $\mathfrak p+(b)$ meet $S$. Thus there exist
\[
s_1=u+ra\in S,\qquad s_2=v+tb\in S
\]
with $u,v\in\mathfrak p$. Their product is
\[
s_1s_2=uv+utb+vra+rtab\in\mathfrak p,
\]
because $u,v,ab\in\mathfrak p$. But $s_1s_2\in S$ since $S$ is multiplicatively closed, contradicting $\mathfrak p\cap S=\varnothing$. Hence $\mathfrak p$ is prime.

Since $x\in S$ and $\mathfrak p\cap S=\varnothing$, we have $x\notin\mathfrak p$.
:::

<1>3. Therefore
\[
\sqrt{(0)}=\bigcap_{\mathfrak p\in\operatorname{Spec}(R)}\mathfrak p.
\]
::: {.proof}
By <1>1, the nilradical is contained in every prime ideal. By <1>2, every nonnilpotent element is omitted by at least one prime ideal. Thus an element lies in every prime ideal exactly when it is nilpotent.
:::
:::
