---
schema: qual/card@1
id: P-TIE-S15-22
kind: problem
title: Möbius transformations mapping one circle to another with two prescribed points
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 22.
---

::: {.problem}
Let $C$ and $C'$ be two circles and let $z_{1} \in C$, $z_{2} \notin C$, $z_{1}' \in C'$, $z_{2}' \notin C'$. Show that there is a unique fractional linear transformation $f$ with $f(C) = C'$ and $f(z_{1}) = z_{1}'$, $f(z_{2}) = z_{2}'$.
:::

::: {.solution}

::: pf

::: pf-step

There exists a fractional linear transformation
$$
T
$$
such that
$$
T(C)=\RR\cup\{\infty\},
\qquad
T(z_1)=\infty.
$$
Likewise, there exists $T'$ with
$$
T'(C')=\RR\cup\{\infty\},
\qquad
T'(z_1')=\infty.
$$


::: pf-proof

A fractional linear transformation sends generalized circles to generalized circles. First choose any Möbius map sending the ordinary circle $C$ to the unit circle. The image of $z_1$ lies on the unit circle. A disk automorphism can move that boundary point to $1$, and the Cayley transform
$$
\zeta\longmapsto i\frac{1+\zeta}{1-\zeta}
$$
sends the unit circle to $\RR\cup\{\infty\}$ and sends $1$ to $\infty$.
Composing these maps gives $T$. The same construction gives $T'$.

:::

:::

::: {.pf-step #s1-2}

The points
$$
w\coloneqq T(z_2),
\qquad
w'\coloneqq T'(z_2')
$$
are nonreal.


::: pf-proof

Since $z_2\notin C$ and $T$ maps $C$ exactly onto
$$
\RR\cup\{\infty\},
$$
the point $w=T(z_2)$ does not lie on the extended real line. Hence
$$
\operatorname{Im}w\ne0.
$$
The same argument gives
$$
\operatorname{Im}w'\ne0.
$$

:::

:::

::: {.pf-step #s1-3}

There is a unique real affine map
$$
L(\zeta)=a\zeta+b,
\qquad
a,b\in\RR,
\quad
a\ne0,
$$
such that
$$
L(w)=w'.
$$


::: pf-proof

Write
$$
w=x+iy,
\qquad
w'=x'+iy',
$$
with $y,y'\ne0$ by step [](#s1-2){.pf-ref}. The equation
$$
aw+b=w'
$$
with real $a,b$ is equivalent to
$$
ay=y',
\qquad
ax+b=x'.
$$
Thus necessarily
$$
a=\frac{y'}{y}
\ne0,
\qquad
b=x'-ax.
$$
These values are real and give the unique such affine map.

:::

:::

::: {.pf-step #s1-4}

Define
$$
\boxed{
f
\coloneqq
(T')^{-1}\circ L\circ T.
}
$$
Then
$$
f(C)=C',
\qquad
f(z_1)=z_1',
\qquad
f(z_2)=z_2'.
$$


::: pf-proof

Since $L$ has real coefficients and $a\ne0$,
$$
L(\RR\cup\{\infty\})
=
\RR\cup\{\infty\},
$$
and
$$
L(\infty)=\infty.
$$
Therefore
$$
\begin{aligned}
f(C)
&=
(T')^{-1}
\left(
L(T(C))
\right)\\
&=
(T')^{-1}
\left(
\RR\cup\{\infty\}
\right)
=
C'.
\end{aligned}
$$
Also,
$$
f(z_1)
=
(T')^{-1}(L(\infty))
=
(T')^{-1}(\infty)
=
z_1',
$$
and by step [](#s1-3){.pf-ref},
$$
f(z_2)
=
(T')^{-1}(L(w))
=
(T')^{-1}(w')
=
z_2'.
$$
Thus $f$ has all the required properties.

:::

:::

::: {.pf-step #s1-5}

The transformation $f$ is unique.


::: pf-proof

Suppose $f_1$ and $f_2$ both satisfy the required conditions. Set
$$
H
\coloneqq
T'\circ f_2\circ f_1^{-1}\circ (T')^{-1}.
$$
Then $H$ is a fractional linear transformation preserving
$$
\RR\cup\{\infty\},
$$
fixing $\infty$, and fixing the nonreal point
$$
w'=T'(z_2').
$$

Any Möbius transformation preserving the extended real line and fixing $\infty$ has the form
$$
H(\zeta)=a\zeta+b
$$
with $a,b\in\RR$ and $a\ne0$. Since
$$
H(w')=w',
$$
comparison of imaginary parts gives $a=1$, and then comparison of real parts gives $b=0$. Hence
$$
H=\operatorname{id}.
$$
Conjugating back gives
$$
f_1=f_2.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves existence and step [](#s1-5){.pf-ref} proves uniqueness.

:::

:::

:::
