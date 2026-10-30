# Real Analysis Qualifying Examination — Spring 2015

The six problems on this exam have equal weighting. To receive full credit give complete justification for all assertions by either citing known theorems or giving arguments from first principles.

<a id="problems"></a>
## Problems

1. Let $(X,d)$  and $(Y,\rho )$  be metric spaces, $f:X\rightarrow Y$  and $x_{0}\in X$ . Prove that the following two statements are equivalent:

1. For every $\varepsilon >0$ , there exists a $\delta >0$  such that $\rho (f(x),f(x_{0}))<\varepsilon$  whenever $d(x,x_{0})<\delta$ .
2. The sequence $\{f(x_{n})\}_{n=1}^{\infty }$  converges to $f(x_{0})$  for every sequence $\{x_{n}\}_{n=1}^{\infty }$  in $X$  which converges to $x_{0}$ .

2. Let $f\mathbb{:R\rightarrow C}$  be a continuous and periodic function with period $1$ . Prove that

$$
\lim_{N\to \infty }\frac{1}{N}\sum_{n=1}^{N}f(n\alpha )=\int_{0}^{1}f(t) \, dt
$$

- for every irrational real number $\alpha$ . Hint: Do it first for the functions $f(t)=e^{2\pi ikt}$ , with $k\mathbb{\in Z}$ .

3. Let $\mu$  be a finite Borel measure on $\mathbb{R}^{n}$  and $E$  be a Borel subset of $\mathbb{R}^{n}$ . Prove that the following two statements are equivalent:

1. For any $\varepsilon >0$ , there exists an open set $G$  and closed set $F$  such that $F\subseteq E\subseteq G$  and $\mu (G\smallsetminus F)<\varepsilon$ .
2. There exists an $G_{\delta }$  set $V$  and a $F_{\sigma }$  set $H$  such that $H\subseteq E\subseteq V$  and $\mu (V\smallsetminus H)=0$ .

4. Carefully prove that if we define

$$
f(x,y):=\left\{\begin{matrix}\frac{x^{1/3}}{(1+xy)^{3/2}}&if 0\leq x\leq y,\\0&otherwise\end{matrix}\right.
$$

- for each $(x,y)\in \mathbb{R}^{2}$ , then $f$  defines a function in $L^{1}(\mathbb{R}^{2})$ .

5. Let $H$  be a Hilbert space.

1. Let $x\in H$  and $\{u_{1},\ldots ,u_{N}\}$  be an orthonormal set in $H$ . Prove that the best approximation to $x$  in $H$  by an element of the form $\sum_{n=1}^{N}c_{n}u_{n}$ , with $c_{1},\ldots ,c_{N}\mathbb{\in C}$ , is given when $c_{n}=\langle x,u_{n}\rangle$ .
2. Conclude from part (a), or otherwise, that finite dimensional subspaces of $H$  are always closed.

6. Let $f\in L^{1}\mathbb{(R)}$  and $g$  be a bounded measurable function on $\mathbb{R}$ . Recall that the convolution of $f$  and $g$  is the function $f*g$  defined by

$$
f*g(x)=\int_{\mathbb{R}}^{​}f(x-y)g(y) \, dy
$$

- for all $x$  such that the integral exists.

1. Prove that the convolution $f*g$  is well-defined, bounded, and uniformly continuous on $\mathbb{R}$ .
2. Prove that if one makes the further assumption that $g\in C^{1}\mathbb{(R)}$  with bounded derivative, then the convolution $f*g$  will also be in $C^{1}\mathbb{(R)}$  and

$$
\frac{d}{dx}(f*g)=f*\left(\frac{d}{dx}g\right)
$$

- Recall that $C^{1}\mathbb{(R)}$  denotes the space of functions on $\mathbb{R}$  which are continuously differentiable.