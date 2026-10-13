---
schema: qual/card@1
id: P-GRECH1-13
kind: problem
title: Remainder of $p(x)$ modulo $x^2-1$ from its values at $\pm1$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 13 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
When the polynomial $p(x)$ is divided by $x - 1$, it leaves a remainder of 1, and when $p(x)$ is divided by $x + 1$, it leaves a remainder of $-1$. Find the remainder when $p(x)$ is divided by $x^2 - 1$.

(A) $-1$
(B) $0$
(C) $x$
(D) $-x$
(E) $2x$
:::

::: {.solution}
Write the remainder upon division by $x^2-1$ as $r(x)=ax+b$.

<1>1. $r(1)=1$ and $r(-1)=-1$.

::: {.proof}
The given remainders modulo $x-1$ and $x+1$ imply, by the remainder theorem,
$$
p(1)=1,\qquad p(-1)=-1.
$$
Since $p(x)-r(x)$ is divisible by $x^2-1=(x-1)(x+1)$, it vanishes at both $1$ and $-1$. Hence
$$
r(1)=p(1)=1,\qquad r(-1)=p(-1)=-1.
$$
:::

<1>2. $a=1$ and $b=0$.

::: {.proof}
Step <1>1 gives
$$
a+b=1,\qquad -a+b=-1.
$$
Adding the equations gives $2b=0$, so $b=0$, and then $a=1$.
:::

<1>3. The required remainder is
$$
\boxed{r(x)=x},
$$
so the answer is (C).

::: {.proof}
Substitute the coefficients from step <1>2 into $r(x)=ax+b$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the unique remainder of degree less than $2$.
:::
:::
