---
schema: qual/card@1
id: P-NORI-GT-6-04
kind: problem
title: Additive polynomials in characteristic $p$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 6.4 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $f \in F[X]$. Prove that $f(X + Y) = f(X) + f(Y)$ if and only if $f = a_{0}X + a_{1}X^{p} + \cdots + a_{n}X^{p^{n}}$ for some $n \geq 0$ and $a_{0}, \ldots, a_{n} \in F$.
:::

::: {.solution}

Write
$$
f(X)=\sum_{m=0}^d c_mX^m.
$$

::: pf

::: {.pf-step #s1-1}

If
$$
f(X)=a_0X+a_1X^p+\cdots+a_nX^{p^n},
$$
then
$$
f(X+Y)=f(X)+f(Y).
$$


::: pf-proof

In characteristic $p$, the Frobenius identity gives
$$
(X+Y)^p=X^p+Y^p.
$$
Iterating it yields
$$
(X+Y)^{p^i}=X^{p^i}+Y^{p^i}
$$
for every $i\geq0$. Therefore
$$
\begin{aligned}
f(X+Y)
&=\sum_{i=0}^n a_i(X+Y)^{p^i}\\
&=\sum_{i=0}^n a_iX^{p^i}
+\sum_{i=0}^n a_iY^{p^i}\\
&=f(X)+f(Y).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

Conversely, assume
$$
f(X+Y)=f(X)+f(Y).
$$
Then $c_0=0$.


::: pf-proof

Set $X=Y=0$. Then
$$
f(0)=f(0)+f(0),
$$
so $f(0)=0$. Hence the constant coefficient $c_0$ is zero.

:::

:::

::: {.pf-step #s1-3}

If $m\geq1$ and $c_m\neq0$, then
$$
\binom{m}{k}=0
$$
in $F$ for every $1\leq k\leq m-1$.


::: pf-proof

Expanding the assumed identity gives
$$
0=f(X+Y)-f(X)-f(Y)
=\sum_{m=1}^d c_m
\sum_{k=1}^{m-1}\binom{m}{k}X^kY^{m-k}.
$$
Terms coming from different values of $m$ have different total degree. Hence for fixed $m$ and $1\leq k\leq m-1$, the coefficient of $X^kY^{m-k}$ is
$$
c_m\binom{m}{k},
$$
which must vanish. If $c_m\neq0$, then $\binom{m}{k}=0$ in $F$.

:::

:::

::: {.pf-step #s1-4}

If every intermediate binomial coefficient
$$
\binom{m}{k},
\qquad 1\leq k\leq m-1,
$$
vanishes in characteristic $p$, then $m$ is a power of $p$.


::: pf-proof

Write
$$
m=p^rq,
$$
where $r\geq0$ and $p\nmid q$. Suppose $q>1$. Then
$$
1\leq p^r<m.
$$
In the polynomial ring $\FF_p[T]$,
$$
(1+T)^m
=\left((1+T)^{p^r}\right)^q
=\left(1+T^{p^r}\right)^q,
$$
because repeated Frobenius gives $(1+T)^{p^r}=1+T^{p^r}$. The coefficient of $T^{p^r}$ on the left is
$$
\binom{m}{p^r},
$$
whereas on the right it is $q$. Thus
$$
\binom{m}{p^r}\equiv q\not\equiv0\pmod p,
$$
contradicting the hypothesis. Therefore $q=1$, so $m=p^r$.

:::

:::

::: {.pf-step #s1-5}

Every exponent occurring in $f$ with nonzero coefficient is a power of $p$.


::: pf-proof

Let $m\geq1$ with $c_m\neq0$. By step [](#s1-3){.pf-ref}, all intermediate binomial coefficients of $m$ vanish in $F$, hence modulo $p$. Step [](#s1-4){.pf-ref} therefore gives
$$
m=p^r
$$
for some $r\geq0$.

:::

:::

::: {.pf-step #s1-6}

There exist $n\geq0$ and $a_0,\ldots,a_n\in F$ such that
$$
\boxed{f(X)=a_0X+a_1X^p+\cdots+a_nX^{p^n}}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, no constant term occurs. By step [](#s1-5){.pf-ref}, every nonzero remaining term has exponent $p^i$ for some $i\geq0$. Let $n$ be at least the largest such $i$ and let $a_i$ be the coefficient of $X^{p^i}$, allowing $a_i=0$ when that power is absent. This gives the displayed form. The zero polynomial is included by taking $n=0$ and $a_0=0$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves the forward implication from the displayed form to additivity, and steps [](#s1-2){.pf-ref} through [](#s1-6){.pf-ref} prove the converse.

:::

:::

:::
