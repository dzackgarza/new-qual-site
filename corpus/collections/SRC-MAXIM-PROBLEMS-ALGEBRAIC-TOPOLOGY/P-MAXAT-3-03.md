---
schema: qual/card@1
id: P-MAXAT-3-03
kind: problem
title: Maxim algebraic topology 3.3
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 3, problem 3 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Prove Borsuk-Uhlam theorem.
:::

The Borsuk--Ulam theorem states that for every continuous map
\[
f:S^n\to\mathbb R^n
\]
there exists $x\in S^n$ such that
\[
f(x)=f(-x).
\]

::: pf

::: pf-step

Suppose, for contradiction, that
\[
f(x)\ne f(-x)
\qquad\text{for every }x\in S^n.
\]


::: pf-proof

This is the negation of the theorem's conclusion.

:::

:::

::: pf-step

Define
\[
g:S^n\to S^{n-1},
\qquad
g(x)=\frac{f(x)-f(-x)}{\|f(x)-f(-x)\|}.
\]
Then $g$ is continuous and odd:
\[
g(-x)=-g(x).
\]


::: pf-proof

The denominator is nonzero by step <1>1, so the normalization is defined and continuous. Moreover,
\[
g(-x)
=\frac{f(-x)-f(x)}{\|f(-x)-f(x)\|}
=-g(x).
\]

:::

:::

::: pf-step

Because $g$ is odd, it descends to a continuous map
\[
\bar g:\mathbb{RP}^{n}\to\mathbb{RP}^{n-1}
\]
satisfying
\[
q_{n-1}\circ g=\bar g\circ q_n,
\]
where $q_k:S^k\to\mathbb{RP}^k$ is the antipodal quotient.


::: pf-proof

The equality $g(-x)=-g(x)$ means that antipodal pairs in $S^n$ map to antipodal pairs in $S^{n-1}$. Hence the assignment
\[
[x]\longmapsto[g(x)]
\]
is well-defined and continuous on the quotient.

:::

:::

::: pf-step

If
\[
a\in H^1(\mathbb{RP}^{n};\mathbb F_2),
\qquad
b\in H^1(\mathbb{RP}^{n-1};\mathbb F_2)
\]
are the standard generators, then
\[
\bar g^*(b)=a.
\]


::: pf-proof

The double covers $S^n\to\mathbb{RP}^n$ and $S^{n-1}\to\mathbb{RP}^{n-1}$ are classified by the nonzero classes $a$ and $b$ in $H^1(-;\mathbb F_2)$. The commutative square in step <1>3 is a map of these double covers, so the pullback of the target cover along $\bar g$ is the source antipodal cover. Therefore their classifying classes satisfy $\bar g^*(b)=a$. Equivalently, for $n\ge2$, the induced map on fundamental groups sends the nontrivial antipodal loop to the nontrivial antipodal loop; the $n=1$ case is immediate separately.

:::

:::

::: pf-step

Hence
\[
\bar g^*(b^n)=a^n.
\]


::: pf-proof

Cohomology pullback is a ring homomorphism, so by step <1>4,
\[
\bar g^*(b^n)=(\bar g^*b)^n=a^n.
\]

:::

:::

::: pf-step

In the target,
\[
b^n=0,
\]
while in the source,
\[
a^n\ne0.
\]


::: pf-proof

The mod-$2$ cohomology rings are
\[
H^*(\mathbb{RP}^{n-1};\mathbb F_2)
\cong\mathbb F_2[b]/(b^n)
\]
and
\[
H^*(\mathbb{RP}^{n};\mathbb F_2)
\cong\mathbb F_2[a]/(a^{n+1}).
\]
Thus $b^n$ vanishes by the target truncation, whereas $a^n$ is the nonzero top-degree class of the source.

:::

:::

::: pf-step

Steps <1>5--<1>6 give a contradiction.


::: pf-proof

Since $b^n=0$, functoriality gives
\[
0=\bar g^*(b^n).
\]
But step <1>5 identifies this class with $a^n$, which is nonzero by step <1>6.

:::

:::

::: pf-step

Therefore there exists $x\in S^n$ such that
\[
\boxed{f(x)=f(-x)}.
\]


::: pf-proof

The contradiction in step <1>7 disproves the assumption in step <1>1, leaving exactly the Borsuk--Ulam conclusion.

:::

:::

::: pf-qed

Step <1>8 proves the theorem.

:::

:::
