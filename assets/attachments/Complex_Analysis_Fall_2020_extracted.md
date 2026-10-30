# Qualifying Exam: Complex Analysis, Fall 2020

<a id="qualifying-exam-complex-analysis"></a>
## Problems

1. Let $n\geq 2$  be an integer. Show that

$$
2^{n-1}\prod_{k=1}^{n-1}sin\frac{k\pi }{n}=n.
$$

- [Hint: Use $n$ -th roots of unity i.e. solutions of $z^{n}-1=0$ ]

2. Expand $\frac{1}{1-z^{2}}+\frac{1}{z-3}$  in a series of the form $\sum_{-\infty }^{\infty }a_{n}z^{n}$  so it converges for

1. $|z|<1$
2. $1<|z|<3$
3. $|z|>3$

3. Let $a\mathbb{\in R}$  with $0<a<3$ . Evaluate

$$
\int_{0}^{\infty }\frac{x^{a-1}}{1+x^{3}} \, dx.
$$

4. Let $\mathbb{D}:=\{z:|z|<1\}$  denote the open unit disk. Suppose that $f(z\mathbb{):D\rightarrow D}$  is holomorphic, and that there exists $a\mathbb{\in D \textbackslash \{}0\}$  such that $f(a)=f(-a)=0$ .

1. Prove that $|f(0)|\leq |a|^{2}$ .
2. What can you conclude when $|f(0)|=|a|^{2}$ ?

5. Consider the function $f(z)=\frac{1}{2}\left(z+\frac{1}{z}\right)$  for $z\mathbb{\in C \textbackslash \{}0\}$ . Let $\mathbb{D}$  denote the open unit disc.

1. Show that $f$  is one-to-one on the punctured disc $\mathbb{D \textbackslash \{}0\}$ . What is the image of the circle $|z|=r$  under this map when $0<r<1$ ?
2. Show that $f$  is one-to-one on the domain $\mathbb{C \textbackslash}\overline{\mathbb{D}}$ . What is the image of this domain under this map?
3. Show that there exists a map $g\mathbb{:C \textbackslash [-}1,1\mathbb{]\rightarrow D \textbackslash \{}0\}$  such that $(g\circ f)(z)=z$  for all $z\mathbb{\in D \textbackslash \{}0\}$ . Describe the map $g$  by an explicit formula.

6. Suppose that $U$  is a bounded, open and simply connected domain in $\mathbb{C}$  and that $f(z)$  is a complex-valued non-constant continuous function on $‾$  whose restriction to $U$  is holomorphic.

1. Prove the maximum modulus principle by showing that if $z_{0}\in U$ , then

$$
\left|f\left(z_{0}\right)\right|<sup\{|f(z)|:z\in \partial U\}.
$$

2. Show furthermore that if $|f(z)|$  is constant on $\partial U$ , then $f(z)$  has a zero in $U$  (i.e., there exists $z_{0}\in U$  for which $f\left(z_{0}\right)=0$ ).

7. Suppose that $f\mathbb{:D\rightarrow D}$  is holomorphic and $f(0)=0$ . Let $n\geq 1$ , and define the function $f_{n}(z)$  to be the $n$ -th composition of $f$  with itself; more precisely, let

$$
f_{1}(z):=f(z), \quad f_{2}(z):=f(f(z)), \quad in general f_{n}(z):=f\left(f_{n-1}(z)\right).
$$

- Suppose that for each $z\mathbb{\in D}$ , $lim_{n\rightarrow \infty }f_{n}(z)$  exists and equals to $g(z)$ . Prove that either $g(z)\equiv 0$  or $g(z)=z$  for all $z\mathbb{\in D}$ .