---
schema: qual/card@1
id: P-HCAO6
kind: problem
title: Irreducible elements generate maximal ideals in a principal ideal domain
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Factorization
  - Maximal Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $R$ be a principal ideal domain and let $a \in R$ be a nonzero nonunit.
Show that $a$ is irreducible if and only if the ideal $(a)$ is maximal.
:::

::: solution
<1>1. If $a$ is irreducible, then $(a)$ is maximal.
::: proof
Suppose
\[
(a)\subseteq I\subseteq R.
\]
Since $R$ is a PID, $I=(b)$ for some $b\in R$. The inclusion
$(a)\subseteq(b)$ means that $a=bc$ for some $c\in R$.

Because $a$ is irreducible, either $b$ or $c$ is a unit. If $b$ is a unit,
then $I=(b)=R$. If $c$ is a unit, then $b$ is associate to $a$, so
$I=(b)=(a)$. Thus no proper ideal lies strictly between $(a)$ and $R$, and
$(a)$ is maximal.
:::

<1>2. If $(a)$ is maximal, then $a$ is irreducible.
::: proof
Suppose
\[
a=bc.
\]
Then
\[
(a)\subseteq(b)\subseteq R.
\]
Maximality of $(a)$ gives either $(b)=(a)$ or $(b)=R$.

If $(b)=R$, then $b$ is a unit. If $(b)=(a)$, then $b=au$ for some $u\in R$;
substituting into $a=bc$ gives
\[
a=auc.
\]
Since $R$ is a domain and $a\ne0$, cancellation yields $uc=1$, so $c$ is a
unit. Therefore every factorization of $a$ has a unit factor, and $a$ is
irreducible.
:::
:::
