---
schema: qual/card@1
id: E-USHMH
kind: problem
title: Product of sines $\sin(k\pi/n)$ via roots of unity
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.exercise}
Use $n$th roots of unity to show that $2^{n-1}\sin\frac{\pi}{n}\sin\frac{2\pi}{n}\cdots\sin\frac{(n-1)\pi}{n}=n$.

1. Let $f$ be continuous on
   \[
   D=\{z:|z|>R,\ 0\le\arg z\le\theta\},\qquad 0\le\theta\le2\pi,
   \]
   and suppose $zf(z)\to k$ as $z\to\infty$ in $D$. If $L_{R'}$ is the
   part of $|z|=R'$ lying in $D$, show that
   \[
   \lim_{R'\to\infty}\int_{L_{R'}}f(z)\,dz=i\theta k.
   \]

2. Let $f(z)=\sum_{n=0}^\infty c_nz^n$ be analytic and one-to-one on
   $\DD$. For $0<r_0<1$, let $\overline D_{r_0}=\{|z|\le r_0\}$. Show that
   the area of $f(\overline D_{r_0})$ is finite and equals
   \[
   \pi\sum_{n=1}^\infty n|c_n|^2r_0^{2n}.
   \]

3. Prove the parallelogram identity
   \[
   |z_1+z_2|^2+|z_1-z_2|^2=2(|z_1|^2+|z_2|^2),
   \]
   and explain its geometric meaning.

4. Find the Laurent expansions of
   \[
   f(z)=\frac{z+1}{z(z-1)}
   \]
   about $z=0$ and $z=1$ in the punctured disks determined by the other
   singularity.

5. Prove that on $|z|=1$:
   (a) $\sum_{n\ge1}nz^n$ diverges everywhere;
   (b) $\sum_{n\ge1}z^n/n^2$ converges everywhere;
   (c) $\sum_{n\ge1}z^n/n$ converges everywhere except at $z=1$.

6. Let $\gamma$ be a positively oriented piecewise smooth simple closed curve
   with interior $\Omega_1$ and exterior $\Omega_2$. Suppose $f$ is
   holomorphic on an open set containing $\gamma\cup\Omega_2$ and
   $f(z)\to A$ as $z\to\infty$. Prove
   \[
   \frac1{2\pi i}\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi
   =\begin{cases}
   A,&z\in\Omega_1,\\
   -f(z)+A,&z\in\Omega_2.
   \end{cases}
   \]

7. Let $D$ contain the closed unit disk in its interior, and let $f$ be
   analytic in $D$ except for finitely many simple poles $z_1,\dots,z_k$ on
   $|z|=1$, with residues $s_1,\dots,s_k$. If
   \[
   f(z)=\sum_{n=0}^\infty a_nz^n\qquad(|z|<1),
   \]
   prove that there is $M>0$ such that $|a_n|\le M$ for all $n$.

8. Let $f:[0,\infty)\to\RR$ be continuous, differentiable on
   $(0,\infty)$, satisfy $f(0)=0$, and suppose $f'$ is increasing. For
   $x>0$ define $g(x)=f(x)/x$. Prove that $g$ is increasing.

9. Prove or disprove: there is a sequence of analytic polynomials $p_n$ such
   that $p_n(z)\to\bar z$ uniformly for $z\in\partial\DD$.

10. For $R>0$, show that there is $N_R$ such that for $n>N_R$,
    \[
    P_n(z)=1+z+\frac{z^2}{2!}+\cdots+\frac{z^n}{n!}\ne0
    \qquad(|z|\le R).
    \]

11. Let $f$ be analytic on $\DD$, with $f(0)=f'(0)=0$. Show that
    \[
    g(z)=\sum_{n=1}^\infty f(z/n)
    \]
    defines an analytic function on $\DD$. Moreover, prove that
    \[
    g(z)=f(z)\sum_{n=1}^\infty\frac1{n^2}
    \]
    for all $z\in\DD$ if and only if $f(z)=cz^2$ for some constant $c$.
:::

