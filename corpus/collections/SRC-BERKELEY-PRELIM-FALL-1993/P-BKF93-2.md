---
schema: qual/card@1
id: P-BKF93-2
kind: problem
title: Homomorphisms from $(\mathbb Q,+)$ to the positive rationals under multiplication
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $A=(\mathbb Q,+)$ and let $M=(\mathbb Q_{>0},\cdot)$. Determine all group homomorphisms
\[
A\to M.
\]
:::

::: {.solution}
Let
$$
\varphi:(\QQ,+)\longrightarrow(\QQ_{>0},\cdot)
$$
be a group homomorphism.

<1>1. For every positive integer $n$,
$$
\varphi(1)
=
\varphi(1/n)^n.
$$

::: {.proof}
Since
$$
1=
\underbrace{\frac1n+\cdots+\frac1n}_{n\text{ terms}},
$$
the homomorphism property gives
$$
\varphi(1)
=
\underbrace{\varphi(1/n)\cdots\varphi(1/n)}_{n\text{ factors}}
=
\varphi(1/n)^n.
$$
:::

<1>2. One has
$$
\varphi(1)=1.
$$

::: {.proof}
Write the positive rational number $\varphi(1)$ in its unique prime factorization
$$
\varphi(1)
=
\prod_p p^{e_p},
$$
where each $e_p\in\ZZ$ and all but finitely many $e_p$ are zero.

By step <1>1, $\varphi(1)$ is an $n$th power in $\QQ_{>0}$ for every positive integer $n$. Therefore every exponent $e_p$ is divisible by every positive integer $n$. The only integer with this property is $0$. Hence every $e_p=0$, so
$$
\varphi(1)=1.
$$
:::

<1>3. For every positive integer $n$,
$$
\varphi(1/n)=1.
$$

::: {.proof}
Steps <1>1 and <1>2 give
$$
\varphi(1/n)^n=1.
$$
The only positive rational number whose $n$th power is $1$ is $1$. Hence
$$
\varphi(1/n)=1.
$$
:::

<1>4. For every rational number $q$,
$$
\varphi(q)=1.
$$

::: {.proof}
Write
$$
q=\frac mn
$$
with $m\in\ZZ$ and $n>0$. By step <1>3,
$$
\varphi(1/n)=1.
$$
If $m\geq0$, then
$$
\varphi(m/n)
=
\varphi(1/n)^m
=
1.
$$
If $m<0$, then
$$
\varphi(m/n)
=
\varphi((-m)/n)^{-1}
=
1^{-1}
=
1.
$$
:::

<1>5. The only group homomorphism
$$
(\QQ,+)\longrightarrow(\QQ_{>0},\cdot)
$$
is
$$
\boxed{\varphi(q)=1\text{ for every }q\in\QQ}.
$$

::: {.proof}
Step <1>4 shows that every homomorphism is trivial. Conversely, the constant map
$$
q\longmapsto1
$$
is plainly a group homomorphism.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the complete classification.
:::
:::
