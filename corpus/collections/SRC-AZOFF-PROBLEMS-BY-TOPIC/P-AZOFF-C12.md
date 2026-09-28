---
schema: qual/card@1
id: P-AZOFF-C12
kind: problem
title: Möbius transformations preserving the extended real line
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Conformal mapping, Problem 12, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    Page 3 of the retained PDF really prints T(alpha)=alpha in condition (d);
    vector inspection confirms that the overbars occur only in the beta
    equality. The printed claim that (a)--(d) are all equivalent is false:
    T(z)=-1/z satisfies (a)--(c) but has only the fixed points +/-i. The card
    retains the four printed conditions and corrects only the requested
    implication pattern.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Proved (a)--(c) equivalent, proved (d) implies them by comparing T with
    conjugation composed with T composed with conjugation at the three
    distinct points alpha, beta, and conjugate beta, and verified the
    counterexample T(z)=-1/z. The source error is recorded in COMPLAINTS.md.
---

::: {.problem}
(Can omit; related to the discussion of symmetry) Let $T$ be the Möbius transformation
$$
T(z)=\frac{az+b}{cz+d}.
$$
Consider the following conditions.

a) T maps $\mathbb { R } \cup \{ \infty \}$ onto itself.

b) It is possible to choose $a , b , c , d \in \mathbb { R }$

c) ${ \overline { { T z } } } = T ( { \overline { { z } } } )$ for every $z \in \mathbb { C } \cup \infty$

d) There exist $\alpha \in \mathbb { R }$ and $\beta \in \mathbb { C } \backslash \mathbb { R }$ satisfying T (α) = α and $T ( \overline { { \beta } } ) = \overline { { T \beta } }$

Prove that (a), (b), and (c) are equivalent. Prove that (d) implies these
conditions, and show that the converse need not hold.
:::

::: {.solution}
Let
$$
\widehat{\RR}=\RR\cup\{\infty\}
$$
and let
$$
J:\widehat{\CC}\longrightarrow\widehat{\CC},
\qquad
J(z)=\bar z,
\qquad
J(\infty)=\infty.
$$
The fixed-point set of $J$ is exactly $\widehat{\RR}$.

<1>1. Condition (b) implies condition (c).

::: {.proof}
Choose a representative
$$
T(z)=\frac{az+b}{cz+d}
$$
with
$$
a,b,c,d\in\RR,
\qquad
ad-bc\neq0.
$$
For every finite $z$ at which the displayed fractions are finite,
$$
\overline{T(z)}
=
\frac{a\bar z+b}{c\bar z+d}
=
T(\bar z).
$$
The same identity holds at the pole and at $\infty$ in the Riemann sphere,
because real coefficients make the pole and the corresponding extended
values conjugation-invariant. Hence
$$
J\circ T=T\circ J
$$
on all of $\widehat{\CC}$, which is condition (c).
:::

<1>2. Condition (c) implies condition (a).

::: {.proof}
Assume
$$
J\circ T=T\circ J.
$$
If
$$
x\in\widehat{\RR},
$$
then $J(x)=x$, so
$$
J(T(x))
=
T(J(x))
=
T(x).
$$
Thus $T(x)$ is fixed by $J$, and therefore
$$
T(\widehat{\RR})\subseteq\widehat{\RR}.
$$

Taking inverses in
$$
J\circ T=T\circ J
$$
gives
$$
T^{-1}\circ J
=
J\circ T^{-1}.
$$
The same argument applied to $T^{-1}$ gives
$$
T^{-1}(\widehat{\RR})\subseteq\widehat{\RR}.
$$
Equivalently,
$$
\widehat{\RR}\subseteq T(\widehat{\RR}).
$$
Hence
$$
T(\widehat{\RR})=\widehat{\RR},
$$
which is condition (a).
:::

<1>3. Condition (a) implies condition (b).

::: {.proof}
Assume
$$
T(\widehat{\RR})=\widehat{\RR}.
$$
Choose three distinct finite points
$$
x_1,x_2,x_3\in\RR
$$
none of which is the pole of $T$. Then
$$
y_j=T(x_j)\in\RR
$$
for $j=1,2,3$, and the $y_j$ are distinct because $T$ is injective.

