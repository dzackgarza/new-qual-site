---
schema: qual/card@1
id: P-CASP12A
kind: problem
title: "True or False: entire functions with prescribed derivatives, maximum modulus, Picard's theorem, fixed points, and complex structures"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Determine if each statement is true or false.
If false, provide a counterexample.
If true, give a brief proof.

1. If $f$ is an entire function satisfying $f(0) = 1$ and $f'(1/n) = f(1/n)$ for all integers $n \geq 1$, then $f(z) = e^z$ for all $z \in \mathbb{C}$.

2. If $f$ is an entire function satisfying $f(0) = 1$ and $f'(n) = f(n)$ for all integers $n \geq 1$, then $f(z) = e^z$ for all $z \in \mathbb{C}$.

3. If $f$ and $g$ are analytic functions defined on a neighborhood of $|z| \leq 1$, $g \neq 0$ on $|z| \leq 1$, and $|f| \leq |g|$ on $|z| = 1$, then $|f| \leq |g|$ on $|z| \leq 1$.

4. There exists a nonconstant analytic function $f$ on $\mathbb{C}$ such that $\operatorname{ran} f \cap \mathbb{D} = \emptyset$.

5. If $f$ is analytic on a neighborhood of $|z| \leq 1$ and $|f(z)| < 1$ for $|z| \leq 1$, then $f$ when viewed as a mapping of $\overline{\mathbb{D}}$ into $\overline{\mathbb{D}}$ has a unique fixed point.

6. There is no complex structure on $\mathbb{R}^2$ such that the function $f: \mathbb{R}^2 \to \mathbb{C}$ defined by $f(x, y) = x - iy$ is analytic.
:::

::: solution
1. **True.** Put $h=f'-f$. Then $h$ is entire and vanishes at every $1/n$.
Since these zeros accumulate at $0$, the identity theorem gives $h\equiv0$.
Thus $f'=f$, so $(e^{-z}f(z))'=0$ and $f(z)=Ce^z$. From $f(0)=1$,
$C=1$.

2. **False.** Let
\[
f(z)=e^z+\sin(\pi z).
\]
Then $f(0)=1$, and for every positive integer $n$,
\[
f'(n)-f(n)=\pi(-1)^n\ne0,
\]
so this particular perturbation does not work. Instead choose an entire
function $q$ satisfying $q'(n)-q(n)=0$ for all $n$ and $q(0)=0$, for example
\[
q(z)=e^z\sin(2\pi z).
\]
Indeed $q'(n)=2\pi e^n$ while $q(n)=0$, so again not. A correct choice is
obtained by setting $q=e^z h$; then $q'-q=e^zh'$. Taking
$h(z)=1-\cos(2\pi z)$ gives $h(0)=0$ and $h'(n)=0$. Hence
\[
f(z)=e^z\bigl(2-\cos(2\pi z)\bigr)
\]
has $f(0)=1$ and $f'(n)=f(n)$ for every $n$, but $f\ne e^z$.

3. **True.** Since $g$ has no zeros on the closed disk, $f/g$ is analytic on
a neighborhood of it. The maximum modulus principle applied to $f/g$ gives
$|f/g|\le1$ throughout the disk.

4. **False.** If an entire nonconstant $f$ omits the unit disk, then $1/f$ is
an entire bounded function, hence constant by Liouville's theorem. Thus $f$
would be constant.

5. **True.** Existence follows from Brouwer's fixed-point theorem because
$f(\overline{\mathbb D})\subset\mathbb D\subset\overline{\mathbb D}$. If
$a\ne b$ were two fixed points, conjugating by a disk automorphism sending
$a$ to $0$ would produce a disk self-map fixing $0$ and another nonzero point.
The equality case of Schwarz's lemma would make it a disk automorphism. But
$f(\overline{\mathbb D})$ is compactly contained in $\mathbb D$, impossible
for an automorphism. Hence the fixed point is unique.

6. **False.** Give $\mathbb R^2$ the complex structure
\[
J(x,y)=(y,-x),
\]
the negative of the standard one. Then $f(x,y)=x-iy$ is complex-linear from
$(\mathbb R^2,J)$ to the standard complex plane, hence holomorphic.
:::
