---
schema: qual/card@1
id: P-AMD-S4NV7CHI
kind: problem
title: $Q_8\cong\langle a,b\mid a^2=b^2,\, a^{-1}ba=b^{-1}\rangle$
classification:
  areas:
  - algebra
  topics:
  - Group Presentations
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 2, Exercise 8. The source
    asks exactly for the presentation Q_8=<a,b | a^2=b^2, a^{-1}ba=b^{-1}>.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    The relations imply a^4=b^4=e and allow every word to reduce to
    a^epsilon b^r with epsilon in {0,1} and r modulo 4, so the presented group
    has at most eight elements. Sending a to i and b to j gives a surjection
    onto the eight-element quaternion group, hence an isomorphism.
---

::: {.problem}
Prove that
\[
Q_8\cong\langle a,b\mid a^2=b^2,\ a^{-1}ba=b^{-1}\rangle.
\]
:::

::: {.solution}
Let
\[
P=\langle a,b\mid a^2=b^2,\ a^{-1}ba=b^{-1}\rangle.
\]

<1>1. In $P$,
\[
a^4=b^4=e.
\]
::: {.proof}
Conjugating $b^2$ by $a$ and using $a^{-1}ba=b^{-1}$ gives
\[
a^{-1}b^2a=b^{-2}.
\]
Since $b^2=a^2$, the left side is
\[
a^{-1}a^2a=a^2.
\]
Thus
\[
a^2=b^{-2}.
\]
But $a^2=b^2$, so $b^2=b^{-2}$, hence $b^4=e$.
Consequently
\[
a^4=(a^2)^2=(b^2)^2=b^4=e.
\]
:::

<1>2. The defining conjugation relation gives
\[
ba=ab^{-1}
\qquad\text{and}\qquad
b^{-1}a=ab.
\]
::: {.proof}
Multiplying
\[
a^{-1}ba=b^{-1}
\]
on the left by $a$ gives
\[
ba=ab^{-1}.
\]
Taking inverses of the defining relation yields
\[
a^{-1}b^{-1}a=b,
\]
and multiplying on the left by $a$ gives
\[
b^{-1}a=ab.
\]
:::

<1>3. Every element of $P$ is represented by one of the eight words
\[
b^r
\qquad\text{or}\qquad
ab^r,
\qquad
r=0,1,2,3.
\]
::: {.proof}
By <1>1, inverses may be replaced by positive powers:
\[
a^{-1}=a^3,
\qquad
b^{-1}=b^3.
\]
Using <1>2 repeatedly, move every occurrence of $a$ to the left of every occurrence of $b$.
Thus every word is equal in $P$ to
\[
a^m b^n
\]
for some integers $m,n$.
By <1>1, reduce both exponents modulo $4$.

Finally, use $a^2=b^2$.
If $m=2$, then
\[
a^2b^n=b^{n+2},
\]
and if $m=3$, then
\[
a^3b^n=a(a^2)b^n=ab^{n+2}.
\]
Hence $m$ can be reduced to $0$ or $1$, while $n$ is taken modulo $4$.
This gives at most the eight displayed normal forms.
Therefore
\[
|P|\le8.
\]
:::

<1>4. The assignments
\[
a\longmapsto i,
\qquad
b\longmapsto j
\]
define a surjective homomorphism $\Phi:P\to Q_8$.
::: {.proof}
Recall
\[
Q_8=\{\pm1,\pm i,\pm j,\pm k\},
\qquad
i^2=j^2=k^2=-1,
\qquad
ij=k.
\]
The first defining relation is satisfied because
\[
i^2=j^2=-1.
\]
For the second,
\[
i^{-1}ji=(-i)ji=-ki=-j=j^{-1}.
\]
Thus the universal property of the presentation gives a homomorphism
\[
\Phi:P\longrightarrow Q_8
\]
with $\Phi(a)=i$ and $\Phi(b)=j$.

The elements $i$ and $j$ generate $Q_8$: their product is $k$, and $i^2=-1$ supplies all negatives.
Hence $\Phi$ is surjective.
:::

<1>5. The homomorphism $\Phi$ is an isomorphism.
::: {.proof}
By <1>3, the group $P$ has at most eight elements.
By <1>4, it surjects onto $Q_8$, which has exactly eight elements.
Therefore $|P|\ge8$, so in fact
\[
|P|=8.
\]
A surjection between two finite sets of the same cardinality is bijective.
Thus $\Phi$ is an isomorphism, proving the stated presentation of $Q_8$.
:::
:::
