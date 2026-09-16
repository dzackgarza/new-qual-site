---
schema: qual/card@1
id: P-ALGF07A
kind: problem
title: "Sylow subgroups of a group of order 240 and elements of order 15"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $G$ be a group of order $240 = 2^4 \cdot 3 \cdot 5$.

(a) How many $p$-Sylow subgroups might $G$ have, for $p = 2, 3, 5$?

(b) If $G$ has a subgroup of order 15, show that it has an element of order 15.

(c) Say $G$ doesn't have a subgroup of order 15. Show that the number of $3$-Sylows is 10 or 40.
:::

::: {.solution}
**Part (a).**

<1>1. $n_2 \equiv 1 \pmod 2$ and $n_2 \mid 15$, so $n_2 \in \{1, 3, 5, 15\}$.
::: {.proof}
Sylow's third theorem; the odd divisors of $15$ are $1, 3, 5, 15$.
:::

<1>2. $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 80$, so $n_3 \in \{1, 4, 10, 16, 40\}$.
::: {.proof}
the divisors of $80 = 2^4 \cdot 5$ that are $\equiv 1 \pmod 3$ are $1, 4, 10, 16, 40$.
:::

<1>3. $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 48$, so $n_5 \in \{1, 6, 16\}$.
::: {.proof}
the divisors of $48 = 2^4 \cdot 3$ that are $\equiv 1 \pmod 5$ are $1, 6, 16$.
:::

**Part (b).**

<1>1. Let $H \le G$ be a subgroup of order $15 = 3 \cdot 5$.
::: {.proof}
hypothesis.
:::

<1>2. $H$ has a normal Sylow $5$-subgroup.
::: {.proof}
$n_5(H) \equiv 1 \pmod 5$ and $n_5(H) \mid 3$, so $n_5(H) = 1$.
:::

<1>3. $H$ has a normal Sylow $3$-subgroup.
::: {.proof}
$n_3(H) \equiv 1 \pmod 3$ and $n_3(H) \mid 5$, so $n_3(H) = 1$.
:::

<1>4. Hence $H \cong \ZZ/3 \times \ZZ/5 \cong \ZZ/15$.
::: {.proof}
both Sylow subgroups are normal and intersect trivially, so $H$ is their direct product, which is cyclic of order $15$.
:::

<1>5. Therefore $H$ (and hence $G$) has an element of order $15$.
::: {.proof}
a cyclic group of order $15$ has a generator of order $15$.
:::

<1>6. Q.E.D. for parts (a) and (b).
::: {.proof}
<1>3 (a) and <1>5 (b).
:::

**Part (c).**

<1>1. Let $P$ be a Sylow $3$-subgroup of $G$.
Then
\[
|N_G(P)|=\frac{|G|}{n_3}=\frac{240}{n_3}.
\]
::: {.proof}
The conjugation action of $G$ on its Sylow $3$-subgroups is transitive, and the stabilizer of $P$ is $N_G(P)$.
Orbit--stabilizer therefore gives $n_3=[G:N_G(P)]$.
:::

<1>2. Under the hypothesis that $G$ has no subgroup of order $15$, one has $5\nmid |N_G(P)|$.
::: {.proof}
The subgroup $P$ is normal in $N_G(P)$ by definition of the normalizer.
If $5\mid |N_G(P)|$, Cauchy's theorem gives a subgroup $Q\le N_G(P)$ of order $5$.
Since $P\trianglelefteq N_G(P)$, the product $PQ$ is a subgroup of $N_G(P)$, and
\[
|PQ|=\frac{|P||Q|}{|P\cap Q|}=3\cdot5=15,
\]
because $P\cap Q=1$.
This contradicts the hypothesis.
:::

<1>3. Therefore $n_3$ is either $10$ or $40$.
::: {.proof}
Part (a) gives $n_3\in\{1,4,10,16,40\}$.
By <1>1, the corresponding normalizer orders are respectively $240,60,24,15,6$.
The first, second, and fourth are divisible by $5$, contradicting <1>2. Thus only $n_3=10$ or $40$ remain.
:::

<1>4. Q.E.D.
::: {.proof}
Combine <1>1--<1>3.
:::
:::
