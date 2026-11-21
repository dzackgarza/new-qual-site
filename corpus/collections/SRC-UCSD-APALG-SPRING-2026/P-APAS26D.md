---
schema: qual/card@1
id: P-APAS26D
kind: problem
title: An algebra is commutative iff every element is normal
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 4 of the Spring 2026 Applied Algebra Qualifying Exam (Math 202 A/B/C),
    printed p. 8, is the statement the card answers, and the head of the solution names it; the retained
    file assets/attachments/SP26_202_Applied_Algebra_Qual.pdf numbers every page including the blank
    versos, so Problem 4 stands on its page 8. Checked: the statement against the paper's text layer at
    the page named; both directions, through the normality of $a+b$ and of $a+ib$; `qualc.authoring
    check` on the card, and `tmp/lam.sh` for the numbering and the QED. Not checked: no retained
    solution set exists for this paper to compare the argument with, and no other card of the collection
    in this pass.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, with both expansions written out
    rather than described: normality of a+b gives ab* + ba* = a*b + b*a after cancelling aa* = a*a
    and bb* = b*b, and normality of a+ib gives -ab* + ba* = a*b - b*a once the antilinearity
    (ib)* = -i b* is used. Adding and subtracting separate them into ba* = a*b and ab* = b*a, and
    the final step uses surjectivity of the involution, as the prose did. Checked that the argument
    needs nothing beyond the exam's stated structure (associative unital algebra with an antilinear
    antimultiplicative involutive conjugation): no norm, no C*-condition, and no argument that 1 is
    self-adjoint is required, since the conclusion is drawn from b -> b* being onto. Statement
    unchanged; the card says the argument is its own.
---

::: {.problem}
Let $\mathcal{A}$ be an algebra.
Prove that $\mathcal{A}$ is commutative if and only if all its elements are normal.

Note: On this exam, an algebra is a finite-dimensional complex vector space equipped with an associative, bilinear, unital multiplication and an antilinear, antimultiplicative, involutive conjugation.
:::

::: {.solution}

The problem is Problem 4 of the Spring 2026 Applied Algebra Qualifying Exam (Math 202 A/B/C), the retained file `assets/attachments/SP26_202_Applied_Algebra_Qual.pdf` numbers the blank versos too, so the problems stand on its even pages.

One direction is immediate. For the other, the normality of $a+b$ and of $a+ib$ gives two linear relations among the four products $ab^*$, $ba^*$, $a^*b$, $b^*a$, and adding and subtracting them separates $ab^*=b^*a$; since the involution is onto, that says every element commutes with every other. Nothing about a norm or a $C^*$-condition is used, only that the conjugation is antilinear, antimultiplicative and involutive. The argument is this card's own: no retained solution set covers this exam.

::: pf

::: {.pf-step #forward}
If $\mathcal A$ is commutative then every element is normal.

::: pf-proof
For $a\in\mathcal A$ one has $aa^*=a^*a$ by commutativity, with $a^*\in\mathcal A$; that is the definition of normality.
:::

:::


::: {.pf-step #sum}
With every element normal, for all $a,b$: $ab^*+ba^*=a^*b+b^*a$.

::: pf-proof
$a+b$ is an element of $\mathcal A$, hence normal:
$$
(a+b)(a+b)^*=(a+b)^*(a+b).
$$
Using $(a+b)^*=a^*+b^*$ (the involution is additive, being antilinear) and expanding,
$$
aa^*+ab^*+ba^*+bb^*=a^*a+a^*b+b^*a+b^*b .
$$
Normality of $a$ and of $b$ gives $aa^*=a^*a$ and $bb^*=b^*b$, and subtracting those two terms from both sides gives the displayed relation.
:::

:::


::: {.pf-step #ib}
With every element normal, for all $a,b$: $-ab^*+ba^*=a^*b-b^*a$.

::: pf-proof
Apply step [](#sum){.pf-ref} to the pair $a$ and $ib$, which are elements of $\mathcal A$: it gives $a(ib)^*+(ib)a^*=a^*(ib)+(ib)^*a$. The involution is antilinear, so $(ib)^*=\bar i\,b^*=-ib^*$, and then
$$
-i\,ab^*+i\,ba^*=i\,a^*b-i\,b^*a,
$$
using also $a^*(ib)=i\,a^*b$ and $(ib)^*a=-i\,b^*a$. Dividing by $i\ne0$ gives the displayed relation.
:::

:::


::: {.pf-step #separate}
Adding the two relations gives $ba^*=a^*b$, and subtracting them gives $ab^*=b^*a$.

::: pf-proof
Add $ab^*+ba^*=a^*b+b^*a$ and $-ab^*+ba^*=a^*b-b^*a$: the $ab^*$ terms cancel and $2ba^*=2a^*b$. Subtract the second from the first: the $ba^*$ terms cancel and $2ab^*=2b^*a$. Since $2\ne0$ in $\CC$, both displays follow.
:::

:::


::: {.pf-step #commute}
Every element of $\mathcal A$ commutes with every other.

::: pf-proof
By step [](#separate){.pf-ref}, $ab^*=b^*a$ for all $a,b$; writing $c=b^*$ and using that the involution is involutive and hence bijective, every element $c$ of $\mathcal A$ arises as $b^*$ for exactly one $b$, so $ac=ca$ for all $a,c$.
:::

:::


::: {.pf-step #conclusion}
$\mathcal A$ is commutative if and only if every element of $\mathcal A$ is normal.

::: pf-proof
Step [](#forward){.pf-ref} gives one direction, steps [](#sum){.pf-ref} to [](#commute){.pf-ref} the other. The hypotheses used are exactly the ones in the exam's note: associativity and bilinearity of the product, the identity, and an antilinear, antimultiplicative, involutive conjugation; no norm or $C^*$-condition enters.
:::

:::

:::
:::