::: {.solution}
Let $\zeta=e^{2\pi i/n}$. From
\[
z^n-1=(z-1)\prod_{k=1}^{n-1}(z-\zeta^k)
\]
we obtain, after dividing by $z-1$ and setting $z=1$,
\[
n=\prod_{k=1}^{n-1}(1-\zeta^k).
\]
Taking absolute values gives
\[
n=\prod_{k=1}^{n-1}|1-e^{2\pi i k/n}|.
\]
For real $\theta$,
\[
|1-e^{i\theta}|=2\left|\sin\frac\theta2\right|.
\]
Since $0<k\pi/n<\pi$ for $1\le k\le n-1$, all these sines are positive.
Therefore
\[
n=\prod_{k=1}^{n-1}2\sin\frac{k\pi}{n}
=2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n},
\]
as required.

**1. Sector arc.** Parametrize the arc by $z=R'e^{it}$,
$0\le t\le\theta$. Then
\[
\int_{L_{R'}}f(z)\,dz
=i\int_0^\theta R'e^{it}f(R'e^{it})\,dt.
\]
The hypothesis $zf(z)\to k$ as $z\to\infty$ in the region means that the
integrand converges uniformly in $t\in[0,\theta]$ to $k$. Therefore
\[
\boxed{\lim_{R'\to\infty}\int_{L_{R'}}f(z)\,dz=i\theta k}.
\]

**2. Area of a univalent image.** Since $f$ is holomorphic, its real
Jacobian is $|f'(z)|^2$. Injectivity means the change-of-variables formula has
multiplicity one, so
\[
\operatorname{Area}(f(D_{r_0}))
=\int_{|z|<r_0}|f'(z)|^2\,dA(z).
\]
The derivative is bounded on the compact disk $|z|\le r_0$, so this area is
finite. Since
\[
f'(z)=\sum_{n=1}^\infty nc_nz^{n-1},
\]
orthogonality of $e^{in\theta}$ on circles gives
\[
\int_0^{2\pi}|f'(re^{i\theta})|^2\,d\theta
=2\pi\sum_{n=1}^\infty n^2|c_n|^2r^{2n-2}.
\]
Integrating $r\,dr$ from $0$ to $r_0$ yields
\[
\boxed{\operatorname{Area}(f(D_{r_0}))
=\pi\sum_{n=1}^\infty n|c_n|^2r_0^{2n}}.
\]

**3. Parallelogram law.** Expanding with complex conjugates,
\[
|z_1+z_2|^2+|z_1-z_2|^2
=2|z_1|^2+2|z_2|^2.
\]
Geometrically, if $z_1,z_2$ are adjacent side vectors of a parallelogram,
$z_1\pm z_2$ are its diagonal vectors; the identity says that the sum of the
squares of the diagonal lengths equals the sum of the squares of the four
side lengths.

**4. Laurent expansions at $0$ and $1$.** Partial fractions give
\[
\frac{z+1}{z(z-1)}=-\frac1z+\frac2{z-1}.
\]
Thus for $0<|z|<1$,
\[
\boxed{f(z)=-\frac1z-2\sum_{n=0}^\infty z^n}.
\]
Writing $w=z-1$, we have
\[
f(z)=\frac2w-\frac1{1+w},
\]
so for $0<|z-1|<1$,
\[
\boxed{f(z)=\frac2{z-1}-\sum_{n=0}^\infty(-1)^n(z-1)^n}.
\]

**5. Boundary power series.** For $|z|=1$, the terms of
$\sum nz^n$ have modulus $n$, so they do not tend to zero; hence the series
diverges everywhere. The series $\sum z^n/n^2$ converges absolutely because
$\sum1/n^2<\infty$. Finally, at $z=1$, $\sum z^n/n$ is the divergent harmonic
series. If $|z|=1$ and $z\ne1$, the partial sums of $\sum_{n=1}^N z^n$ are
\[
\frac{z(1-z^N)}{1-z},
\]
and are uniformly bounded in $N$; since $1/n\searrow0$, Dirichlet's test
gives convergence.

