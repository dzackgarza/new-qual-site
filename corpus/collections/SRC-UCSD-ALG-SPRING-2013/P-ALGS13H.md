---
schema: qual/card@1
id: P-ALGS13H
kind: problem
title: Integral domain that is not a UFD; quotient of a UFD that is not a UFD
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
(a) Give an example of an integral domain which is not a UFD. Give a brief proof that it is not a UFD.

(b) Find a UFD $A$ and a prime ideal $\mathfrak{p} \subseteq A$ such that $A/\mathfrak{p}$ is not a UFD. (Hint: use part (a)!)
:::

::: {.solution}
<1>1. Let
\[
R=\mathbb Z[\sqrt{-5}]=\{a+b\sqrt{-5}:a,b\in\mathbb Z\}.
\]
Then \(R\) is an integral domain.
::: {.proof}
It is a subring of the field \(\mathbb Q(\sqrt{-5})\).
:::

<1>2. Define the norm
\[
N(a+b\sqrt{-5})=(a+b\sqrt{-5})(a-b\sqrt{-5})=a^2+5b^2.
\]
Then \(N(xy)=N(x)N(y)\), and the units of \(R\) are exactly \(\pm1\).
::: {.proof}
Multiplicativity is immediate from conjugation.
If \(u\) is a unit, then \(1=N(1)=N(u)N(u^{-1})\), so \(N(u)=1\). The equation \(a^2+5b^2=1\) gives \(b=0\) and \(a=\pm1\). Conversely \(\pm1\) are units.
:::

<1>3. There are no elements of norm \(2\) or \(3\) in \(R\).
::: {.proof}
If \(a^2+5b^2\in\{2,3\}\), then \(b=0\), so \(a^2\in\{2,3\}\), impossible in \(\mathbb Z\).
:::

<1>4. The elements \(2\), \(3\), \(1+\sqrt{-5}\), and \(1-\sqrt{-5}\) are irreducible in \(R\).
::: {.proof}
Their norms are \(4,9,6,6\), respectively.
In a nontrivial factorization into nonunits, multiplicativity of the norm would factor these integers into norms strictly larger than \(1\). For norm \(4\), the only possibility is \(2\cdot2\), but norm \(2\) does not occur.
For norm \(9\), the only possibility is \(3\cdot3\), but norm \(3\) does not occur.
For norm \(6\), the only nontrivial possibility is \(2\cdot3\), but neither norm occurs.
Hence all four elements are irreducible.
:::

<1>5. We have two inequivalent factorizations
\[
6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5}).
\]
Thus \(R\) is not a UFD.
::: {.proof}
The equality is immediate.
The only units are \(\pm1\), so elements with different norms cannot be associates.
Hence neither \(2\) nor \(3\) is associate to either \(1+\sqrt{-5}\) or \(1-\sqrt{-5}\). By <1>4, these are two genuinely different factorizations into irreducibles.
:::

<1>6. For part (b), take the UFD \(A=\mathbb Z[x]\) and the ideal
\[
\mathfrak p=(x^2+5).
\]
Then
\[
A/\mathfrak p\cong \mathbb Z[\sqrt{-5}]=R.
\]
::: {.proof}
The evaluation homomorphism \(\mathbb Z[x]\to R\) defined by \(x\mapsto\sqrt{-5}\) is surjective.
Division by the monic polynomial \(x^2+5\) shows that every polynomial has a unique remainder \(a+bx\); such a remainder maps to zero only when \(a+b\sqrt{-5}=0\), hence \(a=b=0\). Therefore the kernel is exactly \((x^2+5)\), giving the stated isomorphism.
:::

<1>7. The ideal \(\mathfrak p\) is prime, but \(A/\mathfrak p\) is not a UFD.
::: {.proof}
By <1>6, the quotient is isomorphic to \(R\), which is an integral domain by <1>1; hence \(\mathfrak p\) is prime.
The quotient is not a UFD by <1>5. Since \(\mathbb Z[x]\) is a UFD by Gauss's lemma, this answers part (b).
:::
:::
