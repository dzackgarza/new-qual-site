---
schema: qual/card@1
id: E-AMD-YITMZNBK
kind: problem
title: In a PID, a nonzero $x$ is irreducible iff $(x)$ is maximal
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Maximal Ideals
  - Factorization
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

::: {.exercise}
Let $R$ be a PID and let $0\neq x\in R$. Show that $x$ is irreducible if and only if the ideal $\gens{x}$ is maximal.
:::


::: {.solution}
Let $R$ be a PID and $0\neq x\in R$.

<1>1. If $x$ is irreducible, then $(x)$ is a maximal ideal.
::: {.proof}
Since $x$ is irreducible, it is a nonunit, so $(x)$ is proper. Let $I$ be an ideal with
\[
(x)\subseteq I\subsetneq R.
\]
Because $R$ is a PID, $I=(a)$ for some $a\in R$. The inclusion $(x)\subseteq(a)$ gives $x=ab$ for some $b\in R$. Since $I$ is proper, $a$ is not a unit. Irreducibility of $x$ therefore forces $b$ to be a unit. Hence
\[
(x)=(ab)=(a)=I.
\]
Thus there is no proper ideal strictly between $(x)$ and $R$, so $(x)$ is maximal.
:::

<1>2. If $(x)$ is maximal, then $x$ is irreducible.
::: {.proof}
Since $(x)$ is proper, $x$ is not a unit. Suppose
\[
x=ab.
\]
Then
\[
(x)\subseteq(a)\subseteq R.
\]
Maximality of $(x)$ implies either $(a)=R$ or $(a)=(x)$. In the first case $a$ is a unit. In the second case $a=ux$ for some $u\in R$, so
\[
x=ab=uxb.
\]
Because $R$ is a domain and $x\neq0$, cancellation gives $ub=1$, so $b$ is a unit. Thus every factorization of $x$ has a unit factor, and $x$ is irreducible.
:::

<1>3. Therefore, for every nonzero element $x$ of a PID,
\[
x\text{ is irreducible}\quad\Longleftrightarrow\quad (x)\text{ is maximal}.
\]
::: {.proof}
Combine <1>1 and <1>2.
:::
:::
