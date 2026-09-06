---
schema: qual/card@1
id: P-AMD-PGA3YVH7
kind: problem
title: $\langle x,y\mid xy^2=y^3x,\, yx^2=x^3y\rangle$ is trivial
classification:
  areas:
  - algebra
  topics:
  - Group Presentations
  - Commutators
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 2, Exercise 9. The prior
    transcription omitted the trailing x in the first relation: the source has
    xy^2 = y^3 x, not xy^2 = y^3. Consequently the existing solution, which
    deduced x = y from the mistranscribed relation, solved a different group
    presentation and has been replaced.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Followed the source hint from xy^2x^{-1}=y^3 to obtain
    x^2y^8x^{-2}=y^18 and x^3y^8x^{-3}=y^27. The second relation identifies
    the latter conjugate with y times the former times y^{-1}, forcing y^9=e;
    the two defining relations then force y=e and x=e.
---

::: {.problem}
Consider the group
\[
G=\langle x,y\mid xy^2=y^3x,\ yx^2=x^3y\rangle.
\]
Show that $G$ is trivial.

**Hint.** First establish
\[
x^2y^8x^{-2}=y^{18}
\qquad\text{and}\qquad
x^3y^8x^{-3}=y^{27}
\]
using the first relation.
Then use the second relation to deduce $y^9=e$.
:::

::: {.solution}
<1>1. The first defining relation is equivalent to
\[
xy^2x^{-1}=y^3.
\]
::: {.proof}
Starting from
\[
xy^2=y^3x,
\]
multiply on the right by $x^{-1}$.
:::

<1>2. We have
\[
x^2y^8x^{-2}=y^{18}.
\]
::: {.proof}
By <1>1,
\[
xy^8x^{-1}
=x(y^2)^4x^{-1}
=(xy^2x^{-1})^4
=y^{12}.
\]
Conjugating once more by $x$ gives
\[
\begin{aligned}
x^2y^8x^{-2}
&=x y^{12}x^{-1}\\
&=x(y^2)^6x^{-1}\\
&=(xy^2x^{-1})^6\\
&=y^{18}.
\end{aligned}
\]
:::

<1>3. We have
\[
x^3y^8x^{-3}=y^{27}.
\]
::: {.proof}
Conjugate the identity in <1>2 by $x$:
\[
x^3y^8x^{-3}=xy^{18}x^{-1}.
\]
Since $y^{18}=(y^2)^9$, <1>1 gives
\[
xy^{18}x^{-1}
=(xy^2x^{-1})^9
=y^{27}.
\]
:::

<1>4. The second defining relation gives
\[
x^3=yx^2y^{-1}.
\]
::: {.proof}
From
\[
yx^2=x^3y,
\]
multiply on the right by $y^{-1}$.
:::

<1>5. We have $y^9=e$.
::: {.proof}
By <1>4,
\[
x^{-3}=yx^{-2}y^{-1}.
\]
Therefore
\[
\begin{aligned}
x^3y^8x^{-3}
&=(yx^2y^{-1})y^8(yx^{-2}y^{-1})\\
&=y(x^2y^8x^{-2})y^{-1}.
\end{aligned}
\]
Using <1>2, the right-hand side is
\[
y y^{18} y^{-1}=y^{18}.
\]
But <1>3 says that the same left-hand side is $y^{27}$.
Hence
\[
y^{27}=y^{18},
\]
and multiplying by $y^{-18}$ gives
\[
y^9=e.
\]
:::

<1>6. We have $y=e$.
::: {.proof}
Raise the conjugation identity in <1>1 to the third power:
\[
xy^6x^{-1}=y^9=e.
\]
Conjugation is injective, so $y^6=e$.
Together with <1>5,
\[
y^3=y^9(y^6)^{-1}=e.
\]

The first defining relation now becomes
\[
xy^2=y^3x=x.
\]
Left cancellation by $x$ gives $y^2=e$.
Since also $y^3=e$,
\[
y=y^3(y^2)^{-1}=e.
\]
:::

<1>7. We have $x=e$, and therefore $G$ is trivial.
::: {.proof}
Substitute $y=e$ from <1>6 into the second defining relation:
\[
x^2=x^3.
\]
Multiplying by $x^{-2}$ gives $x=e$.
Thus both generators are the identity, so
\[
G=\{e\}.
\]
:::
:::
