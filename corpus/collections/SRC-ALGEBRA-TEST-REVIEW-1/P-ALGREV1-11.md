---
schema: qual/card@1
id: P-ALGREV1-11
kind: problem
title: Equal coprime powers in an integral domain
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Review1.md, true/sometimes/false question 4."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Classified the assertion as sometimes true: coprime exponents force equality, while m=2,n=4 with a=-1,b=1 in Z is a counterexample."
---

::: {.problem}
Classify the following assertion as true, sometimes true, or false: in an integral domain, for distinct positive integers $m$ and $n$, if $a^m=b^m$ and $a^n=b^n$, then $a=b$.
:::

::: {.solution}
The assertion is **sometimes true**.

<1>1. If $\gcd(m,n)=1$, the two power equalities force $a=b$.
::: {.proof}
If one of $a,b$ is zero, then the equality of any positive power forces the
other to be zero as well, because an integral domain has no nonzero
nilpotents. Hence assume $a,b\ne0$.

Pass to the fraction field $K$ of the domain and put
$$
r=ab^{-1}.
$$
The hypotheses imply
$$
r^m=1,
\qquad
r^n=1.
$$
If $\gcd(m,n)=1$, Bézout's identity gives integers $u,v$ such that
$$
um+vn=1.
$$
Therefore, in the multiplicative group $K^*$,
$$
r=r^{um+vn}=(r^m)^u(r^n)^v=1.
$$
Thus $a=b$.
:::

<1>2. For distinct exponents that are not coprime, the assertion can fail.
::: {.proof}
Take the integral domain $\mathbb Z$, let
$$
m=2,
\qquad
n=4,
\qquad
a=-1,
\qquad
b=1.
$$
Then
$$
a^2=b^2=1,
\qquad
a^4=b^4=1,
$$
but $a\ne b$.
:::

<1>3. Conclude the classification.
::: {.proof}
Step <1>1 gives a broad class of cases in which the implication is true,
while step <1>2 gives a valid counterexample to the unrestricted statement.
Hence
$$
\boxed{\text{sometimes true}.}
$$
:::
:::
