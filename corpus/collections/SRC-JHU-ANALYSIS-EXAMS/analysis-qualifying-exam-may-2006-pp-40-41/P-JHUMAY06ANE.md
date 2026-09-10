---
schema: qual/card@1
id: P-JHUMAY06ANE
kind: problem
title: Derivative range of a half-plane self-map at a fixed point
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "PDF page 40, May 2006 problem 5, asks for a maximum of f prime without modulus bars. Preserved the question and resolved the ambiguity by determining all possible complex derivatives."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified that conjugation cancels the normalization derivatives, that every value in the closed unit disk occurs, and that modulus and real-value maxima are both one."
---

5. Let H denote the upper half plane $\{ z \in \mathbb { C } : \operatorname { I m } z > 0 \}$ . Suppose that $f : H \to H$ is holomorphic, and $f ( 3 + 1 7 i ) = 3 + 1 7 i$ What is the maximum possible value of $f ^ { \prime } ( 3 { + } 1 7 i )$ . Give a reason for your answer (and try not to do any lengthy computations).

::: remark
A complex derivative need not be real, so a maximum
requires a real-valued objective. The complete derivative
range below gives both the maximum modulus and the
largest possible real derivative, without assuming that
all derivatives are real.
:::

::: solution
Let $a=3+17i$ and $D=\{w\in\mathbb C:|w|<1\}$.
The possible values are exactly
$$
\boxed{\{f'(a):f:H\to H\text{ holomorphic},\ f(a)=a\}
=\{\lambda\in\mathbb C:|\lambda|\leq1\}.}
$$
In particular $\max|f'(a)|=1$, and the largest possible
real value of $f'(a)$ is also one, attained by $f(z)=z$.

<1>1. Conjugation to the disk bounds the derivative.
::: proof
The fractional map
$$
\phi(z)=\frac{z-a}{z-\overline a},\qquad
\phi^{-1}(w)=\frac{a-\overline a w}{1-w}
$$
is a biholomorphism $H\to D$, with $\phi(a)=0$.
Indeed,
$$
1-|\phi(z)|^2
=\frac{4\operatorname{Im}a\operatorname{Im}z}{|z-\overline a|^2}>0,
\qquad
\operatorname{Im}\phi^{-1}(w)
=\operatorname{Im}a\frac{1-|w|^2}{|1-w|^2}>0,
$$
and substitution verifies that the formulas are inverse.
For $F=\phi\circ f\circ\phi^{-1}$, one has $F:D\to D$
holomorphic and $F(0)=0$. The chain rule and
$(\phi^{-1})'(0)=1/\phi'(a)$ give $F'(0)=f'(a)$.
Schwarz's lemma therefore gives $|f'(a)|\leq1$ [@SS03].
:::

<1>2. Every derivative in that disk is attained.
::: proof
For any $|\lambda|\leq1$, the map $w\mapsto\lambda w$
takes $D$ into $D$, including when $\lambda=0$. Thus
$$
f_\lambda(z)=\phi^{-1}\bigl(\lambda\phi(z)\bigr)
$$
is a holomorphic self-map of $H$, fixes $a$ and has
derivative $f_\lambda'(a)=\lambda$ by the same chain-rule
cancellation. This proves equality of the stated sets.
For example $\lambda=i$ gives a nonreal derivative,
while $\lambda=1$ gives the identity and attains both
real-valued maxima described above.
:::
:::
