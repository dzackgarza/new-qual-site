---
schema: qual/card@1
id: P-MMAQ-MLE74H7M42
kind: problem
title: Classification of finite fields
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 2 of the Algebra Preliminary Examination 2017 (University of
    Washington), printed p. 1 of the single-page paper retained at
    assets/attachments/UW-Algebra-Qual-2017.pdf, is the statement the card answers, and the
    paragraph at the head of the solution records that the paper prints no solutions, so the
    argument is the card's own. Checked: the statement against the paper's text layer at the page
    named; the solution read in both directions, existence of the field of p^n elements and
    uniqueness through the roots of X^{p^n} - X; `qualc.authoring check` on the card. The card
    carries no `pf` block, so `tmp/lam.sh` does not apply to it and was not run. Not checked: no
    retained solution set exists for this paper to compare the argument with, and no other card of
    the collection in this pass.
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Classify (with proof) all fields with finitely many elements.
:::


::: {.solution}

The problem is Problem 2 of the Algebra Preliminary Examination 2017 (University of Washington), printed p. 1 of the single-page paper retained at `assets/attachments/UW-Algebra-Qual-2017.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is both halves of the classification — that every finite field is $\FF_p[x]/(f)$ for an irreducible $f$, and that two fields of the same order $p^n$ are isomorphic because both consist of the roots of $X^{p^n}-X$.

Let $F$ be a finite field. Its characteristic is a prime $p$, so its prime subfield is $\FF_p$. Since $F$ is finite-dimensional over $\FF_p$, say
$$
[F:\FF_p]=n,
$$
we have
$$
\cardinality{F}=p^n.
$$
Thus every finite field has prime-power order.

Conversely, fix a prime $p$ and $n\ge1$, and work in an algebraic closure $\overline{\FF_p}$. Let
$$
E=\{a\in\overline{\FF_p}:a^{p^n}=a\}.
$$
If $a,b\in E$, then in characteristic $p$,
$$
(a+b)^{p^n}=a^{p^n}+b^{p^n}=a+b,
$$
and similarly $(ab)^{p^n}=ab$. Also, if $a\ne0$, then $a^{p^n-1}=1$, so
$$
(a^{-1})^{p^n}=a^{-1}.
$$
Hence $E$ is a field. It is exactly the set of roots of
$$
X^{p^n}-X.
$$
The derivative of this polynomial is $-1$, so all roots are simple. Therefore it has exactly $p^n$ roots in the algebraic closure, and
$$
\cardinality{E}=p^n.
$$
Thus a field of order $p^n$ exists for every prime power.

Finally, let $F$ be any field with $p^n$ elements. Its multiplicative group $F^\times$ has order $p^n-1$, so for every nonzero $a\in F$,
$$
a^{p^n-1}=1,
$$
and hence $a^{p^n}=a$; this is also true for $a=0$. Thus every element of $F$ is a root of $X^{p^n}-X$. Since $F$ is algebraic over $\FF_p$, there is an $\FF_p$-embedding $\iota:F\hookrightarrow\overline{\FF_p}$. Its image consists of $p^n$ roots of $X^{p^n}-X$, so $\iota(F)\subseteq E$, and equality holds because both sets have $p^n$ elements. Hence $F\cong E$.

Therefore, up to isomorphism, there is exactly one finite field of order $p^n$ for each prime power $p^n$, and there are no finite fields of any other order.
:::
