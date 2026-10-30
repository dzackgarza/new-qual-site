# Real Analysis Qualifying Exam — August 2017

<a id="real-analysis-qualifying-exam"></a>
## Instructions

Give clear reasoning. State clearly which theorem you are using. You should not cite anything else such as examples, exercises, or problems. Cross out the parts you do not want to be graded. Problems are not in the order of difficulty.

Notation: $m$  and $dx$  denote the Lebesgue measure on the set $\mathbb{R}$  of reals.

<a id="problems"></a>
## Problems

1. Describe the intervals on which the series

$$
\sum_{n=0}^{\infty }\frac{x^{n}}{n!}
$$

- converges uniformly and those on which it does not converge uniformly and prove your assertion.

2. Let $f(x)=x^{2}$ . Let $E$  be a subset in $[0,\infty )$ .

1. Show that $m^{*}(E)=0$  if and only if $m^{*}(f(E))=0$ , where $m^{*}$  is Lebesgue outer measure.
2. Deduce that $E\mapsto f(E)$  is a bijection from the class of Lebesgue measurable sets in $[0,\infty )$  onto itself.

3. Let $S$  be the vector space consisting of complex linear span of characteristic functions of the form $\chi _{(a,b)}$ , where $a,b\mathbb{\in R}$ . Show that for every $f\in L^{1}\mathbb{(R)}$ , there exists a sequence of functions $f_{n}$  in $S$  such that

$$
\lim_{n\to \infty }\parallel f_{n}-f\parallel _{1}=0.
$$

4. Let $f_{n}(x)=nx(1-x)^{n}, \hspace{0.25em} n\mathbb{\in N}$ .

1. Show $f_{n}$  converges to zero pointwise, but not uniformly on $[0,1]$ .

- Hint: Consider the maximum of $f_{n}$ .

2. Show that

$$
\lim_{n\to \infty }\int_{0}^{1}n(1-x)^{n}sinx \, dx=0.
$$

5. Let $\phi (x)$  be a smooth function (i.e. $\phi (x)$  has derivatives of all orders) on $\mathbb{R}$  that vanishes outside some interval $[-N,N]$  and that

$$
\int_{\mathbb{R}}^{​}\phi (x) \, dx=1.
$$

- Let $K_{j}(x):=j\phi (jx)$ . For $f\in L^{1}\mathbb{(R)}$ , define

$$
f*K_{j}(x):=\int_{\mathbb{R}}^{​}f(x-y)K_{j}(y) \, dy.
$$

- Prove the following:

1. Each $f*K_{j}$  is a smooth function and vanishes outside some compact interval.

$$
\lim_{j\to \infty }\parallel f*K_{j}-f\parallel _{1}=0.
$$

- (May use $lim_{y\rightarrow 0}\int_{\mathbb{R}}^{​}|f(x-y)-f(x)| \, dx=0$  without proof.)

6. Let $X$  be a compact metric space and equip the space $C_{\mathbb{R}}(X)$  of continuous functions from $X$  to $\mathbb{R}$  with the maximum norm:

$$
\parallel f\parallel :=max\{|f(x)|:x\in X\}.
$$

- Prove that this norm is complete.