---
schema: qual/card@1
id: P-BKS19-8B
kind: problem
title: Boolean rings are commutative of characteristic 2
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 idempotence argument. Both the characteristic-$2$ and commutativity deductions are correct and do not use an identity element.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the expansion of $(a+a)^2$, additive cancellation yielding $2a=0$, the expansion of $(a+b)^2$, and the conversion of $ab+ba=0$ to $ab=ba$ in characteristic $2$.
---

::: {.problem}
Let $R$ be a ring, possibly noncommutative and possibly without an identity, in which every element is idempotent: $a^2=a$ for all $a\in R$.
Show that $R$ has characteristic $2$ (that is, $2a=0$ for all $a$) and is commutative.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $a\in R$,
$$
2a=0.
$$


::: pf-proof

The element $a+a$ is idempotent, so
$$
(a+a)^2=a+a=2a.
$$
By distributivity and the identity $a^2=a$,
$$
\begin{aligned}
(a+a)^2
&=a^2+a^2+a^2+a^2\\
&=4a.
\end{aligned}
$$
Hence $4a=2a$. Cancelling $2a$ in the additive abelian group of the ring gives $2a=0$.

:::

:::

::: {.pf-step #s1-2}

For every $a,b\in R$,
$$
ab+ba=0.
$$


::: pf-proof

The element $a+b$ is idempotent. Thus
$$
(a+b)^2=a+b.
$$
Expanding the left-hand side and using $a^2=a$ and $b^2=b$ gives
$$
a+ab+ba+b=a+b.
$$
Cancelling $a+b$ in the additive group yields $ab+ba=0$.

:::

:::

::: {.pf-step #s1-3}

The ring $R$ is commutative.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
ab=-ba.
$$
By step [](#s1-1){.pf-ref} applied to $ba$,
$$
ba+ba=0,
$$
so $-ba=ba$. Therefore $ab=ba$ for all $a,b\in R$.

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{2a=0\ \text{and}\ ab=ba\quad\text{for all }a,b\in R}.
$$


::: pf-proof

This combines steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives both required conclusions.

:::

:::

:::
