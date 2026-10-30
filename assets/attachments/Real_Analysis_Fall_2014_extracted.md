# Real Analysis Qualifying Examination, Fall 2014

<a id="real-analysis-qualifying-examination"></a>
## Instructions

The six problems on this exam have equal weighting.

<a id="problems"></a>
## Problems

1. Let $\left\{f_{n}\right\}_{n=1}^{\infty }$  be a sequence of continuous functions on $\mathbb{R}$  for which the series $\sum_{n=1}^{\infty }f_{n}$  converges uniformly. Prove that the sum function $f:=\sum_{n=1}^{\infty }f_{n}$  is also continuous.
2. Let $I$  be an index set and $a:I\rightarrow (0,\infty )$ .

1. Show that if

$$
\sum_{i\in I}^{​}a(i):=\underset{J\subset I, \hspace{0.33em} J \hspace{0.25em} finite}{sup}\sum_{i\in J}^{​}a(i)<\infty ,
$$

- then $I$  is countable.

2. Suppose $I\mathbb{=Q}$ , and that $\sum_{q\mathbb{\in Q}}^{​}a(q)<\infty$ . Show that the function $f$ , defined for all $x\mathbb{\in R}$  by

$$
f(x):=\sum_{q\mathbb{\in Q,} \, q\leq x}^{​}a(q),
$$

- is continuous at $x$  if and only if $x\mathbb{\notin Q}$ .

3. Let $f$  be a Lebesgue integrable function on $\mathbb{R}$ . Prove that for every $\varepsilon >0$  there exists $\delta >0$  such that

$$
\int_{E}^{​}|f(x)| \, dx<\varepsilon
$$

- whenever $m(E)<\delta$ .

4. Let $g\in L^{\infty }([0,1])$ . Prove that if

$$
\int_{[0,1]}^{​}f(x)g(x) \, dx=0
$$

- for all continuous functions $f$  on $[0,1]$ , then $g(x)=0$  almost everywhere.

1. Show that if $f$  is continuous with compact support on $\mathbb{R}^{n}$ , then

$$
\lim_{t\to 0}\int_{\mathbb{R}^{n}}^{​}|f(x+t)-f(x)| \, dx=0
$$

2. Extend the result above to functions in $L^{1}(\mathbb{R}^{n})$  and use this extension to prove that if $f\in L^{1}(\mathbb{R}^{n})$  and $g\in L^{\infty }(\mathbb{R}^{n})$ , then

$$
f*g(x)=\int_{\mathbb{R}^{n}}^{​}f(x-y)g(y) \, dy
$$

- is both bounded and uniformly continuous.

5. Let $1\leq p,q\leq \infty$  be conjugate exponents, i.e. $\frac{1}{p}+\frac{1}{q}=1$ . Prove that if $f\in L^{p}(\mathbb{R}^{n})$ , then

$$
\parallel f\parallel _{p}=\underset{\parallel g\parallel _{q}=1}{sup}\left|\int f(x)g(x) \, dx\right|.
$$