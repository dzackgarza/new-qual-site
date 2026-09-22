---
schema: qual/card@1
id: P-BERK85S-02
kind: problem
title: Product of commuting elements of coprime finite orders has product order
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used commutativity to show (ab)^{rs}=e, then showed any exponent killing
    ab is divisible by both r and s; coprimality forces divisibility by rs.
---

::: {.problem}
Let $G$ be an abelian group. Suppose $a,b\in G$ have finite orders $r,s$ with
\[
\gcd(r,s)=1.
\]
Show that $ab$ has order $rs$.
:::

::: {.solution}
<1>1. The element $ab$ satisfies
$$
(ab)^{rs}=e.
$$

::: {.proof}
Since $G$ is abelian,
$$
(ab)^{rs}
=
a^{rs}b^{rs}
=
(a^r)^s(b^s)^r
=e.
$$
Thus $ab$ has finite order dividing $rs$.
:::

<1>2. If
$$
(ab)^m=e
$$
for some positive integer $m$, then
$$
r\mid m.
$$

::: {.proof}
Commutativity gives
$$
a^mb^m=e,
$$
so
$$
a^m=b^{-m}.
$$
Raise both sides to the $s$th power:
$$
a^{ms}
=
b^{-ms}
=
(b^s)^{-m}
=e.
$$
Since $a$ has order $r$, this implies $r\mid ms$. Because
$\gcd(r,s)=1$, Euclid's lemma gives $r\mid m$.
:::

<1>3. Under the same hypothesis,
$$
s\mid m.
$$

::: {.proof}
From $a^m=b^{-m}$, raise both sides to the $r$th power:
$$
(a^r)^m=b^{-mr}.
$$
Hence $b^{mr}=e$. Since $b$ has order $s$, one has $s\mid mr$.
The coprimality $\gcd(r,s)=1$ therefore gives $s\mid m$.
:::

<1>4. Every positive exponent $m$ satisfying $(ab)^m=e$ is divisible by
$rs$.

::: {.proof}
Steps <1>2 and <1>3 give
$$
r\mid m
\qquad\text{and}\qquad
s\mid m.
$$
Since $\gcd(r,s)=1$, their product divides $m$:
$$
rs\mid m.
$$
:::

<1>5. Therefore
$$
\boxed{\operatorname{ord}(ab)=rs}.
$$

::: {.proof}
Step <1>1 shows that the order of $ab$ divides $rs$. Step <1>4 shows
that every positive exponent annihilating $ab$, in particular its order,
is divisible by $rs$. The two divisibilities force equality.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