**6. Exterior Cauchy formula.** Put $h=f-A$, so $h(z)\to0$ at infinity.
Choose a large circle $C_R$ containing $\gamma$ and the point $z$ when
$z\in\Omega_2$. Since $h(\xi)/(\xi-z)=o(1/R)$ uniformly on $C_R$,
\[
\int_{C_R}\frac{h(\xi)}{\xi-z}\,d\xi\to0.
\]
If $z\in\Omega_1$, the integrand is holomorphic in the annulus between
$\gamma$ and $C_R$, hence
\[
\int_{C_R}\frac{h(\xi)}{\xi-z}\,d\xi
-\int_\gamma\frac{h(\xi)}{\xi-z}\,d\xi=0,
\]
and the second integral is therefore zero. If $z\in\Omega_2$, the same annulus
contains the simple pole at $\xi=z$, so
\[
\int_{C_R}\frac{h(\xi)}{\xi-z}\,d\xi
-\int_\gamma\frac{h(\xi)}{\xi-z}\,d\xi
=2\pi i h(z).
\]
Letting $R\to\infty$ gives
$(2\pi i)^{-1}\int_\gamma h/(\xi-z)=0$ in $\Omega_1$ and $-h(z)$ in
$\Omega_2$. Adding the constant term $A$, whose Cauchy integral is $A$ in
$\Omega_1$ and $0$ in $\Omega_2$, gives the claimed formula.

**7. Bounded Taylor coefficients.** Define
\[
H(z)=f(z)-\sum_{j=1}^k\frac{s_j}{z-z_j}.
\]
The simple poles are removed, so $H$ is holomorphic on a neighborhood of the
closed unit disk. Hence there is $\rho>1$ such that $H(z)=\sum b_nz^n$ on
$|z|<\rho$, and Cauchy's estimates give $|b_n|\le C\rho^{-n}$ for some $C$.
For $|z|<1$ and $|z_j|=1$,
\[
\frac{s_j}{z-z_j}
=-\sum_{n=0}^\infty\frac{s_j}{z_j^{n+1}}z^n.
\]
Thus
\[
a_n=b_n-\sum_{j=1}^k\frac{s_j}{z_j^{n+1}},
\]
and therefore
\[
|a_n|\le C+\sum_{j=1}^k|s_j|.
\]
This constant is independent of $n$.

**8. Monotonicity of $f(x)/x$.** Let $0<x<y$. By the mean value theorem
there are $\xi\in(0,x)$ and $\eta\in(x,y)$ such that
\[
\frac{f(x)-f(0)}x=f'(\xi),
\qquad
\frac{f(y)-f(x)}{y-x}=f'(\eta).
\]
Since $f'$ is increasing, the second slope is at least the first. Using
$f(0)=0$,
\[
f(y)\ge f(x)+(y-x)\frac{f(x)}x
=y\frac{f(x)}x,
\]
so $f(y)/y\ge f(x)/x$.

**9. Polynomial approximation to $\bar z$ on the circle.** Such a sequence
does not exist. On $|z|=1$, $\bar z=1/z$. If $p_n\to\bar z$ uniformly there,
then
\[
zp_n(z)\to1
\]
uniformly on $|z|=1$. By the maximum modulus principle applied to
$zp_n(z)-1$, the convergence would be uniform on the whole closed disk. But
at $z=0$ every term equals $-1$, a contradiction.

**10. Exponential partial sums.** The polynomials $P_n$ converge uniformly to
$e^z$ on every closed disk. On $|z|\le R$,
\[
|e^z|=e^{\Re z}\ge e^{-R}.
\]
Choose $N_R$ so that
\[
\sup_{|z|\le R}|P_n(z)-e^z|<e^{-R}/2
\qquad(n>N_R).
\]
Then $|P_n(z)|\ge e^{-R}/2>0$ on the disk, as required.

**11. The series $\sum f(z/n)$.** Since $f(0)=f'(0)=0$, the function
$F(z)=f(z)/z^2$ extends holomorphically across $0$. On every compact disk
$|z|\le r<1$, let $M_r=\max_{|w|\le r}|F(w)|$. Then
\[
|f(z/n)|\le M_r\frac{|z|^2}{n^2},
\]
so the series defining $g$ converges uniformly on compact subsets by the
$M$-test and hence defines a holomorphic function.

Write
\[
f(z)=\sum_{m=2}^\infty a_mz^m.
\]
Normal convergence permits summing coefficientwise:
\[
g(z)=\sum_{m=2}^\infty a_m\zeta(m)z^m,
\qquad
\zeta(m)=\sum_{n=1}^\infty n^{-m}.
\]
Thus $g=\zeta(2)f$ exactly when
\[
a_m(\zeta(m)-\zeta(2))=0
\qquad(m\ge2).
\]
For every $m>2$, $\zeta(m)<\zeta(2)$, so $a_m=0$. Hence
$f(z)=a_2z^2$. Conversely, for $f(z)=cz^2$ one has
$g(z)=cz^2\sum n^{-2}=\zeta(2)f(z)$.
:::
