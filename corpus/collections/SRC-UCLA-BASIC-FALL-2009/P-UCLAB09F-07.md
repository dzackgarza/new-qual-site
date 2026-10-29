---
schema: qual/card@1
id: P-UCLAB09F-07
kind: problem
title: Dimension of the span of powers of an endomorphism
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
Let $V$ be an $n$-dimensional real vector space and let $T\in\operatorname{End}(V)$.
Let $W\subseteq\operatorname{End}(V)$ be the vector subspace spanned by the nonnegative powers $T^k$, $k\ge0$.
Prove that
$$
\dim W\le \dim V=n.
$$
:::

::: {.solution}

Let
$$
\chi_T(X)
=
X^n+c_{n-1}X^{n-1}+\cdots+c_1X+c_0
$$
be the characteristic polynomial of $T$.

::: pf

::: {.pf-step #s1-1}

The Cayley--Hamilton theorem gives
$$
T^n
=
-c_{n-1}T^{n-1}
-\cdots
-c_1T
-c_0I.
$$


::: pf-proof

The Cayley--Hamilton theorem states that every endomorphism satisfies its characteristic polynomial:
$$
\chi_T(T)=0.
$$
Expanding this identity and solving for $T^n$ gives the displayed formula.

:::

:::

::: {.pf-step #s1-2}

For every integer $m\ge n$,
$$
T^m
\in
\operatorname{span}\{I,T,\ldots,T^{n-1}\}.
$$


::: pf-proof

Proceed by induction on $m$.
The case $m=n$ is step [](#s1-1){.pf-ref}.

Assume the claim holds for all powers from $n$ through $m$. Multiply the identity in step [](#s1-1){.pf-ref} by $T^{m+1-n}$ to obtain
$$
T^{m+1}
=
-c_{n-1}T^m
-c_{n-2}T^{m-1}
-\cdots
-c_0T^{m+1-n}.
$$
Every power on the right has exponent at most $m$. By the induction hypothesis, all powers with exponent at least $n$ lie in the span of
$$
I,T,\ldots,T^{n-1},
$$
and the lower powers already lie there. Hence $T^{m+1}$ lies in the same span.

:::

:::

::: {.pf-step #s1-3}

The space $W$ satisfies
$$
W
=
\operatorname{span}\{I,T,\ldots,T^{n-1}\}.
$$


::: pf-proof

By definition, $W$ is spanned by all nonnegative powers of $T$. The right-hand side is contained in $W$. Conversely, step [](#s1-2){.pf-ref} shows that every power $T^m$ with $m\ge n$ lies in the span of the first $n$ powers. Thus every generator of $W$ lies in the displayed finite span.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\dim W\le n=\dim V}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, $W$ is spanned by the $n$ vectors
$$
I,T,\ldots,T^{n-1}
$$
in $\operatorname{End}(V)$. A vector space spanned by $n$ vectors has dimension at most $n$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required inequality.

:::

:::

:::
