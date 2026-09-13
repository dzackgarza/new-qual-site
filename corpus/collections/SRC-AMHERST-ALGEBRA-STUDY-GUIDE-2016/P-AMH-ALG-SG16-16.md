---
schema: qual/card@1
id: P-AMH-ALG-SG16-16
kind: problem
title: Amherst algebra study guide problem 16
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified that the explicit subtraction and absorption conditions are exactly the two-sided ideal axioms without relying on undefined shorthand.
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(January 2016) Define what it means for a subset $I\subseteq R$ to be an ideal of $R$.
Note: If you use other technical terms like "closed," "subring," "subgroup," etc., you must fully define those terms as well.

Answer: $I\subseteq R$ is an ideal if:

1. $I\ne\varnothing$.

2. For all $x,y\in I$, we have $x-y\in I$.

3. For all $x\in I$ and $r\in R$, we have $rx\in I$ and $xr\in I$.

DONE! Comment.

We often see answers to this question that look like the following: Answer: $I\subseteq R$ is an ideal if:

1. $I$ is a subgroup of $R$ under $+$.

2. For all $x\in I$ and $r\in R$, we have $rx\in I$ and $xr\in I$.

But you cannot say "DONE!" at this point.
Although it is technically a correct definition, it does not follow the instructions, since it uses the technical term "subgroup".

But if you add: 3. $I$ is a subgroup of $R$ under $+$ if it forms a group under $+$ itself.

Then you are not done, since "group" is also a technical term that you have to define.
This is why you should strike this out.

But if you replace it with: 3. $I$ is a subgroup of $R$ under $+$ if it is nonempty and closed under subtraction.

Then you are still not done since "closed" is also a technical term!
So you would have to add: 4. $I$ is closed under $-$ if for all $x,y\in I$, we have $x-y\in I$.
FINALLY DONE! Conclusion.

Hopefully the moral is clear here.
You should definitely think of the concepts like "subgroup under $+$" and "closed under subtraction" in your head, but you're going to have to write out their meanings anyhow.
So by all means think "closed," but write "for all $x,y\in I$, we have $x-y\in I$."
:::

:::::: {.solution}
A subset $I\subseteq R$ is a two-sided ideal precisely when the following three explicit conditions hold:

1. $I\ne\varnothing$.
2. For every $x,y\in I$, one has $x-y\in I$.
3. For every $x\in I$ and $r\in R$, one has both $rx\in I$ and $xr\in I$.

<1>1. Conditions 1 and 2 give exactly the required additive structure.
::: {.proof}
Choose $a\in I$, possible by condition 1. Then condition 2 gives
\[
0=a-a\in I.
\]
For $x\in I$,
\[
-x=0-x\in I.
\]
For $x,y\in I$, since $-y\in I$,
\[
x+y=x-(-y)\in I.
\]
Thus $I$ contains $0$ and is closed under addition and additive inverses. Conversely, any subset with those additive properties is nonempty and is closed under subtraction, because
\[
x-y=x+(-y).
\]
:::

<1>2. Condition 3 is exactly two-sided absorption by ring elements.
::: {.proof}
The definition of a two-sided ideal requires that multiplying an element of $I$ by an arbitrary element of $R$ on either side remains in $I$. Condition 3 states precisely
\[
rI\subseteq I
\qquad\text{and}\qquad
Ir\subseteq I
\]
for every $r\in R$.
:::

Hence the three displayed conditions are a complete definition of a two-sided ideal and use no further technical term that needs expansion.
:::
