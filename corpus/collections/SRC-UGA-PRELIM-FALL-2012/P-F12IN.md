---
schema: qual/card@1
id: P-F12IN
kind: problem
title: $A\subseteq f^{-1}(f(A))$, with equality when $f$ is injective
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's three-part proof into numbered steps; the inclusions for (a) and (b) and
    the constant-map example are unchanged. Checked: the elementwise arguments and the example.
    Not checked against a printed source: the UGA preliminary examinations are not retained in
    tmp/sources and the card records no page.
---

::: {.problem}
Let $f: X \to Y$ be a (not necessarily invertible) function, and $A \subseteq X$.

(a) Prove that $A \subseteq f^{-1}(f(A))$.

(b) Prove that if $f$ is injective (one-to-one) then $A = f^{-1}(f(A))$.

(c) Give an example for which $A \neq f^{-1}(f(A))$.
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $f:X\to Y$, $A\subseteq X$, $f(A)=\theset{f(a)\mid a\in A}$ and $f^{-1}(B)=\theset{x\in X\mid f(x)\in B}$.

::: pf

::: {.pf-step #a}

(a) $A\subseteq f^{-1}(f(A))$.

::: pf-proof

If $x\in A$ then $f(x)\in f(A)$ by definition of the image, so $x$ lies in the preimage of $f(A)$.

:::

:::

::: {.pf-step #b}

(b) If $f$ is injective then $f^{-1}(f(A))\subseteq A$.

::: pf-proof

Let $x\in f^{-1}(f(A))$, so $f(x)\in f(A)$ and there is $a\in A$ with $f(x)=f(a)$; injectivity gives $x=a\in A$.

:::

:::

::: {.pf-step #b2}

(b) If $f$ is injective then $A=f^{-1}(f(A))$.

::: pf-proof

Steps [](#a){.pf-ref} and [](#b){.pf-ref}.

:::

:::

::: {.pf-step #c}

(c) There is a map and a set with $A\neq f^{-1}(f(A))$.

::: pf-proof

Take $X=\theset{0,1}$, $Y=\theset{0}$, $f$ the constant map and $A=\theset{0}$. Then $f(A)=\theset{0}$ and $f^{-1}(f(A))=X$, which is not $A$.

:::

:::

:::

:::
