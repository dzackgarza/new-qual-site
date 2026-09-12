---
schema: qual/card@1
id: P-CEU5R
kind: problem
title: Contrapositive and negation of "if all birds swim or some fish fly, then no
  whales walk"
classification:
  areas:
  - prelim
  topics:
  - Logic and Quantifiers
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Write the following statement in symbolic form, and then give (in symbolic form and in English) its contrapositive and its negation:

"If all birds can swim or some fish can fly, then no whales can walk"
:::


::: solution
<1>1. Let the universe be all animals, and let
\[
B(x),S(x),F(x),Y(x),W(x),K(x)
\]
mean respectively that $x$ is a bird, can swim, is a fish, can fly, is a whale, and can walk.
:::

<1>2. The original statement is
\[
\left[(\forall x\,(B(x)\Rightarrow S(x)))\lor(\exists x\,(F(x)\land Y(x)))\right]
\Rightarrow
\left[\forall x\,(W(x)\Rightarrow \neg K(x))\right].
\]
:::

<1>3. Its contrapositive is
\[
\left[\exists x\,(W(x)\land K(x))\right]
\Rightarrow
\left[(\exists x\,(B(x)\land\neg S(x)))\land
(\forall x\,(F(x)\Rightarrow\neg Y(x)))\right].
\]
::: {.proof}
Write the original implication as $(A\lor C)\Rightarrow D$. Its contrapositive is
\[
\neg D\Rightarrow\neg(A\lor C),
\]
and De Morgan's law gives $\neg(A\lor C)=\neg A\land\neg C$. Moreover,
\[
\neg\forall x(B(x)\Rightarrow S(x))
\equiv \exists x(B(x)\land\neg S(x)),
\]
\[
\neg\exists x(F(x)\land Y(x))
\equiv \forall x(F(x)\Rightarrow\neg Y(x)),
\]
and
\[
\neg\forall x(W(x)\Rightarrow\neg K(x))
\equiv \exists x(W(x)\land K(x)).
\]
:::

<1>4. In English, the contrapositive is: "If some whale can walk, then some bird cannot swim and no fish can fly."
:::

<1>5. The negation of the original statement is
\[
\left[(\forall x\,(B(x)\Rightarrow S(x)))\lor(\exists x\,(F(x)\land Y(x)))\right]
\land
\left[\exists x\,(W(x)\land K(x))\right].
\]
::: {.proof}
The negation of an implication $P\Rightarrow Q$ is $P\land\neg Q$. Apply this with the antecedent and consequent from <1>2, and use the final equivalence in <1>3.
:::

<1>6. In English, the negation is: "All birds can swim or some fish can fly, and some whale can walk."
:::
:::
