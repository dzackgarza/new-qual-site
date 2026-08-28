---
schema: qual/card@1
id: E-SS8.EX-7
kind: exercise
title: "Provide all the details in the proof of the formula for the solution of the Diri"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
---

::: exercise
7. Provide all the details in the proof of the formula for the solution of the Dirichlet problem in a strip discussed in Section 1.3. Recall that it sufices to compute the solution at the points $z = i y$ with $0 < y < 1$

(a) Show that if $r e ^ { i \theta } = G ( i y )$ , then

$$
r e ^ {i \theta} = i \frac {\cos \pi y}{1 + \sin \pi y}.
$$

This leads to two separate cases: either $0 < y \le 1 / 2$ and $\theta = \pi / 2$ , or $1 / 2 \leq$

$y < 1$ and $\theta = - \pi / 2$ . In either case, show that

$$
r ^ {2} = \frac {1 - \sin \pi y}{1 + \sin \pi y} \quad \mathrm{and} \quad P _ {r} (\theta - \varphi) = \frac {\sin \pi y}{1 - \cos \pi y \sin \varphi}.
$$

(b) In the integral $\begin{array} { r } { \frac { 1 } { 2 \pi } \int _ { 0 } ^ { \pi } P _ { r } ( \theta - \varphi ) \tilde { f } _ { 0 } ( \varphi ) d \varphi } \end{array}$ make the change of variables $t =$ $F ( e ^ { i \varphi } )$ . Observe that

$$
e ^ {i \varphi} = \frac {i - e ^ {\pi t}}{i + e ^ {\pi t}},
$$

and then take the imaginary part and diferentiate both sides to establish the two identities

$$
\sin \varphi = \frac {1}{\cosh \pi t} \quad \mathrm{and} \quad \frac {d \varphi}{d t} = \frac {\pi}{\cosh \pi t}.
$$

Hence deduce that

$$
\begin{array}{r} \frac {1}{2 \pi} \int_ {0} ^ {\pi} P _ {r} (\theta - \varphi) \tilde {f} _ {0} (\varphi) d \varphi = \frac {1}{2 \pi} \int_ {0} ^ {\pi} \frac {\sin \pi y}{1 - \cos \pi y \sin \varphi} \tilde {f} _ {0} (\varphi) d \varphi \\ = \frac {\sin \pi y}{2} \int_ {- \infty} ^ {\infty} \frac {f _ {0} (t)}{\cosh \pi t - \cos \pi y} d t. \end{array}
$$

(c) Use a similar argument to prove the formula for the integra $\begin{array} { r } { \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { 0 } P _ { r } ( \theta - \varphi ) \tilde { f } _ { 1 } ( \varphi ) d \varphi . } \end{array}$
:::
