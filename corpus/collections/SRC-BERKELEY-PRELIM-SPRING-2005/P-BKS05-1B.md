---
schema: qual/card@1
id: P-BKS05-1B
kind: problem
title: Finite groups whose prime-power-order elements commute are abelian
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained argument and made the cyclic
    prime-power decomposition explicit using CRT idempotents.
---

::: {.problem}
Let G be a finite group.
Suppose ab = ba holds whenever $a , b \in G$ have prime power order.
Prove that G is abelian.
:::

::: {.solution}
<1>1. Every element $x\in G$ can be written as a product
$$
x=x_1\cdots x_s
$$
in which each nonidentity factor $x_i$ has prime-power order.

::: {.proof}
If $x=1$, there is nothing to prove. Suppose $x$ has order
$$
n=\prod_{i=1}^s p_i^{e_i},
$$
where the $p_i$ are distinct primes. Put
$$
n_i=p_i^{e_i}.
$$
By the Chinese remainder theorem, for each $i$ there is an integer
$a_i$ satisfying
$$
a_i\equiv1\pmod{n_i},
\qquad
a_i\equiv0\pmod{n_j}
\quad(j\neq i).
$$
The same theorem gives
$$
a_1+\cdots+a_s\equiv1\pmod n.
$$
Set
$$
x_i\coloneqq x^{a_i}.
$$
Then
$$
x_1\cdots x_s
=
x^{a_1+\cdots+a_s}
=x.
$$
Moreover, for $j\neq i$ the integer $a_i$ is divisible by $n_j$, so
the order of $x_i$ divides $n_i=p_i^{e_i}$. Since
$a_i\equiv1\pmod{n_i}$, its order is in fact $n_i$, hence a prime
power.
:::

<1>2. Any two elements $x,y\in G$ commute.

::: {.proof}
Apply step <1>1 to write
$$
x=x_1\cdots x_s,
\qquad
y=y_1\cdots y_t,
$$
where every displayed factor has prime-power order. By hypothesis,
$$
x_i y_j=y_jx_i
$$
for every pair $i,j$. Therefore all $x_i$ factors may be moved past all
$y_j$ factors:
$$
xy
=(x_1\cdots x_s)(y_1\cdots y_t)
=(y_1\cdots y_t)(x_1\cdots x_s)
=yx.
$$
:::

<1>3. The group $G$ is abelian.

::: {.proof}
The elements $x,y$ in step <1>2 were arbitrary, so every pair of
elements of $G$ commutes.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
