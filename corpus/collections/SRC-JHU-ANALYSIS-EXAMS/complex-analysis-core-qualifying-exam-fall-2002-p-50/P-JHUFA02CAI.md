---
schema: qual/card@1
id: P-JHUFA02CAI
kind: problem
title: A disk automorphism sending $1/2$ to $-1/\pi$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Disc Automorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the unit-disk source and target, surjectivity requirement and prescribed value f(1/2)=-1/pi with Fall 2002 Complex Analysis problem 4."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Composed two explicit disk automorphisms, verified their disk identities and inverses, checked the denominator, and evaluated the prescribed point."
---

4. (20 points) Let D denote the unit disc $\{ z : | z | < 1 \}$ . Determine a holomorphic mapping f of D onto itself for which $\begin{array} { r } { f ( \frac { 1 } { 2 } ) = - \frac { 1 } { \pi } } \end{array}$


::: solution
Let
$$
\phi(z)=\frac{z-1/2}{1-z/2}
$$
and put $b=-1/\pi$. Define
$$
\boxed{f(z)=\frac{\phi(z)+b}{1+b\phi(z)}
=\frac{\displaystyle\frac{z-1/2}{1-z/2}-1/\pi}
{\displaystyle1-\frac1\pi\frac{z-1/2}{1-z/2}}.}
$$

<1>1. The two factors used in the formula are disk automorphisms.
::: proof
For real $a\in(-1,1)$, the Möbius map
$$
\phi_a(z)=\frac{z-a}{1-az}
$$
satisfies
$$
1-|\phi_a(z)|^2
=\frac{(1-a^2)(1-|z|^2)}{|1-az|^2}>0
\qquad(|z|<1),
$$
and has inverse
$$
\phi_a^{-1}(w)=\frac{w+a}{1+aw}.
$$
Thus $\phi=\phi_{1/2}$ is a biholomorphic map of the disk onto itself and
$\phi(1/2)=0$.

Since $|b|=1/\pi<1$, the map
$$
\psi_b^{-1}(w)=\frac{w+b}{1+bw}
$$
is also a disk automorphism. Its denominator cannot vanish for $|w|<1$ because
$|bw|<1$.
:::

<1>2. Their composition has the required value and is onto.
::: proof
The displayed function is precisely
$$
f=\psi_b^{-1}\circ\phi.
$$
It is therefore holomorphic and bijective from $D$ onto $D$. Moreover,
$$
f(1/2)=\psi_b^{-1}(\phi(1/2))=\psi_b^{-1}(0)=b=-\frac1\pi.
$$
Thus it satisfies every condition in the problem.
:::
:::
