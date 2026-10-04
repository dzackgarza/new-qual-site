---
schema: qual/card@1
id: P-AMH-ALG-SG16-16
kind: problem
title: Definition of an ideal of a ring
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

::: {.solution}
<1>1. A subset $I\subseteq R$ is a two-sided ideal if and only if all three
conditions hold:

(a) $I\neq\varnothing$.

(b) For all $x,y\in I$, one has $x-y\in I$.

(c) For all $x\in I$ and $r\in R$, one has $rx\in I$ and $xr\in I$.

::: {.proof}
These conditions are explicit and contain no undefined auxiliary term such as
“subgroup” or “closed under subtraction.”  Steps <1>2--<1>4 verify that they
are exactly the usual two-sided ideal axioms.
:::

<1>2. Conditions (a) and (b) imply that $0\in I$ and that $I$ is closed under
additive inverses.

::: {.proof}
Choose $a\in I$, which is possible by (a).  Then (b) gives
$$
0=a-a\in I.
$$
If $x\in I$, then $0,x\in I$, so another application of (b) gives
$$
-x=0-x\in I.
$$
:::

<1>3. Conditions (a) and (b) imply that $I$ is closed under addition.

::: {.proof}
Let $x,y\in I$.  By step <1>2, $-y\in I$.  Applying (b) to $x$ and $-y$
gives
$$
x+y=x-(-y)\in I.
$$
Thus $I$ is an additive subgroup of the underlying additive group of $R$,
with the subgroup property written out explicitly.
:::

<1>4. Condition (c) is exactly the required two-sided absorption condition.

::: {.proof}
For every $r\in R$ and $x\in I$, condition (c) asserts both
$$
rx\in I
\qquad\text{and}\qquad
xr\in I.
$$
Thus multiplication by an arbitrary ring element on either side preserves
$I$.
:::

<1>5. Conversely, every two-sided ideal satisfies conditions (a)--(c).

::: {.proof}
A two-sided ideal is an additive subgroup of $R$, so it contains $0$ and is
therefore nonempty.  If $x,y\in I$, then $-y\in I$ and hence
$$
x-y=x+(-y)\in I,
$$
which proves (b).  The two-sided ideal absorption axiom is precisely (c).
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>2--<1>4 show that conditions (a)--(c) imply the usual two-sided ideal
axioms, and step <1>5 proves the converse.  Therefore the three explicit
conditions in step <1>1 give the requested definition without invoking any
further technical term.
:::
:::
