---
schema: qual/card@1
id: P-PRACT20-W5-15
kind: problem
title: Group and ring endomorphisms of $\ZZ$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 15).
---

::: {.problem}
Find all group and ring homomorphisms from $\ZZ \to \ZZ$.
:::

::: {.solution}

Regard $\ZZ$ as an additive group when discussing group homomorphisms.

::: pf

::: {.pf-step #s1-1}

If $\phi:(\ZZ,+)\to(\ZZ,+)$ is a group homomorphism and
$$
k=\phi(1),
$$
then
$$
\phi(n)=kn
\qquad(n\in\ZZ).
$$


::: pf-proof

For $n>0$,
$$
\phi(n)
=\phi(\underbrace{1+\cdots+1}_{n\text{ terms}})
=n\phi(1)
=kn.
$$
Also $\phi(0)=0$. For $n<0$,
$$
0=\phi(n+(-n))=\phi(n)+\phi(-n),
$$
so
$$
\phi(n)=-\phi(-n)=kn.
$$

:::

:::

::: {.pf-step #s1-2}

Conversely, for every $k\in\ZZ$, the map
$$
\phi_k(n)=kn
$$
is a group homomorphism.


::: pf-proof

For $m,n\in\ZZ$,
$$
\phi_k(m+n)
=k(m+n)
=km+kn
=\phi_k(m)+\phi_k(n).
$$

:::

:::

::: {.pf-step #s1-3}

Hence the group homomorphisms $\ZZ\to\ZZ$ are exactly
$$
\boxed{\phi_k(n)=kn,\qquad k\in\ZZ}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} prove both directions.

:::

:::

::: {.pf-step #s1-4}

If $\phi:\ZZ\to\ZZ$ is a ring homomorphism, then
$$
\phi(1)\in\{0,1\}.
$$


::: pf-proof

Every ring homomorphism is additive, so by step [](#s1-1){.pf-ref},
$$
\phi(n)=n\phi(1).
$$
Multiplicativity gives
$$
\phi(1)
=\phi(1\cdot1)
=\phi(1)^2.
$$
Writing $k=\phi(1)\in\ZZ$, this says
$$
k^2=k,
$$
or
$$
k(k-1)=0.
$$
Since $\ZZ$ is an integral domain, $k=0$ or $k=1$.

:::

:::

::: {.pf-step #s1-5}

The ring homomorphisms are exactly
$$
\boxed{\phi(n)=0\quad\text{for all }n}
$$
and
$$
\boxed{\phi(n)=n\quad\text{for all }n}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} leaves only $\phi(1)=0$ or $\phi(1)=1$, and step [](#s1-1){.pf-ref} then gives
the two displayed maps. Both preserve addition and multiplication.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} classifies the group homomorphisms and step [](#s1-5){.pf-ref} classifies the ring
homomorphisms.

:::

:::

:::
