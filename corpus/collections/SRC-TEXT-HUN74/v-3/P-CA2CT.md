---
schema: qual/card@1
id: P-CA2CT
kind: problem
title: Algebraic elements inside an algebraically closed field form an algebraic closure
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved UGA problem-set reproduction of the statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If $F$ is algebraically closed and $E$ is the set of all elements in $F$ that are algebraic over a field $K$, then $E$ is an algebraic closure of $K$.
:::

::: {.solution}
Assume $K\subseteq F$, with $F$ algebraically closed, and set
\[
E=\{a\in F:a\text{ is algebraic over }K\}.
\]

::: pf

::: pf-step

The set $E$ is a subfield of $F$ containing $K$.

::: pf-proof

Every element of $K$ is algebraic over $K$, so $K\subseteq E$. If
$a,b\in E$, then $K(a,b)/K$ is finite. Hence every element of $K(a,b)$ is
algebraic over $K$. In particular,
\[
a-b,\quad ab\in E,
\]
and, if $a\ne0$, also $a^{-1}\in E$. Thus $E$ is a subfield of $F$.

:::

:::

::: {.pf-step #s2}

The extension $E/K$ is algebraic.

::: pf-proof

This is immediate from the definition of $E$: every element of $E$ is algebraic
over $K$.

:::

:::

::: {.pf-step #s3}

Every nonconstant polynomial in $E[x]$ has a root in $E$.

::: pf-proof

Let
\[
f(x)=a_0+a_1x+\cdots+a_nx^n\in E[x],
\qquad n>0.
\]
The field
\[
K'=K(a_0,\ldots,a_n)
\]
is a finite extension of $K$, since each coefficient is algebraic over $K$.

Because $F$ is algebraically closed, $f$ has a root $\alpha\in F$. The element
$\alpha$ is algebraic over $K'$ because it satisfies the nonzero polynomial
$f\in K'[x]$. Hence $K'(\alpha)/K'$ is finite. Since $K'/K$ is finite, the
tower law shows that $K'(\alpha)/K$ is finite. Therefore $\alpha$ is algebraic
over $K$, so $\alpha\in E$.

:::

:::

::: {.pf-step #s4}

The field $E$ is algebraically closed.

::: pf-proof

By step [](#s3){.pf-ref} every nonconstant polynomial in $E[x]$ has a root in $E$. Factoring off
a linear factor and repeating by induction on degree shows that every polynomial
in $E[x]$ splits into linear factors over $E$. Thus $E$ is algebraically closed.

:::

:::

::: pf-step

Hence $E$ is an algebraic closure of $K$.

::: pf-proof

By step [](#s2){.pf-ref}, $E/K$ is algebraic, and by step [](#s4){.pf-ref}, $E$ is algebraically closed. These are
exactly the defining properties of an algebraic closure of $K$.

:::

:::

:::

:::
