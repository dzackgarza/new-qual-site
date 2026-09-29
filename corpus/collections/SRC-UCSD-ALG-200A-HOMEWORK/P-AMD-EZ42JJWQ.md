---
schema: qual/card@1
id: P-AMD-EZ42JJWQ
kind: problem
title: $D_{2n}$ is nilpotent iff $n$ is a power of $2$
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - p-Groups
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 6, Exercise 2(b). Restored
    the source's iff statement and used the suggested criterion from part (a).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    If n is a power of 2, D_{2n} is a finite 2-group and hence nilpotent. If n
    has an odd prime divisor p, a rotation of order p and a reflection of order
    2 fail to commute, contradicting the coprime-order characterization of
    finite nilpotent groups.
---

::: {.problem}
Let
\[
D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle
\]
be the dihedral group of order $2n$.
Prove that $D_{2n}$ is nilpotent if and only if $n$ is a power of $2$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every finite $p$-group is nilpotent.

::: pf-proof

We induct on the order of a finite $p$-group $P$.
The trivial group is nilpotent.
If $P\ne1$, the class equation gives
\[
Z(P)\ne1.
\]
Thus $P/Z(P)$ is a smaller $p$-group and is nilpotent by induction.

Let
\[
\gamma_1(P)=P,
\qquad
\gamma_{i+1}(P)=[P,\gamma_i(P)]
\]
be the lower central series.
If
\[
\gamma_{c+1}(P/Z(P))=1,
\]
then the quotient map sends $\gamma_{c+1}(P)$ to $1$, so
\[
\gamma_{c+1}(P)\le Z(P).
\]
Consequently
\[
\gamma_{c+2}(P)
  =[P,\gamma_{c+1}(P)]
  \le[P,Z(P)]
  =1.
\]
Hence $P$ is nilpotent.

:::

:::

::: {.pf-step #s2}

If $n$ is a power of $2$, then $D_{2n}$ is nilpotent.

::: pf-proof

Write
\[
n=2^i.
\]
Then
\[
|D_{2n}|=2n=2^{i+1},
\]
so $D_{2n}$ is a finite $2$-group.
By step [](#s1){.pf-ref} it is nilpotent.

:::

:::

::: {.pf-step #s3}

Suppose that $n$ is not a power of $2$.
Then $D_{2n}$ contains elements of relatively prime orders that do not commute.

::: pf-proof

Since $n$ is not a power of $2$, some odd prime $p$ divides $n$.
Set
\[
x=r^{n/p}.
\]
Because $r$ has order $n$, the element $x$ has order $p$.
The reflection $s$ has order $2$, so
\[
\gcd(|x|,|s|)=1.
\]

The dihedral relation gives
\[
sxs^{-1}
  =sr^{n/p}s^{-1}
  =r^{-n/p}
  =x^{-1}.
\]
Since $p$ is odd and $x$ has order $p>2$,
\[
x^{-1}\ne x.
\]
Thus $sx\ne xs$.

:::

:::

::: {.pf-step #s4}

If $n$ is not a power of $2$, then $D_{2n}$ is not nilpotent.

::: pf-proof

For a finite nilpotent group, any two elements of relatively prime orders commute.
By step [](#s3){.pf-ref}, $D_{2n}$ has an element $x$ of odd prime order and a reflection $s$ of order $2$ that do not commute.
Therefore $D_{2n}$ cannot be nilpotent.

:::

:::

::: pf-qed

The forward and reverse directions are steps [](#s4){.pf-ref} and [](#s2){.pf-ref}, respectively.

:::

:::

:::
