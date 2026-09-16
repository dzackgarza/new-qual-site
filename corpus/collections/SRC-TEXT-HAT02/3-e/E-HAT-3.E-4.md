---
schema: qual/card@1
id: E-HAT-3.E-4
kind: problem
title: "$SO(5)$ is not a product of two CW complexes"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.E, Exercise 4 and Example 3E.7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
Using the cup product structure in $H^*(SO(5); \mathbb{Z})$, show that $SO(5)$ is not homotopy equivalent to the product of any two CW complexes with nontrivial cohomology.
:::

::: {.solution}
Assume for contradiction that
\[
SO(5)\simeq X\times Y
\]
with both \(X\) and \(Y\) having nontrivial reduced cohomology. Replacing the factors by the images of the two standard retractions, each factor is homotopy dominated by \(SO(5)\). Hence its integral cohomology is a direct summand of the corresponding cohomology of \(SO(5)\); in particular all torsion in the factors is \(2\)-torsion.

Over \(\mathbb F_2\), Hatcher's computation gives
\[
H^*(SO(5);\mathbb F_2)
\cong
\mathbb F_2[\beta_1,\beta_3]/(\beta_1^8,\beta_3^2),
\qquad
|\beta_1|=1,\ |\beta_3|=3.
\]
By the field-coefficient Künneth theorem,
\[
H^*(SO(5);\mathbb F_2)
\cong H^*(X;\mathbb F_2)\otimes H^*(Y;\mathbb F_2)
\]
as graded algebras.

Let \(Q(A)=A^+/(A^+)^2\) denote the indecomposables of a connected graded algebra. Here
\[
QH^*(SO(5);\mathbb F_2)
\]
has dimension \(2\), with generators in degrees \(1\) and \(3\). For a tensor product,
\[
Q(B\otimes C)\cong QB\oplus QC.
\]
Since both factors have nontrivial reduced cohomology, both summands on the right are nonzero. Thus, after interchanging \(X,Y\), one factor has one indecomposable in degree \(1\), and the other has one in degree \(3\).

The degree-1 indecomposable is necessarily \(\beta_1\). Hence the first factor contains
\[
1,\beta_1,\dots,\beta_1^7,
\]
so its top nonzero degree is at least \(7\). The degree-3 generator of the other factor must therefore square to zero: otherwise that factor would have a nonzero class in degree \(6\), and multiplying it by \(\beta_1^7\) would give a nonzero class in degree \(13\), impossible since \(SO(5)\) has dimension \(10\).

The degree-3 elements of the displayed ring are
\[
0,\quad \beta_1^3,\quad \beta_3,\quad \beta_1^3+\beta_3.
\]
Their squares are respectively
\[
0,\quad \beta_1^6,\quad 0,\quad \beta_1^6.
\]
Thus the degree-3 factor generator is necessarily \(\beta_3\). Consequently, under the product decomposition, \(\beta_1\) comes from one factor and \(\beta_3\) from the other.

Now use the integral Bockstein
\[
\delta:H^*(-;\mathbb F_2)\longrightarrow H^{*+1}(-;\mathbb Z)
\]
for
\[
0\to\mathbb Z\xrightarrow{2}\mathbb Z\to\mathbb F_2\to0.
\]
Hatcher's calculation of the integral ring gives a class
\[
x\in H^2(SO(5);\mathbb Z),\qquad 2x=0,
\]
with
\[
\delta(\beta_1)=x,
\qquad
\delta(\beta_3)=x^2\ne0.
\]
The first equality and naturality show that \(x\) lies in the integral cohomology subring coming from the \(\beta_1\)-factor, hence so does \(x^2\). The second equality and naturality show that the same nonzero class \(x^2\) lies in the positive-degree subring coming from the \(\beta_3\)-factor.

But for a product, the images of the two projection maps on positive-degree cohomology have zero intersection. Indeed, if
\[
p_X^*a=p_Y^*b
\]
with \(|a|=|b|>0\), restricting to \(X\times\{y_0\}\) gives \(a=0\), while restricting to \(\{x_0\}\times Y\) gives \(b=0\). Hence their common class must be zero.

This contradicts \(x^2\ne0\). Therefore no such nontrivial product decomposition exists:
\[
\boxed{SO(5)\not\simeq X\times Y}
\]
whenever both factors have nontrivial cohomology.
:::
