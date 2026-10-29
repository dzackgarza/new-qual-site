---
schema: qual/card@1
id: P-UCLAB06W-01
kind: problem
title: Covering the rationals by intervals of arbitrarily small total length
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 of the official UCLA Basic Qual Winter 2006 PDF.
---

::: {.problem}
Show that for each $\varepsilon>0$ there exists a sequence of intervals $(I_n)$ such that
\[
\bigcup_{n=1}^{\infty} I_n\supset\QQ
\qquad\text{and}\qquad
\sum_{n=1}^{\infty}|I_n|<\varepsilon.
\]
:::

::: {.solution}

Fix $\varepsilon>0$.

::: pf

::: pf-step

Enumerate the rational numbers as
$$
\QQ=\{q_1,q_2,\ldots\}.
$$


::: pf-proof

The set $\QQ$ is countable, so such an enumeration exists.

:::

:::

::: {.pf-step #s1-2}

For each $n\ge1$, define
$$
I_n=
\left(
q_n-\frac{\varepsilon}{2^{n+3}},
q_n+\frac{\varepsilon}{2^{n+3}}
\right).
$$
Then
$$
|I_n|=\frac{\varepsilon}{2^{n+2}}.
$$


::: pf-proof

The interval has radius $\varepsilon/2^{n+3}$, so its length is twice that number.

:::

:::

::: {.pf-step #s1-3}

The intervals cover $\QQ$:
$$
\QQ\subseteq\bigcup_{n=1}^{\infty}I_n.
$$


::: pf-proof

For every $n$, the center $q_n$ belongs to $I_n$. Hence every rational number belongs to at least one interval in the union.

:::

:::

::: {.pf-step #s1-4}

Their total length satisfies
$$
\sum_{n=1}^{\infty}|I_n|<\varepsilon.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\sum_{n=1}^{\infty}|I_n|
=
\varepsilon\sum_{n=1}^{\infty}2^{-(n+2)}
=
\frac{\varepsilon}{4}
<\varepsilon.
$$

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} give exactly the two required properties.

:::

:::

:::
