---
schema: qual/card@1
id: P-AMH-ALG-SG16-27
kind: problem
title: Amherst algebra study guide problem 27
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
(March 2009) Let F be a ﬁeld, let R = F[x] be the ring of polynomials in one variable with coeﬃcients in F, and let f(x)∈R be a polynomial of degree 2009. Let I ={g(x)f(x)|g∈R} be the set of all polynomials which are multiples of f(x). It is a fact, which you may assume, that I is an ideal of R. (a) For any g,h∈R, prove that I +g =I +h if and only if (g−h) is divisible by f. (b) Prove that for any g∈ R, there is a unique polynomial h∈ R with deg h < 2009 such that I +g =I +h.
:::

::: {.solution}
Proof. (a) Given g,h∈R, we have I +g =I +h if and only if g−h∈I, by the coset relation. But
the deﬁnition of I implies that g−h∈I if and only if g−h is a multiple of f.
(b) Given g∈R:
(Existence) The division algorithm yields q,h∈ F[x] such that
g =qf +h with deg h< degf = 2009.
Thusg−h =qf∈I, so by part (a), I +g =I +h, proving existence.
(Uniqueness) Suppose we are givenh,h′∈R withI+g =I+h′ =I+h′, and with degh, degh′ < 2009.
Then I +h =I +h′, so by part (a), h−h′ is a multiple of f. That is,
h−h′ =kf for some k∈R.
If k⁄= 0, then
deg(h−h′) = deg(kf ) = degk + degf≥ degf = 2009.
However, the fact that deg h, degh′ < 2009 implies that deg(h−h′)< 2009 also, a contradiction.
Thus, we must have k = 0, and hence h−h′ = 0. That is, h =h′, proving uniqueness. QED
Every Ideal in k[x] is Principal. Recall that a principal ideal in a commutative ring consists of all
multiples of a ﬁxed element. Problem 27 features principal ideals in k[x]. This is no accident, since
every ideal in k[x] is of the form ⟨f⟩ ={gf|g∈k[x]}.
Furthermore,f is unique up to multiplication by a nonzero constant ofk. Since the units of k[x] are precisely
the nonzero constants, we can equivalently say that f is unique up to multiplication by a unit.
Irreducible Polynomials and Maximal Ideals in k[x]. Know the following:
• The deﬁnition of reducible and irreducible polynomial in k[x].
• The irreducibility criterion for polynomials f∈k[x] of degree 2 or 3: such a polynomial is irreducible
if and only if it has no roots in the ﬁeld k. (See problem 28 below for a proof of this fact for cubic
polynomials; can you do the proof for quadratic polynomials?)
• An ideal I⊆k[x] is maximal if and only if I =⟨f⟩, where f∈k[x] irreducible. That is:
f is irreducible ⇐⇒ ⟨f⟩⊆ k[x] is maximal ⇐⇒ k[x]/⟨f⟩ is a ﬁeld.
Here some problems about these concepts.
:::
