---
schema: qual/card@1
id: P-WESTOP14-5
kind: problem
title: Compare the $L^1$ and uniform metric topologies on $C[0,1]$
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $C[0,1]$ be the set of continuous functions $f:[0,1]\to\RR$. Define
$$
\rho(f,g)=\int_0^1|f(x)-g(x)|\,dx
$$
and
$$
\mu(f,g)=\max_{x\in[0,1]}|f(x)-g(x)|.
$$
Both define metrics on $C[0,1]$. Which metric induces the finer topology?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $f,g\in C[0,1]$,
$$
\rho(f,g)\le \mu(f,g).
$$


::: pf-proof

For every $x\in[0,1]$,
$$
|f(x)-g(x)|\le\mu(f,g).
$$
Integrating over an interval of length $1$ gives
$$
\rho(f,g)
=\int_0^1|f(x)-g(x)|\,dx
\le\int_0^1\mu(f,g)\,dx
=\mu(f,g).
$$

:::

:::

::: {.pf-step #s1-2}

The topology induced by $\mu$ is finer than the topology induced by $\rho$.


::: pf-proof

Fix $f\in C[0,1]$ and $\varepsilon>0$. By step [](#s1-1){.pf-ref},
$$
B_\mu(f,\varepsilon)
\subseteq
B_\rho(f,\varepsilon).
$$
Hence every $\rho$-open neighborhood of $f$ contains a $\mu$-open neighborhood of $f$. Equivalently, every $\rho$-open set is $\mu$-open, so the $\mu$-topology is finer.

:::

:::

::: {.pf-step #s1-3}

The inclusion of topologies is strict.


::: pf-proof

For $n\ge1$, define
$$
f_n(x)=\max(1-nx,0).
$$
Then $f_n\in C[0,1]$ and
$$
\mu(f_n,0)=1
$$
for every $n$, because $f_n(0)=1$. On the other hand,
$$
\rho(f_n,0)
=\int_0^{1/n}(1-nx)\,dx
=\frac1{2n}
\longrightarrow0.
$$
Thus $f_n\to0$ in the metric $\rho$ but not in the metric $\mu$. Therefore the two topologies are not equal.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\text{the uniform metric }\mu\text{ induces the strictly finer topology}.}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} proves fineness, and step [](#s1-3){.pf-ref} proves strictness.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} answers the comparison question.

:::

:::

:::