Define
$$
A(z)
=
\frac{(z-x_2)(x_3-x_1)}
{(z-x_1)(x_3-x_2)}
$$
and
$$
B(z)
=
\frac{(z-y_2)(y_3-y_1)}
{(z-y_1)(y_3-y_2)}.
$$
Both are Möbius transformations with real coefficients, and
$$
\begin{aligned}
A(x_1)&=\infty,&A(x_2)&=0,&A(x_3)&=1,\\
B(y_1)&=\infty,&B(y_2)&=0,&B(y_3)&=1.
\end{aligned}
$$
Therefore
$$
S=B\circ T\circ A^{-1}
$$
fixes the three points
$$
\infty,\quad0,\quad1.
$$
A Möbius transformation fixing $\infty$ has zero lower-left coefficient;
fixing $0$ then forces its upper-right coefficient to vanish; fixing $1$
forces the two remaining diagonal coefficients to agree up to the common
projective scalar. Hence $S$ is the identity.

Thus
$$
T=B^{-1}\circ A.
$$
Both $A$ and $B^{-1}$ have real coefficients, so their composition admits
real coefficients. This is condition (b).
:::

<1>4. Conditions (a), (b), and (c) are equivalent.

::: {.proof}
Steps <1>1--<1>3 give the cycle
$$
\text{(b)}
\Longrightarrow
\text{(c)}
\Longrightarrow
\text{(a)}
\Longrightarrow
\text{(b)}.
$$
:::

<1>5. Condition (d) implies condition (c).

::: {.proof}
Assume condition (d). Thus there are
$$
\alpha\in\RR,
\qquad
\beta\in\CC\sm\RR
$$
such that
$$
T(\alpha)=\alpha
$$
and
$$
T(\bar\beta)=\overline{T(\beta)}.
$$
Define the Möbius transformation
$$
S=J\circ T\circ J.
$$

Since $\alpha$ is real,
$$
S(\alpha)
=
J(T(\alpha))
=
\alpha
=
T(\alpha).
$$
Using the second hypothesis in (d),
$$
\begin{aligned}
S(\beta)
&=
J(T(\bar\beta))\\
&=
J(\overline{T(\beta)})\\
&=
T(\beta),
\end{aligned}
$$
and also
$$
S(\bar\beta)
=
J(T(\beta))
=
\overline{T(\beta)}
=
T(\bar\beta).
$$
The three points
$$
\alpha,\quad\beta,\quad\bar\beta
$$
are distinct. Two Möbius transformations agreeing at three distinct points
are equal, so
$$
S=T.
$$
Thus
$$
J\circ T\circ J=T,
$$
and composing on the right with $J$ gives
$$
J\circ T=T\circ J.
$$
This is condition (c).
:::

<1>6. Condition (d) therefore implies each of (a), (b), and (c).

::: {.proof}
Step <1>5 gives (c), and step <1>4 gives the equivalence of (a)--(c).
:::

<1>7. The converse implication from (a)--(c) to (d) is false.

::: {.proof}
Consider
$$
T(z)=-\frac1z.
$$
It is represented by the real matrix
$$
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
$$
so it satisfies condition (b), and hence conditions (a) and (c) by step
<1>4.

Its fixed points satisfy
$$
z=-\frac1z,
$$
equivalently
$$
z^2=-1.
$$
Thus its only fixed points are
$$
z=\pm i.
$$
Neither is real, and $\infty$ is not fixed because $T(\infty)=0$.
Consequently there is no
$$
\alpha\in\RR
$$
with $T(\alpha)=\alpha$, so condition (d) fails.
:::

<1>8. The true implication pattern for the four printed conditions is
$$
\boxed{
\text{(d)}
\Longrightarrow
\text{(a)}
\Longleftrightarrow
\text{(b)}
\Longleftrightarrow
\text{(c)},
}
$$
and the implication from (a)--(c) back to (d) need not hold.

::: {.proof}
Step <1>4 proves the three-way equivalence, step <1>6 proves the implication
from (d), and step <1>7 disproves the converse.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the corrected conclusion requested by the repaired problem.
:::
:::

::: {.remark}
Erratum: the source asks to prove that all four printed conditions are
equivalent. This is false. The Möbius transformation
$$
T(z)=-\frac1z
$$
has real coefficients and therefore satisfies (a)--(c), but its fixed-point
equation is $z^2=-1$, so it has no real fixed point and cannot satisfy (d).
The problem above keeps the four source conditions and corrects the requested
implications.
:::
