---
schema: qual/card@1
id: P-JHUSP02CAD
kind: problem
title: Even-part Schwarz bound for a normalized disk self-map
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked Spring 2002 Complex Analysis question 4 on PDF page 52. The printed source omits f(0)=0 and does not exclude z=0 from its equality case; both omissions make the literal assertions false."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Factored the even part through z squared, applied Schwarz's lemma, and used circle orthogonality of Taylor coefficients to show that equality at a nonzero point forces all coefficients except the quadratic one to vanish."
---

::: problem
Let $f:\Delta\to\Delta$ be holomorphic and satisfy $f(0)=0$. Prove that
$$
|f(z)+f(-z)|\le 2|z|^2
$$
for every $z\in\Delta$.

If equality holds for some nonzero $z\in\Delta$, prove that
$$
f(z)=e^{i\theta}z^2
$$
for some real $\theta$.
:::

::: remark
As printed, the source omits $f(0)=0$, so the inequality is false at $z=0$;
$f\equiv1/2$ is a counterexample. It also says only "equality holds for some
$z$". After the necessary normalization, equality at $z=0$ is automatic, so
the equality statement must require a nonzero point; $f(z)=z$ otherwise gives
a counterexample to the claimed conclusion.
:::

::: solution
<1>1. The even part factors holomorphically through $z^2$ as a disk map fixing zero.
::: proof
Set
$$
E(z)=\frac{f(z)+f(-z)}2.
$$
The unit disk is convex, and $f(z),f(-z)\in\Delta$, so
$$
|E(z)|\le\frac{|f(z)|+|f(-z)|}{2}<1.
$$
Thus $E:\Delta\to\Delta$ is holomorphic. It is even and, by the normalization,
$E(0)=f(0)=0$.

Write the Taylor series of $E$ at zero as
$$
E(z)=\sum_{n=0}^\infty b_nz^n.
$$
Evenness gives $b_{2m+1}=0$, and $b_0=0$. Hence
$$
E(z)=G(z^2),\qquad
G(w)=\sum_{m=1}^\infty b_{2m}w^m.
$$
The series for $G$ converges for $|w|<1$: if $|w|<1$, choose $z$ with
$z^2=w$, so the corresponding even subseries is absolutely convergent.
Therefore $G$ is holomorphic on $\Delta$, satisfies $G(0)=0$, and obeys
$|G(w)|<1$ because $G(w)=E(z)$ for either square root $z$ of $w$.
Thus $G:\Delta\to\Delta$ is a holomorphic self-map fixing zero.
:::

<1>2. Schwarz's lemma gives the required inequality.
::: proof
Schwarz's lemma applied to $G$ gives
$$
|G(w)|\le|w|\qquad(w\in\Delta).
$$
Putting $w=z^2$ yields
$$
\frac12|f(z)+f(-z)|=|E(z)|=|G(z^2)|\le|z|^2.
$$
Multiplying by two gives the asserted bound.
:::

<1>3. Equality at a nonzero point fixes the entire even part.
::: proof
Suppose equality holds at $z_0\ne0$. Then
$$
|G(z_0^2)|=|z_0^2|,
$$
and $z_0^2\ne0$. The equality case of Schwarz's lemma gives
$$
G(w)=\lambda w
$$
for some $|\lambda|=1$. Therefore
$$
E(z)=\lambda z^2
$$
throughout the disk. If
$$
f(z)=\sum_{n=1}^\infty a_nz^n,
$$
then $E$ is precisely the even part of this Taylor series, so
$$
a_2=\lambda,\qquad a_{2m}=0\quad(m\ne1).
$$
In particular $|a_2|=1$.
:::

<1>4. A disk map with a Taylor coefficient of modulus one at degree two has no other coefficients.
::: proof
For $0<r<1$, orthogonality of the exponentials on the circle gives
$$
\frac1{2\pi}\int_0^{2\pi}|f(re^{it})|^2\,dt
=\sum_{n=1}^\infty |a_n|^2r^{2n}.
$$
The left side is at most one because $f(\Delta)\subset\Delta$. Letting
$r\uparrow1$ and using monotone convergence for the nonnegative series gives
$$
\sum_{n=1}^\infty|a_n|^2\le1.
$$
Step <1>3 gives $|a_2|=1$, so every other coefficient must vanish. Thus
$$
f(z)=a_2z^2=\lambda z^2=e^{i\theta}z^2
$$
for some real $\theta$, which is exactly the corrected equality conclusion.
:::
:::
