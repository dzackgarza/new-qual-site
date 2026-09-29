---
schema: qual/card@1
id: P-BERK79S-14
kind: problem
title: Cancellation for direct products of finite abelian groups
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
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the elementary-divisor form of the fundamental theorem of finite
    abelian groups. For each prime p and exponent k, let a_{p,k},
    b_{p,k}, c_{p,k} be the multiplicities of C_{p^k}. Direct products add
    these multiplicities. Uniqueness of elementary divisors applied to
    A×B≅A×C gives a_{p,k}+b_{p,k}=a_{p,k}+c_{p,k}, hence
    b_{p,k}=c_{p,k} for every p,k and therefore B≅C.
---

::: {.problem}
Let $A,B,C$ be finite abelian groups.
Suppose
\[
A\times B\cong A\times C.
\]
Prove that
\[
B\cong C.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

By the fundamental theorem of finite abelian groups, there are
uniquely determined nonnegative integers
$$
a_{p,k},
\qquad
b_{p,k},
\qquad
c_{p,k},
$$
all but finitely many zero, such that
$$
\begin{aligned}
A
&\cong
\prod_{p}
\prod_{k\geq1}
\left(\ZZ/p^k\ZZ\right)^{a_{p,k}},\\
B
&\cong
\prod_{p}
\prod_{k\geq1}
\left(\ZZ/p^k\ZZ\right)^{b_{p,k}},\\
C
&\cong
\prod_{p}
\prod_{k\geq1}
\left(\ZZ/p^k\ZZ\right)^{c_{p,k}}.
\end{aligned}
$$

::: pf-proof

The elementary-divisor form of the fundamental theorem states that every
finite abelian group is a finite direct product of cyclic groups of
prime-power order, and that the multiplicity of each cyclic factor
$\ZZ/p^k\ZZ$ is uniquely determined by the isomorphism type of the group.
Apply this theorem separately to $A$, $B$, and $C$.

:::

:::

::: {.pf-step #s2}

The elementary-divisor decomposition of $A\times B$ contains
$$
a_{p,k}+b_{p,k}
$$
copies of $\ZZ/p^k\ZZ$ for every prime $p$ and every $k\geq1$.

::: pf-proof

Using the decompositions from step [](#s1){.pf-ref},
$$
\begin{aligned}
A\times B
&\cong
\left(
\prod_p\prod_{k\geq1}
(\ZZ/p^k\ZZ)^{a_{p,k}}
\right)
\times
\left(
\prod_p\prod_{k\geq1}
(\ZZ/p^k\ZZ)^{b_{p,k}}
\right)\\
&\cong
\prod_p\prod_{k\geq1}
(\ZZ/p^k\ZZ)^{a_{p,k}+b_{p,k}}.
\end{aligned}
$$
Thus direct product adds the multiplicities of identical elementary
divisors.

:::

:::

::: {.pf-step #s3}

The elementary-divisor decomposition of $A\times C$ contains
$$
a_{p,k}+c_{p,k}
$$
copies of $\ZZ/p^k\ZZ$ for every prime $p$ and every $k\geq1$.

::: pf-proof

The same calculation as in step [](#s2){.pf-ref}, with $C$ in place of $B$, gives
$$
A\times C
\cong
\prod_p\prod_{k\geq1}
(\ZZ/p^k\ZZ)^{a_{p,k}+c_{p,k}}.
$$

:::

:::

::: {.pf-step #s4}

For every prime $p$ and every $k\geq1$,
$$
b_{p,k}=c_{p,k}.
$$

::: pf-proof

The hypothesis gives
$$
A\times B\cong A\times C.
$$
By uniqueness of the elementary-divisor multiplicities in the fundamental
theorem, steps [](#s2){.pf-ref} and [](#s3){.pf-ref} imply
$$
a_{p,k}+b_{p,k}
=
a_{p,k}+c_{p,k}
$$
for every $p,k$. Cancelling the integer $a_{p,k}$ gives
$$
b_{p,k}=c_{p,k}.
$$

:::

:::

::: {.pf-step #s5}

The groups $B$ and $C$ are isomorphic:
$$
\boxed{
B\cong C.
}
$$

::: pf-proof

Step [](#s4){.pf-ref} says that $B$ and $C$ have exactly the same elementary-divisor
multiplicities. Their decompositions in step [](#s1){.pf-ref} are therefore
isomorphic term by term.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required cancellation conclusion.

:::

:::

:::
