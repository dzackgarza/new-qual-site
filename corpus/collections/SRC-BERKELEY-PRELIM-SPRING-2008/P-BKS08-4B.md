---
schema: qual/card@1
id: P-BKS08-4B
kind: problem
title: Groups of order $p^2q^2$ are not simple
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
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the Sylow-number reduction to order 36 and the
    conjugation action on the four Sylow 3-subgroups against the vendored
    solution.
---

::: {.problem}
Let $p$ and $q$ be distinct primes.
Show that every group of order
$$
p^2q^2
$$
is not simple.
:::

::: {.solution}
Suppose, for contradiction, that a group $G$ of order $p^2q^2$ is
simple. Interchange $p$ and $q$ if necessary so that $p<q$.

::: pf

::: pf-step
The number $n_q$ of Sylow $q$-subgroups is either $p$ or
$p^2$.

::: pf-proof
Sylow's theorem gives
$$
n_q\mid p^2
\qquad\text{and}\qquad
n_q\equiv1\pmod q.
$$
Because $G$ is simple, a Sylow $q$-subgroup cannot be unique and
normal, so $n_q\ne1$. The only remaining divisors of $p^2$ are
$p$ and $p^2$.
:::

:::

::: {.pf-step #q-equals-p-plus-one}
One must have
$$
q=p+1.
$$

::: pf-proof
If $n_q=p$, then $n_q\equiv1\pmod q$ gives
$q\mid p-1$, impossible because $0<p-1<q$. Therefore
$n_q=p^2$, so
$$
q\mid p^2-1=(p-1)(p+1).
$$
Since $q$ is prime, it divides $p-1$ or $p+1$. The first is again
impossible because $p<q$. Hence $q\mid p+1$. Since
$p<q$ also gives $p+1\le q$, it follows that $q=p+1$.
:::

:::

::: pf-step
The only possible pair of distinct primes is
$$
(p,q)=(2,3),
$$
so $\abs{G}=36$.

::: pf-proof
By step [](#q-equals-p-plus-one){.pf-ref}, the primes are consecutive integers. If $p$ were odd,
then $q=p+1>2$ would be even and hence not prime. Thus $p=2$ and
$q=3$.
:::

:::

::: pf-step
A hypothetical simple group $G$ of order $36$ has exactly four
Sylow $3$-subgroups.

::: pf-proof
If $n_3$ denotes the number of Sylow $3$-subgroups, then
$$
n_3\mid4
\qquad\text{and}\qquad
n_3\equiv1\pmod3.
$$
Thus $n_3$ is $1$ or $4$. Simplicity excludes $n_3=1$, so $n_3=4$.
:::

:::

::: {.pf-step #nontrivial-hom}
Conjugation on the four Sylow $3$-subgroups gives a nontrivial
homomorphism
$$
\rho:G\longrightarrow S_4.
$$

::: pf-proof
Conjugation permutes the Sylow $3$-subgroups, giving the displayed
homomorphism. If the action were trivial, every Sylow $3$-subgroup
would be fixed under conjugation by every element of $G$, hence would
be normal in $G$. This contradicts simplicity. Therefore $\rho$ is
nontrivial.
:::

:::

::: {.pf-step #contradiction}
The homomorphism $\rho$ contradicts simplicity.

::: pf-proof
The kernel of $\rho$ is normal in $G$. Since $G$ is simple and
$\rho$ is nontrivial by step [](#nontrivial-hom){.pf-ref}, the kernel must be trivial.
Hence $\rho$ would embed $G$ into $S_4$. But
$$
\abs{G}=36>24=\abs{S_4},
$$
which is impossible.
:::

:::

::: {.pf-step #not-simple-conclusion}
Therefore every group of order $p^2q^2$ is not simple.

::: pf-proof
The assumption of simplicity led to the contradiction in step [](#contradiction){.pf-ref}.
:::

:::

::: pf-qed
Step [](#not-simple-conclusion){.pf-ref} is the required conclusion.
:::

:::

:::
