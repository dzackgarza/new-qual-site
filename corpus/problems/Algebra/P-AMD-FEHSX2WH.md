---
schema: qual/card@1
id: P-AMD-FEHSX2WH
kind: problem
title: The nilradical is contained in the Jacobson radical, i.e.
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Nilpotence
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
The nilradical is contained in the Jacobson radical, i.e.
\[
\nilrad{R} \subseteq J(R)
.\]
:::

::: {.solution}
<1>1. Let $x \in \nilrad{R}$, so $x^n = 0$ for some $n \ge 1$.
::: {.proof}
definition of the nilradical.
:::

<1>2. Let $M$ be any maximal ideal of $R$.
::: {.proof}
take an arbitrary maximal ideal.
:::

<1>3. Suppose $x \notin M$. Then $(x) + M = R$ (since $M$ is maximal), so $1 = rx + m$ for some $r \in R$, $m \in M$.
::: {.proof}
maximality of $M$.
:::

<1>4. Then $1 = (rx + m)^n = (rx)^n + (\text{terms in } M) \in M$ (since $x^n = 0$ makes $(rx)^n = r^n x^n = 0$, and all other terms contain a factor of $m \in M$).
::: {.proof}
<1>1 and <1>3, expanding by the binomial theorem.
:::

<1>5. This contradicts $M$ being a proper ideal (it contains $1$).
::: {.proof}
<1>4.
:::

<1>6. Hence $x \in M$ for every maximal ideal $M$.
::: {.proof}
<1>5 (contradiction forces $x \in M$).
:::

<1>7. Therefore $x \in \bigcap_{M \text{ maximal}} M = J(R)$.
::: {.proof}
<1>6 and the definition of the Jacobson radical.
:::

<1>8. Hence $\nilrad{R} \subseteq J(R)$.
::: {.proof}
<1>1 and <1>7 (for arbitrary $x \in \nilrad{R}$).
:::

<1>9. Q.E.D.
::: {.proof}
<1>8.
:::
:::
