# Complex Analysis Qualifying Exam — Spring 2021

<a id="instructions"></a>
## Instructions

All problems are of equal weight. Please arrange your solutions in numerical order even if you do not solve them in that order. Show work and carefully justify/prove your assertions.

<a id="problems"></a>
## Problems

1. Let $z_{1}$  and $z_{2}$  be two complex numbers.

1. Show that $\left|z_{1}-‾_{1}z_{2}\right|^{2}-\left|z_{1}-z_{2}\right|^{2}=\left(1-\left|z_{1}\right|^{2}\right)\left(1-\left|z_{2}\right|^{2}\right)$ .
2. Show that if $\left|z_{1}\right|<1$  and $\left|z_{2}\right|<1$ , then $\left|\frac{z_{1}-z_{2}}{1-‾_{1}z_{2}}\right|<1$ .
3. Assume that $z_{1}\ne z_{2}$ . Show that $\left|\frac{z_{1}-z_{2}}{1-‾_{1}z_{2}}\right|=1$  if and only if $\left|z_{1}\right|=1$  or $\left|z_{2}\right|=1$ .

2. Evaluate the integral $\int_{-\infty }^{\infty }\frac{e^{i\xi x}}{cosh(x)} \, dx$  where $cosh(x)=\frac{e^{x}+e^{-x}}{2}$  and $\xi$  is real.

- Hint: Use an appropriate rectangular contour containing $[-R,R]$  as one side.

3. Suppose $f(z)$  is entire and there exist $A,R>0$  and a natural number $N$  such that

$$
|f(z)|\geq A|z|^{N} \quad for |z|\geq R
$$

- Show that

1. $f$  is a polynomial, and
2. the degree of $f$  is at least $N$ .

4. Let $f(z)=u+iv$  be an entire function such that $u(x,y)=Re(f(x+iy))$  is a polynomial in $x,y$ . Show that $f(z)$  is a polynomial in $z$ .
5. Let $f(z)$  be a holomorphic map of the open unit disk $\mathbb{D}$  into itself. Show that for any two points $z$  and $w$  in $\mathbb{D}$ ,

$$
\left|\frac{f(w)-f(z)}{1-\overline{f(w)} \, f(z)}\right|\leq \left|\frac{w-z}{1-‾z}\right|
$$

- and the inequality is strict for $z\ne w$  except when $f$  is a linear fractional transformation mapping the unit disk into itself.

6. Suppose $\{f_{n}(z)\}_{n=1}^{\infty }$  is a sequence of holomorphic functions on the unit disk $\mathbb{D}$ , and $f(z)$  is a holomorphic function on the unit disk $\mathbb{D}$ . Show that the following are equivalent.

1. $\{f_{n}(z)\}$  converges to $f(z)$  uniformly on compact subsets in $\mathbb{D}$ .
2. $\int_{|z|=r}^{​}\left|f_{n}(z)-f(z)\right| \, |dz|$  converges to $0$  if $0<r<1$ .

7. Let $R$  be the intersection of the right half plane and the outside of the circle $\left|z-\frac{1}{2}\right|=\frac{1}{2}$  with the line segment $[1,2]$  removed, i.e.

$$
R=\left\{z\mathfrak{:R}z>0 and \left|z-\frac{1}{2}\right|>\frac{1}{2}\right\} \textbackslash \{z=x+iy:1\leq x\leq 2 and y=0\}
$$

- Find a conformal map from $R$  to the upper half plane.