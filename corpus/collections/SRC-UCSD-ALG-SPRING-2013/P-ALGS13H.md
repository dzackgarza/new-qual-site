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
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 8 of the Spring 2013 UCSD Algebra Qualifying Examination, printed p. 1
    of the single-page paper retained at assets/attachments/SP13_200_Algebra_Qual.pdf, is the statement
    the card answers, and the paragraph at the head of the solution records that the paper prints no
    solutions, so the argument is the card's own. Checked: the statement against the paper's text layer
    at the page named; both parts, including the two factorizations of 6 in $\ZZ[\sqrt{-5}]$ and the
    quotient $\ZZ[x]/(x^2+5)$; `qualc.authoring check` on the card, and `tmp/lam.sh` for the numbering
    and the QED. Not checked: no retained solution set exists for this paper to compare the argument
    with, and no other card of the collection in this pass.
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

::: {.problem}
(a) Give an example of an integral domain which is not a UFD. Give a brief proof that it is not a UFD.

(b) Find a UFD $A$ and a prime ideal $\mathfrak{p} \subseteq A$ such that $A/\mathfrak{p}$ is not a UFD. (Hint: use part (a)!)
:::

::: {.solution}

The problem is Problem 8 of the Spring 2013 UCSD Algebra Qualifying Examination, printed p. 1 of the single-page paper retained at `assets/attachments/SP13_200_Algebra_Qual.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is (a) $\ZZ[\sqrt{-5}]$ with the two factorizations of $6$, and the norm argument that $2$, $3$, $1\pm\sqrt{-5}$ are irreducible and no element has norm $2$ or $3$; (b) the UFD $\ZZ[x]$ with the prime ideal $(x^2+5)$, whose quotient is $\ZZ[\sqrt{-5}]$


::: pf

::: {.pf-step #s1}

Let
$$
R=\ZZ[\sqrt{-5}]=\{a+b\sqrt{-5}:a,b\in\ZZ\}.
$$
Then $R$ is an integral domain.

::: pf-proof

It is a subring of the field $\QQ(\sqrt{-5})$.

:::

:::

::: pf-step

Define the norm
$$
N(a+b\sqrt{-5})=(a+b\sqrt{-5})(a-b\sqrt{-5})=a^2+5b^2.
$$
Then $N(xy)=N(x)N(y)$, and the units of $R$ are exactly $\pm1$.

::: pf-proof

Multiplicativity is immediate from conjugation.
If $u$ is a unit, then $1=N(1)=N(u)N(u^{-1})$, so $N(u)=1$. The equation $a^2+5b^2=1$ gives $b=0$ and $a=\pm1$. Conversely $\pm1$ are units.

:::

:::

::: pf-step

There are no elements of norm $2$ or $3$ in $R$.

::: pf-proof

If $a^2+5b^2\in\{2,3\}$, then $b=0$, so $a^2\in\{2,3\}$, impossible in $\ZZ$.

:::

:::

::: {.pf-step #s4}

The elements $2$, $3$, $1+\sqrt{-5}$, and $1-\sqrt{-5}$ are irreducible in $R$.

::: pf-proof

Their norms are $4,9,6,6$, respectively.
In a nontrivial factorization into nonunits, multiplicativity of the norm would factor these integers into norms strictly larger than $1$. For norm $4$, the only possibility is $2\cdot2$, but norm $2$ does not occur.
For norm $9$, the only possibility is $3\cdot3$, but norm $3$ does not occur.
For norm $6$, the only nontrivial possibility is $2\cdot3$, but neither norm occurs.
Hence all four elements are irreducible.

:::

:::

::: {.pf-step #s5}

We have two inequivalent factorizations
$$
6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5}).
$$
Thus $R$ is not a UFD.

::: pf-proof

The equality is immediate.
The only units are $\pm1$, so elements with different norms cannot be associates.
Hence neither $2$ nor $3$ is associate to either $1+\sqrt{-5}$ or $1-\sqrt{-5}$. By step [](#s4){.pf-ref}, these are two genuinely different factorizations into irreducibles.

:::

:::

::: {.pf-step #s6}

For part (b), take the UFD $A=\ZZ[x]$ and the ideal
$$
\mathfrak p=(x^2+5).
$$
Then
$$
A/\mathfrak p\cong \ZZ[\sqrt{-5}]=R.
$$

::: pf-proof

The evaluation homomorphism $\ZZ[x]\to R$ defined by $x\mapsto\sqrt{-5}$ is surjective.
Division by the monic polynomial $x^2+5$ shows that every polynomial has a unique remainder $a+bx$; such a remainder maps to zero only when $a+b\sqrt{-5}=0$, hence $a=b=0$. Therefore the kernel is exactly $(x^2+5)$, giving the stated isomorphism.

:::

:::

::: pf-step

The ideal $\mathfrak p$ is prime, but $A/\mathfrak p$ is not a UFD.

::: pf-proof

By step [](#s6){.pf-ref}, the quotient is isomorphic to $R$, which is an integral domain by step [](#s1){.pf-ref}; hence $\mathfrak p$ is prime.
The quotient is not a UFD by step [](#s5){.pf-ref}. Since $\ZZ[x]$ is a UFD by Gauss's lemma, this answers part (b).

:::

:::

:::

:::
