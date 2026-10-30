# Real Analysis Qualifying Examination, Spring 2020

<a id="real-analysis-qualifying-examination"></a>
## Instructions

The six problems on this exam have equal weighting. To receive full credit give complete justification for all assertions by either citing known theorems or giving arguments from first principles.

<a id="problems"></a>
## Problems

1. Prove that if $f:[0,1\mathbb{]\rightarrow R}$  is continuous, then

$$
\lim_{k\to \infty }\int_{0}^{1}kx^{k-1}f(x) \, dx=f(1).
$$

2. Let $m_{*}$  denote Lebesgue outer measure on $\mathbb{R}$ .

1. Prove that for every $E\mathbb{\subseteq R}$  there exists a Borel set $B$  containing $E$  with the property that

$$
m_{*}(B)=m_{*}(E).
$$

2. Prove that if $E\mathbb{\subseteq R}$  has the property that $m_{*}(A)=m_{*}(A\cap E)+m_{*}(A\cap E^{c})$  for every set $A\mathbb{\subseteq R}$ , then there exists a Borel set $B\mathbb{\subseteq R}$  such that $E=B \textbackslash N$  with $m_{*}(N)=0$ .

- Make sure you address the case when $m_{*}(E)=\infty$ .

1. Prove that if $f\in L^{1}\mathbb{(R)}$ , then

$$
\lim_{N\to \infty }\int_{|x|\geq N}^{​}|f(x)| \, dx=0,
$$

- and demonstrate that it is not necessarily the case that $f(x)\rightarrow 0$  as $|x|\rightarrow \infty$ .

2. Prove that if $f\in L^{1}([1,\infty ))$  and decreasing, then $lim_{x\rightarrow \infty }f(x)=0$  and in fact $lim_{x\rightarrow \infty }xf(x)=0$ .
3. If $f:[1,\infty )\rightarrow [0,\infty )$  is decreasing with $lim_{x\rightarrow \infty }xf(x)=0$ , does this ensure $f\in L^{1}([1,\infty ))$ ?

3. Let $f\in L^{1}\mathbb{(R)}$  and $g\in L^{1}\mathbb{(R)}$ . Argue that $H(x,y)=f(y)g(x-y)$  defines a function in $L^{1}(\mathbb{R}^{2})$  and deduce from this that

$$
f*g(x)=\int_{\mathbb{R}}^{​}f(y)g(x-y) \, dy
$$

- defines a function in $L^{1}\mathbb{(R)}$  that satisfies

$$
\parallel f*g\parallel _{1}\leq \parallel f\parallel _{1}\parallel g\parallel _{1}.
$$

4. Compute the following limit and justify your calculations:

$$
\lim_{n\to \infty }\int_{0}^{n}\left(1+\frac{x^{2}}{n}\right)^{-(n+1)} \, dx.
$$

1. Show that $L^{2}([0,1])\subseteq L^{1}([0,1])$  and $\mathscr{l}^{1}\mathbb{(Z)\subseteq}\mathscr{l}^{2}\mathbb{(Z)}$ .
2. For $f\in L^{1}([0,1])$  define

$$
\hat{f}(n):=\int_{0}^{1}f(x)e^{-2\pi inx} \, dx
$$

- Prove that if $f\in L^{1}([0,1])$  and $\{\hat{f}(n)\}\in \mathscr{l}^{1}\mathbb{(Z)}$ , then

$$
S_{N}f(x)=\sum_{|n|\leq N}^{​}\hat{f}(n)e^{2\pi inx}
$$

- converges uniformly on $[0,1]$  to a continuous function $g$  that equals $f$  almost everywhere.
- Hint: One possible approach is to argue that if $f\in L^{1}([0,1])$  with $\{\hat{f}(n)\}\in \mathscr{l}^{1}\mathbb{(Z)}$ , then $f\in L^{2}([0,1])$ .