---
schema: qual/card@1
id: P-JHUFA10CA5
kind: problem
title: Contour integral of meromorphic function
classification:
  areas:
  - complex-analysis
  topics:
  - Residue Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the complete contour and integrand with Fall 2010 problem 5 on PDF page 27."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Replaced the incorrect loop-location claims by exact quadratic root counts; the index at one half is four, and its missing residue changes the answer."
---

Let $\gamma$ be the closed curve in the complex plane that is given in polar coordinates by $r = 2 + 3\cos\theta$, $0 \leq \theta \leq 4\pi$, oriented in the direction of increasing $\theta$.
Let

$$f(z) = \frac{e^z}{2z - 1} + \frac{\sin(2z)}{(z - 2)^2} + \frac{\cos(5z)}{(z + 5i)^3}.$$

Calculate $\int_\gamma f(z) \, dz$.

[Recall that in polar coordinates, $(-r, \theta)$ and $(r, \theta + \pi)$ give the same point in the plane.]

::: solution
<1>1. The winding numbers are determined by three quadratic polynomials.

::: proof
Put $P(w)=3w^2/2+2w+3/2$. For $w=e^{i\theta}$,
$$
P(w)=(2+3\cos\theta)e^{i\theta}=\gamma(\theta).
$$
The parameter $w$ runs twice counterclockwise around $|w|=1$.
Consequently, for a point $a$ off the curve, substitution
in the index integral and the argument principle give
$$
\operatorname{Ind}(\gamma,a)
=2\frac1{2\pi i}\int_{|w|=1}\frac{P'(w)}{P(w)-a}\,dw
=2N_a,
$$
where $N_a$ is the number of zeros of $P-a$ in $|w|<1$,
counted with multiplicity [@SS03].

For $a=1/2$ the two roots are $(-2\pm i\sqrt2)/3$,
of modulus $\sqrt6/3<1$. For $a=2$ the roots are
$(-2\pm\sqrt7)/3$; the plus root has modulus less than
one and the minus root has modulus greater than one,
since $2<\sqrt7<3$. Finally, on $|w|=1$,
$$
|3w^2/2+2w|\leq7/2<\sqrt{109}/2=|3/2+5i|.
$$
Rouché's theorem compares $P+5i$ with the nonzero constant
$3/2+5i$, giving no zeros in the disk [@SS03]. These
calculations also exclude zeros on the unit circle for
all three polynomials. Thus the curve avoids the poles and
$$
\operatorname{Ind}(\gamma,1/2)=4,\qquad
\operatorname{Ind}(\gamma,2)=2,\qquad
\operatorname{Ind}(\gamma,-5i)=0.
$$
:::

<1>2. The indexed residue formula evaluates the integral.

::: proof
The only possible poles of $f$ are $1/2$, $2$, and $-5i$.
At the first two, the residues are
$$
\operatorname{Res}_{1/2}f=e^{1/2}/2,
\qquad \operatorname{Res}_{2}f=(\sin(2z))'|_{z=2}=2\cos4.
$$
The other summands are holomorphic at each respective point.
The third residue is multiplied by index zero, so contributes
nothing. The residue theorem for a closed curve gives
$$
\int_\gamma f(z)\,dz
=2\pi i\left(4\frac{e^{1/2}}2+2\cdot2\cos4\right)
=\boxed{4\pi i e^{1/2}+8\pi i\cos4}
$$
[@SS03]. The use of winding numbers accounts for both
loops and both traversals, without assuming the curve simple.
:::
:::
