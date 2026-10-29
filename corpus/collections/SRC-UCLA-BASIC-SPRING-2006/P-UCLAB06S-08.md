---
schema: qual/card@1
id: P-UCLAB06S-08
kind: problem
title: Orthogonal maps of $\RR^{2n+1}$ have an eigenvalue $\pm1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 8 of the retained UCLA Basic Examination Spring 2006 PDF.
---

::: {.problem}
A linear transformation $T$ is called orthogonal if it is nonsingular and ${}^tT = T^{-1}$. Prove that if $T : \RR^{2n+1} \to \RR^{2n+1}$ is orthogonal, then there exists a vector $v \in \RR^{2n+1}$ such that $Tv = \pm v$.
:::

::: {.solution}

::: pf

::: pf-step

The characteristic polynomial
$$
\chi_T(\lambda)=\det(\lambda I-T)
$$
has a real root.


::: pf-proof

The matrix $T$ has size $(2n+1)\times(2n+1)$, so $\chi_T$ is a real polynomial of odd degree $2n+1$ with leading coefficient $1$.
Hence $\chi_T(\lambda)\to+\infty$ as $\lambda\to+\infty$ and $\chi_T(\lambda)\to-\infty$ as $\lambda\to-\infty$.
By the intermediate value theorem, there exists $\lambda_0\in\RR$ such that
$$
\chi_T(\lambda_0)=0.
$$

:::

:::

::: {.pf-step #s1-2}

There exists a nonzero real vector $v$ such that
$$
Tv=\lambda_0v.
$$


::: pf-proof

Since
$$
\det(\lambda_0I-T)=0,
$$
the real matrix $\lambda_0I-T$ is singular.
Therefore its kernel contains a nonzero real vector $v$.
For such a vector,
$$
(\lambda_0I-T)v=0,
$$
so
$$
Tv=\lambda_0v.
$$

:::

:::

::: {.pf-step #s1-3}

The orthogonality relation implies
$$
\|Tx\|_2=\|x\|_2
$$
for every $x\in\RR^{2n+1}$.


::: pf-proof

From
$$
T^t=T^{-1},
$$
one gets
$$
T^tT=I.
$$
Hence
$$
\|Tx\|_2^2
=(Tx)^t(Tx)
=
x^tT^tTx
=
x^tx
=
\|x\|_2^2.
$$
Taking square roots gives the claim.

:::

:::

::: pf-step

The real eigenvalue $\lambda_0$ satisfies
$$
|\lambda_0|=1.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
Tv=\lambda_0v
$$
for some nonzero $v$.
Using step [](#s1-3){.pf-ref},
$$
\|v\|_2
=
\|Tv\|_2
=
\|\lambda_0v\|_2
=
|\lambda_0|\|v\|_2.
$$
Since $\|v\|_2>0$, division gives $|\lambda_0|=1$.

:::

:::

::: {.pf-step #s1-5}

Since $\lambda_0$ is real,
$$
\lambda_0=\pm1.
$$


::: pf-proof

The only real numbers with absolute value $1$ are $1$ and $-1$.

:::

:::

::: {.pf-step #s1-6}

Therefore there exists a nonzero vector
$$
v\in\RR^{2n+1}
$$
such that
$$
\boxed{Tv=\pm v}.
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
