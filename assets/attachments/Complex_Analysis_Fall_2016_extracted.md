# Qualifying Exam: Complex Analysis — Fall 2016

Juan B. Gutierrez (Chair), Saar Hersonsky, and Jingzhi Tie

<a id="instructions"></a>
## Instructions

Justify your answers and state clearly any theorem(s) that you are applying. You should not cite examples, exercises, or problems. Cross out the parts you do not want to be graded. Each question has an equal weight–answer them all.

<a id="problems"></a>
## Problems

1. Prove that the map

$$
w=\frac{z-1}{z+1}
$$

- maps the first quadrant in the plane conformally onto the upper, open unit-disk $\Delta ^{+}=\{w=u+iv:u^{2}+v^{2}<1 and v>0\}$ .

1. Is the intersection of $\Delta ^{+}$  with the first quadrant conformally equivalent to the upper half-plane $\{z=x+iy:y>0\}$ ?

2. Let $u(x,y)$  be a harmonic functions defined in an open disk of radius $R>0$ . Suppose that $u(x,y)$  has continuous partial derivatives of order two in its domain.

1. Let two points $(a,b),(x,y)$  in this disk be given. Show that the following integral is independent of the path in this disk joining these points:

$$
v(x,y)=\int_{(a,b)}^{(x,y)}\left(-\frac{\partial u}{\partial y} \, dx+\frac{\partial u}{\partial x} \, dy\right)
$$

1. Prove that $u(x,y)+iv(x,y)$  is an analytic function in this disk.
2. Prove that $v(x,y)$  is harmonic in this disk.

3. Let $f:D\mathbb{\rightarrow C}$  be a continuous function, where $D\mathbb{\subset C}$  is a domain. Let $\alpha :[a,b]\rightarrow D$  be a smooth curve.

1. Define the complex line integral $\int_{\alpha }^{​}f$ .
2. Assume that there exists a constant $M$  such that $|f(\tau )|\leq M$  for all $\tau \in Image(\alpha )$ . Prove that

$$
\left|\int_{\alpha }^{​}f\right|\leq M\times length(\alpha )
$$

3. Let $C_{R}$  be the circle $|z|=R$ , described in the counterclockwise direction, where $R>1$ . Provide an upper bound for $\left|\int_{C_{R}}^{​}\frac{log(z)}{z^{2}}\right|$ , which depends only on $R$  and (possibly) other constants.

1. Let $f\mathbb{:C\rightarrow C}$  be an entire function. Assume the existence of a non-negative integer $m$ , and of positive constants $L$  and $R$ , such that for all $z$  with $|z|>R$  the inequality $|f(z)|\leq L|z|^{m}$ holds. Prove that $f$  is a polynomial of degree $\leq m$ .
2. Let $f\mathbb{:C\rightarrow C}$  be an entire function. Suppose that there exists a real number $M$  such that for all $z\mathbb{\in C}$

$$
Re(f)\leq M
$$

- Prove that $f$  must be a constant.

4. Prove that all the roots of the complex polynomial

$$
z^{7}-5z^{3}+12=0
$$

- lie between the circles $|z|=1$  and $|z|=2$ .

5. Let $\Omega$  be a star-shaped domain of $\mathbb{C}$ . Let $\{f_{n}\}_{n=1}^{\infty }$  be a sequence of injective analytic functions on $\Omega$  that converges uniformly on every compact subset of $\Omega$  to a function $f$ . Prove that:

1. $f$  is analytic on $\Omega$ , and
2. $f$  is either injective or a constant.

6. Evaluate

$$
\int_{0}^{\infty }\frac{sin(t)}{t} \, dt
$$

7. Let $\Delta \subset \mathbb{C}$  denote the open unit-disk.
    1. Prove that for each $\phi \in Aut(\Delta )$  and each $z\in \Delta$ , the following holds:

$$
\frac{\left|\phi ^{'}\left(z\right)\right|}{1-|\phi (z)|^{2}}=\frac{1}{1-|z|^{2}}
$$

2. Let $f:\Delta \rightarrow \Delta$  be an analytic map having two different fixed points, $z_{1},z_{2}\in \Delta$ . Prove that $f(z)=z$  for all $z\in \Delta$ .