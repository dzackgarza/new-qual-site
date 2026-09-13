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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(January 2016) Define what it means for a subset $I\subseteq R$ to be an ideal of $R$. Note: If you use other technical terms like "closed," "subring," "subgroup," etc., you must fully define those terms as well.

Answer: $I\subseteq R$ is an ideal if:

1. $I\ne\varnothing$.
2. For all $x,y\in I$, we have $x-y\in I$.
3. For all $x\in I$ and $r\in R$, we have $rx\in I$ and $xr\in I$.

DONE! Comment.

We often see answers to this question that look like the following: Answer: $I\subseteq R$ is an ideal if:

1. $I$ is a subgroup of $R$ under $+$.
2. For all $x\in I$ and $r\in R$, we have $rx\in I$ and $xr\in I$.

But you cannot say "DONE!" at this point. Although it is technically a correct definition, it does not follow the instructions, since it uses the technical term "subgroup".

But if you add: 3. $I$ is a subgroup of $R$ under $+$ if it forms a group under $+$ itself.

Then you are not done, since "group" is also a technical term that you have to define. This is why you should strike this out.

But if you replace it with: 3. $I$ is a subgroup of $R$ under $+$ if it is nonempty and closed under subtraction.

Then you are still not done since "closed" is also a technical term! So you would have to add: 4. $I$ is closed under $-$ if for all $x,y\in I$, we have $x-y\in I$. FINALLY DONE! Conclusion.

Hopefully the moral is clear here. You should definitely think of the concepts like "subgroup under $+$" and "closed under subtraction" in your head, but you're going to have to write out their meanings anyhow. So by all means think "closed," but write "for all $x,y\in I$, we have $x-y\in I$."
:::
